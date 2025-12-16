"""Stub file for split C extension."""

from collections.abc import Sequence
from typing import Literal

def split_text(
    text: str,
    delim: str | list[str] | None = None,
    include_delim: bool | Literal["prev", "next"] | None = False,
    min_characters_per_segment: int = 1,
    whitespace_mode: bool = False,
    character_fallback: bool = False
) -> Sequence[str]:
    """Split text using given delimiters.
    
    Args:
        text: Text to split
        delim: Delimiter string or list of delimiter strings
        include_delim: Whether to include delimiters in output
        min_characters_per_segment: Minimum characters per segment
        whitespace_mode: Whether to use whitespace splitting
        character_fallback: Whether to fall back to character splitting
        
    Returns:
        Sequence of text splits

    """
    ...