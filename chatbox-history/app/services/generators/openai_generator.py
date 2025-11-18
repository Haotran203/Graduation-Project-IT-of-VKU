# app/services/generators/openai_generator.py
from openai import OpenAI
from app.services.generators.base import BaseGenerator
from app.config.settings import settings
import logging

logger = logging.getLogger(__name__)


class OpenAIGenerator(BaseGenerator):
    def __init__(self):
        """
        Khởi tạo OpenAI client.
        Yêu cầu: OPENAI_API_KEY trong settings
        """
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)

        # Mô hình mặc định (không web search)
        self.default_model = settings.OPENAI_MODEL or "gpt-4o-mini"

        # Mô hình cao cấp (nếu cần)
        self.premium_model = "gpt-4o"

        logger.info(f"OpenAI Generator initialized with model: {self.default_model}")

    def generate(
            self,
            prompt: str,
            system: str = "You are a helpful assistant.",
            enable_web_search: bool = False
    ) -> dict:
        """
        Tạo câu trả lời từ OpenAI API.

        Args:
            prompt: Câu hỏi hoặc context từ RAG
            system: System message
            enable_web_search: True = sử dụng premium model (gpt-4o)
                              False = sử dụng default model

        Returns:
            dict với keys: answer, model_used, raw, usage
        """
        try:
            # Chọn mô hình dựa trên flag
            model_to_use = self.premium_model if enable_web_search else self.default_model

            logger.info(f"[OPENAI] Using model: {model_to_use}, web_search={enable_web_search}")

            # Gọi API
            completion = self.client.chat.completions.create(
                model=model_to_use,
                messages=[
                    {"role": "system", "content": system},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,  # Điều chỉnh creativity (0.0 - 2.0)
                max_tokens=2000,  # Giới hạn độ dài response
                top_p=0.9,
            )

            answer = completion.choices[0].message.content

            # Extract usage info (tokens used)
            usage = {
                "prompt_tokens": completion.usage.prompt_tokens,
                "completion_tokens": completion.usage.completion_tokens,
                "total_tokens": completion.usage.total_tokens
            }

            logger.info(
                f"[OPENAI] ✓ Response generated | "
                f"Tokens: {usage['total_tokens']} "
                f"(prompt: {usage['prompt_tokens']}, completion: {usage['completion_tokens']})"
            )

            return {
                "answer": answer,
                "model_used": model_to_use,
                "usage": usage,
                "raw": completion
            }

        except Exception as e:
            logger.exception(f"[OPENAI] ✗ API error: {e}")
            return {
                "answer": "Xin lỗi, không thể kết nối với OpenAI API. Vui lòng kiểm tra API key hoặc thử lại sau.",
                "model_used": None,
                "usage": None,
                "raw": None,
                "error": str(e)
            }
