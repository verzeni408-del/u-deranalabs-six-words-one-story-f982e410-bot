import os
from pathlib import Path

ENTRY = "She left. The dog waited years."

words = ENTRY.split()
assert len(words) == 6, "entry must be exactly six words"

output_dir = Path(os.environ.get("ENTRY_OUTPUT_DIR", "/output"))
output_dir.mkdir(parents=True, exist_ok=True)
with open(output_dir / "entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(ENTRY)
