---
tags: [algorithms, dynamic-programming, sequences, optimization]
---

# Longest Increasing Subsequence

## Problem Definition
Given a sequence, find the **longest subsequence** where elements are in **strictly increasing order**.

### Example
Sequence: `[1, 4, 2, 10, 6, 14, 9, 5, 13, 3, 11]`

**Some increasing subsequences**:
- [1, 4]
- [2, 10]
- [2, 6, 14]
- [6, 9, 13]

**The LIS has length 5**:
- [1, 2, 6, 9, 11]
- [1, 4, 6, 9, 11]
- [1, 2, 6, 9, 13]
- [1, 4, 6, 9, 13]

### Applications
- Studying phenomena in physics
- Modeling uncertainty using matrices

## DP Approach

### First Attempt (Doesn't Work)
- Define $LIS(j)$ as the length of the LIS of $x_1, ..., x_j$
- **Problem**: Just knowing the length of LIS of $x_1, ..., x_{j-1}$ doesn't help
- We need to know the **endpoints** to determine if $x_j$ can be appended

### Correct Approach
Define $LIS(j)$ as the length of the LIS **which ends at** $x_j$.

**Key insight**: We can increase the LIS by appending a larger number to the end.

**Strategy**:
- For some $x_i < x_j$ where $i < j$, we can append $x_j$ to the LIS ending at $x_i$
- Whatever is the value at $LIS(i)$ increments by 1 since we added $x_j$ to the end
- Out of all possibilities, we try all and pick the best

## Recurrence Relation
$$
LIS(j) = 
\begin{cases}
1 & \text{if } j = 1 \\
1 + \max_{\substack{1 \leq i < j \\ x_i < x_j}} LIS(i) & \text{otherwise}
\end{cases}
$$

## Example Walkthrough
For $x = (6, 10, 14, 5, 12, 8)$:

| $j$ | 1 | 2 | 3 | 4 | 5 | 6 |
|-----|---|---|---|---|---|---|
| $x_j$ | 6 | 10 | 14 | 5 | 12 | 8 |
| $LIS(j)$ | 1 | 2 | 3 | 1 | 3 | 2 |

**Step-by-step**:
- $LIS(1) = 1$ (base case)
- $LIS(2) = 1 + LIS(1) = 2$ (10 > 6)
- $LIS(3) = 1 + \max(LIS(1), LIS(2)) = 3$ (14 > 6, 10)
- $LIS(4) = 1$ (5 is smaller than all previous)
- $LIS(5) = 1 + \max(LIS(1), LIS(4)) = 3$ (12 > 6, 5)
- $LIS(6) = 1 + \max(LIS(1), LIS(4)) = 2$ (8 > 6, 5)

### Important Note
- $LIS(n)$ is **not necessarily the output**
- Final answer: $\max_{1 \leq i \leq n} LIS(i)$
- In this example: $\max = 3$ (at positions 3 and 5)

## Analysis
- **Runtime**: $O(n^2)$
  - Need $O(i)$ time to find $LIS(i)$
  - Total: $\sum_{i=1}^n O(i) = O(n^2)$
- **Space**: $O(n)$ for the memoization table
- **Backtracking**: Find actual LIS by backtracking through choices made when filling $LIS(\cdot)$

## Variations
Same approach works for:
- **Longest decreasing subsequence**: Change condition to $x_i > x_j$
- **Longest non-increasing subsequence**: Change condition to $x_i \geq x_j$
- **Longest non-decreasing subsequence**: Change condition to $x_i \leq x_j$

## Related Topics
- [[Sequences and Subsequences]]
- [[Edit Distance and Sequence Alignment]]
- [[Dynamic Programming]]
