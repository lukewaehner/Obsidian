---
type: problem
source: neetcode
number: 3
url: https://neetcode.io/problems/longest-substring-without-duplicates
difficulty: Medium
pattern: Sliding Window
patterns: ["Sliding Window", "Arrays & Hashing"]
topics: ["[[Career/Prep/topics/Strings/String Manipulation|String Manipulation]]", "[[Career/Prep/topics/Data Structures/Hash Tables|Hash Tables]]"]
solved_on: 2026-09-08
attempts: 1
aid: unaided
revisit: false
time: O(n)
space: O(min(n, k)) for an alphabet of size k
language: python
---

# 3 · Longest Substring Without Repeating Characters

> [!question]- Problem
> Return the length of the longest substring of `s` containing no repeated characters.

## Idea

Extend a window to the right one character at a time; when the new character is
already inside the window, jump the left edge to just past its previous
occurrence rather than walking it forward.

## Optimal

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sm = {}
        l = 0
        ml = 0
        
        for r in range(len(s)):
            if s[r] in sm and sm[s[r]] >= l:
                l = sm[s[r]] + 1
                
            sm[s[r]] = r
            ml = max(ml, r - l + 1)
            
        return ml
```

## Why it works

The invariant is that `s[l:r+1]` never contains a duplicate. Everything else
follows from maintaining it.

**`sm` stores last index, not presence.** A set would answer "is this character
in the window?" but not "where", which is what makes the jump possible. Storing
the index lets the left edge move to `sm[c] + 1` in one assignment — the
smallest position at which the repeat is excluded.

**`sm[s[r]] >= l` is the whole subtlety.** Entries are never deleted from `sm`,
so it accumulates characters that have already fallen out of the window on the
left. Without the second condition, a stale index would drag `l` *backwards* and
silently readmit duplicates. Concretely, on `"abba"`:

| r | char | `sm` before | `l` | window |
|---|---|---|---|---|
| 0 | a | {} | 0 | `a` |
| 1 | b | {a:0} | 0 | `ab` |
| 2 | b | {a:0, b:1} | 2 | `b` |
| 3 | a | {a:0, b:2} | 2 | `ba` |

At `r = 3`, `a` is in `sm` at index `0`, but `0 < l = 2` — that `a` is behind the
window and must be ignored. Drop the guard and `l` becomes `1`, producing window
`"bba"` and the wrong answer `3`.

`>= l` and not `> l`: an index equal to `l` is the leftmost character *inside* the
window, a genuine duplicate, and `l` must move past it.

**Why it is linear.** `r` advances once per character and `l` only ever increases,
so together they take at most `2n` steps. The alternative — decrementing a count
map while walking `l` forward one at a time — is also O(n) amortised, but this
version does it in a single jump and needs no removal logic at all.

## Template

The last-seen-index window, which generalises to any "no repeats within k"
constraint:

```python
last = {}
left = best = 0
for right, c in enumerate(s):
    if c in last and last[c] >= left:
        left = last[c] + 1
    last[c] = right
    best = max(best, right - left + 1)
```

## Related

- [[Career/Prep/problems/Arrays & Hashing/217 · Contains Duplicate|217 · Contains Duplicate]] — duplicate detection with no window at all
- [[Career/Prep/topics/Data Structures/Hash Tables|Hash Tables]]
