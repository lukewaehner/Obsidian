

## Overview

Binary Search Trees provide a flexible foundation for implementing many higher-level data structures and solving various algorithmic problems.

**Key advantage**: BSTs can solve all these problems in O(log n) time (when balanced). While specialized data structures may be faster for specific use cases, BSTs can do everything reasonably well.

## 1. Sets

### Problem
Does set S contain element x?

### Implementation
Store elements of S as keys in a BST.

### Operations
- **Contains**: Search for element → O(log n)
- **Insert**: Add new element → O(log n)
- **Remove**: Delete element → O(log n)
- **Min/Max**: Find minimum/maximum → O(log n)
- **Iterate in order**: In-order traversal → O(n)

### Example
```python
class Set:
    def __init__(self):
        self.bst = BST()
    
    def contains(self, x):
        return self.bst.search(x) is not None
    
    def add(self, x):
        self.bst.insert(x)
    
    def remove(self, x):
        self.bst.delete(x)
```

**Use case**: When you need both membership testing AND sorted iteration.

## 2. Associative Arrays (Dictionaries / Maps)

### Problem
Store key-value pairs where keys are unique. Support lookup, insertion, updates, and deletion.

Also known as: **Key-Value stores**, **Dictionaries**, **Symbol Tables**, **Maps**

### Implementation
Store keys in BST, with values stored in each node.

### Operations
- **Lookup**: Get value for key k → O(log n)
- **Insert**: Add new key-value pair → O(log n)
- **Update**: Change value for existing key → O(log n)
- **Delete**: Remove key-value pair → O(log n)
- **Iterate by key order**: In-order traversal → O(n)

### Example
```python
class Dictionary:
    def __init__(self):
        self.bst = BST()  # Each node stores (key, value)
    
    def get(self, key):
        node = self.bst.search(key)
        return node.value if node else None
    
    def put(self, key, value):
        node = self.bst.search(key)
        if node:
            node.value = value  # Update
        else:
            self.bst.insert(key, value)  # Insert
    
    def delete(self, key):
        self.bst.delete(key)
```

**Use case**: When you need key-value storage with sorted key iteration.

**Standard library**: 
- C++ `std::map`
- Java `TreeMap`
- Python `sortedcontainers.SortedDict`

## 3. Priority Queues

### Problem
Store values with priorities. Allow quick access to highest (or lowest) priority elements.

### Implementation
Store priorities as keys in BST.

### Operations
- **Insert**: Add new element with priority → O(log n)
- **Find-min**: Get leftmost entry (minimum) → O(log n)*
- **Find-max**: Get rightmost entry (maximum) → O(log n)*
- **Delete-min**: Remove minimum → O(log n)
- **Delete-max**: Remove maximum → O(log n)

*Can be O(1) if maintaining pointers to min/max nodes

### Example
```python
class PriorityQueue:
    def __init__(self):
        self.bst = BST()
    
    def insert(self, priority, value):
        self.bst.insert(priority, value)
    
    def get_min(self):
        # Find leftmost node
        node = self.bst.root
        while node.left:
            node = node.left
        return node
    
    def delete_min(self):
        min_node = self.get_min()
        self.bst.delete(min_node.key)
```

**Comparison with heaps**:
- **BST**: O(log n) insert, O(log n) find-min, O(log n) delete-min
- **Binary Heap**: O(log n) insert, O(1) find-min, O(log n) delete-min

**Use heap when**: Only need min/max operations
**Use BST when**: Need arbitrary priority access or sorted iteration

## 4. Order Statistic Trees

### Problem
Extend BST to support:
1. Select k-th smallest element
2. Find rank of element x (how many elements are smaller)

### Implementation
**Augmentation**: Store subtree size at each node.

```python
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.size = 1  # Size of subtree rooted at this node
```

Update size during rotations:
```python
node.size = 1 + size(node.left) + size(node.right)
```

### Operations

#### Select k-th smallest
Find element with rank k (k elements are smaller).

```python
def Select(node, k):
    if node is None:
        return None
    
    left_size = size(node.left)
    
    if k == left_size + 1:
        return node  # This is k-th smallest
    elif k <= left_size:
        return Select(node.left, k)  # Search in left subtree
    else:
        return Select(node.right, k - left_size - 1)  # Search in right
```

**Time**: O(log n)

#### Find rank of x
Count how many elements are smaller than x.

```python
def Rank(node, x):
    if node is None:
        return 0
    
    if x < node.key:
        return Rank(node.left, x)
    elif x > node.key:
        return 1 + size(node.left) + Rank(node.right, x)
    else:  # x == node.key
        return size(node.left) + 1
```

**Time**: O(log n)

### Applications
- Find median in dynamic dataset
- Find k-th largest/smallest frequently
- Count elements in range [a, b]

## General Augmentation Principle

You can augment BSTs with **any information that's locally available**:

**Locally available** means: information computable from:
- The node itself
- Its children
- Its grandchildren
- Or constant generations away

### Examples of Augmentations

1. **Subtree size**: size(node) = 1 + size(left) + size(right)
2. **Subtree height**: height(node) = 1 + max(height(left), height(right))
3. **Subtree min/max**: Easily maintained from children
4. **Subtree sum**: sum(node) = node.value + sum(left) + sum(right)

### Maintaining Augmented Data

Update augmented information during rotations:

```python
def UpdateSize(node):
    node.size = 1 + size(node.left) + size(node.right)

def RightRotate(y):
    x = y.left
    β = x.right
    
    x.right = y
    y.left = β
    
    # Update augmented data
    UpdateSize(y)  # Update y first (now child)
    UpdateSize(x)  # Update x second (now parent)
    
    return x
```

## Additional Applications

### Range Queries
Find all elements in range [a, b].

**Approach**: 
1. Search for a (leftmost element ≥ a)
2. In-order traversal until reach element > b
3. Time: O(log n + k) where k = number of elements in range

### Interval Trees
Store intervals [a, b] and find overlapping intervals.

**Augmentation**: Store max endpoint in subtree at each node.

### Dynamic Median
Maintain median of a stream of numbers.

**Approach**: Two BSTs (or heaps):
- One for smaller half
- One for larger half
- Balance sizes to keep median accessible

## When NOT to Use BSTs

**Use hash table instead** when:
- Don't need sorted order
- Don't need range queries
- Want O(1) average operations

**Use heap instead** when:
- Only need min/max operations
- Don't need arbitrary access
- Want simpler implementation

**Use sorted array instead** when:
- Data is mostly static
- Memory layout matters (cache-friendly)
- Can afford O(n) insertions

## Summary Table

| Application | Key Feature | Time Complexity |
|-------------|-------------|-----------------|
| **Set** | Membership testing | O(log n) |
| **Dictionary** | Key-value storage | O(log n) |
| **Priority Queue** | Min/max access | O(log n) |
| **Order Statistic** | k-th element, rank | O(log n) |
| **Range Query** | Elements in [a,b] | O(log n + k) |

## Related Topics

- [[BST Operations]] - Basic operations that enable applications
- [[Self-Balancing BSTs]] - Maintain O(log n) performance
- [[Heaps]] - Alternative priority queue implementation
- [[Hash Tables]] - Alternative for unordered key-value storage

---

**Source**: CS3000 Lecture 13
**Parent**: [[Code/Topics/Algorithms/Binary Search Trees/Binary Search Trees]]