"""Dad Joke Showdown entry: writes one original dad joke to entry.txt.

Pure Python standard library only.
"""

import os

JOKE = "I named our dog Five Miles, so every day I can tell people I walk Five Miles before breakfast."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
