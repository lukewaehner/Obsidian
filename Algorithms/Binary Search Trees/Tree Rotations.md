

## Purpose

**Tree rotations** are operations that restructure a BST while **preserving the BST invariant**. They are the fundamental mechanism for rebalancing trees.

## Key Properties

- ✓ Maintains BST ordering property
- ✓ Changes tree height/structure
- ✓ Operates in O(1) time
- ✓ Reversible operation

## Basic Rotation

### Right Rotation

Transform a left-heavy subtree:

```
      y                    x
     / \                  / \
    x   γ      ⟹        α   y
   / \                      / \
  α   β                    β   γ
```

**Code**:
```python
def RightRotate(y):
    x = y.left
    β = x.right
    
    # Perform rotation
    x.right = y
    y.left = β
    
    # Update parent pointers if needed
    
    return x  # New root of subtree
```

### Left Rotation

Transform a right-heavy subtree (mirror of right rotation):

```
    x                      y
   / \                    / \
  α   y        ⟹        x   γ
     / \                / \
    β   γ              α   β
```

**Code**:
```python
def LeftRotate(x):
    y = x.right
    β = y.left
    
    # Perform rotation
    y.left = x
    x.right = β
    
    # Update parent pointers if needed
    
    return y  # New root of subtree
```

## Why Rotations Preserve BST Invariant

Consider right rotation (x becomes new root, y becomes right child):

**Original ordering**: α < x < β < y < γ

After rotation:
- Left subtree of x: α (still < x) ✓
- Right child of x: y with subtrees β and γ
  - β is left child of y (x < β < y) ✓
  - γ is right child of y (y < γ) ✓
- Overall: α < x < β < y < γ ✓

The in-order traversal remains unchanged!

## Four Rotation Cases

Self-balancing BSTs identify imbalances and apply appropriate rotations:

### 1. Left-Left Case
**Problem**: Left child of left child is too deep

```
        5 (Root)
       /
      3 (Pivot)
     /
    2
```

**Solution**: Right rotation at Root

```
      3
     / \
    2   5
```

### 2. Right-Right Case
**Problem**: Right child of right child is too deep

```
    3 (Root)
     \
      5 (Pivot)
       \
        7
```

**Solution**: Left rotation at Root

```
      5
     / \
    3   7
```

### 3. Left-Right Case
**Problem**: Right child of left child is too deep

```
      5 (Root)
     /
    3
     \
      4 (Pivot)
```

**Solution**: Left rotation at Pivot, then right rotation at Root

Step 1 (Left rotation at 3):
```
      5
     /
    4
   /
  3
```

Step 2 (Right rotation at 5):
```
      4
     / \
    3   5
```

### 4. Right-Left Case
**Problem**: Left child of right child is too deep

```
    3 (Root)
     \
      5
     /
    4 (Pivot)
```

**Solution**: Right rotation at Pivot, then left rotation at Root

Step 1 (Right rotation at 5):
```
    3
     \
      4
       \
        5
```

Step 2 (Left rotation at 3):
```
      4
     / \
    3   5
```

## Visual Summary of Cases

| Case | Shape | Single/Double | Rotations |
|------|-------|---------------|-----------|
| Left-Left | `\` | Single | Right at root |
| Right-Right | `/` | Single | Left at root |
| Left-Right | `<` | Double | Left at pivot, then right at root |
| Right-Left | `>` | Double | Right at pivot, then left at root |

## When Rotations Are Applied

Rotations are triggered when tree becomes **unbalanced**:

1. **After insertion**: New node might create imbalance
2. **After deletion**: Removing node might create imbalance

The specific trigger conditions depend on the balancing strategy:
- **AVL Trees**: When height difference > 1
- **Red-Black Trees**: When red-black properties violated

## Time Complexity

**Single rotation**: O(1)
- Fixed number of pointer updates
- No loops or recursion

**Rebalancing after operation**: O(log n)
- May need rotations at multiple levels
- At most O(log n) rotations up the tree
- Total operation time remains O(log n)

## Example: Rebalancing After Insert

Insert 10, 20, 30 into empty BST (without balancing becomes degenerate):

**After inserting 10, 20**:
```
    10
      \
       20
```

**After inserting 30** (unbalanced):
```
    10
      \
       20
         \
          30
```

This is Right-Right case → Left rotation at 10:

**After left rotation** (balanced):
```
      20
     /  \
   10    30
```

## Related Topics

- [[BST Time Complexity]] - Rotations maintain O(log n) height
- [[Self-Balancing BSTs]] - AVL and Red-Black trees use rotations
- [[BST Operations]] - Operations that may trigger rotations
- [[Tree Traversals]] - In-order traversal unchanged by rotations

---

**Source**: CS3000 Lecture 13
**Parent**: [[Binary Search Trees]]