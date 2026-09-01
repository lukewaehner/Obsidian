---
type: topic
group: Data Structures
tier: core
confidence:
---

# Linked Lists

> [!abstract]- Coverage — 5/6
> - [x] [[#Idea]]
> - [x] [[#How it works]]
> - [x] [[#Implementation]]
> - [ ] [[#Complexity]]
> - [x] [[#When to use it]]
> - [x] [[#Gotchas]]

## Idea

A linked list is a sequence of nodes, each holding a value and a pointer to the
next node — the shape lives in memory as scattered nodes connected by pointers,
not contiguous storage. See [[Linked List]]. A doubly linked list additionally
holds a pointer to the previous node — see [[Doubly Linked List]].

## How it works

Two-pointer / runner technique — [[Linked List]] § Two-Pointer Technique.

Doubly linked list operations: delete-given-node, insert-before, `pop_back`,
reverse traversal — [[Doubly Linked List]] (went past what the plan asked for).

## Implementation

Implemented a singly linked list — [[Linked List]] § Full Implementation:
`size()`, `empty()`, `value_at(index)`, `push_front(value)`, `pop_front()`,
`push_back(value)` (as `append`), `pop_back()`, `front()`, `back()`,
`insert(index, value)`, `erase(index)` (as `remove`), `value_n_from_end(n)`,
`reverse()`, `remove_value(value)`.

## Complexity

## When to use it

Know when a linked list beats an array, and when it doesn't — [[Linked List]].

## Gotchas

Edge cases: empty list, single node, head/tail updates — [[Linked List]].

Still open:

- [ ] Circular linked list — named in [[Linked List]] § Types, never worked through
- [ ] Pointer-to-pointer traversal (C-specific gotcha) — deliberately avoided; hurts
      readability and maintainability for the cleverness it buys

## Resources

- [Linked Lists CS50 Harvard University](https://www.youtube.com/watch?v=2T-A_GFuoTo&t=650s) - this builds the intuition.
- [Singly Linked Lists (video)](https://www.coursera.org/lecture/data-structures/singly-linked-lists-kHhgK)
- [CS 61B - Linked Lists 1 (video)](https://archive.org/details/ucberkeley_webcast_htzJdKoEmO0)
- [CS 61B - Linked Lists 2 (video)](https://archive.org/details/ucberkeley_webcast_-c4I3gFYe3w)
- [[Review] Linked lists in 4 minutes (video)](https://youtu.be/F8AbOfQwl1c)
- [C Code (video)](https://www.youtube.com/watch?v=QN6FPiD0Gzo) - not the whole video, just the portions about Node struct and memory allocation
- Linked List vs Arrays: [Core Linked Lists Vs Arrays (video)](https://www.coursera.org/lecture/data-structures-optimizing-performance/core-linked-lists-vs-arrays-rjBs9), [In The Real World Linked Lists Vs Arrays (video)](https://www.coursera.org/lecture/data-structures-optimizing-performance/in-the-real-world-lists-vs-arrays-QUaUd)
- [Why you should avoid linked lists (video)](https://www.youtube.com/watch?v=YQs6IC-vgmo)
- Gotcha: you need pointer-to-pointer knowledge (for when you pass a pointer to a
  function that may change the address where that pointer points) — [Pointers to Pointers](https://www.eskimo.com/~scs/cclass/int/sx8.html)
- Doubly-linked list: [Description (video)](https://www.coursera.org/lecture/data-structures/doubly-linked-lists-jpGKD)

## Problems

_None yet._
