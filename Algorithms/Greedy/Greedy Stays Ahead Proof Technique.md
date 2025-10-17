# Greedy Stays Ahead Proof Technique

## Overview

**Greedy Stays Ahead** is a proof technique used to show that a [[Greedy Algorithm Pattern|greedy algorithm]] produces an optimal solution.

The key idea: Prove that after making $k$ greedy choices, the greedy solution is "at least as good as" (or "ahead of") any other solution at that point.

## When to Use

This technique works well when:
1. You can measure "progress" toward the solution
2. You can compare the greedy solution to any other solution at intermediate steps
3. Being "ahead" at step $k$ implies being ahead at step $k+1$

Common in problems involving:
- Scheduling
- Selection problems
- Resource allocation

## General Structure

### Setup
- Let $G$ = greedy solution
- Let $O$ = any optimal solution (or any solution)
- Define a metric to compare them

### Claim
After $k$ steps, greedy is "no worse" than optimal:
$$\text{metric}(G_k) \leq \text{metric}(O_k)$$

(The inequality direction depends on what "better" means in context)

### Proof Method
Use **proof by induction** on the number of steps:

1. **Base case:** Show greedy stays ahead at step 1
2. **Inductive hypothesis:** Assume greedy stays ahead at step $k$
3. **Inductive step:** Prove greedy stays ahead at step $k+1$

### Contradiction Finish
After proving greedy stays ahead at all steps:
- Assume greedy produces fewer/worse results than optimal
- Show this leads to a contradiction
- Conclude greedy must be optimal

## Example: Interval Scheduling

For the [[Interval Scheduling Problem]] with [[Earliest Finish Time Rule]]:

**Metric:** Finish time of the $k$-th interval selected

**Claim:** $f(i_k) \leq f(j_k)$ for all $k$
- Where $i_k$ is greedy's $k$-th choice and $j_k$ is optimal's $k$-th choice

**Why it matters:**
- If greedy finishes its $k$-th job earlier, it has more time for additional jobs
- Being "ahead" in finish time means better positioning for future selections

### The Induction

**Base case ($k=1$):**
- Greedy picks earliest finishing job by design
- Therefore $f(i_1) \leq f(j_1)$ ✓

**Inductive step:**
- Assume $f(i_k) \leq f(j_k)$
- Since optimal must pick compatible jobs: $f(j_k) \leq s(j_{k+1})$
- So: $f(i_k) \leq f(j_k) \leq s(j_{k+1})$
- Greedy picks earliest compatible job, so: $f(i_{k+1}) \leq f(j_{k+1})$ ✓

### The Contradiction

Now suppose greedy produces $r$ jobs but optimal produces $m > r$ jobs.

Since greedy stays ahead: $f(i_r) \leq f(j_r) \leq s(j_{r+1})$

This means job $j_{r+1}$ is compatible with greedy's schedule, so greedy **could have picked it**. But greedy tries everything before stopping - **contradiction**!

Therefore: greedy must produce optimal number of jobs.

## Key Insights

1. **"Ahead" is relative:** Define what "ahead" means for your problem
2. **Start times matter:** Often need both start and finish times to show compatibility
3. **Induction is crucial:** Must prove ahead at every step, not just the end
4. **The contradiction seals it:** Showing greedy stays ahead isn't enough - must prove optimality

## Common Pitfalls

❌ **Only comparing final solutions** - Must show ahead at *every* step
❌ **Forgetting base case** - Must establish ahead from the very first choice  
❌ **Weak inductive step** - Need rigorous proof, not just intuition
❌ **Incomplete contradiction** - Must clearly show the logical impossibility

## Comparison to Other Proof Techniques

| Technique | When to Use | Key Idea |
|-----------|-------------|----------|
| **Greedy Stays Ahead** | Incremental progress measurable | Show ahead at each step |
| **Exchange Argument** | Can swap choices | Transform optimal to greedy |
| **Structural Induction** | Problem has recursive structure | Prove on subproblem size |

## Related Concepts

- [[Greedy Algorithm Pattern]] - The algorithms this proves correct
- [[Earliest Finish Time Rule]] - Example application
- [[Interval Scheduling Problem]] - Classic problem using this technique
- [[Proof by Induction]] - Mathematical foundation

## Important Note

**You need a proof that your greedy algorithm works!** 

Greedy algorithms are:
- Easy to describe
- Non-trivial to prove correct
- Often wrong if not carefully designed

Never assume a greedy approach works without proof.

---
*Related: [[Greedy]]*
