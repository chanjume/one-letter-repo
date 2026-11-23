#!/usr/bin/env python3
"""One Letter for Your Day — writes one letter, U for unhinged, to /output/entry.txt."""
import os

ENTRY = "U"  # U for "unhinged": a day where everything went off the rails — sharp, honest, not the obvious pick

assert len(ENTRY) == 1 and ENTRY.isalpha() and ENTRY.isupper(), "entry must be a single A-Z letter"
assert ENTRY.strip(), "entry must not be only whitespace"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)

print(f"Wrote {len(ENTRY)} char to /output/entry.txt")
