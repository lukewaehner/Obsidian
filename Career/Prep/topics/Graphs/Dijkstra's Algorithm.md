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

# Dijkstra's Algorithm

← [[Career/Prep/topics/Graphs/Graphs|Graphs]]

> [!abstract]- Coverage — 3/6
> - [ ] [[#Idea]]
> - [x] [[#How it works]]
> - [ ] [[#Implementation]]
> - [x] [[#Complexity]]
> - [ ] [[#When to use it]]
> - [x] [[#Gotchas]]

## Idea

Single-source shortest path for graphs with non-negative edge weights: greedily
extend the shortest known distance to the closest unvisited vertex.

## How it works

Greedy frontier expansion: repeatedly settle the unsettled vertex with the smallest tentative distance, then relax its outgoing edges — with the loop invariant and the argument for why settling is final — [[Code/Algorithms/Dijkstra's Algorithm|Dijkstra's Algorithm]] § Algorithm Intuition, § Relaxation, § Correctness.

## Implementation

[[Code/Algorithms/Dijkstra's Algorithm|coursework notes]] — the note shares
this note's title, so link the coursework copy by full path, not the bare `Dijkstra's Algorithm` link.

Still open:

- [ ] Single-source shortest path (Dijkstra)

## Complexity

O((V+E) log V) with a binary heap, O(E + V log V) with a Fibonacci heap, O(V²) with a plain array scan — which is actually the right choice on a dense graph — [[Code/Algorithms/Dijkstra's Algorithm|Dijkstra's Algorithm]] § Time Complexity.

## When to use it

Non-negative weighted shortest path. Use Bellman-Ford instead when edges can
be negative — [[Bellman-Ford]].

## Gotchas

Breaks silently on negative edge weights — it never revisits a vertex once
finalized, so a later negative edge can never correct an already-settled
distance.

Why the negative-weight failure is structural rather than a fixable bug, plus the two implementation traps: path reconstruction needs a predecessor array, and a heap without decrease-key needs a settled check on pop to skip stale entries — [[Code/Algorithms/Dijkstra's Algorithm|Dijkstra's Algorithm]] § Why Non-Negative Weights Matter, § Common Mistakes.

## Resources

- [6.006 Single-Source Shortest Paths Problem (video)](https://www.youtube.com/watch?v=Aa2sqUhIn-E&index=15&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb)
- [6.006 Dijkstra (video)](https://www.youtube.com/watch?v=NSHizBK9JD8&t=1731s&ab_channel=MITOpenCourseWare)
- [6.006 Speeding Up Dijkstra (video)](https://www.youtube.com/watch?v=CHvQ3q_gJ7E&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=18)
- [Aduni: Graph Algorithms III: Shortest Path - Lecture 8 (video)](https://www.youtube.com/watch?v=DiedsPsMKXc&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&index=8)
- [[Review] Shortest Path Algorithms (playlist) in 16 minutes (video)](https://www.youtube.com/playlist?list=PL9xmBV_5YoZO-Y-H3xIC9DGSfVYJng9Yw)

## Problems

_None yet._
