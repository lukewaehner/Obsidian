---
tags:
  - dsa
  - data-structures
  - hashtable
  - hashmap
complexity: O(1) average
related:
  - '[[Binary Search]]'
  - '[[Linked List]]'
  - '[[DSA]]'
---
# Hashtable (Hash Map)

## Overview
A **hashtable** (hash map, hash table) is a data structure that maps **keys to values** using a **hash function** for fast lookups, inserts, and deletions.

**Core Operations:**
- `insert(key, value)` - Add/update key-value pair
- `get(key)` - Retrieve value by key
- `delete(key)` - Remove key-value pair
- `contains(key)` - Check if key exists

**Time Complexity (Average):** O(1) for all operations  
**Space Complexity:** O(k) where k = number of keys

---

## Key Concepts

### Dictionary vs Hashtable
- **Dictionary**: Generic concept - any way to map keys to values
- **Hashtable**: Specific implementation using hash functions to map keys to array indices

### Hash Function
Converts a key into an array index:
```
h(key) → index in table
```

**Properties of good hash functions:**
- **Deterministic**: Same key always produces same hash
- **Uniform distribution**: Minimizes collisions
- **Fast to compute**: O(1) operation
- **Minimize collisions**: Different keys should produce different hashes

### Common Hash Function: Division Method
```python
def hash(key, table_size):
    return hash(key) % table_size
```
Where `m` = size of the table (ideally a prime number)

---

## Collision Handling

When two keys hash to the same index, we have a **collision**.

### 1. Chaining
Use a linked list at each table slot to store multiple key-value pairs:
```
Table[0] → [(k1, v1)] → [(k2, v2)] → None
Table[1] → [(k3, v3)] → None
Table[2] → None
```

**Pros:** Simple, no clustering  
**Cons:** Extra memory for linked list pointers

### 2. Open Addressing (Linear Probing)
If slot is occupied, try the next slot:
```python
index = hash(key)
while table[index] is occupied:
    index = (index + 1) % capacity  # Wrap around
```

**Pros:** Better cache locality, no extra pointers
**Cons:** Clustering can degrade performance

---

## Load Factor & Resizing

**Load Factor** = `size / capacity`

When load factor exceeds threshold (typically 0.7), **resize** the table:
1. Double the capacity
2. Rehash all existing keys into new table
3. Reset size counter

**Why resize?**
- Keeps operations close to O(1)
- Prevents too many collisions
- Maintains performance guarantees

---

## Implementation: Hash Map (Chaining)

```python
class HashMap:
    def __init__(self, capacity=8):
        self.capacity = capacity
        self.size = 0
        self.map = [None] * capacity
    
    def _hash(self, key):
        """Calculate index for key"""
        return hash(key) % self.capacity
    
    def add(self, key, value):
        """Add or update key-value pair"""
        # Check if resize needed
        if (self.size + 1) / self.capacity >= 0.7:
            self._resize()
        
        # Find slot for key
        slot, exists = self._find_slot(key)
        
        # Update existing or add new
        self.map[slot] = (key, value)
        if not exists:
            self.size += 1
    
    def _find_slot(self, key):
        """Find slot for key using linear probing"""
        index = self._hash(key)
        
        for _ in range(self.capacity):
            # Empty slot - key doesn't exist
            if self.map[index] is None:
                return (index, False)
            
            # Found existing key
            if self.map[index][0] == key:
                return (index, True)
            
            # Collision - try next slot
            index = (index + 1) % self.capacity
        
        # Table is full (should never happen with proper resizing)
        raise Exception("Hash table is full")
    
    def _resize(self):
        """Double capacity and rehash all entries"""
        old_map = self.map
        self.capacity *= 2
        self.map = [None] * self.capacity
        self.size = 0
        
        # Rehash all existing entries
        for slot in old_map:
            if slot:
                k, v = slot
                self.add(k, v)
    
    def get(self, key):
        """Get value for key, or None if not found"""
        index = self._hash(key)
        
        for _ in range(self.capacity):
            slot = self.map[index]
            
            # Empty slot - key doesn't exist
            if slot is None:
                return None
            
            # Found the key
            if slot[0] == key:
                return slot[1]
            
            # Keep probing
            index = (index + 1) % self.capacity
        
        return None
    
    def exists(self, key):
        """Check if key exists in map"""
        _, found = self._find_slot(key)
        return found
    
    def remove(self, key):
        """Remove key-value pair"""
        index = self._hash(key)
        
        for _ in range(self.capacity):
            slot = self.map[index]
            
            # Not found
            if slot is None:
                return
            
            # Found - remove it
            if slot[0] == key:
                self.map[index] = None
                self.size -= 1
                return
            
            # Keep probing
            index = (index + 1) % self.capacity


# Example usage
hm = HashMap()
hm.add("name", "Alice")
hm.add("age", 25)
hm.add("city", "Boston")

print(hm.get("name"))      # Output: Alice
print(hm.exists("age"))    # Output: True

hm.remove("age")
print(hm.exists("age"))    # Output: False
print(hm.get("city"))      # Output: Boston
```

---

## Implementation: Hash Set (Keys Only)

```python
class HashTable:
    """Hash set implementation - stores only keys, no values"""
    
    def __init__(self, capacity=10, load_factor=0.7):
        self.size = 0
        self.capacity = capacity
        self.table = [None] * capacity
        self.load_factor = load_factor
    
    def hash(self, key):
        """Hash function: key → index"""
        return hash(key) % self.capacity
    
    def resize(self):
        """Double capacity and rehash all keys"""
        old_table = self.table
        self.capacity *= 2
        self.table = [None] * self.capacity
        self.size = 0
        
        for item in old_table:
            if item is not None:
                self.add(item)
    
    def add(self, key):
        """Add key to set (ignore if already exists)"""
        # Resize if load factor exceeded
        if self.size / self.capacity > self.load_factor:
            self.resize()
        
        index = self.hash(key)
        
        # Linear probing to find empty slot
        while self.table[index] not in (None, key):
            index = (index + 1) % self.capacity
        
        # Add key if it's a new entry
        if self.table[index] != key:
            self.table[index] = key
            self.size += 1
    
    def contains(self, key):
        """Check if key exists in set"""
        index = self.hash(key)
        
        for _ in range(self.capacity):
            # Found key
            if self.table[index] == key:
                return True
            
            # Empty slot - key doesn't exist
            if self.table[index] is None:
                return False
            
            # Keep probing
            index = (index + 1) % self.capacity
        
        return False
    
    def remove(self, key):
        """Remove key from set"""
        index = self.hash(key)
        
        for _ in range(self.capacity):
            # Found key - delete it
            if self.table[index] == key:
                self.table[index] = None
                self.size -= 1
                return
            
            # Already deleted or never existed
            if self.table[index] is None:
                return
            
            # Keep probing
            index = (index + 1) % self.capacity


# Example usage
h = HashTable(10)
h.add(1)
h.add(3)
h.add(5)

for i in range(1, 6):
    print(f"h contains {i}: {h.contains(i)}")
# Output:
# h contains 1: True
# h contains 2: False
# h contains 3: True
# h contains 4: False
# h contains 5: True

h.remove(1)
print(f"h contains 1: {h.contains(1)}")  # Output: False
```

---

## Time Complexity Analysis

| Operation | Average Case | Worst Case |
|-----------|--------------|------------|
| Insert    | O(1)         | O(n)*      |
| Search    | O(1)         | O(n)*      |
| Delete    | O(1)         | O(n)*      |

\*Worst case occurs with many collisions (all keys hash to same index)

**Space Complexity:** O(k) where k = number of keys stored

**Why O(1) average?**
- Good hash function distributes keys uniformly
- Load factor kept low through resizing
- Expected chain length is O(1)

---

## Hash Function Techniques

1. **Division Method**: `h(k) = k mod m` (simple, fast)
2. **Multiplication Method**: `h(k) = ⌊m(kA mod 1)⌋` where 0 < A < 1
3. **Universal Hashing**: Randomly select hash function from family
4. **Dynamic Perfect Hashing**: Two-level hashing for O(1) worst case

---

## Common Use Cases

✅ **Caching** - Store computed results  
✅ **Frequency counting** - Count occurrences  
✅ **Duplicate detection** - Check if element seen before  
✅ **Database indexing** - Fast record lookup  
✅ **Symbol tables** - Compilers use for variable storage  
✅ **Two Sum problem** - Store complements

---

## Comparison with Other Structures

| Structure | Search | Insert | Delete | Ordered |
|-----------|--------|--------|--------|---------|
| Hashtable | O(1)   | O(1)   | O(1)   | No      |
| [[Binary Search]] (sorted array) | O(log n) | O(n) | O(n) | Yes |
| [[Linked List]] | O(n) | O(1) | O(1) | No |

---

## Common Pitfalls

1. **Poor hash function** → Too many collisions
2. **Not resizing** → Performance degrades to O(n)
3. **Using mutable keys** → Key changes after insertion breaks lookup
4. **Ignoring load factor** → Table becomes too full
5. **Deletion in open addressing** → May break probe sequence

---

## Related Concepts
- [[DSA]] - Main data structures overview
- [[Linked List]] - Used in chaining approach
- **Hash Function Design** - Critical for performance
- **Time Complexity** - Understanding O(1) average case
- **Load Factor** - Performance tuning parameter

---

## Key Takeaways
✅ **O(1) average** time for insert/search/delete  
✅ Requires **good hash function** to minimize collisions  
✅ **Load factor** determines when to resize  
✅ Trade-off: fast operations but **no ordering** of keys  
✅ Perfect for **fast lookups** and **duplicate detection**
