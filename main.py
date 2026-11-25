#!/usr/bin/env python3
"""The One-Liner Groan-Off — one-line dad joke entry.

Writes the joke to /output/entry.txt (UTF-8, 1-140 chars).
"""

import os

JOKE = "I started a band called 1023MB — we still haven't got a gig yet."


def main() -> None:
    text = JOKE.strip()
    assert 1 <= len(text) <= 140, f"joke must be 1-140 chars, got {len(text)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
