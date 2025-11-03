# Greedy vs Dynamic Programming

## Key Differences

| Aspect | Greedy | Dynamic Programming |
|--------|--------|-------------------|
| **Decision making** | Locally optimal at each step | Considers all subproblem solutions |
| **Look ahead** | Never looks back or ahead | Examines future via subproblems |
| **Passes over data** | Single pass | Multiple passes (builds table) |
| **Speed** | Fastest (usually $O(n \log n)$ from sorting) | Slower (depends on table size) |
| **Memory** | Minimal (just current state) | Stores subproblem solutions |
| **Correctness** | Requires proof (often complex) | More mechanical to verify |
| **Applicability** | Limited to specific problems | More widely applicable |

## When to Use Each

### Use Greedy When:
- Making locally optimal choices leads to global optimum
- You can prove correctness (e.g., [[Greedy Stays Ahead Proof Technique]])
- Problem has a clear "priority" or "ordering" strategy
- Speed is critical

**Example:** [[Interval Scheduling Problem]] (unweighted)

### Use Dynamic Programming When:
- Problem has overlapping subproblems
- Need to consider multiple options at each step
- Can define recursive structure (Bellman equation)
- Greedy approach fails

**Example:** [[Dynamic Programming|Weighted Interval Scheduling]]

## Case Study: Interval Scheduling

### Weighted Version (Need DP)
- Jobs have start time $s(i)$, finish time $f(i)$, and **weight** $w_i$
- Goal: Maximize **total weight** of compatible jobs
- Greedy fails: highest weight job might block many lighter jobs

**DP Solution:**
```
OPT(i) = max{OPT(i-1), w_i + OPT(p_i)}
```
- Must consider: skip job $i$ OR take job $i$ (and skip conflicts)
- Requires $O(n \log n)$ time and $O(n)$ space for memoization table

### Unweighted Version (Greedy Works)
- Same as weighted but $v_i = 1$ for all jobs
- Goal: Maximize **number** of jobs (not time spent)
- Compatibility is sole constraint

**Why DP is Overkill:**
- The partial values in the memoization table aren't useful
- We memoize for the value, but now it's just counting jobs
- All we need to track: "Can we add this job?" (compatibility check)

**Greedy Solution:**
- Sort by finish time: $O(n \log n)$
- Pick earliest finishing compatible job: $O(n)$
- Much simpler, same complexity

## Relationship Between Approaches

### Greedy as a Special Case
Greedy can be viewed as DP where:
- Only **one** subproblem choice is ever optimal
- No need to store and compare multiple options
- Memoization table degenerates to simple state tracking

### Optimal Substructure
**Both require optimal substructure:**
- DP: Optimal solution contains optimal solutions to subproblems
- Greedy: Locally optimal choice leads to globally optimal solution

The difference: Greedy makes the choice *without* examining all subproblems.

### Greedy Choice Property
What separates greedy from DP:

**Greedy Choice Property:** We can make a locally optimal choice and solve the remaining subproblem independently.

If this property holds → Greedy works
If this property fails → Need DP

## When Greedy Fails: A Subtle Example

Consider modified interval scheduling where earliest finish time fails:

```
Jobs with weights:
|----| w=10    
    |----| w=1
       |----| w=10
```

Greedy (earliest finish): picks first job (w=10), blocks others. Total = 10
Optimal: picks last two jobs. Total = 11

Here we need [[Dynamic Programming]] to consider all possibilities.

## Proof Complexity

### Dynamic Programming
- Define subproblem structure
- Write Bellman equation
- Prove optimal substructure (usually straightforward)
- Complexity: Moderate

### Greedy
- Identify greedy choice
- Prove greedy choice property (can be very hard!)
- Common techniques:
  - [[Greedy Stays Ahead Proof Technique]]
  - Exchange argument
  - Structural induction
- Complexity: **Often the hardest part of algorithm design**

## Design Philosophy

### DP Approach:
"Let's systematically explore all possibilities and remember what we learned."

### Greedy Approach:
"Let's make the obviously best choice right now and never reconsider."

## Practical Guidance

1. **Start with DP intuition:** Try to formulate the problem with subproblems
2. **Look for greedy opportunity:** Can you identify a choice that's always safe?
3. **Prove it or use DP:** If you can't prove greedy works, fall back to DP
4. **Profile if needed:** Sometimes DP is "fast enough" and easier to trust

## Related Concepts

- [[Greedy Algorithm Pattern]] - Structure of greedy algorithms
- [[Dynamic Programming]] - Full DP approach and examples
- [[Interval Scheduling Problem]] - Problem that illustrates the difference
- [[Greedy Stays Ahead Proof Technique]] - Common greedy proof method
- [[Divide and Conquer]] - Third major algorithm paradigm

---
*Related: [[Greedy]], [[Dynamic Programming]]*
