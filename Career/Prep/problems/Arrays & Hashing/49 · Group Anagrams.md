---
type: problem
source: neetcode
number: 49
url: https://neetcode.io/problems/anagram-groups
difficulty: Medium
pattern: Arrays & Hashing
patterns: ["Arrays & Hashing"]
topics: ["[[Career/Prep/topics/Data Structures/Hash Tables|Hash Tables]]", "[[Career/Prep/topics/Strings/String Manipulation|String Manipulation]]"]
solved_on: 2026-08-31
attempts: 1
aid: unaided
revisit: false
time: O(m · n) for m words of average length n
space: O(m · n)
language: python
---

# 49 · Group Anagrams

> [!question]- Problem
> Group the strings that are anagrams of one another.

## Idea

Two words are anagrams exactly when their letter-count vectors match — so the count vector *is* the group key.

## Optimal

```python
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())
```

## Why it works

The whole problem is choosing a key that is equal for anagrams and different
for everything else. The 26-slot count vector is that key, and it costs O(n)
per word to build.

Sorting each word also produces a valid key and is the more obvious first
thought, but it costs O(n log n) per word. Counting wins because the alphabet
is bounded — you are effectively doing a counting sort and skipping the
reconstruction.

`tuple(count)` matters: a list is unhashable, so it cannot key a dict. The
conversion is what lets the count vector do the work.

> [!tip] The assumption in `[0] * 26`
> This hard-codes lowercase a–z, which the problem's constraints allow. It
> would break silently on uppercase, Unicode, or punctuation — a
> `defaultdict(int)` keyed by character, then `tuple(sorted(counts.items()))`,
> is the version that survives a loosened constraint.

## Template

```python
groups = defaultdict(list)
for s in strs:
    key = [0] * 26
    for c in s:
        key[ord(c) - ord('a')] += 1
    groups[tuple(key)].append(s)
return list(groups.values())
```

## Related

- [[Career/Prep/problems/Arrays & Hashing/242 · Valid Anagram|242 · Valid Anagram]] — same signature, comparing two words instead of grouping many
