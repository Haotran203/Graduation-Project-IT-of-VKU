# app/data_ingestion/auto_crawler.py

import logging
from typing import List, Set

from app.data_ingestion.wikipedia_scraper import WikipediaScraper
from app.data_ingestion.sources.historical_sources import HISTORICAL_SOURCES

logger = logging.getLogger(__name__)


class AutoCrawler:
    def __init__(self):
        self.wiki_scraper = WikipediaScraper()

    def discover_new_articles(
            self,
            max_per_category: int,
            known_titles: Set[str]
    ) -> List[str]:
        """
        Khám phá các bài viết mới cho đến khi đủ số lượng yêu cầu.

        Args:
            max_per_category: Số lượng bài viết MỚI tối đa cần tìm cho mỗi category.
            known_titles: Một set chứa tất cả các tiêu đề đã được xử lý (trí nhớ).
        """
        all_new_articles_set = set()  # Dùng set để tránh trùng lặp giữa các category
        categories = HISTORICAL_SOURCES["wikipedia_vi"]["categories"]

        for category in categories:
            logger.info(f"Scanning category: '{category}' for {max_per_category} new articles...")

            # Lấy một danh sách lớn các bài viết từ category để làm ứng viên
            # Giả định rằng trong 500 bài đầu tiên sẽ có đủ bài mới
            candidate_titles, _ = self.wiki_scraper.get_category_members_page(
                category=category,
                limit=max_per_category * 10  # Lấy gấp 10 lần để có dư
            )

            found_in_this_category = 0
            for title in candidate_titles:
                # Dừng lại nếu đã tìm đủ bài mới cho category này
                if found_in_this_category >= max_per_category:
                    break

                # Kiểm tra xem bài viết đã biết hoặc đã được thêm trong lần chạy này chưa
                if title not in known_titles and title not in all_new_articles_set:
                    logger.info(f"  [NEW] Found: {title}")
                    all_new_articles_set.add(title)
                    found_in_this_category += 1

            logger.info(f"  -> Found {found_in_this_category} new articles in this category.")

        total_found = len(all_new_articles_set)
        logger.info(f"\n[AUTO-DISCOVERY] Total new articles found across all categories: {total_found}")

        return list(all_new_articles_set)

    def mark_as_crawled(self, articles: List[str]):
        # Phương thức này không còn cần thiết trong logic mới,
        # vì DeduplicationManager đã quản lý việc này.
        pass
