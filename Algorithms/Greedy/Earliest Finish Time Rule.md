

## The Rule

For the [[Interval Scheduling Problem]], the optimal greedy strategy is:

**Always pick the interval that finishes earliest among remaining compatible intervals.**

## Algorithm

```
Sort input so that f(1) ≤ f(2) ≤ ... ≤ f(n)
S = {}
free = 0
for i = 1,...,n
    if s(i) ≥ free        // current job starts after last picked job ends
        S = S ∪ {i}
        free = f(i)        // update the time we're free
return S
```

## Complexity

**Time:** $O(n \log n)$
- The **bottleneck is the initial sorting** by finish times
- The greedy selection itself is just $O(n)$
- This is typical for [[Greedy Algorithm Pattern|greedy algorithms]] - sorting dominates

**Space:** $O(1)$ (excluding output)

## Why This Works

**Intuition:** The earlier you finish a job, the more time remains to schedule additional jobs.

### Why Other Rules Fail

- **Earliest start time:** Can block many later jobs
- **Shortest duration:** Doesn't consider positioning in time
- **Fewest conflicts:** Local measure doesn't guarantee global optimum

The earliest finish time rule works because it:
1. Maximizes remaining time for future jobs
2. Never makes a choice that blocks more opportunities than necessary
3. "Stays ahead" of any other strategy (see proof)

## Proof of Correctness

The correctness is proven using the [[Greedy Stays Ahead Proof Technique]].

**Key insight:** When the greedy algorithm completes $k$ intervals, no other schedule can have completed more than $k$ intervals at that point.

### Formal Proof Structure

Let:
- $G = \{i_1, i_2, ..., i_r\}$ be the greedy schedule, $|G| = r$
- $O = \{j_1, j_2, ..., j_m\}$ be any optimal schedule, $|O| = m$

**Claim:** For all indices $t$, we have $f(i_t) \leq f(j_t)$ (greedy stays ahead)

**Proof by induction:**

**Base case:** $t = 1$
- $f(i_1) \leq f(j_1)$ 
- True because $f(i_1)$ is the minimum possible finish time by algorithm design (sorted this way)

**Inductive hypothesis:** For some $t \leq k$, assume $f(i_t) \leq f(j_t)$

**Inductive step:** Prove $f(i_{k+1}) \leq f(j_{k+1})$

From the hypothesis and compatibility:
$$f(i_k) \leq f(j_k) \leq s(j_{k+1}) \leq f(j_{k+1})$$

The important part: $f(i_k) \leq f(j_{k+1})$

We also know:
$$f(i_k) \leq s(i_{k+1}) \leq f(i_{k+1})$$

Since $i_{k+1}$ has the earliest end time among all jobs compatible with $i_k$ (that's what greedy does):
$$f(i_{k+1}) \leq f(j_{k+1})$$

### Completing the Proof

Now suppose $|G| = r < |O| = m$ (greedy is supposedly suboptimal).

From the induction above: $f(i_r) \leq f(j_r)$

Since $O$ is compatible and has $m > r$ jobs, there exists some job $j_{r+1}$ where:
$$f(i_r) \leq f(j_r) \leq s(j_{r+1})$$

This means:
- Job $j_{r+1}$ is compatible with $i_r$ (could start after greedy's last job)
- Therefore, $G$ **could have picked** $j_{r+1}$
- But this is a **contradiction** - the greedy algorithm tries everything before stopping

We said there's a job we could have picked but didn't, which contradicts the algorithm's behavior.

Therefore: $|G| \not< |O|$, so **greedy maximizes the number of intervals** ∎

## Related Concepts

- [[Interval Scheduling Problem]] - The problem this rule solves
- [[Greedy Stays Ahead Proof Technique]] - The proof method used
- [[Greedy Algorithm Pattern]] - General framework
- [[Sorts]] - Needed for initial sorting step

---
*Related: [[Greedy]]*
