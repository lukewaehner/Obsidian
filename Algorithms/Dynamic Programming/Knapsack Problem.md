---
tags: [algorithms, dynamic-programming, optimization, knapsack]
---
## Problem Definition

### Input
- $n$ items, each with:
  - Value $v_i > 0$
  - Weight $w_i > 0$
  - Where $v_i, w_i \in \mathbb{N}$
- Knapsack with capacity $W$

### Goal
Pack knapsack to **maximum value possible**.

## Example
If $W = 11$ and:

| i | $v_i$ | $w_i$ |
|---|-------|-------|
| 1 | 1     | 1     |
| 2 | 6     | 2     |
| 3 | 18    | 5     |
| 4 | 22    | 6     |
| 5 | 28    | 7     |

**Greedy approach** (pick largest value):
- $\{1, 2, 5\}$ has value 35, weight 10

**Optimal solution** (be smarter):
- $\{3, 4\}$ has value 40, weight 11 ✓

## DP Approach

### Similarity to WIS
- Similar to [[Weighted Interval Scheduling]]: pick or not pick item
- But **weight limit causes conflicts**, not start/end times
- Need to consider which item gets picked and how much it weighs

### Subproblem Definition
**Define**: $OPT(i, w)$ as the max value using items $1, ..., i$ with weight limit $w$

**Goal**: Find $OPT(n, W)$

### Two Cases for Item $i$

1. **Don't pick item $i$**: 
   - $OPT(i, w) = OPT(i-1, w)$
   
2. **Pick item $i$**: 
   - $OPT(i, w) = v_i + OPT(i-1, w - w_i)$
   - Get $v_i$, incur $w_i$
   - So pick best from first $i-1$ items using $w - w_i$ budget

## Bellman Optimality Equation
$$
OPT(i, w) = 
\begin{cases}
0 & i = 0 \\
OPT(i-1, w) & w_i > w \\
\max\{OPT(i-1, w), v_i + OPT(i-1, w - w_i)\} & \text{else}
\end{cases}
$$

## Implementation

### Top-Down with Memoization
```python
# Global variables: n, W, v_i, w_i
# Initialize size n × W table OPT to all Null

def Knapsack(i, w):
    if OPT[i, w] == Null:  # not yet computed
        if w + w_i > W:     # knapsack overflows
            OPT[i, w] = Knapsack(i-1, w)  # can't pick this
        else:
            OPT[i, w] = max(
                Knapsack(i-1, w),           # don't pick
                v_i + Knapsack(i-1, w + w_i) # pick
            )
    return OPT[i, w]

# Output: Knapsack(n, W)
```

## Analysis

### Correctness
Follows from the Bellman Optimality Equation.
- Always ensure recursive equation correctness before implementing

### Runtime Analysis
Account for:
1. Time taken by pre/post processing steps (if any)
2. Number of subproblems
3. Time taken per subproblem

**Number of subproblems**: $n \cdot W$

**Time per subproblem**: $O(1)$
- One addition, subtraction, comparison (for max)

**Total runtime**: $O(nW)$

### Space Complexity
**Space**: $O(nW)$ for memoization table
- Can be optimized (see [[Space Optimization in DP]])

## Related Topics
- [[Weighted Interval Scheduling]]
- [[Space Optimization in DP]]
- [[Dynamic Programming]]
