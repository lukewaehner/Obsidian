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

# Sorting Fundamentals

> [!abstract]- Coverage — 0/6
> - [ ] [[#Idea]]
> - [ ] [[#How it works]]
> - [ ] [[#Implementation]]
> - [ ] [[#Complexity]]
> - [ ] [[#When to use it]]
> - [ ] [[#Gotchas]]

## Idea

Every comparison sort is bounded below by Ω(n log n) comparisons. Stability —
whether equal elements keep their relative order — is a property of the
algorithm, not the data, and interview answers should name it for whichever
sort is being discussed.

## How it works

Which algorithms work on linked lists, which on arrays, which on both:
merge sort is doable on a linked list (no random access needed for the
merge step); most others assume array-style indexing. Sorting a linked list
in place is rarely the right call regardless.

## Implementation

## Complexity

Comparison-based sorts: Ω(n log n) lower bound. Non-comparison sorts
(counting, radix) can beat this under extra assumptions about the keys —
see [[Counting and Radix Sort]].

## When to use it

## Gotchas

## Resources

- [Sorting Algorithm Stability (Wikipedia)](https://en.wikipedia.org/wiki/Sorting_algorithm#Stability)
- [Stability In Sorting Algorithms (Stack Overflow)](http://stackoverflow.com/questions/1517793/stability-in-sorting-algorithms)
- [Stability In Sorting Algorithms (GeeksforGeeks)](http://www.geeksforgeeks.org/stability-in-sorting-algorithms/)
- [Sorting Algorithms - Stability (PDF)](http://homepages.math.uic.edu/~leon/cs-mcs401-s08/handouts/stability.pdf)
- [Merge Sort For Linked List (GeeksforGeeks)](http://www.geeksforgeeks.org/merge-sort-for-linked-list/)
- [UC Berkeley CS 61B Lecture 29: Sorting I (video)](https://archive.org/details/ucberkeley_webcast_EiUvYS2DT6I)
- [UC Berkeley CS 61B Lecture 30: Sorting II (video)](https://archive.org/details/ucberkeley_webcast_2hTY3t80Qsk)
- [UC Berkeley CS 61B Lecture 32: Sorting III (video)](https://archive.org/details/ucberkeley_webcast_Y6LOLpxg6Dc)
- [UC Berkeley CS 61B Lecture 33: Sorting V (video)](https://archive.org/details/ucberkeley_webcast_qNMQ4ly43p4)

## Problems

- [[Career/Prep/problems/Two Pointers/15 · 3Sum|15 · 3Sum]] · Medium · Two Pointers
