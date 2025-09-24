---

---

---
## The Abstract
- Create overlapping subproblems
- Solve recursively
- Add them together

---
### Fibonacci:
> $F(n) = F(n-1) + F(n-2)$

- In calculating F(6) we need F(5) and F(4)
- But F5 needs F(4) and F(3), thus we have calls to the same function being repeated.

- We can keep a table that we need to fill in for later use:

| $n$ | $F_n$ |
| --- | ----- |
| 1   | 1     |
| 2   | 1     |
| 3   | 2     |
| 4   | 3     |
| 5   | 5     |
| 6   | 8     |

This is called **Memoization**:
- Keep a table of already solved subproblems.
- Use them when we need those solutions again.

---
## Optimal Substructure:
- Similar to Divide-and-Conquer
- Optimally solving subproblems -> optimal solution to overall problem.
- "Bellman Equation" of optimality. Example: $F_n = F_{n-1} + F_{n-2}$

> Only different from Divide-and-Conquer because we already solved subproblems.
> We solve the same things repeatedly
> This is where memoizing helps


---
# Problems
## Weighted Interval Scheduling
- Jobs start at time $s_i$, and finish at time $f_i$
- If two job's time ranges overlap, they are incompatible.
- Each job has an associated weight $w_i$
- Goal: Find **maximum weight subset** of mutually compatible jobs.

- How do we break them down into subproblems?
- Since the goal is to find the "best" subset, we can look at smaller subsets.
- But the number of subsets is huge ($2^n$ for $n$ jobs), we need to be smarter.

- If we solve for the first $i-1$ jobs, can we then solve until job $i$?
- But jobs don't have any order. What are "first" $i-1$ jobs?
- Idea: Sort by $f_i$ and now there is an ordering on the jobs.
- Using this sorting, we want to use "Best" from $1,...,i-1$ to find the "best" from $1,...,i$

- Define $OPT(i)$ as the maximum weight subset possible using jobs $1$ to $i$
- These $OPT(\cdot)$ will be our subproblems
- New goal: How to find $OPT(i)$ in terms of smaller $OPT(1), OPT(2), ..., OPT(i-1)$

- Define $OPT(i)$ as the maximum weight subset using jobs $1$ to $i$.
- If we do not pick job $i$, then $OPT(i-1)$ is the best possible option
- If we do pick job $i$, we can't pick anything that conflicts

- If $i$ is picked, the no job from $1,...,i-1$ which conflicts with $i$ can be picked.
- Find largest index $j < i$ that doesn't conflict with $i$ and pick $OPT(j)$
- Define this index value $j$ to b4 $p_i$. Can find this via Binary Search.

- We how have the necessary ideas to find $OPT(n)$

---

###  Bellman Optimality Equation for WIS
- We have everything to get the recursive solution
- Writing it out formally helps understanding and implementation.
- How do we write a recursive equation for $OPT(i)$?
- First, the base case: $OPT(0) = 0$

- Job $i$ is either in the true optimal or it isn't
	1. If $i$ is not in true optimal, then $OPT(i) = OPT(i-1)$
	2. If $i$ is in the true optimal, then $OPT(i) = w_i + OPT(p_i)$.

- Is $i$ in the true optimal or not?
- Bellman Optimality Equation:
$$
OPT(i) = 
\begin{cases}
0 & i=0 \\  max\{OPT(i-1), w_i+OPT(p_i)\} & i > 0
\end{cases}
$$
---

We must figure out the subproblem structure
Need the Bellman Optimality Equation
These tell you the table you'll fill
Sometimes it is easier to start with the table and work the rest out.
Sometimes bottom-up (start with smallest values) may be easier

---
## Maximum Grid Path Sum

- Input: an $n \times m$ grid of positive numbers
- Path: Starts on top left, moves right or down on each step, ends on bottom right
- Path sum: The sum of elements in the path
- Goal: Find maximum path sum among all paths

```
---------
|1|5|1|9|
---------
|2|7|8|2|
---------
|8|2|6|4|
---------
```

- Greedy that searches immediate neighbors will fail:

```
-----------
|1|5|1|100|
-----------
|2|7|8| 2 |
-----------
|8|2|6| 4 |
-----------
```

Definitely not Brute Force:
- Way too expensive: = $(\frac{n-1+m-1}{m-1} \approx 2^{2^n})$
What is minimum sum you'll always get
- Top-left value + Bottom-right value.
If grid size is $1 \times 1$, you always get the Top-left value, since there are no other values.
If grid size is $2\times2$, top-left, bottom-right + top right or bottom left 
If grid size is $2\times3$, 
Subproblems are $n-1\times m$ and $n\times m-1$
Bellman Optimality Equation:
	$S(n,m) = A[n,m]+max\{S(n-1,m),S(n,m-1)\}$
Base case, Bellman Optimality Equation


