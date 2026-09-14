---
type: topic
group: Data Structures
tier: extra
confidence:
sections_total: 6
sections_done: 2
coverage: 0.33
status: learning
updated: 2026-09-13
---

# Augmented Data Structures

← [[Career/Prep/topics/Data Structures/Data Structures|Data Structures]]

> [!abstract]- Coverage — 2/6
> - [x] [[#Idea]]
> - [x] [[#How it works]]
> - [ ] [[#Implementation]]
> - [ ] [[#Complexity]]
> - [ ] [[#When to use it]]
> - [ ] [[#Gotchas]]

## Idea

Store an extra field at each node so a new query becomes O(log n) — a subtree-size field turns a BST into an order-statistic tree answering `select(k)` and `rank(x)` — [[Code/Algorithms/Binary Search Trees/BST Applications|BST Applications]] § 4. Order Statistic Trees.

## How it works

The general principle: an augmentation is maintainable when a node's augmented value is computable from its own value plus its children's augmented values — then it can be repaired along the O(log n) path an insert, delete, or rotation touches — [[Code/Algorithms/Binary Search Trees/BST Applications|BST Applications]] § General Augmentation Principle, § Maintaining Augmented Data.

## Implementation

## Complexity

## When to use it

## Gotchas

## Resources

- [CS 61B Lecture 39: Augmenting Data Structures](https://archive.org/details/ucberkeley_webcast_zksIj9O8_jc)

## Problems

_None yet._
