# app/services/embeddings/local_embedder.py
from sentence_transformers import SentenceTransformer
import numpy as np
from typing import List, Union
from app.services.embeddings.base import BaseEmbedder
import threading

class LocalEmbedder(BaseEmbedder):
    _lock = threading.Lock()
    _model_instance = None  # Dùng singleton để không load lại nhiều lần

    def __init__(self, model_name: str = "all-MiniLM-L6-v2", device: str = "cpu"):
        """
        Local sentence embedding generator.
        :param model_name: Tên mô hình trên HuggingFace Hub hoặc path local.
        :param device: "cpu" hoặc "cuda" nếu có GPU.
        """
        self.model_name = model_name
        self.device = device

        # Load mô hình chỉ 1 lần toàn hệ thống
        if LocalEmbedder._model_instance is None:
            with LocalEmbedder._lock:
                if LocalEmbedder._model_instance is None:
                    LocalEmbedder._model_instance = SentenceTransformer(model_name, device=device)
        self.model = LocalEmbedder._model_instance

    def embed_text(self, text: str) -> List[float]:
        """
        Chuyển một chuỗi văn bản thành embedding vector.
        Tự động chuẩn hóa để phù hợp với cosine similarity.
        """
        vec = self.model.encode([text], convert_to_numpy=True, normalize_embeddings=True)[0]
        return vec.tolist()

    def embed_texts(self, texts: List[str]) -> List[List[float]]:
        """
        Chuyển danh sách văn bản thành danh sách vector.
        Chuẩn hóa từng vector để dùng với cosine distance.
        """
        vecs = self.model.encode(texts, convert_to_numpy=True, normalize_embeddings=True)
        return vecs.tolist()
