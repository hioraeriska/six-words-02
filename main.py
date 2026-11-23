#!/usr/bin/env python3
"""Six Words, One Story entry.

Writes a complete story in exactly six words to
$MAKEFUN_OUTPUT_DIR/entry.txt (UTF-8, 1-60 characters, exactly six words).
"""
import os

STORY = "I kept his voicemail. Still do."


def validate_length(text):
    """Gate part 1: the story must be 1-60 characters."""
    if not (1 <= len(text) <= 60):
        raise ValueError("story must be 1-60 characters")


def validate_content(text):
    """Gate part 2: the story must be exactly six words, not only
    whitespace."""
    if not text.strip():
        raise ValueError("story must not be only whitespace")
    words = text.split()
    if len(words) != 6:
        raise ValueError("story must be exactly six words")


def validate_story(text):
    """Gate: the bounty only judges a story of exactly six words, 1-60
    characters, not only whitespace. Fail loudly here rather than silently
    submitting a story that can never be judged."""
    validate_length(text)
    validate_content(text)


def main():
    validate_story(STORY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
