---
type: problem
source: neetcode
number: 146
url: https://neetcode.io/problems/lru-cache
difficulty: Medium
pattern: Linked List
patterns: ["Linked List", "Arrays & Hashing"]
topics: ["[[Career/Prep/topics/Data Structures/LRU Cache|LRU Cache]]", "[[Career/Prep/topics/Data Structures/Linked Lists|Linked Lists]]", "[[Career/Prep/topics/Data Structures/Hash Tables|Hash Tables]]", "[[Career/Prep/topics/Systems/Caches|Caches]]"]
solved_on: 2026-09-08
attempts: 2
aid: solution
revisit: false
time: O(1) for both get and put
space: O(capacity)
language: python
---

# 146 · LRU Cache

> [!question]- Problem
> Implement a cache with a fixed capacity supporting `get` and `put` in O(1) average time, evicting the least recently used key when full.

## Idea

A hash map gives O(1) *lookup* but no order; a doubly linked list gives O(1)
*reordering* but no lookup — so run both, with the map storing the node rather
than the value.

## Optimal

```python
class Node:
    def __init__(self, key: int = 0, value: int = 0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key -> Node
        self.head = Node() # dummy start
        self.tail = Node() # dummy end
        self.head.next = self.tail # start links
        self.tail.prev = self.head
    
    def _remove(self, node: Node):
        # take the node out of the list
        prev_node = node.prev 
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _append(self, node: Node):
        # add the node to the end of the list
        prev_tail = self.tail.prev # grab the real last node from the sentinel

        # append through
        prev_tail.next = node
        node.prev = prev_tail
        # update to link back to sentinel
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        # grab the node from cache, remove, and append to its recent
        node = self.cache[key]
        self._remove(node)
        self._append(node)

        return node.value
        

    def put(self, key: int, value: int) -> None:
        # update node in cache
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            # refresh usage
            self._remove(node)
            self._append(node)
        else:
            # spawn a new node
            new = Node(key, value)
            # evict if needed
            if len(self.cache) >= self.capacity:
                lru_n = self.head.next
                self._remove(lru_n)
                del self.cache[lru_n.key]
            # add to cache with proper space already configured
            self.cache[key] = new
            self._append(new)
```

## Why it works

Neither structure alone can do it, and the reason is worth stating precisely:

- A hash map alone finds a key in O(1) but has no notion of "oldest", so eviction
  is an O(n) scan.
- An ordered list alone knows the oldest in O(1) but finding a key is an O(n)
  walk.

Composing them means every operation touches both, and each touch is O(1).

**Why doubly linked, and why `key` lives in the node.** Removal from the middle
requires splicing `prev` and `next` together, which needs a back pointer — a
singly linked list would force an O(n) search for the predecessor. And eviction
finds the node *first*, then has to delete the corresponding map entry; without
`node.key` there is no way back from node to key, and the map could not be
cleaned up. Those two fields are not decoration — they are what make the
composition work.

**Why two sentinels.** `head` and `tail` are permanent dummies that never hold
data, so `node.prev` and `node.next` are never `None` inside `_remove` and
`_append`. Every empty/single/full-list special case disappears; the four pointer
writes are unconditional. The convention here is *tail side = most recently
used*, so `self.head.next` is always the LRU victim.

**The eviction guard.** `len(self.cache) >= self.capacity` sits inside the `else`
branch only, which is correct: updating an existing key changes no size and must
never evict. Checking before insertion (rather than trimming after) keeps the
cache from ever momentarily exceeding capacity.

Both public methods reduce to the same two-line refresh — `_remove` then
`_append` — which is the operation "mark as most recently used". Factoring it out
is what keeps `get` and `put` readable.

> [!tip] `OrderedDict` in an interview
> `OrderedDict.move_to_end(key)` and `popitem(last=False)` are both O(1) and
> collapse this to about ten lines. Say that you know it, then write the node
> version anyway — the question is asking whether you can build the ordering, not
> whether you can call it.

> [!tip] Capacity zero
> With `capacity = 0`, `put` evicts from an empty list — `self.head.next` is the
> `tail` sentinel — and then stores the new key anyway, leaving a cache of size
> one. The constraints guarantee `capacity >= 1`, so this never fires; a
> `if self.capacity == 0: return` guard closes it if the invariant is ever
> relaxed.

## Template

Hash map to node, plus a sentinel-bounded doubly linked list:

```python
self.head.next, self.tail.prev = self.tail, self.head   # empty list
# most recent at the tail, LRU at self.head.next
```

## Mistakes I made

The one on this list I could not get to unaided — took hints and then a video
walkthrough. Worth being honest about where the wall was, because it was not the
code: both submissions are the same implementation and neither is broken.

The wall was the *composition*. I could see that a map gives O(1) lookup and that
a list gives O(1) reordering, and could not get from there to running both at
once over the same nodes. The move I was missing is that **the map does not store
the value, it stores the node** — that one indirection is what lets a lookup hand
you a position, and everything else follows from it.

Two details only make sense downstream of that, and both are worth re-deriving
rather than memorising:

- **`node.key` exists for eviction, not for `get`.** Eviction finds the victim
  *node* first and must then delete the map entry; without a back-reference there
  is no route from node to key. When two structures index each other, check that
  every traversal you need has a route in both directions.
- **The list must be doubly linked** because removal from the middle needs the
  predecessor, and a singly linked list would make finding it O(n) — which
  destroys the only property the whole design exists to provide.

Flagged for a re-solve from scratch rather than a re-read.

## Related

- [[Career/Prep/problems/Linked List/206 · Reverse Linked List|206 · Reverse Linked List]] — the same pointer discipline, one direction and no sentinels
- [[Career/Prep/topics/Systems/Caches|Caches]] — where the eviction policy this implements actually matters
