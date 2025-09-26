
## Statement

The recurrence $T(n) = aT(n/b) + f(n)$ can be solved as follows:

**Case 1:** If $a \cdot f(n/b) = \kappa \cdot f(n)$ for some constant $\kappa < 1$, then $T(n) = \Theta(f(n))$.

**Case 2:** If $a \cdot f(n/b) = K \cdot f(n)$ for some constant $K > 1$, then $T(n) = \Theta(n^{\log_b a})$.

**Case 3:** If $a \cdot f(n/b) = f(n)$, then $T(n) = \Theta(f(n) \log_b n)$.

**Case 4:** If none of these three cases apply, you're on your own.

## Proof Intuition

**Case 1:** If $f(n)$ is a constant factor larger than $a \cdot f(n/b)$, then by induction, the level sums define a descending geometric series. The sum of any geometric series is a constant times its largest term. In this case, the largest term is the first term $f(n)$.

**Case 2:** If $f(n)$ is a constant factor smaller than $a \cdot f(n/b)$, then by induction, the level sums define an ascending geometric series. The sum of any geometric series is a constant times its largest term. In this case, this is the last term, which by our earlier argument is $\Theta(n^{\log_b a})$.

**Case 3:** If $a \cdot f(n/b) = f(n)$, then by induction, each of the $L + 1$ terms in the sum is equal to $f(n)$, and the recursion tree has depth $L = \Theta(\log_b n)$.

## Standard Form Comparison

The Master Theorem can also be stated in the more common form by comparing $f(n)$ with $n^{\log_b a}$:

- **Case 1:** If $f(n) = O(n^{\log_b a - \epsilon})$ for some $\epsilon > 0$, then $T(n) = \Theta(n^{\log_b a})$
- **Case 2:** If $f(n) = \Theta(n^{\log_b a})$, then $T(n) = \Theta(n^{\log_b a} \log n)$  
- **Case 3:** If $f(n) = \Omega(n^{\log_b a + \epsilon})$ for some $\epsilon > 0$, and $a \cdot f(n/b) \leq c \cdot f(n)$ for some $c < 1$, then $T(n) = \Theta(f(n))$

## Examples

### Binary Search: $T(n) = T(n/2) + 1$
- $a = 1, b = 2, f(n) = 1$
- $n^{\log_b a} = n^{\log_2 1} = n^0 = 1$
- $f(n) = \Theta(n^{\log_b a})$ → Case 2
- $T(n) = \Theta(1 \cdot \log n) = \Theta(\log n)$

### Merge Sort: $T(n) = 2T(n/2) + n$
- $a = 2, b = 2, f(n) = n$
- $n^{\log_b a} = n^{\log_2 2} = n^1 = n$
- $f(n) = \Theta(n^{\log_b a})$ → Case 2
- $T(n) = \Theta(n \log n)$
