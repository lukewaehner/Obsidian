#sorting #divide-and-conquer #stable

## TL;DR
- **Type:** Comparison sort, divide & conquer
- **Stable:** Yes (natural implementation)
- **In-place:** Not in the straightforward array version (needs Θ(n) aux); linked-list version is in-place
- **Time:** Θ(n log n) in **best/avg/worst**
- **Extra space:** Θ(n) (array), Θ(1) (linked list)

## Idea

Divide the array into halves, recursively sort each half, then **merge** two sorted lists in linear time.

## Pseudocode (top-down)

```
MERGESORT(A, lo, hi):  
    if lo >= hi: return  
    mid = floor((lo + hi)/2)  
    MERGESORT(A, lo, mid)  
    MERGESORT(A, mid+1, hi)  
    MERGE(A, lo, mid, hi)

MERGE(A, lo, mid, hi):  
    L = A[lo..mid], R = A[mid+1..hi]  
    i = 0; j = 0; k = lo  
    
    while i < len(L) and j < len(R):  
        if L[i] <= R[j]:    // "≤" preserves stability  
            A[k] = L[i]; i = i + 1  
        else:  
            A[k] = R[j]; j = j + 1  
        k = k + 1  
    
    // copy any remainder  
    while i < len(L): A[k] = L[i]; i++; k++  
    while j < len(R): A[k] = R[j]; j++; k++
```

## Correctness (Sketch)

- **By induction:** recursive calls return sorted halves.

- **Merge maintains invariant:** `A[lo..k-1]` is the sorted merge of `L[0..i-1]` and `R[0..j-1]`.

- **Stability** from using `≤` when equal.

## Complexity

- **Recurrence:** $T(n) = 2T(n/2) + \Theta(n) \Rightarrow \Theta(n\log n)$ (Master Theorem).

- **All cases** are Θ(n log n) because work is dominated by the merge step each level.

- **Space:** Θ(n) auxiliary buffer; linked-list mergesort achieves Θ(1) extra.

## Variants & Optimizations

- **Bottom-up mergesort:** iterative; merge runs of size 1, 2, 4, …

- **TimSort** (Python/Java): hybrid of mergesort + run detection + galloping; stable; excellent on partially sorted data.

- **Natural mergesort:** detect existing runs to reduce passes.

- **In-place mergesort:** possible but complex; larger constants.

- **Small-subarray cutoff:** switch to insertion sort for tiny segments.

- **External mergesort:** for huge data on disk; multi-way merges minimize I/O.

- **Linked-list mergesort:** split via fast/slow pointers; stable, in-place.

## Cache & Parallelism

- **Cache behavior:** sequential scans during merge are cache-friendly; extra buffer can help locality.

- **Parallel mergesort:** both halves sort in parallel; parallel merge with partitioning by binary searches.

## When to Use

- When **stability** is required (e.g., multi-key sorts).

- **External sorting** (large, disk-resident datasets).

- Sorting **linked lists** efficiently.

---

## Quicksort vs Mergesort (At a Glance)

- **Time:** QS avg Θ(n log n), worst Θ(n²); MS Θ(n log n) worst-case guaranteed.

- **Space:** QS Θ(log n) stack; MS Θ(n) aux (array).

- **Stability:** QS no (default); MS yes.

- **Practical speed:** QS often faster in-memory due to in-place partition + smaller constants; MS shines when stability/external sort matters.

---

## Proof/Math Nuggets

- **Quicksort average:**  
  $$\mathbb{E}[T(n)] = \Theta(n \log n)$$
  via linearity of expectation over all pivot positions;  
  exact count of comparisons ≈ $2n\ln n + O(n)$.

- **Mergesort levels:**  
  $\log_2 n$ levels; each level does Θ(n) work ⇒ Θ(n log n).

---
