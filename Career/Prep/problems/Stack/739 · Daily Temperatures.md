---
type: problem
source: neetcode
number: 739
url: https://neetcode.io/problems/daily-temperatures
difficulty: Medium
pattern: Stack
patterns: ["Stack"]
topics: ["[[Career/Prep/topics/Data Structures/Stacks|Stacks]]", "[[Career/Prep/topics/Data Structures/Arrays|Arrays]]"]
solved_on: 2026-09-02
attempts: 1
aid: unaided
revisit: false
time: O(n)
space: O(n)
language: python
---

# 739 · Daily Temperatures

> [!question]- Problem
> For each day, how many days until a warmer temperature? 0 if none.

## Idea

Keep the days that are still waiting for a warmer one on a stack; when a warmer day arrives it resolves all of them at once.

## Optimal

```python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # indices waiting for a warmer day, temps decreasing
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                j = stack.pop()
                res[j] = i - j
            stack.append(i)
        return res
```

## Why it works

This is the **monotonic stack**, and it is worth naming as a pattern rather
than remembering as a trick — it is the answer to a whole family of "next
greater / next smaller element" questions.

The stack holds *indices whose answer is not yet known*, and it is kept in
decreasing temperature order. That invariant is what makes the algorithm
correct: if day `a` is below day `b` on the stack, then `temps[a] >= temps[b]`,
so any day warm enough to resolve `a` has already resolved `b`. Resolving from
the top therefore resolves in the right order and never skips anyone.

The distance falls out for free — because the stack stores indices rather than
temperatures, `i - j` is the answer at the moment of resolution, with no
second pass.

**Why it is O(n) despite the nested loop.** Each index is pushed exactly once
and popped at most once, so the inner `while` runs at most `n` times *in
total* across the whole outer loop — not per iteration. Being able to say that
out loud is the point; a reader who only sees `for` around `while` will assume
O(n²).

Days still on the stack at the end never found a warmer day, and their answers
stay `0` from the initialisation — no cleanup pass needed.

## Template

The next-greater-element skeleton:

```python
res = [0] * len(a)
stack = []                      # indices, values decreasing
for i, x in enumerate(a):
    while stack and a[stack[-1]] < x:
        j = stack.pop()
        res[j] = i - j          # or a[i], for "next greater value"
    stack.append(i)
```

## Related

- [[Career/Prep/problems/Stack/853 · Car Fleet|853 · Car Fleet]] — also a stack, but driven by a greedy merge rather than a monotonic invariant
- [[Career/Prep/topics/Data Structures/Stacks|Stacks]]
