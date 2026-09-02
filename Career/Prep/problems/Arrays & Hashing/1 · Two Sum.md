---
type: problem
source: neetcode
number: 1
url: https://neetcode.io/problems/two-integer-sum
difficulty: Easy
pattern: Arrays & Hashing
patterns: ["Arrays & Hashing"]
topics: ["[[Career/Prep/topics/Data Structures/Arrays|Arrays]]", "[[Career/Prep/topics/Data Structures/Hash Tables|Hash Tables]]"]
solved_on: 2026-08-31
attempts: 1
aid: hint
revisit: false
time: O(n)
space: O(n)
language: python
---

# 1 · Two Sum

> [!question]- Problem
> Return the indices of the two numbers that add to `target`. Exactly one answer exists.

## Idea

Store value → index as you go, and for each number ask whether its complement is already *behind* you.

## Optimal

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            if (target - num) in seen:
                return [seen[target-num], i]
            else:
                seen[num] = i
        return []
            
```

## Why it works

The insight worth keeping is that you never need to look forward. For any
valid pair `(i, j)` with `i < j`, by the time the loop reaches `j` the value at
`i` is already in `seen`. So checking backwards at every step covers every
pair, and one pass is enough.

Checking the complement *before* inserting `num` also handles the
`target == 2 * num` case correctly — it stops an element pairing with itself,
because it is not yet in the map when its own complement is looked up.

## Template

```python
seen = {}
for i, x in enumerate(xs):
    if target - x in seen:
        return [seen[target - x], i]
    seen[x] = i
```

## Mistakes I made

Needed a hint here. The instinct was the O(n²) double loop, and then a
two-pass version that builds the whole map first. The leap is realising the map
only has to contain what you have already walked past — which collapses it to
one pass and, more importantly, makes the self-pairing edge case disappear
rather than needing a guard.

## Related

- [[Career/Prep/problems/Arrays & Hashing/217 · Contains Duplicate|217 · Contains Duplicate]] — the same one-pass shape without the index bookkeeping
