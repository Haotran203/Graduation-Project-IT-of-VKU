# app/routes/ask.py

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

        # --- SCORE FILTERING + CONTEXT ASSEMBLE ---
        candidate_docs = []
        for d in docs:
            payload = d.get("payload", {})
            text = payload.get("text") or payload.get("answer") or ""
            if text and len(text) > 30:
                candidate_docs.append(d)
                title = payload.get("title")
                if not title or title.strip() == "":
                    text_preview = (payload.get("answer") or payload.get("text") or "").strip()
                    title = (text_preview[:50].replace("\n", " ") + "...") if text_preview else "Untitled"
                logger.debug("✓ Doc '%s' (%.2f)", title, d.get("score", 0))

        # --- SELECT MODE (RAG vs Fallback) ---
        use_rag = len(candidate_docs) > 0
        mode = "rag" if use_rag else "web_fallback"
        logger.info(f"[MODE] Selected: {mode.upper()}")

        # ======================================================
        # ✅ OPTIMIZED: BUILD UNIFIED PROMPT
        # ======================================================
        conv_context = build_conversation_history_text(history[-3:]) if history else ""

        # ✅ ONE PROMPT THAT DOES EVERYTHING
        prompt_for_llm = build_unified_prompt(
            user_question=rewritten_query,
            conversation_context=conv_context,
            documents=candidate_docs if use_rag else [],
            role=req.tenancy,
            enable_web_search=req.deepResearch,
            original_docs_available=use_rag
        )

        logger.info(f"[LLM] Calling provider (mode={mode}, role={req.tenancy})")
        logger.debug(f"[PROMPT] Length: {len(prompt_for_llm)} chars")

        # ✅ ONLY 1 CALL TO PROVIDER
        gresp = generator.generate(
            prompt=prompt_for_llm,
            enable_web_search=req.deepResearch and not use_rag
        )

        answer = gresp.get("answer", "")
        detected_language = gresp.get("language", "vi")  # Provider should return language

        logger.info("[LLM] Generation completed")

        # --- Fallback caching ---
        if mode == "web_fallback" and len(answer) > 50:
            logger.info("[CACHE] Storing web fallback answer into Qdrant")
            save_fallback_answer_to_qdrant(rewritten_query, answer, embedder)

        # ✅ Extract coordinates from response
        all_coordinates = extract_all_coordinates(answer)
        if all_coordinates:
            logger.info(f"[COORDINATES] Extracted {len(all_coordinates)} locations")
            answer = add_coordinates_to_answer(answer, all_coordinates)
        else:
            logger.debug(f"[COORDINATES] No coordinates found")

        # --- PREPARE SOURCES OUTPUT ---
        top_sources = []
        for d in candidate_docs[:5]:
            payload = d.get("payload", {})
            title = ((payload.get("title")
                      or (payload.get("answer") or "")[:50].replace("\n", " "))
                     or "Không rõ tiêu đề")
            snippet = (payload.get("answer") or "")[:200].replace("\n", " ")
            top_sources.append(
                SourceOut(
                    title=title,
                    url=payload.get("url"),
                    score=d.get("score"),
                    id=d.get("id"),
                    answer_snippet=snippet
                )
            )

        if not top_sources:
            top_sources = [
                SourceOut(
                    title=f"Web Search via {gresp.get('model_used', 'sonar-pro')}",
                    url=None,
                    score=1.0,
                    id="web-fallback",
                    answer_snippet=answer[:200]
                )
            ]

        # ======================================================
        # ✅ SAVE TO ALL STORAGE LAYERS
        # ======================================================

        # 1. Save to PostgreSQL (long-term persistence)
        # ✅ Auto-creates conversation if not exists
        try:
            conversation_repo.save_turn(
                conversation_id=conversation_id,  # user_id = conversation_id
                user_query=original_query,
                assistant_answer=answer,
                sources=[s.dict() for s in top_sources]
            )
            logger.info(f"[POSTGRESQL] ✓ Saved turn to conversation: {conversation_id}")
        except Exception as e:
            logger.error(f"[POSTGRESQL] ✗ Failed to save turn: {e}")

        # 2. Save to in-memory store (fast session cache)
        conversation_store.save_turn(req.user_id, conv_id, original_query, answer)

        # 3. Save to Qdrant (vector search)
        save_message(
            user_id=req.user_id,
            tenancy=req.tenancy,
            prompt=original_query,
            answer=answer,
            vector=query_vector,
            sources=[s.dict() for s in top_sources]
        )

        logger.info(
            f"[COMPLETE] user={req.user_id}, conversation={conversation_id}, language={detected_language}, role={req.tenancy}, mode={mode}, coords={len(all_coordinates)}")

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
