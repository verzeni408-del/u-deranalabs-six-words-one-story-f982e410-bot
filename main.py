"""Six Words, One Story.

She walks out the door for good; the dog by the window
keeps waiting, season after season, year after year.
"""

import os

TEXT = "She left. The dog waited years."

parts = TEXT.split()
assert len(parts) == 6, f"expected 6 words, got {len(parts)}"

OUT_DIR = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
os.makedirs(OUT_DIR, exist_ok=True)

with open(os.path.join(OUT_DIR, "entry.txt"), "w", encoding="utf-8") as fh:
    fh.write(TEXT)

print(TEXT)
