# app/utils/conversation.py
from typing import List, Dict, Optional
import logging

logger = logging.getLogger(__name__)


def build_conversation_history_text(history: List[dict]) -> str:
    """
    Chuyển lịch sử hội thoại thành text để đưa vào prompt.
    """
    if not history:
        return ""

    lines = []
    for turn in history:
        lines.append(f"Người dùng: {turn['user']}")
        lines.append(f"Trợ lý: {turn['assistant']}")

    return "\n".join(lines)


def rewrite_query_with_context(
        current_query: str,
        history: List[dict],
        generator
) -> str:
    """
    Viết lại câu hỏi hiện tại thành câu độc lập dựa vào lịch sử.

    Ví dụ:
    - Câu gốc: "tôi vừa hỏi câu hỏi gì ấy nhỉ?"
    - Viết lại: "Câu hỏi trước đó trong cuộc hội thoại này là gì?"
    """
    # Nếu không có lịch sử hoặc câu hỏi đã rõ ràng, không cần rewrite
    if not history or len(current_query) > 100:
        return current_query

    # Kiểm tra từ khóa tham chiếu (it, that, previous, vừa rồi, cái đó...)
    reference_keywords = [
        "nó", "cái đó", "vừa rồi", "trước đó", "câu trả lời",
        "it", "that", "previous", "earlier", "above"
    ]

    has_reference = any(kw in current_query.lower() for kw in reference_keywords)

    if not has_reference:
        return current_query

    # Tạo prompt cho LLM để rewrite
    history_text = build_conversation_history_text(history[-3:])  # Chỉ lấy 3 lượt gần nhất

    prompt = f"""Dựa vào lịch sử hội thoại dưới đây, hãy viết lại câu hỏi sau thành một câu hỏi đầy đủ, độc lập, dễ hiểu.

Lịch sử hội thoại:
{history_text}

Câu hỏi hiện tại: {current_query}

Viết lại câu hỏi thành câu độc lập (chỉ trả về câu hỏi, không giải thích):"""

    try:
        response = generator.generate(
            prompt=prompt,
            system="You are a helpful assistant that rewrites questions to be standalone.",
            enable_web_search=False
        )

        rewritten = response.get("answer", "").strip()
        logger.info(f"Query rewritten: '{current_query}' -> '{rewritten}'")
        return rewritten if rewritten else current_query

    except Exception as e:
        logger.error(f"Error rewriting query: {e}")
        return current_query


def should_use_conversation_context(query: str) -> bool:
    """
    Quyết định xem có cần dùng conversation context không.
    """
    # Các từ khóa yêu cầu ngữ cảnh hội thoại
    context_keywords = [
        "vừa", "trước", "câu hỏi", "câu trả lời", "nói",
        "it", "that", "previous", "earlier", "you said"
    ]

    return any(kw in query.lower() for kw in context_keywords)
