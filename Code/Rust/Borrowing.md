---
tags:
  - rust
  - ownership
  - memory
type: note
related:
  - '[[Rust]]'
  - '[[Copying]]'
  - '[[Memory Types]]'
---
# Borrowing

Rust's system for safely sharing references to data without transferring ownership.

## Overview

Borrowing allows you to reference data without taking ownership. The borrow checker enforces rules at compile time to prevent data races and dangling references.

## By Value (Move)

Passing by value transfers ownership—the original variable becomes invalid:

```rust
fn consume(val: String) {
    println!("{}", val);
}

let s = String::from("hello");
consume(s);      // Ownership moves to consume()
// consume(s);   // ERROR: s is no longer valid
```

## Shared Borrow (`&T`)

Immutable reference—multiple allowed simultaneously:

```rust
fn print(val: &String) {
    println!("{}", val);
}

let s = String::from("hello");
print(&s);  // Borrow s
print(&s);  // Borrow again - s still valid
println!("{}", s);  // s still owned here
```

## Mutable Borrow (`&mut T`)

Mutable reference—only one allowed at a time:

```rust
fn append(val: &mut String) {
    val.push_str(" world");
}

let mut s = String::from("hello");
append(&mut s);
println!("{}", s);  // "hello world"
```

## Borrowing Rules

1. **One mutable OR many immutable** — never both at the same time
2. **References must be valid** — no dangling pointers
3. **Borrows have scope** — end when last used (NLL)

```rust
let mut s = String::from("hello");

let r1 = &s;      // OK: immutable borrow
let r2 = &s;      // OK: multiple immutable borrows
println!("{} {}", r1, r2);
// r1 and r2 no longer used after this point

let r3 = &mut s;  // OK: mutable borrow (r1, r2 already done)
r3.push_str("!");
```

## Method Receivers

```rust
impl MyStruct {
    fn read(&self) { }       // Immutable borrow
    fn mutate(&mut self) { } // Mutable borrow
    fn consume(self) { }     // Takes ownership
}
```

## Common Patterns

### Limiting Borrow Scope

Use blocks to end borrows early:

```rust
let mut data = vec![1, 2, 3];

{
    let first = &data[0];  // Immutable borrow
    println!("{}", first);
}  // Borrow ends here

data.push(4);  // Now we can mutate
```

### Prefer `&str` over `String`

```rust
// Takes ownership - caller loses their String
fn bad(s: String) { }

// Borrows - caller keeps ownership
fn good(s: &str) { }

let owned = String::from("hello");
good(&owned);  // Borrow
good("literal");  // Works with literals too
```

## Tips

- Use `&self` for read-only methods, `&mut self` for mutating methods
- Prefer borrowing over cloning for performance
- The borrow checker is your friend—it prevents real bugs
- Use `&str` in function parameters instead of `&String`

## See Also

- [[Copying]] — Copy vs Clone traits
- [[Memory Types]] — Stack vs heap
- [[Rust]]
