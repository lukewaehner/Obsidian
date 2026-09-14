---
type: topic
group: Graphs
tier: core
confidence:
sections_total: 6
sections_done: 3
coverage: 0.50
status: learning
updated: 2026-09-13
---

# Breadth-First Search

← [[Career/Prep/topics/Graphs/Graphs|Graphs]]

> [!abstract]- Coverage — 3/6
> - [ ] [[#Idea]]
> - [x] [[#How it works]]
> - [ ] [[#Implementation]]
> - [x] [[#Complexity]]
> - [x] [[#When to use it]]
> - [ ] [[#Gotchas]]

## Idea

Level-by-level traversal from a source vertex, using a queue instead of a
stack — the graph analog of tree level order.

## How it works

A queue is the whole algorithm: dequeue, visit, enqueue unvisited neighbours. Level-order traversal is the same loop with a per-level size snapshot — [[Code/Algorithms/Queue|Queue]] § 1. BFS (Breadth-First Search), § 2. Level Order Traversal; [[Code/Algorithms/Tree|Tree]].

## Implementation

Still open:

- [ ] BFS with adjacency list
- [ ] BFS with adjacency matrix

## Complexity

O(V+E) time on an adjacency list; O(V) space for the queue and visited set, which is the cost BFS pays over DFS's O(h) — [[Code/Algorithms/Queue|Queue]] § Time Complexity Summary.

## When to use it

Shortest path in an unweighted graph; know its complexity and trade-offs
against DFS before reaching for either.

Recognition cues for reaching for a queue at all — "nearest", "fewest steps", "level by level" — and the red flags that mean it is not a queue problem — [[Code/Algorithms/Queue|Queue]] § Problem-Solving Patterns: When to Think "Queue".

## Gotchas

## Resources

- [Breadth-First Search (MIT video)](https://www.youtube.com/watch?v=oFVYVzlvk9c&t=14s&ab_channel=MITOpenCourseWare)
- [Skiena: CSE373 2020 - Lecture 11 - Graph Traversal (video)](https://www.youtube.com/watch?v=ZTwjXj81NVY&list=PLOtl7M3yp-DX6ic0HGT0PUX_wiNmkWkXx&index=11)
- [Aduni: Graph Algorithms II - DFS, BFS, Kruskal's Algorithm, Union Find Data Structure - Lecture 7 (video)](https://www.youtube.com/watch?v=ufj5_bppBsA&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&index=7)

## Problems

_None yet._
