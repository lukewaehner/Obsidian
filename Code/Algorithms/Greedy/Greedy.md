# Greedy Algorithms

Greedy algorithms build solutions by making locally optimal choices at each step, never looking back or worrying about future consequences.

## Core Concepts

### What Makes an Algorithm Greedy?
- [[Greedy Algorithm Pattern]] - The general structure and components of greedy algorithms
- [[Greedy vs Dynamic Programming]] - When to use greedy vs DP approaches

### Proof Techniques
- [[Greedy Stays Ahead Proof Technique]] - The primary method for proving greedy correctness

## Classic Problems

### Interval Scheduling
- [[Interval Scheduling Problem]] - The unweighted interval scheduling problem
- [[Earliest Finish Time Rule]] - The optimal greedy solution and its proof

## Key Insights

### Advantages
- **Fastest and simplest** when applicable
- **Sometimes optimal** - produces the best solution
- **Great hints** - even when not optimal, guides toward better solutions  
- **Easy to adapt** - simplicity makes them flexible across domains

### Challenges
- **Proof required** - Must prove the greedy choice is correct
- **Limited applicability** - Only works for specific problem types
- **Easy to get wrong** - Intuitive approaches often fail

### Common Characteristics
- Sorting usually dominates complexity ($O(n \log n)$)
- Single pass through data
- Minimal memory usage
- Local choices must lead to global optimum

## Relationship to Other Paradigms
- [[Dynamic Programming]] - More powerful but slower; greedy is special case
- [[Divide and Conquer]] - Different paradigm with independent subproblems
- [[Sorts]] - Often the bottleneck in greedy algorithms

---

*Part of: [[Algorithms]]*

%% Begin Waypoint %%
- [[Earliest Finish Time Rule]]
- [[Greedy Algorithm Pattern]]
- [[Greedy Stays Ahead Proof Technique]]
- [[Greedy vs Dynamic Programming]]
- [[Interval Scheduling Problem]]

%% End Waypoint %%
