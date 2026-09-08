---
type: problem
source: neetcode
number: 33
url: https://neetcode.io/problems/find-target-in-rotated-sorted-array
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

# 33 · Search in Rotated Sorted Array

> [!question]- Problem
> A sorted array of distinct integers has been rotated an unknown number of
> times. Return the index of `target`, or -1, in O(log n).

## Idea

Whichever way the array is cut, at least one half of `[l, m, r]` is still
properly sorted — so identify that half, and you can test membership by a plain
range comparison.

## Optimal

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r-l) // 2
            if nums[m] == target:
                return m
            elif nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    # nums[l] is less less or the target and
                    # less than the midpoint, we have a sorted left
                    # segment, which target resides
                    r = m - 1
                else:
                    # The pivot hit somewhere within the left 
                    # side of the array
                    # we will not find target there
                    l = m + 1
            else:
                # the same logic applied on the right side
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1
```

## Why it works

The rotation destroys the one property binary search depends on — but only
globally. Locally it survives: cut the window at `m`, and the pivot can only
land in one of the two halves, so the *other* half is a contiguous ascending
run. That is the entire insight, and everything else is bookkeeping.

**`nums[l] <= nums[m]` identifies the sorted half.** If it holds, `l..m` is a
clean run; otherwise the pivot is somewhere in `l..m`, which means `m..r` is the
clean one. The `<=` rather than `<` matters: when the window narrows to two
elements, `m == l`, and `nums[l] < nums[m]` would be false — misclassifying a
perfectly sorted left half as the rotated one and sending the search the wrong
way.

**Once a half is known sorted, membership is a range test, not a search.** In
the left-sorted case, `nums[l] <= target < nums[m]` decides it outright: the run
is ascending and contains every value between its endpoints, so if `target` is
inside that interval it must be in that half, and if it is not, it cannot be —
go right. The asymmetric bounds are deliberate. `nums[m]` was already tested for
equality at the top of the loop, so it is excluded with `<`, while `nums[l]` has
not been, so it is included with `<=`. The mirrored branch flips this for the
same reason: `nums[m] < target <= nums[r]`.

Every path either returns or moves a bound past `m`, so the window shrinks
every iteration — O(log n) time, O(1) space, and the same
[[Career/Prep/problems/Binary Search/704 · Binary Search|704]] termination
argument. With a rotation of zero it degenerates to exactly that plain binary
search, since the left half is always the sorted one.

> [!tip] Two searches would also work, and this is better
> The obvious alternative is to run
> [[Career/Prep/problems/Binary Search/153 · Find Minimum in Rotated Sorted Array|153]]
> to find the pivot, then binary search the correct half — also O(log n), but two
> passes and an index-offset calculation that is easy to fumble. Deciding the
> sorted half inline does it in one pass with no arithmetic on wrapped indices.

## Template

Binary search over a rotated array — pick the sorted half, then range-test:

```python
l, r = 0, len(a) - 1
while l <= r:
    m = l + (r - l) // 2
    if a[m] == target:
        return m
    if a[l] <= a[m]:                      # left half is sorted
        if a[l] <= target < a[m]:
            r = m - 1
        else:
            l = m + 1
    else:                                 # right half is sorted
        if a[m] < target <= a[r]:
            l = m + 1
        else:
            r = m - 1
return -1
```

## Related

- [[Career/Prep/problems/Binary Search/153 · Find Minimum in Rotated Sorted Array|153 · Find Minimum in Rotated Sorted Array]] — same rotated input, locating the pivot instead of a target
- [[Career/Prep/problems/Binary Search/704 · Binary Search|704 · Binary Search]] — the unrotated base case this degrades to when the rotation is zero
- [[Career/Prep/topics/Sorting & Searching/Binary Search|Binary Search]]
