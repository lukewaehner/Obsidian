import datetime
import re
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

    def test_a_topic_in_an_unlisted_group_fails_loudly(self):
        # arrange
        with tempfile.TemporaryDirectory() as tmp:
            root = build_vault(tmp)
            (root / "topics" / "Graphs" / "Stray.md").write_text(
                TOPIC.replace("group: Graphs", "group: Bonus Round"),
                encoding="utf-8",
            )

            # act / assert
            with self.assertRaises(prep_sync.PrepError) as caught:
                prep_sync.sync(root, TODAY, dry_run=False)
            self.assertIn("Stray.md", str(caught.exception))
            self.assertIn("Bonus Round", str(caught.exception))

    def test_a_run_on_a_later_day_changes_nothing(self):
        # arrange
        with tempfile.TemporaryDirectory() as tmp:
            root = build_vault(tmp)
            prep_sync.sync(root, TODAY, dry_run=False)
            later = datetime.date(2026, 12, 25)

            # act
            changed = prep_sync.sync(root, later, dry_run=False)

            # assert
            self.assertEqual([], changed)


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


class RenderRollupTest(unittest.TestCase):
    def test_a_zero_total_row_does_not_divide_by_zero(self):
        # arrange
        groups = {"Graphs": [("Empty", 0, 0, "core")]}

        # act
        block = prep_sync.render_rollup(groups, [])

        # assert
        self.assertIn(
            "- [[Career/Prep/topics/Graphs/Empty|Empty]] — 0/0", "\n".join(block)
        )

    def test_emits_no_bare_wikilinks(self):
        # arrange
        groups = {"Trees": [("Binary Search Trees", 2, 6, "core")]}
        records = [
            {
                "name": "104 · Maximum Depth of Binary Tree",
                "pattern": "Trees",
                "difficulty": "Easy",
                "solved_on": "2026-09-01",
                "revisit": True,
                "aid": "hint",
            }
        ]

        # act
        text = "\n".join(prep_sync.render_rollup(groups, records))

        # assert
        bare = re.findall(r"\[\[([^\]|]+)\]\]", text)
        self.assertEqual([], bare)


if __name__ == "__main__":
    unittest.main()
