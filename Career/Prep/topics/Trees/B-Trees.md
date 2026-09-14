---
type: topic
group: Trees
tier: extra
confidence:
sections_total: 6
sections_done: 2
coverage: 0.33
status: learning
updated: 2026-09-13
---

# B-Trees

← [[Career/Prep/topics/Trees/Trees|Trees]]

> [!abstract]- Coverage — 2/6
> - [x] [[#Idea]]
> - [ ] [[#How it works]]
> - [ ] [[#Implementation]]
> - [ ] [[#Complexity]]
> - [x] [[#When to use it]]
> - [ ] [[#Gotchas]]

## Idea

Fun fact: it's a mystery, but the B could stand for Boeing, Balanced, or Bayer (co-inventor).

Generalise a BST to many children per node, keeping each node between `t−1` and `2t−1` keys, so one node fills one disk block and the tree stays shallow — [[Code/Algorithms/Binary Search Trees/Self-Balancing BSTs|Self-Balancing BSTs]] § B-Trees.

## How it works

## Implementation

## Complexity

## When to use it

Widely used in databases. Most modern filesystems use B-trees (or variants)
for quick random access to an arbitrary block in a file — turning a file
block address into a disk block (or cylinder/head/sector) address.

This is what a database index actually is: the B-tree is why `WHERE email = ...` becomes an O(log n) seek instead of a sequential scan, and why every index also costs disk and write throughput — [[Code/Databases/Indexes/Indexes|Indexes]].

## Gotchas

## Resources

- [B-Tree](https://en.wikipedia.org/wiki/B-tree)
- [B-Tree Datastructure](http://btechsmartclass.com/data_structures/b-trees.html)
- [Introduction to B-Trees (video)](https://www.youtube.com/watch?v=I22wEC1tTGo&list=PLA5Lqm4uh9Bbq-E0ZnqTIa8LRaL77ica6&index=6)
- [B-Tree Definition and Insertion (video)](https://www.youtube.com/watch?v=s3bCdZGrgpA&index=7&list=PLA5Lqm4uh9Bbq-E0ZnqTIa8LRaL77ica6)
- [B-Tree Deletion (video)](https://www.youtube.com/watch?v=svfnVhJOfMc&index=8&list=PLA5Lqm4uh9Bbq-E0ZnqTIa8LRaL77ica6)
- [MIT 6.851 - Memory Hierarchy Models (video)](https://www.youtube.com/watch?v=V3omVLzI0WE&index=7&list=PLUl4u3cNGP61hsJNdULdudlRL493b-XZf) — covers cache-oblivious B-Trees; the first 37 minutes are very technical and may be skipped
- [[Review] B-Trees (playlist) in 26 minutes (video)](https://www.youtube.com/playlist?list=PL9xmBV_5YoZNFPPv98DjTdD9X6UI9KMHz)

## Problems

_None yet._
