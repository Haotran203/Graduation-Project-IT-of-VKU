# app/db/conversation_store.py
from typing import List, Dict
from datetime import datetime


class ConversationStore:
    """
    Lưu trữ và truy xuất lịch sử hội thoại.
    Có thể dùng Qdrant payload hoặc database riêng (PostgreSQL/Redis).
    """

    def __init__(self):
        # Tạm thời dùng dict in-memory, sau chuyển sang DB thực
        self._memory: Dict[str, List[dict]] = {}

    def save_turn(self, user_id: str, conversation_id: str, user_query: str, assistant_answer: str):
        """
        Lưu một lượt hội thoại.
        """
        key = f"{user_id}:{conversation_id}"

        if key not in self._memory:
            self._memory[key] = []

        self._memory[key].append({
            "user": user_query,
            "assistant": assistant_answer,
            "timestamp": datetime.now().isoformat()
        })

    def get_history(self, user_id: str, conversation_id: str, limit: int = 5) -> List[dict]:
        """
        Lấy lịch sử hội thoại gần nhất.
        """
        key = f"{user_id}:{conversation_id}"
        history = self._memory.get(key, [])
        return history[-limit:] if history else []

    def clear_history(self, user_id: str, conversation_id: str):
        """
        Xóa lịch sử một cuộc hội thoại.
        """
        key = f"{user_id}:{conversation_id}"
        if key in self._memory:
            del self._memory[key]


# Singleton instance
conversation_store = ConversationStore()
