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
