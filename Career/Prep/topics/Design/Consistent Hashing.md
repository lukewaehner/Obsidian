---
type: topic
group: Design
tier: core
confidence:
---

# Consistent Hashing

> [!abstract]- Coverage — 0/6
> - [ ] [[#Idea]]
> - [ ] [[#How it works]]
> - [ ] [[#Implementation]]
> - [ ] [[#Complexity]]
> - [ ] [[#When to use it]]
> - [ ] [[#Gotchas]]

## Idea

A hashing scheme where adding or removing a node only remaps a small
fraction of keys, instead of the near-total remapping a naive `hash(key) %
n` scheme causes whenever `n` changes.

## How it works

Nodes and keys are hashed onto the same ring (a circular hash space); a key
belongs to the first node found walking clockwise from its position.
Adding or removing a node only affects the keys between it and its
neighbor on the ring — everything else keeps its assignment.

## Implementation

## Complexity

Remaps O(k/n) keys on a node join/leave, where k is the number of keys and
n the number of nodes — versus remapping nearly all of them under
`hash(key) % n`.

## When to use it

Distributed caches and databases where nodes are added or removed while the
system is running (autoscaling, node failure) and minimizing cache-miss /
data-movement storms on those events matters.

## Gotchas

Naive consistent hashing can distribute keys unevenly across a small number
of nodes — virtual nodes (each physical node hashed to multiple ring
positions) are the standard fix.

## Resources

- [Consistent Hashing](http://www.tom-e-white.com/2007/11/consistent-hashing.html)

## Problems

_None yet._
