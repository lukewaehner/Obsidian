

## Three Primary Operations

All BST operations depend on the ability to search through the tree:

1. **Search** for a key k
2. **Insert** a new key k
3. **Delete** an existing key k

## Search Operation

Find a node with key k in the tree.

### Algorithm

```python
def Search(root, k):
    if root is NULL or root.key == k:
        return root
    
    if k < root.key:
        return Search(root.left, k)
    else:  # k > root.key
        return Search(root.right, k)
```

### Process
1. Start at root
2. If found, return node
3. If k < current node, go left
4. If k > current node, go right
5. If reach NULL, key not in tree

### Time Complexity
- **O(h)** where h = height of tree
- Best case: O(log n) for balanced tree
- Worst case: O(n) for degenerate tree (essentially a linked list)

## Insert Operation

Add a new key k to the tree while maintaining BST invariant.

### Algorithm

```python
def Insert(root, k):
    if root is NULL:
        return new Node(k)
    
    if k < root.key:
        root.left = Insert(root.left, k)
    elif k > root.key:
        root.right = Insert(root.right, k)
    # else: k == root.key, duplicate (handle based on convention)
    
    return root
```

### Process
1. Search for appropriate position (as in search)
2. When reach NULL, create new node
3. Attach new node as leaf

### Time Complexity
- **O(h)** where h = height of tree
- Same as search: O(log n) balanced, O(n) worst case

## Delete Operation

Remove a node with key k while maintaining BST invariant.

### Three Cases

#### Case 1: Node has no children (leaf node)
Simply remove the node.

```python
if node.left is NULL and node.right is NULL:
    return NULL
```

#### Case 2: Node has one child
Replace node with its child.

```python
if node.left is NULL:
    return node.right
if node.right is NULL:
    return node.left
```

#### Case 3: Node has two children
Replace node with its **in-order successor** (or predecessor):
1. Find successor: smallest node in right subtree (leftmost node in right)
2. Copy successor's value to current node
3. Delete successor (which has at most one child)

```python
def Delete(root, k):
    if root is NULL:
        return NULL
    
    # Search for node to delete
    if k < root.key:
        root.left = Delete(root.left, k)
    elif k > root.key:
        root.right = Delete(root.right, k)
    else:
        # Found node to delete
        
        # Case 1 & 2: Node has 0 or 1 child
        if root.left is NULL:
            return root.right
        elif root.right is NULL:
            return root.left
        
        # Case 3: Node has 2 children
        # Find in-order successor (min in right subtree)
        successor = FindMin(root.right)
        root.key = successor.key
        # Delete the successor
        root.right = Delete(root.right, successor.key)
    
    return root

def FindMin(node):
    while node.left is not NULL:
        node = node.left
    return node
```

### Time Complexity
- **O(h)** where h = height of tree
- Same as search and insert

## Example Walkthrough

Starting tree:
```
        8
       / \
      3   10
     / \    \
    1   6   14
       / \   /
      4   7 13
```

### Insert 5
1. Start at 8: 5 < 8, go left
2. At 3: 5 > 3, go right
3. At 6: 5 < 6, go left
4. At 4: 5 > 4, go right
5. Right child of 4 is NULL → insert 5 there

Result:
```
        8
       / \
      3   10
     / \    \
    1   6   14
       / \   /
      4   7 13
       \
        5
```

### Delete 3 (has two children)
1. Find successor: min in right subtree of 3 → node 4
2. Replace 3 with 4
3. Delete original 4 node (now has one child: 5)

Result:
```
        8
       / \
      4   10
     / \    \
    1   6   14
       / \   /
      5   7 13
```

## Iterative vs Recursive

All operations can be implemented iteratively or recursively:

### Iterative Search
```python
def SearchIterative(root, k):
    current = root
    while current is not NULL and current.key != k:
        if k < current.key:
            current = current.left
        else:
            current = current.right
    return current
```

**Iterative**: O(h) time, O(1) space
**Recursive**: O(h) time, O(h) space (call stack)

## Related Topics

- [[BST Definition]] - The BST invariant these operations maintain
- [[BST Time Complexity]] - Analysis of operation performance
- [[Tree Rotations]] - Used by self-balancing BSTs after operations
- [[In-Order Traversal]] - Finding successors/predecessors

---

**Source**: CS3000 Lecture 13
**Parent**: [[Binary Search Trees]]