# app/utils/chunking.py
from typing import List
import re


def chunk_text_by_tokens(
        text: str,
        chunk_size: int = 512,
        chunk_overlap: int = 50,
        separator: str = "\n\n"
) -> List[dict]:
    """
    Chia văn bản thành các chunks với overlap.

    Args:
        text: Văn bản cần chia
        chunk_size: Kích thước chunk (tokens)
        chunk_overlap: Số tokens overlap giữa các chunks
        separator: Ký tự phân tách ưu tiên (paragraph)

    Returns:
        List of dicts with 'text' and some metadata (chunk_id, start_idx, end_idx)
    """
    # Tokenize đơn giản (split by whitespace)
    # Trong môi trường production nên dùng tokenizer cụ thể của model
    words = text.split()

    chunks = []
    start_idx = 0
    chunk_id = 0

    while start_idx < len(words):
        # Lấy chunk_size tokens
        end_idx = min(start_idx + chunk_size, len(words))
        chunk_words = words[start_idx:end_idx]
        chunk_text = " ".join(chunk_words)

        # Tìm điểm ngắt tự nhiên (câu hoàn chỉnh)
        if end_idx < len(words):
            # Tìm dấu chấm câu gần nhất trong chunk (để không cắt giữa câu)
            last_period = chunk_text.rfind(". ")
            if last_period > chunk_size * 0.5:  # Không quá ngắn phần còn lại
                chunk_text = chunk_text[:last_period + 1]
                # Tính lại end_idx theo độ dài chunk_text mới
                end_idx = start_idx + len(chunk_text.split())

        chunks.append({
            "text": chunk_text.strip(),
            "chunk_id": chunk_id,
            "start_idx": start_idx,
            "end_idx": end_idx
        })

        # Di chuyển con trỏ với overlap
        start_idx = end_idx - chunk_overlap
        chunk_id += 1

        # Tránh vòng lặp vô hạn khi gần kết thúc
        if start_idx >= len(words) - chunk_overlap:
            break

    return chunks


def chunk_text_semantic(
        text: str,
        max_chunk_size: int = 512,
        min_chunk_size: int = 100
) -> List[dict]:
    """
    Chia văn bản theo ngữ nghĩa (dựa trên đoạn văn).

    Ưu tiên giữ nguyên đoạn văn hoàn chỉnh, chia nhỏ đoạn quá dài.

    Args:
        text: Văn bản cần chia
        max_chunk_size: Kích thước tối đa của chunk (token)
        min_chunk_size: Kích thước tối thiểu để tránh chunk quá nhỏ

    Returns:
        List of dicts với 'text' và 'chunk_id'
    """
    # Chia đoạn văn bằng dấu xuống dòng đôi
    paragraphs = re.split(r'\n\n+', text)

    chunks = []
    current_chunk = []
    current_size = 0
    chunk_id = 0

    for para in paragraphs:
        para = para.strip()
        if not para:
            continue

        para_size = len(para.split())

        # Nếu đoạn quá dài, chia nhỏ
        if para_size > max_chunk_size:
            # Lưu chunk hiện tại nếu có
            if current_chunk:
                chunks.append({
                    "text": "\n\n".join(current_chunk),
                    "chunk_id": chunk_id
                })
                chunk_id += 1
                current_chunk = []
                current_size = 0

            # Chia nhỏ đoạn dài thành các sub-chunks token-based
            sub_chunks = chunk_text_by_tokens(para, max_chunk_size, 50)
            for sub in sub_chunks:
                chunks.append({
                    "text": sub["text"],
                    "chunk_id": chunk_id
                })
                chunk_id += 1

        # Nếu thêm đoạn này vượt quá kích thước max chunk
        elif current_size + para_size > max_chunk_size:
            # Lưu chunk hiện tại
            if current_chunk:
                chunks.append({
                    "text": "\n\n".join(current_chunk),
                    "chunk_id": chunk_id
                })
                chunk_id += 1

            # Bắt đầu chunk mới với đoạn hiện tại
            current_chunk = [para]
            current_size = para_size

        else:
            # Thêm đoạn vào chunk hiện tại
            current_chunk.append(para)
            current_size += para_size

    # Lưu chunk cuối cùng
    if current_chunk:
        chunks.append({
            "text": "\n\n".join(current_chunk),
            "chunk_id": chunk_id
        })

    return chunks


# Test và demo nhanh
if __name__ == "__main__":
    sample_text = """
    Đây là đoạn văn số 1. Nó chứa nhiều thông tin quan trọng về lịch sử.

    Đây là đoạn văn số 2. Nó tiếp tục câu chuyện từ đoạn trước.

    Đoạn văn số 3 rất dài và có thể cần được chia nhỏ. """ * 50

    chunks = chunk_text_semantic(sample_text, max_chunk_size=512)
    print(f"Created {len(chunks)} chunks")
    for i, chunk in enumerate(chunks[:3]):
        print(f"\nChunk {i}: {len(chunk['text'].split())} words")
        print(chunk['text'][:200] + "...")
