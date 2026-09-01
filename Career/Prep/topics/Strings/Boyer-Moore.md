---
type: topic
group: Strings
tier: extra
confidence:
sections_total: 6
sections_done: 0
coverage: 0.00
status: untouched
updated: 2026-09-01
---

# Boyer-Moore

> [!abstract]- Coverage — 0/6
> - [ ] [[#Idea]]
> - [ ] [[#How it works]]
> - [ ] [[#Implementation]]
> - [ ] [[#Complexity]]
> - [ ] [[#When to use it]]
> - [ ] [[#Gotchas]]

## Idea

Scan the pattern against the text right-to-left instead of left-to-right,
so a mismatch can skip ahead by more than one position — [[String Manipulation]].

## How it works

Two heuristics decide how far to skip on a mismatch: the bad-character rule
(jump so the mismatched text character aligns with its last occurrence in
the pattern) and the good-suffix rule (reuse the matched suffix to skip past
positions that can't work). Real implementations take the larger of the two
skips.

## Implementation

## Complexity

Best case sublinear, O(n/m) — large skips on a distinctive pattern. Worst
case O(nm), same bound as naive search, on pathological patterns like a
repeated character.

## When to use it

Long patterns against long texts, where the sublinear best case pays for the
extra preprocessing — text editors' "find" is a classic use.

## Gotchas

The bad-character and good-suffix tables are more bookkeeping than KMP's
single LPS array, which is why Boyer-Moore is asked about conceptually far
more often than implemented from scratch in an interview.

## Resources

- [Boyer-Moore String Search Algorithm (Wikipedia)](https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_string_search_algorithm)
- [Advanced String Searching Boyer-Moore-Horspool Algorithms (video)](https://www.youtube.com/watch?v=QDZpzctPf10)
- [Sedgewick - Boyer-Moore (video)](https://www.coursera.org/learn/algorithms-part2/lecture/CYxOT/boyer-moore)

## Problems

_None yet._
