---
type: topic
group: Complexity
tier: core
confidence:
sections_total: 6
sections_done: 5
coverage: 0.83
status: learning
updated: 2026-09-13
---

# Recurrences and the Master Theorem

← [[Career/Prep/topics/Complexity/Complexity|Complexity]]

> [!abstract]- Coverage — 5/6
> - [x] [[#Idea]]
> - [x] [[#How it works]]
> - [ ] [[#Implementation]]
> - [x] [[#Complexity]]
> - [x] [[#When to use it]]
> - [x] [[#Gotchas]]

## Idea

A recurrence states a recursive algorithm's runtime in terms of itself on smaller inputs: `T(n) = cost of recursive calls + cost of extra work` — [[Code/Algorithms/Recurrences|Recurrences]] § Core Idea.

## How it works

Three techniques, in order of generality: substitution (guess the form, prove by induction), recursion tree (expand, cost each level, sum across levels), and the Master Theorem as the divide-and-conquer shortcut — [[Code/Algorithms/Recurrences|Recurrences]] § Techniques for Solving Recurrences.

## Implementation

## Complexity

All four cases of `T(n) = aT(n/b) + f(n)`, given both in the `a·f(n/b)` vs `f(n)` comparison form and the standard `f(n)` vs `n^{log_b a}` form, with the geometric-series proof intuition for each — [[Code/Algorithms/Master Theorem|Master Theorem]].

## When to use it

Worked both ways on the two recurrences that matter most: binary search `T(n) = T(n/2) + 1 → Θ(log n)` and merge sort `T(n) = 2T(n/2) + n → Θ(n log n)` — [[Code/Algorithms/Master Theorem|Master Theorem]] § Examples, [[Code/Algorithms/Recurrences|Recurrences]] § Examples.

## Gotchas

Case 4 is a real case: when none of the three patterns match, the Master Theorem gives nothing and you fall back to substitution or a recursion tree — [[Code/Algorithms/Master Theorem|Master Theorem]] § Statement.

## Resources

- [[Recurrences]]
- [[Master Theorem]]
- TopCoder (includes recurrence relations and master theorem):
    - [Computational Complexity: Section 1](https://www.topcoder.com/thrive/articles/Computational%20Complexity%20part%20one)
    - [Computational Complexity: Section 2](https://www.topcoder.com/thrive/articles/Computational%20Complexity%20part%20two)

## Problems

_None yet._
