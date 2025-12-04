# app/utils/context.py

import re
import json
from typing import List, Dict, Any, Optional
from app.config.settings import settings

logger_imported = False
try:
    import logging

    logger = logging.getLogger(__name__)
    logger_imported = True
except:
    pass


def trim_text_to_chars(text: str, max_chars: int) -> str:
    """Cắt nội dung dài thành đoạn ngắn có độ dài tối đa."""
    if len(text) <= max_chars:
        return text
    return text[:max_chars - 3] + "..."


def build_unified_prompt(
        user_question: str,
        conversation_context: str,
        documents: List[Dict[str, Any]],
        role: str,
        enable_web_search: bool,
        original_docs_available: bool
) -> str:
    """
    ✅ OPTIMIZED: Build 1 unified prompt that tells provider everything.

    Provider will:
    1. Detect language automatically
    2. Generate answer in user's language
    3. Include coordinates if it's about locations
    4. Format response as needed

    All in 1 call.
    """

    # ✅ Role-specific guidance
    role_instructions = {
        "traveler": """Role: Tour Guide & Travel Advisor
Style: Friendly, practical, actionable (travel tips, hours, prices, transportation)
If about location: MUST include coordinates in JSON format""",
        "student": """Role: History & Geography Teacher
Style: Concise, structured, easy to understand
Focus: Historical context, events, figures, cause-effect
If about location: MUST include coordinates in JSON format""",
        "researcher": """Role: Academic Researcher
Style: Evidence-based, accurate citations, scholarly analysis
Include: Sources, references, different perspectives
If about location: MUST include coordinates in JSON format""",
        "enthusiast": """Role: Cultural Storyteller
Style: Vivid, engaging, emotional narrative
Focus: Stories, cultural heritage, connections to today
If about location: MUST include coordinates in JSON format"""
    }

    role_guidance = role_instructions.get(role, role_instructions["traveler"])

    # ✅ Build documents section
    documents_section = ""
    if original_docs_available and documents:
        max_docs = settings.MAX_CONTEXT_DOCS
        docs = documents[:max_docs]

        documents_section = "REFERENCE DOCUMENTS:\n"
        documents_section += "=" * 80 + "\n"

        for i, d in enumerate(docs, start=1):
            payload = d.get("payload", {}) or {}
            text = (
                    payload.get("text")
                    or payload.get("answer")
                    or payload.get("prompt")
                    or ""
            )
            title = (payload.get("title") or f"doc-{d.get('id') or i}").strip()
            url = (payload.get("url") or "").strip()
            score = d.get("score", 0)

            max_chars = 600
            snippet = trim_text_to_chars(text, max_chars)

            documents_section += f"\nDocument {i} (relevance={score:.2f})\n"
            documents_section += f"Title: {title}\n"
            if url:
                documents_section += f"URL: {url}\n"
            documents_section += f"Content:\n{snippet}\n"
            documents_section += "-" * 80 + "\n"
    else:
        documents_section = "NO REFERENCE DOCUMENTS AVAILABLE - Use your knowledge and web search if needed.\n"

    # ✅ UNIFIED PROMPT - FIX: Avoid f-string format issues with curly braces
    prompt_template = """### SYSTEM INSTRUCTIONS (Read Carefully)

{role_guidance}

### TASK
Answer the user's question comprehensively and accurately.

### KEY REQUIREMENTS

1. **LANGUAGE DETECTION & RESPONSE**
   - Auto-detect the language of the user's question
   - Respond ENTIRELY in the same language
   - Include the detected language in your response: <language>vi</language> (or en, zh, ja, ko, th, etc.)

2. **OUTPUT FORMAT**
   - Use Markdown for clear formatting
   - Headers: use ##
   - Bold for important terms: **text**
   - Use bullet points or tables when appropriate
   - Cite sources: [1] Title - URL

3. **LOCATION/COORDINATES**
   - If your answer mentions ANY location (city, landmark, address):
     MUST provide coordinates in JSON format
   - Format example:
     **Coordinates:**
     [
       {{"name": "Location 1", "latitude": 21.05, "longitude": 105.85}},
       {{"name": "Location 2", "latitude": 15.88, "longitude": 108.33}}
     ]
   - Include multiple coordinates if multiple locations are mentioned

4. **CONVERSATION CONTEXT**
   Use this to provide context-aware responses:
{conversation_context}

5. **REFERENCE DOCUMENTS**
{documents_section}

6. **WEB SEARCH**
   - Use real-time information if available
   - Prioritize accuracy and recency

---

### USER QUESTION
{user_question}

---

### YOUR RESPONSE
Start with language tag, then provide answer:
<language>DETECTED_LANGUAGE</language>

[Your comprehensive answer here - follow all requirements above]

---

Remember:
✓ Answer entirely in the user's language
✓ Include coordinates for locations (use double curly braces: {{}})
✓ Cite sources
✓ Follow the role-specific style above
✓ Be comprehensive and accurate
"""

    # ✅ Use .format() instead of f-string to avoid curly brace conflicts
    prompt_for_llm = prompt_template.format(
        role_guidance=role_guidance,
        conversation_context=conversation_context,
        documents_section=documents_section,
        user_question=user_question
    )

    return prompt_for_llm


def extract_single_coordinate(text: str) -> Optional[Dict[str, float]]:
    """Extract a single coordinate from text."""
    # Format 1: JSON-like
    json_pattern = r'\{\s*"latitude"\s*:\s*([0-9.-]+)\s*,\s*"longitude"\s*:\s*([0-9.-]+)\s*\}'
    match = re.search(json_pattern, text)
    if match:
        try:
            return {
                "latitude": float(match.group(1)),
                "longitude": float(match.group(2))
            }
        except (ValueError, IndexError):
            pass

    # Format 2: Vietnamese
    vi_pattern = r'vĩ\s*độ\s*:?\s*([0-9.]+).*?kinh\s*độ\s*:?\s*([0-9.]+)'
    match = re.search(vi_pattern, text, re.IGNORECASE | re.DOTALL)
    if match:
        try:
            return {
                "latitude": float(match.group(1)),
                "longitude": float(match.group(2))
            }
        except (ValueError, IndexError):
            pass

    # Format 3: Degree format
    degree_pattern = r'([0-9.]+)\s*°\s*[NS]\s*,?\s*([0-9.]+)\s*°\s*[EW]'
    match = re.search(degree_pattern, text)
    if match:
        try:
            return {
                "latitude": float(match.group(1)),
                "longitude": float(match.group(2))
            }
        except (ValueError, IndexError):
            pass

    return None


def extract_all_coordinates(text: str) -> List[Dict[str, Any]]:
    """
    ✅ Extract ALL coordinates from text.
    Supports multiple formats from provider response.
    """
    coordinates_list = []

    # Pattern 1: Array of objects
    array_pattern = r'\[\s*\{[^[\]]*"latitude"[^[\]]*"longitude"[^[\]]*\}[^\[\]]*\]'
    array_matches = re.finditer(array_pattern, text)

    for match in array_matches:
        try:
            parsed = json.loads(match.group(0))
            if isinstance(parsed, list):
                for coord in parsed:
                    lat = coord.get("latitude") or coord.get("lat")
                    lon = coord.get("longitude") or coord.get("lon")

                    if lat is not None and lon is not None:
                        coordinates_list.append({
                            "latitude": float(lat),
                            "longitude": float(lon),
                            "name": coord.get("name", f"Location {len(coordinates_list) + 1}"),
                        })
        except (json.JSONDecodeError, ValueError, TypeError):
            pass

    # Pattern 2: Individual JSON objects
    if len(coordinates_list) == 0:
        coord_pattern = r'\{[^{}]*"latitude"[^{}]*"longitude"[^{}]*\}|\{[^{}]*"longitude"[^{}]*"latitude"[^{}]*\}'
        matches = re.finditer(coord_pattern, text)

        for idx, match in enumerate(matches):
            try:
                parsed = json.loads(match.group(0))
                lat = parsed.get("latitude") or parsed.get("lat")
                lon = parsed.get("longitude") or parsed.get("lon")

                if lat is not None and lon is not None:
                    coordinates_list.append({
                        "latitude": float(lat),
                        "longitude": float(lon),
                        "name": parsed.get("name", f"Location {idx + 1}"),
                    })
            except (json.JSONDecodeError, ValueError, TypeError):
                pass

    # Pattern 3: Named locations with coordinates
    if len(coordinates_list) == 0:
        named_pattern = r'([^:\n]+):\s*vĩ\s*độ\s*([0-9.]+)\s*,\s*kinh\s*độ\s*([0-9.]+)'
        named_matches = re.finditer(named_pattern, text, re.IGNORECASE)

        for match in named_matches:
            try:
                coordinates_list.append({
                    "name": match.group(1).strip(),
                    "latitude": float(match.group(2)),
                    "longitude": float(match.group(3))
                })
            except (ValueError, IndexError):
                pass

    # Pattern 4: Table format
    if len(coordinates_list) == 0:
        table_pattern = r'\|\s*([^|\n]+)\s*\|\s*([0-9.]+)\s*\|\s*([0-9.]+)\s*\|'
        table_matches = re.finditer(table_pattern, text)

        for match in table_matches:
            try:
                if 'địa điểm' in match.group(1).lower() or 'location' in match.group(1).lower():
                    continue

                coordinates_list.append({
                    "name": match.group(1).strip(),
                    "latitude": float(match.group(2)),
                    "longitude": float(match.group(3))
                })
            except (ValueError, IndexError):
                pass

    # Remove duplicates
    seen = set()
    unique_coords = []
    for coord in coordinates_list:
        key = (round(coord['latitude'], 4), round(coord['longitude'], 4))
        if key not in seen:
            seen.add(key)
            unique_coords.append(coord)

    if logger_imported:
        logger.info(f"[COORDINATES] Extracted {len(unique_coords)} from response")

    return unique_coords


def add_coordinates_to_answer(answer: str, coordinates: List[Dict[str, Any]]) -> str:
    """Add coordinates section to answer if not present."""
    if not coordinates:
        return answer

    if "latitude" in answer and "longitude" in answer:
        return answer

    coords_section = "\n\n**Tọa độ bản đồ:**\n"
    coords_json = json.dumps(coordinates, ensure_ascii=False, indent=2)
    coords_section += coords_json

    return answer + coords_section
