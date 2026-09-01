---
type: topic
group: Design
tier: core
confidence:
sections_total: 6
sections_done: 0
coverage: 0.00
status: untouched
updated: 2026-09-01
---

# NoSQL and Data Modeling

> [!abstract]- Coverage — 0/6
> - [ ] [[#Idea]]
> - [ ] [[#How it works]]
> - [ ] [[#Implementation]]
> - [ ] [[#Complexity]]
> - [ ] [[#When to use it]]
> - [ ] [[#Gotchas]]

## Idea

Relational modeling normalizes data to eliminate redundancy and update
anomalies; NoSQL modeling often does the opposite on purpose — denormalizing
(embedding, duplicating) to make the read pattern you actually have cheap,
at the cost of write complexity and eventual consistency between copies.

## How it works

Normalization (1NF-4NF) is about eliminating redundancy in a relational
schema — see [[Code/Databases/Database Schemas/Database Schemas|Database Schemas]]
and [[Code/Databases/Entity-Relationship Diagrams/Entity-Relationship Diagrams|Entity-Relationship Diagrams]]
for the relational side. NoSQL patterns invert this for specific access
patterns: document stores embed related data together, wide-column stores
optimize for a known query shape, and key-value stores give up querying
entirely in exchange for O(1) lookup.

## Implementation

## Complexity

## When to use it

Choose NoSQL when the access pattern is known in advance and denormalizing
for it beats join cost; choose relational when the query shape isn't fixed
yet and normalization's flexibility is worth the join cost.

## Gotchas

Denormalization means the same fact can live in multiple places — an update
has to touch all of them, or the copies drift, which is a bug class
relational integrity constraints would have caught for free.

## Resources

- [NoSQL Patterns](http://horicky.blogspot.com/2009/11/nosql-patterns.html)
- [Database Normalization - 1NF, 2NF, 3NF and 4NF (video)](https://www.youtube.com/watch?v=UrYLYV7WSHM)

## Problems

_None yet._
