---
type: problem
source: neetcode
number: 74
url: https://neetcode.io/problems/search-2d-matrix
difficulty: Medium
pattern: Binary Search
patterns: ["Binary Search"]
topics: ["[[Career/Prep/topics/Sorting & Searching/Binary Search|Binary Search]]", "[[Career/Prep/topics/Data Structures/Arrays|Arrays]]"]
solved_on: 2026-09-02
attempts: 1
aid: hint
revisit: false
time: O(log m + log n)
space: O(1)
language: python
---

# 74 · Search a 2D Matrix

> [!question]- Problem
> Search a matrix where each row is sorted and each row's first element exceeds the previous row's last.

## Idea

That second guarantee means the whole matrix is already one sorted sequence — so it can be searched as if it were a single flat array.

## Optimal

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # BS col 0, BS the proper row
        m = matrix
        l, r  = 0, len(m) - 1
        row = -1
        # column search to find the row to target
        while row == -1 and l <= r:
            mi = l + (r-l) // 2
            if m[mi][0] == target:
                return True
            elif m[mi][0] < target:
                # move right
                if mi == len(m) - 1:
                    row = mi
                elif m[mi+1][0] > target:
                    row = mi
                else:
                    l = mi + 1
            else:
                if mi == 0:
                    row = mi
                elif m[mi-1][0] < target:
                    row = mi - 1
                else: 
                    r = mi - 1
                
        print(row)
        
        # search within row
        l, r = 0, len(m[0]) - 1
        while l <= r:
            mi = l + (r-l) // 2
            if m[row][mi] == target:
                return True
            if m[row][mi] < target:
                l = mi + 1
            else:
                r = mi - 1
        return False
```

> [!warning] Defect
> `print(row)` is live debug output — it fires on every call, not a comment.
> Same slip as in
> [[Career/Prep/problems/Stack/150 · Evaluate Reverse Polish Notation|150 · Evaluate RPN]]
> and [[Career/Prep/problems/Two Pointers/125 · Valid Palindrome|125 · Valid Palindrome]].
> Delete it. That is three submissions now carrying a stray `print`, which is
> worth turning into a habit: scan for debug output before hitting submit.

## Why it works

The approach is right and the complexity is optimal — binary search column 0 to
find the candidate row, then binary search inside that row. O(log m + log n),
which is O(log(m·n)).

The row-finding loop is where it gets expensive to reason about. It is
searching for a **boundary** rather than an exact match, and boundary searches
are the hard case. It uses a `row = -1` sentinel plus four special cases
(`mi == len(m) - 1`, `m[mi+1][0] > target`, `mi == 0`, `m[mi-1][0] < target`).

I traced it and believe it is correct — including the case where `target` is
smaller than every element, where `row` becomes 0 and the row search then
correctly returns `False`. But *"I traced it and believe it is correct"* is an
uncomfortable place to be with a boundary search, and that discomfort is the
real finding here.

**The simplification worth taking away.** The problem guarantees the rows join
end to end, so the matrix **is** one sorted array of length `m·n`. Index `k`
maps to row `k // n`, column `k mod n` — and the whole thing collapses into a
single ordinary binary search. No sentinel, no special cases, no second loop:

```python
rows, n = len(matrix), len(matrix[0])
lo, hi = 0, rows * n - 1
while lo <= hi:
    mid = lo + (hi - lo) // 2
    val = matrix[mid // n][mid % n]
    if val == target:
        return True
    elif val < target:
        lo = mid + 1
    else:
        hi = mid - 1
return False
```

Same O(log(m·n)), a third of the code, and every line is the binary search from
[[Career/Prep/problems/Binary Search/704 · Binary Search|704]].

If a two-stage search *is* wanted, the clean way to find the row is an
upper-bound search: on `m[mi][0] > target` set `hi = mi - 1`, otherwise
`lo = mi + 1`, then take `row = hi` once the loop ends. No sentinel, no edge
cases.

## Template

Flattening a sorted 2-D grid into a 1-D index space, for `k` in `[0, m*n)`:

```python
val = matrix[k // n][k % n]
```

## Mistakes I made

Took a hint. The thing to carry forward is not the hint itself but the
recognition behind it: **the row-boundary version was hard because it was
solving a harder problem than necessary.** The guarantee that rows join end to
end was in the problem statement the whole time, and using it collapses two
searches into one.

Generalises well — when a binary search starts accumulating special cases at
the edges, that is usually the signal that the *search space* has been framed
wrong, not that the edges need more branches.

## Related

- [[Career/Prep/problems/Binary Search/704 · Binary Search|704 · Binary Search]] — the plain form this reduces to once the index space is flattened
