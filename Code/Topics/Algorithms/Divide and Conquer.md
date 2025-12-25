---
## Topic:
---
---
#divide-and-conquer 
## Divide and conquer:
1. Divide up problem into subproblems of the same time
2. Solve each subproblem recursively
3. Combine solutions to subproblems into overall solution

### Common usage:
1. Divide problem of size n into 2 subproblems of size $n/2 \leftarrow O(n)$
2. Solve two subproblems recursively $\leftarrow 2T(n/2)$
3. Combine two solutions into overall solution $\leftarrow O(n)$

### Consequences
- Brute forces $O(n)^2$

---
## Summarize Divide and Conquer for Sorting
- Sorting can benefit greatly from Div & Conq
- Naively O(n^2) time by comparing all pairs of elements
- With D-C we reduce it to $O(n \log{n})$ time. ([[Merge Sort]], [[Quick Sort]]) 