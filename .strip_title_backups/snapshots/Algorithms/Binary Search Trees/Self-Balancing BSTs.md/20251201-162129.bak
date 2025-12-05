# Self-Balancing BSTs

## Overview

**Self-balancing BSTs** automatically maintain a height of O(log n) by performing rebalancing operations after insertions and deletions.

**Key idea**: After each modifying operation, check if the tree is unbalanced and apply [[Tree Rotations]] to restore balance.

## Rebalancing Process

1. Perform standard BST operation (insert or delete)
2. Check balance condition (varies by implementation)
3. If unbalanced, identify which case applies
4. Apply appropriate rotation(s)
5. Recurse/iterate up the tree if needed

## Time Complexity Guarantee

Every operation runs in **O(log n)** time:
- Standard BST operation: O(h)
- Rebalancing: O(h) in worst case
- Since h = O(log n), total is O(log n)

Where n = number of nodes in the tree.

## Common Implementations

### AVL Trees (Adelson-Velsky and Landis)

**Balance condition**: For every node, heights of left and right subtrees differ by at most 1.

**Balance factor**: BF(node) = height(left) - height(right)
- Must be in {-1, 0, 1}
- If |BF| > 1, rebalancing needed

**Properties**:
- ✓ Strictly balanced (most balanced BST)
- ✓ Height ≤ 1.44 log n
- ✓ Faster lookups than Red-Black trees
- ✗ More rotations on insert/delete
- ✗ Higher rebalancing overhead

**When to use**: When read-heavy workload (many searches, few modifications)

### Red-Black Trees

**Balance conditions**: 
1. Every node is either red or black
2. Root is black
3. All leaves (NULL) are black
4. Red nodes have black children (no two reds in a row)
5. All paths from node to leaves have same number of black nodes

**Properties**:
- ✓ Height ≤ 2 log n (less strict than AVL)
- ✓ Fewer rotations on insert/delete
- ✓ Better for write-heavy workloads
- ✗ Slightly slower searches than AVL
- ✗ More complex implementation

**When to use**: When modification-heavy workload (many inserts/deletes)

**Used in**: Java TreeMap, C++ std::map, Linux kernel

## Comparison

| Feature | AVL Trees | Red-Black Trees |
|---------|-----------|-----------------|
| **Height bound** | 1.44 log n | 2 log n |
| **Balance strictness** | Strict | Relaxed |
| **Lookup time** | Faster | Slightly slower |
| **Insert/delete time** | More rotations | Fewer rotations |
| **Best for** | Read-heavy | Write-heavy |
| **Implementation** | Simpler | More complex |

## Other Self-Balancing Trees

### Splay Trees
- Move recently accessed nodes closer to root
- Amortized O(log n) operations
- No balance information stored
- Good for non-uniform access patterns

### B-Trees
- Generalization to more than 2 children
- Optimized for disk/database access
- Keep nodes between [t-1, 2t-1] keys
- Used in file systems and databases

### Treaps
- Combination of BST + heap properties
- Randomized balancing (via priorities)
- Simpler than deterministic approaches
- Expected O(log n) operations

## Why Not Just Use Plain BSTs?

**Problem with plain BSTs**:
```
Insert 1, 2, 3, 4, 5 in order:

    1
     \
      2
       \
        3
         \
          4
           \
            5

Height = n, operations degrade to O(n)
```

**With self-balancing**:
```
Same insertions:

      2
     / \
    1   4
       / \
      3   5

Height = log n, operations stay O(log n)
```

## When to Use Self-Balancing BSTs

**Recommended for**:
- Production code with unknown input patterns
- When worst-case guarantees needed
- Dynamic data with frequent modifications
- Need for sorted order + fast operations

**Standard library implementations**:
- C++: `std::map`, `std::set` (Red-Black)
- Java: `TreeMap`, `TreeSet` (Red-Black)
- Python: No built-in, use external library (bintrees)

## Practical Considerations

### Implementation Complexity

From simplest to most complex:
1. Plain BST (no balancing)
2. AVL Tree (height balance)
3. Red-Black Tree (color properties)
4. B-Tree (variable degree)

**Trade-off**: More complex balancing → better performance guarantees

### Memory Overhead

**AVL Trees**: Store height at each node (1 integer)
**Red-Black Trees**: Store color at each node (1 bit, often 1 byte)

Additional memory is minimal compared to key/value/pointer storage.

### When NOT to Use

**Use hash table instead** if:
- Only need insert, delete, search (no ordering)
- Don't need sorted iteration
- O(1) average case more important than O(log n) worst case

**Use sorted array instead** if:
- Data is mostly static (few modifications)
- Can afford O(n) insertions
- Want cache-friendly linear memory layout

## Rotation Overhead

**AVL Trees**:
- Insert: Up to 2 rotations
- Delete: Up to O(log n) rotations

**Red-Black Trees**:
- Insert: Up to 2 rotations
- Delete: Up to 3 rotations

Despite worst-case counts, average case usually requires very few rotations.

## Implementation Assumption

In this course, we **assume**:
- Any BST discussed is self-balancing
- Height is maintained at O(log n)
- All operations run in O(log n) time

We **don't cover**:
- Specific implementation details of AVL/Red-Black balancing
- Exact rotation counts
- Proof of height bounds

These are important for implementation but not needed for understanding BST applications and complexity analysis.

## Related Topics

- [[Tree Rotations]] - Mechanism for rebalancing
- [[BST Time Complexity]] - Why balancing matters
- [[BST Operations]] - Operations that trigger rebalancing
- [[AVL Trees]] - Specific balancing algorithm (if detailed notes exist)
- [[Red-Black Trees]] - Alternative balancing algorithm (if detailed notes exist)

---

**Source**: CS3000 Lecture 13
**Parent**: [[Binary Search Trees]]