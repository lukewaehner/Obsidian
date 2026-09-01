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

# Merge Sort

> [!abstract]- Coverage — 0/6
> - [ ] [[#Idea]]
> - [ ] [[#How it works]]
> - [ ] [[#Implementation]]
> - [ ] [[#Complexity]]
> - [ ] [[#When to use it]]
> - [ ] [[#Gotchas]]

## Idea

Divide and conquer: split the input in half, sort each half recursively,
then merge the two sorted halves — [[Career/Prep/topics/Algorithm Design/Divide and Conquer|Divide and Conquer]].

## How it works

## Implementation

[[Code/Algorithms/Sorts/Merge Sort|coursework notes]] — the note shares this
note's title, so link the coursework copy by full path, not the bare `Merge Sort` link.

Still open:

- [ ] Mergesort: O(n log n) average and worst case

## Complexity

O(n log n) average, best, and worst case. O(n) extra space for the array
version; the linked-list version can be done in place.

## When to use it

Stable sort needed, or sorting a linked list (no random access required for
the merge step) — see [Merge Sort For Linked List](http://www.geeksforgeeks.org/merge-sort-for-linked-list/)
in Resources.

## Gotchas

## Resources

- [Sedgewick - Mergesort (5 videos)](https://www.coursera.org/learn/algorithms-part1/home/week/3)
    - [1. Mergesort](https://www.coursera.org/lecture/algorithms-part1/mergesort-ARWDq)
    - [2. Bottom-up Mergesort](https://www.coursera.org/learn/algorithms-part1/lecture/PWNEl/bottom-up-mergesort)
    - [3. Sorting Complexity](https://www.coursera.org/lecture/algorithms-part1/sorting-complexity-xAltF)
    - [4. Comparators](https://www.coursera.org/lecture/algorithms-part1/comparators-9FYhS)
    - [5. Stability](https://www.coursera.org/learn/algorithms-part1/lecture/pvvLZ/stability)
- [Insertion Sort, Merge Sort (video)](https://www.youtube.com/watch?v=Kg4bqzAqRBM&index=3&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb)
- [Merge Sort (video)](https://www.youtube.com/watch?v=GCae1WNvnZM&index=3&list=PL89B61F78B552C1AB)
- [Merge sort in 3 minutes (video)](https://youtu.be/4VqmGXwpLqc)
- [Merge Sort For Linked List (GeeksforGeeks)](http://www.geeksforgeeks.org/merge-sort-for-linked-list/)
- [Using output array (C)](http://www.cs.yale.edu/homes/aspnes/classes/223/examples/sorting/mergesort.c)
- [Using output array (Python)](https://github.com/jwasham/practice-python/blob/master/merge_sort/merge_sort.py)
- [In-place (C++)](https://github.com/jwasham/practice-cpp/blob/master/merge_sort/merge_sort.cc)
- [Skiena: CSE373 2020 - Mergesort/Quicksort (video)](https://www.youtube.com/watch?v=jUf-UQ3a0kg&list=PLOtl7M3yp-DX6ic0HGT0PUX_wiNmkWkXx&index=8)

## Problems

_None yet._
