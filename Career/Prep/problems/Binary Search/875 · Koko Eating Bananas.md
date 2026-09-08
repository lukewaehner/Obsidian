---
type: problem
source: neetcode
number: 875
url: https://neetcode.io/problems/eating-bananas
difficulty: Medium
pattern: Binary Search
patterns: ["Binary Search"]
topics: ["[[Career/Prep/topics/Sorting & Searching/Binary Search|Binary Search]]", "[[Career/Prep/topics/Complexity/Big-O and Asymptotic Notation|Big-O and Asymptotic Notation]]"]
solved_on: 2026-09-07
attempts: 1
aid: hint
revisit: false
time: O(n log m)
space: O(1)
language: python
---

# 875 · Koko Eating Bananas

> [!question]- Problem
> Given `piles` of bananas and `h` hours, find the smallest integer eating speed
> `k` such that eating `ceil(piles[i] / k)` hours per pile finishes every pile
> within `h` hours.

## Idea

There is nothing sorted to search — so search the *answer* instead: "can she
finish at speed `k`?" is false for every `k` below the answer and true for
every `k` above it, and that monotone step is all binary search ever needed.

## Optimal

```python
import math

class Solution:
    def testSpeed(self, t, ps, h):
        mt = 0
        for p in ps:
            mt += math.ceil(p / t)
        if mt <= h:
            return True
        else:
            return False
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_k = max(piles) # the absolute maximum needed - we can eat p piles at max_k because len(piles) >= h
        res = -1 # the target result
        l, r = 1, max_k
        while l <= r:
            m = (l + r) // 2
            # print(m)
            # print(self.testSpeed(m, piles, h))
            if self.testSpeed(m, piles, h):
                res = m
                r = m - 1
            else:
                l = m + 1
        return res
```

## Why it works

The move worth internalising is the reframing. Ordinary binary search needs a
sorted array; here the array is arbitrary. What is sorted is the *predicate*:
`testSpeed(k)` returns `False, False, …, False, True, True, …, True` as `k` runs
from 1 to `max(piles)`. That is a sorted boolean array in disguise, and the
answer is the index of its first `True`. Binary search finds boundaries in
sorted things — so it applies, even though nothing was handed to you sorted.

**The bounds are not arbitrary.** `l = 1` because a speed of zero never finishes.
`r = max(piles)` because at that speed every pile takes exactly one hour, so the
total is `len(piles)` hours — and the problem guarantees `h >= len(piles)`, so
the top of the range is always feasible. A larger `k` cannot help: you cannot
eat from two piles in the same hour, so one-hour-per-pile is the floor on time.
Correctly bounding the space is half the work in an answer-space search, and
the comment in the code shows the reasoning was actually done rather than
assumed.

**`res` is what makes the "shrink" branch safe.** When `testSpeed(m)` succeeds,
`m` is *an* answer but maybe not the smallest, so you record it and keep looking
left. When it fails, `m` and everything below it is ruled out. The loop exits
with `l > r` — pointing at nothing — and `res` holds the last feasible speed
seen, which is the smallest one. The alternative is to drop `res` and `return l`,
since `l` converges to the first feasible value; both are correct, and carrying
`res` is the version that is harder to get wrong under pressure.

The complexity is the product of the two loops: `O(log m)` binary search steps,
each paying `O(n)` to evaluate the predicate, so `O(n log m)` where
`m = max(piles)`. Note the log is over the *value* range, not the input length —
the giveaway that this is an answer-space search.

> [!tip] `math.ceil(p / t)` goes through a float
> `p / t` is floating-point division, so this is exact only while `p` fits in a
> double's 53-bit mantissa. It does here (`piles[i] <= 10^9`), so the code is
> correct — but the integer form `-(-p // t)` (or `(p + t - 1) // t`) does the
> same ceiling with no float in the path, and is the habit worth having for
> languages and ranges where the float would silently lose a unit.

## Template

Binary search on the answer space — reach for it when the question is "smallest
/ largest value such that some condition holds" and the condition is monotone:

```python
def feasible(k) -> bool:
    ...

lo, hi = MIN_ANSWER, MAX_ANSWER
res = -1
while lo <= hi:
    mid = lo + (hi - lo) // 2
    if feasible(mid):
        res = mid
        hi = mid - 1     # looking for the smallest; flip to lo = mid + 1 for largest
    else:
        lo = mid + 1
return res
```

## Mistakes I made

Took a hint — and it is worth naming what the hint was for, because it was not
the binary search. The mechanics were fine. The gap was recognising that a
problem with no sorted input can still be a binary search problem, because the
thing being searched is the range of possible answers. "Minimise `k` subject to
a monotone constraint" is the signal.

The first submission left two `print` calls inside the loop. They do not change
the result, but they run `O(log m)` times against stdout, which is a real way to
lose a submission to the time limit on a larger test set. Second submission just
commented them out.

## Related

- [[Career/Prep/problems/Binary Search/704 · Binary Search|704 · Binary Search]] — the same skeleton, searching an actual array rather than an answer range
- [[Career/Prep/topics/Sorting & Searching/Binary Search|Binary Search]]
