# app/services/generators/perplexity_generator.py
from perplexity import Perplexity
from app.services.generators.base import BaseGenerator
from app.config.settings import settings
import logging

logger = logging.getLogger(__name__)


class PerplexityGenerator(BaseGenerator):
    def __init__(self):
        # Truyền API key khi khởi tạo client
        self.client = Perplexity(api_key=settings.PERPLEXITY_API_KEY)

        # Mô hình mặc định (offline - không truy cập web)
        self.default_model = settings.PERPLEXITY_MODEL or "sonar-medium-chat"

        # Mô hình có khả năng tìm kiếm web
        self.web_model = "sonar-pro"

    def generate(
            self,
            prompt: str,
            system: str = "You are a helpful assistant.",
            enable_web_search: bool = False
    ) -> dict:
        """
        Tạo câu trả lời từ Perplexity API.

        Args:
            prompt: Câu hỏi hoặc context từ RAG
            system: System message
            enable_web_search: True = dùng mô hình có web search (sonar-pro)

        Returns:
            dict với keys: answer, model_used, raw
        """
        try:
            # Chọn mô hình dựa trên flag
            model_to_use = self.web_model if enable_web_search else self.default_model

            logger.info(f"Using model: {model_to_use}, web_search={enable_web_search}")

            completion = self.client.chat.completions.create(
                model=model_to_use,
                messages=[
                    {"role": "system", "content": system},
                    {"role": "user", "content": prompt}
                ]
            )

            answer = completion.choices[0].message.content

            return {
                "answer": answer,
                "model_used": model_to_use,
                "raw": completion
            }

        except Exception as e:
            logger.exception(f"Perplexity API error: {e}")
            return {
                "answer": "Xin lỗi, không thể kết nối với Perplexity API. Vui lòng thử lại sau.",
                "model_used": None,
                "raw": None,
                "error": str(e)
            }
