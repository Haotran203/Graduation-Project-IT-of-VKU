# app/data_ingestion/web_scraper.py

import feedparser
import logging
from typing import List, Dict

logger = logging.getLogger(__name__)


class WebScraper:
    def fetch_rss(self, url: str) -> List[Dict]:
        """Thu thập từ RSS feed."""
        articles = []

        try:
            feed = feedparser.parse(url)
            logger.info(f"Fetching RSS from {url}")

            for entry in feed.entries[:20]:
                articles.append({
                    "title": entry.get("title", ""),
                    "text": entry.get("summary", ""),
                    "url": entry.get("link", ""),
                    "source": "rss"
                })

            logger.info(f"[OK] Fetched {len(articles)} articles from RSS")

        except Exception as e:
            logger.error(f"Error fetching RSS {url}: {e}")

        return articles
