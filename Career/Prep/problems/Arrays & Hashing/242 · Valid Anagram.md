---
type: problem
source: neetcode
number: 242
url: https://neetcode.io/problems/is-anagram
difficulty: Easy
pattern: Arrays & Hashing
patterns: ["Arrays & Hashing"]
topics: ["[[Career/Prep/topics/Data Structures/Hash Tables|Hash Tables]]", "[[Career/Prep/topics/Strings/String Manipulation|String Manipulation]]"]
solved_on: 2026-08-31
attempts: 2
aid: unaided
revisit: false
time: O(n)
space: O(k) for k distinct characters
language: python
---

# 242 · Valid Anagram

> [!question]- Problem
> Return true if `t` is an anagram of `s`.

## Idea

Count up for one string and down for the other; an anagram leaves every count at zero.

## Naive

The first version — correct, and the counting is already the right idea:

```python
from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Early exit if strings don't have same length - impossible case
        if len(s) != len(t):
            return False

        counts = defaultdict(int)
        for c in s:
            counts[c] +=1
        for c in t:
            counts[c] -= 1
        
        for val in counts:
            if counts[val] != 0:
                return False
        return True
```

## Optimal

The second version, same algorithm with the final check tightened:

```python
from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Early exit if strings don't have same length - impossible case
        if len(s) != len(t):
            return False

        counts = defaultdict(int)
        for c in s:
            counts[c] +=1
        for c in t:
            counts[c] -= 1
        
        return all(v == 0 for v in counts.values())
```

## Why it works

The single-dictionary increment/decrement trick is better than building two
counts and comparing them: it halves the memory and removes the question of
what to do about keys present in one map but not the other. A character only
in `t` drives its count negative, which the zero-check catches just as well as
a positive leftover.

The length guard is not an optimisation, it is a correctness shortcut —
without it, `s = "a"`, `t = "aa"` would still net to a non-zero count, so the
guard is redundant here, but it exits in O(1) on the common mismatch.

> [!tip] Naming trap in the first version
> `for val in counts` iterates **keys**, not values — so `val` is a character
> and `counts[val]` is its count. It works, but the name says the opposite of
> what it holds. The second version's `counts.values()` removes both the
> indirection and the misleading name.

## Template

```python
counts = defaultdict(int)
for c in s: counts[c] += 1
for c in t: counts[c] -= 1
return all(v == 0 for v in counts.values())
```

## Mistakes I made

Nothing wrong — the second submission was a readability pass, not a fix. Worth
noting that the improvement came from naming: once the loop said `values()`,
the awkward key-indexing disappeared on its own.

## Related

- [[Career/Prep/problems/Arrays & Hashing/49 · Group Anagrams|49 · Group Anagrams]] — the same count signature, used as a grouping key
