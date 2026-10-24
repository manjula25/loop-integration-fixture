"""Text utilities for loopsample."""

ELLIPSIS = "…"


def truncate(text: str, limit: int) -> str:
    """Return *text* shortened to at most *limit* characters.

    Text that already fits is returned unchanged. Longer text is cut and an
    ellipsis marks the cut, the ellipsis counting toward the limit:
    ``truncate("abcdef", 4) == "abc…"`` (three characters plus the ellipsis).
    """
    if len(text) <= limit:
        return text
    return text[:limit] + ELLIPSIS
