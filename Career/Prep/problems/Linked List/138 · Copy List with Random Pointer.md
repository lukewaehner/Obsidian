---
type: problem
source: neetcode
number: 138
url: https://neetcode.io/problems/copy-linked-list-with-random-pointer
difficulty: Medium
pattern: Linked List
patterns: ["Linked List", "Arrays & Hashing"]
topics: ["[[Career/Prep/topics/Data Structures/Linked Lists|Linked Lists]]", "[[Career/Prep/topics/Data Structures/Hash Tables|Hash Tables]]"]
solved_on: 2026-09-08
attempts: 2
aid: hint
revisit: false
time: O(n)
space: O(n)
language: python
---

# 138 · Copy List with Random Pointer

> [!question]- Problem
> Deep-copy a linked list where each node has a `next` pointer and a `random` pointer that may point at any node in the list, or at `None`.

## Idea

The only hard part is that a `random` may point *forward* at a node you have not
created yet — so create every node first, then wire the pointers in a second pass
using an old-node → new-node map.

## Naive

The same two-pass shape, but routed through integer indices instead of the nodes
themselves:

```python
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        ht = {}
        ht[None] = None
        f = head
        l = 0
        while f:
            ht[l] = (f.val, f.random) # val, r_mem_slot
            f = f.next
            l += 1
        idx_of = {}
        f = head
        j = 0
        while f:
            idx_of[f] = j
            f = f.next
            j += 1

        ht2 = {}
        for j in range(l):
            ht2[j] = Node(ht[j][0])
        ht2[l] = None
        for j in range(l):
            t = ht2[j]
            t.next = ht2[j+1]
            r_val = ht[j][1]
            if r_val == None:
                t.random = ht2[l]
            else:
                t.random = ht2[idx_of[r_val]]
            ht2[j] = t
        return ht2[0]
```

Correct, and the same O(n)/O(n) — but four passes and three dictionaries where
one pass and one dictionary do the job. It also returns `ht2[0]`, which raises
`KeyError` on an empty list, where the optimal version returns `None` naturally.

## Optimal

```python
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        m = { None : None }
        cur = head
        while cur:
            m[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head
        while cur:
            t = m[cur]
            t.next = m[cur.next]
            t.random = m[cur.random]
            cur = cur.next
    
        return m[head]
```

## Why it works

**Why two passes are unavoidable.** A single pass cannot work because `random`
has no ordering guarantee: node 0 may point at node 9, which does not exist yet.
Splitting into *create everything* then *link everything* removes the ordering
problem entirely — by the time any pointer is assigned, every possible target
already exists.

**Why the map is keyed by the node itself.** The naive version builds an
index because it is thinking in positions. But the old node *is* a perfectly good
key — `Node` has no `__hash__` override, so it hashes by identity, which is
exactly the equality the problem cares about ("the same node", not "a node with
the same value"). Keying on the object collapses `idx_of` and both index
dictionaries into one map and makes the second pass a literal transcription of
the structure:

```python
t.next   = m[cur.next]     # copy of whatever the original pointed at
t.random = m[cur.random]
```

**Why `m[None] = None` is the whole trick.** Without it, both lines need a
`None` guard, and the naive version's `if r_val == None` branch is exactly that
guard written out. Seeding the map with the null case makes `None` a legitimate
key that maps to a legitimate value, so the lookup is total and there is no
branch at all. The same seeding is what makes `return m[head]` correct on an
empty list.

> [!tip] The O(1)-extra-space version
> The map can be eliminated by weaving the copies into the original list —
> `A → A' → B → B' → …` — so that `A'` is always `A.next`. Then
> `A'.random = A.random.next`, and a final pass unzips the two lists. Same O(n)
> time, no auxiliary structure, at the cost of mutating the input while it runs.
> Worth knowing it exists; the map version is the one to write under time
> pressure.

## Template

Clone-a-graph in general, of which this is the two-pointer special case:

```python
old_to_new = {None: None}
for node in nodes:              # pass 1: create
    old_to_new[node] = Node(node.val)
for node in nodes:              # pass 2: link
    for ptr in node.edges:
        old_to_new[node].edges.append(old_to_new[ptr])
```

## Mistakes I made

Took a hint, and it was aimed squarely at the first version's detour.

The first version reached for indices because "map the old list to the new one"
sounded like it needed positions. It does not — it needs *identity*, and objects
are hashable by identity for free. Three dictionaries appeared to work around a
key type I already had.

The second lesson is the null seeding. Putting `None` in the map turns a special
case into an ordinary lookup, and that pattern — **seed the sentinel so the
lookup is total** — recurs anywhere a mapping has to survive a missing edge.

## Related

- [[Career/Prep/problems/Linked List/206 · Reverse Linked List|206 · Reverse Linked List]] — the other list problem that turns on not losing a pointer before you have used it
- [[Career/Prep/topics/Data Structures/Hash Tables|Hash Tables]]
