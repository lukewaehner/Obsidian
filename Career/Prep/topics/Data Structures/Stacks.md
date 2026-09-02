---
type: topic
group: Data Structures
tier: core
confidence:
sections_total: 6
sections_done: 6
coverage: 1.00
status: solid
updated: 2026-09-01
---

# Stacks

> [!abstract]- Coverage — 6/6
> - [x] [[#Idea]] ✅ 2026-09-01
> - [x] [[#How it works]] ✅ 2026-09-01
> - [x] [[#Implementation]] ✅ 2026-09-01
> - [x] [[#Complexity]] ✅ 2026-09-01
> - [x] [[#When to use it]] ✅ 2026-09-01
> - [x] [[#Gotchas]] ✅ 2026-09-01

## Idea

Explain LIFO and the core operations — [[Code/Algorithms/Stack|Stack]].

## How it works

A stack is a data structure type, usually implemented with a standard array where data is stored and retrieved from the top - ergo the latest item added to the structure is what is retrieved first (last in, first out). Its a push and pop system.

## Implementation

Implemented with an array and with a linked list — [[Code/Algorithms/Stack|Stack]]
(the plan called the linked-list version optional; did it anyway).

## Complexity
Pushing and Appending is O(1) - generally dynamic sized arrays amortize down to O(1) to append to the back of a list, same with popping. Look at the vector implementation.

## When to use it

Recognize stack problems from the prompt — [[Code/Algorithms/Stack|Stack]] § Recognition Patterns.

Classic problems: balanced parentheses, RPN, next greater element, decode
string, min stack — [[Code/Algorithms/Stack|Stack]] § Common Problem Patterns.

## Gotchas

## Resources

- [Stacks (video)](https://www.coursera.org/lecture/data-structures/stacks-UdKzQ)
- [[Review] Stacks in 3 minutes (video)](https://youtu.be/KcT3aVgrrpU)

## Problems

- [[Career/Prep/problems/Stack/150 · Evaluate Reverse Polish Notation|150 · Evaluate Reverse Polish Notation]] · Medium · Stack
- [[Career/Prep/problems/Stack/155 · Min Stack|155 · Min Stack]] · Medium · Stack
- [[Career/Prep/problems/Stack/20 · Valid Parentheses|20 · Valid Parentheses]] · Easy · Stack
