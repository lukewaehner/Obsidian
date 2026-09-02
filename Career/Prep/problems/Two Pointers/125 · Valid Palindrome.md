---
type: problem
source: neetcode
number: 125
url: https://neetcode.io/problems/is-palindrome
difficulty: Easy
pattern: Two Pointers
patterns: ["Two Pointers", "Strings"]
topics: ["[[Career/Prep/topics/Strings/String Manipulation|String Manipulation]]"]
solved_on: 2026-08-31
attempts: 2
aid: unaided
revisit: false
time: O(n)
space: O(1)
language: python
---

# 125 · Valid Palindrome

> [!question]- Problem
> Return true if the string is a palindrome, considering only alphanumeric characters and ignoring case.

## Idea

Skip the non-alphanumerics *in place* from both ends, instead of building a cleaned copy first.

## Naive

Build a filtered lowercase copy, then walk two pointers over it:

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        

        cs = ""
        for c in s:
            if c.isalnum():
                cs += c.lower()
        print(cs)
        
        l = 0
        r = len(cs) - 1

        while l < r:
            if cs[l] != cs[r]:
               return False
            l += 1
            r -= 1
        return True
```

> [!warning] Defect
> Line 8 is a leftover `print(cs)` — debug output shipped in a submitted
> solution. It is harmless on the judge but would be a visible slip in an
> interview or a code review. Delete it.
>
> Separately, this version is O(n) in extra space for `cs`, which the problem
> is really asking you to avoid.

## Optimal

Two pointers over the original string, skipping non-alphanumerics as they move:

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1 or len(s) == 0:
            return True
        l = 0
        r = len(s) - 1
        while r >= l:
            while r > l and not s[r].isalnum():
                r -= 1
            while l < r and not s[l].isalnum():
                l += 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
```

## Why it works

The cleaned-copy version is not wrong, and it is the honest first answer — it
separates "normalise" from "compare", which is easier to reason about. The
second version fuses those two steps so nothing has to be materialised.

The inner `while` loops are the whole difference. Each advances a pointer past
characters that do not participate in the comparison, and each is guarded by
`r > l` / `l < r` so the pointers cannot cross while skipping. Both pointers
still only ever move inward, so the total work stays O(n) despite the nested
loops — every character is visited at most once by exactly one pointer.

Lowercasing is deferred to the comparison itself rather than done up front,
which is what removes the last reason to allocate.

> [!tip] The hidden cost in the first version
> `cs += c` inside a loop is quadratic in the general case, because each
> concatenation can copy the accumulated string. CPython has an optimisation
> that usually makes it amortised O(n), but it is an implementation detail, not
> a guarantee — `"".join(...)` is the version that is O(n) by construction.

## Template

Two pointers with skip conditions, the shape to reach for whenever some
elements are not participants:

```python
l, r = 0, len(s) - 1
while l < r:
    while l < r and not ok(s[l]): l += 1
    while l < r and not ok(s[r]): r -= 1
    if s[l] != s[r]: return False
    l += 1
    r -= 1
```

## Mistakes I made

Left a `print` in the first submission — worth a habit of scanning for debug
output before hitting submit.

The real lesson is the progression itself: the instinct was to normalise the
input into a clean form and then solve the easy problem. Fusing the two passes
is what buys the O(1) space, and it is the move most two-pointer string
problems want.

## Related

- The two-pointer skip shape recurs across the [[Career/Prep/problems/Two Pointers/Two Pointers|Two Pointers]] set
