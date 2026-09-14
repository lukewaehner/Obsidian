---
type: topic
group: Algorithm Design
tier: core
confidence:
sections_total: 6
sections_done: 3
coverage: 0.50
status: learning
updated: 2026-09-13
---

# Recursion

← [[Career/Prep/topics/Algorithm Design/Algorithm Design|Algorithm Design]]

> [!abstract]- Coverage — 3/6
> - [x] [[#Idea]]
> - [x] [[#How it works]]
> - [ ] [[#Implementation]]
> - [x] [[#Complexity]]
> - [ ] [[#When to use it]]
> - [ ] [[#Gotchas]]

## Idea

Recursion runs on the call stack: each call pushes a frame holding its own locals and return address, and the base case is what stops the stack from growing — [[Code/Algorithms/Stack|Stack]] § 1. Function Call Stack; [[Code/Computer Systems/Stack & Functions|Stack & Functions]] § Stack Frames.

## How it works

How the call stack works and how recursion uses it —
[[Code/Algorithms/Stack|Stack]] § 1. Function Call Stack.

## Implementation

## Complexity

The runtime of a recursive function is a recurrence, and the depth is the space — [[Code/Algorithms/Recurrences|Recurrences]], [[Code/Algorithms/Master Theorem|Master Theorem]].

## When to use it

Still open:

- [ ] When it is appropriate to use recursion vs. an iterative approach

## Gotchas

Still open:

- [ ] How is tail recursion better than plain recursion, and when does the
      language/runtime actually optimize it away

## Resources

- [Stanford Programming Abstractions - Lecture 8 (video)](https://www.youtube.com/watch?v=gl3emqCuueQ&list=PLFE6E58F856038C69&index=8)
- [Stanford Programming Abstractions - Lecture 9 (video)](https://www.youtube.com/watch?v=uFJhEPrbycQ&list=PLFE6E58F856038C69&index=9)
- [Stanford Programming Abstractions - Lecture 10 (video)](https://www.youtube.com/watch?v=NdF1QDTRkck&index=10&list=PLFE6E58F856038C69)
- [Stanford Programming Abstractions - Lecture 11 (video)](https://www.youtube.com/watch?v=p-gpaIGRCQI&list=PLFE6E58F856038C69&index=11)
- [What Is Tail Recursion, Why Is It So Bad? (Quora)](https://www.quora.com/What-is-tail-recursion-Why-is-it-so-bad)
- [Tail Recursion (video)](https://www.coursera.org/lecture/programming-languages/tail-recursion-YZic1)
- [5 Simple Steps for Solving Any Recursive Problem (video)](https://youtu.be/ngCos392W4w)

## Problems

_None yet._
