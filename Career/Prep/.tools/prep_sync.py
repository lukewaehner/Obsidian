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
COVERAGE_HEADER_RE = re.compile(r"^> \[!abstract\]-? Coverage — (\d+)/(\d+)\s*$")
COVERAGE_ITEM_RE = re.compile(r"^> - \[([ xX])\] ")
DERIVED_KEYS = ("sections_total", "sections_done", "coverage", "status", "updated")
PROBLEMS_HEADING = "## Problems"
NO_PROBLEMS = "_None yet._"


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


def parse_coverage(path, body_lines):
    """Locate and count the note's Coverage callout.

    Returns (header_index, done, total). Counting stops at the first line that
    is not a callout checklist item, so ordinary checkboxes elsewhere in the
    note are never mistaken for coverage.
    """
    header_index = None
    for i, line in enumerate(body_lines):
        if COVERAGE_HEADER_RE.match(line):
            header_index = i
            break
    if header_index is None:
        raise PrepError("%s: no Coverage callout" % path)

    done = 0
    total = 0
    for line in body_lines[header_index + 1:]:
        match = COVERAGE_ITEM_RE.match(line)
        if match is None:
            break
        total += 1
        if match.group(1) in ("x", "X"):
            done += 1

    if total == 0:
        raise PrepError("%s: Coverage callout has no items" % path)
    return header_index, done, total


def derive_status(done, total):
    """Map coverage counts onto the three status values Bases groups on."""
    if done == 0:
        return "untouched"
    if done < total:
        return "learning"
    return "solid"


def replace_problems_section(body_lines, entries):
    """Rewrite the '## Problems' section body with *entries*.

    Everything before the heading and from the next '## ' onwards is left
    untouched. A note without the heading is returned unchanged, which is how
    meta notes and problem notes pass through harmlessly.
    """
    try:
        start = body_lines.index(PROBLEMS_HEADING)
    except ValueError:
        return list(body_lines)

    end = len(body_lines)
    for i in range(start + 1, len(body_lines)):
        if body_lines[i].startswith("## "):
            end = i
            break

    content = [""] + (list(entries) if entries else [NO_PROBLEMS]) + [""]
    return list(body_lines[:start + 1]) + content + list(body_lines[end:])


def sync_topic(path, text, today, problem_entries):
    """Return (new_text, done, total) for one topic note.

    Pure: takes the note's current text and returns what it should be. The
    caller decides whether that differs from disk and therefore needs writing.
    """
    fm, body = split_note(path, text)
    header_index, done, total = parse_coverage(path, body)

    body = list(body)
    body[header_index] = re.sub(
        r"Coverage — \d+/\d+",
        "Coverage — %d/%d" % (done, total),
        body[header_index],
    )
    body = replace_problems_section(body, problem_entries)

    previous_done = fm_get(fm, "sections_done")
    fm = fm_set(fm, "sections_total", str(total))
    fm = fm_set(fm, "sections_done", str(done))
    fm = fm_set(fm, "coverage", "%.2f" % (float(done) / total))
    fm = fm_set(fm, "status", derive_status(done, total))
    # 'updated' means "when did progress last move", not "when did the script
    # last run" -- so it only advances when the tick count actually changed.
    if previous_done != str(done) or fm_get(fm, "updated") is None:
        fm = fm_set(fm, "updated", today.isoformat())

    return join_note(fm, body), done, total
