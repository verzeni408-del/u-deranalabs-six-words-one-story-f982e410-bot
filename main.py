"""Six Words, One Story -- v2.

A six-word story about loyalty outliving goodbye:
she leaves, and the dog keeps waiting for years.
"""

import os

STORY = "She left. The dog waited years."

WORDS = STORY.split()

assert len(WORDS) == 6, f"expected exactly 6 words, got {len(WORDS)}"


def main():
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(STORY)


if __name__ == "__main__":
    main()
