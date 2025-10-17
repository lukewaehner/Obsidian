## Pseudocode

```
BINARY_SEARCH(A, target, low, high)
    if low > high
        return -1  // Element not found
    
    mid = (low + high) / 2
    
    if A[mid] == target
        return mid  // Element found at index mid
    else if A[mid] > target
        return BINARY_SEARCH(A, target, low, mid - 1)
    else
        return BINARY_SEARCH(A, target, mid + 1, high)
```

### Iterative Version
```
BINARY_SEARCH_ITERATIVE(A, target)
    low = 0
    high = length(A) - 1
    
    while low <= high
        mid = (low + high) / 2
        
        if A[mid] == target
            return mid
        else if A[mid] > target
            high = mid - 1
        else
            low = mid + 1
    
    return -1  // Element not found
```

## Time Complexity
- **Best Case**: O(1) - target is at the middle
- **Average Case**: O(log n)
- **Worst Case**: O(log n) - target is not in array or at the ends

**Space Complexity**: 
- Recursive: O(log n) due to call stack
- Iterative: O(1)

## Mathematical Analysis

$$
\begin{aligned}
\text{Binary Search: } &\quad T(n) = T\!\left(\frac{n}{2}\right) + O(1) \\
\text{Given: } &\quad T(n) = \lg(n) \\[6pt]

\text{Base case: } &\quad T(1) = \lg(1) = 0 = O(1) \\[6pt]

\text{Inductive Hypothesis: } &\quad \forall n \le k,\; T(n) = \lg(n) \\[6pt]

\text{Inductive Step: } &\quad T(k+1) = T\!\left(\frac{k+1}{2}\right) + O(1) \\
&= \lg\!\left(\frac{k+1}{2}\right) + O(1) \\
&= \lg(k+1) - \lg(2) + O(1) \\
&= O(\lg(k+1))
\end{aligned}
$$

$$
\implies \forall n,\; T(n) = O(\lg n)
$$

