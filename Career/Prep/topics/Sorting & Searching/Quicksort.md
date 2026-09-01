---
type: topic
group: Sorting & Searching
tier: core
confidence:
---

# Quicksort

> [!abstract]- Coverage — 0/6
> - [ ] [[#Idea]]
> - [ ] [[#How it works]]
> - [ ] [[#Implementation]]
> - [ ] [[#Complexity]]
> - [ ] [[#When to use it]]
> - [ ] [[#Gotchas]]

## Idea

Divide and conquer: pick a pivot, partition the array around it, recurse on
each side — [[Divide and Conquer]].

## How it works

## Implementation

[[Code/Algorithms/Sorts/Quick Sort|Quick Sort]] — coursework notes on
pivoting as a sorting strategy.

Still open:

- [ ] Quicksort O(n log n) average case

## Complexity

O(n log n) average case, O(n²) worst case (already-sorted input with a naive
pivot choice) — randomized pivot selection makes the worst case
astronomically unlikely rather than eliminating it.

## When to use it

## Gotchas

Not stable. Worst case is real, not just theoretical, on adversarial or
already-sorted input with a fixed pivot strategy.

## Resources

- [Sedgewick - Quicksort (4 videos)](https://www.coursera.org/learn/algorithms-part1/home/week/3)
    - [1. Quicksort](https://www.coursera.org/lecture/algorithms-part1/quicksort-vjvnC)
    - [3. Duplicate Keys](https://www.coursera.org/lecture/algorithms-part1/duplicate-keys-XvjPd)
    - [4. System Sorts](https://www.coursera.org/lecture/algorithms-part1/system-sorts-QBNZ7)
- [Quicksort (video)](https://www.youtube.com/watch?v=y_G9BkAm6B8&index=4&list=PL89B61F78B552C1AB)
- [Quick sort in 4 minutes (video)](https://youtu.be/Hoixgm4-P4M)
- [Implementation (C)](http://www.cs.yale.edu/homes/aspnes/classes/223/examples/randomization/quick.c)
- [Implementation (C)](https://github.com/jwasham/practice-c/blob/master/quick_sort/quick_sort.c)
- [Implementation (Python)](https://github.com/jwasham/practice-python/blob/master/quick_sort/quick_sort.py)
- [Randomization: Matrix Multiply, Quicksort, Freivalds' algorithm (video)](https://www.youtube.com/watch?v=cNB2lADK3_s&index=8&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp)
- [Skiena: CSE373 2020 - Mergesort/Quicksort (video)](https://www.youtube.com/watch?v=jUf-UQ3a0kg&list=PLOtl7M3yp-DX6ic0HGT0PUX_wiNmkWkXx&index=8)

## Problems

_None yet._
