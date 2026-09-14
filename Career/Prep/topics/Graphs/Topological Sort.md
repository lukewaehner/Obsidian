---
type: topic
group: Graphs
tier: core
confidence:
sections_total: 6
sections_done: 4
coverage: 0.67
status: learning
updated: 2026-09-13
---

# Topological Sort

← [[Career/Prep/topics/Graphs/Graphs|Graphs]]

> [!abstract]- Coverage — 4/6
> - [ ] [[#Idea]]
> - [x] [[#How it works]]
> - [ ] [[#Implementation]]
> - [x] [[#Complexity]]
> - [x] [[#When to use it]]
> - [x] [[#Gotchas]]

## Idea

A linear ordering of a DAG's vertices such that for every directed edge
(u, v), u comes before v. Requires the graph to be acyclic.

## How it works

Two algorithms with the same output. Kahn's: repeatedly emit a vertex of in-degree 0 and decrement its neighbours. DFS: emit vertices in decreasing finish time, with the proof of why that ordering is valid — [[Code/Algorithms/Topological Ordering|Topological Ordering]]; [[Code/Algorithms/Graphs/DAGs and Topological Ordering|DAGs and Topological Ordering]].

## Implementation

DFS-based, using finish times — [[Topological Ordering]],
[[Code/Algorithms/Graphs/DAGs and Topological Ordering|DAGs and Topological Ordering]].

Still open:

- [ ] Check for a cycle (needed before starting, since a cycle means no
      topological order exists)
- [ ] Topological sort

## Complexity

Both are O(V+E). Kahn's needs an in-degree array and a worklist; the DFS version needs only the recursion stack and a reversed output list — [[Code/Algorithms/Topological Ordering|Topological Ordering]] § Comparing the Two Algorithms.

## When to use it

Dependency resolution — build systems, course prerequisites, task scheduling.

Any prerequisite/dependency ordering — course plans, build graphs, task scheduling — and as a cycle test: a graph has a topological order iff it is a DAG — [[Code/Algorithms/Graphs/DAGs and Topological Ordering|DAGs and Topological Ordering]] § Existence, § Common Applications.

## Gotchas

The ordering is generally not unique, so a test that compares against one expected array is wrong — [[Code/Algorithms/Topological Ordering|Topological Ordering]] § Non-Uniqueness.

## Resources

- [Aduni: Graph Algorithms I - Topological Sorting, Minimum Spanning Trees, Prim's Algorithm - Lecture 6 (video)](https://www.youtube.com/watch?v=i_AQT_XfvD8&index=6&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm)

## Problems

_None yet._
