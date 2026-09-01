A queue is a linear data structure that follows the **FIFO (First In, First Out)** principle - the first element added is the first one to be removed.

## Core Operations

- **enqueue()** - Insert element at the back
- **dequeue()** - Remove element from the front
- **peek()/front()** - View the front element without removing
- **isEmpty()** - Check if queue is empty
- **size()** - Get number of elements

## Visual Example

```
[]
Enqueue 1
[1]
Enqueue 2
[1, 2]
Enqueue 3
[1, 2, 3]
Dequeue() → returns 1
[2, 3]
Dequeue() → returns 2
[3]
```

---

## Implementation 1: Fixed-Size Array (Circular Queue)

Using a circular buffer to avoid wasting space when elements are dequeued.

```python
class QueueArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = 0
        self.size = 0
    
    def enqueue(self, data):
        if self.size == self.capacity:
            raise OverflowError("Queue is full")
        
        self.queue[self.rear] = data
        self.rear = (self.rear + 1) % self.capacity  # Wrap around
        self.size += 1
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        
        data = self.queue[self.front]
        self.queue[self.front] = None  # Optional: clear reference
        self.front = (self.front + 1) % self.capacity  # Wrap around
        self.size -= 1
        return data
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue[self.front]
    
    def is_empty(self):
        return self.size == 0
    
    def is_full(self):
        return self.size == self.capacity
    
    def __len__(self):
        return self.size
```

**Time Complexity:**
- Enqueue: O(1)
- Dequeue: O(1)
- Peek: O(1)
- Space: O(n) where n is capacity

**Pros:**
- Constant time operations
- Cache-friendly (contiguous memory)
- Predictable memory usage

**Cons:**
- Fixed size - must know capacity upfront
- Can't grow dynamically

---

## Implementation 2: Linked List Queue

Dynamic size with no capacity limit.

```python
class QueueLinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
    
    def __init__(self):
        self.front = None  # Points to first node
        self.rear = None   # Points to last node
        self.size = 0
    
    def enqueue(self, data):
        new_node = self.Node(data)
        
        if self.rear is None:  # Empty queue
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        
        self.size += 1
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        
        data = self.front.data
        self.front = self.front.next
        
        if self.front is None:  # Queue became empty
            self.rear = None
        
        self.size -= 1
        return data
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.front.data
    
    def is_empty(self):
        return self.front is None
    
    def __len__(self):
        return self.size
```

**Time Complexity:**
- Enqueue: O(1)
- Dequeue: O(1)
- Peek: O(1)
- Space: O(n) where n is number of elements

**Pros:**
- Dynamic size - grows as needed
- No wasted space
- No capacity limit

**Cons:**
- Extra memory per node (next pointer)
- Less cache-friendly (non-contiguous memory)
- Memory allocation overhead per enqueue

---

## Python's Built-in: `collections.deque`

```python
from collections import deque

queue = deque()
queue.append(1)      # Enqueue at back
queue.append(2)
x = queue.popleft()  # Dequeue from front → 1
front = queue[0]     # Peek at front
```

**Note:** `deque` is implemented as a doubly-linked list internally and supports O(1) operations at both ends.

---

## Time Complexity Summary

| Operation | Array (Circular) | Linked List | deque |
|-----------|------------------|-------------|-------|
| Enqueue   | O(1)            | O(1)        | O(1)  |
| Dequeue   | O(1)            | O(1)        | O(1)  |
| Peek      | O(1)            | O(1)        | O(1)  |
| Search    | O(n)            | O(n)        | O(n)  |
| Space     | O(capacity)     | O(n)        | O(n)  |

---

## Common Patterns & When to Use Queues

### 1. **BFS (Breadth-First Search)**
Queues are essential for level-order traversal in trees and graphs.

```python
def bfs(root):
    if not root:
        return
    
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        print(node.val)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
```

### 2. **Level Order Traversal**
Process nodes level by level.

```python
def level_order(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    return result
```

### 3. **Sliding Window Maximum/Minimum**
Use a deque to maintain elements in a specific order.

```python
def sliding_window_max(nums, k):
    result = []
    dq = deque()  # Stores indices
    
    for i, num in enumerate(nums):
        # Remove elements outside window
        if dq and dq[0] < i - k + 1:
            dq.popleft()
        
        # Remove smaller elements (they can't be max)
        while dq and nums[dq[-1]] < num:
            dq.pop()
        
        dq.append(i)
        
        if i >= k - 1:
            result.append(nums[dq[0]])
    
    return result
```

### 4. **Task Scheduling**
Process tasks in order they arrive.

```python
def process_tasks(tasks):
    queue = deque(tasks)
    
    while queue:
        task = queue.popleft()
        process(task)
        
        if not task.is_complete():
            queue.append(task)  # Re-queue if not done
```

### 5. **Producer-Consumer Pattern**
One thread produces data, another consumes it.

```python
from queue import Queue
import threading

task_queue = Queue()

def producer():
    for i in range(10):
        task_queue.put(i)

def consumer():
    while True:
        task = task_queue.get()
        process(task)
        task_queue.task_done()
```

---

## Problem-Solving Patterns: When to Think "Queue"

### Look for these clues:
1. **"First come, first served"** - explicit FIFO ordering
2. **"Process in order of arrival"** - tasks, requests, events
3. **"Level by level"** - tree/graph traversal
4. **"Sliding window"** - especially with monotonic properties
5. **"Shortest path in unweighted graph"** - BFS
6. **"Generate all combinations at distance k"** - layer-by-layer expansion
7. **"Recently used/accessed"** - combined with hash map for LRU-like patterns

### Red flags that it's NOT a queue:
- Need to access middle elements frequently → use list/array
- Need LIFO (most recent first) → use [[Career/Prep/work/Stack|Stack]]
- Need sorted order → use heap/priority queue
- Need fast lookup by key → use hash map

---

## Variants

- **Deque (Double-ended Queue)** - Can enqueue/dequeue from both ends
- **Priority Queue** - Elements have priority, not just FIFO (use heap)
- **Circular Queue** - Fixed size with wraparound (shown in array implementation)
- **Blocking Queue** - Thread-safe queue that blocks on empty/full (Python's `queue.Queue`)

---

## Related Data Structures

- [[Career/Prep/work/Stack|Stack]] - LIFO counterpart to queue's FIFO
- [[Career/Prep/work/Linked List|Linked List]] - Can implement queue with linked list
- [[Career/Prep/work/Doubly Linked List|Doubly Linked List]] - Used in `collections.deque`
- Heap - For priority queues

---

## Key Takeaways

**Use Queue when:** Processing items in arrival order (FIFO)  
**Use BFS with Queue:** For shortest path, level-order traversal  
**Circular Array:** Best for fixed-size, high-performance scenarios  
**Linked List:** Best for dynamic size, unpredictable growth  
**Python's deque:** Best for most real-world use cases  

⚠**Watch out for:** Forgetting to handle empty queue in dequeue/peek  
⚠**Common mistake:** Using list with `pop(0)` - that's O(n), not O(1)!
