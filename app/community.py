from __future__ import annotations

import json
import uuid
from datetime import datetime
from pathlib import Path
import re

STORE_PATH = Path("/kaggle/working/data/community.json")
STORE_PATH.parent.mkdir(parents=True, exist_ok=True)

# Content safety filters
SPAM_KEYWORDS = ["buy now", "click here", "limited offer", "viagra", "casino", "lottery", "bitcoin"]
MAX_TEXT_LENGTH = 5000
MAX_AUTHOR_LENGTH = 100


def _sanitize_text(text: str) -> tuple[bool, str]:
    """Sanitize and validate text content. Returns (is_valid, cleaned_text)."""
    if not text or not text.strip():
        return False, ""

    text = text.strip()

    # Check length
    if len(text) > MAX_TEXT_LENGTH:
        return False, ""

    # Check for spam patterns
    text_lower = text.lower()
    if any(keyword in text_lower for keyword in SPAM_KEYWORDS):
        return False, ""

    # Remove excessive whitespace
    text = re.sub(r'\s+', ' ', text)

    # Basic HTML/script tag removal (if any)
    text = re.sub(r'<script.*?</script>', '', text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r'<.*?>', '', text)

    return True, text


def _sanitize_author(author: str) -> str:
    """Sanitize author name."""
    if not author or not author.strip():
        return "Anonymous"

    author = author.strip()[:MAX_AUTHOR_LENGTH]
    author = re.sub(r'<.*?>', '', author)  # Remove HTML tags
    return author or "Anonymous"


def _load() -> list:
    if not STORE_PATH.exists():
        return []
    try:
        with open(STORE_PATH) as f:
            return json.load(f)
    except Exception:
        return []


def _save(data: list):
    with open(STORE_PATH, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def get_all_tips() -> list:
    return _load()


def post_tip(author: str, language: str, text: str) -> dict:
    # Sanitize inputs
    is_valid, cleaned_text = _sanitize_text(text)
    if not is_valid:
        raise ValueError("Invalid tip content: text is empty, too long, or contains spam")

    cleaned_author = _sanitize_author(author)

    tips = _load()
    tip = {
        "id":        str(uuid.uuid4()),
        "author":    cleaned_author,
        "language":  language,
        "text":      cleaned_text,
        "timestamp": datetime.now().strftime("%d %b %Y, %I:%M %p"),
        "replies":   [],
        "likes":     0,
    }
    tips.insert(0, tip)
    _save(tips)
    return tip


def post_reply(tip_id: str, author: str, text: str) -> bool:
    # Sanitize inputs
    is_valid, cleaned_text = _sanitize_text(text)
    if not is_valid:
        raise ValueError("Invalid reply content: text is empty, too long, or contains spam")

    cleaned_author = _sanitize_author(author)

    tips = _load()
    for tip in tips:
        if tip["id"] == tip_id:
            tip["replies"].append({
                "id":        str(uuid.uuid4()),
                "author":    cleaned_author,
                "text":      cleaned_text,
                "timestamp": datetime.now().strftime("%d %b %Y, %I:%M %p"),
            })
            _save(tips)
            return True
    return False


def like_tip(tip_id: str) -> bool:
    tips = _load()
    for tip in tips:
        if tip["id"] == tip_id:
            tip["likes"] += 1
            _save(tips)
            return True
    return False