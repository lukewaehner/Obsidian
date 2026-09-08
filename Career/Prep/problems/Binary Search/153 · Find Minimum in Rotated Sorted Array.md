---
type: problem
source: neetcode
number: 153
url: https://neetcode.io/problems/find-minimum-in-rotated-sorted-array
difficulty: Medium
pattern: Binary Search
patterns: ["Binary Search"]
topics: ["[[Career/Prep/topics/Sorting & Searching/Binary Search|Binary Search]]", "[[Career/Prep/topics/Data Structures/Arrays|Arrays]]"]
solved_on: 2026-09-07
attempts: 1
aid: unaided
revisit: false
time: O(log n)
space: O(1)
language: python
---

# 153 · Find Minimum in Rotated Sorted Array

> [!question]- Problem
> A sorted array of distinct integers has been rotated an unknown number of
> times. Return its minimum element in O(log n).

## Idea

Comparing the midpoint to the *right end* tells you which side the rotation
point fell on, so half the array can be discarded without ever finding the pivot
explicitly.

## Optimal

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]
        while l <= r:
            m = l + (r-l) // 2
            # track any better minimum
            res = min(res, nums[m])
            # if the right point in our search is less than the middle, the rotation happened exclusively right
            # we shift into the right side
            if nums[m] > nums[r]:
                l = m + 1 
            else:
                # the inverse stands for the left side
                r = m - 1
        # after the two pointers have met, we are guarantted to have homed in on the minimum point, since there is no (stop at the minimum here)
        return res
```

## Why it works

A rotated sorted array is two ascending runs glued together, and the minimum is
the first element of the second run. The whole problem is deciding which run the
midpoint is in.

**Compare against `nums[r]`, not `nums[l]`.** If `nums[m] > nums[r]`, then `m`
sits in the *left* (higher) run — the array must drop somewhere between `m` and
`r`, so the minimum is strictly to the right and `l = m + 1` is safe. Otherwise
`m..r` is one clean ascending run, so nothing to the right of `m` beats
`nums[m]`, and the minimum is at `m` or left of it. Comparing against `nums[l]`
instead is the version that needs an extra case, because a fully unrotated array
satisfies `nums[m] >= nums[l]` while its minimum is at `l` — the right-end
comparison has no such blind spot.

**`res = min(res, nums[m])` is what lets the bounds be sloppy.** The branch that
does `r = m - 1` throws away `m` — and `m` might have *been* the minimum. Most
write-ups avoid that by using `while l < r` with `r = m` and returning `nums[l]`,
which never discards a candidate. This version instead keeps the standard
inclusive `l <= r` skeleton and records every midpoint it visits before
discarding it, so nothing can be lost. Seeding `res = nums[0]` rather than
`float('inf')` also handles the single-element array before the loop even runs.

Same shape as [[Career/Prep/problems/Binary Search/704 · Binary Search|704]]:
each iteration strictly shrinks `[l, r]`, so it terminates in O(log n) steps
with O(1) extra space. The invariant is *the minimum is always inside `[l, r]`,
or already stored in `res`* — and both branches preserve it.

> [!tip] Distinct elements is load-bearing
> With duplicates (LeetCode 154), `nums[m] > nums[r]` no longer discriminates —
> `[3, 3, 1, 3]` and `[3, 1, 3, 3]` can present the same `m` and `r`. The fix is
> to shrink `r` by one when `nums[m] == nums[r]`, which drags the worst case to
> O(n). Worth knowing that the guarantee is what buys the log.

## Template

Rotation-aware binary search, midpoint against the right end:

```python
l, r = 0, len(a) - 1
res = a[0]
while l <= r:
    m = l + (r - l) // 2
    res = min(res, a[m])
    if a[m] > a[r]:
        l = m + 1        # the drop is to the right
    else:
        r = m - 1        # m..r is sorted; look left
return res
```

## Related

- [[Career/Prep/problems/Binary Search/33 · Search in Rotated Sorted Array|33 · Search in Rotated Sorted Array]] — same rotated input, asking for a target instead of the minimum
- [[Career/Prep/problems/Binary Search/704 · Binary Search|704 · Binary Search]] — the unrotated base case
- [[Career/Prep/topics/Sorting & Searching/Binary Search|Binary Search]]
