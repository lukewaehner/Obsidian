---
type: topic
group: Systems
tier: core
confidence:
sections_total: 6
sections_done: 3
coverage: 0.50
status: learning
updated: 2026-09-13
---

# Concurrency and Parallel Programming

← [[Career/Prep/topics/Systems/Systems|Systems]]

> [!abstract]- Coverage — 3/6
> - [ ] [[#Idea]]
> - [x] [[#How it works]]
> - [ ] [[#Implementation]]
> - [x] [[#Complexity]]
> - [ ] [[#When to use it]]
> - [x] [[#Gotchas]]

## Idea

Concurrency is structuring a program as multiple logically-independent
tasks; parallelism is actually running them at the same time on multiple
cores — [[Code/Computer Systems/Concurrency/Concurrency vs Parallelism|Concurrency vs Parallelism]]
covers the distinction directly. See [[Processes and Threads]] for the
mechanisms.

## How it works

Concurrency (interleaved, interacting units of execution) is not parallelism (simultaneous execution on multiple cores) — [[Code/Computer Systems/Concurrency/Concurrency vs Parallelism|Concurrency vs Parallelism]]; [[Code/Computer Systems/Concurrency/Concurrency|Concurrency]].

## Implementation

[[Code/Computer Systems/Concurrency/Concurrency|Concurrency]] and
[[Code/Computer Systems/Concurrency/Concurrency vs Parallelism|Concurrency vs Parallelism]]
cover this from the coursework side.

## Complexity

The synchronisation primitives and what each is for: mutexes for mutual exclusion ([[Code/Computer Systems/Concurrency/Mutex Locks|Mutex Locks]]) and semaphores for counting and signalling ([[Code/Computer Systems/Concurrency/Semaphores|Semaphores]]).

## When to use it

Parallelism pays off for CPU-bound work with multiple cores available;
concurrency alone (without parallelism) still helps for I/O-bound work by
overlapping waiting with other work.

## Gotchas

Deadlock's four Coffman conditions and how to break each one — [[Code/Computer Systems/Concurrency/Deadlocks|Deadlocks]]. Race conditions are non-deterministic and timing-dependent, so they vanish under a debugger — [[Code/Computer Systems/Concurrency/Concurrency|Concurrency]] § Debugging. Rust encodes the discipline in the type system instead: [[Code/Rust/Send and Sync|Send and Sync]], [[Code/Rust/Concurrency|Concurrency]].

## Resources

- [Parallel Programming (Scala, Coursera)](https://www.coursera.org/learn/parprog1/home/week/1)
- [Efficient Python for High-Performance Parallel Computing (video)](https://www.youtube.com/watch?v=uY85GkaYzBk)

## Problems

_None yet._
