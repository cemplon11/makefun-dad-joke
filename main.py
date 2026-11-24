"""Dad Joke Showdown entry: writes one original dad joke to entry.txt.

Pure Python standard library only.
"""

import os

JOKE = "I named our dog Five Miles, so every day I can tell people I walk Five Miles before breakfast."

# The showdown entry is a single short joke; cap its length so an accidental
# edit that bloats or truncates the punchline fails loudly instead of
# silently shipping a broken entry.
MAX_CHARS = 200


def check_joke(text: str) -> None:
    """Self-check the joke before it is written anywhere."""
    assert text.strip(), "joke must not be empty"
    assert len(text) <= MAX_CHARS, f"joke is {len(text)} chars, limit is {MAX_CHARS}"


def write_joke(path: str) -> None:
    """Write the (already checked) joke to path, with no trailing newline."""
    check_joke(JOKE)
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    write_joke(path)


if __name__ == "__main__":
    main()
