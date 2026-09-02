---
type: problem
source: neetcode
number: 11
url: https://neetcode.io/problems/max-water-container
difficulty: Medium
pattern: Two Pointers
patterns: ["Two Pointers"]
topics: ["[[Career/Prep/topics/Data Structures/Arrays|Arrays]]", "[[Career/Prep/topics/Algorithm Design/Greedy Algorithms|Greedy Algorithms]]"]
solved_on: 2026-09-01
attempts: 1
aid: unaided
revisit: false
time: O(n)
space: O(1)
language: python
---

# 11 · Container With Most Water

> [!question]- Problem
> Given heights, pick two lines that with the x-axis hold the most water. Return that area.

## Idea

Width shrinks on every step no matter what, so the only move that can ever help is discarding the shorter wall.

## Optimal

```python
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_water = 0
        while l < r:
            height = min(heights[l], heights[r])
            area = height * (r - l)
            # print(area)
            if area > max_water:
                max_water = area

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            # print(l,r)
            # print(heights[l], heights[r])
        return max_water
```

## Why it works

The exchange argument is the whole problem, and it is worth being able to state
it out loud:

The area is `min(h[l], h[r]) * (r - l)`, so it is capped by the **shorter**
wall. Suppose `h[l] < h[r]`. Consider every pair that still uses `l`. All of
them have width smaller than `r - l`, and all of them are still capped by
`h[l]` or less — because the height term can never exceed `h[l]` while `l` is
one of the two walls. So every remaining pair involving `l` is strictly worse
than the one just measured. `l` can be discarded outright.

That is what licenses a single pass: each step permanently eliminates one
candidate wall having proven no unexamined pair through it can win. The
brute-force O(n²) comparison is doing the same search without the proof.

Moving the *taller* wall would be the mistake — it shrinks the width without
lifting the cap, so it can only make things worse.

> [!tip] Leftover scaffolding
> Three commented-out `print` lines survive in the submitted version. They are
> inert, unlike the live `print` in
> [[Career/Prep/problems/Two Pointers/125 · Valid Palindrome|125 · Valid Palindrome]]
> — but worth clearing out before a real review reads it.

## Template

```python
l, r = 0, len(a) - 1
best = 0
while l < r:
    best = max(best, min(a[l], a[r]) * (r - l))
    if a[l] < a[r]:
        l += 1
    else:
        r -= 1
```

## Related

- [[Career/Prep/problems/Two Pointers/167 · Two Sum II - Input Array Is Sorted|167 · Two Sum II]] — converging pointers driven by a comparison rather than a greedy argument
