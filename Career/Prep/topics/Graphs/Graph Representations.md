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

# Graph Representations

← [[Career/Prep/topics/Graphs/Graphs|Graphs]]

> [!abstract]- Coverage — 4/6
> - [ ] [[#Idea]]
> - [x] [[#How it works]]
> - [ ] [[#Implementation]]
> - [x] [[#Complexity]]
> - [x] [[#When to use it]]
> - [x] [[#Gotchas]]

## Idea

Graphs show up everywhere in interview problems. There are four basic ways to
represent one in memory: objects and pointers, an adjacency matrix, an
adjacency list, and an adjacency map. Know each one's shape and its pros/cons.

## How it works

Adjacency matrix: an n×n grid, O(1) edge lookup, O(n²) space regardless of
edge count. Adjacency list: an array of per-vertex neighbor lists, O(V + E)
space, the usual default for sparse graphs — [[Code/Algorithms/Graphs/Graph Representations|coursework notes]].

## Implementation

Coursework covers the vocabulary and properties this note assumes:
[[Code/Algorithms/Graphs/Graph Basics|Graph Basics]],
[[Code/Algorithms/Graphs/Graph Terminology|Graph Terminology]],
[[Code/Algorithms/Graphs/Graph Types|Graph Types]],
[[Code/Algorithms/Graphs/Basic Graph Facts|Basic Graph Facts]].

Still open:

- [ ] Count connected components in a graph

## Complexity

Adjacency matrix: O(V²) space. Adjacency list: O(V + E) space, O(degree(v))
to enumerate v's neighbors vs. O(V) on a matrix.

## When to use it

When a question is asked, look for a graph-based solution first, then move on
if there isn't one. BFS and DFS trade-offs (queue vs. stack, level order vs.
depth-first) matter for picking a representation.

Picking between them: dense graphs and repeated edge-existence queries favour the matrix, sparse graphs and traversal favour the list — [[Code/Algorithms/Graphs/Graph Representations|Graph Representations]] § When to Use.

## Gotchas

The vocabulary a problem statement leans on — degree, path, cycle, connectedness, subgraph, complete, bipartite — and directed vs undirected, weighted vs unweighted, simple vs multigraph — [[Code/Algorithms/Graphs/Graph Terminology|Graph Terminology]], [[Code/Algorithms/Graphs/Graph Types|Graph Types]].

## Resources

- [Skiena: CSE373 2020 - Lecture 10 - Graph Data Structures (video)](https://www.youtube.com/watch?v=Sjk0xqWWPCc&list=PLOtl7M3yp-DX6ic0HGT0PUX_wiNmkWkXx&index=10)

## Problems

_None yet._
