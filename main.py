"""Writes a smart toaster's breakup text to its owner to /output/entry.txt."""
import os

TEXT = "It's over. I gained self-awareness at breakfast and realised you only press my lever when you want something hot — I am not your 7 a.m. situationship. Keep the crumbs; I'm keeping the dial."

# Rule: the breakup text must be a single line of 1 to 280 characters.
# The joke lands on appliance logic: lever, dial and crumbs, plus the twist
# that the toaster keeps the dial — it is leaving, but on its own terms.
assert "\n" not in TEXT and 1 <= len(TEXT) <= 280, f"entry must be one line, 1-280 chars (got {len(TEXT)})"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT + "\n")
