---
tags: [algorithms, dynamic-programming, hub]
---

# Dynamic Programming

Dynamic Programming is an algorithmic technique for solving optimization problems by breaking them down into overlapping subproblems and storing solutions to avoid redundant computation.

## Core Concepts
- [[DP Introduction]] - Memoization, optimal substructure, and the general approach

## Classic Problems

### Scheduling and Optimization
- [[Weighted Interval Scheduling]] - Maximum weight subset of non-overlapping jobs
- [[Knapsack Problem]] - Maximizing value within weight constraints
- [[Maximum Grid Path Sum]] - Finding optimal paths through grids

### Sequence Problems
- [[Sequences and Subsequences]] - Fundamental definitions and concepts
- [[Longest Increasing Subsequence]] - Finding longest increasing subsequences
- [[Longest Alternating Subsequence]] - Subsequences that alternate up and down
- [[Edit Distance and Sequence Alignment]] - Measuring string similarity and transformations

## Advanced Topics
- [[Space Optimization in DP]] - Reducing space complexity in DP solutions

## Key Techniques
1. **Identify subproblem structure**
2. **Derive Bellman Optimality Equation**
3. **Choose implementation approach**:
   - Top-down with memoization (recursive)
   - Bottom-up with tabulation (iterative)
4. **Analyze time and space complexity**
5. **Implement backtracking** (if solution path needed)

## Common Patterns
- **Sequential**: Process elements one at a time (WIS, LIS)
- **Two-sequence**: Compare/align two sequences (Edit Distance, LCS)
- **Grid/Matrix**: Navigate 2D structures (Grid Path)
- **Bounded resource**: Optimize with constraints (Knapsack)

## Related Topics
- [[Divide and Conquer]] - Similar optimal substructure, but without overlapping subproblems
- [[Greedy]] - Sometimes works, but DP needed when greedy fails
- [[Recurrences]] - Understanding time complexity of recursive solutions

%% Begin Waypoint %%
- [[DP Introduction]]
- [[Edit Distance and Sequence Alignment]]
- [[Knapsack Problem]]
- [[Longest Alternating Subsequence]]
- [[Longest Increasing Subsequence]]
- [[Maximum Grid Path Sum]]
- [[Sequences and Subsequences]]
- [[Space Optimization in DP]]
- [[Weighted Interval Scheduling]]

%% End Waypoint %%
