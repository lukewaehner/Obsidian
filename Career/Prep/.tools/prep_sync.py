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

import argparse
import datetime
import re
import sys
from collections import Counter, OrderedDict
from pathlib import Path

FM_KEY_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_]*):(.*)$")
COVERAGE_HEADER_RE = re.compile(r"^> \[!abstract\]-? Coverage — (\d+)/(\d+)\s*$")
COVERAGE_ITEM_RE = re.compile(r"^> - \[([ xX])\] ")
DERIVED_KEYS = ("sections_total", "sections_done", "coverage", "status", "updated")
PROBLEMS_HEADING = "## Problems"
NO_PROBLEMS = "_None yet._"
TOPIC_LINK_RE = re.compile(r"\[\[([^\]|#]+)")
PREP_BEGIN = "<!-- prep:begin -->"
PREP_END = "<!-- prep:end -->"
GROUP_ORDER = (
    "Complexity",
    "Data Structures",
    "Trees",
    "Graphs",
    "Sorting & Searching",
    "Algorithm Design",
    "Strings",
    "Math & Bits",
    "Systems",
    "Design",
)


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


TRUE_VALUES = frozenset(["true", "yes", "on", "1"])


def fm_bool(fm_lines, key):
    """Return *key* as a boolean, tolerating YAML's several spellings of true.

    Obsidian's property editor writes lowercase `true`, but a note edited by
    hand may say `True` or `yes`. Anything absent, empty, or unrecognised is
    False -- these properties are opt-in flags, so absence means off.
    """
    raw = fm_get(fm_lines, key)
    if raw is None:
        return False
    return raw.strip().strip("\"'").lower() in TRUE_VALUES


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


def parse_topic_links(raw_value):
    """Pull wikilink targets out of an inline frontmatter list.

    Accepts the flow form the templates emit, e.g.
    topics: ["[[Arrays]]", "[[Hash Tables]]"]. A folder path or a display
    alias on the link is stripped, so only the note name comes back.
    """
    if not raw_value:
        return []
    targets = []
    for match in TOPIC_LINK_RE.finditer(raw_value):
        target = match.group(1).strip()
        targets.append(target.rsplit("/", 1)[-1])
    return targets


def problem_entry(path, fm):
    """Render the list line a problem contributes to a topic's Problems section."""
    difficulty = fm_get(fm, "difficulty")
    pattern = path.parent.name
    return "- [[Career/Prep/problems/%s/%s|%s]] · %s · %s" % (
        pattern, path.stem, path.stem, difficulty, pattern
    )


def scan_problems(problems_root):
    """Read every problem note under *problems_root*.

    Returns (rewrites, entries_by_topic, records):
      rewrites          path -> the note's text with 'pattern' set from its folder
      entries_by_topic  topic note stem -> sorted list lines for its Problems section
      records           flat dicts for the Prep.md roll-up

    A note whose filename matches its folder is the folder note, not a
    problem, and is skipped.
    """
    rewrites = {}
    entries_by_topic = {}
    records = []

    if not problems_root.is_dir():
        return rewrites, entries_by_topic, records

    for path in sorted(problems_root.glob("*/*.md")):
        if path.stem == path.parent.name:
            continue

        text, _ = read_note(path)
        fm, body = split_note(path, text)

        difficulty = fm_get(fm, "difficulty")
        if difficulty is None:
            raise PrepError("%s: missing 'difficulty'" % path)

        new_fm = fm_set(fm, "pattern", path.parent.name)
        rewrites[path] = join_note(new_fm, body)

        entry = problem_entry(path, fm)
        for topic in parse_topic_links(fm_get(fm, "topics")):
            entries_by_topic.setdefault(topic, []).append(entry)

        records.append(
            {
                "name": path.stem,
                "pattern": path.parent.name,
                "difficulty": difficulty,
                "solved_on": fm_get(fm, "solved_on"),
                "revisit": fm_bool(fm, "revisit"),
                "aid": fm_get(fm, "aid"),
            }
        )

    for entries in entries_by_topic.values():
        entries.sort()

    return rewrites, entries_by_topic, records


def progress_bar(done, total, width=24):
    """Render an integer ratio as a fixed-width block bar."""
    filled = 0 if total == 0 else int(round(float(done) / total * width))
    return "█" * filled + "░" * (width - filled)


def replace_marked_block(lines, block):
    """Swap the content between PREP_BEGIN and PREP_END for *block*."""
    try:
        start = lines.index(PREP_BEGIN)
        end = lines.index(PREP_END)
    except ValueError:
        raise PrepError(
            "Prep.md: missing the %s / %s markers" % (PREP_BEGIN, PREP_END)
        ) from None
    return list(lines[:start + 1]) + list(block) + list(lines[end:])


def render_rollup(groups, records):
    """Build the generated section of Prep.md.

    *groups* maps a group name to a list of (note_name, done, total, tier).
    The date is deliberately absent from the output: it would make the hub
    differ from disk on the first run of every new day even when nothing
    moved, which is exactly the churn write-only-on-change exists to avoid.
    """
    core = [
        row for rows in groups.values() for row in rows if row[3] == "core"
    ]
    core_done = sum(row[1] for row in core)
    core_total = sum(row[2] for row in core)

    out = ["", "## Progress", ""]
    out.append(
        "`%s`  **%d / %d sections** across %d core topics"
        % (progress_bar(core_done, core_total), core_done, core_total, len(core))
    )
    out.append("")
    out.append("| Group | Coverage | Sections | Topics |")
    out.append("|---|---|---|---|")
    for name in GROUP_ORDER:
        rows = [row for row in groups.get(name, []) if row[3] == "core"]
        if not rows:
            continue
        done = sum(row[1] for row in rows)
        total = sum(row[2] for row in rows)
        out.append(
            "| [[Career/Prep/topics/%s/%s|%s]] | `%s` | %d/%d | %d |"
            % (name, name, name, progress_bar(done, total, width=16), done, total, len(rows))
        )

    weakest = sorted(
        (
            (group, row)
            for group, rows in groups.items()
            for row in rows
            if row[3] == "core"
        ),
        key=lambda pair: (
            float(pair[1][1]) / pair[1][2] if pair[1][2] else 0.0,
            pair[1][0],
        ),
    )[:5]
    out += ["", "## Weakest topics", ""]
    for group, (name, done, total, _) in weakest:
        out.append(
            "- [[Career/Prep/topics/%s/%s|%s]] — %d/%d"
            % (group, name, name, done, total)
        )

    out += ["", "## Problems", ""]
    if not records:
        out.append("None logged yet.")
    else:
        by_difficulty = Counter(r["difficulty"] for r in records)
        out.append(
            "**%d solved** — %d Easy · %d Medium · %d Hard"
            % (
                len(records),
                by_difficulty.get("Easy", 0),
                by_difficulty.get("Medium", 0),
                by_difficulty.get("Hard", 0),
            )
        )
        out.append("")
        out.append("| Pattern | Solved |")
        out.append("|---|---|")
        by_pattern = Counter(r["pattern"] for r in records)
        for pattern in sorted(by_pattern):
            out.append(
                "| [[Career/Prep/problems/%s/%s|%s]] | %d |"
                % (pattern, pattern, pattern, by_pattern[pattern])
            )

        revisit = sorted(
            (r for r in records if r["revisit"] or r["aid"] != "unaided"),
            key=lambda r: r["name"],
        )
        if revisit:
            out += ["", "## Needs revisit", ""]
            for record in revisit:
                out.append(
                    "- [[Career/Prep/problems/%s/%s|%s]] — %s"
                    % (record["pattern"], record["name"], record["name"], record["aid"])
                )

    out += ["", "_Generated by `prep_sync.py`. Do not edit between the markers._", ""]
    return out


def sync(root, today, dry_run):
    """Bring every derived value in the prep tree up to date.

    Returns the relative paths whose content differs from disk. With
    *dry_run* set, nothing is written.
    """
    root = Path(root)
    changed = []

    problem_rewrites, entries_by_topic, records = scan_problems(root / "problems")
    for path, new_text in sorted(problem_rewrites.items()):
        old_text, crlf = read_note(path)
        if new_text != old_text:
            changed.append(str(path.relative_to(root)))
            if not dry_run:
                write_note(path, new_text, crlf)

    groups = OrderedDict()
    for path in sorted((root / "topics").glob("*/*.md")):
        if path.stem == path.parent.name:
            continue
        old_text, crlf = read_note(path)
        fm, _ = split_note(path, old_text)
        if fm_get(fm, "type") != "topic":
            continue

        new_text, done, total = sync_topic(
            path, old_text, today, entries_by_topic.get(path.stem, [])
        )
        if new_text != old_text:
            changed.append(str(path.relative_to(root)))
            if not dry_run:
                write_note(path, new_text, crlf)

        group = fm_get(fm, "group") or path.parent.name
        if group not in GROUP_ORDER:
            raise PrepError(
                "%s: group '%s' is not one of: %s"
                % (path, group, ", ".join(GROUP_ORDER))
            )
        tier = fm_get(fm, "tier") or "core"
        groups.setdefault(group, []).append((path.stem, done, total, tier))

    hub = root / "Prep.md"
    if hub.is_file():
        old_text, crlf = read_note(hub)
        new_text = "\n".join(
            replace_marked_block(
                old_text.split("\n"), render_rollup(groups, records)
            )
        )
        if new_text != old_text:
            changed.append("Prep.md")
            if not dry_run:
                write_note(hub, new_text, crlf)

    return changed


def main(argv=None):
    """Entry point. 0 = clean, 1 = --check found drift, 2 = a note is malformed."""
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "root",
        nargs="?",
        default=str(Path(__file__).resolve().parent.parent),
        help="the Career/Prep directory (default: the parent of .tools)",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="report what would change and exit 1 if anything would, writing nothing",
    )
    args = parser.parse_args(argv)

    try:
        changed = sync(Path(args.root), datetime.date.today(), dry_run=args.check)
    except PrepError as error:
        sys.stderr.write("prep_sync: %s\n" % error)
        return 2

    if not changed:
        sys.stdout.write("prep_sync: up to date\n")
        return 0

    verb = "would update" if args.check else "updated"
    sys.stdout.write("prep_sync: %s %d file(s)\n" % (verb, len(changed)))
    for name in changed:
        sys.stdout.write("  %s\n" % name)
    return 1 if args.check else 0


if __name__ == "__main__":
    sys.exit(main())
