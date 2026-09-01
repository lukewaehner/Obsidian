# Prep System Design

Date: 2026-09-01
Status: Approved

Lives in `.tools/` rather than a vault folder so Obsidian does not index it into
the graph. It is version-controlled with the notes it describes.

## Problem

The current `Career/Prep/` splits every subject across two mirrored trees:
`topics/` holds reference material copied from Coding Interview University, and
`work/` holds a checkbox list per topic. The split forces a decision on every
edit — reference or work? — and the checkboxes record only that something
happened, not what was learned. `Prep.md` hand-maintains a 16-row progress table
that is already stale. There is nowhere to put a solved problem.

## Goals

1. One note per idea. No reference/work split.
2. Sections to write study notes under, not boxes to tick for their own sake.
3. A problems area with a real database view over it.
4. Progress visible at a glance and never hand-maintained.
5. Study is the only manual input. Tracking, roll-ups, and review are automated.

## Non-goals

- Spaced repetition scheduling. Rejected in favour of an explicit revisit flag.
- Preserving Coding Interview University's section numbering or its
  "Even More Knowledge" / "Additional Learning" grouping.
- Migrating `Code/Algorithms/` into `Career/Prep/`. Those notes stay where they
  are; topic notes link to them.

## Constraints

- Obsidian 1.9.10. Bases is a core plugin and is enabled. Dataview, Tasks,
  Templater, folder-note-plugin, and obsidian-git are installed.
- **Bases formulas cannot read checkboxes or tasks from a note body.** Only
  frontmatter properties and `file.*` implicit properties are visible. This is
  the single constraint that shapes the automation design.
- The vault is in iCloud Drive. Bulk writes while Obsidian is open on another
  device produce ` 2` / ` 3` conflict duplicates. Two such empty directories
  (`topics 2`, `work 2`) already exist and are removed by this migration.
- System Python is 3.9.6. Tooling must be stdlib-only.
- 840 internal `[[Career/Prep/...]]` wikilinks exist. `Career/Career.md` links
  inbound.

## Architecture

Three layers, each with one job.

```
  note bodies  ──parse──>  frontmatter  ──read──>  Bases views
  (you write)              (derived)               (you browse)
       ^                        ^                       ^
       │                   prep_sync.py                 │
       └──────────── agent commands ────────────────────┘
```

- **Note bodies** are the source of truth. A Coverage checklist at the top of
  each topic note is the only completion signal you touch.
- **`prep_sync.py`** derives frontmatter from note bodies. Pure function of the
  filesystem: idempotent, writes only on change.
- **Bases** renders. It never computes anything the script has not already
  written, and it never needs to.

### Why not Dataview for the topic roll-up

Dataview could count body checkboxes directly and skip the sync step, but its
tables are read-only. Confidence would have to be edited note by note, and the
problem database would lose inline editing — the thing that makes it feel like a
database rather than a report. The sync script costs ~200 lines and buys a
single consistent UI for both topics and problems.

## Folder structure

```
Career/Prep/
├── Prep.md                       master hub
├── Topics.base
├── Problems.base
├── .tools/
│   ├── DESIGN.md                 this file
│   └── prep_sync.py
├── topics/
│   ├── Complexity/
│   ├── Data Structures/
│   ├── Trees/
│   ├── Graphs/
│   ├── Sorting & Searching/
│   ├── Algorithm Design/
│   ├── Strings/
│   ├── Math & Bits/
│   ├── Systems/
│   └── Design/
├── problems/
│   ├── Arrays & Hashing/
│   ├── Two Pointers/
│   ├── Sliding Window/
│   ├── Stack/
│   ├── Binary Search/
│   ├── Linked List/
│   ├── Trees/
│   ├── Tries/
│   ├── Heap & Priority Queue/
│   ├── Backtracking/
│   ├── Graphs/
│   ├── Advanced Graphs/
│   ├── 1-D DP/
│   ├── 2-D DP/
│   ├── Greedy/
│   ├── Intervals/
│   ├── Math & Geometry/
│   └── Bit Manipulation/
└── meta/
```

Each `topics/<Group>/` and `problems/<Pattern>/` directory gets a folder-note of
the same name, embedding that slice of the relevant Base.

Depth is expressed by a `tier: core | extra` property, not by folder. Skip lists
sit beside Hash Tables in `Data Structures/`; the Base filters them out of the
core progress number.

## Topic note contract

```markdown
---
type: topic
group: Graphs
tier: core
confidence: 3
sections_total: 6
sections_done: 4
coverage: 0.67
status: learning
updated: 2026-09-01
---

# Dijkstra's Algorithm

> [!abstract]- Coverage — 4/6
> - [x] [[#Idea]]
> - [x] [[#How it works]]
> - [x] [[#Implementation]]
> - [x] [[#Complexity]]
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
```

Properties:

| Property | Set by | Values |
|---|---|---|
| `type` | template | `topic` |
| `group` | template | one of the ten group names |
| `tier` | template | `core`, `extra` |
| `confidence` | **you**, from the Bases table | `1`–`5`, empty until first set |
| `sections_total` | `prep_sync` | count of Coverage items |
| `sections_done` | `prep_sync` | count of ticked Coverage items |
| `coverage` | `prep_sync` | `sections_done / sections_total`, 2dp |
| `status` | `prep_sync` | `untouched` (0), `learning` (partial), `solid` (all) |
| `updated` | `prep_sync` | date `sections_done` last changed |

`confidence` is the only hand-set property in the system, and it is set from the
database table, not by opening the note.

`status` is derived, never authored. A `rusty` state is not derived — a topic
becomes review-worthy through low `confidence` or a stale `updated`, both of
which the *Needs review* view filters on.

### The six-section skeleton

Every topic note has the same six sections. This is the deliberate opinionated
call in the design: it makes coverage percentages comparable across the whole
plan, so "62% through Graphs" and "62% through Systems" mean the same thing.

The cost is that Dijkstra and Endianness get the same shape, and some sections
will be thin for some topics. A thin section is still an honest signal — it says
you looked and there was little to say.

Coding Interview University's per-topic checklists are mostly *resource links*,
not concepts. Rendering each link as a section would give Sorting forty
sections. Links go under `## Resources`. Where CIU has a genuinely distinct
concept item — Arrays' "implement a vector", Hash Tables' "distributed hash
tables" — it is added as an extra section and counted in `sections_total`.

`## Problems` is regenerated by `prep_sync` from problem notes that name this
topic. It is not counted in `sections_total`.

## Problem note contract

```markdown
---
type: problem
source: leetcode
number: 121
url: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
difficulty: Easy
pattern: Sliding Window
patterns: [Sliding Window, Arrays & Hashing]
topics: ["[[Arrays]]"]
solved_on: 2026-09-01
attempts: 2
aid: hint
revisit: true
time: O(n)
space: O(1)
language: python
---

# 121 · Best Time to Buy and Sell Stock

> [!question]- Problem

## Idea
## Naive
## Optimal
## Why it works
## Template
## Mistakes I made
## Related
```

| Property | Set by | Values |
|---|---|---|
| `pattern` | `prep_sync`, from the folder | one of the eighteen pattern names |
| `patterns` | me, when writing the note | list; includes `pattern` |
| `difficulty` | me | `Easy`, `Medium`, `Hard` |
| `topics` | me | wikilinks to topic notes |
| `aid` | me, from what you tell me | `unaided`, `hint`, `solution` |
| `revisit` | **you**, from the Bases table | boolean |
| everything else | me | — |

A problem's folder is its primary pattern; `patterns` carries the cross-cutting
ones so a Two Pointers / Sliding Window problem appears under both in the Base.

Pasted solutions are transcribed verbatim under `## Optimal` (or `## Naive`, if
that is what they are) — they are the record of what you actually wrote. Bugs
and suboptimal approaches get a callout naming the defect and the fix, the same
treatment the existing Hash table note gives its tombstone bug. The mistake is
preserved, not silently corrected.

## Databases

### `Topics.base`

| View | Filter | Notes |
|---|---|---|
| Core progress | `tier == "core"` | grouped by `group`, sorted by `coverage` ascending |
| Extras | `tier == "extra"` | same columns |
| Needs review | `confidence <= 2 or (status == "solid" and updated older than 30d)` | sorted by `confidence` |
| Recently touched | all | sorted by `updated` descending, limit 20 |

Columns: name, group, tier, status, coverage, confidence, updated.
`confidence` is inline-editable.

### `Problems.base`

| View | Filter | Notes |
|---|---|---|
| All | `type == "problem"` | sorted by `solved_on` descending |
| By pattern | all | grouped by `pattern` |
| Needs revisit | `revisit or aid != "unaided"` | sorted by `solved_on` |
| By difficulty | all | grouped by `difficulty` |
| Recent | all | limit 25, sorted by `solved_on` descending |

Columns: number, name, difficulty, pattern, time, space, aid, attempts,
`solved_on`, revisit. `revisit` is inline-editable.

### `Prep.md`

Regenerated by `prep_sync` between `<!-- prep:begin -->` / `<!-- prep:end -->`
markers, so it cannot go stale the way the current table has:

- Overall core coverage, as a fraction and a bar.
- Per-group coverage table.
- Problems solved, by pattern and by difficulty.
- Five weakest topics.
- Anything flagged for revisit.

Outside the markers: hand-written orientation and links to the Bases and to
`Career.md`.

## `prep_sync.py`

Stdlib Python 3.9. Entry point takes the prep root as an optional argument,
defaulting to the directory two levels up from the script.

Responsibilities, in order:

1. Walk `topics/`. For each note, parse the Coverage callout, count total and
   ticked items, compute `coverage` and `status`.
2. Walk `problems/`. Derive `pattern` from the parent directory name. Collect
   the `topics` backlinks.
3. For each topic note, rebuild the `## Problems` section from the collected
   backlinks.
4. Write frontmatter — but only for keys whose value changed. If a file's
   computed frontmatter and `## Problems` section both match what is on disk,
   the file is not opened for writing at all.
5. Regenerate the `Prep.md` marker block.
6. Print a one-line summary of what changed.

Correctness requirements:

- Never touch anything outside the derived key set and the two marked regions.
  Hand-written frontmatter keys and all prose survive untouched.
- Preserve frontmatter key order and the file's existing line endings.
- `updated` advances only when `sections_done` changes, not on every run.
- Exit non-zero on a malformed note (missing Coverage block, unparseable
  frontmatter) and name the file. Never silently skip.
- A `--check` flag reports what would change and writes nothing.

The write-only-on-change rule is not an optimisation. Rewriting ~100 files on
every tick, inside an iCloud folder, is exactly how the existing ` 2` conflict
directories were created.

### Triggers

1. **launchd `WatchPaths`** on `Career/Prep/`, debounced, so ticking a box
   updates the database within seconds. Modelled on the existing
   `com.luke.procmon` job.
2. **`/prep sync`** slash command, as the manual escape hatch.
3. Automatically whenever an agent writes to `Career/Prep/`.

## Agent commands

Claude Code commands in the vault's `.claude/commands/`:

| Command | Does |
|---|---|
| `/prep drop` | Takes pasted solutions, writes problem notes, fills every property, cross-links topics, flags bugs |
| `/prep review` | Picks weakest topics and revisit-flagged problems, quizzes conversationally, updates `confidence` and `revisit` |
| `/prep next` | Recommends what to study, from coverage gaps and problem-pattern gaps |
| `/prep status` | Progress report |
| `/prep sync` | Runs `prep_sync.py` |

## Topic manifest

95 topic notes across ten groups; 62 core, 33 extra. The Source column names the
note or section the content comes from, relative to `Career/Prep/`.

### Complexity — 4 core

| Note | Tier | Source |
|---|---|---|
| Big-O and Asymptotic Notation | core | `topics/05 Big-O and Complexity.md` |
| Amortized Analysis | core | `topics/05 Big-O and Complexity.md` |
| Recurrences and the Master Theorem | core | `topics/05`, links `Code/Algorithms/Recurrences`, `Master Theorem` |
| NP-Completeness and Approximation | core | `topics/11 …/NP, NP-Complete and Approximation Algorithms.md` |

### Data Structures — 9 core, 8 extra

| Note | Tier | Source |
|---|---|---|
| Arrays | core | `topics/06 …/Arrays.md` + `work/06 …/Arrays.md` (vector implementation) |
| Linked Lists | core | `topics/06 …/Linked Lists.md` + `work/06 …/Linked Lists.md` |
| Stacks | core | `topics/06 …/Stack.md` |
| Queues and Deques | core | `topics/06 …/Queue.md` + `work/06 …/Queue.md` |
| Hash Tables | core | `topics/06 …/Hash table.md` + `work/06 …/Hash table.md` (tombstone defect callout) |
| Heaps and Priority Queues | core | `topics/08 Trees/Heap - Priority Queue - Binary Heap.md` |
| Tries | core | `topics/11 …/Tries.md` |
| Union-Find | core | `topics/15 …/Disjoint Sets & Union Find.md` + `topics/16 …/Union-Find.md` |
| LRU Cache | core | `topics/11 …/Caches.md` (application half) |
| Bloom Filters | extra | `topics/15 …/Bloom Filter.md` |
| Skip Lists | extra | `topics/15 …/Skip lists.md` |
| Augmented Data Structures | extra | `topics/15 …/Augmented Data Structures.md` |
| Treaps | extra | `topics/15 …/Treap.md` |
| k-D Trees | extra | `topics/15 …/k-D Trees.md` |
| van Emde Boas Trees | extra | `topics/15 …/van Emde Boas Trees.md` |
| HyperLogLog | extra | `topics/15 …/HyperLogLog.md` |
| Locality-Sensitive Hashing | extra | `topics/15 …/Locality-Sensitive Hashing.md` |

### Trees — 4 core, 2 extra

| Note | Tier | Source |
|---|---|---|
| Trees Intro and Terminology | core | `topics/08 Trees/Trees - Intro.md` |
| Tree Traversals | core | `topics/08 Trees/Trees - Intro.md` |
| Binary Search Trees | core | `topics/08 Trees/Binary search trees - BSTs.md` + `work/` counterpart |
| Balanced Search Trees | core | `topics/15 …/Balanced search trees.md` |
| Segment and Fenwick Trees | extra | new |
| B-Trees | extra | `topics/15 …/Balanced search trees.md` |

### Graphs — 8 core, 4 extra

| Note | Tier | Source |
|---|---|---|
| Graph Representations | core | `topics/10 Graphs.md` |
| Breadth-First Search | core | `topics/10 Graphs.md` |
| Depth-First Search | core | `topics/10 Graphs.md`, links `Code/Algorithms/Depth First Search` |
| Topological Sort | core | `topics/10 Graphs.md`, links `Code/Algorithms/Topological Ordering` |
| Dijkstra's Algorithm | core | `topics/10 Graphs.md`, links `Code/Algorithms/Dijkstra's Algorithm` |
| Bellman-Ford | core | `topics/10 Graphs.md`, links `Code/Algorithms/Bellman-Ford Algorithm` |
| Minimum Spanning Trees | core | `topics/10 Graphs.md` |
| Strongly Connected Components | core | `topics/10 Graphs.md` |
| Bipartite Graphs | extra | `topics/10 Graphs.md` |
| Floyd-Warshall | extra | `topics/16 …/Advanced Graph Processing.md` |
| A* Search | extra | `topics/15 …/A-star.md` |
| Network Flow | extra | `topics/15 …/Network Flows.md` |

### Sorting & Searching — 10 core

| Note | Tier | Source |
|---|---|---|
| Sorting Fundamentals | core | `topics/09 Sorting.md` (stability, comparison bound, arrays vs lists) |
| Insertion Sort | core | `topics/09 Sorting.md` |
| Selection Sort | core | `topics/09 Sorting.md` |
| Bubble Sort | core | `topics/09 Sorting.md` |
| Merge Sort | core | `topics/09 Sorting.md` |
| Quicksort | core | `topics/09 Sorting.md` |
| Heapsort | core | `topics/09 Sorting.md` |
| Counting and Radix Sort | core | `topics/09 Sorting.md` + `topics/16 …/Sorting.md` |
| Quickselect and Order Statistics | core | `topics/09`, links `Code/Algorithms/Order Statistics` |
| Binary Search | core | `topics/07 …/Binary search.md` + `work/` counterpart |

### Algorithm Design — 5 core, 1 extra

| Note | Tier | Source |
|---|---|---|
| Recursion | core | `topics/11 …/Recursion.md` + `work/` counterpart |
| Divide and Conquer | core | new, links `Code/Algorithms/Divide and Conquer` |
| Greedy Algorithms | core | new, links `Code/Algorithms/Greedy` |
| Dynamic Programming | core | `topics/11 …/Dynamic Programming.md` + `topics/16 …/More Dynamic Programming.md` + `work/` counterpart |
| Backtracking | core | new |
| Linear Programming | extra | `topics/15 …/Linear Programming.md` |

### Strings — 3 core, 2 extra

| Note | Tier | Source |
|---|---|---|
| String Manipulation | core | `topics/11 …/String searching & manipulations.md` |
| Knuth-Morris-Pratt | core | `topics/16 …/String Matching.md` |
| Rabin-Karp | core | `topics/16 …/String Matching.md` |
| Boyer-Moore | extra | `topics/16 …/String Matching.md` |
| Suffix Arrays | extra | `topics/09 Sorting.md` (Sedgewick radix series) |

### Math & Bits — 3 core, 6 extra

| Note | Tier | Source |
|---|---|---|
| Bitwise Operations | core | `topics/07 …/Bitwise operations.md` |
| Combinatorics and Probability | core | `topics/11 …/Combinatorics (n choose k) & Probability.md` |
| Floating Point Numbers | core | `topics/11 …/Floating Point Numbers.md` |
| Discrete Math | extra | `topics/15 …/Discrete math.md` |
| Math for Fast Processing | extra | `topics/15 …/Math for Fast Processing.md` |
| Geometry and Convex Hull | extra | `topics/15 …/Geometry, Convex hull.md` |
| Fast Fourier Transform | extra | `topics/15 …/Fast Fourier Transform.md` |
| Information Theory and Entropy | extra | `topics/15 …/Information theory.md` + `topics/15 …/Entropy.md` |
| Parity and Hamming Codes | extra | `topics/15 …/Parity & Hamming Code.md` |

### Systems — 6 core, 9 extra

| Note | Tier | Source |
|---|---|---|
| How a Program Runs | core | `topics/11 …/How computers process a program.md` |
| Processes and Threads | core | `topics/11 …/Processes and Threads.md` |
| Concurrency and Parallel Programming | core | `topics/15 …/Parallel Programming.md` |
| Caches | core | `topics/11 …/Caches.md` (hardware half) |
| Memory and Garbage Collection | core | `topics/15 …/Garbage collection.md` |
| Networking | core | `topics/11 …/Networking.md` |
| Endianness | extra | `topics/11 …/Endianness.md` |
| Unicode | extra | `topics/11 …/Unicode.md` |
| Compilers | extra | `topics/15 …/Compilers.md` |
| Compression | extra | `topics/15 …/Compression.md` |
| Computer Security | extra | `topics/15 …/Computer Security.md` |
| Cryptography | extra | `topics/15 …/Cryptography.md` |
| Unix and Linux Command Line | extra | `topics/15 …/Unix - Linux command line tools.md` |
| DevOps | extra | `topics/15 …/DevOps.md` |
| Editors: Emacs and Vim | extra | `topics/15 …/Emacs and vi(m).md` |

### Design — 10 core, 1 extra

| Note | Tier | Source |
|---|---|---|
| System Design | core | `topics/14 System Design.md` |
| Scalability | core | `topics/14 System Design.md` |
| CAP Theorem and Consistency | core | `topics/14 System Design.md` |
| Consistent Hashing | core | `topics/14 System Design.md` |
| NoSQL and Data Modeling | core | `topics/14 System Design.md` |
| Messaging, Serialization, and Queues | core | `topics/15 …/Messaging, Serialization, and Queueing Systems.md` |
| Object-Oriented Design | core | new, links `Code/OOD` |
| SOLID | core | `topics/16 …/SOLID.md` |
| Design Patterns | core | `topics/11 …/Design patterns.md` |
| Testing | core | `topics/11 …/Testing.md` |
| Consensus: Paxos and Raft | extra | `topics/14 System Design.md` |

### meta — 8 notes, excluded from all progress numbers

| Note | Source |
|---|---|
| Mindset and Approach | `topics/00 Mindset and Approach/` (5 notes merged) |
| Choosing a Language | `topics/01 Choose a Programming Language.md` |
| The Daily Plan | `topics/03 The Daily Plan.md` |
| Practice Sites | `topics/04 Coding Question Practice.md` |
| Books | `topics/02 Books/` (4 notes merged) |
| Resources | `topics/17 Resources/` (5 notes merged) |
| Getting the Job | `topics/13 Getting the Job/` (6 notes merged) |
| Final Review | `topics/12 Final Review.md` |

meta notes carry `type: meta` and no Coverage block. `prep_sync` skips them.

## Migration

1. Commit the working tree as it stands. The current `Career/Prep/` has
   uncommitted deletions and modifications; they are captured before anything
   moves.
2. Confirm Obsidian is closed on other devices.
3. Build the new tree alongside the old one.
4. Port content per the manifest. Seven `work/` notes carry real prose beyond
   their checklists and are ported explicitly:
   `work/06 …/Arrays.md` (vector implementation),
   `work/06 …/Hash table.md` (tombstone defect callout),
   `work/06 …/Linked Lists.md`, `work/06 …/Queue.md`,
   `work/07 …/Binary search.md`, `work/08 …/Binary search trees - BSTs.md`,
   `work/11 …/Dynamic Programming.md`.
   Every `[x]` in the old trees maps to a ticked Coverage box in the new one, so
   existing progress is not reset.
5. Rewrite the 840 internal wikilinks and `Career.md`'s inbound links.
6. Verify every wikilink resolves. Any unresolved link fails the migration.
7. Delete `topics/`, `work/`, `topics 2/`, and `work 2/`.
8. Run `prep_sync.py --check`, then for real. Verify the Bases render.

Migration and the new tooling land as separate commits: `refactor:` for the note
reorganisation, `feat:` for `prep_sync.py`, the Bases, and the agent commands.

## Risks

| Risk | Mitigation |
|---|---|
| iCloud conflict duplicates during the bulk move | Obsidian closed elsewhere; write-only-on-change in the sync script thereafter |
| Broken wikilinks across 840 references | Link verification is a migration gate, not a follow-up |
| The six-section skeleton fits some topics badly | Extra sections are allowed and counted; a thin section is a valid signal |
| launchd watcher fighting iCloud | Idempotent no-op runs; the watcher can be dropped for on-demand sync alone |
| `confidence` never gets set, so *Needs review* is empty | `/prep review` sets it as a side effect of quizzing |
