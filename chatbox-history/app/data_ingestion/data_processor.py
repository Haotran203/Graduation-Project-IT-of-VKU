# app/data_ingestion/data_processor.py

import re
import logging
import hashlib
import uuid
from typing import List, Dict
from sentence_transformers import SentenceTransformer
from app.data_ingestion.deduplication import DeduplicationManager
from app.utils.chunking import chunk_text_semantic

logger = logging.getLogger(__name__)


class DataProcessor:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        logger.info("Loading embedding model...")
        self.embedder = SentenceTransformer(model_name)
        logger.info("[OK] Model loaded")

        self.dedup = DeduplicationManager()

    def clean_text(self, text: str) -> str:
        """Làm sạch văn bản."""
        text = re.sub(r'\s+', ' ', text)
        return text.strip()

    def chunk_text(self, text: str, chunk_size: int = 512, overlap: int = 50) -> List[str]:
        """Chia văn bản thành chunks theo ngữ nghĩa."""
        chunks = chunk_text_semantic(text, max_chunk_size=chunk_size, min_chunk_size=100)
        return [chunk['text'] for chunk in chunks]

    def process_article(self, article: Dict) -> List[Dict]:
        """
        Process article: clean, chunk, embed.
        ✅ Thêm fields cho backend: group_id, tenancy, is_shared
        """
        if self.dedup.is_duplicate(article):
            logger.info(f"  [SKIP] Duplicate article: {article.get('title', 'Unknown')}")
            return []

        text = article.get("text", "")
        cleaned = self.clean_text(text)
        chunk_objs = chunk_text_semantic(cleaned, max_chunk_size=512, min_chunk_size=100)

        content_hash = self.dedup.generate_content_hash(text, article.get("title", ""))

        processed = []
        for idx, chunk_obj in enumerate(chunk_objs):
            chunk = chunk_obj["text"]
            vector = self.embedder.encode(chunk).tolist()

            # ✅ NEW: Add backend fields
            processed.append({
                "id": str(uuid.uuid4()),
                "text": chunk,
                "title": article.get("title", ""),
                "url": article.get("url", ""),
                "source": article.get("source", ""),
                "chunk_id": idx,
                "vector": vector,
                "content_hash": content_hash,

                # ✅ Backend fields
                "group_id": "PUBLIC",  # Shared to all users
                "tenancy": "PUBLIC",  # For all roles
                "is_shared": True,  # Mark as shared knowledge
                "message_type": "knowledge",
            })

        if processed:
            self.dedup.mark_as_ingested(article)

        return processed
