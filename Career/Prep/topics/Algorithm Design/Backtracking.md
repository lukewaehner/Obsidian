---
type: topic
group: Algorithm Design
tier: core
confidence:
sections_total: 6
sections_done: 1
coverage: 0.17
status: learning
updated: 2026-09-13
---

# Backtracking

← [[Career/Prep/topics/Algorithm Design/Algorithm Design|Algorithm Design]]

> [!abstract]- Coverage — 1/6
> - [x] [[#Idea]]
> - [ ] [[#How it works]]
> - [ ] [[#Implementation]]
> - [ ] [[#Complexity]]
> - [ ] [[#When to use it]]
> - [ ] [[#Gotchas]]

## Idea

DFS over a space of partial solutions, undoing the last choice when a branch cannot be completed — the same traversal, with state that is mutated on the way down and restored on the way up — [[Code/Algorithms/Graphs/Depth First Search|Depth First Search]]; [[Code/Algorithms/Stack|Stack]] § 4. DFS (Depth-First Search).

## How it works

Builds candidates incrementally and abandons ("backtracks" from) a candidate
as soon as it can't possibly lead to a valid solution — recursion is the
usual mechanism, so this builds on
[[Career/Prep/topics/Algorithm Design/Recursion|Recursion]].

## Implementation

Backtracking blueprint: [Java](https://leetcode.com/problems/combination-sum/discuss/16502/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partitioning)),
[Python](https://leetcode.com/problems/combination-sum/discuss/429538/General-Backtracking-questions-solutions-in-Python-for-reference-%3A).

## Complexity

## When to use it

Combinatorial search: subsets, permutations, combination sum, palindrome
partitioning, N-Queens — anywhere the search space is pruned as it's built.

## Gotchas

## Resources

- [Backtracking (Wikipedia)](https://en.wikipedia.org/wiki/Backtracking)
- [Stanford Programming Abstractions - Lecture 8 (video)](https://www.youtube.com/watch?v=gl3emqCuueQ&list=PLFE6E58F856038C69&index=8)
- [Stanford Programming Abstractions - Lecture 9 (video)](https://www.youtube.com/watch?v=uFJhEPrbycQ&list=PLFE6E58F856038C69&index=9)
- [Stanford Programming Abstractions - Lecture 10 (video)](https://www.youtube.com/watch?v=NdF1QDTRkck&index=10&list=PLFE6E58F856038C69)
- [Stanford Programming Abstractions - Lecture 11 (video)](https://www.youtube.com/watch?v=p-gpaIGRCQI&list=PLFE6E58F856038C69&index=11)

## Problems

_None yet._
