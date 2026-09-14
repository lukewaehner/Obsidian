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

# Trees Intro and Terminology

← [[Career/Prep/topics/Trees/Trees|Trees]]

> [!abstract]- Coverage — 5/6
> - [x] [[#Idea]]
> - [x] [[#How it works]]
> - [x] [[#Implementation]]
> - [ ] [[#Complexity]]
> - [x] [[#When to use it]]
> - [x] [[#Gotchas]]

## Idea

Terminology: root, node, height, depth, arity — [[Tree]].

## How it works

A tree as a special graph: connected and acyclic, `n − 1` edges, unique path between any two vertices — and the equivalence that any two of those three properties imply the third — [[Code/Algorithms/Graphs/Trees and Rooted Trees|Trees and Rooted Trees]]; [[Code/Algorithms/Graphs/Graph Terminology|Graph Terminology]] § Trees.

## Implementation

Rooting an unrooted tree, and the parent/child/ancestor/descendant/level vocabulary that follows from the choice of root — [[Code/Algorithms/Graphs/Trees and Rooted Trees|Trees and Rooted Trees]] § Rooted Trees. An n-ary `TreeNode` with a `children` list — [[Code/Algorithms/Tree|Tree]].

## Complexity

## When to use it

Real uses: HTML/XML parsing, ASTs, hierarchies — [[Tree]].

## Gotchas

General tree, n-ary tree, and binary tree are different constraints, and "binary tree" alone says nothing about ordering — that is the BST invariant, a separate thing — [[Code/Algorithms/Tree|Tree]].

## Resources

- [Intro to Trees (video)](https://www.coursera.org/lecture/data-structures/trees-95qda)

## Problems

_None yet._
