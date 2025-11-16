# app/data_ingestion/wikipedia_scraper.py

import wikipediaapi
import logging
import time
from typing import List, Dict, Tuple, Optional

logger = logging.getLogger(__name__)


class WikipediaScraper:
    def __init__(self):
        self.wiki = wikipediaapi.Wikipedia(
            language='vi',
            user_agent='RAGHistoryBot/1.0 (contact@example.com)'
        )

    def get_category_members_page(
            self,
            category: str,
            limit: int = 500  # Lấy một số lượng lớn để đảm bảo có đủ ứng viên
    ) -> Tuple[List[str], Optional[str]]:
        """
        Lấy một "trang" (page) các bài viết từ một category.
        Do thư viện không hỗ trợ pagination, chúng ta lấy một danh sách lớn.
        """
        titles = []
        cat = self.wiki.page(f"Thể loại:{category}")

        if not cat.exists():
            logger.warning(f"Category not found: {category}")
            return [], None

        try:
            # Lấy các thành viên của category, giới hạn bởi `limit`
            # Thư viện sẽ trả về một generator, chúng ta chuyển nó thành list
            members = list(cat.categorymembers.keys())
            titles = members[:limit]
        except Exception as e:
            logger.error(f"Error getting members for category '{category}': {e}")

        return titles, None  # Trả về None vì không có token cho trang tiếp theo

    def fetch_articles(self, titles: List[str]) -> List[Dict]:
        """Thu thập nội dung từ danh sách tiêu đề."""
        articles = []
        if not titles:
            return articles

        for idx, title in enumerate(titles, 1):
            try:
                logger.info(f"Fetching {idx}/{len(titles)}: {title}")
                page = self.wiki.page(title)

                if not page.exists():
                    logger.warning(f"  Page not found: {title}")
                    continue

                articles.append({
                    "title": page.title,
                    "text": page.text,
                    "url": page.fullurl,
                    "source": "wikipedia"
                })

                logger.info(f"  [OK] Fetched ({len(page.text)} chars)")
                time.sleep(0.5)  # Rate limiting

            except Exception as e:
                logger.error(f"  [ERROR] Fetching article '{title}': {e}")

        return articles
