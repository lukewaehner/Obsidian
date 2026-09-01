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

# Concurrency and Parallel Programming

> [!abstract]- Coverage — 0/6
> - [ ] [[#Idea]]
> - [ ] [[#How it works]]
> - [ ] [[#Implementation]]
> - [ ] [[#Complexity]]
> - [ ] [[#When to use it]]
> - [ ] [[#Gotchas]]

## Idea

Concurrency is structuring a program as multiple logically-independent
tasks; parallelism is actually running them at the same time on multiple
cores — [[Code/Computer Systems/Concurrency/Concurrency vs Parallelism|Concurrency vs Parallelism]]
covers the distinction directly. See [[Processes and Threads]] for the
mechanisms.

## How it works

## Implementation

[[Code/Computer Systems/Concurrency/Concurrency|Concurrency]] and
[[Code/Computer Systems/Concurrency/Concurrency vs Parallelism|Concurrency vs Parallelism]]
cover this from the coursework side.

## Complexity

## When to use it

Parallelism pays off for CPU-bound work with multiple cores available;
concurrency alone (without parallelism) still helps for I/O-bound work by
overlapping waiting with other work.

## Gotchas

## Resources

- [Parallel Programming (Scala, Coursera)](https://www.coursera.org/learn/parprog1/home/week/1)
- [Efficient Python for High-Performance Parallel Computing (video)](https://www.youtube.com/watch?v=uY85GkaYzBk)

## Problems

_None yet._
