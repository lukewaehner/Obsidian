---
## Topic:
---

---
## Basics
- Statistical values characterizing order
- Minimum and maximum, these are special cases of order statistics
- The $k^{th}$ order statistics of a collection is the $k^{th}$ smallest value in it. Rank $k$ element.
- Minimum is $k=1$, maximum is $k=n$ (where n is the size of the collection).
- We also have other special order statistics:
	- Quartile: $0.25n$, $0.5n$, $0.75n$
	- Decile: $0.1n$, $0.2n$, $0.3n$, ..., $0.8n$, $0.9n$
	- Percentile: $0.1n$, $0.33n$, $0.68n$, $0.95n$, $0.99n$, etc.
	- Median: $[\frac{n}{2}]$
- There are extensive applications in statistics and inference
- We'll see the $1^{st}/n^{th}$ order statistics (max / min) show up a lot

---
## Finding order statistics $k$-Selection
- $k=1$ minimum and $k=n$ maximum can both be found in $\Theta(n)$ time.
- Note: $k$-selection is $\Omega(n)$ since we must look at all the data (Cannot be faster, must spend linear time)
	
- Using $\Theta(k)$ space, we can do $k$-selection in $\Theta(n)$ time.
- Without space usage, we can find minimums repeatedly and finish in $\Theta(kn)$ time.
	
- All of the above assumed unordered collection/list/array
- If sorted, k-selection is doable in $\Theta(1)$ for any value of $k$ (index into array)
	
- Spending $O(n\log{n})$ on sorting will allow $k$-selection in $\Theta(1)$
- Can we do selection without sorting and in $\Theta(n)$ for all k

---
## Pivot and Conquer
- Pick a pivot element $p$. It can be any element
- Split array into everything $\lt p$ (Left), everything $=p$ (Middle), everything $\gt p$ (Right)
- This is $\Theta(n)$. [[Divide and Conquer]]
- Let $\ell, m, r$ be the sizes of *Left, Middle and Right*
- We need to know where the rank *k* is compared to $\ell, m, r$
- If $k \leq \ell$. then rank $k$ element is on the left: recurse in *Left*
- If $\ell \lt k \leq \ell + m$, elements in the *Middle*, that is $p$ is the $k^{th}$ order statistic.
- If $k \gt \ell + m$, then rank $k$ element is in the right half.
- So we recurse on *Right*, to find $k^{'th}$ order statistic where $k' = k - \ell - m$

---
## Good and Bad Pivots

## Median of Medians
