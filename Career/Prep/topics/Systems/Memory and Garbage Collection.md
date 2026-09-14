---
type: topic
group: Systems
tier: core
confidence:
sections_total: 6
sections_done: 5
coverage: 0.83
status: learning
updated: 2026-09-13
---

# Memory and Garbage Collection

← [[Career/Prep/topics/Systems/Systems|Systems]]

> [!abstract]- Coverage — 5/6
> - [ ] [[#Idea]]
> - [x] [[#How it works]]
> - [x] [[#Implementation]]
> - [x] [[#Complexity]]
> - [x] [[#When to use it]]
> - [x] [[#Gotchas]]

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

Virtual memory end to end: address spaces and protection ([[Code/Computer Systems/Memory Virtualization/Memory Protection|Memory Protection]]), paging and the page table ([[Code/Computer Systems/Memory Virtualization/Paging|Paging]], [[Code/Computer Systems/Memory Virtualization/Page Tables|Page Tables]]), and the virtual→physical translation itself ([[Code/Computer Systems/Memory Virtualization/Virtual Address Translation|Virtual Address Translation]]).

## Implementation

[[Code/Computer Systems/Memory Virtualization/Memory Virtualization|Memory Virtualization]]
covers OS-level memory management (paging, allocation strategies) — a
different layer from language-level garbage collection, but the two
interact (heap growth, page faults) in ways worth being able to name.

One level below that hub note, a heap allocator from the ground up — free list, splitting, coalescing, headers, and growing the heap via `sbrk` — [[Code/Computer Systems/Memory Virtualization/Free List|Free List]], [[Code/Computer Systems/Memory Virtualization/Splitting|Splitting]], [[Code/Computer Systems/Memory Virtualization/Coalescing|Coalescing]], [[Code/Computer Systems/Memory Virtualization/Headers and Metadata|Headers and Metadata]], [[Code/Computer Systems/Memory Virtualization/Growing the Heap|Growing the Heap]].

## Complexity

Placement policies compared on speed and fragmentation — first fit, next fit, best fit, worst fit — then the structures that beat all four: segregated lists, buddy allocation, slab — [[Code/Computer Systems/Memory Virtualization/Allocation Strategies|Allocation Strategies]], [[Code/Computer Systems/Memory Virtualization/Segregated Lists|Segregated Lists]], [[Code/Computer Systems/Memory Virtualization/Buddy Allocation|Buddy Allocation]], [[Code/Computer Systems/Memory Virtualization/Slab Allocator|Slab Allocator]].

## When to use it

The alternative to a collector: Rust's ownership and borrowing free memory deterministically at scope exit, with `Box`/`Rc`/`Arc` for the heap cases — [[Code/Rust/Memory Types|Memory Types]], [[Code/Rust/Borrowing|Borrowing]], [[Code/Rust/Smart Pointers|Smart Pointers]].

## Gotchas

Reference counting alone leaks cyclic structures (two objects referencing
each other with nothing else pointing to either) — this is exactly why
CPython needs a secondary cyclic collector rather than relying on refcounts
alone.

External fragmentation (free memory exists but not contiguously) and internal fragmentation (rounding waste inside an allocated block) are different problems with different fixes — [[Code/Computer Systems/Memory Virtualization/External Fragmentation|External Fragmentation]], [[Code/Computer Systems/Memory Virtualization/Internal Fragmentation|Internal Fragmentation]].

## Resources

- [GC in Python (video)](https://www.youtube.com/watch?v=iHVs_HkjdmI)
- [Deep Dive Java: Garbage Collection is Good!](https://www.infoq.com/presentations/garbage-collection-benefits)
- [Deep Dive Python: Garbage Collection in CPython (video)](https://www.youtube.com/watch?v=P-8Z0-MhdQs&list=PLdzf4Clw0VbOEWOS_sLhT_9zaiQDrS5AR&index=3)

## Problems

_None yet._
