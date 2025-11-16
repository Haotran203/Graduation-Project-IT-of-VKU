# -*- coding: utf-8 -*-


# manual_expand.py

"""
Manual Knowledge Base Expansion Script

Usage:
    python manual_expand.py
    python manual_expand.py --limit 50
    python manual_expand.py --no-auto-discover
"""
import argparse
import sys
import logging
from datetime import datetime

# Add project root to path
sys.path.insert(0, '.')

from app.data_ingestion.enhanced_pipeline import EnhancedIngestionPipeline
from app.db.qdrant_client import get_client
from app.config.settings import settings

# Logging setup
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(
            f'manual_expand_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log',
            encoding='utf-8'
        )
    ]
)
logger = logging.getLogger(__name__)



def get_current_count():
    """Get current vector count from Qdrant."""
    try:
        client = get_client()
        result = client.count(collection_name=settings.COLLECTION_NAME)
        return result.count
    except Exception as e:
        logger.error(f"Error getting count: {e}")
        return 0

def main():
    parser = argparse.ArgumentParser(
        description='Manual Knowledge Base Expansion',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Chạy full historical ingestion (seed + auto-discover)
  python manual_expand.py

  # Chỉ chạy fetch RSS feeds
  python manual_expand.py --fetch-rss

  # Chạy cả historical và RSS
  python manual_expand.py --max-per-category 100 --fetch-rss
        """
    )

    parser.add_argument(
        '--limit', type=int, default=None,
        help='Limit number of articles to process (default: all)'
    )
    parser.add_argument(
        '--no-auto-discover', action='store_true',
        help='Skip auto-discovery phase (process seed articles only)'
    )
    parser.add_argument(
        '--max-per-category', type=int, default=50,
        help='Max articles to auto-discover per category (default: 50)'
    )
    # --- Thêm cờ mới ---
    parser.add_argument(
        '--fetch-rss', action='store_true',
        help='Fetch new articles from RSS feeds defined in sources.'
    )

    args = parser.parse_args()

    # --- In thông tin ---
    print("=" * 80)
    logger.info("MANUAL KNOWLEDGE BASE EXPANSION")
    print("=" * 80)

    run_historical = not (args.fetch_rss and not args.limit and args.no_auto_discover is False)

    if run_historical:
        logger.info("Historical Ingestion: ENABLED")
    if args.fetch_rss:
        logger.info("RSS Fetching: ENABLED")

    logger.info(f"Start time: {datetime.now()}")
    initial_count = get_current_count()
    logger.info(f"Initial vectors in Qdrant: {initial_count}")
    print("=" * 80)

    try:
        pipeline = EnhancedIngestionPipeline()

        # --- Giai đoạn 1: Historical ---
        if run_historical:
             pipeline.ingest_phase_1_historical_foundation(
                 limit_articles=args.limit,
                 auto_discover=not args.no_auto_discover,
                 max_per_category=args.max_per_category
             )

        # --- Giai đoạn 2: RSS Feeds ---
        if args.fetch_rss:
            pipeline.ingest_rss_feeds()

        # --- In tóm tắt ---
        final_count = get_current_count()
        actual_added = final_count - initial_count

        print("\n" + "=" * 80)
        logger.info("EXPANSION SUMMARY")
        print("=" * 80)
        logger.info(f"Initial vectors: {initial_count}")
        logger.info(f"Final vectors: {final_count}")
        logger.info(f"New vectors added: {actual_added}")
        logger.info(f"Articles processed: {pipeline.stats['total_articles_processed']}")
        logger.info(f"Articles skipped (duplicates): {pipeline.stats['total_articles_skipped']}")
        logger.info(f"Chunks created: {pipeline.stats['total_chunks_created']}")
        logger.info(f"Chunks saved: {pipeline.stats['total_chunks_saved']}")
        logger.info(f"Errors: {pipeline.stats['errors']}")
        logger.info(f"End time: {datetime.now()}")
        print("=" * 80)

        if pipeline.stats['total_articles_processed'] > 0:
            logger.info("\n✅ SUCCESS: Ingestion completed!")
            return 0
        else:
            logger.warning("\n⚠️  WARNING: No articles were processed")
            logger.info("Possible reasons:")
            logger.info("  - All articles already exist in database")
            logger.info("  - No new articles discovered")
            logger.info("  - Check logs for errors")
            return 1

    except KeyboardInterrupt:
        logger.warning("\n❌ Interrupted by user")
        return 2
    except Exception as e:
        logger.exception(f"\n❌ Error: {e}")
        return 3

if __name__ == "__main__":
    sys.exit(main())
