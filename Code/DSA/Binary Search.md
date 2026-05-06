---
tags:
  - dsa
  - algorithms
  - search
  - divide-and-conquer
complexity: O(log n)
related:
  - '[[Linked List]]'
  - '[[Stack]]'
  - '[[Queue]]'
---
# Binary Search

## Overview
Binary Search is a **divide-and-conquer** algorithm that efficiently searches for a target value in a **sorted array** by repeatedly dividing the search interval in half.

**Key Requirements:**
- Array **must be sorted**
- Random access to elements (works with arrays, not linked lists)

**Time Complexity:** O(log n)
**Space Complexity:** O(1) iterative, O(log n) recursive (call stack)

---

## How It Works

1. Start with two pointers: `left` at index 0, `right` at last index
2. Calculate middle index: `mid = (left + right) // 2`
3. Compare `arr[mid]` with target:
   - If `arr[mid] == target`: Found! Return `mid`
   - If `arr[mid] < target`: Search right half (set `left = mid + 1`)
   - If `arr[mid] > target`: Search left half (set `right = mid - 1`)
4. Repeat until `left > right` (element not found)

---

## Implementation

### Iterative Approach (Recommended)
```python
def binary_search(arr, target):
    l = 0
    r = len(arr) - 1
    
    while l <= r:
        # Calculate middle index
        m = (r + l) // 2
        
        # Found target at middle
        if arr[m] == target:
            return m
        
        # Target is in right half
        # Middle value is less than target, search right
        if arr[m] < target:
            l = m + 1
        
        # Target is in left half
        # Middle value is greater than target, search left
        if arr[m] > target:
            r = m - 1
    
    # Target not found
    return -1


# Test cases
arr = [1, 3, 4, 6, 9, 13, 19, 22, 2000, 5000, 9214]
print(binary_search(arr, 19))  # Output: 6
print(binary_search(arr, 3))   # Output: 1
print(binary_search(arr, 100)) # Output: -1 (not found)
```

### Recursive Approach
```python
def binary_search_recursive(arr, target, l=0, r=None):
    # Initialize right pointer on first call
    if r is None:
        r = len(arr) - 1
    
    # Base case: element not found
    if l > r:
        return -1
    
    # Calculate middle
    m = (l + r) // 2
    
    # Found target
    if arr[m] == target:
        return m
    
    # Search left half
    if arr[m] > target:
        return binary_search_recursive(arr, target, l, m - 1)
    
    # Search right half
    if arr[m] < target:
        return binary_search_recursive(arr, target, m + 1, r)


# Test
arr = [1, 2, 3, 4, 5, 6]
print(binary_search_recursive(arr, 2))  # Output: 1
```

---

## Time Complexity Analysis

**Why O(log n)?**

We're reducing the problem size by half with each iteration:
- Start: n elements
- After 1 step: n/2 elements
- After 2 steps: n/4 elements
- After k steps: n/2^k elements

We stop when we reach 1 element: `n/2^k = 1`

Solving for k:
```
n/2^k = 1
n = 2^k
k = log₂(n)
```

Therefore: **O(log n)** (base doesn't matter in Big O notation)

**Comparison:**
- Linear search: O(n) - check every element
- Binary search: O(log n) - much faster for large arrays

**Example:** For 1 million elements:
- Linear: ~1,000,000 comparisons worst case
- Binary: ~20 comparisons worst case

---

## Common Pitfalls

1. **Forgetting array must be sorted** - Binary search only works on sorted data
2. **Integer overflow** - In some languages, `(l + r)` can overflow. Use `l + (r - l) // 2` instead
3. **Off-by-one errors** - Carefully handle `l <= r` vs `l < r` and `m + 1` vs `m - 1`
4. **Using on [[Linked List]]** - O(log n) comparisons but O(n) access time = O(n) overall

---

## Variations

- **Find first/last occurrence** of duplicate values
- **Search in rotated sorted array**
- **Find insertion position** for a value
- **Search in 2D sorted matrix**

---

## Related Concepts
- [[DSA]] - Main data structures & algorithms overview
- **Divide and Conquer** - Problem-solving paradigm
- **Sorted Arrays** - Prerequisite for binary search
- **Time Complexity** - Understanding O(log n)

---

## Key Takeaways
Only works on **sorted** arrays  
**O(log n)** time complexity - very efficient  
**Iterative** version preferred (no call stack overhead)  
Great for large datasets where sorting overhead is worth it
