---
type: problem
source: neetcode
number: 217
url: https://neetcode.io/problems/duplicate-integer
difficulty: Easy
pattern: Arrays & Hashing
patterns: ["Arrays & Hashing"]
topics: ["[[Career/Prep/topics/Data Structures/Arrays|Arrays]]", "[[Career/Prep/topics/Data Structures/Hash Tables|Hash Tables]]"]
solved_on: 2026-08-31
attempts: 1
aid: unaided
revisit: false
time: O(n)
space: O(n)
language: python
---

# 217 · Contains Duplicate

> [!question]- Problem
> Return true if any value appears at least twice in the array.

## Idea

A set answers “have I seen this before?” in O(1), so one pass is enough — no sorting, no nested loop.

## Optimal

```python
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False
```

## Why it works

Checking membership *before* inserting is what makes a single pass sufficient:
the moment you meet a value already in `seen`, the duplicate is proven, so you
can return without looking at the rest of the array.

The alternative framings are strictly worse. Sorting first and scanning
adjacent pairs is O(n log n). The nested-loop comparison is O(n²). Both trade
time to avoid the O(n) set — rarely the right trade unless memory is the
binding constraint.

## Template

The seen-set one-pass, which recurs constantly:

```python
seen = set()
for x in xs:
    if x in seen:
        return True
    seen.add(x)
return False
```

> [!tip] One-liner
> `len(set(nums)) != len(nums)` is the same idea compressed. It always scans
> the whole array, so it loses the early exit — same asymptotics, worse on
> inputs that duplicate early.

## Related

- [[Career/Prep/problems/Arrays & Hashing/1 · Two Sum|1 · Two Sum]] — same seen-set shape, storing indices instead of a bare set
- [[Career/Prep/problems/Arrays & Hashing/242 · Valid Anagram|242 · Valid Anagram]]
