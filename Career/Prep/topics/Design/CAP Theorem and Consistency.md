---
type: topic
group: Design
tier: core
confidence:
sections_total: 6
sections_done: 1
coverage: 0.17
status: learning
updated: 2026-09-13
---

# CAP Theorem and Consistency

← [[Career/Prep/topics/Design/Design|Design]]

> [!abstract]- Coverage — 1/6
> - [ ] [[#Idea]]
> - [x] [[#How it works]]
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

The single-node version of the same trade-off, where it is concrete: isolation levels trade consistency for throughput, and each level is defined by which anomaly it permits — dirty read, non-repeatable read, phantom — [[Code/Databases/Transactions/Isolation Levels|Isolation Levels]], [[Code/Databases/Transactions/Transactions|Transactions]], [[Code/Databases/Transactions/Locking|Locking]].

## Implementation

The distributed treatment is coursework in progress — [[Courses/Distributed Systems/Distributed Systems|Distributed Systems]] covers quorums, Paxos, and the Dynamo/Cassandra and GFS/BigTable/Spanner case studies from week 7 on. Those week notes are still scaffolds.

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
