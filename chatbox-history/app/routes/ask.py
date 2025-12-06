from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, List
import uuid
import logging
from datetime import datetime
import json
import re

from app.services.factory import get_embedder, get_generator
from app.db.qdrant_client import search_similar_hybrid, save_message, get_client
from app.db.conversation_store import conversation_store
from app.db.conversation_repository import conversation_repo  # ← Import repository
from app.utils.context import (
    build_unified_prompt,
    extract_all_coordinates,
    add_coordinates_to_answer
)
from app.utils.conversation import (
    rewrite_query_with_context,
    build_conversation_history_text,
    should_use_conversation_context
)
from app.config import settings

# ======================================================
# CONFIG
# ======================================================
logger = logging.getLogger(__name__)
router = APIRouter()


def save_fallback_answer_to_qdrant(query: str, answer: str, embedder):
    """Lưu câu trả lời fallback vào Qdrant."""
    try:
        from qdrant_client.models import PointStruct
        import hashlib

        vector = embedder.embed_text(answer)
        content_hash = hashlib.sha256(f"{query}::{answer[:300]}".encode("utf-8")).hexdigest()

        payload = {
            "text": answer,
            "title": f"WebAnswer: {query[:60]}...",
            "url": None,
            "source": "web_fallback",
            "original_query": query,
            "content_hash": content_hash,
            "ingestion_date": datetime.utcnow().isoformat(),
            "content_type": "web_fallback",
            "chunk_id": 0,
            "keywords": query.lower().split()[:10],
        }

        client = get_client()
        point = PointStruct(id=str(uuid.uuid4()), vector=vector, payload=payload)
        client.upsert(collection_name=settings.COLLECTION_NAME, points=[point])

        logger.info(f"[QDRANT UPDATE] ✓ Saved web fallback response")
    except Exception as e:
        logger.warning(f"[QDRANT UPDATE] ✗ Could not save fallback answer: {e}")


# ==================== PYDANTIC SCHEMAS ====================

class AskRequest(BaseModel):
    prompt: str = Field(..., description="Câu hỏi người dùng gửi lên")
    model: str = Field(..., description="model AI generator")
    deepResearch: bool = Field(..., description="deep research")
    user_id: str = Field("default", description="Mã định danh người dùng (= conversation_id)")
    tenancy: str = Field(..., description="Nhóm người dùng: traveler | student | researcher | enthusiast")
    history_limit: Optional[int] = Field(5, ge=0, le=20, description="Number of history messages")
    top_k: Optional[int] = Field(5, description="Số lượng tài liệu liên quan tối đa")
    use_keyword: Optional[bool] = Field(True, description="Dùng hybrid search (keyword + vector)")


class SourceOut(BaseModel):
    title: Optional[str]
    url: Optional[str]
    score: Optional[float]
    id: Optional[str]
    answer_snippet: Optional[str]


class AskResponse(BaseModel):
    prompt: str
    answer: str
    sources: List[SourceOut]
    conversation_id: str
    mode: str
    language: Optional[str] = None
    rewritten_query: Optional[str] = None


# ======================================================
# MAIN ENDPOINT
# ======================================================
@router.post("/", response_model=AskResponse)
async def ask(req: AskRequest):
    """
    ✅ OPTIMIZED: 1 lần gọi provider, tất cả logic trong 1 prompt.

    Flow:
    1. Backend builds unified prompt
    2. Send 1 request to provider
    3. Provider detects language, generates answer, includes coordinates
    4. Backend extracts coordinates

    ✅ Storage Strategy:
    - user_id = conversation_id (1 user = 1 conversation)
    - PostgreSQL: Long-term persistence
    - In-memory: Fast session cache
    - Qdrant: Vector search
    """
    try:
        # --- INIT CORE SERVICES ---
        embedder = get_embedder()
        generator = get_generator(req.model)

        # ✅ In this context: user_id = conversation_id
        conversation_id = req.user_id
        conv_id = f"{req.user_id}-memory-session"  # For in-memory compatibility

        # ======================================================
        # ✅ GET HISTORY FROM POSTGRESQL
        # ======================================================
        try:
            # Get from PostgreSQL (using user_id as conversation_id)
            pg_messages = conversation_repo.get_recent_messages(
                conversation_id=conversation_id,  # ← user_id = conversation_id
                limit=req.history_limit or 5
            )

            # Convert PostgreSQL format to memory store format for compatibility
            # PostgreSQL: [{"role": "user", "content": "..."}, {"role": "assistant", "content": "..."}]
            # Memory: [{"user": "...", "assistant": "...", "timestamp": "..."}]
            history = []
            for i in range(0, len(pg_messages), 2):
                if i + 1 < len(pg_messages):
                    user_msg = pg_messages[i]
                    assistant_msg = pg_messages[i + 1]

                    if user_msg.get("role") == "user" and assistant_msg.get("role") == "assistant":
                        history.append({
                            "user": user_msg.get("content", ""),
                            "assistant": assistant_msg.get("content", ""),
                            "timestamp": user_msg.get("created_at", "")
                        })

            logger.info(f"[CONTEXT] Retrieved {len(history)} turns from PostgreSQL (user={req.user_id})")

        except Exception as e:
            # If conversation doesn't exist yet, history is empty (will be created on save)
            logger.info(f"[CONTEXT] No history found in PostgreSQL (new user/conversation): {e}")
            history = []

        # --- QUERY REWRITE ---
        original_query = req.prompt
        rewritten_query = (
            rewrite_query_with_context(original_query, history, generator)
            if should_use_conversation_context(original_query)
            else original_query
        )
        if rewritten_query != original_query:
            logger.info(f"[QUERY] Rewrite: '{original_query}' -> '{rewritten_query}'")

        # --- EMBEDDING ---
        query_vector = embedder.embed_text(rewritten_query)
        logger.info(f"[EMBED] Vector generated")

        # --- SEARCH RAG SOURCES ---
        if req.use_keyword:
            docs = search_similar_hybrid(
                user_id=req.user_id,
                tenancy=req.tenancy,
                query_vector=query_vector,
                query_text=rewritten_query,
                limit=req.top_k or settings.MAX_CONTEXT_DOCS,
            )
            logger.info(f"[SEARCH] Hybrid search returned {len(docs)} results")
        else:
            logger.info("[SEARCH] Dense only (vector search)")
            from app.db.qdrant_client import search_similar
            docs = search_similar(
                user_id=req.user_id,
                tenancy=req.tenancy,
                query_vector=query_vector,
                limit=req.top_k or settings.MAX_CONTEXT_DOCS,
            )

        # --- FALLBACK WIKI/NON-LOCAL SEARCH ---
        if len(docs) < 2:
            logger.info("[FALLBACK] Using external Wikipedia-based retrieval")
            from app.services.external_search import get_external_docs
            external_docs = await get_external_docs(rewritten_query, embedder)
            for d in external_docs:
                d["payload"]["source"] = "external"
            docs.extend(external_docs)

        logger.info(f"[DOCS] Total candidate docs = {len(docs)}")

        # --- FINAL RETURN ---
        return AskResponse(
            prompt=original_query,
            answer=answer,
            sources=top_sources,
            conversation_id=conversation_id,  # Return user_id (since user_id = conversation_id)
            mode=mode,
            language=detected_language,
            rewritten_query=None if rewritten_query == original_query else rewritten_query
        )

    except Exception as e:
        logger.exception(f"[ERROR] /ask failed: {e}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
