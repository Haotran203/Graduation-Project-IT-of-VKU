# app/services/factory.py
from app.config.settings import settings

def get_embedder():
    """
    Factory function để lấy embedder instance theo config.

    Supported providers:
        - OPENAI: OpenAI embedding API
        - LOCAL / SENTENCE_TRANSFORMERS: Local sentence-transformers
    """
    provider = settings.EMBEDDING_PROVIDER.upper()

    if provider == "OPENAI":
        return OpenAIEmbedder()
    elif provider in ["LOCAL", "SENTENCE_TRANSFORMERS"]:
        return LocalEmbedder()
    else:
        raise ValueError(f"Unsupported embedding provider: {provider}")

