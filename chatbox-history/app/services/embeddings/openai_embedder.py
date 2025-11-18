# app/services/embeddings/openai_embedder.py
import openai
import httpx # Cần import httpx
from app.config.settings import settings
from app.services.embeddings.base import BaseEmbedder

class OpenAIEmbedder(BaseEmbedder):
    def __init__(self):
        # Cách làm hiện đại và an toàn để vô hiệu hóa proxy cho OpenAI
        http_client = httpx.Client()

        self.client = openai.OpenAI(
            api_key=settings.OPENAI_API_KEY,
            http_client=http_client
        )
        self.model = settings.OPENAI_EMBEDDING_MODEL

    def embed_text(self, text: str):
        # Sử dụng client đã được khởi tạo
        resp = self.client.embeddings.create(
            model=self.model,
            input=text
        )
        return resp.data[0].embedding