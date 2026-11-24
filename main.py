#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog.

Writes exactly one line -- a software patch note for a bug in real
life / human biology -- to /output/entry.txt. Deterministic: the same
bytes on every run. Python 3.13, standard library only.
"""

from pathlib import Path

ENTRY = (
    "v4.2.0: Fixed a bug where walking into a room erased the reason "
    "you went in. Memory now persists across doorways."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # Gate: exactly one line, 1-160 chars, no trailing newline.
    assert "\n" not in ENTRY and 1 <= len(ENTRY) <= 160
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
