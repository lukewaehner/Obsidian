---
type: problem
source: neetcode
number: 704
url: https://neetcode.io/problems/binary-search
difficulty: Easy
pattern: Binary Search
patterns: ["Binary Search"]
topics: ["[[Career/Prep/topics/Sorting & Searching/Binary Search|Binary Search]]", "[[Career/Prep/topics/Complexity/Big-O and Asymptotic Notation|Big-O and Asymptotic Notation]]"]
solved_on: 2026-09-02
attempts: 1
aid: unaided
revisit: false
time: O(log n)
space: O(1)
language: python
---

# 704 · Binary Search

> [!question]- Problem
> Return the index of `target` in a sorted array, or -1.

## Idea

Halve the search space every step by comparing against the middle element.

## Optimal

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            mi = lo + (hi - lo) // 2
            if target == nums[mi]:
                return mi
            elif target > nums[mi]:
                lo = mi + 1
            else:
                hi = mi - 1
        return -1
```

## Why it works

The textbook form, and the details that are easy to get wrong are all correct
here — which is worth recording, because binary search is famous for being
easy to describe and hard to write.

**`while lo <= hi`, not `<`.** The interval is *inclusive* on both ends, so
`lo == hi` still contains one unexamined element. Using `<` skips it and fails
whenever the target sits at the final candidate position.

**`mi + 1` and `mi - 1`, not `mi`.** `nums[mi]` has just been ruled out, so
excluding it is what guarantees the interval shrinks every iteration. Assigning
`lo = mi` instead is the classic infinite loop: with two elements left, `mi`
rounds down to `lo` and nothing moves.

**`lo + (hi - lo) // 2`, not `(lo + hi) // 2`.** These are equal in Python,
whose integers are arbitrary precision. The habit matters in C, Java or Rust,
where `lo + hi` can overflow — the bug that famously sat in the JDK's own
binary search for nine years. Writing it this way costs nothing and is a
signal to a reader that you know about it.

The invariant that makes it correct: *if the target is in the array, it is
always within `[lo, hi]`*. Every branch preserves that, and the loop exits only
when the interval is empty — at which point the target genuinely is not there.

## Template

Worth memorising in exactly this shape:

```python
lo, hi = 0, len(a) - 1
while lo <= hi:
    mi = lo + (hi - lo) // 2
    if a[mi] == target:
        return mi
    elif a[mi] < target:
        lo = mi + 1
    else:
        hi = mi - 1
return -1
```

## Mistakes I made

Solved unaided, but the submission index says it took several passes to land —
which is the normal experience with this problem and exactly why the three
details above are worth having memorised rather than re-derived under
pressure.

## Related

- [[Career/Prep/problems/Binary Search/74 · Search a 2D Matrix|74 · Search a 2D Matrix]] — the same search run twice, or once over a flattened index space
- [[Career/Prep/topics/Sorting & Searching/Binary Search|Binary Search]]
