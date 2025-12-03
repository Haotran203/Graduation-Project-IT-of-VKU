# app/utils/text.py

def normalize_title(payload: dict) -> str:
    title = payload.get("title")
    if not title or title.strip() == "":
        text = payload.get("text", "")
        title = text[:100].replace("\n", " ") + "..." if text else "Không rõ tiêu đề"
    return title
