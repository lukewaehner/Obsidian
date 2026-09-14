---
type: topic
group: Data Structures
tier: core
confidence:
sections_total: 6
sections_done: 2
coverage: 0.33
status: learning
updated: 2026-09-13
---

# LRU Cache

← [[Career/Prep/topics/Data Structures/Data Structures|Data Structures]]

> [!abstract]- Coverage — 2/6
> - [ ] [[#Idea]]
> - [x] [[#How it works]]
> - [ ] [[#Implementation]]
> - [ ] [[#Complexity]]
> - [ ] [[#When to use it]]
> - [x] [[#Gotchas]]

## Idea

An LRU cache combines a hash map with a doubly linked list. [[Doubly Linked List]]
§ LRU Cache names the pattern but doesn't implement it.

## How it works

Why the doubly linked list is the right list here: given a node reference, deletion is O(1) because you already hold `prev` — that is the whole reason the hash map stores node pointers — [[Code/Algorithms/Doubly Linked List|Doubly Linked List]] § LRU Cache - Classic Use Case, § Unique Advantages.

## Implementation

Pending: implement it (hash map + doubly linked list).

## Complexity

## When to use it

## Gotchas

The splice bugs that break an LRU in practice: updating only one direction, forgetting to check both head and tail on delete, and rewiring neighbours before setting the new node's own pointers — [[Code/Algorithms/Doubly Linked List|Doubly Linked List]] § Common Gotchas.

## Resources

- [The Magic of LRU Cache (100 Days of Google Dev) (video)](https://www.youtube.com/watch?v=R5ON3iwx78M)
- [Implementing LRU (video)](https://www.youtube.com/watch?v=bq6N7Ym81iI)
- [LeetCode - 146 LRU Cache (C++) (video)](https://www.youtube.com/watch?v=8-FZRAjR7qU)

## Problems

- [[Career/Prep/problems/Linked List/146 · LRU Cache|146 · LRU Cache]] · Medium · Linked List
