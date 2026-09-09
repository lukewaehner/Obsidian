---
type: problem
source: neetcode
number: 23
url: https://neetcode.io/problems/merge-k-sorted-linked-lists
difficulty: Hard
pattern: Linked List
patterns: ["Linked List", "Heap & Priority Queue"]
topics: ["[[Career/Prep/topics/Data Structures/Linked Lists|Linked Lists]]", "[[Career/Prep/topics/Sorting & Searching/Merge Sort|Merge Sort]]", "[[Career/Prep/topics/Algorithm Design/Divide and Conquer|Divide and Conquer]]"]
solved_on: 2026-09-08
attempts: 3
aid: hint
revisit: false
time: O(N log k) for N total nodes across k lists
space: O(1) extra
language: python
---

# 23 · Merge k Sorted Lists

> [!question]- Problem
> Merge `k` sorted linked lists into one sorted list.

## Idea

Merging two lists is already solved, so merge them in pairs and halve `k` each
round — the bottom-up half of merge sort, with the lists as the pre-sorted runs.

## Optimal

```python
class Solution:
    def mergeList(self, l1, l2):
        d = n = ListNode()
        while l1 and l2:
            if l1.val < l2.val:
                n.next = l1
                l1 = l1.next
            else:
                n.next = l2
                l2 = l2.next
            n = n.next 
        n.next = l1 or l2
        return d.next



    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        gap = 1
        while gap < len(lists):
            for i in range(0, len(lists), 2*gap):
                if i + gap < len(lists):
                    lists[i] = self.mergeList(lists[i], lists[i+gap])
            gap = gap * 2
        return lists[0]
```

## Why it works

**Why pairing beats folding.** The obvious approach — merge list 0 into an
accumulator, then list 1, then list 2 — re-walks the growing accumulator every
time. The first list's nodes are traversed `k` times, giving O(Nk). Pairing
instead means every node is touched once per *round*, and there are only
`log k` rounds, so O(N log k). The work per round is the same; the number of
rounds is what changed.

**How the gap indexing implements that.** `gap` is the distance to the partner
list, doubling each round; `2*gap` is the stride, so each round merges disjoint
pairs and parks every result at the lower index:

```
gap=1:  (0,1) (2,3) (4,5) (6,7)   ->  results at 0, 2, 4, 6
gap=2:  (0,2) (4,6)               ->  results at 0, 4
gap=4:  (0,4)                     ->  result at 0
```

Everything ends up funnelled into `lists[0]`, which is why that is the return.

**The `i + gap < len(lists)` guard** is what handles an odd count. A list with no
partner this round is simply left where it is and picked up in a later round,
which is exactly right — it is already sorted, so it needs no work until someone
can be merged with it. Merging into the array in place is also what keeps the
extra space at O(1): no queue of pending lists, no recursion stack.

**Inside `mergeList`**, `n.next = l1 or l2` is the tail splice. When one list is
exhausted the other is already sorted and already linked, so the entire remainder
attaches with a single pointer write — no loop. Python's `or` returns the first
truthy operand, so this yields whichever list is non-empty, or `None` if both are.
Note `l1.val < l2.val` takes from `l2` on ties, which is fine here; `<=` would
make the merge stable, which matters when the payload carries more than a value.

> [!tip] The heap alternative
> Push the head of every list into a min-heap, pop the smallest, push its
> successor. Also O(N log k) — `log k` per node instead of `log k` passes over
> everything — and it is the version that generalises to *streaming* inputs whose
> total size is unknown. It needs O(k) space and, in Python, a tiebreaker in the
> tuple since `ListNode` is not comparable: `heappush(h, (node.val, i, node))`.

## Template

Bottom-up pairwise reduction, useful any time an associative binary merge is
applied to `k` inputs:

```python
gap = 1
while gap < len(items):
    for i in range(0, len(items), 2 * gap):
        if i + gap < len(items):
            items[i] = combine(items[i], items[i + gap])
    gap *= 2
return items[0]
```

## Mistakes I made

The approach was mine — pair up, halve `k`, `log k` rounds — and the reasoning
behind it held up. What I needed help with was the *syntax* of expressing it:
specifically the `range(0, len(lists), 2*gap)` stride and the `i + gap` partner
index, which is a fiddly way to say something simple.

Worth separating those two failures, because they get fixed differently. The
idea is the part that generalises: **when reducing `k` things with a binary
operation whose cost scales with the size of its operands, folding left is O(k)
rounds over a growing accumulator; pairing is O(log k) rounds over the same
total.** Same operation, different tree shape. The stride arithmetic is just
practice — and if it will not come, the recursive form says the same thing with
no index juggling at all:

```python
def merge_all(lists):
    if len(lists) <= 1:
        return lists[0] if lists else None
    mid = len(lists) // 2
    return self.mergeList(merge_all(lists[:mid]), merge_all(lists[mid:]))
```

Same O(N log k), O(log k) stack instead of O(1). Reach for it when the in-place
gap version will not come out cleanly.

## Related

- [[Career/Prep/problems/Linked List/21 · Merge Two Sorted Lists|21 · Merge Two Sorted Lists]] — the `mergeList` helper, on its own
- [[Career/Prep/topics/Sorting & Searching/Merge Sort|Merge Sort]] — this is its merge phase with the recursion unrolled
