---
type: topic
group: Math & Bits
tier: extra
confidence:
sections_total: 6
sections_done: 0
coverage: 0.00
status: untouched
updated: 2026-09-01
---

# Geometry and Convex Hull

> [!abstract]- Coverage — 0/6
> - [ ] [[#Idea]]
> - [ ] [[#How it works]]
> - [ ] [[#Implementation]]
> - [ ] [[#Complexity]]
> - [ ] [[#When to use it]]
> - [ ] [[#Gotchas]]

## Idea

The convex hull of a point set is the smallest convex polygon containing
every point — the geometric analog of "find the boundary."

## How it works

Graham scan and Jarvis march are the two classic hull algorithms: Graham
scan sorts points by angle around a pivot and sweeps once; Jarvis march
("gift wrapping") walks the boundary directly. A divide-and-conquer approach
also exists, splitting the point set and merging hulls — [[Career/Prep/topics/Algorithm Design/Divide and Conquer|Divide and Conquer]].

## Implementation

## Complexity

Graham scan: O(n log n), dominated by the angular sort. Jarvis march: O(nh)
where h is the number of hull points — better than Graham scan only when h
is small.

## When to use it

## Gotchas

## Resources

- [Graph Alg. IV: Intro to geometric algorithms - Lecture 9 (video)](https://youtu.be/XIAQRlNkJAw?list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&t=3164)
- [Geometric Algorithms: Graham & Jarvis - Lecture 10 (video)](https://www.youtube.com/watch?v=J5aJEcOr6Eo&index=10&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm)
- [Divide & Conquer: Convex Hull, Median Finding (video)](https://www.youtube.com/watch?v=EzeYI7p9MjU&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp&index=2)

## Problems

_None yet._
