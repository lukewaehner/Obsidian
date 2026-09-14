---
type: topic
group: Complexity
tier: core
confidence:
sections_total: 6
sections_done: 2
coverage: 0.33
status: learning
updated: 2026-09-13
---

# Amortized Analysis

← [[Career/Prep/topics/Complexity/Complexity|Complexity]]

> [!abstract]- Coverage — 2/6
> - [ ] [[#Idea]]
> - [x] [[#How it works]]
> - [ ] [[#Implementation]]
> - [ ] [[#Complexity]]
> - [x] [[#When to use it]]
> - [ ] [[#Gotchas]]

## Idea

When a algorithm can run theoretically at different rates per different input, we claim the average to be the true runtime, but note the best and worst case.

Like in a binary search, the worst case is the item not being in the list at all, we would check all log(n) iterations, but if it's the midpoint, we have a best case O(1) - just one single call. But on average we check log(n) items

## How it works

Worked case in the vault: `push`/`pop` on a dynamic array are O(1) amortised even though an individual resize is O(n) — [[Code/Algorithms/Stack|Stack]] § Array vs Linked List Implementation.

## Implementation

## Complexity

## When to use it

Splay trees are the canonical "amortised, not worst-case" structure: O(log n) amortised per operation with no balance metadata stored at all, at the cost of an individual operation that can be O(n) — [[Code/Algorithms/Binary Search Trees/BST Time Complexity|BST Time Complexity]] § Amortized Analysis.

## Gotchas

## Resources

- [Amortized Analysis (video)](https://www.youtube.com/watch?v=B3SpQZaAZP4&index=10&list=PL1BaGV1cIH4UhkL8a9bJGG356covJ76qN)

## Problems

_None yet._
