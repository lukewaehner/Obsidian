---
tags: [algorithms, dynamic-programming, optimization]
---

# DP Introduction

## The Abstract
- Create overlapping subproblems
- Solve recursively
- Add them together

## Key Concept: Memoization
Keep a table of already solved subproblems and use them when we need those solutions again.

### Example: Fibonacci
> $F(n) = F(n-1) + F(n-2)$

In calculating F(6) we need F(5) and F(4). But F5 needs F(4) and F(3), thus we have calls to the same function being repeated.

We can keep a table that we need to fill in for later use:

| $n$ | $F_n$ |
| --- | ----- |
| 1   | 1     |
| 2   | 1     |
| 3   | 2     |
| 4   | 3     |
| 5   | 5     |
| 6   | 8     |

## Optimal Substructure
- Similar to [[Divide and Conquer]]
- Optimally solving subproblems → optimal solution to overall problem
- "Bellman Equation" of optimality. Example: $F_n = F_{n-1} + F_{n-2}$

> Only different from Divide-and-Conquer because we already solved subproblems.
> We solve the same things repeatedly.
> This is where memoizing helps.

## General Approach
1. Figure out the subproblem structure
2. Derive the Bellman Optimality Equation
3. These tell you the table you'll fill
4. Sometimes it is easier to start with the table and work the rest out
5. Sometimes bottom-up (start with smallest values) may be easier

## Related Topics
- [[Weighted Interval Scheduling]]
- [[Maximum Grid Path Sum]]
- [[Knapsack Problem]]
- [[Sequences and Subsequences]]
- [[Space Optimization in DP]]
