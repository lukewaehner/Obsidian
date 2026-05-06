## Key Difference from Singly Linked List

Each node has **two pointers** instead of one:
- `next` - points to the next node
- `prev` - points to the previous node

```python
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
```

## Unique Advantages

1. **Bidirectional Traversal** - Can traverse forward AND backward
2. **O(1) Deletion with Node Reference** - Can delete a node when given only that node (no need to find previous)
3. **O(1) Insert Before** - Can insert before a given node efficiently
4. **O(1) Pop Back** - Can remove from tail without traversing entire list

## Key Operations That Are Different

### Deletion (Given Node Reference)

**Time: O(1)** - This is the BIG advantage over singly linked lists!

```python
def delete_node(self, node):
    # Handle edge cases
    if node.prev:
        node.prev.next = node.next
    else:
        self.head = node.next  # Deleting head
    
    if node.next:
        node.next.prev = node.prev
    else:
        self.tail = node.prev  # Deleting tail
```

**Key Pattern**: Update BOTH directions
```python
prev.next = curr.next      # Forward link
curr.next.prev = curr.prev # Backward link
```

### Insert Before a Node

**Time: O(1)** - Easy with prev pointer!

```python
def insert_before(self, node, new_val):
    new_node = Node(new_val)
    new_node.next = node
    new_node.prev = node.prev
    
    if node.prev:
        node.prev.next = new_node
    else:
        self.head = new_node  # Inserting before head
    
    node.prev = new_node
```

### Pop Back (Remove from Tail)

**Time: O(1)** - Just use tail.prev!

```python
def pop_back(self):
    if not self.tail:
        return None
    
    val = self.tail.val
    
    if self.tail.prev:
        self.tail = self.tail.prev
        self.tail.next = None
    else:
        self.head = self.tail = None  # Was only node
    
    return val
```

Compare to singly linked list which needs O(n) traversal to find second-to-last node!

### Reverse Traversal

**Time: O(n)** - Can go backwards easily

```python
def print_reverse(self):
    current = self.tail
    while current:
        print(current.val)
        current = current.prev  # Move backward
```

## Common Gotchas

### 1. Always Update Both Pointers
```python
# WRONG - Only updates one direction
node.next = new_node

# CORRECT - Updates both directions
node.next = new_node
new_node.prev = node
```

### 2. Check Both Head and Tail for Edge Cases
```python
# When deleting
if node.prev is None:  # Deleting head
    self.head = node.next
if node.next is None:  # Deleting tail
    self.tail = node.prev
```

### 3. Order Matters During Insertion
```python
# Set new_node's pointers first
new_node.next = node
new_node.prev = node.prev

# Then update surrounding nodes
if node.prev:
    node.prev.next = new_node
node.prev = new_node
```

## When to Use Doubly Linked List

### Use When:
- Need to traverse in both directions
- Frequent deletions with node reference
- Need O(1) access to both ends (like deque)
- Implementing **LRU Cache** (most common use case!)
- Undo/Redo functionality (navigate history)
- Browser history (back/forward buttons)

### Don't Use When:
- Memory is tight (2 pointers vs 1 = ~50% more overhead)
- Only need forward traversal
- Don't need fast deletion given node reference

## Comparison: Singly vs Doubly

| Operation | Singly | Doubly |
|-----------|--------|--------|
| Memory per node | 1 pointer | 2 pointers |
| Delete given node | O(n) | O(1) |
| Insert before node | O(n) | O(1) |
| Pop back | O(n) | O(1) |
| Reverse traversal | O(n) extra space | O(n) time, O(1) space |
| Cache locality | Better | Worse |

## LRU Cache - Classic Use Case

Doubly linked list + hash map is the standard solution for LRU Cache:

- Hash map: O(1) access to nodes
- Doubly linked list: O(1) move to front/remove from back
- Most recently used = head
- Least recently used = tail

**Why doubly?** Need to remove from middle (given node) and move to front in O(1).

## Quick Reference

```python
# Node structure
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

# Delete pattern (both directions!)
prev.next = curr.next
curr.next.prev = curr.prev

# Insert pattern (order matters!)
new_node.next = node
new_node.prev = node.prev
node.prev.next = new_node  # Update prev's next
node.prev = new_node       # Update node's prev
```

## Related Topics
- [[Linked List]] - Base structure
- [[LRU Cache]] - Primary interview use case
- [[Deque]] - Often implemented with doubly linked list
- [[Hash Table]] - Combined with DLL for LRU Cache