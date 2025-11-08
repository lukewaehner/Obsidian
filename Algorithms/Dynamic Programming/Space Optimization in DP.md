---
tags: [algorithms, dynamic-programming, optimization, space-complexity]
---

# Space Optimization in DP

## Key Insight
Do we always need to keep track of the whole memoization table?

**Question**: Can we forget something we'll never need again?

**Answer**: If we know we won't need it, we can discard it!

## The Concept
- We memoize because we **might** need it again
- If we **know** we won't need it → we can discard it
- This saves space and fixes one of the "drawbacks" of DP

## When to Apply
Ask yourself:
- Are there times when we can forget something?
- What if we know it'll never be needed again?

If yes, then space savings are possible!

## Applicable Problems
Space savings can be applied to:
- **Fibonacci**: Only need last 2 values
- **[[Knapsack Problem]]**: Only need previous row
- **[[Maximum Grid Path Sum]]**: Only need previous row/column
- **[[Edit Distance and Sequence Alignment]]**: Only need previous row
- And many other DP problems

## Example: Fibonacci
### Standard DP
```python
# Uses O(n) space
F = [0] * (n+1)
F[0] = 0
F[1] = 1
for i in range(2, n+1):
    F[i] = F[i-1] + F[i-2]
```

### Space Optimized
```python
# Uses O(1) space
prev2 = 0  # F[i-2]
prev1 = 1  # F[i-1]
for i in range(2, n+1):
    curr = prev1 + prev2
    prev2 = prev1
    prev1 = curr
```

## Example: Knapsack
### Standard DP
- Uses $O(nW)$ space for full table

### Space Optimized
- Only need previous row: $O(W)$ space
- Process row by row, keeping only 2 rows at a time

## General Strategy
1. **Identify dependencies**: What previous values do we need?
2. **Determine minimum retention**: Keep only what's necessary
3. **Implement rolling arrays**: Reuse space for new computations
4. **Careful with backtracking**: May need full table to reconstruct solution

## Trade-offs
- **Pros**: Reduced space complexity
- **Cons**: 
  - May make backtracking harder
  - Code can be more complex
  - Debugging is more difficult

## Related Topics
- [[DP Introduction]]
- [[Dynamic Programming]]
- [[Knapsack Problem]]
- [[Edit Distance and Sequence Alignment]]
