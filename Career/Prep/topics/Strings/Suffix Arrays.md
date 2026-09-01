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

# Suffix Arrays

> [!abstract]- Coverage — 0/6
> - [ ] [[#Idea]]
> - [ ] [[#How it works]]
> - [ ] [[#Implementation]]
> - [ ] [[#Complexity]]
> - [ ] [[#When to use it]]
> - [ ] [[#Gotchas]]

## Idea

A sorted array of every suffix of a string, indexed by starting position —
it turns substring and pattern-matching queries into binary searches.

## How it works

Sorting all n suffixes naively costs O(n² log n) (each comparison is up to
O(n)). Faster constructions build the array via radix-sort-style passes over
increasing suffix-prefix lengths, doubling the compared length each round —
the same LSD/MSD radix idea as [[Counting and Radix Sort]], applied to
strings instead of fixed-width keys.

## Implementation

## Complexity

O(n log n) to build with a radix/doubling construction (naive comparison
sort is O(n² log n)); O(m log n) to search for a pattern of length m via
binary search over the array.

## When to use it

Repeated substring queries against a fixed text — full-text search, longest
common substring/repeat problems — where paying the O(n log n) build cost
once is cheaper than re-scanning per query.

## Gotchas

## Resources

- [Sedgewick - Suffix Arrays (video)](https://www.coursera.org/learn/algorithms-part2/lecture/TH18W/suffix-arrays)

## Problems

_None yet._
