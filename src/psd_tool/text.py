"""Text helpers - the template's example of a small, typed, tested module.

Replace this module with your tool's real logic; keep the pattern
(typed signature, docstring, explicit error paths, real tests).
"""

import re
import unicodedata

_NON_ALNUM_RUNS = re.compile(r"[^a-z0-9]+")


def slugify(text: str, *, max_length: int = 64, separator: str = "-") -> str:
    """Convert arbitrary text into a URL- and filename-safe slug.

    Accents are stripped, case is folded, and runs of non-alphanumeric
    characters collapse into a single separator.

    Args:
        text: Input text.
        max_length: Maximum slug length; truncation never leaves a trailing
            separator.
        separator: Single character placed between words.

    Returns:
        The slug, or an empty string when nothing usable remains.

    Raises:
        ValueError: If ``max_length`` < 1 or ``separator`` is not exactly one
            character.
    """
    if max_length < 1:
        raise ValueError(f"max_length must be >= 1, got {max_length}")
    if len(separator) != 1:
        raise ValueError(f"separator must be a single character, got {separator!r}")

    ascii_text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    slug = _NON_ALNUM_RUNS.sub(separator, ascii_text.lower()).strip(separator)
    if len(slug) <= max_length:
        return slug
    return slug[:max_length].rstrip(separator)
