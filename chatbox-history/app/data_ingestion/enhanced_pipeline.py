# app/data_ingestion/enhanced_pipeline.py

import logging
import sys
import time
from datetime import datetime
from typing import Dict, List
import uuid

from qdrant_client.models import PointStruct

from app.config.settings import settings
from app.data_ingestion.auto_crawler import AutoCrawler
from app.data_ingestion.data_processor import DataProcessor
from app.data_ingestion.sources.historical_sources import SEED_HISTORICAL_ARTICLES
from app.data_ingestion.sources.tourism_sources import DYNAMIC_SOURCES
from app.data_ingestion.web_scraper import WebScraper
from app.data_ingestion.wikipedia_scraper import WikipediaScraper
from app.db.qdrant_client import get_client, init_collection

# --- Cấu hình logging ---
if sys.platform == 'win32':
    import codecs

    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.StreamHandler(sys.stdout)])
logger = logging.getLogger(__name__)


class EnhancedIngestionPipeline:
    def __init__(self):
        logger.info("=" * 80)
        logger.info("INITIALIZING ENHANCED INGESTION PIPELINE")
        logger.info("=" * 80)
        start_time = time.time()

        self.wiki_scraper = WikipediaScraper()
        self.web_scraper = WebScraper()
        self.processor = DataProcessor()
        self.qdrant = get_client()
        init_collection()

        logger.info(f"[DONE] Pipeline initialized in {time.time() - start_time:.2f} seconds")
        dedup_stats = self.processor.dedup.get_stats()
        logger.info(f"[DEDUP] Tracking {dedup_stats['total_tracked_titles']} existing titles")
        logger.info("=" * 80)

        self.stats = {
            "total_articles_processed": 0, "total_articles_skipped": 0,
            "total_chunks_created": 0, "total_chunks_saved": 0, "errors": 0,
            "start_time": datetime.now()
        }

    def ingest_phase_1_historical_foundation(self, limit_articles: int = None, auto_discover: bool = True,
                                             max_per_category: int = 50):
        """Phase 1: Ingest critical historical knowledge."""
        logger.info("\n" + "=" * 80 + "\n[PHASE 1] HISTORICAL FOUNDATION\n" + "=" * 80)
        phase_start = time.time()

        # Step 1: Seed articles
        logger.info("\n>>> STEP 1.1: CRITICAL SEED ARTICLES")
        seed_to_process = SEED_HISTORICAL_ARTICLES[:limit_articles] if limit_articles else SEED_HISTORICAL_ARTICLES
        self.ingest_wikipedia(seed_to_process)

        # Step 2: Auto-discover
        if auto_discover:
            logger.info("\n>>> STEP 1.2: AUTO-DISCOVERING NEW ARTICLES (SMART MODE)")
            auto_crawler = AutoCrawler()

            # ✨ THAY ĐỔI QUAN TRỌNG: Truyền "trí nhớ" vào crawler
            new_articles = auto_crawler.discover_new_articles(
                max_per_category=max_per_category,
                known_titles=self.processor.dedup.ingested_titles
            )

            if new_articles:
                logger.info(f"[OK] Discovered {len(new_articles)} new articles to ingest.")
                # Không cần áp dụng limit ở đây nữa vì crawler đã kiểm soát số lượng
                self.ingest_wikipedia(new_articles)
            else:
                logger.info("[INFO] No new articles discovered.")

        logger.info(f"\n[DONE] PHASE 1 COMPLETED in {time.time() - phase_start:.2f} seconds")
        self._print_stats()

    def ingest_rss_feeds(self):
        logger.info("\n" + "=" * 80 + "\n[PHASE 2] RSS FEED INGESTION\n" + "=" * 80)
        phase_start = time.time()

        rss_sources = DYNAMIC_SOURCES.get("rss_feeds", {}).get("sources", [])
        if not rss_sources:
            logger.warning("No RSS sources found.")
            return

        for rss_url in rss_sources:
            try:
                articles_from_rss = self.web_scraper.fetch_rss(rss_url)
                if articles_from_rss:
                    self.ingest_articles(articles_from_rss, source_name=f"RSS ({rss_url})")
            except Exception as e:
                logger.error(f"  [FATAL] Failed to process RSS feed {rss_url}: {e}")
                self.stats["errors"] += 1

        logger.info(f"\n[DONE] PHASE 2 (RSS) COMPLETED in {time.time() - phase_start:.2f} seconds")
        self._print_stats()

    def ingest_articles(self, articles: List[Dict], source_name: str = "articles"):
        if not articles: return
        logger.info(f"\n[PROCESS] Processing {len(articles)} {source_name}...")

        for idx, article in enumerate(articles, 1):
            try:
                logger.info(f"\n   [{idx}/{len(articles)}] Processing: {article.get('title', 'Unknown')}")
                chunks = self.processor.process_article(article)

                if not chunks:
                    self.stats["total_articles_skipped"] += 1
                    continue

                logger.info(f"      Created {len(chunks)} chunks")
                self.stats["total_articles_processed"] += 1
                self.stats["total_chunks_created"] += len(chunks)
                self._save_to_qdrant(chunks)
            except Exception as e:
                logger.error(f"      [ERROR] Processing article '{article.get('title')}': {e}")
                self.stats["errors"] += 1

    def ingest_wikipedia(self, topics: List[str]):
        if not topics: return
        articles = self.wiki_scraper.fetch_articles(topics)
        self.ingest_articles(articles, source_name="Wikipedia articles")

    def _save_to_qdrant(self, chunks: List[Dict]):
        if not chunks: return
        points = [
            PointStruct(
                id=str(chunk.get("id", uuid.uuid4())),
                vector=chunk["vector"],
                payload={
                    "text": chunk["text"], "title": chunk["title"], "url": chunk["url"],
                    "source": chunk["source"], "chunk_id": chunk.get("chunk_id", 0),
                    "content_hash": chunk.get("content_hash", ""),
                    "ingestion_date": datetime.utcnow().isoformat(),
                    "group_id": "PUBLIC", "tenancy": "PUBLIC",
                    "is_shared": True, "message_type": "knowledge",
                }
            ) for chunk in chunks
        ]
        try:
            self.qdrant.upsert(collection_name=settings.COLLECTION_NAME, points=points)
            self.stats["total_chunks_saved"] += len(points)
        except Exception as e:
            logger.error(f"      [ERROR] Qdrant upsert failed: {e}")
            self.stats["errors"] += 1

    def _print_stats(self):
        elapsed = (datetime.now() - self.stats["start_time"]).total_seconds()
        logger.info("\n[STATS] INGESTION STATISTICS (CUMULATIVE):")
        logger.info(f"   Articles processed: {self.stats['total_articles_processed']}")
        logger.info(f"   Articles skipped (duplicate): {self.stats['total_articles_skipped']}")
        logger.info(f"   Chunks created: {self.stats['total_chunks_created']}")
        logger.info(f"   Chunks saved: {self.stats['total_chunks_saved']}")
        logger.info(f"   Errors: {self.stats['errors']}")
        logger.info(f"   Total time: {elapsed:.2f} seconds")
