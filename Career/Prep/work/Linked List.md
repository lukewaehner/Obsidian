## What is a Linked List?

A **linked list** is a linear data structure where elements (nodes) are stored in non-contiguous memory locations. Each node contains:
- **Data**: The value stored in the node
- **Pointer/Reference**: A link to the next node in the sequence

Unlike arrays, linked lists don't require contiguous memory allocation, making them more flexible for dynamic memory management.

## Types of Linked Lists

### 1. Singly Linked List
- Each node points only to the next node
- Traversal is unidirectional (forward only)
- Last node points to `null`

### 2. Doubly Linked List
- Each node has pointers to both next and previous nodes
- Traversal is bidirectional
- More memory overhead but easier backward traversal

### 3. Circular Linked List
- Last node points back to the first node (forms a circle)
- No `null` terminator
- Useful for round-robin scheduling and circular buffers
- **Implementation below uses this variant**

## When to Use Linked Lists

### Use Linked Lists When:
- Frequent insertions/deletions at the beginning or middle
- Size is unknown or changes frequently
- Don't need random access to elements
- Memory is fragmented (can't allocate large contiguous block)
- Implementing other data structures (stacks, queues, graphs)

### Don't Use Linked Lists When:
- Need fast random access by index (O(n) vs O(1) for arrays)
- Memory is limited (extra memory for pointers)
- Need cache-friendly sequential access (arrays are better)
- Searching is frequent (O(n) linear search required)

## Common Problem Patterns

Look for linked lists when you see:
- "Insert/delete at position"
- "Reverse a sequence"
- "Detect cycles"
- "Find middle element"
- "Merge sorted sequences"
- "Remove duplicates"
- "Reorder/rearrange elements"
- LRU Cache implementation
- Undo/Redo functionality

## Linked List Operations

### Core Operations

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Access by index | O(n) | O(1) |
| Search | O(n) | O(1) |
| Insert at head | O(1) | O(1) |
| Insert at tail | O(1)* | O(1) |
| Insert at position | O(n) | O(1) |
| Delete at head | O(1) | O(1) |
| Delete at tail | O(n)** | O(1) |
| Delete at position | O(n) | O(1) |

*O(1) only if you maintain a tail pointer
**O(n) for singly linked list, O(1) for doubly linked list

## Method Implementations & Explanations

### 1. Append (Add to End)

**Time Complexity**: O(1)  
**Space Complexity**: O(1)

```python
def append(self, data):
    if self.head is None:
        self.head = self.tail = linkedlist.Node(data)
    else:
        new_node = linkedlist.Node(data)
        self.tail.next = new_node
        self.tail = new_node
        self.tail.next = self.head  # Circular link
```

**Explanation**: Adds element to end of list. With tail pointer, this is O(1). In circular variant, the new tail points back to head to maintain the circle.

---

### 2. Push Front (Add to Beginning)

**Time Complexity**: O(1)  
**Space Complexity**: O(1)

```python
def push_front(self, data):
    new_node = linkedlist.Node(data)
    new_node.next = self.head
    self.head = new_node
    self.tail.next = self.head  # Update circular link
```

**Explanation**: Adds element to beginning. Update head pointer and maintain circular link from tail.

---

### 3. Insert at Index

**Time Complexity**: O(n)  
**Space Complexity**: O(1)

```python
def insert(self, index: int, data):
    if index > self.size() or index < 0:
        return
    if self.head is None or index == self.size():
        self.append(data)
        return
    if index == 0:
        self.push_front(data)
        return
    current = self.head
    for _ in range(index - 1):
        current = current.next
    new_node = linkedlist.Node(data)
    new_node.next = current.next
    current.next = new_node
```

**Explanation**: Traverse to index-1 position, then insert new node by updating pointers. Must traverse up to index position (O(n)).

---

### 4. Remove at Index

**Time Complexity**: O(n)  
**Space Complexity**: O(1)

```python
def remove(self, index: int):
    if index >= self.size() or index < 0 or self.head is None:
        return
    if index == 0:
        self.pop_front()
        return
    current = self.head
    for _ in range(index - 1):
        current = current.next
    current.next = current.next.next  # Skip over node to remove
```

**Explanation**: Traverse to node before target, update its next pointer to skip the node being removed.

---

### 5. Pop Front (Remove from Beginning)

**Time Complexity**: O(1)  
**Space Complexity**: O(1)

```python
def pop_front(self):
    if self.head is None:
        return None
    self.head = self.head.next
    self.tail.next = self.head  # Maintain circular link
```

**Explanation**: Simply move head pointer forward. Update tail's circular link to maintain structure.

---

### 6. Pop Back (Remove from End)

**Time Complexity**: O(n)  
**Space Complexity**: O(1)

```python
def pop_back(self):
    current = self.head
    
    if self.head == self.tail:
        self.head = self.tail = None
        return
    
    while current.next != self.tail:
        current = current.next
    
    current.next = self.head  # New tail points to head
```

**Explanation**: Must traverse entire list to find second-to-last node. This is why doubly linked lists are better if you need frequent tail deletions.

---

### 7. Reverse

**Time Complexity**: O(n)  
**Space Complexity**: O(1)

```python
def reverse(self):
    if not self.head or self.head.next is self.head:
        return
    prev = self.tail  # Start "behind" head to preserve ring
    curr = self.head
    while True:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
        if curr is self.head:
            break
    # Swap head/tail
    self.tail = self.head
    self.head = prev
```

**Explanation**: Reverse pointer direction of each node. For circular list, must carefully handle the loop condition and swap head/tail at the end.

**Key Pattern**: Three-pointer technique (prev, curr, next) is standard for reversing linked lists.

---

### 8. Search/Access by Index

**Time Complexity**: O(n)  
**Space Complexity**: O(1)

```python
def value_at(self, index: int):
    if index > self.size() - 1 or index < 0:
        return None
    
    current = self.head
    for _ in range(index):
        current = current.next
    return current.data
```

**Explanation**: No random access - must traverse from head to reach target index. This is the main disadvantage vs arrays.

---

### 9. Find Nth from End

**Time Complexity**: O(n)  
**Space Complexity**: O(1)

```python
def value_n_from_end(self, n: int):
    current = self.head
    for _ in range(self.size() - n - 1):
        current = current.next
    return current.data
```

**Explanation**: Calculate position from start as (size - n - 1), then traverse.

**Better approach** (two-pointer technique): Use two pointers n nodes apart, advance both until first reaches end.

---

### 10. Remove by Value

**Time Complexity**: O(n)  
**Space Complexity**: O(1)

```python
def remove_value(self, value):
    if self.head is None:
        return
    if self.head.data == value:
        self.pop_front()
        return
    current = self.head
    while current.next != self.head:
        if current.next.data == value:
            current.next = current.next.next
            return
        current = current.next
```

**Explanation**: Search for node with matching value while keeping track of previous node to update pointers.

---

### 11. Size

**Time Complexity**: O(n)  
**Space Complexity**: O(1)

```python
def size(self) -> int:
    i = 0
    current = self.head
    while current is not None:
        i += 1
        current = current.next
        if current == self.head:  # Circular list check
            break
    return i
```

**Explanation**: Must count nodes by traversal. **Optimization**: Maintain a size counter variable and update on insert/delete for O(1) size queries.

---

## Classic Interview Problems

### Two-Pointer Technique
- **Fast & Slow Pointers**: Detect cycles (Floyd's algorithm)
- **Nth from End**: Place pointers n nodes apart
- **Middle Element**: Fast pointer moves 2x speed of slow

### Common Challenges
1. **Reverse Linked List** - Practice the 3-pointer technique
2. **Detect Cycle** - Floyd's cycle detection (tortoise & hare)
3. **Merge Two Sorted Lists** - Maintain pointers for both lists
4. **Remove Nth Node from End** - Two-pointer with gap of n
5. **Palindrome Check** - Find middle, reverse second half, compare
6. **Intersection of Two Lists** - Align lengths, then traverse together

### Edge Cases to Test
- Empty list (`head == None`)
- Single node list
- Operations at boundaries (index 0, last index)
- Circular list termination (avoid infinite loops)
- Null pointer dereferences

## Implementation Comparison

### Array vs Linked List

| Feature | Array | Linked List |
|---------|-------|-------------|
| Memory | Contiguous | Non-contiguous |
| Access Time | O(1) | O(n) |
| Insert/Delete (beginning) | O(n) | O(1) |
| Insert/Delete (middle) | O(n) | O(n)* |
| Cache Performance | Excellent | Poor |
| Memory Overhead | None | Pointer per node |
| Fixed Size | Yes (static) | No |

*O(n) to find position, O(1) to update pointers

## Full Implementation

```python
# pyright: reportOptionalMemberAccess=false
from __future__ import annotations

from typing import Any, Optional


class linkedlist:
    class Node:
        def __init__(self, data: Any):
            self.data: Any = data
            self.next: Optional["linkedlist.Node"] = None

    def __init__(self):
        self.head: Optional[linkedlist.Node] = None
        self.tail: Optional[linkedlist.Node] = None

    def append(self, data):
        if self.head is None:
            self.head = self.tail = linkedlist.Node(data)
        else:
            new_node = linkedlist.Node(data)
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head

    def empty(self) -> bool:
        return self.head is None

    # Returns the value at the given index
    def value_at(self, index: int):
        if index > self.size() - 1 or index < 0:
            return None

        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

    def front(self):
        return self.head.data if self.head is not None else None

    def back(self):
        return self.tail.data if self.tail is not None else None

    def insert(self, index: int, data):
        if index > self.size() or index < 0:
            return
        if self.head is None or index == self.size():
            self.append(data)
            return
        if index == 0:
            self.push_front(data)
            return
        current = self.head
        for _ in range(index - 1):
            current = current.next
        new_node = linkedlist.Node(data)
        new_node.next = current.next
        current.next = new_node

    def remove(self, index: int):
        if index >= self.size() or index < 0 or self.head is None:
            return
        if index == 0:
            self.pop_front()
            return
        current = self.head
        for _ in range(index - 1):
            current = current.next
        current.next = current.next.next

    # Returns number of elements in the list
    def size(self) -> int:
        i = 0
        current = self.head
        while current is not None:
            i += 1
            current = current.next
            if current == self.head:
                break
        return i

    def display(self):
        current = self.head
        while current is not None:
            print(current.data)
            if current.next == self.head:
                break
            current = current.next

    def clear(self):
        self.head = self.tail = None

    def push_front(self, data):
        new_node = linkedlist.Node(data)
        new_node.next = self.head
        self.head = new_node
        self.tail.next = self.head

    def pop_front(self):
        if self.head is None:
            return None
        self.head = self.head.next
        self.tail.next = self.head

    def pop_back(self):
        current = self.head

        if self.head == self.tail:
            self.head = self.tail = None
            return

        while current.next != self.tail:
            current = current.next

        current.next = self.head

    def value_n_from_end(self, n: int):
        current = self.head
        for _ in range(self.size() - n - 1):
            current = current.next
        return current.data

    def reverse(self):
        if not self.head or self.head.next is self.head:
            return
        prev = self.tail  # start "behind" head to preserve the ring
        curr = self.head
        while True:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            if curr is self.head:
                break
        # swap head/tail
        self.tail = self.head
        self.head = prev

    def remove_value(self, value):
        # empty list
        if self.head is None:
            return
        # only one element and it is the value, clear the list
        if self.head.data == value:
            self.pop_front()
            return
        current = self.head
        # loop entire list
        while current.next != self.head:
            # if the next node is the value, take it out of the chain
            if current.next.data == value:
                current.next = current.next.next
                return
            # iterate
            current = current.next


def test():
    ll = linkedlist()
    ll.append(1)
    ll.append(2)
    ll.display()
    print(f"Size: {ll.size()}")
    llempty = linkedlist()
    print(f"Is empty: {llempty.empty()}")
    ll.append(3)
    print(f"Should be 3: {ll.value_at(2)}")
    ll.push_front(999)
    print(f"Pushed 999 to front, head.data is: {ll.head.data}")
    ll.pop_front()
    print(f"Popped the front, should be 1: {ll.head.data}")
    ll.append(999)
    print(
        f"Appended 999, the value at the array size is: {ll.value_at(ll.size() - 1)}"
    )
    ll.insert(3, 998)
    print(f"Inserted 998 at index 3, value at index 3 is: {ll.value_at(3)}")
    ll.remove(0)
    print(f"Removed index 0 new head is: {ll.front()}")


def testRev():
    l = linkedlist()
    l.append(1)
    l.append(2)
    l.append(3)
    l.reverse()
    l.display()


testRev()
```

## Key Takeaways

1. **Strengths**: Dynamic size, O(1) insertions/deletions at known positions
2. **Weaknesses**: No random access, extra memory for pointers, poor cache locality
3. **Master These**: Reversing, two-pointer techniques, cycle detection
4. **Interview Tip**: Always clarify if singly/doubly/circular linked list
5. **Common Bug**: Forgetting to update head/tail pointers or breaking circular links

## Related Topics
- [[Career/Prep/work/Doubly Linked List|Doubly Linked List]]
- [[Career/Prep/work/Stack|Stack]] - Often implemented with linked lists
- [[Career/Prep/work/Queue|Queue]] - Often implemented with linked lists
- [[Career/Prep/work/Hashtable|Hash Table]] - Collision handling with chaining uses linked lists
- [[LRU Cache]] - Combines hash map + doubly linked list