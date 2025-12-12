from qdrant_client.models import PointStruct
from app.config.settings import settings
import logging
from app.db.qdrant_client import get_client

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def normalize_title(text: str) -> str:
    if text:
        return text[:100].replace("\n", " ") + "..."
    return "Không rõ tiêu đề"

def batch_update_title_source():
    qdrant = get_client()

    batch_size = 100
    offset = None
    total_updated = 0

    while True:
        points, offset = qdrant.scroll(
            collection_name=settings.COLLECTION_NAME,
            limit=batch_size,
            offset=offset,
            with_payload=True,
            with_vectors=True
        )

        if not points:
            break

        points_to_update = []

        for point in points:
            payload = point.payload or {}

            title = payload.get("title")
            source = payload.get("source")
            text = payload.get("text", "")

            # Kiểm tra title và source
            need_update = False

            if not title or title.strip() == "":
                payload["title"] = normalize_title(text)
                need_update = True

            if not source or source.strip() == "":
                payload["source"] = "unknown"
                need_update = True

            if need_update:
                updated_point = PointStruct(
                    id=point.id,
                    payload=payload,
                    vector=point.vector  # giữ nguyên vector
                )
                points_to_update.append(updated_point)

        if points_to_update:
            qdrant.upsert(
                collection_name=settings.COLLECTION_NAME,
                points=points_to_update
            )
            total_updated += len(points_to_update)
            logger.info(f"Updated {len(points_to_update)} points at offset {offset}")

        if offset is None:
            break

    logger.info(f"Batch update complete. Total points updated: {total_updated}")


if __name__ == "__main__":
    batch_update_title_source()
