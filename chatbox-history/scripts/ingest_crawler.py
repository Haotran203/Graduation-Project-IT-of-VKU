# scripts/ingest_crawler.py

import sys
import argparse
import logging
import os
from pathlib import Path
from datetime import datetime

# ✅ FIX: Add parent directory to path
PROJECT_ROOT = Path(__file__).parent.parent.absolute()
sys.path.insert(0, str(PROJECT_ROOT))

# ✅ FIX: Set PYTHONPATH
os.environ['PYTHONPATH'] = str(PROJECT_ROOT)

print(f"[DEBUG] Project root: {PROJECT_ROOT}")
print(f"[DEBUG] Python path: {sys.path[0]}")

# Now import app modules
try:
    from app.data_ingestion.enhanced_pipeline import EnhancedIngestionPipeline
    from app.data_ingestion.auto_crawler import AutoCrawler
    from app.data_ingestion.wikipedia_scraper import WikipediaScraper
    from app.data_ingestion.data_processor import DataProcessor
    from app.db.qdrant_client import get_client, init_collection
    from app.config.settings import settings
    from qdrant_client.models import PointStruct
    import uuid

    print("[OK] All imports successful ✅")
except ImportError as e:
    print(f"[ERROR] Import failed: {e}")
    print(f"[ERROR] Make sure you're running from project root:")
    print(f"[ERROR] cd {PROJECT_ROOT}")
    print(f"[ERROR] python scripts/ingest_crawler.py")
    sys.exit(1)

# Setup logging
log_dir = PROJECT_ROOT / "logs"
log_dir.mkdir(exist_ok=True)

log_file = log_dir / f"ingest_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(log_file, encoding='utf-8')
    ]
)

logger = logging.getLogger(__name__)


def run_ingestion(
        seed_limit: int = None,
        auto_discover_limit: int = None,
        max_per_category: int = 50,
        only_seed: bool = False,
):
    """Run ingestion pipeline."""

    logger.info("=" * 80)
    logger.info("INGESTION PIPELINE")
    logger.info("=" * 80)
    logger.info(f"Parameters:")
    logger.info(f"  - Seed limit: {seed_limit or 'ALL'}")
    logger.info(f"  - Auto-discover limit: {auto_discover_limit or 'ALL'}")
    logger.info(f"  - Max per category: {max_per_category}")
    logger.info(f"  - Only seed: {only_seed}")
    logger.info("=" * 80)

    try:
        # Step 1: Initialize
        logger.info("[STEP 1/4] Initializing...")
        pipeline = EnhancedIngestionPipeline()
        logger.info("[OK] Pipeline ready")

        # Step 2: Ingest seed articles
        logger.info("[STEP 2/4] Processing seed articles...")
        from app.data_ingestion.sources.historical_sources import SEED_HISTORICAL_ARTICLES

        seed_articles = SEED_HISTORICAL_ARTICLES
        if seed_limit:
            seed_articles = seed_articles[:seed_limit]
            logger.info(f"Limited to {len(seed_articles)} seed articles")

        pipeline.ingest_wikipedia(seed_articles)
        logger.info(f"[OK] Seed articles completed")

        # Step 3: Auto-discover
        if not only_seed:
            logger.info("[STEP 3/4] Auto-discovering new articles...")
            crawler = AutoCrawler()
            new_articles = crawler.discover_new_articles(max_per_category=max_per_category)

            if not new_articles:
                logger.warning("❌ No new articles discovered")
            else:
                logger.info(f"✅ Found {len(new_articles)} new articles")

                articles_to_ingest = new_articles
                if auto_discover_limit:
                    articles_to_ingest = new_articles[:auto_discover_limit]
                    logger.info(f"Limited to {len(articles_to_ingest)} auto-discover articles")

                pipeline.ingest_wikipedia(articles_to_ingest)
                crawler.mark_as_crawled(articles_to_ingest)
                logger.info(f"[OK] Auto-discovery completed")
        else:
            logger.info("[STEP 3/4] Skipped (--only-seed flag)")

        # Step 4: Final stats
        logger.info("[STEP 4/4] Final statistics...")
        total_count = get_client().count(collection_name=settings.COLLECTION_NAME)

        logger.info("=" * 80)
        logger.info("INGESTION COMPLETED ✅")
        logger.info("=" * 80)
        logger.info(f"Total documents in Qdrant: {total_count.count}")
        logger.info(f"Log file: {log_file}")
        logger.info("=" * 80)

        return True

    except Exception as e:
        logger.exception(f"❌ ERROR: {e}")
        logger.info("=" * 80)
        return False


def main():
    parser = argparse.ArgumentParser(
        description='Crawler Ingestion Script',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
EXAMPLES:
  python scripts/ingest_crawler.py
  python scripts/ingest_crawler.py --only-seed
  python scripts/ingest_crawler.py --seed-limit 5
  python scripts/ingest_crawler.py --auto-discover-limit 20 --max-per-category 100
        """
    )

    parser.add_argument(
        '--seed-limit',
        type=int,
        default=None,
        help='Limit seed articles to N (default: ALL)'
    )

    parser.add_argument(
        '--auto-discover-limit',
        type=int,
        default=None,
        help='Limit auto-discover articles to N (default: ALL)'
    )

    parser.add_argument(
        '--max-per-category',
        type=int,
        default=50,
        help='Max articles per category for auto-discovery (default: 50)'
    )

    parser.add_argument(
        '--only-seed',
        action='store_true',
        help='Only ingest seed articles, skip auto-discovery'
    )

    args = parser.parse_args()

    # Run ingestion
    success = run_ingestion(
        seed_limit=args.seed_limit,
        auto_discover_limit=args.auto_discover_limit,
        max_per_category=args.max_per_category,
        only_seed=args.only_seed,
    )

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
