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
                [
                    "- [[Career/Prep/problems/Advanced Graphs/743 · Network Delay Time"
                    "|743 · Network Delay Time]] · Medium · Advanced Graphs"
                ],
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

    def test_capitalised_revisit_is_read_as_true(self):
        # arrange
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            capitalised = PROBLEM.replace("revisit: true", "revisit: True")
            write_problem(
                root, "Advanced Graphs", "743 · Network Delay Time", capitalised
            )

            # act
            _, _, records = prep_sync.scan_problems(root)

            # assert
            self.assertTrue(records[0]["revisit"])

    def test_raises_naming_the_file_when_difficulty_is_blank(self):
        # arrange
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            broken = PROBLEM.replace("difficulty: Medium\n", "difficulty:\n")
            write_problem(root, "Advanced Graphs", "743 · Network Delay Time", broken)

            # act / assert
            with self.assertRaises(prep_sync.PrepError) as caught:
                prep_sync.scan_problems(root)
            self.assertIn("743", str(caught.exception))

    def test_quoted_difficulty_is_accepted_and_normalised(self):
        # arrange
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            quoted = PROBLEM.replace("difficulty: Medium\n", 'difficulty: "Medium"\n')
            write_problem(root, "Advanced Graphs", "743 · Network Delay Time", quoted)

            # act
            _, _, records = prep_sync.scan_problems(root)

            # assert
            self.assertEqual("Medium", records[0]["difficulty"])

    def test_raises_naming_the_file_when_aid_is_invalid(self):
        # arrange
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            broken = PROBLEM.replace("aid: hint\n", "aid: Unaided\n")
            write_problem(root, "Advanced Graphs", "743 · Network Delay Time", broken)

            # act / assert
            with self.assertRaises(prep_sync.PrepError) as caught:
                prep_sync.scan_problems(root)
            self.assertIn("743", str(caught.exception))

    def test_block_style_topics_yields_the_same_links_as_flow_form(self):
        # arrange
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            block = PROBLEM.replace(
                'topics: ["[[Dijkstra\'s Algorithm]]", "[[Heaps and Priority Queues]]"]\n',
                "topics:\n"
                '  - "[[Dijkstra\'s Algorithm]]"\n'
                '  - "[[Heaps and Priority Queues]]"\n',
            )
            write_problem(root, "Advanced Graphs", "743 · Network Delay Time", block)

            # act
            _, by_topic, _ = prep_sync.scan_problems(root)

            # assert
            self.assertIn("Dijkstra's Algorithm", by_topic)
            self.assertIn("Heaps and Priority Queues", by_topic)

    def test_raises_when_a_topic_does_not_resolve_to_a_known_topic_note(self):
        # arrange
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_problem(
                root, "Advanced Graphs", "743 · Network Delay Time", PROBLEM
            )
            known_topics = {"heaps and priority queues": "Heaps and Priority Queues"}

            # act / assert
            with self.assertRaises(prep_sync.PrepError) as caught:
                prep_sync.scan_problems(root, known_topics)
            self.assertIn("743", str(caught.exception))

    def test_fully_qualified_topic_link_resolves_to_its_stem(self):
        # arrange
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            qualified = PROBLEM.replace(
                'topics: ["[[Dijkstra\'s Algorithm]]", "[[Heaps and Priority Queues]]"]',
                'topics: ["[[Career/Prep/topics/Graphs/Dijkstra\'s Algorithm'
                '|Dijkstra\'s Algorithm]]"]',
            )
            write_problem(root, "Advanced Graphs", "743 · Network Delay Time", qualified)
            known_topics = {"dijkstra's algorithm": "Dijkstra's Algorithm"}

            # act
            _, by_topic, _ = prep_sync.scan_problems(root, known_topics)

            # assert
            self.assertIn("Dijkstra's Algorithm", by_topic)


if __name__ == "__main__":
    unittest.main()
