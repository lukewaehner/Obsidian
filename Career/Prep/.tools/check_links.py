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

LINK_RE = re.compile(r"(!?)\[\[([^\]]+)\]\]")
ATTACHMENT_EXTS = (
    ".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".avif",
    ".pdf", ".mp3", ".mp4", ".mov", ".wav", ".webm", ".excalidraw",
)
SKIP_DIRS = {".git", ".obsidian", ".trash", ".tools", ".strip_title_backups"}


def iter_links(text):
    """Yield wikilink targets, with aliases and heading anchors removed.

    Attachment embeds (![[diagram.png]]) are skipped -- they are images and
    files, not notes. A note embed (![[Arrays]]) is NOT skipped: it is a real
    link that can dangle, and this checker exists to catch dangling links.
    Bare intra-note anchors ([[#Heading]]) always resolve to the current note.
    """
    for match in LINK_RE.finditer(text):
        target = match.group(2).split("|", 1)[0].split("#", 1)[0].strip()
        if not target:
            continue
        if match.group(1) == "!" and target.lower().endswith(ATTACHMENT_EXTS):
            continue
        if target.lower().endswith(".md"):
            target = target[:-3]
        yield target


def build_index(vault_root):
    """Collect every string Obsidian would resolve to a note.

    Both the bare stem ('Arrays') and the vault-relative path without its
    extension ('Career/Prep/topics/Data Structures/Arrays') are indexed,
    because the vault uses both link styles. The index is case-folded because
    Obsidian resolves links case-insensitively.
    """
    index = set()
    for path in vault_root.rglob("*.md"):
        if SKIP_DIRS & set(path.relative_to(vault_root).parts):
            continue
        index.add(path.stem.lower())
        index.add(str(path.relative_to(vault_root).with_suffix("")).lower())
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
            if target.lower() not in index:
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
