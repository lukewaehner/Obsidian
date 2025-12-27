---
tags:
  - rust
  - collections
  - data-structures
type: note
related:
  - '[[Rust]]'
  - '[[Iterators]]'
  - '[[Memory Types]]'
---
# Collections

Standard library data structures in Rust.

## Overview

Rust's standard library provides efficient, generic collections for common data storage patterns. Unlike arrays, collections are heap-allocated and can grow dynamically.

## Vec - Dynamic Array

Contiguous, growable array:

```rust
let mut v: Vec<i32> = Vec::new();
v.push(1);
v.push(2);
v.push(3);

// Macro shorthand
let v = vec![1, 2, 3];

// Access
v[0];           // 1 (panics if out of bounds)
v.get(0);       // Some(&1) (safe)
v.first();      // Some(&1)
v.last();       // Some(&3)

// Modify
v.push(4);      // Add to end
v.pop();        // Remove from end -> Some(4)
v.insert(0, 0); // Insert at index
v.remove(0);    // Remove at index
```

| Operation | Complexity |
|-----------|------------|
| `push` / `pop` | O(1) amortized |
| `insert` / `remove` | O(n) |
| Index access | O(1) |
| Search | O(n) |

## VecDeque - Double-Ended Queue

Efficient push/pop at both ends:

```rust
use std::collections::VecDeque;

let mut dq = VecDeque::new();
dq.push_back(1);   // [1]
dq.push_back(2);   // [1, 2]
dq.push_front(0);  // [0, 1, 2]

dq.pop_front();    // Some(0) -> [1, 2]
dq.pop_back();     // Some(2) -> [1]
```

| Operation | Complexity |
|-----------|------------|
| `push_front` / `push_back` | O(1) amortized |
| `pop_front` / `pop_back` | O(1) |
| Index access | O(1) |

**Use case**: FIFO queues, sliding windows

## HashMap - Hash Table

Key-value storage with fast lookup:

```rust
use std::collections::HashMap;

let mut map = HashMap::new();
map.insert("key", 42);

// Access
map.get("key");           // Some(&42)
map.get("missing");       // None
map["key"];               // 42 (panics if missing)

// Check and insert
map.entry("key").or_insert(0);  // Returns &mut to existing or inserted
*map.entry("count").or_insert(0) += 1;  // Increment pattern

// Iterate
for (k, v) in &map {
    println!("{}: {}", k, v);
}
```

| Operation | Complexity |
|-----------|------------|
| `insert` / `get` / `remove` | O(1) average |
| Iteration | O(n) |

**Key requirements**: `Eq + Hash`

## BTreeMap - Sorted Map

Sorted key-value storage:

```rust
use std::collections::BTreeMap;

let mut map = BTreeMap::new();
map.insert(3, "three");
map.insert(1, "one");
map.insert(2, "two");

// Iteration is sorted by key
for (k, v) in &map {
    println!("{}: {}", k, v);  // 1, 2, 3
}

// Range queries
map.range(1..3);  // Keys 1 and 2

// First/last
map.first_key_value();  // Some((&1, &"one"))
map.last_key_value();   // Some((&3, &"three"))
```

| Operation | Complexity |
|-----------|------------|
| `insert` / `get` / `remove` | O(log n) |
| `first` / `last` | O(log n) |
| Iteration | O(n) |

**Key requirements**: `Ord`

**Use case**: When you need sorted iteration or range queries

## HashSet - Unique Values

Unordered set of unique values:

```rust
use std::collections::HashSet;

let mut set = HashSet::new();
set.insert(1);
set.insert(2);
set.insert(1);  // Duplicate, ignored

set.contains(&1);  // true
set.len();         // 2

// Set operations
let a: HashSet<_> = [1, 2, 3].into();
let b: HashSet<_> = [2, 3, 4].into();

&a | &b;  // Union: {1, 2, 3, 4}
&a & &b;  // Intersection: {2, 3}
&a - &b;  // Difference: {1}
```

## BTreeSet - Sorted Set

Sorted set of unique values:

```rust
use std::collections::BTreeSet;

let mut set = BTreeSet::new();
set.insert(3);
set.insert(1);
set.insert(2);

// Iteration is sorted
for x in &set {
    println!("{}", x);  // 1, 2, 3
}

set.first();  // Some(&1)
set.last();   // Some(&3)
```

## Choosing a Collection

| Need | Collection |
|------|------------|
| Ordered list, fast append | `Vec` |
| Queue (FIFO) | `VecDeque` |
| Fast key lookup | `HashMap` |
| Sorted keys | `BTreeMap` |
| Unique values | `HashSet` |
| Sorted unique values | `BTreeSet` |

## Common Patterns

### Initializing from Iterators

```rust
let v: Vec<_> = (0..10).collect();
let set: HashSet<_> = vec![1, 2, 3].into_iter().collect();
let map: HashMap<_, _> = vec![("a", 1), ("b", 2)].into_iter().collect();
```

### Entry API for HashMap

```rust
// Insert if missing
map.entry("key").or_insert(default);

// Insert with computation
map.entry("key").or_insert_with(|| expensive_default());

// Modify existing
map.entry("key").and_modify(|v| *v += 1).or_insert(1);
```

## Tips

- Use `Vec` by default—it's cache-friendly and fast
- Use `HashMap` for O(1) lookups by key
- Use `BTreeMap` when you need sorted keys or range queries
- Preallocate with `with_capacity()` if you know the size
- Use `.entry()` API to avoid double lookups in maps

## See Also

- [[Iterators]] — Working with collection iterators
- [[Memory Types]] — Heap allocation
- [[Rust]]
