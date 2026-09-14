---
type: topic
group: Trees
tier: core
confidence:
sections_total: 6
sections_done: 5
coverage: 0.83
status: learning
updated: 2026-09-13
---

# Binary Search Trees

← [[Career/Prep/topics/Trees/Trees|Trees]]

> [!abstract]- Coverage — 5/6
> - [x] [[#Idea]]
> - [x] [[#How it works]]
> - [ ] [[#Implementation]]
> - [x] [[#Complexity]]
> - [x] [[#When to use it]]
> - [x] [[#Gotchas]]

## Idea

What the BST invariant is — [[Tree]].

## How it works

Search, insert, and delete, with delete's three cases (leaf, one child, two children → replace with in-order successor) worked through — [[Code/Algorithms/Binary Search Trees/BST Operations|BST Operations]].

## Implementation

Implemented `insert(value)` — [[Tree]] § BST.

Still pending: `is_in_tree(value)`, `get_height()`, `delete_value(value)`,
`get_node_count()`, `print_values()` (in-order), `delete_tree()`,
`get_min()` / `get_max()`, `is_binary_search_tree()`, `get_successor(value)`.

## Complexity

Every operation is O(h), so the whole question is height: O(log n) balanced, O(n) degenerate, plus the comparison table against arrays and hash tables — [[Code/Algorithms/Binary Search Trees/BST Time Complexity|BST Time Complexity]].

## When to use it

The four things a BST buys over a hash table — sets, ordered maps, priority queues, and order-statistic queries — [[Code/Algorithms/Binary Search Trees/BST Applications|BST Applications]]. Consolidated single-note version: [[Code/Algorithms/Graphs/Binary Search Trees|Binary Search Trees]].

## Gotchas

> [!abstract] From coursework — needs review
> [[Code/Algorithms/Binary Search Trees/Binary Search Trees|Binary Search Trees]], [[BST Definition]],
> [[BST Operations]], [[BST Time Complexity]], [[Self-Balancing BSTs]], and
> [[Tree Rotations]] under `Code/Algorithms` cover search/insert/delete, height
> analysis, AVL and red-black. Written for class, not re-read since — and not yet
> reconciled with [[Tree]].

Sorted input into a naive BST produces a linked list and O(n) operations — the degenerate case that motivates balancing. Duplicate handling is a design decision the invariant does not make for you — [[Code/Algorithms/Binary Search Trees/BST Time Complexity|BST Time Complexity]] § Worst Case: Degenerate Tree; [[Code/Algorithms/Binary Search Trees/BST Definition|BST Definition]] § Handling Duplicates.

## Resources

- [Binary Search Tree Review (video)](https://www.youtube.com/watch?v=x6At0nzX92o&index=1&list=PLA5Lqm4uh9Bbq-E0ZnqTIa8LRaL77ica6)
- [Introduction (video)](https://www.coursera.org/learn/data-structures/lecture/E7cXP/introduction)
- [MIT (video)](https://www.youtube.com/watch?v=76dhtgZt38A&ab_channel=MITOpenCourseWare)
- C/C++: [Binary search tree - Implementation in C/C++ (video)](https://www.youtube.com/watch?v=COZK7NATh4k&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P&index=28), [BST implementation - memory allocation in stack and heap (video)](https://www.youtube.com/watch?v=hWokyBoo0aI&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P&index=29), [Find min and max element in a binary search tree (video)](https://www.youtube.com/watch?v=Ut90klNN264&index=30&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P), [Find the height of a binary tree (video)](https://www.youtube.com/watch?v=_pnqMz5nrRs&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P&index=31), [Binary tree traversal - breadth-first and depth-first strategies (video)](https://www.youtube.com/watch?v=9RHO6jU--GU&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P&index=32), [Binary tree: Level Order Traversal (video)](https://www.youtube.com/watch?v=86g8jAQug04&index=33&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P), [Binary tree traversal: Preorder, Inorder, Postorder (video)](https://www.youtube.com/watch?v=gm8DUJJhmY4&index=34&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P), [Check if a binary tree is a binary search tree or not (video)](https://www.youtube.com/watch?v=yEwSGhSsT0U&index=35&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P), [Delete a node from Binary Search Tree (video)](https://www.youtube.com/watch?v=gcULXE7ViZw&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P&index=36), [Inorder Successor in a binary search tree (video)](https://www.youtube.com/watch?v=5cPbNCrdotA&index=37&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P)
- Implement: [insert (LeetCode)](https://leetcode.com/problems/insert-into-a-binary-search-tree/submissions/987660183/), [get_height (GeeksforGeeks)](https://www.geeksforgeeks.org/find-the-maximum-depth-or-height-of-a-tree/), [is_binary_search_tree (LeetCode)](https://leetcode.com/problems/validate-binary-search-tree/)

## Problems

_None yet._
