---
type: topic
group: Trees
tier: core
confidence:
sections_total: 6
sections_done: 0
coverage: 0.00
status: untouched
updated: 2026-09-01
---

# Balanced Search Trees

> [!abstract]- Coverage — 0/6
> - [ ] [[#Idea]]
> - [ ] [[#How it works]]
> - [ ] [[#Implementation]]
> - [ ] [[#Complexity]]
> - [ ] [[#When to use it]]
> - [ ] [[#Gotchas]]

## Idea

Know at least one type of balanced binary tree (and know how it's implemented).

"Among balanced search trees, AVL and 2/3 trees are now passé and red-black
trees seem to be more popular. A particularly interesting self-organizing
data structure is the splay tree, which uses rotations to move any accessed
key to the root." — Skiena.

Chose to aim at a splay tree, on the theory you rarely implement a balanced
search tree in an interview but the exposure is worth having; read a lot of
red-black tree code alongside it. No splay tree code has been written yet.

## How it works

- **AVL trees** — more rigidly balanced than red-black trees: slower insertion
  and removal, faster retrieval.
- **Splay trees** — self-organizing; every access rotates the accessed key to
  the root.
- **Red-black trees** — a translation of a 2-3 tree; give worst-case guarantees
  for insert/delete/search instead of AVL's stricter balance.
- **2-3 trees** — implementation involves different node types, so they're
  rarely used directly.
- **2-3-4 trees** — insertion/deletion are equivalent to color-flipping and
  rotations in red-black trees; mostly a teaching bridge to red-black.
- **N-ary (K-ary, M-ary) trees** — N/K is the branching factor; a binary tree
  is 2-ary, a 2-3 tree is 3-ary.

## Implementation

## Complexity

AVL trees support O(log n) search, insertion, and removal — more rigidly
balanced than red-black trees, so slower insert/remove but faster retrieval.

## When to use it

- **AVL**: attractive for structures built once and loaded without
  reconstruction, e.g. language/program dictionaries.
- **Splay trees**: caches, memory allocators, routers, garbage collectors,
  data compression, ropes, Windows NT (virtual memory, networking, file
  system code).
- **Red-black**: time-sensitive / real-time applications needing worst-case
  guarantees; the Linux Completely Fair Scheduler and Java's `HashMap`
  (since Java 8, for buckets with many collisions) use them.
- **2-3 trees**: faster inserts at the expense of slower searches than AVL;
  rarely used directly since red-black trees give similar guarantees more
  simply.
- **2-3-4 trees**: not often used in practice directly; valuable for
  understanding the logic behind red-black trees.

## Gotchas

> [!abstract] From coursework — needs review
> [[Self-Balancing BSTs]] and [[Tree Rotations]] under `Code/Algorithms` cover AVL
> and red-black. Written for class, not re-read since.

## Resources

- [Self-balancing binary search tree](https://en.wikipedia.org/wiki/Self-balancing_binary_search_tree)
- AVL: [MIT AVL Trees / AVL Sort (video)](https://www.youtube.com/watch?v=FNeL18KsWPc&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=6), [AVL Trees (video)](https://www.coursera.org/learn/data-structures/lecture/Qq5E0/avl-trees), [AVL Tree Implementation (video)](https://www.coursera.org/learn/data-structures/lecture/PKEBC/avl-tree-implementation), [Split And Merge](https://www.coursera.org/learn/data-structures/lecture/22BgE/split-and-merge), [[Review] AVL Trees (playlist) in 19 minutes (video)](https://www.youtube.com/playlist?list=PL9xmBV_5YoZOUFgdIeOPuH6cfSnNRMau-)
- Splay: [CS 61B: Splay Trees (video)](https://archive.org/details/ucberkeley_webcast_G5QIXywcJlY), MIT Lecture: Splay Trees (gets very mathy, but watch the last 10 minutes for sure) — [Video](https://www.youtube.com/watch?v=QnPl_Y6EqMo)
- Red-black: [Aduni - Algorithms - Lecture 4 (video, jumps to the starting point)](https://youtu.be/1W3x0f_RmUo?list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&t=3871), [Aduni - Algorithms - Lecture 5 (video)](https://www.youtube.com/watch?v=hm2GHwyKF1o&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&index=5), [Red-Black Tree](https://en.wikipedia.org/wiki/Red%E2%80%93black_tree), [An Introduction To Binary Search And Red Black Tree](https://www.topcoder.com/thrive/articles/An%20Introduction%20to%20Binary%20Search%20and%20Red-Black%20Trees), [[Review] Red-Black Trees (playlist) in 30 minutes (video)](https://www.youtube.com/playlist?list=PL9xmBV_5YoZNqDI8qfOZgzbqahCUmUEin)
- 2-3 trees: [23-Tree Intuition and Definition (video)](https://www.youtube.com/watch?v=C3SsdUqasD4&list=PLA5Lqm4uh9Bbq-E0ZnqTIa8LRaL77ica6&index=2), [Binary View of 23-Tree](https://www.youtube.com/watch?v=iYvBtGKsqSg&index=3&list=PLA5Lqm4uh9Bbq-E0ZnqTIa8LRaL77ica6), [2-3 Trees (student recitation) (video)](https://www.youtube.com/watch?v=TOb1tuEZ2X4&index=5&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp)
- 2-3-4 trees: [CS 61B Lecture 26: Balanced Search Trees (video)](https://archive.org/details/ucberkeley_webcast_zqrqYXkth6Q), [Bottom Up 234-Trees (video)](https://www.youtube.com/watch?v=DQdMYevEyE4&index=4&list=PLA5Lqm4uh9Bbq-E0ZnqTIa8LRaL77ica6), [Top Down 234-Trees (video)](https://www.youtube.com/watch?v=2679VQ26Fp4&list=PLA5Lqm4uh9Bbq-E0ZnqTIa8LRaL77ica6&index=5)
- N-ary trees: [K-Ary Tree](https://en.wikipedia.org/wiki/K-ary_tree)

## Problems

_None yet._
