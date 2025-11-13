import hashlib
import uuid
import logging
from datetime import datetime
from typing import List, Optional, Dict, Any

from qdrant_client import QdrantClient
from qdrant_client.models import (
    VectorParams, Distance, PointStruct, Filter,
    FieldCondition, MatchValue
)

from app.config.settings import settings

logger = logging.getLogger(__name__)

# Global client instance
client = None


def get_client() -> QdrantClient:
    """Get or create Qdrant client instance."""
    global client
    if client is None:
        client = QdrantClient(
            url=settings.QDRANT_URL,
            api_key=settings.QDRANT_API_KEY,
            timeout=30
        )
        logger.info(f"Connected to Qdrant at {settings.QDRANT_URL}")
    return client


def init_collection():
    """Initialize collection if not exists."""
    try:
        qdrant = get_client()
        collections = qdrant.get_collections().collections
        collection_names = [col.name for col in collections]

        if settings.COLLECTION_NAME not in collection_names:
            qdrant.create_collection(
                collection_name=settings.COLLECTION_NAME,
                vectors_config=VectorParams(
                    size=settings.VECTOR_SIZE,
                    distance=Distance.COSINE
                )
            )
            logger.info(f"[OK] Created collection: {settings.COLLECTION_NAME}")
        else:
            logger.info(f"[OK] Collection already exists: {settings.COLLECTION_NAME}")

        # Create indexes
        try:
            qdrant.create_payload_index(
                collection_name=settings.COLLECTION_NAME,
                field_name="tenancy",
                field_schema="keyword",
            )
        except:
            pass

        try:
            qdrant.create_payload_index(
                collection_name=settings.COLLECTION_NAME,
                field_name="group_id",
                field_schema="keyword",
            )
        except:
            pass

        try:
            qdrant.create_payload_index(
                collection_name=settings.COLLECTION_NAME,
                field_name="is_shared",
                field_schema="keyword",
            )
        except:
            pass

    except Exception as e:
        logger.error(f"Error initializing collection: {e}")
        raise


def search_similar(
        user_id: str,
        tenancy: str,
        query_vector: List[float],
        limit: int = 6,
) -> List[dict]:
    """
    Dense search with multi-source support.
    ✅ Search personal data (user's conversations)
    ✅ Search shared knowledge (crawler data marked as PUBLIC)
    """
    try:
        qdrant = get_client()

        logger.info(f"[SEARCH_SIMILAR] user={user_id}, tenancy={tenancy}, limit={limit}")

        # ✅ Filter 1: Personal data (user's own conversations)
        personal_filter = Filter(
            must=[
                FieldCondition(key="group_id", match=MatchValue(value=user_id)),
                FieldCondition(key="tenancy", match=MatchValue(value=tenancy)),
            ]
        )

        personal_results = qdrant.search(
            collection_name=settings.COLLECTION_NAME,
            query_vector=query_vector,
            query_filter=personal_filter,
            limit=limit // 2,
            with_payload=True,
        )

        logger.info(f"[SEARCH] Personal results: {len(personal_results)}")

        # ✅ Filter 2: Shared knowledge (PUBLIC - for all users)
        shared_filter = Filter(
            must=[
                FieldCondition(key="group_id", match=MatchValue(value="PUBLIC")),
            ]
        )

        shared_results = qdrant.search(
            collection_name=settings.COLLECTION_NAME,
            query_vector=query_vector,
            query_filter=shared_filter,
            limit=limit // 2,
            with_payload=True,
        )

        logger.info(f"[SEARCH] Shared results: {len(shared_results)}")

        # Merge and deduplicate
        all_results = (
                [{"id": r.id, "score": r.score * 1.1, "payload": r.payload} for r in personal_results] +
                [{"id": r.id, "score": r.score, "payload": r.payload} for r in shared_results]
        )

        # Remove duplicates by ID, keep highest score
        seen = {}
        for result in all_results:
            doc_id = result["id"]
            if doc_id not in seen or result["score"] > seen[doc_id]["score"]:
                seen[doc_id] = result

        unique_results = sorted(seen.values(), key=lambda x: x["score"], reverse=True)[:limit]

        return unique_results

    except Exception as e:
        logger.error(f"[SEARCH_SIMILAR] Error for user={user_id}, tenancy={tenancy}: {e}")
        return []

