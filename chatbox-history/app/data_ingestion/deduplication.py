# app/data_ingestion/deduplication.py

import hashlib
import logging
from typing import Set, Dict
from app.db.qdrant_client import get_client
from app.config.settings import settings

logger = logging.getLogger(__name__)


class DeduplicationManager:
    """Quản lý deduplication cho data ingestion."""

    def __init__(self):
        self.qdrant = get_client()
        self.ingested_titles: Set[str] = set()
        self.ingested_hashes: Set[str] = set()
        self._load_existing_data()

    def _load_existing_data(self):
        """Load danh sách titles và hashes đã có trong Qdrant."""
        try:
            logger.info("Loading existing data from Qdrant for deduplication...")

            offset = None
            total_loaded = 0

            while True:
                result = self.qdrant.scroll(
                    collection_name=settings.COLLECTION_NAME,
                    limit=100,
                    offset=offset,
                    with_payload=True,
                    with_vectors=False
                )

                points, next_offset = result

                if not points:
                    break

                for point in points:
                    payload = point.payload

                    title = payload.get("title")
                    if title:
                        self.ingested_titles.add(title)

                    content_hash = payload.get("content_hash")
                    if content_hash:
                        self.ingested_hashes.add(content_hash)

                    total_loaded += 1

                offset = next_offset
                if offset is None:
                    break

            logger.info(f"[OK] Loaded {total_loaded} existing records")
            logger.info(f"  - Unique titles: {len(self.ingested_titles)}")
            logger.info(f"  - Unique hashes: {len(self.ingested_hashes)}")

        except Exception as e:
            logger.warning(f"Could not load existing data: {e}")
            logger.info("Starting with empty deduplication cache")

    @staticmethod
    def generate_content_hash(text: str, title: str) -> str:
        """Tạo hash duy nhất cho content."""
        content = f"{title}::{text[:500]}"
        return hashlib.sha256(content.encode('utf-8')).hexdigest()

    def is_duplicate(self, article: Dict) -> bool:
        """Kiểm tra xem article có bị duplicate không."""
        title = article.get("title", "")
        text = article.get("text", "")

        # Check 1: By title
        if title in self.ingested_titles:
            logger.debug(f"  [DUPLICATE] Title exists: {title}")
            return True

        # Check 2: By content hash
        content_hash = self.generate_content_hash(text, title)
        if content_hash in self.ingested_hashes:
            logger.debug(f"  [DUPLICATE] Content hash exists: {title}")
            return True

        return False

    def mark_as_ingested(self, article: Dict):
        """Đánh dấu article đã được ingest."""
        title = article.get("title", "")
        text = article.get("text", "")

        self.ingested_titles.add(title)

        content_hash = self.generate_content_hash(text, title)
        self.ingested_hashes.add(content_hash)

    def get_stats(self) -> Dict:
        """Lấy thống kê deduplication."""
        return {
            "total_tracked_titles": len(self.ingested_titles),
            "total_tracked_hashes": len(self.ingested_hashes)
        }
