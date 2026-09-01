---
type: topic
group: Graphs
tier: extra
confidence:
---

# A* Search

> [!abstract]- Coverage — 0/6
> - [ ] [[#Idea]]
> - [ ] [[#How it works]]
> - [ ] [[#Implementation]]
> - [ ] [[#Complexity]]
> - [ ] [[#When to use it]]
> - [ ] [[#Gotchas]]

## Idea

Dijkstra plus a heuristic: prioritize frontier vertices by known distance so
far plus an estimate of the remaining distance to the goal.

## How it works

## Implementation

## Complexity

## When to use it

Pathfinding with a single known goal and a good admissible heuristic (e.g.
Manhattan/Euclidean distance on a grid) — worse fit than Dijkstra when there
is no useful heuristic or no single goal.

## Gotchas

An inadmissible heuristic (one that overestimates) breaks the optimality
guarantee.

## Resources

- [A* search algorithm (Wikipedia)](https://en.wikipedia.org/wiki/A*_search_algorithm)
- [A* Pathfinding (E01: algorithm explanation) (video)](https://www.youtube.com/watch?v=-L-WgKMFuhE)

## Problems

_None yet._
