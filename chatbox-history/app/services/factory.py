# app/services/factory.py
from app.config.settings import settings
from app.services.embeddings.openai_embedder import OpenAIEmbedder
from app.services.embeddings.local_embedder import LocalEmbedder
from app.services.generators.perplexity_generator import PerplexityGenerator
from app.services.generators.openai_generator import OpenAIGenerator


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


def get_generator(providerRouter: str = None):
    """
    Factory function để lấy generator instance theo config.

    Supported providers:
        - OPENAI: OpenAI ChatGPT (gpt-4o-mini, gpt-4o)
        - PERPLEXITY: Perplexity Sonar (sonar-medium-chat, sonar-pro)
    """
    provider = providerRouter.upper() or settings.LLM_PROVIDER.upper()

    if provider == "OPENAI":
        return OpenAIGenerator()
    elif provider == "PERPLEXITY":
        return PerplexityGenerator()
    else:
        raise ValueError(f"Unsupported LLM provider: {provider}")
