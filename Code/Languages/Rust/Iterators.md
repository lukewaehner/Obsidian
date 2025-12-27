---
tags:
  - rust
  - iterators
  - functional
type: note
related:
  - '[[Rust]]'
  - '[[Collections]]'
  - '[[Pattern Matching]]'
---
# Iterators

Lazy sequence processing in Rust.

## Overview

Iterators provide a way to process sequences of elements lazily. They're zero-cost abstractions—the compiler optimizes them to be as fast as hand-written loops.

## Basic Iteration

```rust
let v = vec![1, 2, 3];

// for loop (most common)
for x in &v {
    println!("{}", x);
}

// Iterator methods
v.iter().for_each(|x| println!("{}", x));
```

## Iterator Types

```rust
let v = vec![1, 2, 3];

v.iter();       // Iterator over &T
v.iter_mut();   // Iterator over &mut T
v.into_iter();  // Iterator over T (consumes v)
```

## Common Adapters

### map - Transform Elements

```rust
let v = vec![1, 2, 3];
let doubled: Vec<_> = v.iter().map(|x| x * 2).collect();
// [2, 4, 6]
```

### filter - Select Elements

```rust
let v = vec![1, 2, 3, 4, 5];
let evens: Vec<_> = v.iter().filter(|x| *x % 2 == 0).collect();
// [2, 4]
```

### filter_map - Filter and Transform

```rust
let strings = vec!["1", "two", "3"];
let nums: Vec<i32> = strings
    .iter()
    .filter_map(|s| s.parse().ok())
    .collect();
// [1, 3]
```

### flat_map - Flatten Nested Iterators

```rust
let nested = vec![vec![1, 2], vec![3, 4]];
let flat: Vec<_> = nested.iter().flat_map(|v| v.iter()).collect();
// [1, 2, 3, 4]
```

### take / skip

```rust
let v = vec![1, 2, 3, 4, 5];
let first_two: Vec<_> = v.iter().take(2).collect();  // [1, 2]
let after_two: Vec<_> = v.iter().skip(2).collect();  // [3, 4, 5]
```

### enumerate - Add Indices

```rust
for (i, x) in v.iter().enumerate() {
    println!("{}: {}", i, x);
}
```

### zip - Pair Elements

```rust
let a = [1, 2, 3];
let b = ["a", "b", "c"];
let zipped: Vec<_> = a.iter().zip(b.iter()).collect();
// [(1, "a"), (2, "b"), (3, "c")]
```

### chain - Concatenate Iterators

```rust
let a = [1, 2];
let b = [3, 4];
let chained: Vec<_> = a.iter().chain(b.iter()).collect();
// [1, 2, 3, 4]
```

## Consumers

### collect - Gather into Collection

```rust
let v: Vec<_> = (0..5).collect();
let set: HashSet<_> = v.iter().collect();
let s: String = vec!['a', 'b', 'c'].into_iter().collect();
```

### fold / reduce - Accumulate

```rust
let sum = (1..=5).fold(0, |acc, x| acc + x);  // 15
let sum = (1..=5).reduce(|acc, x| acc + x);   // Some(15)
```

### find - First Match

```rust
let v = vec![1, 2, 3, 4];
let first_even = v.iter().find(|x| *x % 2 == 0);  // Some(&2)
```

### any / all

```rust
let v = vec![1, 2, 3];
v.iter().any(|x| *x > 2);  // true
v.iter().all(|x| *x > 0);  // true
```

### count / sum / product

```rust
(0..10).count();           // 10
(1..=5).sum::<i32>();      // 15
(1..=5).product::<i32>();  // 120
```

### min / max

```rust
let v = vec![3, 1, 4, 1, 5];
v.iter().min();  // Some(&1)
v.iter().max();  // Some(&5)

// With custom comparison
v.iter().min_by_key(|x| -(*x));  // Some(&5)
```

## Chaining

Compose multiple operations:

```rust
let result: i32 = (1..=10)
    .filter(|x| x % 2 == 0)   // Keep evens
    .map(|x| x * x)           // Square them
    .take(3)                  // First 3
    .sum();                   // Sum: 4 + 16 + 36 = 56
```

## Creating Iterators

```rust
// Ranges
0..10           // 0 to 9
0..=10          // 0 to 10 (inclusive)

// Repeat
std::iter::repeat(42).take(5);  // [42, 42, 42, 42, 42]

// From function
std::iter::from_fn(|| Some(rand::random::<u8>())).take(5);

// Once / Empty
std::iter::once(42);
std::iter::empty::<i32>();
```

## Lazy Evaluation

Iterators are lazy—nothing happens until consumed:

```rust
let v = vec![1, 2, 3];

// This does nothing by itself
let iter = v.iter().map(|x| {
    println!("Processing {}", x);
    x * 2
});

// Only when consumed does it execute
let result: Vec<_> = iter.collect();
```

## Common Patterns

### Building Results

```rust
let mut trades = Vec::new();
while let Some(order) = get_next_order() {
    trades.push(process(order));
}
```

### Finding Minimum/Maximum

```rust
let fill = taker.qty.min(maker.qty);
let best = prices.iter().min();
```

### Cleaning Up Empty Entries

```rust
if queue.is_empty() {
    self.levels.remove(&price);
}
```

## Tips

- Prefer iterator methods over manual loops for clarity
- Use `iter()` for borrowing, `into_iter()` for ownership
- Collect with turbofish: `collect::<Vec<_>>()`
- Use `&` in filter closures: `.filter(|&x| x > 0)`
- Iterators are zero-cost—use them freely

## See Also

- [[Collections]] — Data structures to iterate
- [[Pattern Matching]] — Matching in closures
- [[Rust]]
