---
type: problem
source: neetcode
number: 21
url: https://neetcode.io/problems/merge-two-sorted-linked-lists
difficulty: Easy
pattern: Linked List
patterns: ["Linked List", "Two Pointers"]
topics: ["[[Career/Prep/topics/Data Structures/Linked Lists|Linked Lists]]", "[[Career/Prep/topics/Sorting & Searching/Merge Sort|Merge Sort]]"]
solved_on: 2026-09-07
attempts: 1
aid: unaided
revisit: false
time: O(n + m)
space: O(1)
language: python
---

# 21 · Merge Two Sorted Lists

> [!question]- Problem
> Given the heads of two sorted linked lists, splice them into one sorted list
> and return its head.

## Idea

Repeatedly take the smaller of the two front nodes — and because these are
nodes, not values, "take" is a pointer assignment rather than a copy.

## Optimal

```python
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        d = n = ListNode()
        
        # with two full lists, start merging
        while list1 and list2:
            if list1.val < list2.val:
                # append l1's val
                n.next = list1
                # move l1
                list1 = list1.next
            else:
                # append l2's val
                n.next = list2
                # move l2
                list2 = list2.next
            # move the merged list
            n = n.next
        # append a non-flushed list (or if only given one valid list)
        n.next = list1 or list2
        # move to the head of the merged list (or nothing if both l1 and l2 empty)
        return d.next
```

## Why it works

This is the merge step of [[Career/Prep/topics/Sorting & Searching/Merge Sort|merge sort]],
and on linked lists it is strictly nicer than on arrays: there is no output
buffer to allocate, because merging is just re-pointing nodes that already
exist. Hence O(1) extra space rather than the O(n + m) an array merge pays.

**The dummy head is the trick, and it is worth naming.** `d = n = ListNode()`
makes two names for one throwaway node: `d` stays pinned to it, `n` walks
forward as the tail of the result. Without it, the first append is a special
case — you would need an `if result is None` branch on every iteration, or a
pre-loop comparison to pick the starting head. The dummy absorbs that entirely,
so the loop body is uniform from the first node, and `d.next` at the end is the
real head. The same one-line pattern also handles the both-lists-empty input,
where `d.next` is never assigned and stays `None`.

**`n.next = list1 or list2` is the whole tail case.** The loop stops as soon as
either list runs out, leaving the other with an arbitrary number of nodes still
attached — but they are already sorted and already all greater than everything
emitted, so they can be spliced on wholesale in one assignment. No second loop.
Python's `or` returns the first truthy operand, so this reads as "whichever is
left, or `None` if neither", which is exactly the required semantics. This also
covers being handed one empty list to start with: the loop never runs and the
non-empty list is returned intact.

Every iteration consumes exactly one node from one list, so the loop runs at most
`n + m` times — linear, with no node visited twice.

> [!tip] `<` versus `<=` decides stability, not correctness
> On a tie the `else` branch takes from `list2`, so equal values come out
> `list2`-first. The merged order is still sorted either way, so the problem
> does not care. It matters the moment this merge is the inner step of a sort
> that is expected to be stable — `<=`, taking from `list1` on ties, is the
> spelling that preserves the original relative order.

## Template

Dummy head plus a walking tail — the shape for any problem that builds a linked
list rather than mutating one in place:

```python
dummy = tail = ListNode()
while a and b:
    if a.val <= b.val:
        tail.next, a = a, a.next
    else:
        tail.next, b = b, b.next
    tail = tail.next
tail.next = a or b
return dummy.next
```

## Related

- [[Career/Prep/problems/Linked List/206 · Reverse Linked List|206 · Reverse Linked List]] — the other half of the pointer-rewiring vocabulary
- [[Career/Prep/topics/Sorting & Searching/Merge Sort|Merge Sort]] — this is its merge step, with the output buffer replaced by pointer surgery
- [[Career/Prep/topics/Data Structures/Linked Lists|Linked Lists]]
