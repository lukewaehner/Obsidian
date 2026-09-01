---
type: topic
group: Strings
tier: core
confidence:
---

# Knuth-Morris-Pratt

> [!abstract]- Coverage — 0/6
> - [ ] [[#Idea]]
> - [ ] [[#How it works]]
> - [ ] [[#Implementation]]
> - [ ] [[#Complexity]]
> - [ ] [[#When to use it]]
> - [ ] [[#Gotchas]]

## Idea

Never re-examine a text character twice: precompute how much of the pattern's
own prefix overlaps its suffix, so a mismatch lets the pattern pointer jump
back intelligently instead of restarting from scratch — [[String Manipulation]].

## How it works

Build the failure function (longest-prefix-suffix, or LPS, array) for the
pattern first: `lps[i]` is the length of the longest proper prefix of
`pattern[0..i]` that is also a suffix. On a mismatch at text position `j`
against pattern position `i`, resume at `lps[i-1]` instead of `0`.

## Implementation

## Complexity

O(n + m): the LPS table is O(m) to build, and the scan touches each text
character a bounded number of times, giving O(n) for the search itself.

## When to use it

Repeated or self-similar patterns, or any case where Ω(nm) naive search is
too slow and the pattern is reused across many searches.

## Gotchas

The LPS table construction is the fiddly part — off-by-one errors there are
the most common bug, not the search loop itself.

## Resources

- [Sedgewick - Knuth-Morris-Pratt (video)](https://www.coursera.org/learn/algorithms-part2/lecture/TAtDr/knuth-morris-pratt)
- [The Knuth-Morris-Pratt (KMP) String Matching Algorithm (video)](https://www.youtube.com/watch?v=5i7oKodCRJo)

## Problems

_None yet._
