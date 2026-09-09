---
type: problem
source: neetcode
number: 143
url: https://neetcode.io/problems/reorder-linked-list
difficulty: Medium
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

# 143 · Reorder List

> [!question]- Problem
> Reorder `L0 → L1 → … → Ln` in place as `L0 → Ln → L1 → Ln-1 → …`.

## Idea

The target order alternates between walking forward from the head and backwards
from the tail — so reverse the back half and the whole thing becomes a plain
forward zip of two lists.

## Optimal

```python
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # Two halves of the LL are rendered with the start being the slow pointer
        second = slow.next
        prev = slow.next = None
        
        # reverse second half of the list
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge two halfs
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
```

## Why it works

A singly linked list cannot be walked backwards, so "take from the end" is not an
operation that exists. Three standard pieces manufacture it.

**Find the midpoint.** `slow` advances one, `fast` two, so `slow` is at the middle
when `fast` reaches the end. The initialisation `fast = head.next` — rather than
`fast = head` — is deliberate: it biases `slow` to the *end of the first half*, so
on an even-length list the split is `[1,2] [3,4]` rather than `[1] [2,3,4]`. That
matters because the zip below stops when the second half runs out, and it needs
the second half to be no longer than the first.

**Cut and reverse.**

```python
second = slow.next
prev = slow.next = None
```

The chained assignment does two things at once: it severs the first half's tail
(so it terminates) and seeds `prev` for the reversal. Order matters — `second` is
captured before `slow.next` is cleared, or the back half would be unreachable.
The loop that follows is the three-pointer reversal from
[[Career/Prep/problems/Linked List/206 · Reverse Linked List|206]], leaving `prev`
at the head of the reversed second half.

**Zip.** Both temporaries are saved before either pointer is overwritten, for the
same reason the reversal needs its temporary — the writes destroy the links being
walked:

```python
tmp1, tmp2 = first.next, second.next   # save both futures
first.next = second                    # then rewire
second.next = tmp1
```

Looping `while second` is the right guard: with the biased midpoint the second
half is the shorter or equal one, so it exhausts first, and the first half's tail
already points at the correct final node. Guarding on `first` instead would run
one step too far and close a cycle.

O(n) — three linear passes — and O(1) space, which is what forces the
reverse-and-zip approach over the obvious one of dumping the nodes into an array
and indexing from both ends.

> [!tip] `head.next` on an empty list
> The very first line dereferences `head` unguarded, so `reorderList(None)` raises
> `AttributeError`. The constraints guarantee at least one node, so it never
> fires; `if not head: return` closes it. Single- and two-node lists are already
> handled — the loop simply does not run.

## Template

The three-move shape for any "combine the list with its own reverse" problem —
also how you test a list for palindromicity in O(1) space:

```python
# 1. midpoint via slow/fast
# 2. cut, reverse the second half
# 3. walk both halves inward together
```

## Related

- [[Career/Prep/problems/Linked List/206 · Reverse Linked List|206 · Reverse Linked List]] — step two, in isolation
- [[Career/Prep/problems/Linked List/141 · Linked List Cycle|141 · Linked List Cycle]] — the same slow/fast pair asking a different question
