---
type: topic
group: Design
tier: extra
confidence:
sections_total: 6
sections_done: 0
coverage: 0.00
status: untouched
updated: 2026-09-01
---

# Consensus: Paxos and Raft

> [!abstract]- Coverage — 0/6
> - [ ] [[#Idea]]
> - [ ] [[#How it works]]
> - [ ] [[#Implementation]]
> - [ ] [[#Complexity]]
> - [ ] [[#When to use it]]
> - [ ] [[#Gotchas]]

## Idea

Consensus algorithms get a set of distributed nodes to agree on a single
value despite node failures and message delays — Paxos and Raft are the two
canonical protocols. Raft was explicitly designed to be more understandable
than Paxos while providing the same guarantees.

## How it works

Both rely on a majority-quorum: a value is committed once more than half
the nodes have accepted it, which guarantees any two quorums overlap and
therefore can't both commit conflicting values. Raft structures this around
an elected leader with terms, making the normal-case flow (leader proposes,
followers replicate) easier to reason about than Paxos's more general
protocol.

## Implementation

## Complexity

## When to use it

Distributed databases, coordination services (leader election, config
management), and anywhere multiple replicas must agree on an ordered log of
operations.

## Gotchas

Consensus is expensive — it costs a round trip to a majority of nodes per
decision — so it's used for coordination and metadata (leader election,
config), not as the data path for every read and write.

## Resources

- [Paxos Agreement - Computerphile (video)](https://www.youtube.com/watch?v=s8JqcZtvnsM)
- [An Introduction to the Raft Distributed Consensus Algorithm (video)](https://www.youtube.com/watch?v=P9Ydif5_qvE)
- [Raft: Easy-to-read paper](https://raft.github.io/)
- [Raft infographic](http://thesecretlivesofdata.com/raft/)

## Problems

_None yet._
