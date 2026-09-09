---
type: problem
source: neetcode
number: 141
url: https://neetcode.io/problems/linked-list-cycle-detection
difficulty: Easy
pattern: Linked List
patterns: ["Linked List", "Two Pointers"]
topics: ["[[Career/Prep/topics/Data Structures/Linked Lists|Linked Lists]]"]
solved_on: 2026-09-08
attempts: 1
aid: unaided
revisit: false
time: O(n)
space: O(1)
language: python
---

# 141 · Linked List Cycle

> [!question]- Problem
> Return whether a linked list contains a cycle.

## Idea

Two runners on a circular track always meet; two runners on a straight one never
do — so run one pointer at twice the speed of the other and see whether they
collide.

## Optimal

```python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False


        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
```

## Why it works

**Why they must meet.** Once both pointers are inside a cycle of length `C`, look
at the gap from `fast` to `slow` measured forward around the cycle. Each step
`fast` advances 2 and `slow` advances 1, so that gap shrinks by exactly 1 per
step. It cannot skip past zero — it decreases one at a time — so within at most
`C` steps it is zero and the pointers are on the same node. This is why the
"fast might hop over slow" worry is unfounded, and it is *specific to the step
sizes*: with speeds 3 and 1 the gap shrinks by 2 and can jump from 1 to −1
without ever being 0.

**Why the loop condition is what it is.** `fast` is the only pointer that can run
off the end, and it dereferences two links per step, so both must exist:

- `fast` — needed before reading `fast.next`.
- `fast.next` — needed before reading `fast.next.next`.

`slow` never needs a guard, because it is always at or behind `fast`. Exiting the
loop means `fast` hit the end, which means there is no cycle.

The time bound is O(n): with no cycle, `fast` reaches the end in n/2 steps; with
one, `slow` needs at most n steps to enter the cycle and at most `C` more to be
caught.

> [!tip] The `if not head` guard is redundant
> `while fast and fast.next` already handles `head is None` — the loop body never
> runs and the function returns `False`. The guard is harmless, but it is a second
> place where emptiness is decided, and the same instinct produced the extra exit
> path in [[Career/Prep/problems/Linked List/206 · Reverse Linked List|206]].
> Let the loop condition own that question.

> [!tip] `slow == fast` vs `slow is fast`
> `ListNode` defines no `__eq__`, so `==` falls through to identity and this is
> correct as written. It is comparing *nodes*, not values, though — and if the
> node class ever grew a value-based `__eq__`, `==` would report a cycle for two
> distinct nodes holding the same number. `is` says what is meant.

## Template

Floyd's cycle detection, phase one:

```python
slow = fast = head
while fast and fast.next:
    slow, fast = slow.next, fast.next.next
    if slow is fast:
        return True
return False
```

## Related

- [[Career/Prep/problems/Linked List/287 · Find the Duplicate Number|287 · Find the Duplicate Number]] — the same runners, plus phase two to locate where the cycle begins
- [[Career/Prep/problems/Linked List/143 · Reorder List|143 · Reorder List]] — slow/fast used to find the midpoint rather than a cycle
