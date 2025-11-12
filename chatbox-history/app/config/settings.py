from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from pydantic import Field
from typing import Optional

# Load .env file
load_dotenv()

class Settings(BaseSettings):
    APP_NAME: str = Field("RAG History & Travel Assistant", env="APP_NAME")

    # Qdrant
    QDRANT_HOST: str = Field("localhost", env="QDRANT_HOST")
    QDRANT_PORT: int = Field(6333, env="QDRANT_PORT")
    QDRANT_URL: Optional[str] = Field(None, env="QDRANT_URL")  # 🆕 Thêm
    QDRANT_API_KEY: Optional[str] = Field(None, env="QDRANT_API_KEY")  # 🆕 Thêm
    COLLECTION_NAME: str = Field("rag_history_travel", env="COLLECTION_NAME")
    VECTOR_SIZE: int = Field(1024, env="VECTOR_SIZE")
    VECTOR_DISTANCE: str = Field("Cosine", env="VECTOR_DISTANCE")

    # Embedding
    EMBEDDING_PROVIDER: str = Field("LOCAL", env="EMBEDDING_PROVIDER")  # OPENAI / LOCAL
    OPENAI_API_KEY: Optional[str] = Field(None, env="OPENAI_API_KEY")
    OPENAI_EMBEDDING_MODEL: str = Field("text-embedding-3-small", env="OPENAI_EMBEDDING_MODEL")
    LOCAL_EMBEDDING_MODEL: str = Field("BAAI/bge-large-en-v1.5", env="LOCAL_EMBEDDING_MODEL")

    # LLM / Generator
    LLM_PROVIDER: str = Field("PERPLEXITY", env="LLM_PROVIDER")  # PERPLEXITY / OPENAI
    OPENAI_CHAT_MODEL: Optional[str] = Field("gpt-4o-mini", env="OPENAI_CHAT_MODEL")
    PERPLEXITY_API_KEY: Optional[str] = Field(None, env="PERPLEXITY_API_KEY")
    PERPLEXITY_MODEL: str = Field("sonar-pro", env="PERPLEXITY_MODEL")

    # Behavior
    MAX_CONTEXT_DOCS: int = Field(5, env="MAX_CONTEXT_DOCS")
    MAX_CONVERSATION_HISTORY: int = Field(5, env="MAX_CONVERSATION_HISTORY")

    # Misc
    DEBUG: bool = Field(True, env="DEBUG")

    # PostgreSQL
    POSTGRESQL_URL: str = Field(
        "postgresql+psycopg://postgres:postgres_password@localhost:5432/chatbot_db",
        env="POSTGRESQL_URL"
    )
    POSTGRESQL_ECHO: bool = Field(False, env="POSTGRESQL_ECHO")

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        "extra": "allow"
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # 🆕 Tự động tạo QDRANT_URL nếu chưa có
        if not self.QDRANT_URL:
            self.QDRANT_URL = f"http://{self.QDRANT_HOST}:{self.QDRANT_PORT}"

settings = Settings()