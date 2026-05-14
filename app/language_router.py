from __future__ import annotations

# Unicode script ranges for Indian languages
SCRIPT_RANGES = {
    "Telugu":  (0x0C00, 0x0C7F),
    "Hindi":   (0x0900, 0x097F),   # Devanagari — covers Hindi, Marathi
    "Bengali": (0x0980, 0x09FF),
    "Tamil":   (0x0B80, 0x0BFF),
    "Kannada": (0x0C80, 0x0CFF),
    "Malayalam": (0x0D00, 0x0D7F),
    "Gujarati": (0x0A80, 0x0AFF),
    "Punjabi": (0x0A00, 0x0A7F),
    "Urdu":    (0x0600, 0x06FF),   # Arabic script
    "Odia":    (0x0B00, 0x0B7F),
}


def detect_language(text: str) -> str | None:
    """
    Detect language from Unicode script ranges.
    Returns language name or None if only ASCII/unknown.
    """
    if not text:
        return None

    counts = {lang: 0 for lang in SCRIPT_RANGES}

    for char in text:
        cp = ord(char)
        for lang, (start, end) in SCRIPT_RANGES.items():
            if start <= cp <= end:
                counts[lang] += 1

    # pick language with most characters
    dominant = max(counts, key=counts.get)
    if counts[dominant] > 0:
        return dominant

    return None


def resolve_language(symptom_text: str, selected_language: str) -> str:
    """
    If symptom text contains a non-Latin script, use detected language.
    Otherwise fall back to sidebar selection.
    """
    detected = detect_language(symptom_text)
    return detected if detected else selected_language