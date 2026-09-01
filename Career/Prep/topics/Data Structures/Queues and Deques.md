---
type: topic
group: Data Structures
tier: core
confidence:
---

# Queues and Deques

> [!abstract]- Coverage — 5/6
> - [x] [[#Idea]]
> - [ ] [[#How it works]]
> - [x] [[#Implementation]]
> - [x] [[#Complexity]]
> - [x] [[#When to use it]]
> - [x] [[#Gotchas]]

## Idea

Explain FIFO and the core operations — [[Code/Algorithms/Queue|Queue]].

## How it works

## Implementation

Implemented with a linked list and a tail pointer, and with a fixed-size
array / circular buffer — [[Code/Algorithms/Queue|Queue]].

## Complexity

- enqueue: O(1) (amortized, linked list and array [probing])
- dequeue: O(1) (linked list and array)
- empty: O(1) (linked list and array)

Know the cost of each operation, and why enqueue-at-head/dequeue-at-tail is
O(n) — [[Code/Algorithms/Queue|Queue]].

## When to use it

`collections.deque` and when to reach for it.

Queue-shaped problems: BFS, level-order, sliding window max, scheduling —
[[Code/Algorithms/Queue|Queue]].

## Gotchas

A bad implementation using a linked list where you enqueue at the head and
dequeue at the tail is O(n), because it needs the second-to-last element,
forcing a full traversal on every dequeue.

## Resources

- [Queue (video)](https://www.coursera.org/lecture/data-structures/queues-EShpq)
- [Circular buffer/FIFO](https://en.wikipedia.org/wiki/Circular_buffer)
- [[Review] Queues in 3 minutes (video)](https://youtu.be/D6gu-_tmEpQ)

## Problems

_None yet._
