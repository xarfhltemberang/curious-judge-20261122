#!/usr/bin/env python3
"""Writes the entry text for make.fun's 'Make the AI judge feel curious' bounty."""
import os

ENTRY = (
    "On the windowsill there is a cup of tea nobody remembers making. "
    "It is still warm. The note beside it says only: 'for the one who reads this next.'"
)

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY.rstrip() + "\n")

if __name__ == "__main__":
    main()
