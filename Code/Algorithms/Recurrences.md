
---
## Core Idea

- A **recurrence relation** describes the runtime of a recursive algorithm in terms of itself on smaller inputs.
    
- General form:
- $$
	\begin{aligned}
    T(n)=\text{cost of recursive calls}+\text{cost of extra work} \\
    \end{aligned}
    $$
---

## Big-O, Big-Omega, Big-Theta Recap

- **Big-O (O):** upper bound → "at most this fast"
    
- **Big-Omega (Ω):** lower bound → "at least this fast"
    
- **Big-Theta (Θ):** tight bound → "exactly this fast" (both upper & lower)
    
- **Little-o / Little-ω:** strict versions (strictly slower/faster)
    
> [[Times]]

**Constants in proofs:**

- $c$: multiplier to scale comparison function.
    
- $n_0$: cutoff; only need inequality for $n \ge n_0$.
    

---

## Common Growth Rate Hierarchy

$$
1 < \log{n} < n < n\log{n} < n^2 < n^3 < 2^n < n! < n^n
$$
---

## Techniques for Solving Recurrences

1. **Substitution method (guess & prove)**
    
    - Guess the form of the solution.
        
    - Prove by induction.
        
2. **Recursion tree method**
    
    - Expand recursion into a tree.
        
    - Compute cost at each level.
        
    - Add up totals across levels.
        
3. **[[Master Theorem]]** (shortcut for divide & conquer)  
    Works for recurrences of the form:
    $$
    T(n) = aT\left(\frac{n}{b}\right)+f(n)
    $$
    - $a$: number of subproblems
    - $b$: input size shrink factor
    - $f(n)$: extra work outside recursion
    
    See [[Master Theorem]] for complete details and proof.

---

## Examples

### Binary Search

Recurrence:

$$
T(n) = T\left(\frac{n}{2}\right)+1
$$

- Each step does constant work and halves the problem.
    
- Depth of tree = $\log n$.
    
- Total = $\Theta(\log n)$.

> [[Code/Topics/Algorithms/Binary Search/Binary Search]]

### Merge Sort

Recurrence:

$T(n)=2T(n/2)+n$

- Two recursive calls of size $n/2$.
    
- Merging costs $n$.
    
- Each level of tree costs $n$.
    
- Depth = $\log n$.
    
- Total = $\Theta(n \log n)$.

> [[Merge Sort]]
