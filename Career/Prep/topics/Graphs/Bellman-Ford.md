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

# Bellman-Ford

← [[Career/Prep/topics/Graphs/Graphs|Graphs]]

> [!abstract]- Coverage — 3/6
> - [ ] [[#Idea]]
> - [x] [[#How it works]]
> - [ ] [[#Implementation]]
> - [x] [[#Complexity]]
> - [ ] [[#When to use it]]
> - [x] [[#Gotchas]]

## Idea

Single-source shortest path for graphs that may have negative edge weights,
by relaxing every edge V−1 times.

## How it works

Relax every edge `V−1` times — after round `k` every shortest path using at most `k` edges is correct — then one extra round: anything that still improves is reachable from a negative cycle — [[Code/Algorithms/Bellman-Ford Algorithm|Bellman-Ford Algorithm]] § Algorithm, § Loop Invariant, § Negative Cycle Detection.

## Implementation

[[Bellman-Ford Algorithm]] — coursework notes on the relaxation loop and
negative-cycle detection.

## Complexity

O(V·E), against Dijkstra's O((V+E) log V) — the price of handling negative weights. Early termination when a round changes nothing, and the SPFA queue-based variant, are the practical speedups — [[Code/Algorithms/Bellman-Ford Algorithm|Bellman-Ford Algorithm]] § Time Complexity, § Optimizations.

## When to use it

Negative edge weights, or when negative-cycle detection is itself the
question — otherwise prefer [[Career/Prep/topics/Graphs/Dijkstra's Algorithm|Dijkstra's Algorithm]] for its better time
complexity.

## Gotchas

Detecting that a negative cycle *exists* is not the same as knowing which vertices it poisons — that needs one more propagation pass — [[Code/Algorithms/Bellman-Ford Algorithm|Bellman-Ford Algorithm]] § Finding Vertices Affected by Negative Cycles.

## Resources

- [6.006 Bellman-Ford (video)](https://www.youtube.com/watch?v=f9cVS_URPc0&ab_channel=MITOpenCourseWare)
- [Aduni: Graph Algorithms III: Shortest Path - Lecture 8 (video)](https://www.youtube.com/watch?v=DiedsPsMKXc&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&index=8)
- [[Review] Shortest Path Algorithms (playlist) in 16 minutes (video)](https://www.youtube.com/playlist?list=PL9xmBV_5YoZO-Y-H3xIC9DGSfVYJng9Yw)

## Problems

_None yet._
