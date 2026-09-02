---
type: problem
source: neetcode
number: 347
url: https://neetcode.io/problems/top-k-elements-in-list
difficulty: Medium
pattern: Arrays & Hashing
patterns: ["Arrays & Hashing", "Heap & Priority Queue"]
topics: ["[[Career/Prep/topics/Data Structures/Hash Tables|Hash Tables]]", "[[Career/Prep/topics/Sorting & Searching/Counting and Radix Sort|Counting and Radix Sort]]", "[[Career/Prep/topics/Data Structures/Heaps and Priority Queues|Heaps and Priority Queues]]"]
solved_on: 2026-08-31
attempts: 1
aid: unaided
revisit: false
time: O(n)
space: O(n)
language: python
---

# 347 · Top K Frequent Elements

> [!question]- Problem
> Return the `k` most frequent elements.

## Idea

A frequency can never exceed `n`, so you can index buckets *by* frequency and read them from the top — which beats sorting.

## Optimal

```python
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k or len(nums) == 1:
            return nums
        
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            buckets[freq].append(num)
        
        result = []
        for freq in range(len(buckets) -1, 0, -1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result

        return result
```

## Why it works

The move that gets this under O(n log n) is recognising the range of the
values you would otherwise sort. Frequencies live in `[1, n]`, so instead of
ordering them you can place each number into `buckets[freq]` and walk the
buckets downward. That is a counting sort with the reconstruction step
replaced by an early exit once `k` items are collected.

The two standard alternatives are both slower for the same reason: sorting the
count pairs is O(n log n), and a size-`k` heap is O(n log k). The heap wins
only when `k` is tiny and memory matters — worth knowing as the follow-up
answer when an interviewer asks for O(1) extra space beyond the output.

`buckets` is sized `len(nums) + 1` because a frequency of exactly `n` must be
addressable; index 0 is left unused and the downward loop stops before it.

> [!tip] The early return is safe, but only because of a constraint
> `if len(nums) == k` returns `nums` unfiltered. That is correct here **only**
> because the problem guarantees `k ≤ number of distinct elements` — which
> forces every element to be distinct when `k == len(nums)`. Relax that
> guarantee and the line returns duplicates. It is a shortcut resting on an
> external promise rather than on the code, which is worth noticing.

## Template

```python
buckets = [[] for _ in range(len(nums) + 1)]
for num, freq in count.items():
    buckets[freq].append(num)
for freq in range(len(buckets) - 1, 0, -1):
    for num in buckets[freq]:
        ...
```

## Mistakes I made

Nothing — this landed first try. The four synced submissions are the same
bytes; NeetCode was down and the submit button got hit repeatedly.

## Related

- [[Career/Prep/problems/Arrays & Hashing/217 · Contains Duplicate|217 · Contains Duplicate]] — the counting half, without the ranking
- Bucketing by a bounded key is the same trick as [[Career/Prep/topics/Sorting & Searching/Counting and Radix Sort|Counting and Radix Sort]]
