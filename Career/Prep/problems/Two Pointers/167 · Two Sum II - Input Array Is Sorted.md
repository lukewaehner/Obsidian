---
type: problem
source: neetcode
number: 167
url: https://neetcode.io/problems/two-integer-sum-ii
difficulty: Medium
pattern: Two Pointers
patterns: ["Two Pointers", "Binary Search"]
topics: ["[[Career/Prep/topics/Data Structures/Arrays|Arrays]]"]
solved_on: 2026-09-01
attempts: 1
aid: hint
revisit: false
time: O(n)
space: O(1)
language: python
---

# 167 · Two Sum II - Input Array Is Sorted

> [!question]- Problem
> Given a **sorted** array, return the 1-indexed positions of the two numbers that add to `target`. Exactly one solution exists, and you may not use extra space.

## Idea

Because the array is sorted, the sum at `(l, r)` tells you which pointer to move: too big means the right end is too large, too small means the left end is.

## Optimal

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while True:
            res = numbers[r] + numbers[l]

            if res == target:
                return [l + 1, r + 1]
            elif res > target:
                r -= 1
            else:
                l += 1
        return []
```

## Why it works

This is the payoff for the array being sorted, and it is worth seeing exactly
what that buys.

[[Career/Prep/problems/Arrays & Hashing/1 · Two Sum|Two Sum]] on an unsorted
array needs a hash map, because there is no way to tell where the complement
might be — so you pay O(n) space to remember everything you have seen. Here,
sortedness means the sum is monotonic in each pointer: moving `l` right can
only increase the sum, moving `r` left can only decrease it. That turns the
search into a decision at each step, so nothing has to be remembered and the
space drops to O(1).

Each iteration eliminates one element permanently. If `numbers[l] + numbers[r]`
is too large, then `numbers[r]` paired with *any* remaining element is also too
large — every candidate on the left is ≤ `numbers[l]`. So `r` can be discarded
outright rather than tested against the rest. That is why the pointers never
need to back up, and why the whole scan is O(n) rather than O(n²).

> [!tip] The 1-indexed return
> `return [l + 1, r + 1]` is the trap on this problem — it is the one thing
> that differs from every other two-sum variant, and it is easy to lose a
> submission to. You got it right first time.

> [!warning] `while True` is load-bearing on a guarantee
> The loop has no exit condition of its own; it terminates only because the
> problem promises a solution exists. Without that promise the pointers cross
> and `numbers[r]` starts indexing with a negative `r` — which Python happily
> wraps to the end of the array rather than raising — so the loop could spin or
> return nonsense instead of failing loudly.
>
> `while l < r:` is the version that stands on its own, and it makes the
> trailing `return []` reachable instead of dead code. Same complexity, no
> reliance on the constraint.

## Template

Converging pointers on a sorted array — reach for this whenever the input is
sorted and you are looking for a pair:

```python
l, r = 0, len(a) - 1
while l < r:
    s = a[l] + a[r]
    if s == target:
        return [l, r]
    elif s > target:
        r -= 1
    else:
        l += 1
```

## Mistakes I made

Took a hint. Worth being precise about what the hint was actually for, because
the gap is a useful one to name: the two-pointer mechanics were not the hard
part — the hard part was noticing that *sorted* is a signal, not just a
property of the input.

The general lesson: when a problem hands you a sorted array and forbids extra
space, converging pointers is almost always the intended shape. The sortedness
is the hint.

## Related

- [[Career/Prep/problems/Arrays & Hashing/1 · Two Sum|1 · Two Sum]] — the unsorted version, which needs O(n) space precisely because it lacks this one
- [[Career/Prep/problems/Two Pointers/125 · Valid Palindrome|125 · Valid Palindrome]] — the same converging-pointer skeleton, with a skip condition instead of a sum comparison
