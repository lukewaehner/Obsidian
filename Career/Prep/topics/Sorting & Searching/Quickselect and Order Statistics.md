---
type: topic
group: Sorting & Searching
tier: core
confidence:
sections_total: 6
sections_done: 0
coverage: 0.00
status: untouched
updated: 2026-09-01
---

# Quickselect and Order Statistics

> [!abstract]- Coverage — 0/6
> - [ ] [[#Idea]]
> - [ ] [[#How it works]]
> - [ ] [[#Implementation]]
> - [ ] [[#Complexity]]
> - [ ] [[#When to use it]]
> - [ ] [[#Gotchas]]

## Idea

The k-th order statistic is the k-th smallest element of a collection —
minimum is k = 1, maximum is k = n. Quickselect finds it without fully
sorting, by partitioning like quicksort and recursing into only the side
that contains the target rank — [[Order Statistics]].

## How it works

## Implementation

## Complexity

O(n) average case, O(n²) worst case — same partitioning risk as quicksort,
since it's the same core operation with one side of the recursion discarded.

## When to use it

Kth largest/smallest, median-of-array, and top-k problems where a full sort
would do unnecessary work.

## Gotchas

## Resources

- [Sedgewick - Quicksort: 2. Selection (video)](https://www.coursera.org/lecture/algorithms-part1/selection-UQxFT)

## Problems

_None yet._
