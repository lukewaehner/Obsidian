---
type: topic
group: Sorting & Searching
tier: core
confidence:
---

# Heapsort

> [!abstract]- Coverage — 0/6
> - [ ] [[#Idea]]
> - [ ] [[#How it works]]
> - [ ] [[#Implementation]]
> - [ ] [[#Complexity]]
> - [ ] [[#When to use it]]
> - [ ] [[#Gotchas]]

## Idea

Build a max-heap from the array, then repeatedly swap the root with the last
element and sift down — see [[Heaps and Priority Queues]] for the underlying
structure.

## How it works

## Implementation

## Complexity

O(n log n) average, best, and worst case. O(1) extra space — sorts in place.

## When to use it

Guaranteed O(n log n) with O(1) space and stability isn't required — the one
comparison sort that gets both without merge sort's extra space.

## Gotchas

Not stable, unlike merge sort.

## Resources

- [Heap sort in 4 minutes (video)](https://youtu.be/2DmK_H7IdTo)

## Problems

_None yet._
