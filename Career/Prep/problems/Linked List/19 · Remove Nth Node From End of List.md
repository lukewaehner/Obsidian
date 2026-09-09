---
type: problem
source: neetcode
number: 19
url: https://neetcode.io/problems/remove-node-from-end-of-linked-list
difficulty: Medium
pattern: Linked List
patterns:
  - Linked List
  - Two Pointers
topics:
  - "[[Career/Prep/topics/Data Structures/Linked Lists|Linked Lists]]"
solved_on: 2026-09-08
attempts: 4
aid: unaided
revisit: false
time: O(n), two passes
space: O(1)
language: python
---

# 19 · Remove Nth Node From End of List

> [!question]- Problem
> Remove the `n`-th node from the end of a linked list and return the head.

## Idea

"`n`-th from the end" is just "`length - n`-th from the start" — and the node you
actually need is the one *before* it, which a dummy head makes reachable even when
the target is the head itself.

## Optimal

```python
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
            # generate a sentinel
            dummy = ListNode(0, head)
            l = 0
            f = head
            # find the length of the array
            while f:
                f = f.next
                l += 1
            # start before the array
            prev = dummy
            for _ in range(l - n):
                prev = prev.next
            prev.next = prev.next.next
            # shift into the actual array
            return dummy.next
```

## Why it works

Deleting from a singly linked list means rewiring the node *before* the target,
so the whole problem is locating that predecessor.

**The index arithmetic.** With length `l`, the node `n` from the end sits at
0-based index `l - n`. Its predecessor is at `l - n - 1` — which does not exist
when `n == l`, i.e. when the head itself is being deleted. That off-by-one is the
usual source of a `NoneType` crash here.

**Why the dummy removes it.** Starting `prev` at `dummy` rather than `head`
shifts every position by one, so `l - n` steps from `dummy` land exactly on the
predecessor — and when `n == l` that is `dummy` itself, whose `next` is the head.
The delete becomes unconditional:

```python
prev.next = prev.next.next
```

No branch for "is this the head", and `return dummy.next` reads back the possibly
new head for free. This is the general reason to reach for a sentinel: **it makes
the head an ordinary node.**

Two full passes, O(n) time and O(1) space, which is asymptotically optimal — the
one-pass version below saves a constant factor, not an order.

> [!tip] The one-pass gap version
> Advance a lead pointer `n` steps first, then move both until the lead falls off
> the end. The gap between them is fixed at `n`, so `prev` arrives at the
> predecessor exactly as the lead runs out — the length is never computed, it is
> encoded in the spacing:
>
> ```python
> dummy = ListNode(0, head)
> lead = prev = dummy
> for _ in range(n):
>     lead = lead.next
> while lead.next:
>     lead, prev = lead.next, prev.next
> prev.next = prev.next.next
> return dummy.next
> ```
>
> Same complexity, but it is the version to reach for when the input is a stream
> you only get to walk once — and it is what the interviewer is usually fishing
> for after the two-pass answer.

## Template

Sentinel head whenever a deletion or insertion might touch the first node:

```python
dummy = ListNode(0, head)
# ... operate, treating dummy as the node before the head ...
return dummy.next
```

## Related

- [[Career/Prep/problems/Linked List/141 · Linked List Cycle|141 · Linked List Cycle]] — two pointers again, separated by speed rather than by a fixed gap
- [[Career/Prep/problems/Linked List/2 · Add Two Numbers|2 · Add Two Numbers]] — the dummy head used for construction instead of deletion
