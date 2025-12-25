---
## Topic:
---
---
# Pivoting as a Sorting Algorithm

- Pivoting can be used as the basis of a sorting algorithm.
- Process:
  - Perform pivoting.
  - Recursively sort the left and right halves.

## Complexity Considerations
- Same problems as before with finding a good pivot.
- Worst-case complexity: Θ(n²) (exercise).
- Use Median of Medians (MoM) to get a good pivot.
  - In this case, runtime becomes Θ(n log n).
- Note: Here we put effort into **splitting** (unlike mergesort, which puts effort into **merging**).

## Randomized Approach
- Alternative: **Randomness!**
  - Pick a random element as the pivot.
  - Chance that it is a bad pivot is low.
- We won’t do a proof, but this also gives a runtime of Θ(n log n).
- In practice, due to large constants in MoM, randomized quicksort is commonly used.

---

# Quicksort
#sorting #divide-and-conquer

## TL;DR
- **Type:** Comparison sort, divide & conquer
- **Stable:** No (unless using special stable partition)
- **In-place:** Yes (typical implementations)
- **Average time:** Θ(n log n)
- **Worst time:** Θ(n²) (bad pivots)
- **Best time:** Θ(n log n)
- **Extra space:** Θ(log n) stack (average), Θ(n) if not in-place partition

## Idea
Pick a **pivot**, partition the array into elements `< pivot` and `≥ pivot`, then recursively sort the partitions.

## Pseudocode (Hoare-style; in-place)
```
QUICKSORT(A, lo, hi):  
if lo >= hi: return  
p = PARTITION(A, lo, hi) // returns final pivot index  
QUICKSORT(A, lo, p-1)  
QUICKSORT(A, p+1, hi)

PARTITION(A, lo, hi): // Lomuto (simple) version  
pivot = A[hi]  
i = lo  
for j = lo to hi-1:  
if A[j] < pivot:  
swap A[i], A[j]  
i = i + 1  
swap A[i], A[hi]  
return i
```

> Tip: For performance, prefer **Hoare partition** or **Dutch National Flag** (3-way) when there are many duplicates.

## Correctness (Sketch)
- **Loop invariant** of `PARTITION`: elements before `i` are `< pivot`, elements between `i` and `j-1` are `≥ pivot`.
- Recursion terminates as subarray size decreases.
- Result is permutation of input; post-partition pivot is in its final place; recursion sorts both sides.

## Complexity
- Let comparison cost be linear partitioning plus recursive calls.
- Recurrence with split sizes `k` and `n-k-1`:  
  \( T(n) = T(k) + T(n-k-1) + \Theta(n) \)
- **Worst case** (always extreme pivot): \( T(n) = T(n-1) + \Theta(n) = \Theta(n^2) \)
- **Best case** (perfectly balanced): \( T(n) = 2T(n/2) + \Theta(n) = \Theta(n\log n) \)
- **Average case** (random pivot or random input):  
  \( \mathbb{E}[T(n)] = 2(n+1)H_n - 4n = \Theta(n \log n) \) where \( H_n \) is the harmonic number.

## Pivot Selection
- **Random pivot**: expected Θ(n log n); tiny constants; widely used.
- **Median-of-Medians (MoM)**: deterministic linear-time pivot selection ⇒ worst-case Θ(n log n) but larger constants.
- **Median-of-3 / 5**: heuristic; reduces probability of bad splits.

## Practical Optimizations
- **Insertion-sort cutoff**: switch to insertion sort for small subarrays (e.g., size ≤ 16–32).
- **Tail recursion elimination**: recurse into smaller side, loop on larger to reduce stack depth to Θ(log n).
- **3-way partitioning**: handle many duplicates efficiently.
- **Cache behavior**: in-place linear scans are cache-friendly.
- **Introsort**: start with quicksort; if depth exceeds \( 2\lfloor\log_2 n\rfloor \), switch to heapsort to guarantee \( O(n\log n) \).

## When to Use
- General-purpose in-memory sorting of primitive types.
- Not ideal when **stability** is required (consider [[Mergesort]]), or when pathological pivoting is likely without safeguards.

---
