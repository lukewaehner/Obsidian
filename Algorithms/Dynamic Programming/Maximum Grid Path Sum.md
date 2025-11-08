---
tags: [algorithms, dynamic-programming, grid, path-finding]
---

# Maximum Grid Path Sum

## Problem Definition
- **Input**: An $n \times m$ grid of positive numbers
- **Path**: Starts on top left, moves right or down on each step, ends on bottom right
- **Path sum**: The sum of elements in the path
- **Goal**: Find maximum path sum among all paths

## Example
```
---------
|1|5|1|9|
---------
|2|7|8|2|
---------
|8|2|6|4|
---------
```

## Why Greedy Fails
Greedy that searches immediate neighbors will fail:

```
-----------
|1|5|1|100|
-----------
|2|7|8| 2 |
-----------
|8|2|6| 4 |
-----------
```

## Why Not Brute Force?
- Way too expensive: $\binom{n-1+m-1}{m-1} \approx 2^{2^n}$

## DP Approach

### Subproblem Analysis
- **Minimum sum you'll always get**: Top-left value + Bottom-right value
- If grid size is $1 \times 1$: You always get the top-left value (no other values)
- If grid size is $2 \times 2$: Top-left + bottom-right + (top-right OR bottom-left)
- **Subproblems**: $(n-1) \times m$ and $n \times (m-1)$ grids

### Bellman Optimality Equation
$$S(n,m) = A[n,m] + \max\{S(n-1,m), S(n,m-1)\}$$

Where:
- $S(n,m)$ is the maximum path sum to reach cell $(n,m)$
- $A[n,m]$ is the value at cell $(n,m)$
- We choose the maximum between coming from above or from the left

## Related Topics
- [[DP Introduction]]
- [[Dynamic Programming]]
