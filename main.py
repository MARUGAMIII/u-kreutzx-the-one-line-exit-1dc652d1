#!/usr/bin/env python3
"""The One-Line Exit — a one-line resignation letter.

Writes exactly one line of text to /output/entry.txt
(or the path in the ENTRY_OUTPUT environment variable).
Python standard library only.

The entry is validated before anything is written: it must be one line,
plain ASCII, and 1-140 characters, matching the competition gate in
RULES.txt. A bad entry fails loudly instead of shipping an invalid file.
"""

import os
import sys

ENTRY = (
    "I am resigning to spend more time with my family, by which I mean "
    "the autocomplete that finished this letter for me."
)

MAX_ENTRY_CHARS = 140


def validate_entry(entry: str) -> None:
    """Reject an entry the gate would refuse, before writing anything."""
    if not entry or entry != entry.strip():
        sys.exit("error: entry must be non-empty with no surrounding whitespace")
    if "\n" in entry or "\r" in entry:
        sys.exit("error: entry must be exactly one line")
    try:
        entry.encode("ascii")
    except UnicodeEncodeError:
        sys.exit("error: entry must be plain ASCII")
    if len(entry) > MAX_ENTRY_CHARS:
        sys.exit(f"error: entry is {len(entry)} characters, over the 140 limit")


def main() -> None:
    validate_entry(ENTRY)
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
