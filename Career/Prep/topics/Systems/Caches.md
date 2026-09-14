---
type: topic
group: Systems
tier: core
confidence:
sections_total: 6
sections_done: 2
coverage: 0.33
status: learning
updated: 2026-09-13
---

# Caches

← [[Career/Prep/topics/Systems/Systems|Systems]]

> [!abstract]- Coverage — 2/6
> - [ ] [[#Idea]]
> - [ ] [[#How it works]]
> - [x] [[#Implementation]]
> - [ ] [[#Complexity]]
> - [x] [[#When to use it]]
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

The TLB is the cache that matters for address translation — without it every memory access costs an extra page-table walk — [[Code/Computer Systems/Memory Virtualization/Page Tables|Page Tables]], [[Code/Computer Systems/Memory Virtualization/Paging|Paging]]. The slab allocator is a cache of pre-initialised kernel objects, built for exactly this reason — [[Code/Computer Systems/Memory Virtualization/Slab Allocator|Slab Allocator]].

## Complexity

## When to use it

Cache-friendliness as a design constraint, not an afterthought: a sorted array beats a balanced tree partly on linear memory layout ([[Code/Algorithms/Binary Search Trees/Self-Balancing BSTs|Self-Balancing BSTs]] § When NOT to Use), and merge sort's sequential access is why it survives despite the extra array ([[Code/Algorithms/Sorts/Merge Sort|Merge Sort]] § Cache & Parallelism).

## Gotchas

Cache-unfriendly access patterns (e.g. iterating a 2D array in the wrong
order for the language's storage layout) can cost an order of magnitude in
real time despite identical Big-O — the memory hierarchy is invisible to
asymptotic analysis but not to a benchmark.

## Resources

- [MIT 6.004 L15: The Memory Hierarchy (video)](https://www.youtube.com/watch?v=vjYF_fAZI5E&list=PLrRW1w6CGAcXbMtDFj205vALOGmiRc82-&index=24)
- [MIT 6.004 L16: Cache Issues (video)](https://www.youtube.com/watch?v=ajgC3-pyGlk&index=25&list=PLrRW1w6CGAcXbMtDFj205vALOGmiRc82-)

## Problems

- [[Career/Prep/problems/Linked List/146 · LRU Cache|146 · LRU Cache]] · Medium · Linked List
