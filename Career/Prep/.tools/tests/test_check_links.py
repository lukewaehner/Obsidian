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
