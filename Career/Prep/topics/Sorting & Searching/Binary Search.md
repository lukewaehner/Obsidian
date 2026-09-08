---
type: topic
group: Sorting & Searching
tier: core
confidence:
sections_total: 6
sections_done: 3
coverage: 0.50
status: learning
updated: 2026-09-01
---

# Binary Search

> [!abstract]- Coverage — 3/6
> - [x] [[#Idea]]
> - [ ] [[#How it works]]
> - [x] [[#Implementation]]
> - [ ] [[#Complexity]]
> - [ ] [[#When to use it]]
> - [x] [[#Gotchas]]

## Idea

The invariant that keeps the search space provably shrinking, and why that
makes it O(log n) — [[Binary Search 1|Binary Search 1]].

## How it works

take two pointers to the start and end of a sorted list. 
- l = start
- r = end of the list len(list) - 1
compute the midpoint
- m = l + (r - l) // 2 for safe overflow computation
if the target value is == m, you are done. return the index being mid
if the target value is > m, l = m + 1
if the target value is < m, r = m - 1

This repeatedly shrinks the searchable window in half.

We already know that consistent dividing by two can be represented as O(logn)

## Implementation

Implemented iteratively and recursively over a sorted array —
[[Binary Search 1|Binary Search 1]].

Still open:

- [ ] Variations as working code: first/last occurrence, lower/upper bound,
      search on answer space — listed in [[Binary Search 1|Binary Search 1]]
      § Variations, not implemented

## Complexity

O(logn) time, best O(1) - the middle of the array is the target
O(1) space complexity in iterative approach with 3 extra pointers, O(logn) recursively for call stack overhead

## When to use it

## Gotchas

Classic pitfalls: overflow on `mid`, off-by-one bounds, infinite loop from a
bound that never moves — [[Binary Search 1|Binary Search 1]] § Common Pitfalls.

## Resources

- [Binary Search (video)](https://www.youtube.com/watch?v=D5SrAga1pno)
- [Binary Search (Khan Academy video)](https://www.khanacademy.org/computing/computer-science/algorithms/binary-search/a/binary-search)
- [Binary search detail (TopCoder)](https://www.topcoder.com/thrive/articles/Binary%20Search)
- [Binary search blueprint (LeetCode discussion)](https://leetcode.com/discuss/general-discussion/786126/python-powerful-ultimate-binary-search-template-solved-many-problems)
- [Binary search in 4 minutes (video)](https://youtu.be/fDKIpRe8GW4)

## Problems

- [[Career/Prep/problems/Binary Search/153 · Find Minimum in Rotated Sorted Array|153 · Find Minimum in Rotated Sorted Array]] · Medium · Binary Search
- [[Career/Prep/problems/Binary Search/33 · Search in Rotated Sorted Array|33 · Search in Rotated Sorted Array]] · Medium · Binary Search
- [[Career/Prep/problems/Binary Search/704 · Binary Search|704 · Binary Search]] · Easy · Binary Search
- [[Career/Prep/problems/Binary Search/74 · Search a 2D Matrix|74 · Search a 2D Matrix]] · Medium · Binary Search
- [[Career/Prep/problems/Binary Search/875 · Koko Eating Bananas|875 · Koko Eating Bananas]] · Medium · Binary Search
