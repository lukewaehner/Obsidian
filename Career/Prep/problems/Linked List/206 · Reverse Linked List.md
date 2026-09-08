---
type: problem
source: neetcode
number: 206
url: https://neetcode.io/problems/reverse-a-linked-list
difficulty: Easy
pattern: Linked List
patterns: ["Linked List"]
topics: ["[[Career/Prep/topics/Data Structures/Linked Lists|Linked Lists]]"]
solved_on: 2026-09-07
attempts: 1
aid: unaided
revisit: false
time: O(n)
space: O(1)
language: python
---

# 206 · Reverse Linked List

> [!question]- Problem
> Reverse a singly linked list and return the new head.

## Idea

Walk the list flipping each `next` pointer backwards, carrying the node behind
you — the only thing you must not lose is the node ahead, so save it first.

## Naive

The first pass. Correct, but it stops one node early and then patches up:

```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        prev = None
        curr = head
        while curr and curr.next is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        curr.next = prev
        return curr
```

## Optimal

```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
```

## Why it works

The loop body is four lines that must happen in exactly this order, and the
order is the whole problem:

```python
next = curr.next     # 1. save the rest of the list
curr.next = prev     # 2. flip this node's pointer backwards
prev = curr          # 3. this node becomes the new "behind"
curr = next          # 4. advance
```

Step 2 destroys `curr.next`. If step 1 has not already saved it, the remainder
of the list is unreachable — there is no back pointer to recover it from, so the
rest of the list is simply gone. That is the single mistake this problem exists
to teach, and the reason the temporary is not optional.

The invariant: at the top of every iteration, `prev` heads the reversed prefix
and `curr` heads the untouched suffix. The loop ends when `curr` is `None`,
which means the suffix is empty and `prev` heads the whole reversed list — which
is why the return is `prev` and not `curr`. Each node is visited once: O(n) time,
O(1) space, three pointers regardless of length.

**Why the first version needed the patch.** Guarding on `curr and curr.next is
not None` exits one node early, with `curr` still pointing at the final node and
its pointer not yet flipped — hence the trailing `curr.next = prev` and
`return curr`. It is correct, including on the empty and single-node inputs, but
it carries a redundant guard, a special case, and two exit paths to reason about
instead of none. Looping while `curr` alone handles every case uniformly: an
empty list never enters the loop and returns `prev`, which is already `None`.
Same complexity, strictly less to get wrong.

> [!tip] `next` shadows the builtin
> Inside this method it is harmless — nothing here calls `next()`. It is still
> worth breaking the habit before it lands in a function that iterates a
> generator, where the shadow turns into a `TypeError` far from its cause.
> `nxt` is the conventional spelling.

## Template

The three-pointer reversal, worth having in muscle memory — it is the inner loop
of half the linked list problems:

```python
prev, curr = None, head
while curr:
    nxt = curr.next
    curr.next = prev
    prev = curr
    curr = nxt
return prev
```

## Mistakes I made

Nothing wrong in the result — both submissions pass — but the first one
approached the loop bound defensively, guarding against a `None` dereference
that the simpler condition makes impossible. The lesson is about where to put
the check: `while curr` puts the emptiness test in one place and lets the
initial `prev = None` do the work that the special case was doing by hand.

## Related

- [[Career/Prep/problems/Linked List/21 · Merge Two Sorted Lists|21 · Merge Two Sorted Lists]] — the same pointer-rewiring discipline, splicing two lists instead of flipping one
- [[Career/Prep/topics/Data Structures/Linked Lists|Linked Lists]]
