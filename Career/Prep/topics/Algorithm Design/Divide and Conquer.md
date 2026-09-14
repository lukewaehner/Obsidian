---
type: topic
group: Algorithm Design
tier: core
confidence:
sections_total: 6
sections_done: 3
coverage: 0.50
status: learning
updated: 2026-09-13
---

# Divide and Conquer

← [[Career/Prep/topics/Algorithm Design/Algorithm Design|Algorithm Design]]

> [!abstract]- Coverage — 3/6
> - [x] [[#Idea]]
> - [ ] [[#How it works]]
> - [ ] [[#Implementation]]
> - [x] [[#Complexity]]
> - [x] [[#When to use it]]
> - [ ] [[#Gotchas]]

## Idea

Three steps: divide into subproblems of the same kind, solve each recursively, combine. The common shape is two halves plus O(n) combine, i.e. `T(n) = 2T(n/2) + O(n)` — [[Code/Algorithms/Divide and Conquer|Divide and Conquer]].

## How it works

## Implementation

[[Code/Algorithms/Divide and Conquer|coursework notes]] — the note shares
this note's title, so link the coursework copy by full path, not
the bare `Divide and Conquer` link.

## Complexity

The recurrence is the analysis — solve it by recursion tree or the Master Theorem — [[Code/Algorithms/Recurrences|Recurrences]], [[Code/Algorithms/Master Theorem|Master Theorem]].

## When to use it

Sorting is the headline case (O(n²) → O(n log n) via [[Code/Algorithms/Sorts/Merge Sort|Merge Sort]] and [[Code/Algorithms/Sorts/Quick Sort|Quick Sort]]), and selection is the case where the combine step vanishes because only one side is recursed into — [[Code/Algorithms/Order Statistics|Order Statistics]] § Pivot and Conquer.

## Gotchas

## Resources

- [Divide-and-conquer algorithm (Wikipedia)](https://en.wikipedia.org/wiki/Divide-and-conquer_algorithm)

## Problems

- [[Career/Prep/problems/Linked List/23 · Merge k Sorted Lists|23 · Merge k Sorted Lists]] · Hard · Linked List
