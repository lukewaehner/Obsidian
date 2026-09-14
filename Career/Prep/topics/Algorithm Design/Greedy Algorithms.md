---
type: topic
group: Algorithm Design
tier: core
confidence:
sections_total: 6
sections_done: 4
coverage: 0.67
status: learning
updated: 2026-09-13
---

# Greedy Algorithms

← [[Career/Prep/topics/Algorithm Design/Algorithm Design|Algorithm Design]]

> [!abstract]- Coverage — 4/6
> - [x] [[#Idea]]
> - [x] [[#How it works]]
> - [ ] [[#Implementation]]
> - [x] [[#Complexity]]
> - [x] [[#When to use it]]
> - [ ] [[#Gotchas]]

## Idea

Build the solution one locally-optimal choice at a time and never reconsider — cheap to run, expensive to justify — [[Code/Algorithms/Greedy/Greedy Algorithm Pattern|Greedy Algorithm Pattern]].

## How it works

Three components every greedy algorithm needs: a ranking metric to sort by, a compatibility check for whether the next candidate can be taken, and a correctness proof — [[Code/Algorithms/Greedy/Greedy Algorithm Pattern|Greedy Algorithm Pattern]] § Essential Components.

## Implementation

[[Code/Algorithms/Greedy/Greedy|Greedy]] — coursework hub note; the plain
`Greedy` link is ambiguous with a problems folder note of the same name.

Also: [[Greedy Algorithm Pattern]], [[Greedy Stays Ahead Proof Technique]],
[[Interval Scheduling Problem]], [[Earliest Finish Time Rule]].

## Complexity

Usually the sort dominates: O(n log n) to rank, then one O(n) pass — [[Code/Algorithms/Greedy/Earliest Finish Time Rule|Earliest Finish Time Rule]] § Complexity.

## When to use it

Interval scheduling is the worked example, including the three rules that *look* reasonable and are wrong — earliest start, shortest duration, fewest conflicts — [[Code/Algorithms/Greedy/Interval Scheduling Problem|Interval Scheduling Problem]] § Failed Greedy Strategies; [[Code/Algorithms/Greedy/Earliest Finish Time Rule|Earliest Finish Time Rule]].

## Gotchas

Greedy only works when the problem has optimal substructure and the greedy
choice property — see [[Greedy vs Dynamic Programming]] for when it doesn't
and dynamic programming is needed instead.

## Resources

- [Greedy algorithm (Wikipedia)](https://en.wikipedia.org/wiki/Greedy_algorithm)

## Problems

- [[Career/Prep/problems/Sliding Window/121 · Best Time to Buy and Sell Stock|121 · Best Time to Buy and Sell Stock]] · Easy · Sliding Window
- [[Career/Prep/problems/Stack/853 · Car Fleet|853 · Car Fleet]] · Medium · Stack
- [[Career/Prep/problems/Two Pointers/11 · Container With Most Water|11 · Container With Most Water]] · Medium · Two Pointers
