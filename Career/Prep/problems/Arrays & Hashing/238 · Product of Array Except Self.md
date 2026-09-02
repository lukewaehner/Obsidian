---
type: problem
source: neetcode
number: 238
url: https://neetcode.io/problems/products-of-array-discluding-self
difficulty: Medium
pattern: Arrays & Hashing
patterns: ["Arrays & Hashing"]
topics: ["[[Career/Prep/topics/Data Structures/Arrays|Arrays]]"]
solved_on: 2026-08-31
attempts: 2
aid: hint
revisit: false
time: O(n)
space: O(1) extra, excluding the output
language: python
---

# 238 · Product of Array Except Self

> [!question]- Problem
> Return an array where `answer[i]` is the product of every element except `nums[i]`, without using division.

## Idea

The answer at `i` is (everything to its left) × (everything to its right), and each side is one sweep.

## Naive

Two auxiliary arrays, one for each direction. Correct, O(n) time — but O(n)
extra space. The scratch comments are the working-out, left in as submitted:

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # load pref suf with 1s
        prefixes = [1] * len(nums)
        suffixes = [1] * len(nums)
        res = []
        # prefix + suffix of i 

        # [1, 2, 3]
        # pref: [1, 1, 1]
        # go:
        # pref: [1, 1, 1]
        # pref: [1, 1, 1]
        # pref: [1, 1, 2]
        
        # fill prefixes:
        for i in range(len(nums) - 1):
            prefixes[i+1] = prefixes[i] * nums[i]

        for i in range(len(nums)-1, 0, -1):
            suffixes[i-1] = suffixes[i] * nums[i]    
        # print(prefixes)
        # print(suffixes)
        for i in range(len(prefixes)):
            res.append(prefixes[i] * suffixes[i])
        # print(res)
        return res
```

## Optimal

Same two sweeps, but the output array carries the prefix pass and the suffix
collapses into a single running scalar:

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        
        return res
```

## Why it works

Both versions compute the same two quantities. The difference is where the
prefix products are *stored*.

The first sweep writes each prefix straight into `res[i]` — at that moment
`res[i]` holds the product of everything strictly left of `i`. The second
sweep then walks backwards multiplying in `suffix`, which holds the product of
everything strictly right of `i`. Because the suffix is only ever a scalar
carried between iterations, the second array disappears.

The ordering inside each loop is the whole trick: `res[i]` is read/written
*before* `prefix`/`suffix` absorbs `nums[i]`, which is what keeps element `i`
out of its own product. Swap those two lines and every entry silently includes
itself.

The output array does not count against the space bound by convention — worth
saying out loud in an interview rather than assuming it is granted.

## Template

```python
res = [1] * n
prefix = 1
for i in range(n):
    res[i] = prefix
    prefix *= nums[i]
suffix = 1
for i in range(n - 1, -1, -1):
    res[i] *= suffix
    suffix *= nums[i]
```

## Mistakes I made

Got the two-array version unaided — the prefix/suffix decomposition was the
real insight and that part came without help. Needed a hint only for the space
optimisation: that the output array can hold the prefix pass, so the suffix
never needs an array of its own.

Worth remembering as a general move rather than a trick for this problem —
**when a second pass only ever reads one accumulated value, that array can
become a scalar.**

## Related

- The prefix-sum family generally; this is its multiplicative sibling
