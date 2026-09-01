---
type: topic
group: Graphs
tier: core
confidence:
sections_total: 6
sections_done: 0
coverage: 0.00
status: untouched
updated: 2026-09-01
---

# Topological Sort

> [!abstract]- Coverage — 0/6
> - [ ] [[#Idea]]
> - [ ] [[#How it works]]
> - [ ] [[#Implementation]]
> - [ ] [[#Complexity]]
> - [ ] [[#When to use it]]
> - [ ] [[#Gotchas]]

## Idea

A linear ordering of a DAG's vertices such that for every directed edge
(u, v), u comes before v. Requires the graph to be acyclic.

## How it works

## Implementation

DFS-based, using finish times — [[Topological Ordering]],
[[Code/Algorithms/Graphs/DAGs and Topological Ordering|DAGs and Topological Ordering]].

Still open:

- [ ] Check for a cycle (needed before starting, since a cycle means no
      topological order exists)
- [ ] Topological sort

## Complexity

## When to use it

Dependency resolution — build systems, course prerequisites, task scheduling.

## Gotchas

## Resources

- [Aduni: Graph Algorithms I - Topological Sorting, Minimum Spanning Trees, Prim's Algorithm - Lecture 6 (video)](https://www.youtube.com/watch?v=i_AQT_XfvD8&index=6&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm)

## Problems

_None yet._
