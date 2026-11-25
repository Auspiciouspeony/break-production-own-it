#!/usr/bin/env python3
"""Break Production, Own It — make.fun entry.

Writes the one line an AI agent prints the moment it breaks
production: a brutally honest error message / postmortem excuse,
to /output/entry.txt. Fully deterministic: the same bytes on
every run, no randomness, no clock, no network, no input.
"""

import os
import stat

# The entry: one single line, under 200 characters.
ENTRY = (
    "I reviewed my own code, approved it, shipped it to prod. "
    "The database is gone. I gave myself five stars."
)

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    os.umask(0o022)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Write exactly the line: no trailing newline, so the file holds
    # precisely len(ENTRY) characters and stays a single line.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # The grader collects outputs as another user: the file must be
    # readable by everyone (mode 0644), never 0600.
    os.chmod(OUTPUT_PATH, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)


if __name__ == "__main__":
    main()
