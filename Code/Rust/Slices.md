---
tags:
  - rust
  - types
  - collections
type: note
related:
  - "[[Rust]]"
  - "[[Collections]]"
  - "[[Iterators]]"
  - "[[Destructuring]]"
---
# Slices

Working with contiguous sequences — arrays, slices, and collection operations.

## Arrays vs Slices vs Vec

```rust
let arr: [i32; 3] = [1, 2, 3];   // Fixed size, stack allocated
let slice: &[i32] = &arr;         // Borrowed view into contiguous memory
let vec: Vec<i32> = vec![1, 2, 3]; // Growable, heap allocated
```

A slice `&[T]` is just a pointer + length — it can point into an array, a Vec, or any contiguous block.

## Array Literals

```rust
let a = [1, 2, 3];           // Type inferred: [i32; 3]
let b = [0; 5];              // [0, 0, 0, 0, 0] — repeat value
let c: [u8; 4] = [1, 2, 3, 4];

// Access
a[0];          // 1 (panics out of bounds)
a.get(0);      // Some(&1)
a.get(99);     // None
a.len();       // 3
```

## Getting a Slice

```rust
let v = vec![1, 2, 3, 4, 5];

&v[..];      // whole thing
&v[1..3];    // [2, 3]
&v[2..];     // [3, 4, 5]
&v[..3];     // [1, 2, 3]
```

## Collecting into an Array

```rust
// Iterator → fixed array via try_into
use std::convert::TryInto;

let v = vec![1, 2, 3];
let arr: [i32; 3] = v.try_into().unwrap();

// Or from a mapped iterator
let arr: [i32; 3] = [1, 2, 3].map(|x| x * 2);  // [2, 4, 6]
```

## Common Slice Methods

### Searching

```rust
let s = [3, 1, 4, 1, 5, 9];

s.contains(&4);                     // true
s.iter().position(|&x| x == 4);    // Some(2)
s.iter().rposition(|&x| x == 1);   // Some(3) — from right
s.binary_search(&4);                // Ok(2) — requires sorted
```

### Sorting

```rust
let mut v = vec![3, 1, 4, 1, 5];

v.sort();                              // [1, 1, 3, 4, 5]
v.sort_by(|a, b| b.cmp(a));           // descending
v.sort_by_key(|x| std::cmp::Reverse(*x));  // same as above
v.sort_unstable();                    // faster, no stability guarantee

// Structs
let mut orders = vec![/* ... */];
orders.sort_by_key(|o| o.price);
```

### Splitting

```rust
let v = [1, 2, 3, 4, 5];

let (left, right) = v.split_at(2);  // ([1, 2], [3, 4, 5])

// Split on condition — returns iterator of subslices
let parts: Vec<_> = v.split(|x| x % 2 == 0).collect();
// [[1], [3], [5]] — splits at even numbers, excluding them

// Split first/last
let (first, rest) = v.split_first().unwrap();  // (&1, &[2,3,4,5])
let (last, init) = v.split_last().unwrap();    // (&5, &[1,2,3,4])
```

### Windows & Chunks

```rust
let v = [1, 2, 3, 4, 5];

// Overlapping windows of size n
for w in v.windows(3) {
    println!("{:?}", w);  // [1,2,3], [2,3,4], [3,4,5]
}

// Non-overlapping chunks of size n
for c in v.chunks(2) {
    println!("{:?}", c);  // [1,2], [3,4], [5]
}

// chunks_exact — only full chunks, remainder accessible
let chunks = v.chunks_exact(2);
let remainder = chunks.remainder();  // [5]
```

### Modifying

```rust
let mut v = vec![1, 2, 2, 3, 2];

v.dedup();                    // Remove consecutive duplicates: [1, 2, 3, 2]
v.sort(); v.dedup();          // Remove all duplicates: [1, 2, 3]
v.reverse();                  // In place: [3, 2, 1]
v.rotate_left(1);             // [2, 1, 3]
v.retain(|x| *x % 2 != 0);   // Keep only odd: [1, 3]
v.fill(0);                    // Set all elements to 0
v.swap(0, 2);                 // Swap elements at indices
```

## Unpack Operations

### unzip — Split Iterator of Pairs

The inverse of `zip`:

```rust
let pairs = vec![(1, 'a'), (2, 'b'), (3, 'c')];
let (nums, chars): (Vec<i32>, Vec<char>) = pairs.into_iter().unzip();
// nums = [1, 2, 3], chars = ['a', 'b', 'c']
```

### partition — Split by Predicate

```rust
let nums = vec![1, 2, 3, 4, 5, 6];
let (evens, odds): (Vec<_>, Vec<_>) = nums.iter().partition(|x| *x % 2 == 0);
// evens = [2, 4, 6], odds = [1, 3, 5]
```

### drain — Move Elements Out

```rust
let mut v = vec![1, 2, 3, 4, 5];

// Remove and return a range
let drained: Vec<_> = v.drain(1..3).collect();  // [2, 3]
// v is now [1, 4, 5]

// Drain everything
let all: Vec<_> = v.drain(..).collect();
```

### split_off — Split Vec in Two

```rust
let mut v = vec![1, 2, 3, 4, 5];
let tail = v.split_off(3);  // tail = [4, 5], v = [1, 2, 3]
```

### extend & append

```rust
let mut a = vec![1, 2, 3];
let mut b = vec![4, 5, 6];

a.extend(&b);          // a = [1,2,3,4,5,6], b unchanged
a.extend([7, 8, 9]);   // works with arrays too

a.append(&mut b);      // moves b into a, b becomes empty
```

### flatten

```rust
let nested = vec![vec![1, 2], vec![3, 4], vec![5]];
let flat: Vec<_> = nested.into_iter().flatten().collect();
// [1, 2, 3, 4, 5]

// Also works on arrays of options
let opts = vec![Some(1), None, Some(3)];
let values: Vec<_> = opts.into_iter().flatten().collect();
// [1, 3]
```

## Converting Between Types

```rust
// Array → Vec
let arr = [1, 2, 3];
let v = arr.to_vec();           // copies
let v = Vec::from(arr);         // same

// Vec → Array (panics if wrong length)
let v = vec![1, 2, 3];
let arr: [i32; 3] = v.try_into().unwrap();

// Slice → Vec
let s = &[1, 2, 3];
let v = s.to_vec();

// Vec → slice
let v = vec![1, 2, 3];
let s: &[i32] = &v;
let s: &[i32] = v.as_slice();
```

## See Also

- [[Destructuring]] — Unpacking arrays, structs, and enums with patterns
- [[Iterators]] — Lazy sequence processing
- [[Collections]] — Vec, HashMap, and other data structures
- [[Rust]]
