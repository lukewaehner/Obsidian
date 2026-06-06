---
tags:
  - rust
  - learning
type: plan
related:
  - "[[Rust]]"
---
# Rust Learning Plan

A structured path through the notes with exercises at each stage. Each task includes expected input and output — implement it, then verify.

---

## Stage 1 — Types & Structure

Read: [[Cargo]] → [[Structs]] → [[Implementation]] → [[Derives]] → [[Enums]]

### Tasks

- [x] **1.1** Define a `Point` struct with `x: f64, y: f64`. Implement a method `distance_from_origin` that returns the Euclidean distance. ✅ 2026-05-11
```
input:  Point { x: 3.0, y: 4.0 }
output: 5.0
```

- [x] **1.2** Create a `Shape` enum with `Circle(f64)` and `Rectangle(f64, f64)`. Implement an `area` method. ✅ 2026-05-11
```
input:  Shape::Circle(3.0)
output: 28.274...

input:  Shape::Rectangle(4.0, 5.0)
output: 20.0
```

- [x] **1.3** Derive `Debug` and `PartialEq` on both types. Write assertions comparing two `Point` values and print a `Shape` with `{:?}`. ✅ 2026-05-11
```
input:  Point { x: 1.0, y: 1.0 } == Point { x: 1.0, y: 1.0 }
output: true
```

---

## Stage 2 — Ownership & Borrowing

Read: [[Copying]] → [[Borrowing]] → [[Memory Types]] → [[Lifetimes]]

### Tasks

- [x] **2.1** Write a function `count_vowels(s: &str) -> usize` that counts vowels without taking ownership. ✅ 2026-05-11
```
input:  "hello world"
output: 3
```

- [x] **2.2** Write a function `first_word(s: &str) -> &str` that returns a slice of the first word. ✅ 2026-05-11
```
input:  "hello world"
output: "hello"
```

- [x] **2.3** Write a function `longest<'a>(a: &'a str, b: &'a str) -> &'a str` that returns the longer string with an explicit lifetime. ✅ 2026-05-11
```
input:  "short", "longer string"
output: "longer string"
```

---

## Stage 3 — Traits & Generics

Read: [[Traits]] → [[Generics]] → [[Closures]] → [[Derives]]

### Tasks

- [x] **3.1** Define a `Summary` trait with `fn summarize(&self) -> String`. Implement it on two different structs. ✅ 2026-05-12
```
input:  Article { title: "Rust", author: "Steve" }.summarize()
output: "Rust, by Steve"
```

- [x] **3.2** Write a generic function `largest<T: PartialOrd>(list: &[T]) -> &T`. ✅ 2026-05-12
```
input:  [34, 50, 25, 100, 65]
output: &100
```

- [x] **3.3** Write a function `apply_twice<F: Fn(i32) -> i32>(f: F, x: i32) -> i32`. ✅ 2026-05-12
```
input:  |x| x + 3,  7
output: 13
```

---

## Stage 4 — Pattern Matching & Destructuring

Read: [[Pattern Matching]] → [[Destructuring]] → [[Slices]]

### Tasks

- [x] **4.1** Given a `Vec<Option<i32>>`, collect only the `Some` values into a new `Vec<i32>` using pattern matching in a loop. ✅ 2026-05-14
```
input:  [Some(1), None, Some(3), None, Some(5)]
output: [1, 3, 5]
```

- [x] **4.2** Destructure an array of pairs into two separate vecs of keys and values using `unzip`. ✅ 2026-05-14
```
input:  [(1, "one"), (2, "two"), (3, "three")]
output: keys=[1,2,3]  values=["one","two","three"]
```

- [x] **4.3** Use a slice pattern to write a recursive function `head_tail(s: &[i32]) -> Option<(i32, &[i32])>`. ✅ 2026-05-18
```
input:  [10, 20, 30]
output: Some((10, [20, 30]))

input:  []
output: None
```

---

## Stage 5 — Error Handling

Read: [[Result & Option]] → [[Error Handling Patterns]]

### Tasks

- [x] **5.1** Write `parse_all(inputs: &[&str]) -> Vec<i32>` that silently skips unparseable strings. ✅ 2026-05-16
```
input:  ["1", "two", "3", "four", "5"]
output: [1, 3, 5]
```

- [x] **5.2** Write `parse_strict(inputs: &[&str]) -> Result<Vec<i32>, String>` that returns `Err` on the first failure, including the bad value in the message.
```
input:  ["1", "2", "bad"]
output: Err("could not parse: \"bad\"")
```

- [x] **5.3** Define a custom error enum `AppError` with `Parse(String)` and `OutOfRange(i32)` variants. Write `validated_parse(s: &str) -> Result<i32, AppError>` that errors if the number is outside 1–100. ✅ 2026-05-19
```
input:  "42"   → Ok(42)
input:  "abc"  → Err(AppError::Parse("abc"))
input:  "200"  → Err(AppError::OutOfRange(200))
```

---

## Stage 6 — Collections & Iterators

Read: [[Collections]] → [[Iterators]] → [[Slices]] → [[Strings]]

### Tasks

- [x] **6.1** Given a `Vec<i32>`, compute the sum using iterator `fold` (recursive accumulation). ✅ 2026-05-26
```
input:  [1, 2, 3]
output: 6
```

- [x] **6.2** Partition a `Vec<i32>` into evens and odds in one pass.
```
input:  [1, 2, 3, 4, 5, 6]
output: evens=[2,4,6]  odds=[1,3,5]
```

- [x] **6.3** Find the most frequent element in a `Vec<i32>` using a `HashMap`. ✅ 2026-05-28
```
input:  [1, 3, 2, 3, 1, 3]
output: 3
```

- [x] **6.4** Given a sentence, return a `HashMap<char, usize>` of character frequencies (ignore spaces). ✅ 2026-05-28
```
input:  "hello world"
output: {'l': 3, 'o': 2, 'h': 1, 'e': 1, 'w': 1, 'r': 1, 'd': 1}
```

---

## Stage 7 — Code Organization & Testing

Read: [[Modules]] → [[Testing]] → [[Logging]]

### Tasks

- [x] **7.1** Move your `Shape` and `Point` types from Stage 1 into a `geometry` module. Make the types and methods `pub`. Call them from `main`. ✅ 2026-05-29
```
// Before: Shape::Circle(3.0)
// After: geometry::Shape::Circle(3.0)
```

- [x] **7.2** Write unit tests for `parse_strict` and `validated_parse` from Stage 5 — test both the `Ok` and `Err` paths. ✅ 2026-05-29
```
#[test] fn rejects_out_of_range()
#[test] fn accepts_valid_input()
```

---

## Stage 8 — Smart Pointers & Concurrency

Read: [[Smart Pointers]] → [[Concurrency]]

### Tasks

- [x] **8.1** Use `Rc<RefCell<Vec<i32>>>` to share a vec between two owners and push to it from both. ✅ 2026-06-05
```
input:  owner_a pushes 1, owner_b pushes 2
output: shared vec = [1, 2]
```

- [x] **8.2** Spawn 4 threads that each push their thread index into a shared `Arc<Mutex<Vec<usize>>>`. Collect and sort the result. ✅ 2026-06-06
```
output: [0, 1, 2, 3]
```

---

## Stage 9 — Async

Read: [[Async Await]]

### Tasks

- [ ] **9.1** Write an async function `fetch_len(url: &str) -> usize` using `reqwest` that returns the byte length of a response body. Call it with `tokio::main`.

- [ ] **9.2** Run two async tasks concurrently with `tokio::join!` and return both results as a tuple.
```
input:  async_double(3), async_double(5)
output: (6, 10)
```

---

## Stage 10 — Generics Deep Cut

Read: [[Generics]] → [[Traits]] → [[Lifetimes]]

### Tasks

- [ ] **10.1** Implement a generic `Stack<T>` struct with `push`, `pop`, `peek`, and `is_empty`.
```
let mut s: Stack<i32> = Stack::new();
s.push(1); s.push(2);
s.peek()   → Some(&2)
s.pop()    → Some(2)
s.pop()    → Some(1)
s.pop()    → None
```

- [ ] **10.2** Implement the `Iterator` trait on `Stack<T>` so you can use it in a `for` loop.
```
for item in stack { println!("{}", item); }
```

---

## Reference

| Stage | Focus          | Key Notes                       |
| ----- | -------------- | ------------------------------- |
| 1     | Types          | Structs, Enums, Derives         |
| 2     | Ownership      | Borrowing, Lifetimes            |
| 3     | Abstractions   | Traits, Generics, Closures      |
| 4     | Patterns       | Pattern Matching, Destructuring |
| 5     | Errors         | Result & Option, Error Handling |
| 6     | Data           | Collections, Iterators, Slices  |
| 7     | Org            | Modules, Testing                |
| 8     | Concurrency    | Smart Pointers, Concurrency     |
| 9     | Async          | Async Await                     |
| 10    | Advanced Types | Generics + Traits + Lifetimes   |
