"""One Star, Written in Sap -- a houseplant's one-star review of its human owner.

Writes a single fixed review line to <output>/entry.txt.
Deterministic: the same text, byte-identical, on every run.
"""

import os

REVIEW = "One star: he waters me every time his ex texts, so I'm rotting from the roots up and he has closure."


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
