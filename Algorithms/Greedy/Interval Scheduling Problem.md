# Interval Scheduling Problem

## Problem Definition

**Input:** 
- $n$ intervals with start time $s(i)$ and finish time $f(i)$
- Each interval has value $v_i$

**Output:** 
- Subset of intervals making a compatible schedule with largest total value

**Constraints:**
- A schedule $S$ is **compatible** if no two intervals $i, j \in S$ overlap
- The total value of $S$ is $\sum_{i \in S} v_i$

## Unweighted Version

In **unweighted interval scheduling**, we set $v_i = 1$ for all intervals. This simplifies to:
- **Goal:** Maximize the **number** of intervals scheduled (not their duration or value)
- **Total value** = $|S|$ (just counting how many jobs you can do)

The problem is purely about **how many jobs you can complete**, not the amount of time spent doing jobs.

## Comparison to Weighted Version

The weighted version can be solved with [[Dynamic Programming]] using an $O(n \log n)$ approach. However, for the unweighted version:
- The DP approach is **overkill**
- Partial values in the memoization table aren't useful
- In DP, we memoize for the value, but now it's just the number of jobs picked
- **Compatibility is the sole constraint** - problem is solved if conflicts/collisions are handled

This makes the unweighted version ideal for a [[Greedy Algorithm Pattern|greedy approach]].

## Greedy Solution

The key insight: Sort intervals by finish time and greedily pick the earliest finishing job that doesn't conflict.

See [[Earliest Finish Time Rule]] for the complete solution and proof.

## Failed Greedy Strategies

Several intuitive greedy rules **don't work**:

### 1. Earliest Start Time ❌
**Intuition:** Start early to do more

**Counterexample:**
```
a)
 |---| |---| |---| |---| 
|------------------------|
```
Choosing the earliest starting job blocks all others.

### 2. Shortest Duration ❌
**Intuition:** Short jobs leave more time for others

**Counterexample:**
```
b)
|-----| |-----| 
     |---|
```
The short job in the middle blocks both longer jobs (optimal = 2, greedy = 1).

### 3. Fewest Conflicts ❌
**Intuition:** Jobs with fewer conflicts leave more options

**Counterexample:**
```
c)
|---| |---| |---| |---|
  |---| |---| |---|
   |---|       |---|
   |---|       |---|
   |---|       |---|
```
The middle item has many conflicts but should be skipped for optimal solution.

## Related Concepts
- [[Dynamic Programming]] - Alternative approach for weighted version
- [[Greedy Algorithm Pattern]] - General template this problem follows
- [[Earliest Finish Time Rule]] - The correct greedy strategy
- [[Greedy Stays Ahead Proof Technique]] - How we prove the solution correct

---
*Related: [[Greedy]]*
