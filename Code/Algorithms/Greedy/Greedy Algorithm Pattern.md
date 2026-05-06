

## What is a Greedy Algorithm?
A greedy algorithm builds a solution by making locally optimal choices at each step:
- **Never looks back** - decisions are final
- **Never worries about future** - only considers current best option
- **Makes a single pass** over the input

## Why Use Greedy Algorithms?
1. **Fastest and simplest** approach when applicable
2. **Sometimes optimal** - can produce the best solution
3. **Provide great hints** - even when not optimal, they guide toward better solutions
4. **Easy to adapt** - simplicity makes them flexible across different domains

## General Pattern

All greedy algorithms follow this structure:

```
Sort choices by some metric
S = {}
for i = 1...n
    if i is compatible with S
        S = S ∪ {i}
return S
```

The key is to:
1. **Pick criteria** (the rule) to prioritize choices
2. **Pick choices in order** of criteria as long as valid
3. **Prove correctness** - this is the hardest part!

## Essential Components

### 1. Ranking/Priority Metric
Every greedy algorithm needs a way to compare choices. You essentially give everything a "rank" and pick highest ranks greedily.

### 2. Compatibility Check
Determine if a choice can be added to the current solution without violating constraints.

### 3. Correctness Proof
**You need a proof that your greedy algorithm works!** Without proof, you can't be sure the locally optimal choices lead to a globally optimal solution.

## Related Concepts
- [[Dynamic Programming]] - More powerful but slower; greedy is a special case where memoization isn't needed
- [[Divide and Conquer]] - Different paradigm that breaks problems into independent subproblems
- [[Sorts]] - Often the bottleneck in greedy algorithms (O(n log n))
- [[Greedy Stays Ahead Proof Technique]] - Common method to prove greedy correctness

## See Also
- [[Interval Scheduling Problem]] - Classic example of greedy algorithm
- [[Earliest Finish Time Rule]] - Specific greedy rule that works optimally

---
*Related: [[Greedy]]*
