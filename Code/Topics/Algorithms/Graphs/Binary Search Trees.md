---
tags: [algorithms, data-structures, trees, binary-search-tree]
---

# Binary Search Trees

## Definition
A **Binary Search Tree (BST)** is a rooted binary tree data structure satisfying the BST invariant:
- The key of a node is **greater than** all keys in the left subtree
- The key of a node is **smaller than** all keys in the right subtree

```
       8
      / \
     3   10
    / \    \
   1   6   14
      / \  /
     4  7 13
```

## Operations

All operations depend on searching, which follows the tree structure.

### Search
Search for a key $k$:
1. Start at root
2. If $k$ equals current node, found!
3. If $k <$ current node, go left
4. If $k >$ current node, go right
5. Repeat until found or reach null

### Insert
Insert new key $k$:
1. Search for where $k$ should be
2. When you reach a null position, insert $k$ there
3. Insertion requires searching, which is like binary search

### Delete
Delete existing key $k$:
1. Find the node with key $k$
2. Three cases:
   - **No children** (leaf): Simply remove
   - **One child**: Replace node with its child
   - **Two children**: Replace with in-order successor (leftmost node in right subtree) or in-order predecessor (rightmost node in left subtree), then delete that node

Deletion also requires rewriting/searching.

## Time Complexity

### Operations
Every operation depends on searching time:
- **Search**: $O(h)$ where $h$ is height
- **Insert**: $O(h)$ (search + constant time)
- **Delete**: $O(h)$ (search + constant time)

### Height Analysis
Searching might require going all the way to a leaf node.

**Worst case height**: $O(n)$ 
- When tree becomes a linear chain (insert sorted sequence)
- Example: inserting 1, 9, 10, 17, 27 in order creates a path

**Best case height**: $O(\log n)$
- When tree is balanced
- Number of nodes roughly doubles at each level

**Time for BST operations**: $O(\text{height}(\text{tree}))$

## Self-Balancing BSTs

To maintain $O(\log n)$ height, use self-balancing trees.

### Tree Rotations
Restructure the tree while maintaining BST property.

**Left Rotation** and **Right Rotation** are inverse operations:
```
    y              x
   / \            / \
  x   γ    ⟺    α   y
 / \                / \
α   β              β   γ
```

### Four Rotation Cases
1. **Left-Left Case**: Right rotation at root
2. **Right-Right Case**: Left rotation at root
3. **Left-Right Case**: Left rotation at pivot, then right rotation at root
4. **Right-Left Case**: Right rotation at pivot, then left rotation at root

### Common Implementations
- **AVL Trees**: Maintain height balance at each node
- **Red-Black Trees**: Use coloring to maintain balance

### Assumption
We assume any BST we work with is **self-balancing**, giving us:
- **Insert**: $O(\log n)$
- **Delete**: $O(\log n)$
- **Search**: $O(\log n)$

Where $n$ is the number of nodes before the operation.

## Applications

BSTs provide a flexible foundation for many data structures:

### 1. Sets
Store elements in BST for $O(\log n)$ membership testing.
- **Contains**: $O(\log n)$

### 2. Associative Arrays (Dictionaries/Maps)
Store key-value pairs using keys in BST.
- **Lookup**: $O(\log n)$
- **Insert**: $O(\log n)$
- **Update**: $O(\log n)$
- **Delete**: $O(\log n)$

### 3. Priority Queues
Store priorities in BST.
- **Min priority**: Leftmost entry
- **Max priority**: Rightmost entry
- **Access**: $O(\log n)$

### General Advantage
BSTs can do everything in $O(\log n)$ time. Other specialized data structures may be faster for specific operations, but BSTs are versatile.

## Augmented BSTs

By storing additional information at each node, more operations become possible.

### Order Statistic Tree
Stores subtree size at each node. Enables:
- **Select $k$-th smallest element**: $O(\log n)$
- **Find rank of element $x$**: $O(\log n)$

### Augmentation Principle
You can augment BSTs with any information that's **locally available**:
- Available from children/grandchildren
- Computable from constant generations away

## Related Topics
- [[Trees and Rooted Trees]]
- [[Graph Types]]
