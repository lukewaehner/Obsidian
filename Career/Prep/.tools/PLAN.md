# Prep System Revamp Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace `Career/Prep/`'s mirrored `topics/` + `work/` trees with one note per idea, a pattern-organised problems area, two Bases databases over both, and a sync script that derives every progress property from note-body checkboxes so nothing is hand-maintained.

**Architecture:** Note bodies are the source of truth. `prep_sync.py` parses each topic note's Coverage callout and writes the derived counts into that note's frontmatter; Bases reads only frontmatter and computes nothing. The script is idempotent and writes a file only when its content would actually change, because the vault is in iCloud Drive.

**Tech Stack:** Obsidian 1.9.10 (Bases core plugin), Python 3.9.6 stdlib only, `unittest`, launchd, Claude Code slash commands.

**Spec:** `Career/Prep/.tools/DESIGN.md`. The topic manifest in that file's "Topic manifest" section is the authoritative source→destination mapping for Tasks 9–11 and is not repeated here.

## Global Constraints

- Vault root: `/Users/lukewaehner/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain`. Prep root: `<vault>/Career/Prep`.
- Python 3.9.6, **stdlib only**. No PyYAML, no pip installs. No f-string `=` specifier, no `match`, no `X | Y` type unions at runtime.
- Every file the script writes must be byte-identical to what was there when nothing changed. Gratuitous rewrites inside iCloud Drive create ` 2` conflict duplicates.
- Notes are UTF-8. The Coverage callout header uses an em dash (`—`, U+2014) and the middot in problem titles is `·` (U+00B7). Copy these characters exactly.
- Obsidian must be closed on all other devices before Task 9. Confirm with the user before starting Task 9.
- Commit messages: Conventional Commits, imperative, lowercase after the colon, no trailing period. **No `Co-Authored-By` and no tool-attribution trailers.** Behaviour changes and refactors go in separate commits.
- Never push. Commit only.
- Ten topic group names, exactly: `Complexity`, `Data Structures`, `Trees`, `Graphs`, `Sorting & Searching`, `Algorithm Design`, `Strings`, `Math & Bits`, `Systems`, `Design`.
- Eighteen problem pattern names, exactly: `Arrays & Hashing`, `Two Pointers`, `Sliding Window`, `Stack`, `Binary Search`, `Linked List`, `Trees`, `Tries`, `Heap & Priority Queue`, `Backtracking`, `Graphs`, `Advanced Graphs`, `1-D DP`, `2-D DP`, `Greedy`, `Intervals`, `Math & Geometry`, `Bit Manipulation`.
- Tests live in `Career/Prep/.tools/tests/` and run with `cd "<vault>/Career/Prep/.tools" && python3 -m unittest discover -s tests -v`.

---

### Task 1: Snapshot the working tree

The repo currently has ~40 uncommitted deletions and modifications under `Career/Prep/` from earlier work. Everything after this task rewrites that tree, so the current state has to be recoverable first.

**Files:**
- Modify: none directly — this commits what is already on disk.

**Interfaces:**
- Consumes: nothing.
- Produces: a commit that Tasks 9–12 can be diffed and reverted against.

- [ ] **Step 1: Look at what is uncommitted**

```bash
cd "/Users/lukewaehner/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain"
git status --porcelain -- Career/Prep | cat
```

Expected: a list of `D`, `M`, and `??` entries under `Career/Prep/`. Read it. If anything outside `Career/Prep/` appears, stop and ask — this task must not sweep up unrelated work.

- [ ] **Step 2: Confirm no secrets or binaries are being committed**

```bash
git add -A -- Career/Prep
git diff --staged --stat | tail -5
git diff --staged | grep -inE 'api[_-]?key|secret|password|token|BEGIN [A-Z ]*PRIVATE KEY' | head
```

Expected: the `grep` prints nothing. If it prints anything, unstage that file and stop.

- [ ] **Step 3: Commit**

```bash
git commit -m "chore(prep): snapshot the prep tree before the revamp

The topics/work reorganisation rewrites this whole directory. Capturing
the in-flight state first so the migration has something to diff against."
```

- [ ] **Step 4: Verify the tree is clean**

```bash
git status --porcelain -- Career/Prep | cat
```

Expected: no output.

---

### Task 2: `prep_sync` — note splitting with a byte-exact round trip

The script rewrites frontmatter inside notes full of hand-written prose. Before it derives anything, prove it can take a note apart and put it back together unchanged. Every later task builds on this guarantee.

**Files:**
- Create: `Career/Prep/.tools/prep_sync.py`
- Create: `Career/Prep/.tools/tests/__init__.py` (empty)
- Test: `Career/Prep/.tools/tests/test_prep_sync.py`

**Interfaces:**
- Consumes: nothing.
- Produces:
  - `PrepError(Exception)`
  - `read_note(path) -> Tuple[str, bool]` — returns `(text_with_lf_newlines, had_crlf)`
  - `write_note(path, text, crlf) -> None`
  - `split_note(path, text) -> Tuple[List[str], List[str]]` — `(frontmatter_lines, body_lines)`, delimiters excluded
  - `join_note(fm_lines, body_lines) -> str`
  - `fm_get(fm_lines, key) -> Optional[str]`
  - `fm_set(fm_lines, key, value) -> List[str]`

- [ ] **Step 1: Write the failing tests**

Create `Career/Prep/.tools/tests/__init__.py` as an empty file, then `Career/Prep/.tools/tests/test_prep_sync.py`:

```python
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import prep_sync


NOTE = """---
type: topic
group: Graphs
tier: core
confidence: 3
---

# Dijkstra's Algorithm

> [!abstract]- Coverage — 1/2
> - [x] [[#Idea]]
> - [ ] [[#Gotchas]]

## Idea

Relax edges in order of tentative distance.
"""


class SplitNoteTest(unittest.TestCase):
    def test_round_trip_returns_byte_identical_text(self):
        # arrange
        fm, body = prep_sync.split_note(Path("Dijkstra.md"), NOTE)

        # act
        rebuilt = prep_sync.join_note(fm, body)

        # assert
        self.assertEqual(NOTE, rebuilt)

    def test_frontmatter_excludes_the_delimiters(self):
        # arrange / act
        fm, _ = prep_sync.split_note(Path("Dijkstra.md"), NOTE)

        # assert
        self.assertEqual(
            ["type: topic", "group: Graphs", "tier: core", "confidence: 3"], fm
        )

    def test_body_starts_after_the_closing_delimiter(self):
        # arrange / act
        _, body = prep_sync.split_note(Path("Dijkstra.md"), NOTE)

        # assert
        self.assertEqual("", body[0])
        self.assertEqual("# Dijkstra's Algorithm", body[1])

    def test_raises_naming_the_file_when_frontmatter_is_missing(self):
        # arrange
        text = "# Dijkstra's Algorithm\n"

        # act / assert
        with self.assertRaises(prep_sync.PrepError) as caught:
            prep_sync.split_note(Path("Dijkstra.md"), text)
        self.assertIn("Dijkstra.md", str(caught.exception))

    def test_raises_when_frontmatter_is_unterminated(self):
        # arrange
        text = "---\ntype: topic\n\n# Heading\n"

        # act / assert
        with self.assertRaises(prep_sync.PrepError):
            prep_sync.split_note(Path("Dijkstra.md"), text)


class FrontmatterAccessTest(unittest.TestCase):
    def test_get_returns_the_scalar_value(self):
        # arrange
        fm = ["type: topic", "confidence: 3"]

        # act / assert
        self.assertEqual("3", prep_sync.fm_get(fm, "confidence"))

    def test_get_returns_none_for_an_absent_key(self):
        # arrange
        fm = ["type: topic"]

        # act / assert
        self.assertIsNone(prep_sync.fm_get(fm, "coverage"))

    def test_set_replaces_in_place_preserving_key_order(self):
        # arrange
        fm = ["type: topic", "status: untouched", "confidence: 3"]

        # act
        result = prep_sync.fm_set(fm, "status", "learning")

        # assert
        self.assertEqual(
            ["type: topic", "status: learning", "confidence: 3"], result
        )

    def test_set_appends_a_key_that_is_not_present_yet(self):
        # arrange
        fm = ["type: topic"]

        # act
        result = prep_sync.fm_set(fm, "coverage", "0.5")

        # assert
        self.assertEqual(["type: topic", "coverage: 0.5"], result)

    def test_set_does_not_mutate_the_input_list(self):
        # arrange
        fm = ["type: topic"]

        # act
        prep_sync.fm_set(fm, "coverage", "0.5")

        # assert
        self.assertEqual(["type: topic"], fm)


class LineEndingTest(unittest.TestCase):
    def test_crlf_notes_are_normalised_on_read_and_restored_on_write(self):
        # arrange
        import tempfile

        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "crlf.md"
            with open(path, "wb") as handle:
                handle.write(NOTE.replace("\n", "\r\n").encode("utf-8"))

            # act
            text, crlf = prep_sync.read_note(path)
            prep_sync.write_note(path, text, crlf)

            # assert
            self.assertTrue(crlf)
            self.assertNotIn("\r", text)
            with open(path, "rb") as handle:
                self.assertEqual(NOTE.replace("\n", "\r\n").encode("utf-8"), handle.read())


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run the tests to verify they fail**

```bash
cd "/Users/lukewaehner/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain/Career/Prep/.tools"
python3 -m unittest discover -s tests -v
```

Expected: `ModuleNotFoundError: No module named 'prep_sync'`.

- [ ] **Step 3: Write the implementation**

Create `Career/Prep/.tools/prep_sync.py`:

```python
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
```

- [ ] **Step 4: Run the tests to verify they pass**

```bash
cd "/Users/lukewaehner/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain/Career/Prep/.tools"
python3 -m unittest discover -s tests -v
```

Expected: `OK`, 11 tests.

- [ ] **Step 5: Commit**

```bash
cd "/Users/lukewaehner/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain"
git add Career/Prep/.tools/prep_sync.py Career/Prep/.tools/tests/
git commit -m "feat(prep): add note frontmatter reader with byte-exact round trip

The sync script edits frontmatter inside notes full of hand-written prose,
so splitting and rejoining a note has to be lossless before anything is
derived from it."
```

---

### Task 3: `prep_sync` — Coverage callout parsing

**Files:**
- Modify: `Career/Prep/.tools/prep_sync.py`
- Test: `Career/Prep/.tools/tests/test_prep_sync.py`

**Interfaces:**
- Consumes: `PrepError` from Task 2.
- Produces:
  - `parse_coverage(path, body_lines) -> Tuple[int, int, int]` — `(header_index, done, total)`
  - `derive_status(done, total) -> str` — one of `"untouched"`, `"learning"`, `"solid"`
  - Module constants `COVERAGE_HEADER_RE`, `COVERAGE_ITEM_RE`

- [ ] **Step 1: Write the failing tests**

Append to `Career/Prep/.tools/tests/test_prep_sync.py`, above the `if __name__` block:

```python
class ParseCoverageTest(unittest.TestCase):
    def test_counts_ticked_and_total_items(self):
        # arrange
        body = [
            "# Dijkstra",
            "",
            "> [!abstract]- Coverage — 0/0",
            "> - [x] [[#Idea]]",
            "> - [x] [[#How it works]]",
            "> - [ ] [[#Gotchas]]",
            "",
            "## Idea",
        ]

        # act
        header_index, done, total = prep_sync.parse_coverage(Path("d.md"), body)

        # assert
        self.assertEqual((2, 2, 3), (header_index, done, total))

    def test_stops_counting_at_the_first_non_item_line(self):
        # arrange
        body = [
            "> [!abstract]- Coverage — 0/0",
            "> - [x] [[#Idea]]",
            "",
            "- [ ] a stray checkbox further down the note",
        ]

        # act
        _, done, total = prep_sync.parse_coverage(Path("d.md"), body)

        # assert
        self.assertEqual((1, 1), (done, total))

    def test_accepts_a_capital_x(self):
        # arrange
        body = ["> [!abstract]- Coverage — 0/1", "> - [X] [[#Idea]]"]

        # act
        _, done, _ = prep_sync.parse_coverage(Path("d.md"), body)

        # assert
        self.assertEqual(1, done)

    def test_accepts_an_expanded_callout_without_the_fold_marker(self):
        # arrange
        body = ["> [!abstract] Coverage — 0/1", "> - [ ] [[#Idea]]"]

        # act
        header_index, _, total = prep_sync.parse_coverage(Path("d.md"), body)

        # assert
        self.assertEqual((0, 1), (header_index, total))

    def test_raises_naming_the_file_when_the_callout_is_missing(self):
        # arrange
        body = ["# Dijkstra", "", "## Idea"]

        # act / assert
        with self.assertRaises(prep_sync.PrepError) as caught:
            prep_sync.parse_coverage(Path("Dijkstra.md"), body)
        self.assertIn("Dijkstra.md", str(caught.exception))

    def test_raises_when_the_callout_has_no_items(self):
        # arrange
        body = ["> [!abstract]- Coverage — 0/0", "", "## Idea"]

        # act / assert
        with self.assertRaises(prep_sync.PrepError):
            prep_sync.parse_coverage(Path("Dijkstra.md"), body)


class DeriveStatusTest(unittest.TestCase):
    def test_no_sections_done_is_untouched(self):
        self.assertEqual("untouched", prep_sync.derive_status(0, 6))

    def test_some_sections_done_is_learning(self):
        self.assertEqual("learning", prep_sync.derive_status(3, 6))

    def test_all_sections_done_is_solid(self):
        self.assertEqual("solid", prep_sync.derive_status(6, 6))
```

- [ ] **Step 2: Run the tests to verify they fail**

```bash
cd "/Users/lukewaehner/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain/Career/Prep/.tools"
python3 -m unittest discover -s tests -v
```

Expected: `AttributeError: module 'prep_sync' has no attribute 'parse_coverage'`.

- [ ] **Step 3: Write the implementation**

Add to `prep_sync.py`, below `FM_KEY_RE`:

```python
COVERAGE_HEADER_RE = re.compile(r"^> \[!abstract\]-? Coverage — (\d+)/(\d+)\s*$")
COVERAGE_ITEM_RE = re.compile(r"^> - \[([ xX])\] ")
```

and below `fm_set`:

```python
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
```

- [ ] **Step 4: Run the tests to verify they pass**

```bash
cd "/Users/lukewaehner/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain/Career/Prep/.tools"
python3 -m unittest discover -s tests -v
```

Expected: `OK`, 20 tests.

- [ ] **Step 5: Commit**

```bash
cd "/Users/lukewaehner/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain"
git add Career/Prep/.tools/
git commit -m "feat(prep): parse the Coverage callout into section counts

Counting stops at the first non-item line so checkboxes written elsewhere
in a note never leak into the progress numbers."
```

---

### Task 4: `prep_sync` — topic frontmatter derivation

**Files:**
- Modify: `Career/Prep/.tools/prep_sync.py`
- Test: `Career/Prep/.tools/tests/test_prep_sync.py`

**Interfaces:**
- Consumes: `split_note`, `join_note`, `fm_get`, `fm_set`, `parse_coverage`, `derive_status`.
- Produces:
  - `sync_topic(path, text, today, problem_entries) -> Tuple[str, int, int]` — `(new_text, done, total)`. `today` is a `datetime.date`; `problem_entries` is a `List[str]` of markdown list lines.
  - `DERIVED_KEYS: Tuple[str, ...]`

- [ ] **Step 1: Write the failing tests**

Append to `test_prep_sync.py`:

```python
import datetime

TOPIC = """---
type: topic
group: Graphs
tier: core
confidence: 3
---

# Dijkstra's Algorithm

> [!abstract]- Coverage — 0/3
> - [x] [[#Idea]]
> - [x] [[#How it works]]
> - [ ] [[#Gotchas]]

## Idea

Relax edges in order of tentative distance.

## Problems

_None yet._

## Resources

- [MIT 6.006 Dijkstra](https://example.com)
"""

TODAY = datetime.date(2026, 9, 1)


class SyncTopicTest(unittest.TestCase):
    def test_writes_the_derived_counts_into_frontmatter(self):
        # arrange / act
        text, done, total = prep_sync.sync_topic(Path("d.md"), TOPIC, TODAY, [])

        # assert
        fm, _ = prep_sync.split_note(Path("d.md"), text)
        self.assertEqual("3", prep_sync.fm_get(fm, "sections_total"))
        self.assertEqual("2", prep_sync.fm_get(fm, "sections_done"))
        self.assertEqual("0.67", prep_sync.fm_get(fm, "coverage"))
        self.assertEqual("learning", prep_sync.fm_get(fm, "status"))
        self.assertEqual((2, 3), (done, total))

    def test_preserves_hand_authored_properties_and_their_order(self):
        # arrange / act
        text, _, _ = prep_sync.sync_topic(Path("d.md"), TOPIC, TODAY, [])

        # assert
        fm, _ = prep_sync.split_note(Path("d.md"), text)
        self.assertEqual(
            ["type: topic", "group: Graphs", "tier: core", "confidence: 3"], fm[:4]
        )

    def test_preserves_body_prose_verbatim(self):
        # arrange / act
        text, _, _ = prep_sync.sync_topic(Path("d.md"), TOPIC, TODAY, [])

        # assert
        self.assertIn("Relax edges in order of tentative distance.", text)
        self.assertIn("- [MIT 6.006 Dijkstra](https://example.com)", text)

    def test_rewrites_the_stale_count_in_the_callout_header(self):
        # arrange / act
        text, _, _ = prep_sync.sync_topic(Path("d.md"), TOPIC, TODAY, [])

        # assert
        self.assertIn("> [!abstract]- Coverage — 2/3", text)
        self.assertNotIn("Coverage — 0/3", text)

    def test_is_idempotent(self):
        # arrange
        once, _, _ = prep_sync.sync_topic(Path("d.md"), TOPIC, TODAY, [])

        # act
        twice, _, _ = prep_sync.sync_topic(Path("d.md"), once, TODAY, [])

        # assert
        self.assertEqual(once, twice)

    def test_updated_advances_only_when_sections_done_changes(self):
        # arrange
        first, _, _ = prep_sync.sync_topic(Path("d.md"), TOPIC, TODAY, [])
        later = datetime.date(2026, 10, 15)

        # act
        unchanged, _, _ = prep_sync.sync_topic(Path("d.md"), first, later, [])

        # assert
        fm, _ = prep_sync.split_note(Path("d.md"), unchanged)
        self.assertEqual("2026-09-01", prep_sync.fm_get(fm, "updated"))

    def test_updated_advances_when_a_box_is_ticked(self):
        # arrange
        first, _, _ = prep_sync.sync_topic(Path("d.md"), TOPIC, TODAY, [])
        ticked = first.replace("> - [ ] [[#Gotchas]]", "> - [x] [[#Gotchas]]")
        later = datetime.date(2026, 10, 15)

        # act
        text, _, _ = prep_sync.sync_topic(Path("d.md"), ticked, later, [])

        # assert
        fm, _ = prep_sync.split_note(Path("d.md"), text)
        self.assertEqual("2026-10-15", prep_sync.fm_get(fm, "updated"))
        self.assertEqual("solid", prep_sync.fm_get(fm, "status"))

    def test_fills_the_problems_section_from_the_supplied_entries(self):
        # arrange
        entries = ["- [[743 · Network Delay Time]] · Medium"]

        # act
        text, _, _ = prep_sync.sync_topic(Path("d.md"), TOPIC, TODAY, entries)

        # assert
        self.assertIn("- [[743 · Network Delay Time]] · Medium", text)
        self.assertNotIn("_None yet._", text)

    def test_empty_problems_section_says_so_rather_than_going_blank(self):
        # arrange / act
        text, _, _ = prep_sync.sync_topic(Path("d.md"), TOPIC, TODAY, [])

        # assert
        self.assertIn("## Problems\n\n_None yet._\n", text)

    def test_rewriting_the_problems_section_does_not_eat_the_next_section(self):
        # arrange / act
        text, _, _ = prep_sync.sync_topic(
            Path("d.md"), TOPIC, TODAY, ["- [[1 · Two Sum]] · Easy"]
        )

        # assert
        self.assertIn("## Resources", text)
        self.assertIn("- [MIT 6.006 Dijkstra](https://example.com)", text)
```

- [ ] **Step 2: Run the tests to verify they fail**

```bash
cd "/Users/lukewaehner/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain/Career/Prep/.tools"
python3 -m unittest discover -s tests -v
```

Expected: `AttributeError: module 'prep_sync' has no attribute 'sync_topic'`.

- [ ] **Step 3: Write the implementation**

Add `DERIVED_KEYS` below `COVERAGE_ITEM_RE`:

```python
DERIVED_KEYS = ("sections_total", "sections_done", "coverage", "status", "updated")
PROBLEMS_HEADING = "## Problems"
NO_PROBLEMS = "_None yet._"
```

and append to `prep_sync.py`:

```python
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
```

- [ ] **Step 4: Run the tests to verify they pass**

```bash
cd "/Users/lukewaehner/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain/Career/Prep/.tools"
python3 -m unittest discover -s tests -v
```

Expected: `OK`, 30 tests.

- [ ] **Step 5: Commit**

```bash
cd "/Users/lukewaehner/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain"
git add Career/Prep/.tools/
git commit -m "feat(prep): derive topic progress properties from the Coverage callout

sync_topic is pure so the caller can compare its output against disk and
skip the write entirely when nothing moved."
```

---

### Task 5: `prep_sync` — problem scanning and pattern derivation

**Files:**
- Modify: `Career/Prep/.tools/prep_sync.py`
- Test: `Career/Prep/.tools/tests/test_problems.py`

**Interfaces:**
- Consumes: `read_note`, `split_note`, `join_note`, `fm_get`, `fm_set`.
- Produces:
  - `TOPIC_LINK_RE`
  - `parse_topic_links(raw_value) -> List[str]`
  - `problem_entry(path, fm) -> str` — the markdown list line for a topic's Problems section
  - `scan_problems(problems_root) -> Tuple[Dict[Path, str], Dict[str, List[str]], List[dict]]` — `(rewrites, entries_by_topic_stem, records)`. `records` are dicts with keys `name`, `pattern`, `difficulty`, `solved_on`, `revisit`, `aid`, used by the Task 6 roll-up.

- [ ] **Step 1: Write the failing tests**

Create `Career/Prep/.tools/tests/test_problems.py`:

```python
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import prep_sync


PROBLEM = """---
type: problem
source: leetcode
number: 743
url: https://leetcode.com/problems/network-delay-time/
difficulty: Medium
pattern: WRONG
patterns: [Advanced Graphs]
topics: ["[[Dijkstra's Algorithm]]", "[[Heaps and Priority Queues]]"]
solved_on: 2026-08-20
attempts: 2
aid: hint
revisit: true
time: O(E log V)
space: O(V)
language: python
---

# 743 · Network Delay Time

## Idea

Single-source shortest path from k.
"""


def write_problem(root, pattern, name, text):
    folder = root / pattern
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / (name + ".md")
    path.write_text(text, encoding="utf-8")
    return path


class ParseTopicLinksTest(unittest.TestCase):
    def test_extracts_every_wikilink_target(self):
        # arrange
        raw = '["[[Dijkstra\'s Algorithm]]", "[[Heaps and Priority Queues]]"]'

        # act
        result = prep_sync.parse_topic_links(raw)

        # assert
        self.assertEqual(
            ["Dijkstra's Algorithm", "Heaps and Priority Queues"], result
        )

    def test_strips_a_display_alias(self):
        # arrange
        raw = '["[[Graphs/Dijkstra\'s Algorithm|Dijkstra]]"]'

        # act / assert
        self.assertEqual(
            ["Dijkstra's Algorithm"], prep_sync.parse_topic_links(raw)
        )

    def test_returns_empty_for_an_empty_list(self):
        self.assertEqual([], prep_sync.parse_topic_links("[]"))

    def test_returns_empty_for_a_missing_value(self):
        self.assertEqual([], prep_sync.parse_topic_links(None))


class ScanProblemsTest(unittest.TestCase):
    def test_derives_pattern_from_the_containing_folder(self):
        # arrange
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = write_problem(
                root, "Advanced Graphs", "743 · Network Delay Time", PROBLEM
            )

            # act
            rewrites, _, _ = prep_sync.scan_problems(root)

            # assert
            fm, _ = prep_sync.split_note(path, rewrites[path])
            self.assertEqual("Advanced Graphs", prep_sync.fm_get(fm, "pattern"))

    def test_indexes_the_problem_under_every_topic_it_names(self):
        # arrange
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_problem(
                root, "Advanced Graphs", "743 · Network Delay Time", PROBLEM
            )

            # act
            _, by_topic, _ = prep_sync.scan_problems(root)

            # assert
            self.assertEqual(
                ["- [[743 · Network Delay Time]] · Medium · Advanced Graphs"],
                by_topic["Dijkstra's Algorithm"],
            )
            self.assertIn("Heaps and Priority Queues", by_topic)

    def test_entries_for_one_topic_are_sorted(self):
        # arrange
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            second = PROBLEM.replace("743 · Network Delay Time", "207 · Course Schedule")
            second = second.replace("number: 743", "number: 207")
            write_problem(root, "Advanced Graphs", "743 · Network Delay Time", PROBLEM)
            write_problem(root, "Graphs", "207 · Course Schedule", second)

            # act
            _, by_topic, _ = prep_sync.scan_problems(root)

            # assert
            entries = by_topic["Dijkstra's Algorithm"]
            self.assertEqual(sorted(entries), entries)

    def test_records_carry_the_fields_the_rollup_needs(self):
        # arrange
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_problem(
                root, "Advanced Graphs", "743 · Network Delay Time", PROBLEM
            )

            # act
            _, _, records = prep_sync.scan_problems(root)

            # assert
            self.assertEqual(1, len(records))
            self.assertEqual(
                {
                    "name": "743 · Network Delay Time",
                    "pattern": "Advanced Graphs",
                    "difficulty": "Medium",
                    "solved_on": "2026-08-20",
                    "revisit": True,
                    "aid": "hint",
                },
                records[0],
            )

    def test_ignores_the_folder_note_that_shares_the_folder_name(self):
        # arrange
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            folder = root / "Advanced Graphs"
            folder.mkdir(parents=True)
            (folder / "Advanced Graphs.md").write_text(
                "---\ntype: pattern\n---\n\n# Advanced Graphs\n", encoding="utf-8"
            )
            write_problem(root, "Advanced Graphs", "743 · Network Delay Time", PROBLEM)

            # act
            _, _, records = prep_sync.scan_problems(root)

            # assert
            self.assertEqual(1, len(records))

    def test_raises_naming_the_file_when_difficulty_is_missing(self):
        # arrange
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            broken = PROBLEM.replace("difficulty: Medium\n", "")
            write_problem(root, "Advanced Graphs", "743 · Network Delay Time", broken)

            # act / assert
            with self.assertRaises(prep_sync.PrepError) as caught:
                prep_sync.scan_problems(root)
            self.assertIn("743", str(caught.exception))

    def test_returns_empty_results_when_there_are_no_problems_yet(self):
        # arrange
        with tempfile.TemporaryDirectory() as tmp:
            # act
            rewrites, by_topic, records = prep_sync.scan_problems(Path(tmp))

            # assert
            self.assertEqual(({}, {}, []), (rewrites, by_topic, records))


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run the tests to verify they fail**

```bash
cd "/Users/lukewaehner/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain/Career/Prep/.tools"
python3 -m unittest discover -s tests -v
```

Expected: `AttributeError: module 'prep_sync' has no attribute 'parse_topic_links'`.

- [ ] **Step 3: Write the implementation**

Add the constant below `NO_PROBLEMS`:

```python
TOPIC_LINK_RE = re.compile(r"\[\[([^\]|#]+)")
```

and append to `prep_sync.py`:

```python
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
    return "- [[%s]] · %s · %s" % (path.stem, difficulty, pattern)


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
                "revisit": fm_get(fm, "revisit") == "true",
                "aid": fm_get(fm, "aid"),
            }
        )

    for entries in entries_by_topic.values():
        entries.sort()

    return rewrites, entries_by_topic, records
```

- [ ] **Step 4: Run the tests to verify they pass**

```bash
cd "/Users/lukewaehner/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain/Career/Prep/.tools"
python3 -m unittest discover -s tests -v
```

Expected: `OK`, 41 tests.

- [ ] **Step 5: Commit**

```bash
cd "/Users/lukewaehner/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain"
git add Career/Prep/.tools/
git commit -m "feat(prep): scan problem notes and index them by topic

A problem's folder is the single source of its primary pattern, so moving a
note between folders reclassifies it with no property to remember to edit."
```

---

### Task 6: `prep_sync` — roll-up, CLI, and `--check`

**Files:**
- Modify: `Career/Prep/.tools/prep_sync.py`
- Test: `Career/Prep/.tools/tests/test_sync_run.py`

**Interfaces:**
- Consumes: everything from Tasks 2–5.
- Produces:
  - `progress_bar(done, total, width=24) -> str`
  - `render_rollup(groups, records, today) -> List[str]` — `groups` is `Dict[str, List[Tuple[str, int, int, str]]]` mapping group name to `(note_name, done, total, tier)`
  - `replace_marked_block(lines, block) -> List[str]`
  - `sync(root, today, dry_run) -> List[str]` — returns the relative paths that changed (or would change)
  - `main(argv=None) -> int`
  - Constants `PREP_BEGIN = "<!-- prep:begin -->"`, `PREP_END = "<!-- prep:end -->"`

- [ ] **Step 1: Write the failing tests**

Create `Career/Prep/.tools/tests/test_sync_run.py`:

```python
import datetime
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import prep_sync

TODAY = datetime.date(2026, 9, 1)

TOPIC = """---
type: topic
group: Graphs
tier: core
confidence: 3
---

# Dijkstra's Algorithm

> [!abstract]- Coverage — 0/2
> - [x] [[#Idea]]
> - [ ] [[#Gotchas]]

## Idea

## Problems

_None yet._
"""

HUB = """# Prep

Some hand-written orientation that must survive.

<!-- prep:begin -->
stale content
<!-- prep:end -->

## See Also
"""


def build_vault(tmp):
    root = Path(tmp)
    (root / "topics" / "Graphs").mkdir(parents=True)
    (root / "problems").mkdir(parents=True)
    (root / "meta").mkdir(parents=True)
    (root / "topics" / "Graphs" / "Dijkstra's Algorithm.md").write_text(
        TOPIC, encoding="utf-8"
    )
    (root / "Prep.md").write_text(HUB, encoding="utf-8")
    return root


class ProgressBarTest(unittest.TestCase):
    def test_renders_filled_and_empty_cells(self):
        self.assertEqual("██████░░░░░░", prep_sync.progress_bar(1, 2, width=12))

    def test_zero_total_renders_empty_rather_than_dividing_by_zero(self):
        self.assertEqual("░░░░░░░░░░░░", prep_sync.progress_bar(0, 0, width=12))


class ReplaceMarkedBlockTest(unittest.TestCase):
    def test_replaces_only_between_the_markers(self):
        # arrange
        lines = HUB.split("\n")

        # act
        result = prep_sync.replace_marked_block(lines, ["fresh content"])

        # assert
        text = "\n".join(result)
        self.assertIn("Some hand-written orientation that must survive.", text)
        self.assertIn("fresh content", text)
        self.assertNotIn("stale content", text)
        self.assertIn("## See Also", text)

    def test_raises_when_the_markers_are_missing(self):
        with self.assertRaises(prep_sync.PrepError):
            prep_sync.replace_marked_block(["# Prep"], ["fresh"])


class SyncTest(unittest.TestCase):
    def test_first_run_reports_the_files_it_changed(self):
        # arrange
        with tempfile.TemporaryDirectory() as tmp:
            root = build_vault(tmp)

            # act
            changed = prep_sync.sync(root, TODAY, dry_run=False)

            # assert
            self.assertIn("topics/Graphs/Dijkstra's Algorithm.md", changed)
            self.assertIn("Prep.md", changed)

    def test_second_run_changes_nothing(self):
        # arrange
        with tempfile.TemporaryDirectory() as tmp:
            root = build_vault(tmp)
            prep_sync.sync(root, TODAY, dry_run=False)

            # act
            changed = prep_sync.sync(root, TODAY, dry_run=False)

            # assert
            self.assertEqual([], changed)

    def test_second_run_does_not_touch_file_mtimes(self):
        # arrange
        with tempfile.TemporaryDirectory() as tmp:
            root = build_vault(tmp)
            prep_sync.sync(root, TODAY, dry_run=False)
            note = root / "topics" / "Graphs" / "Dijkstra's Algorithm.md"
            before = note.stat().st_mtime_ns

            # act
            prep_sync.sync(root, TODAY, dry_run=False)

            # assert
            self.assertEqual(before, note.stat().st_mtime_ns)

    def test_dry_run_reports_changes_without_writing(self):
        # arrange
        with tempfile.TemporaryDirectory() as tmp:
            root = build_vault(tmp)
            note = root / "topics" / "Graphs" / "Dijkstra's Algorithm.md"
            before = note.read_text(encoding="utf-8")

            # act
            changed = prep_sync.sync(root, TODAY, dry_run=True)

            # assert
            self.assertNotEqual([], changed)
            self.assertEqual(before, note.read_text(encoding="utf-8"))

    def test_rollup_lands_between_the_markers_in_the_hub(self):
        # arrange
        with tempfile.TemporaryDirectory() as tmp:
            root = build_vault(tmp)

            # act
            prep_sync.sync(root, TODAY, dry_run=False)

            # assert
            hub = (root / "Prep.md").read_text(encoding="utf-8")
            self.assertIn("Some hand-written orientation that must survive.", hub)
            self.assertIn("Graphs", hub)
            self.assertNotIn("stale content", hub)

    def test_meta_notes_are_skipped(self):
        # arrange
        with tempfile.TemporaryDirectory() as tmp:
            root = build_vault(tmp)
            meta = root / "meta" / "Books.md"
            meta.write_text("---\ntype: meta\n---\n\n# Books\n", encoding="utf-8")

            # act
            prep_sync.sync(root, TODAY, dry_run=False)

            # assert
            self.assertEqual(
                "---\ntype: meta\n---\n\n# Books\n", meta.read_text(encoding="utf-8")
            )

    def test_a_topic_note_without_a_coverage_callout_fails_loudly(self):
        # arrange
        with tempfile.TemporaryDirectory() as tmp:
            root = build_vault(tmp)
            broken = root / "topics" / "Graphs" / "Broken.md"
            broken.write_text("---\ntype: topic\n---\n\n# Broken\n", encoding="utf-8")

            # act / assert
            with self.assertRaises(prep_sync.PrepError) as caught:
                prep_sync.sync(root, TODAY, dry_run=False)
            self.assertIn("Broken.md", str(caught.exception))


class MainTest(unittest.TestCase):
    def test_exits_zero_on_a_clean_run(self):
        # arrange
        with tempfile.TemporaryDirectory() as tmp:
            root = build_vault(tmp)
            prep_sync.main([str(root)])

            # act
            code = prep_sync.main([str(root)])

            # assert
            self.assertEqual(0, code)

    def test_check_exits_one_when_something_would_change(self):
        # arrange
        with tempfile.TemporaryDirectory() as tmp:
            root = build_vault(tmp)

            # act
            code = prep_sync.main([str(root), "--check"])

            # assert
            self.assertEqual(1, code)

    def test_exits_two_on_a_malformed_note(self):
        # arrange
        with tempfile.TemporaryDirectory() as tmp:
            root = build_vault(tmp)
            (root / "topics" / "Graphs" / "Broken.md").write_text(
                "---\ntype: topic\n---\n\n# Broken\n", encoding="utf-8"
            )

            # act
            code = prep_sync.main([str(root)])

            # assert
            self.assertEqual(2, code)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run the tests to verify they fail**

```bash
cd "/Users/lukewaehner/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain/Career/Prep/.tools"
python3 -m unittest discover -s tests -v
```

Expected: `AttributeError: module 'prep_sync' has no attribute 'progress_bar'`.

- [ ] **Step 3: Write the implementation**

Add these imports at the top of `prep_sync.py`, after the docstring:

```python
import argparse
import datetime
import re
import sys
from collections import Counter, OrderedDict
from pathlib import Path
```

(remove the now-duplicated bare `import re`.)

Add the constants below `TOPIC_LINK_RE`:

```python
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
```

and append:

```python
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


def render_rollup(groups, records, today):
    """Build the generated section of Prep.md.

    *groups* maps a group name to a list of (note_name, done, total, tier).
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
            "| [[%s]] | `%s` | %d/%d | %d |"
            % (name, progress_bar(done, total, width=16), done, total, len(rows))
        )

    weakest = sorted(
        (row for rows in groups.values() for row in rows if row[3] == "core"),
        key=lambda row: (float(row[1]) / row[2], row[0]),
    )[:5]
    out += ["", "## Weakest topics", ""]
    for name, done, total, _ in weakest:
        out.append("- [[%s]] — %d/%d" % (name, done, total))

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
            out.append("| [[%s]] | %d |" % (pattern, by_pattern[pattern]))

        revisit = sorted(
            (r for r in records if r["revisit"] or r["aid"] != "unaided"),
            key=lambda r: r["name"],
        )
        if revisit:
            out += ["", "## Needs revisit", ""]
            for record in revisit:
                out.append(
                    "- [[%s]] — %s" % (record["name"], record["aid"])
                )

    out += ["", "_Generated by `prep_sync.py` on %s._" % today.isoformat(), ""]
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
        tier = fm_get(fm, "tier") or "core"
        groups.setdefault(group, []).append((path.stem, done, total, tier))

    hub = root / "Prep.md"
    if hub.is_file():
        old_text, crlf = read_note(hub)
        new_text = "\n".join(
            replace_marked_block(
                old_text.split("\n"), render_rollup(groups, records, today)
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
```

- [ ] **Step 4: Run the tests to verify they pass**

```bash
cd "/Users/lukewaehner/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain/Career/Prep/.tools"
python3 -m unittest discover -s tests -v
```

Expected: `OK`, 55 tests.

- [ ] **Step 5: Make the script executable and commit**

```bash
cd "/Users/lukewaehner/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain"
chmod +x Career/Prep/.tools/prep_sync.py
git add Career/Prep/.tools/
git commit -m "feat(prep): add the sync CLI, roll-up rendering, and --check mode

Exit codes separate the two failure modes a watcher cares about: 1 means
the tree drifted, 2 means a note is malformed and needs a human."
```

---

### Task 7: Link checker

The migration rewrites 840 wikilinks. Verifying they all resolve is the gate on Task 12, so the checker has to exist first.

**Files:**
- Create: `Career/Prep/.tools/check_links.py`
- Test: `Career/Prep/.tools/tests/test_check_links.py`

**Interfaces:**
- Consumes: nothing.
- Produces:
  - `iter_links(text) -> Iterator[str]` — wikilink targets, aliases and heading anchors stripped
  - `build_index(vault_root) -> Set[str]` — every resolvable target: note stems and vault-relative paths without `.md`
  - `check(vault_root, scope) -> List[Tuple[str, str]]` — `(source_relative_path, unresolved_target)`
  - `main(argv=None) -> int`

- [ ] **Step 1: Write the failing tests**

Create `Career/Prep/.tools/tests/test_check_links.py`:

```python
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import check_links


class IterLinksTest(unittest.TestCase):
    def test_yields_a_plain_target(self):
        self.assertEqual(["Arrays"], list(check_links.iter_links("see [[Arrays]]")))

    def test_strips_a_display_alias(self):
        self.assertEqual(
            ["Career/Prep/topics/Graphs/Dijkstra's Algorithm"],
            list(check_links.iter_links("[[Career/Prep/topics/Graphs/Dijkstra's Algorithm|Dijkstra]]")),
        )

    def test_strips_a_heading_anchor(self):
        self.assertEqual(
            ["Hashtable"], list(check_links.iter_links("[[Hashtable#Hash Function]]"))
        )

    def test_skips_a_bare_intra_note_anchor(self):
        self.assertEqual([], list(check_links.iter_links("[[#Idea]]")))

    def test_ignores_an_embedded_image(self):
        self.assertEqual([], list(check_links.iter_links("![[diagram.png]]")))


class CheckTest(unittest.TestCase):
    def test_reports_nothing_when_every_link_resolves(self):
        # arrange
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "Career" / "Prep").mkdir(parents=True)
            (root / "Career" / "Prep" / "Arrays.md").write_text("# Arrays\n", encoding="utf-8")
            (root / "Career" / "Prep" / "Hub.md").write_text("[[Arrays]]\n", encoding="utf-8")

            # act
            broken = check_links.check(root, "Career/Prep")

            # assert
            self.assertEqual([], broken)

    def test_reports_the_source_and_target_of_a_broken_link(self):
        # arrange
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "Career" / "Prep").mkdir(parents=True)
            (root / "Career" / "Prep" / "Hub.md").write_text("[[Nope]]\n", encoding="utf-8")

            # act
            broken = check_links.check(root, "Career/Prep")

            # assert
            self.assertEqual([("Career/Prep/Hub.md", "Nope")], broken)

    def test_resolves_a_full_vault_relative_path(self):
        # arrange
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "Career" / "Prep" / "topics").mkdir(parents=True)
            (root / "Career" / "Prep" / "topics" / "Arrays.md").write_text("x", encoding="utf-8")
            (root / "Career" / "Prep" / "Hub.md").write_text(
                "[[Career/Prep/topics/Arrays]]\n", encoding="utf-8"
            )

            # act / assert
            self.assertEqual([], check_links.check(root, "Career/Prep"))

    def test_resolves_a_target_outside_the_scanned_scope(self):
        # arrange
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "Code" / "Algorithms").mkdir(parents=True)
            (root / "Code" / "Algorithms" / "DSA.md").write_text("x", encoding="utf-8")
            (root / "Career" / "Prep").mkdir(parents=True)
            (root / "Career" / "Prep" / "Hub.md").write_text("[[DSA]]\n", encoding="utf-8")

            # act / assert
            self.assertEqual([], check_links.check(root, "Career/Prep"))


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run the tests to verify they fail**

```bash
cd "/Users/lukewaehner/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain/Career/Prep/.tools"
python3 -m unittest discover -s tests -v
```

Expected: `ModuleNotFoundError: No module named 'check_links'`.

- [ ] **Step 3: Write the implementation**

Create `Career/Prep/.tools/check_links.py`:

```python
#!/usr/bin/env python3
"""Report wikilinks under a vault subtree that do not resolve to a note.

The prep migration rewrites hundreds of links at once. Obsidian will happily
render a dead link forever, so this runs as a gate rather than being noticed
later.
"""

import argparse
import re
import sys
from pathlib import Path

LINK_RE = re.compile(r"(?<!!)\[\[([^\]]+)\]\]")
SKIP_DIRS = {".git", ".obsidian", ".trash", ".tools", ".strip_title_backups"}


def iter_links(text):
    """Yield wikilink targets, with aliases and heading anchors removed.

    Embeds (![[...]]) and bare intra-note anchors ([[#Heading]]) are skipped:
    the first are attachments, the second always resolve to the current note.
    """
    for match in LINK_RE.finditer(text):
        target = match.group(1).split("|", 1)[0].split("#", 1)[0].strip()
        if target:
            yield target


def build_index(vault_root):
    """Collect every string Obsidian would resolve to a note.

    Both the bare stem ('Arrays') and the vault-relative path without its
    extension ('Career/Prep/topics/Data Structures/Arrays') are indexed,
    because the vault uses both link styles.
    """
    index = set()
    for path in vault_root.rglob("*.md"):
        if SKIP_DIRS & set(path.relative_to(vault_root).parts):
            continue
        index.add(path.stem)
        index.add(str(path.relative_to(vault_root).with_suffix("")))
    return index


def check(vault_root, scope):
    """Return [(source_relative_path, unresolved_target)] for notes under *scope*."""
    vault_root = Path(vault_root)
    index = build_index(vault_root)

    broken = []
    for path in sorted((vault_root / scope).rglob("*.md")):
        if SKIP_DIRS & set(path.relative_to(vault_root).parts):
            continue
        text = path.read_text(encoding="utf-8")
        for target in iter_links(text):
            if target not in index:
                broken.append((str(path.relative_to(vault_root)), target))
    return broken


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("vault", help="vault root")
    parser.add_argument(
        "--scope", default="Career/Prep", help="subtree to scan (default: Career/Prep)"
    )
    args = parser.parse_args(argv)

    broken = check(Path(args.vault), args.scope)
    if not broken:
        sys.stdout.write("check_links: all links resolve\n")
        return 0

    sys.stderr.write("check_links: %d unresolved link(s)\n" % len(broken))
    for source, target in broken:
        sys.stderr.write("  %s -> [[%s]]\n" % (source, target))
    return 1


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 4: Run the tests to verify they pass**

```bash
cd "/Users/lukewaehner/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain/Career/Prep/.tools"
python3 -m unittest discover -s tests -v
```

Expected: `OK`, 64 tests.

- [ ] **Step 5: Record the pre-migration baseline**

```bash
cd "/Users/lukewaehner/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain"
python3 Career/Prep/.tools/check_links.py . --scope Career/Prep 2>&1 | tail -20
```

Expected: some number of unresolved links in the *old* tree. Write that number down — Task 12 requires the new tree to reach zero, and knowing the starting point tells you whether a failure is pre-existing or newly introduced.

- [ ] **Step 6: Commit**

```bash
git add Career/Prep/.tools/
git commit -m "feat(prep): add a wikilink resolution checker

Gates the migration. Obsidian renders dead links silently, so rewriting 840
of them needs a check that fails rather than a spot inspection."
```

---

### Task 8: New tree skeleton, templates, and meta notes

**Files:**
- Create: `Career/Prep/topics/<Group>/` × 10, each with a folder note `<Group>.md`
- Create: `Career/Prep/problems/<Pattern>/` × 18, each with a folder note `<Pattern>.md`
- Create: `Career/Prep/meta/` with the 8 notes from the spec's meta manifest
- Create: `templates/Prep Topic.md`, `templates/Prep Problem.md`

**Interfaces:**
- Consumes: the group and pattern name lists from Global Constraints.
- Produces: the directory layout Tasks 9–11 write into, and the two templates every note in them follows.

- [ ] **Step 1: Create the directories**

```bash
cd "/Users/lukewaehner/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain/Career/Prep"
for g in "Complexity" "Data Structures" "Trees" "Graphs" "Sorting & Searching" \
         "Algorithm Design" "Strings" "Math & Bits" "Systems" "Design"; do
  mkdir -p "topics/$g"
done
for p in "Arrays & Hashing" "Two Pointers" "Sliding Window" "Stack" "Binary Search" \
         "Linked List" "Trees" "Tries" "Heap & Priority Queue" "Backtracking" \
         "Graphs" "Advanced Graphs" "1-D DP" "2-D DP" "Greedy" "Intervals" \
         "Math & Geometry" "Bit Manipulation"; do
  mkdir -p "problems/$p"
done
mkdir -p meta
ls topics problems
```

Expected: 10 topic directories and 18 problem directories.

- [ ] **Step 2: Write the topic template**

Create `templates/Prep Topic.md`:

```markdown
---
type: topic
group:
tier: core
confidence:
---

# {{title}}

> [!abstract]- Coverage — 0/6
> - [ ] [[#Idea]]
> - [ ] [[#How it works]]
> - [ ] [[#Implementation]]
> - [ ] [[#Complexity]]
> - [ ] [[#When to use it]]
> - [ ] [[#Gotchas]]

## Idea

## How it works

## Implementation

## Complexity

## When to use it

## Gotchas

## Resources

## Problems

_None yet._
```

- [ ] **Step 3: Write the problem template**

Create `templates/Prep Problem.md`:

```markdown
---
type: problem
source: leetcode
number:
url:
difficulty:
pattern:
patterns: []
topics: []
solved_on:
attempts: 1
aid: unaided
revisit: false
time:
space:
language: python
---

# {{title}}

> [!question]- Problem

## Idea

## Naive

## Optimal

## Why it works

## Template

## Mistakes I made

## Related
```

- [ ] **Step 4: Write the ten topic folder notes**

Each `topics/<Group>/<Group>.md` follows this shape. Written out for `Graphs`; produce the other nine identically with the group name substituted in all four places.

````markdown
---
type: group
group: Graphs
---

# Graphs

```base
filters:
  and:
    - 'type == "topic"'
    - 'group == "Graphs"'
views:
  - type: table
    name: Progress
    order:
      - file.name
      - tier
      - status
      - coverage
      - confidence
      - updated
    groupBy:
      property: tier
      direction: ASC
```

← [[Prep]]
````

- [ ] **Step 5: Write the eighteen problem folder notes**

Each `problems/<Pattern>/<Pattern>.md`, written out for `Two Pointers`; produce the other seventeen identically.

````markdown
---
type: pattern
pattern: Two Pointers
---

# Two Pointers

```base
filters:
  and:
    - 'type == "problem"'
    - 'patterns.contains("Two Pointers")'
views:
  - type: table
    name: Problems
    order:
      - number
      - file.name
      - difficulty
      - time
      - space
      - aid
      - solved_on
      - revisit
```

← [[Prep]]
````

Note the filter uses `patterns.contains(...)`, not `pattern ==`, so a problem filed under another folder that also carries this pattern shows up here.

- [ ] **Step 6: Write the eight meta notes**

Per the spec's meta manifest. Each carries `type: meta` and **no Coverage callout** — `prep_sync` skips anything whose `type` is not `topic`. Merge the source notes' content under `##` headings named after the notes they came from. For example `meta/Books.md`:

```markdown
---
type: meta
---

# Books

## Interview Prep Books

<!-- content from topics/02 Books/Interview Prep Books.md -->

## Books for Data Structures and Algorithms

<!-- content from topics/02 Books/Books for Data Structures and Algorithms.md -->

## Additional Books

<!-- content from topics/02 Books/Additional Books.md -->

← [[Prep]]
```

Replace each `<!-- content from ... -->` with the actual body of that source note, headings demoted one level. The eight notes and their sources are in the spec's meta manifest table.

- [ ] **Step 7: Verify the skeleton**

```bash
cd "/Users/lukewaehner/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain/Career/Prep"
# Scoped to the ten new groups by name: the old numbered directories are
# still present alongside them until Task 12, so a bare topics/*/ count
# would legitimately read 20, not 10.
for g in "Complexity" "Data Structures" "Trees" "Graphs" "Sorting & Searching" \
         "Algorithm Design" "Strings" "Math & Bits" "Systems" "Design"; do
  test -f "topics/$g/$g.md" || echo "MISSING topics/$g/$g.md"
done; echo "topic folder notes checked"
test $(ls -d problems/*/ | wc -l) -eq 18 && echo "problems ok"
test $(ls problems/*/*.md | wc -l) -eq 18 && echo "problem folder notes ok"
test $(ls meta/*.md | wc -l) -eq 8 && echo "meta ok"
```

Expected: all five lines print.

- [ ] **Step 8: Commit**

```bash
cd "/Users/lukewaehner/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain"
git add Career/Prep/topics Career/Prep/problems Career/Prep/meta templates/
git commit -m "feat(prep): add the topic and problem tree skeleton with templates

Group and pattern folder notes each embed their own slice of the databases,
so the file explorer and the database views are the same navigation."
```

---

### Task 9: Migrate Complexity, Data Structures, and Trees

**Ask the user to confirm Obsidian is closed on their iPad before starting.**

**Files:**
- Create: 27 notes — `topics/Complexity/` (4), `topics/Data Structures/` (17), `topics/Trees/` (6)
- Read: the sources named in the spec's manifest for those three groups

**Interfaces:**
- Consumes: `templates/Prep Topic.md` from Task 8.
- Produces: 27 topic notes conforming to the topic note contract, ready for `prep_sync`.

- [ ] **Step 1: Port the notes**

For each row in the spec's Complexity, Data Structures, and Trees manifest tables, create the destination note from `templates/Prep Topic.md` and fill it:

- `group:` the group name. `tier:` from the manifest. Leave `confidence:` empty.
- Move the source note's explanatory prose into `## Idea` / `## How it works`.
- Move any code into `## Implementation`. `Data Structures/Arrays.md` takes the full `Vector` class from `work/06 Data Structures/Arrays.md`; `Data Structures/Hash Tables.md` takes the `> [!warning] Open defect in [[Hashtable]]` callout verbatim into `## Gotchas`.
- Move complexity claims into `## Complexity`.
- Move every external link from the source into `## Resources`.
- Add extra Coverage items and matching `##` sections where the manifest's source has a distinct concept todo: `Arrays` gets `## Implement a vector`; `Hash Tables` gets `## Distributed hash tables`.
- **Tick a Coverage box only where the source had `[x]`.** Existing progress carries over; nothing is invented and nothing is reset.
- Keep every `[[...]]` link to `Code/Algorithms/*` working — those notes are not moving.

- [ ] **Step 2: Verify the count and that every note parses**

```bash
cd "/Users/lukewaehner/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain/Career/Prep"
test $(ls topics/Complexity/*.md | wc -l) -eq 5 && echo "Complexity ok (4 + folder note)"
test $(ls "topics/Data Structures"/*.md | wc -l) -eq 18 && echo "Data Structures ok"
test $(ls topics/Trees/*.md | wc -l) -eq 7 && echo "Trees ok"
python3 .tools/prep_sync.py . --check
```

Expected: three `ok` lines, and `prep_sync` exits 1 listing the new notes as "would update" — with **no** `PrepError`. A `PrepError` means a note is missing its Coverage callout or its frontmatter; fix it before moving on.

- [ ] **Step 3: Commit**

```bash
cd "/Users/lukewaehner/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain"
git add Career/Prep/topics
git commit -m "refactor(prep): port Complexity, Data Structures, and Trees to topic notes

Content only -- the old trees stay in place until the cutover so the two can
be diffed."
```

---

### Task 10: Migrate Graphs, Sorting & Searching, and Algorithm Design

**Files:**
- Create: 28 notes — `topics/Graphs/` (12), `topics/Sorting & Searching/` (10), `topics/Algorithm Design/` (6)

**Interfaces:**
- Consumes: `templates/Prep Topic.md`.
- Produces: 28 topic notes conforming to the topic note contract.

- [ ] **Step 1: Port the notes**

Same procedure as Task 9 Step 1, against the spec's Graphs, Sorting & Searching, and Algorithm Design manifest tables. Specific to these groups:

- `topics/10 Graphs.md` and `topics/09 Sorting.md` are single link-dump notes covering a dozen concepts each. Split their links across the destination notes by subject — Sedgewick's mergesort videos go to `Merge Sort`, the MIT Dijkstra lecture goes to `Dijkstra's Algorithm`, and so on. A link that genuinely spans the group goes in the group folder note's body above the embedded base.
- The `~ coursework` items in the old `Prep.md` correspond to `Code/Algorithms/` notes. Link them from `## Implementation` rather than copying: `Depth First Search`, `Dijkstra's Algorithm`, `Bellman-Ford Algorithm`, `Topological Ordering`, `Divide and Conquer`, `Order Statistics`, `Recurrences`, `Master Theorem`, and the `Sorts`, `Graphs`, `Greedy`, `Dynamic Programming`, `Binary Search`, `Binary Search Trees` folders.
- `Binary Search` takes its content from both `topics/07 More Knowledge/Binary search.md` and `work/07 More Knowledge/Binary search.md`.
- `Dynamic Programming` merges three sources: `topics/11 …/Dynamic Programming.md`, `topics/16 …/More Dynamic Programming.md`, and `work/11 …/Dynamic Programming.md`.

- [ ] **Step 2: Verify**

```bash
cd "/Users/lukewaehner/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain/Career/Prep"
test $(ls topics/Graphs/*.md | wc -l) -eq 13 && echo "Graphs ok"
test $(ls "topics/Sorting & Searching"/*.md | wc -l) -eq 11 && echo "Sorting ok"
test $(ls "topics/Algorithm Design"/*.md | wc -l) -eq 7 && echo "Algorithm Design ok"
python3 .tools/prep_sync.py . --check
```

Expected: three `ok` lines, no `PrepError`.

- [ ] **Step 3: Commit**

```bash
cd "/Users/lukewaehner/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain"
git add Career/Prep/topics
git commit -m "refactor(prep): port Graphs, Sorting, and Algorithm Design to topic notes"
```

---

### Task 11: Migrate Strings, Math & Bits, Systems, and Design

**Files:**
- Create: 40 notes — `topics/Strings/` (5), `topics/Math & Bits/` (9), `topics/Systems/` (15), `topics/Design/` (11)

**Interfaces:**
- Consumes: `templates/Prep Topic.md`.
- Produces: 40 topic notes conforming to the topic note contract. With Tasks 9 and 10 this completes all 95.

- [ ] **Step 1: Port the notes**

Same procedure as Task 9 Step 1, against the spec's Strings, Math & Bits, Systems, and Design manifest tables. Specific to these groups:

- `topics/11 …/Caches.md` splits in two: the hardware and cache-line material goes to `Systems/Caches`, the LRU cache implementation goes to `Data Structures/LRU Cache` (created in Task 9 — append to it rather than creating a second note).
- `topics/15 …/Information theory.md` and `topics/15 …/Entropy.md` merge into one note, `Math & Bits/Information Theory and Entropy`.
- `topics/14 System Design.md` is a very large link dump. Split it across the six `Design/` notes sourced from it. The "Practicing the system design process" exercise list goes into `Design/System Design` under `## When to use it`.
- `topics/16 …/String Matching.md` splits across `Knuth-Morris-Pratt`, `Rabin-Karp`, and `Boyer-Moore`.

- [ ] **Step 2: Verify the complete tree**

```bash
cd "/Users/lukewaehner/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain/Career/Prep"
python3 - <<'PY'
from pathlib import Path

GROUPS = [
    "Complexity", "Data Structures", "Trees", "Graphs", "Sorting & Searching",
    "Algorithm Design", "Strings", "Math & Bits", "Systems", "Design",
]

# Scoped to the ten new groups by name. The old numbered directories still sit
# in topics/ until Task 12, so an unscoped glob would both inflate the count
# and flag old notes for lacking a Coverage callout they never had.
notes, missing = [], []
for group in GROUPS:
    for path in sorted(Path("topics", group).glob("*.md")):
        if path.stem == path.parent.name:
            continue
        notes.append(path)
        if "Coverage —" not in path.read_text(encoding="utf-8"):
            missing.append(str(path))

print("topic notes: %d (expect 95)" % len(notes))
print("\n".join(missing) if missing else "every topic note has a Coverage callout")
PY
python3 .tools/prep_sync.py . --check
```

Expected: the count line prints, the grep reports no missing callouts, and `prep_sync --check` exits 1 with no `PrepError`.

- [ ] **Step 3: Commit**

```bash
cd "/Users/lukewaehner/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain"
git add Career/Prep/topics
git commit -m "refactor(prep): port Strings, Math, Systems, and Design to topic notes

Completes the 95-note manifest. The old trees are removed at cutover."
```

---

### Task 12: Cut over — rewrite inbound links and delete the old trees

**Files:**
- Modify: `Career/Career.md`, and any note outside `Career/Prep/` linking into it
- Delete: `Career/Prep/topics/00 …` through `17 …` (the old numbered directories and notes), `Career/Prep/work/`, `Career/Prep/topics 2/`, `Career/Prep/work 2/`

**Interfaces:**
- Consumes: `check_links.py` from Task 7, the new tree from Tasks 8–11.
- Produces: a tree with zero unresolved links and no old-structure remnants.

- [ ] **Step 1: Find every inbound reference from outside the new tree**

```bash
cd "/Users/lukewaehner/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain"
grep -rn "Career/Prep/\(work\|topics/[0-9]\)" --include="*.md" . \
  | grep -v "^./Career/Prep/topics/[0-9]" \
  | grep -v "^./Career/Prep/work/" \
  | grep -v "^./Career/Prep/.tools/"
```

Expected: a short list, including `Career/Career.md`. Rewrite each link to its new destination using the spec's manifest.

- [ ] **Step 2: Delete the old trees**

```bash
cd "/Users/lukewaehner/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain/Career/Prep"
ls -d "topics 2" "work 2" 2>/dev/null && find "topics 2" "work 2" -type f | head
```

Expected: both directories listed, `find` prints nothing — they are the empty iCloud conflict directories. If either contains files, stop and show them to the user before deleting.

```bash
git rm -r --quiet topics/0* topics/1* work
rm -rf "topics 2" "work 2"
ls topics
```

Expected: only the ten new group directories remain.

- [ ] **Step 3: Run the link checker — this is the gate**

```bash
cd "/Users/lukewaehner/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain"
python3 Career/Prep/.tools/check_links.py . --scope Career/Prep
```

Expected: `check_links: all links resolve`, exit 0. Any unresolved link must be fixed here, not deferred.

- [ ] **Step 4: Check nothing elsewhere in the vault now points at a deleted note**

```bash
python3 Career/Prep/.tools/check_links.py . --scope Career
python3 Career/Prep/.tools/check_links.py . --scope Code
```

Expected: any failures name only links that were already broken before the migration — compare against the Task 7 Step 5 baseline. Fix anything the migration introduced.

- [ ] **Step 5: Commit**

```bash
git add -A -- Career
git commit -m "refactor(prep)!: remove the topics/work split

BREAKING CHANGE: every note under Career/Prep/topics/NN * and
Career/Prep/work/ has moved. Inbound links from Career.md are rewritten;
Code/Algorithms/ is untouched and still linked from the new topic notes.

Also removes the empty 'topics 2' and 'work 2' iCloud conflict directories."
```

---

### Task 13: The two Bases

**Files:**
- Create: `Career/Prep/Topics.base`
- Create: `Career/Prep/Problems.base`

**Interfaces:**
- Consumes: the frontmatter contract from the spec, populated by Tasks 9–11.
- Produces: the two databases the folder notes and `Prep.md` embed.

- [ ] **Step 1: Run a real sync so the Bases have data to read**

```bash
cd "/Users/lukewaehner/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain/Career/Prep"
python3 .tools/prep_sync.py .
python3 .tools/prep_sync.py . --check
```

Expected: the first run reports the files it updated; the second prints `prep_sync: up to date` and exits 0. If the second run reports changes, the script is not idempotent — fix that before continuing.

- [ ] **Step 2: Write `Topics.base`**

```yaml
filters:
  and:
    - 'type == "topic"'
formulas:
  progress: 'if(sections_total, (coverage * 100).toFixed(0) + "%", "")'
properties:
  file.name:
    displayName: Topic
  formula.progress:
    displayName: Progress
  sections_done:
    displayName: Done
  sections_total:
    displayName: Of
views:
  - type: table
    name: Core progress
    filters:
      and:
        - 'tier == "core"'
    groupBy:
      property: group
      direction: ASC
    order:
      - file.name
      - status
      - formula.progress
      - sections_done
      - sections_total
      - confidence
      - updated
    sort:
      - property: coverage
        direction: ASC
  - type: table
    name: Extras
    filters:
      and:
        - 'tier == "extra"'
    groupBy:
      property: group
      direction: ASC
    order:
      - file.name
      - status
      - formula.progress
      - confidence
      - updated
  - type: table
    name: Needs review
    filters:
      or:
        - 'confidence <= 2'
        - and:
            - 'status == "solid"'
            - 'updated < (today() - duration("30d"))'
    order:
      - file.name
      - group
      - confidence
      - updated
    sort:
      - property: confidence
        direction: ASC
  - type: table
    name: Recently touched
    limit: 20
    order:
      - file.name
      - group
      - status
      - formula.progress
      - updated
    sort:
      - property: updated
        direction: DESC
```

- [ ] **Step 3: Write `Problems.base`**

```yaml
filters:
  and:
    - 'type == "problem"'
properties:
  file.name:
    displayName: Problem
  solved_on:
    displayName: Solved
  aid:
    displayName: Aid
views:
  - type: table
    name: All
    order:
      - number
      - file.name
      - difficulty
      - pattern
      - time
      - space
      - aid
      - attempts
      - solved_on
      - revisit
    sort:
      - property: solved_on
        direction: DESC
  - type: table
    name: By pattern
    groupBy:
      property: pattern
      direction: ASC
    order:
      - number
      - file.name
      - difficulty
      - time
      - aid
      - solved_on
  - type: table
    name: Needs revisit
    filters:
      or:
        - 'revisit'
        - 'aid != "unaided"'
    order:
      - number
      - file.name
      - difficulty
      - pattern
      - aid
      - attempts
      - solved_on
  - type: table
    name: By difficulty
    groupBy:
      property: difficulty
      direction: ASC
    order:
      - number
      - file.name
      - pattern
      - time
      - solved_on
  - type: table
    name: Recent
    limit: 25
    order:
      - number
      - file.name
      - difficulty
      - pattern
      - solved_on
    sort:
      - property: solved_on
        direction: DESC
```

- [ ] **Step 4: Verify both Bases load in Obsidian**

Open the vault, open `Topics.base` and `Problems.base`, and click through every view.

Expected: all four Topics views and all five Problems views render. `Core progress` shows ten groups; `Problems` views are empty (no problems logged yet) but must not error.

If Obsidian reports a syntax error on a `sort:` block, that key is not supported in this build — delete the `sort:` blocks, set the sort order once through each view's UI, and let Bases write it back into the file itself. Then re-check that all views render.

- [ ] **Step 5: Verify the folder-note embeds render**

Open `topics/Graphs/Graphs.md` and `problems/Two Pointers/Two Pointers.md`.

Expected: the embedded base tables render inline. The Graphs one lists twelve topics; Two Pointers is empty but does not error.

- [ ] **Step 6: Commit**

```bash
cd "/Users/lukewaehner/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain"
git add Career/Prep
git commit -m "feat(prep): add the Topics and Problems databases

Every column is either hand-set (confidence, revisit) or written by
prep_sync. Bases computes nothing, so a view can never disagree with a note."
```

---

### Task 14: The `Prep.md` hub

**Files:**
- Modify: `Career/Prep/Prep.md` (replace wholesale)

**Interfaces:**
- Consumes: `PREP_BEGIN` / `PREP_END` markers required by `prep_sync.replace_marked_block`.
- Produces: the vault's entry point into the prep system.

- [ ] **Step 1: Replace `Prep.md`**

The hand-written frame; everything between the markers is regenerated and must not be edited by hand.

```markdown
---
tags:
  - career
  - interview-prep
  - study-plan
type: moc
source: coding-interview-university
---

# Prep

Technical interview prep. Study plan adapted from
[Coding Interview University](https://github.com/jwasham/coding-interview-university)
(CC-BY-SA-4.0), plus my own notes.

## How this works

- **`topics/`** — one note per idea, grouped ten ways. Each opens with a Coverage
  checklist; tick an item when you have written that section. That is the only
  progress input in the system.
- **`problems/`** — one note per solved problem, filed under its primary pattern.
- **`meta/`** — process notes. Not counted in any progress number.
- **[[Topics]]** and **[[Problems]]** — the databases. `confidence` and `revisit`
  are editable straight from the table; everything else is derived.

Every number below is generated by `.tools/prep_sync.py` from the notes
themselves. Do not edit between the markers.

<!-- prep:begin -->
<!-- prep:end -->

## Groups

- [[Complexity]] · [[Data Structures]] · [[Trees]] · [[Graphs]] · [[Sorting & Searching]]
- [[Algorithm Design]] · [[Strings]] · [[Math & Bits]] · [[Systems]] · [[Design]]

## See Also

- [[Career]] — job search hub
- [[Algorithms]] — coursework notes, linked from the topic notes above
```

- [ ] **Step 2: Populate the generated block**

```bash
cd "/Users/lukewaehner/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain/Career/Prep"
python3 .tools/prep_sync.py .
sed -n '/prep:begin/,/prep:end/p' Prep.md
```

Expected: a progress bar, a ten-row group table, a five-item weakest-topics list, and `None logged yet.` under Problems.

- [ ] **Step 3: Confirm the hand-written frame survived and links resolve**

```bash
cd "/Users/lukewaehner/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain"
grep -c "How this works" Career/Prep/Prep.md
python3 Career/Prep/.tools/check_links.py . --scope Career/Prep
```

Expected: `1`, then `check_links: all links resolve`.

- [ ] **Step 4: Commit**

```bash
git add Career/Prep/Prep.md
git commit -m "feat(prep): rebuild the hub around generated progress

The old table was hand-maintained and had drifted. Everything numeric now
sits between markers that prep_sync owns."
```

---

### Task 15: Agent commands

**Files:**
- Create: `.claude/commands/prep/drop.md`, `review.md`, `next.md`, `status.md`, `sync.md`

**Interfaces:**
- Consumes: `prep_sync.py`, the note contracts, the folder layout.
- Produces: `/prep:drop`, `/prep:review`, `/prep:next`, `/prep:status`, `/prep:sync`.

- [ ] **Step 1: Write `sync.md`**

```markdown
---
description: Rebuild all derived prep data from the notes
---

Run the prep sync script and report what changed.

!`python3 "Career/Prep/.tools/prep_sync.py" "Career/Prep"`

If the script exits 2, it printed the offending file. Open that note, fix the
malformed frontmatter or missing Coverage callout, and run again. Do not work
around it by editing the script.
```

- [ ] **Step 2: Write `status.md`**

```markdown
---
description: Report prep progress
---

!`python3 "Career/Prep/.tools/prep_sync.py" "Career/Prep"`

Read `Career/Prep/Prep.md` and report, in this order:

1. Overall core coverage, as sections done over total.
2. The three strongest and three weakest groups.
3. Any topic with `confidence` of 1 or 2.
4. Problems solved in the last 14 days, and any flagged `revisit`.
5. One sentence on what has moved since the previous `updated` dates suggest.

Keep it under fifteen lines. Do not pad it with encouragement.
```

- [ ] **Step 3: Write `next.md`**

```markdown
---
description: Recommend what to study next
---

!`python3 "Career/Prep/.tools/prep_sync.py" "Career/Prep"`

Read `Career/Prep/Prep.md`, then recommend exactly one topic and two problems.

Choose the topic by, in priority order:
1. A `core` topic in a group whose coverage is furthest behind the others.
2. Among those, the one with the lowest coverage.
3. Break ties toward whatever the topic notes name as a prerequisite for
   something already in progress.

Choose the problems from patterns with the fewest solved notes under
`Career/Prep/problems/`, preferring ones whose `topics` property names the
topic you picked. Give the LeetCode number and title.

Say why in one sentence each. Do not produce a study plan or a schedule.
```

- [ ] **Step 4: Write `drop.md`**

```markdown
---
description: Turn pasted solutions into problem notes
argument-hint: "[paste solutions, or a path to a file of them]"
---

The user has pasted one or more solved problems: $ARGUMENTS

For each one, create a note at
`Career/Prep/problems/<Primary Pattern>/<number> · <Title>.md` from
`templates/Prep Problem.md`. The middot is U+00B7.

Rules:

- **Primary pattern** is the folder. Pick from the eighteen under
  `Career/Prep/problems/`. Put every applicable pattern in `patterns`,
  including the primary one.
- **Transcribe the user's code verbatim** under `## Optimal`, or under
  `## Naive` if that is what it is. It is the record of what they actually
  wrote. Do not tidy it, rename their variables, or fix it in place.
- If the code has a bug, is asymptotically worse than the standard solution,
  or misses an edge case, add a callout naming the defect and the fix:

  > [!warning] Defect
  > What is wrong, when it fails, and the corrected line.

  Follow it with the standard solution under `## Optimal` if the user's was
  the naive one. Never silently replace their code.
- `time` and `space` describe the user's solution, not the ideal one.
- `topics` links the topic notes the problem exercises, by note name.
- `aid`: `unaided` unless the user says they used a hint or looked at a
  solution. Ask if they did not say. Do not assume `unaided`.
- `solved_on`: today unless they say otherwise. `attempts`: 1 unless they say.
- `## Idea` is one sentence — the observation that makes the solution obvious.
- `## Mistakes I made` records what they got wrong. Leave it out if there was
  nothing.

Then run:

!`python3 "Career/Prep/.tools/prep_sync.py" "Career/Prep"`

and report the notes created and which topics now list them.
```

- [ ] **Step 5: Write `review.md`**

```markdown
---
description: Quiz on weak topics and update confidence
argument-hint: "[optional topic or group name]"
---

!`python3 "Career/Prep/.tools/prep_sync.py" "Career/Prep"`

Scope: $ARGUMENTS — if empty, pick from the weakest topics in
`Career/Prep/Prep.md` and anything flagged `revisit` under
`Career/Prep/problems/`.

Run a spoken-interview review, not a quiz show:

1. Pick one topic. Read its note first — quiz what they wrote, so a gap in the
   note and a gap in their head are distinguishable.
2. Ask one question at a time. Start with "explain it to me", then push on the
   part they were vaguest about. Three to five questions per topic.
3. Do not give the answer until they have committed to one.
4. After each topic, tell them plainly how it went, and set `confidence` in
   that note's frontmatter: 1 could not explain it, 3 explained it with gaps,
   5 explained it cleanly including tradeoffs. Say what you set and why.
5. If they could not explain a section they had ticked in Coverage, untick it
   and say so. The checklist should mean something.
6. For a `revisit` problem, ask them to reconstruct the idea, not the code.
   Clear it by setting `revisit: false` if they get it.

Cover at most three topics in one session. Stop and offer to continue.

Finish by running:

!`python3 "Career/Prep/.tools/prep_sync.py" "Career/Prep"`
```

- [ ] **Step 6: Verify the commands are discoverable and `sync` runs**

```bash
cd "/Users/lukewaehner/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain"
ls .claude/commands/prep/
python3 "Career/Prep/.tools/prep_sync.py" "Career/Prep"
```

Expected: five `.md` files, and `prep_sync: up to date`.

In a fresh Claude Code session in this directory, type `/prep` and confirm the five commands are listed.

- [ ] **Step 7: Commit**

```bash
git add .claude/commands/prep/
git commit -m "feat(prep): add the prep agent commands

/prep:drop and /prep:review are the two that carry real policy -- transcribe
solutions verbatim and flag defects rather than correcting them silently, and
untick a Coverage box the user cannot defend."
```

---

### Task 16: The launchd watcher

**Files:**
- Create: `Career/Prep/.tools/com.luke.prepsync.plist`
- Install: `~/Library/LaunchAgents/com.luke.prepsync.plist` (a copy)

**Interfaces:**
- Consumes: `prep_sync.py`.
- Produces: automatic sync within seconds of a checkbox being ticked.

- [ ] **Step 1: Write the plist**

Create `Career/Prep/.tools/com.luke.prepsync.plist`. `WatchPaths` fires on any
change under the watched directory; `ThrottleInterval` debounces a burst of
iCloud writes into one run.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.luke.prepsync</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/bin/python3</string>
        <string>/Users/lukewaehner/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain/Career/Prep/.tools/prep_sync.py</string>
        <string>/Users/lukewaehner/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain/Career/Prep</string>
    </array>
    <key>WatchPaths</key>
    <array>
        <string>/Users/lukewaehner/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain/Career/Prep/topics</string>
        <string>/Users/lukewaehner/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain/Career/Prep/problems</string>
    </array>
    <key>ThrottleInterval</key>
    <integer>15</integer>
    <key>RunAtLoad</key>
    <false/>
    <key>StandardOutPath</key>
    <string>/tmp/prepsync.log</string>
    <key>StandardErrorPath</key>
    <string>/tmp/prepsync.err</string>
</dict>
</plist>
```

- [ ] **Step 2: Verify the plist parses before installing it**

```bash
plutil -lint "/Users/lukewaehner/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain/Career/Prep/.tools/com.luke.prepsync.plist"
```

Expected: `OK`.

- [ ] **Step 3: Install and load**

```bash
cp "/Users/lukewaehner/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain/Career/Prep/.tools/com.luke.prepsync.plist" ~/Library/LaunchAgents/
launchctl unload ~/Library/LaunchAgents/com.luke.prepsync.plist 2>/dev/null
launchctl load ~/Library/LaunchAgents/com.luke.prepsync.plist
launchctl list | grep prepsync
```

Expected: a line for `com.luke.prepsync`.

- [ ] **Step 4: Prove it fires on a tick and is quiet otherwise**

```bash
cd "/Users/lukewaehner/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain/Career/Prep"
: > /tmp/prepsync.log
NOTE="topics/Graphs/Breadth-First Search.md"
python3 - "$NOTE" <<'PY'
import sys
path = sys.argv[1]
text = open(path, encoding="utf-8").read()
open(path, "w", encoding="utf-8").write(text.replace("> - [ ] [[#Idea]]", "> - [x] [[#Idea]]", 1))
PY
```

Wait 20 seconds, then:

```bash
cat /tmp/prepsync.log
grep -E "^(sections_done|status|updated):" "topics/Graphs/Breadth-First Search.md"
```

Expected: the log shows `prep_sync: updated 2 file(s)`, and the note's
`sections_done` is now 1 with `status: learning` and today's `updated`.

Now revert the tick and confirm a run with nothing to do writes nothing:

```bash
python3 - "$NOTE" <<'PY'
import sys
path = sys.argv[1]
text = open(path, encoding="utf-8").read()
open(path, "w", encoding="utf-8").write(text.replace("> - [x] [[#Idea]]", "> - [ ] [[#Idea]]", 1))
PY
```

Wait 20 seconds, then:

```bash
python3 .tools/prep_sync.py . --check
git status --porcelain -- Career/Prep | cat
```

Expected: `prep_sync: up to date` (exit 0), and the only modified file is the
note you toggled — no other note was rewritten.

- [ ] **Step 5: Note the uninstall path in the design doc**

Append to `Career/Prep/.tools/DESIGN.md` under `## Risks`:

```markdown
## Operations

The watcher is installed at `~/Library/LaunchAgents/com.luke.prepsync.plist`,
copied from `.tools/`. To disable it:

    launchctl unload ~/Library/LaunchAgents/com.luke.prepsync.plist
    rm ~/Library/LaunchAgents/com.luke.prepsync.plist

Everything keeps working without it; `/prep:sync` and every other `/prep`
command run the script themselves. Logs are at `/tmp/prepsync.log` and
`/tmp/prepsync.err`.
```

- [ ] **Step 6: Final verification of the whole system**

```bash
cd "/Users/lukewaehner/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain/Career/Prep/.tools"
python3 -m unittest discover -s tests -v 2>&1 | tail -3
cd ..
python3 .tools/prep_sync.py . --check
cd ../..
python3 Career/Prep/.tools/check_links.py . --scope Career/Prep
git status --porcelain -- Career/Prep | cat
```

Expected: `OK` with 64 tests; `prep_sync: up to date`; `check_links: all links
resolve`; and a clean or near-clean status.

- [ ] **Step 7: Commit**

```bash
git add Career/Prep/.tools/
git commit -m "feat(prep): add the launchd watcher that syncs on note changes

Debounced at 15s so a burst of iCloud writes collapses into one run, and the
script no-ops when nothing changed, so the watcher does not itself become a
source of conflict duplicates."
```

---

## Verification summary

The plan is done when all of these hold:

| Check | Command | Expected |
|---|---|---|
| Tests pass | `python3 -m unittest discover -s tests -v` (in `.tools/`) | OK, 64 tests |
| Sync is idempotent | `python3 .tools/prep_sync.py . --check` | `up to date`, exit 0 |
| No dead links | `python3 Career/Prep/.tools/check_links.py . --scope Career/Prep` | all links resolve |
| Old structure gone | `ls Career/Prep` | `Prep.md`, `Problems.base`, `Topics.base`, `meta`, `problems`, `topics` only |
| 95 topic notes | `ls Career/Prep/topics/*/*.md \| wc -l` | 105 (95 + 10 folder notes) |
| Bases render | open both in Obsidian | all nine views load |
| Watcher fires | tick a box, wait 20s, `cat /tmp/prepsync.log` | reports the update |
