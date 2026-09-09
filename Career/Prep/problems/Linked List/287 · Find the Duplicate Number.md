---
type: problem
source: neetcode
number: 287
url: https://neetcode.io/problems/find-duplicate-integer
difficulty: Medium
pattern: Linked List
patterns: ["Linked List", "Two Pointers", "Binary Search"]
topics: ["[[Career/Prep/topics/Data Structures/Linked Lists|Linked Lists]]", "[[Career/Prep/topics/Data Structures/Arrays|Arrays]]"]
solved_on: 2026-09-08
attempts: 2
aid: hint
revisit: false
time: O(n)
space: O(1)
language: python
---

# 287 · Find the Duplicate Number

> [!question]- Problem
> An array of `n + 1` integers holds values in `[1, n]`. Exactly one value repeats. Find it without modifying the array and using O(1) extra space.

## Idea

Read `i → nums[i]` as a linked list; because `n + 1` slots hold only `n` distinct
values, two indices point at the same successor, and that shared successor is the
entry node of a cycle — so this is Floyd's cycle detection wearing an array.

## Optimal

```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
```

## Why it works

**The reframing.** Define `next(i) = nums[i]`. Every index has exactly one
successor, so the structure is a functional graph — a "linked list" you can walk
without building anything. Two facts make it well-formed:

- Values are in `[1, n]`, so no successor is ever index `0`. Starting at `0`
  guarantees you begin *outside* any cycle, which phase two requires.
- There are `n + 1` indices and `n` possible values, so by pigeonhole some value
  `d` appears twice — two different indices point at `d`. Two in-edges into one
  node is precisely what closes a cycle, and `d` is the node where it closes.

So the duplicate is not merely *inside* the cycle; it is the cycle's **entry
node**. Finding the entry finds the answer.

**Phase one** is [[Career/Prep/problems/Linked List/141 · Linked List Cycle|141]]
verbatim: the gap between the pointers shrinks by one per step, so they meet
somewhere inside the cycle. No guards are needed — a cycle is guaranteed to
exist, so the `while True` always terminates.

**Phase two — why restarting from 0 lands on the entry.** Let `F` be the distance
from the start to the entry node, `C` the cycle length, and `a` the distance from
the entry to the meeting point. When they meet, `slow` has travelled `F + a` and
`fast` has travelled `2(F + a)`; since `fast` is exactly some whole number of
laps ahead, `2(F + a) - (F + a) = F + a` is a multiple of `C`. Therefore
advancing `F` more steps from the meeting point lands on a multiple of `C` from
the entry — that is, back on the entry. And `F` steps from index `0` is also the
entry. So two pointers moving at the *same* speed, one from `0` and one from the
meeting point, collide exactly at the entry.

That is why the second loop moves both by one step, and why the reset is to `0`
rather than to `head`-equivalent anything else.

O(n) time, and the only storage is three integers — which is what the problem's
"no modification, O(1) space" constraint is really testing. Sorting, a hash set,
or negating `nums[abs(x)]` in place each violate one of the two constraints.

> [!tip] The binary-search alternative
> Count how many values are `<= m`. If that count exceeds `m`, the duplicate is
> in `[lo, m]`, else in `[m + 1, hi]` — binary search on the *answer*, not the
> array. O(n log n) time, O(1) space, no cycle theory required, and far easier to
> derive under pressure. Worth having as the fallback.

## Template

Floyd's, both phases:

```python
slow = fast = start
while True:                      # phase 1: find a meeting point
    slow, fast = f(slow), f(f(fast))
    if slow == fast:
        break
slow2 = start                    # phase 2: find the cycle entry
while slow != slow2:
    slow, slow2 = f(slow), f(slow2)
return slow
```

## Mistakes I made

Took a hint, and the hint was the reframing — which is fair, because the
reframing *is* the entire problem and it does not come from staring at the
array. Everything after "this is a linked list" is mechanical.

The trigger to remember: **"O(1) space, do not modify the input, values
are bounded by the index range"** — that combination rules out every counting
approach and is effectively a pointer at `i → nums[i]`.

The second thing worth internalising is *why the duplicate is the entry* rather
than just some node in the cycle. Without that, phase two looks like ceremony;
with it, the algorithm is forced.

## Related

- [[Career/Prep/problems/Linked List/141 · Linked List Cycle|141 · Linked List Cycle]] — phase one on its own, on a real list
- [[Career/Prep/problems/Arrays & Hashing/217 · Contains Duplicate|217 · Contains Duplicate]] — the same question with the space constraint lifted, where a set is the whole answer
