# BST Definition

## What is a Binary Search Tree?

A **Binary Search Tree (BST)** is a rooted binary tree data structure that satisfies the **BST invariant**.

## BST Invariant

The BST property that must hold for every node in the tree:

1. The key of a node is **greater than** all keys in its left subtree
2. The key of a node is **smaller than** all keys in its right subtree

## Visual Example

```
        8
       / \
      3   10
     / \    \
    1   6   14
       / \   /
      4   7 13
```

In this tree:
- 8 is greater than all nodes in left subtree (3, 1, 6, 4, 7)
- 8 is smaller than all nodes in right subtree (10, 14, 13)
- This property holds recursively for every node

## Properties

### Ordering Property
An **in-order traversal** of a BST yields elements in **sorted order**.

For the tree above: 1, 3, 4, 6, 7, 8, 10, 13, 14

### Structure
- Each node has at most 2 children (binary tree)
- Left child < parent < right child
- Can be empty (NULL tree is a valid BST)

## Variants

### Handling Duplicates

Different conventions for duplicate keys:
1. **No duplicates allowed** (most common)
2. **Left subtree ≤ node < right subtree** (allow equal on left)
3. **Left subtree < node ≤ right subtree** (allow equal on right)
4. **Store count in node** (maintain unique keys with multiplicity)

## Related Topics

- [[BST Operations]] - How to search, insert, and delete
- [[Tree Rotations]] - Maintaining the invariant while restructuring
- [[Binary Trees]] - General binary tree structure
- [[In-Order Traversal]] - Yields sorted order in BSTs

---

**Source**: CS3000 Lecture 13
**Parent**: [[Binary Search Trees]]