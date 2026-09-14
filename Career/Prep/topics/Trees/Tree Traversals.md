---
type: topic
group: Trees
tier: core
confidence:
sections_total: 6
sections_done: 6
coverage: 1.00
status: solid
updated: 2026-09-13
---

# Tree Traversals

← [[Career/Prep/topics/Trees/Trees|Trees]]

> [!abstract]- Coverage — 6/6
> - [x] [[#Idea]]
> - [x] [[#How it works]]
> - [x] [[#Implementation]]
> - [x] [[#Complexity]]
> - [x] [[#When to use it]]
> - [x] [[#Gotchas]]

## Idea

Preorder (self, left, right), inorder (left, self, right), and postorder (left, right, self) traversal — [[Tree]].

## How it works

BFS notes: level order (BFS, using a queue) — [[Tree]], [[Code/Algorithms/Queue|Queue]].

DFS notes: recursive and iterative with an explicit stack — [[Tree]], [[Code/Algorithms/Stack|Stack]].

## Implementation

DFS, recursive and iterative with an explicit stack — [[Tree]], [[Code/Algorithms/Stack|Stack]].

BFS / level-order with a queue — [[Tree]], [[Code/Algorithms/Queue|Queue]].

## Complexity

BFS: time complexity O(n); space complexity best O(1), worst O(n/2) = O(n).

DFS: time complexity O(n); space complexity best O(log n) (avg. height of
tree), worst O(n).

Traversal complexity overall: O(n) time, O(h) or O(n) space — [[Tree]].

## When to use it

Traversal choice follows the job: in-order for sorted output from a BST, pre-order for structural copies and prefix serialisation, post-order for teardown and bottom-up aggregation, level-order for anything depth-banded — [[Code/Algorithms/Tree|Tree]]. Parsing HTML/XML and abstract syntax trees are the everyday cases.

## Gotchas

Every traversal is O(n); the difference is space — O(h) for the recursive forms (which degrades to O(n) on a degenerate tree) versus O(n) for the BFS queue — [[Code/Algorithms/Tree|Tree]].

## Resources

- [Tree Traversal (video)](https://www.coursera.org/lecture/data-structures/tree-traversal-fr51b)
- [BFS(breadth-first search) and DFS(depth-first search) (video)](https://www.youtube.com/watch?v=uWL6FJhq5fM)
- [[Review] Breadth-first search in 4 minutes (video)](https://youtu.be/HZ5YTanv5QE)
- [[Review] Depth-first search in 4 minutes (video)](https://youtu.be/Urx87-NMm6c)
- [[Review] Tree Traversal (playlist) in 11 minutes (video)](https://www.youtube.com/playlist?list=PL9xmBV_5YoZO1JC2RgEi04nLy6D-rKk6b)

## Problems

_None yet._
