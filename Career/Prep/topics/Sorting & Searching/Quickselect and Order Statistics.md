---
type: topic
group: Sorting & Searching
tier: core
confidence:
sections_total: 6
sections_done: 3
coverage: 0.50
status: learning
updated: 2026-09-13
---

# Quickselect and Order Statistics

← [[Career/Prep/topics/Sorting & Searching/Sorting & Searching|Sorting & Searching]]

> [!abstract]- Coverage — 3/6
> - [ ] [[#Idea]]
> - [x] [[#How it works]]
> - [x] [[#Implementation]]
> - [ ] [[#Complexity]]
> - [ ] [[#When to use it]]
> - [x] [[#Gotchas]]

## Idea

The k-th order statistic is the k-th smallest element of a collection —
minimum is k = 1, maximum is k = n. Quickselect finds it without fully
sorting, by partitioning like quicksort and recursing into only the side
that contains the target rank — [[Order Statistics]].

## How it works

Partition into Left / Middle / Right around a pivot, compare `k` against the three sizes, and recurse into one side only — with the index arithmetic `k' = k − ℓ − m` for the right branch — [[Code/Algorithms/Order Statistics|Order Statistics]] § Pivot and Conquer.

## Implementation

Median of medians: groups of five, median of each, recurse on those medians, use the result as pivot — guaranteeing at least n/4 elements on each side and turning the recurrence `T(n) = T(n/5) + T(3n/4) + Θ(n)` into Θ(n) because 1/5 + 3/4 < 1 — [[Code/Algorithms/Order Statistics|Order Statistics]] § Median of Medians.

## Complexity

O(n) average case, O(n²) worst case — same partitioning risk as quicksort,
since it's the same core operation with one side of the recursion discarded.

## When to use it

Kth largest/smallest, median-of-array, and top-k problems where a full sort
would do unnecessary work.

## Gotchas

A random pivot gives Θ(n) *expected* but still Θ(n²) worst case; only median-of-medians makes it deterministic — and k-selection is Ω(n) regardless, since every element must be examined — [[Code/Algorithms/Order Statistics|Order Statistics]] § Good and Bad Pivots, § Finding order statistics $k$-Selection.

## Resources

- [Sedgewick - Quicksort: 2. Selection (video)](https://www.coursera.org/lecture/algorithms-part1/selection-UQxFT)

## Problems

_None yet._
