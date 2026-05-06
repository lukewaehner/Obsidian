---
tags: [algorithms, dynamic-programming, scheduling, optimization]
---

# Weighted Interval Scheduling

## Problem Definition
- Jobs start at time $s_i$, and finish at time $f_i$
- If two job's time ranges overlap, they are incompatible
- Each job has an associated weight $w_i$
- **Goal**: Find maximum weight subset of mutually compatible jobs

## Breaking Down into Subproblems
- Since the goal is to find the "best" subset, we can look at smaller subsets
- But the number of subsets is huge ($2^n$ for $n$ jobs), we need to be smarter

### Key Insight: Sort by Finish Time
- Jobs don't have any order initially. What are "first" $i-1$ jobs?
- **Idea**: Sort by $f_i$ and now there is an ordering on the jobs
- Using this sorting, we want to use "Best" from $1,...,i-1$ to find the "best" from $1,...,i$

## Subproblem Definition
- Define $OPT(i)$ as the maximum weight subset possible using jobs $1$ to $i$
- These $OPT(\cdot)$ will be our subproblems
- **New goal**: How to find $OPT(i)$ in terms of smaller $OPT(1), OPT(2), ..., OPT(i-1)$

## Two Cases for Job $i$
1. **Do not pick job $i$**: Then $OPT(i-1)$ is the best possible option
2. **Do pick job $i$**: We can't pick anything that conflicts

### Handling Conflicts
- If $i$ is picked, no job from $1,...,i-1$ which conflicts with $i$ can be picked
- Find largest index $j < i$ that doesn't conflict with $i$ and pick $OPT(j)$
- Define this index value $j$ to be $p_i$
- Can find $p_i$ via **Binary Search**

## Bellman Optimality Equation
$$
OPT(i) = 
\begin{cases}
0 & i=0 \\
\max\{OPT(i-1), w_i+OPT(p_i)\} & i > 0
\end{cases}
$$

### Two Cases:
1. If $i$ is not in true optimal, then $OPT(i) = OPT(i-1)$
2. If $i$ is in the true optimal, then $OPT(i) = w_i + OPT(p_i)$

## Related Topics
- [[DP Introduction]]
- [[Dynamic Programming]]
