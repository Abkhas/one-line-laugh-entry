#!/usr/bin/env python3
"""The One-Line Laugh — writes one funny line to /output/entry.txt."""

import os

LINE = (
    "I told my phone I was going to bed early, and it showed me a man "
    "building a log cabin in the woods, so now it's 3am and I own a saw."
)


def validate(line):
    """Gate: one line, 1-200 chars, not only whitespace."""
    stripped = line.strip()
    if not stripped:
        raise ValueError("line must not be blank")
    if len(line) > 200:
        raise ValueError("line exceeds 200 characters")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    return line


def write_entry(line, path="/output/entry.txt"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")


def main():
    write_entry(validate(LINE))


if __name__ == "__main__":
    main()
