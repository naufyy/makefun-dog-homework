#!/usr/bin/env python3
"""Dog-homework excuse entry: writes the winning one-liner to /output/entry.txt.

The line is the proxy-judged winner (A2, 5/5 duels): the dog's own voice,
a concrete scene (the bowl, the good smells), and a twist that lands in
one line, with no stock cat/paper/good-boy move.
"""
from pathlib import Path

TEXT = "You left it where the good smells live, right next to my bowl. I thought it was a snack with questions on it."

assert 1 <= len(TEXT) <= 200, "entry must be 1-200 characters"
out = Path("/output/entry.txt")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(TEXT, encoding="utf-8")
