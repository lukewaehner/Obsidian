## What is a Stack?

A **stack** is a linear data structure that follows the **LIFO (Last In, First Out)** principle. Think of it like a stack of plates or a barbell - the last item you add is the first one you must remove.

```
push(1) → [1]
push(2) → [1, 2]
push(3) → [1, 2, 3]
pop()   → returns 3, stack is now [1, 2]
pop()   → returns 2, stack is now [1]
```

## Core Operations

| Operation | Description | Time Complexity |
|-----------|-------------|----------------|
| `push(data)` | Add element to top | O(1) |
| `pop()` | Remove and return top element | O(1) |
| `peek()` / `top()` | View top element without removing | O(1) |
| `isEmpty()` | Check if stack is empty | O(1) |
| `size()` | Get number of elements | O(1) |

**Space Complexity**: O(n) where n is number of elements

## Implementation

### Using Python List (Array-based)

```python
class Stack:
    def __init__(self):
        self.data = []
    
    def push(self, item):
        self.data.append(item)
    
    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.data.pop()
    
    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.data[-1]
    
    def is_empty(self):
        return len(self.data) == 0
    
    def size(self):
        return len(self.data)
```

### Using Linked List

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self._size = 0
    
    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self._size += 1
    
    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        item = self.top.data
        self.top = self.top.next
        self._size -= 1
        return item
    
    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.top.data
    
    def is_empty(self):
        return self.top is None
    
    def size(self):
        return self._size
```

## When to Use Stacks

### Perfect For:
- **Backtracking algorithms** - DFS, maze solving, pathfinding
- **Expression evaluation** - parsing, compilers, calculators
- **Undo/Redo functionality** - text editors, browsers
- **Function call management** - call stack, recursion
- **Parentheses/bracket matching** - syntax validation
- **Reversing sequences** - reverse string, array
- **Next/Previous greater element** problems

### Recognition Patterns:
- "Most recent" or "last seen"
- "Matching pairs" (parentheses, tags)
- "Valid sequence"
- "Backtrack" or "undo"
- "Nearest greater/smaller"
- "Evaluate expression"

## Common Problem Patterns

### 1. Balanced Parentheses

Check if brackets/parentheses are properly matched.

```python
def is_valid(s: str) -> bool:
    stack = []
    pairs = {'(': ')', '[': ']', '{': '}'}
    
    for char in s:
        if char in pairs:
            stack.append(char)
        elif not stack or pairs[stack.pop()] != char:
            return False
    
    return len(stack) == 0
```

**Time**: O(n), **Space**: O(n)

### 2. Evaluate Reverse Polish Notation (RPN)

```python
def eval_rpn(tokens: list[str]) -> int:
    stack = []
    operators = {'+', '-', '*', '/'}
    
    for token in tokens:
        if token in operators:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            else:
                stack.append(int(a / b))
        else:
            stack.append(int(token))
    
    return stack[0]
```

**Example**: `["2", "1", "+", "3", "*"]` → `((2 + 1) * 3)` → `9`

### 3. Next Greater Element

Find the next greater element for each element in array.

```python
def next_greater_element(nums: list[int]) -> list[int]:
    result = [-1] * len(nums)
    stack = []  # Store indices
    
    for i, num in enumerate(nums):
        while stack and nums[stack[-1]] < num:
            idx = stack.pop()
            result[idx] = num
        stack.append(i)
    
    return result
```

**Time**: O(n), **Space**: O(n)

### 4. Decode String

Decode strings like `"3[a2[c]]"` → `"accaccacc"`

```python
def decode_string(s: str) -> str:
    stack = []
    curr_num = 0
    curr_str = ""
    
    for char in s:
        if char.isdigit():
            curr_num = curr_num * 10 + int(char)
        elif char == '[':
            stack.append((curr_str, curr_num))
            curr_str = ""
            curr_num = 0
        elif char == ']':
            prev_str, num = stack.pop()
            curr_str = prev_str + curr_str * num
        else:
            curr_str += char
    
    return curr_str
```

### 5. Min Stack

Design a stack with O(1) min() operation.

```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    
    def push(self, val: int):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
    
    def pop(self):
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()
    
    def top(self):
        return self.stack[-1]
    
    def get_min(self):
        return self.min_stack[-1]
```

**Key Insight**: Maintain a parallel stack tracking minimums!

## Real-World Applications

### 1. Function Call Stack
Every function call pushes a frame onto the call stack:
```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)  # Each call adds to stack
```

Stack overflow happens when too many recursive calls!

### 2. Browser History
- **Back button**: pop from history stack
- **Forward button**: push to forward stack
- **New page**: clear forward stack

### 3. Text Editor Undo/Redo
- **Undo stack**: stores previous states
- **Redo stack**: stores undone actions
- **New action**: clear redo stack

### 4. DFS (Depth-First Search)
```python
def dfs(graph, start):
    stack = [start]
    visited = set()
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            # Process node
            for neighbor in graph[node]:
                stack.append(neighbor)
```

### 5. Expression Parsing
Compilers use stacks to:
- Parse infix to postfix notation
- Evaluate expressions respecting operator precedence
- Check syntax validity

## Stack vs Other Structures

| Feature | Stack | Queue | Array |
|---------|-------|-------|-------|
| Access | Top only (LIFO) | Front/Rear (FIFO) | Random |
| Insert | O(1) at top | O(1) at rear | O(n) general, O(1) at end |
| Delete | O(1) from top | O(1) from front | O(n) general, O(1) at end |
| Use Case | Backtracking, undo | BFS, scheduling | Random access |

## Array vs Linked List Implementation

| Aspect | Array-Based | Linked List-Based |
|--------|-------------|-------------------|
| **Memory** | Contiguous, may need resize | Non-contiguous, no resize |
| **Cache** | Better (locality) | Worse (scattered) |
| **Overhead** | Wasted space if oversized | Pointer per node |
| **Operations** | All O(1)* | All O(1) |
| **Simplicity** | Very simple | More complex |

*Amortized for dynamic arrays

**Recommendation**: Use array-based (Python list) unless you have specific memory constraints.

## Common Edge Cases

```python
# Always check before popping!
if not stack:  # or stack.is_empty()
    # Handle empty stack
    pass

# Check bounds for peek
if stack:
    top = stack[-1]

# Consider single element
stack = [1]
stack.pop()  # Now empty!

# Consider duplicates in problems
stack = [1, 1, 1]  # How does your logic handle this?
```

## Interview Tips

1. **Ask clarifying questions**:
   - Can the stack have duplicates?
   - What should happen on underflow (empty pop)?
   - Any size constraints?

2. **Common techniques**:
   - Use auxiliary stack for min/max tracking
   - Monotonic stack for next greater/smaller problems
   - Store indices instead of values when you need positions

3. **Time complexity gotcha**:
   - Stack operations are O(1)
   - But iterating through n elements = O(n)
   - Overall complexity often O(n) for stack-based solutions

4. **Practice problems**:
   - Valid Parentheses (LeetCode 20)
   - Min Stack (LeetCode 155)
   - Daily Temperatures (LeetCode 739)
   - Evaluate RPN (LeetCode 150)
   - Basic Calculator (LeetCode 224)

## Key Takeaways

- **LIFO** - Last In, First Out
- **O(1) operations** - push, pop, peek
- **Recognition**: "most recent", "backtrack", "matching pairs"
- **Implementation**: Array-based is simpler and usually better
- **Patterns**: Monotonic stack, auxiliary stack, parentheses matching
- **Real-world**: Function calls, undo/redo, DFS, expression parsing

## Related Topics
- [[Code/Algorithms/Queue|Queue]] - FIFO counterpart
- [[Linked List|Linked List]] - Alternative implementation
- [[DFS]] - Stack-based graph traversal
- [[Monotonic Stack]] - Advanced pattern for next greater/smaller problems