---
type: problem
source: neetcode
number: 853
url: https://neetcode.io/problems/car-fleet
difficulty: Medium
pattern: Stack
patterns: ["Stack", "Greedy"]
topics: ["[[Career/Prep/topics/Data Structures/Stacks|Stacks]]", "[[Career/Prep/topics/Sorting & Searching/Sorting Fundamentals|Sorting Fundamentals]]", "[[Career/Prep/topics/Algorithm Design/Greedy Algorithms|Greedy Algorithms]]", "[[Career/Prep/topics/Math & Bits/Floating Point Numbers|Floating Point Numbers]]"]
solved_on: 2026-09-02
attempts: 1
aid: unaided
revisit: false
time: O(n log n), dominated by the sort
space: O(n)
language: python
---

# 853 · Car Fleet

> [!question]- Problem
> Cars drive toward a target; a faster car catching a slower one joins its fleet and travels at the slower speed. How many fleets arrive?

## Idea

Process cars from the one closest to the target backwards — a car starts a new fleet only if it would arrive strictly later than the fleet already ahead of it.

## Optimal

```python
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        c = sorted(zip(position, speed), reverse=True)
        for i in range(len(speed)):
            ttt = (target - c[i][0]) / c[i][1]
            if not stack:
                stack.append(ttt)
            elif ttt > stack[-1]:
                stack.append(ttt)
        return len(stack)
```

## Why it works

Two moves make this tractable.

**Sort by position, descending.** Cars can only ever be caught by someone
behind them, so processing nearest-to-target first means every car is compared
against a fleet whose fate is already decided. Order the other way and you
would have to revisit decisions.

**Compare arrival times, not positions.** A car catches the one ahead exactly
when it would otherwise *arrive sooner* — `(target - pos) / speed` is that
arrival time assuming a clear road. So:

- `ttt > stack[-1]` — arrives later than the fleet ahead, never catches it, and
  becomes a new fleet.
- `ttt <= stack[-1]` — would arrive at the same time or sooner, so it is caught
  and absorbed. Absorbed cars are simply not pushed, and crucially the fleet's
  time stays the *slower* one already on the stack — which is what makes the
  comparison for the next car correct.

The `<=` matters: a car arriving at exactly the same time has caught the fleet
at the target line and counts as merged, not as a second fleet.

> [!tip] The stack here is a counter in disguise
> Nothing is ever popped — only pushed and its length read. So this runs in
> O(1) extra space with two scalars:
>
> ```python
> fleets, slowest = 0, 0.0
> for pos, spd in sorted(zip(position, speed), reverse=True):
>     t = (target - pos) / spd
>     if t > slowest:
>         fleets, slowest = fleets + 1, t
> return fleets
> ```
>
> The stack version is not wrong, and it is the shape the problem is usually
> taught in — but noticing that a stack you never pop is really an accumulator
> is a useful habit.

> [!tip] Float division
> `(target - pos) / speed` is exact enough for this problem's constraints, but
> comparing floats for `>` is the kind of thing that bites at larger scale. The
> exact form compares cross-multiplied integers:
> `(target - p1) * s2 > (target - p2) * s1`.

## Template

Sort so decisions become final, then a single greedy sweep comparing against
the best-so-far.

## Related

- [[Career/Prep/problems/Stack/739 · Daily Temperatures|739 · Daily Temperatures]] — the other Stack problem in this set, and a genuine monotonic stack
- [[Career/Prep/topics/Algorithm Design/Greedy Algorithms|Greedy Algorithms]]
