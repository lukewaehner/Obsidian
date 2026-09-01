#!/usr/bin/env python3
"""Derive Prep progress frontmatter from note bodies.

Obsidian Bases can read frontmatter properties but cannot see checkboxes in a
note body. This script bridges the two: it reads each topic note's Coverage
callout and writes the resulting counts, ratio, and status back into that
note's frontmatter, so the databases stay accurate without any property being
maintained by hand.

Idempotent by construction. A file is opened for writing only when its content
would actually change -- the vault lives in iCloud Drive, where gratuitous
rewrites produce ' 2' conflict duplicates.
"""

import re
from pathlib import Path

FM_KEY_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_]*):(.*)$")


class PrepError(Exception):
    """A note could not be parsed. The message always names the file."""


def read_note(path):
    """Read *path* as UTF-8, normalising CRLF to LF.

    Returns (text, had_crlf) so write_note can restore the original endings.
    """
    with open(path, "r", encoding="utf-8", newline="") as handle:
        raw = handle.read()
    had_crlf = "\r\n" in raw
    return raw.replace("\r\n", "\n"), had_crlf


def write_note(path, text, crlf):
    """Write *text* to *path*, restoring CRLF endings if the note had them."""
    out = text.replace("\n", "\r\n") if crlf else text
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(out)


def split_note(path, text):
    """Split *text* into (frontmatter_lines, body_lines).

    The '---' delimiters are excluded from both. Raises PrepError when the
    note has no frontmatter: every generated note has one, so a note without
    one means the migration missed it and should fail loudly.
    """
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        raise PrepError("%s: no frontmatter block" % path)
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return lines[1:i], lines[i + 1:]
    raise PrepError("%s: unterminated frontmatter block" % path)


def join_note(fm_lines, body_lines):
    """Inverse of split_note. Byte-exact for anything split_note produced."""
    return "\n".join(["---"] + list(fm_lines) + ["---"] + list(body_lines))


def fm_get(fm_lines, key):
    """Return the raw scalar value for *key*, or None if it is absent."""
    for line in fm_lines:
        match = FM_KEY_RE.match(line)
        if match and match.group(1) == key:
            return match.group(2).strip()
    return None


def fm_set(fm_lines, key, value):
    """Return a copy of *fm_lines* with *key* set to *value*.

    Existing keys are replaced where they sit, so hand-authored key order
    survives. A missing key is appended, which happens only on a note's first
    sync.
    """
    out = list(fm_lines)
    new_line = "%s: %s" % (key, value)
    for i, line in enumerate(out):
        match = FM_KEY_RE.match(line)
        if match and match.group(1) == key:
            out[i] = new_line
            return out
    out.append(new_line)
    return out
