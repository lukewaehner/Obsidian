---
type: problem
source: neetcode
number: 155
url: https://neetcode.io/problems/minimum-stack
difficulty: Medium
pattern: Stack
patterns: ["Stack"]
topics: ["[[Career/Prep/topics/Data Structures/Stacks|Stacks]]"]
solved_on: 2026-09-01
attempts: 1
aid: unaided
revisit: false
time: O(1) for every operation
space: O(n)
language: python
---

# 155 · Min Stack

> [!question]- Problem
> Design a stack supporting push, pop, top and retrieving the minimum, all in constant time.

## Idea

Carry a second stack whose top is always the minimum of everything at or below it — so the min is never computed, only read.

## Optimal

```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
```

## Why it works

The naive `getMin` scans the stack, which is O(n). The requirement is O(1), so
the minimum has to be **maintained** rather than computed — and the reason a
single variable will not do is that `pop` has to *restore* the previous
minimum, which means history must be kept, not just the current value.

A parallel stack is that history. `min_stack[i]` holds the minimum of
`stack[0..i]`, so the answer is always `min_stack[-1]`.

> [!tip] This version avoids the classic bug, and it is worth knowing why
> There are two common shapes for this problem. The *conditional* one only
> pushes to `min_stack` when a new minimum arrives, which makes the two stacks
> different lengths — so `pop` has to check whether the value leaving is the
> current minimum, and pop `min_stack` only then. That comparison is where
> people get it wrong, especially with duplicate minima.
>
> This version pushes **on every call** — the current min if unchanged, the new
> value if smaller. The stacks stay the same length, so `pop` is unconditional
> and there is no comparison to get wrong. It trades a little memory for
> removing an entire class of bug. Good trade, and the one to reach for under
> interview pressure.

The `<=` in `val <= self.min_stack[-1]` is doing real work even here: with
duplicate minima it keeps the invariant simple, and in the conditional variant
using `<` instead is exactly the bug that drops a minimum too early.

## Template

```python
def push(self, val):
    self.stack.append(val)
    self.min_stack.append(
        val if not self.min_stack else min(val, self.min_stack[-1])
    )

def pop(self):
    self.stack.pop()
    self.min_stack.pop()
```

## Related

- [[Career/Prep/topics/Data Structures/Stacks|Stacks]] — the write-up this problem exercises
- The "maintain rather than compute" move recurs whenever a query must be O(1)
