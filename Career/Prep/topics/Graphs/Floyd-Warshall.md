---
type: topic
group: Graphs
tier: extra
confidence:
---

# Floyd-Warshall

> [!abstract]- Coverage — 0/6
> - [ ] [[#Idea]]
> - [ ] [[#How it works]]
> - [ ] [[#Implementation]]
> - [ ] [[#Complexity]]
> - [ ] [[#When to use it]]
> - [ ] [[#Gotchas]]

## Idea

All-pairs shortest paths by dynamic programming: for every intermediate
vertex k, try routing every pair (i, j) through k.

## How it works

## Implementation

## Complexity

O(V³) time, O(V²) space — worse per-pair than running Dijkstra from every
vertex on sparse graphs, but simpler and handles negative edges (no negative
cycles).

## When to use it

Dense graphs, or when all-pairs distances are needed rather than a single
source.

## Gotchas

## Resources

- [Synchronous Distributed Algorithms: Symmetry-Breaking, Shortest-Paths Spanning Trees (video)](https://www.youtube.com/watch?v=mUBmcbbJNf4&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp&index=27)
- [Asynchronous Distributed Algorithms: Shortest-Paths Spanning Trees (video)](https://www.youtube.com/watch?v=kQ-UQAzcnzA&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp&index=28)

## Problems

_None yet._
