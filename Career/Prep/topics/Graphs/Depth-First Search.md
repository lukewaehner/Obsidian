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

# Depth-First Search

← [[Career/Prep/topics/Graphs/Graphs|Graphs]]

> [!abstract]- Coverage — 4/6
> - [ ] [[#Idea]]
> - [x] [[#How it works]]
> - [ ] [[#Implementation]]
> - [x] [[#Complexity]]
> - [x] [[#When to use it]]
> - [x] [[#Gotchas]]

## Idea

Explore as far as possible along each branch before backtracking, using a
stack (explicit or the call stack) instead of a queue.

## How it works

Discovery and finish times drive everything: the `d[v]` / `f[v]` stamps classify every edge as tree, forward, back, or cross, and a back edge is exactly a cycle — [[Code/Algorithms/Graphs/Depth First Search|Depth First Search]] § Edge Classification, § Determining Edge Types; [[Code/Algorithms/Depth First Search|Depth First Search]] § Edge Classification Using Discovery/Finish Times.

## Implementation

Coursework covers discovery/finish times and edge classification —
[[Code/Algorithms/Depth First Search|coursework notes]].

Still open:

- [ ] DFS with adjacency list (recursive)
- [ ] DFS with adjacency list (iterative with stack)
- [ ] DFS with adjacency matrix (recursive)
- [ ] DFS with adjacency matrix (iterative with stack)

## Complexity

O(V+E) time on an adjacency list, O(V²) on a matrix; O(V) space, or O(h) for the recursion stack on a tree — [[Code/Algorithms/Graphs/Depth First Search|Depth First Search]] § Complexity Analysis.

## When to use it

Cycle detection, connected components, and as the basis for topological sort
and strongly connected components — know its complexity and trade-offs
against BFS before reaching for either.

Each of those applications worked out from the edge classification, plus path finding — [[Code/Algorithms/Graphs/Depth First Search|Depth First Search]] § Applications.

## Gotchas

Undirected DFS has no forward or cross edges — only tree and back — so the classification you memorise for digraphs does not transfer unchanged — [[Code/Algorithms/Depth First Search|Depth First Search]] § DFS in Undirected Graphs. A disconnected graph needs an outer loop over all vertices, giving a DFS *forest*, not one tree.

## Resources

- [Depth-First Search (MIT video)](https://www.youtube.com/watch?v=IBfWDYSffUU&t=32s&ab_channel=MITOpenCourseWare)
- [Skiena: CSE373 2020 - Lecture 12 - Depth First Search (video)](https://www.youtube.com/watch?v=KyordYB3BOs&list=PLOtl7M3yp-DX6ic0HGT0PUX_wiNmkWkXx&index=12)
- [Aduni: Graph Algorithms II - DFS, BFS, Kruskal's Algorithm, Union Find Data Structure - Lecture 7 (video)](https://www.youtube.com/watch?v=ufj5_bppBsA&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&index=7)

## Problems

_None yet._
