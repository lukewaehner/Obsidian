import datetime
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


class FmListTest(unittest.TestCase):
    def test_returns_the_flow_form_value_unchanged(self):
        # arrange
        fm = ['topics: ["[[Arrays]]", "[[Hash Tables]]"]']

        # act / assert
        self.assertEqual(
            '["[[Arrays]]", "[[Hash Tables]]"]', prep_sync.fm_list(fm, "topics")
        )

    def test_joins_a_block_style_list_into_one_string(self):
        # arrange
        fm = [
            "topics:",
            '  - "[[Arrays]]"',
            '  - "[[Hash Tables]]"',
            "solved_on: 2026-09-01",
        ]

        # act / assert
        self.assertEqual(
            '"[[Arrays]]", "[[Hash Tables]]"', prep_sync.fm_list(fm, "topics")
        )

    def test_returns_empty_string_for_an_absent_key(self):
        # arrange
        fm = ["type: problem"]

        # act / assert
        self.assertEqual("", prep_sync.fm_list(fm, "topics"))

    def test_returns_empty_string_for_an_empty_value_with_no_block_items(self):
        # arrange
        fm = ["topics:", "solved_on: 2026-09-01"]

        # act / assert
        self.assertEqual("", prep_sync.fm_list(fm, "topics"))


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
            "> - [x] [[#Later]]",
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


class FmBoolTest(unittest.TestCase):
    def test_lowercase_true_is_true(self):
        self.assertTrue(prep_sync.fm_bool(["revisit: true"], "revisit"))

    def test_capitalised_true_is_true(self):
        self.assertTrue(prep_sync.fm_bool(["revisit: True"], "revisit"))

    def test_yes_is_true(self):
        self.assertTrue(prep_sync.fm_bool(["revisit: yes"], "revisit"))

    def test_quoted_true_is_true(self):
        self.assertTrue(prep_sync.fm_bool(['revisit: "true"'], "revisit"))

    def test_false_is_false(self):
        self.assertFalse(prep_sync.fm_bool(["revisit: false"], "revisit"))

    def test_absent_key_is_false(self):
        self.assertFalse(prep_sync.fm_bool(["type: problem"], "revisit"))

    def test_empty_value_is_false(self):
        self.assertFalse(prep_sync.fm_bool(["revisit:"], "revisit"))

    def test_unrecognised_value_is_false(self):
        self.assertFalse(prep_sync.fm_bool(["revisit: maybe"], "revisit"))


if __name__ == "__main__":
    unittest.main()
