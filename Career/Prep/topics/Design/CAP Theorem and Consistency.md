---
type: topic
group: Design
tier: core
confidence:
---

# CAP Theorem and Consistency

> [!abstract]- Coverage — 0/6
> - [ ] [[#Idea]]
> - [ ] [[#How it works]]
> - [ ] [[#Implementation]]
> - [ ] [[#Complexity]]
> - [ ] [[#When to use it]]
> - [ ] [[#Gotchas]]

## Idea

A distributed system can't simultaneously guarantee Consistency (every read
sees the latest write), Availability (every request gets a response), and
Partition tolerance (the system keeps working when nodes can't talk to each
other) — and partitions happen, so in practice the real choice is
consistency vs. availability during a partition.

## How it works

## Implementation

## Complexity

## When to use it

Naming CAP explicitly when justifying a datastore choice (e.g. "we chose
AP because staleness is acceptable but downtime isn't") is the interview
signal — reciting the theorem alone isn't the point.

## Gotchas

Cross-datacenter transactions make consistency expensive in a very concrete
way: coordinating a commit across datacenters costs real round-trip latency,
which is why many systems relax to eventual consistency rather than pay it.

## Resources

- [A plain English introduction to CAP Theorem](http://ksat.me/a-plain-english-introduction-to-cap-theorem)
- [Transactions Across Datacenters (video)](https://www.youtube.com/watch?v=srOgpXECblk)

## Problems

_None yet._
