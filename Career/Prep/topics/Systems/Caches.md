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

# Caches

> [!abstract]- Coverage — 0/6
> - [ ] [[#Idea]]
> - [ ] [[#How it works]]
> - [ ] [[#Implementation]]
> - [ ] [[#Complexity]]
> - [ ] [[#When to use it]]
> - [ ] [[#Gotchas]]

## Idea

The memory hierarchy exists because fast memory is small and expensive and
slow memory is large and cheap — a CPU cache sits between registers and RAM,
exploiting locality of reference to make the common case fast. For the
application-level eviction pattern (hash map + doubly linked list), see
[[LRU Cache]].

## How it works

Caches are organized into lines, not individual bytes — a memory access
pulls in a whole cache line, which is why sequential access patterns
(spatial locality) are fast and scattered access patterns are slow even at
the same total byte count. Multiple levels (L1/L2/L3) trade size for speed
the further they sit from the CPU.

## Implementation

## Complexity

## When to use it

## Gotchas

Cache-unfriendly access patterns (e.g. iterating a 2D array in the wrong
order for the language's storage layout) can cost an order of magnitude in
real time despite identical Big-O — the memory hierarchy is invisible to
asymptotic analysis but not to a benchmark.

## Resources

- [MIT 6.004 L15: The Memory Hierarchy (video)](https://www.youtube.com/watch?v=vjYF_fAZI5E&list=PLrRW1w6CGAcXbMtDFj205vALOGmiRc82-&index=24)
- [MIT 6.004 L16: Cache Issues (video)](https://www.youtube.com/watch?v=ajgC3-pyGlk&index=25&list=PLrRW1w6CGAcXbMtDFj205vALOGmiRc82-)

## Problems

_None yet._
