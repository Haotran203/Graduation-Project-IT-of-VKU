# app/services/external_search.py
import httpx
import logging

logger = logging.getLogger(__name__)

async def get_external_docs(query: str, embedder):
    """
    Wikipedia fallback retrieval — gọi API Wikipedia để lấy tài liệu bên ngoài
    khi nguồn nội bộ (Qdrant) không đủ dữ liệu.
    """
    try:
        async with httpx.AsyncClient() as client:
            resp = await client.get(
                "https://en.wikipedia.org/w/api.php",
                params={
                    "action": "query",
                    "list": "search",
                    "srsearch": query,
                    "utf8": 1,
                    "format": "json"
                }
            )

        data = resp.json().get("query", {}).get("search", [])
        docs = []

        for entry in data[:3]:
            text = entry.get("snippet", "").replace("<span>", "").replace("</span>", "")
            vector = embedder.embed_text(text)
            docs.append({
                "payload": {
                    "title": entry["title"],
                    "url": f"https://en.wikipedia.org/wiki/{entry['title'].replace(' ', '_')}",
                    "text": text,
                    "source": "wikipedia"
                },
                "score": 0.5
            })

        logger.info(f"[EXTERNAL_SEARCH] Retrieved {len(docs)} Wiki docs for query: {query[:50]}...")
        return docs

    except Exception as e:
        logger.error(f"[EXTERNAL_SEARCH] Error retrieving external docs: {e}")
        return []
