

## Height-Dependent Performance

Every BST operation depends on the **height** of the tree:
- Searching might require going all the way to a leaf node
- In the worst case, number of steps = height of tree
- Time complexity: **O(h)** where h = height

## Height Scenarios

### Worst Case: Degenerate Tree
**Height = n** (where n = number of nodes)

When insertions occur in sorted order, the tree becomes a linear chain:

```
1
 \
  2
   \
    3
     \
      4
       \
        5
```

Operations: **O(n)** - as bad as a linked list!

### Best Case: Balanced Tree
**Height = O(log n)**

When the tree is kept balanced, operations are logarithmic:

```
        4
       / \
      2   6
     / \ / \
    1  3 5  7
```

Operations: **O(log n)** - very efficient!

## Comparison Table

| Tree Type | Height | Search | Insert | Delete |
|-----------|--------|--------|--------|--------|
| **Degenerate** (worst) | n | O(n) | O(n) | O(n) |
| **Balanced** (best) | log n | O(log n) | O(log n) | O(log n) |
| **Average** (random) | O(log n)* | O(log n) | O(log n) | O(log n) |

*With random insertions, expected height is O(log n)

## Why Height Matters

Each comparison in the BST:
- Eliminates approximately half of remaining search space (in balanced tree)
- Eliminates only one node (in degenerate tree)

This is why **maintaining balance** is crucial for performance.

## Space Complexity

BST storage: **O(n)**
- Each of n nodes stores: key, value, left pointer, right pointer, (optional parent pointer)

Recursive operation call stack: **O(h)**
- Depth of recursion equals height
- O(log n) for balanced, O(n) for degenerate

## Maintaining O(log n) Height

To guarantee logarithmic operations, BSTs must be **self-balancing**:

### Self-Balancing Strategy
1. Perform standard BST operation (search, insert, delete)
2. Check if tree became unbalanced
3. Apply rotations to restore balance
4. Ensure height remains O(log n)

Common self-balancing implementations:
- **AVL Trees**: Strict balancing (height diff ≤ 1)
- **Red-Black Trees**: Relaxed balancing (height ≤ 2 log n)

See [[Self-Balancing BSTs]] for details.

## Practical Considerations

### When to Use BSTs

**Good for**:
- ✓ Dynamic data (frequent insertions/deletions)
- ✓ Maintaining sorted order
- ✓ Range queries
- ✓ Finding predecessors/successors

**Not optimal for**:
- ✗ Static data (use sorted array + binary search)
- ✗ Simple membership testing (use hash table)
- ✗ Always need min/max (use heap for priority queue)

### Real-World Performance

**Self-balancing BSTs**:
- Guaranteed O(log n) worst case
- Small constant factors
- Well-suited for most applications

**Plain BSTs** (without balancing):
- Average case O(log n) with random data
- Worst case O(n) with sorted/nearly-sorted data
- Risk degrading to linear performance

**Recommendation**: Always use self-balancing implementations in production code.

## Comparison with Other Data Structures

| Operation | Sorted Array | BST (balanced) | Hash Table | Heap |
|-----------|--------------|----------------|------------|------|
| Search | O(log n) | O(log n) | O(1)* | O(n) |
| Insert | O(n) | O(log n) | O(1)* | O(log n) |
| Delete | O(n) | O(log n) | O(1)* | O(log n) |
| Min/Max | O(1) | O(log n)** | O(n) | O(1) |
| Sorted Order | ✓ | ✓ | ✗ | Partial |
| Range Query | ✓ | ✓ | ✗ | ✗ |

*Average case; worst case O(n) for hash table
**O(1) if maintaining pointers to min/max

## Amortized Analysis

For some operations in self-balancing BSTs:
- Individual operation might take O(log n)
- Rebalancing adds overhead
- **Amortized** time remains O(log n) per operation

The cost of rebalancing is "spread out" across multiple operations.

## Related Topics

- [[BST Operations]] - The operations whose complexity we analyze
- [[Tree Rotations]] - Used to maintain O(log n) height
- [[Self-Balancing BSTs]] - Guarantee logarithmic performance
- [[Asymptotic Analysis]] - Big-O notation and complexity classes

---

**Source**: CS3000 Lecture 13
**Parent**: [[Binary Search Trees]]