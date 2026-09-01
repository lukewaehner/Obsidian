---
type: topic
group: Systems
tier: core
confidence:
sections_total: 6
sections_done: 0
coverage: 0.00
status: untouched
updated: 2026-09-01
---

# Memory and Garbage Collection

> [!abstract]- Coverage — 0/6
> - [ ] [[#Idea]]
> - [ ] [[#How it works]]
> - [ ] [[#Implementation]]
> - [ ] [[#Complexity]]
> - [ ] [[#When to use it]]
> - [ ] [[#Gotchas]]

## Idea

Garbage collection automates memory reclamation: the runtime tracks which
allocated objects are still reachable and frees the rest, trading manual
`free`/`delete` discipline for pause time and overhead.

## How it works

Reference counting (CPython's primary mechanism) frees an object the moment
its reference count hits zero, but can't collect reference cycles on its
own — CPython layers a cyclic collector on top for that case. Tracing
collectors (mark-and-sweep, generational) instead walk the object graph from
a set of roots and reclaim whatever wasn't reached.

## Implementation

[[Code/Computer Systems/Memory Virtualization/Memory Virtualization|Memory Virtualization]]
covers OS-level memory management (paging, allocation strategies) — a
different layer from language-level garbage collection, but the two
interact (heap growth, page faults) in ways worth being able to name.

## Complexity

## When to use it

## Gotchas

Reference counting alone leaks cyclic structures (two objects referencing
each other with nothing else pointing to either) — this is exactly why
CPython needs a secondary cyclic collector rather than relying on refcounts
alone.

## Resources

- [GC in Python (video)](https://www.youtube.com/watch?v=iHVs_HkjdmI)
- [Deep Dive Java: Garbage Collection is Good!](https://www.infoq.com/presentations/garbage-collection-benefits)
- [Deep Dive Python: Garbage Collection in CPython (video)](https://www.youtube.com/watch?v=P-8Z0-MhdQs&list=PLdzf4Clw0VbOEWOS_sLhT_9zaiQDrS5AR&index=3)

## Problems

_None yet._
