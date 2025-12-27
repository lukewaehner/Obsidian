---
tags:
  - rust
  - memory
  - pointers
type: note
related:
  - '[[Rust]]'
  - '[[Borrowing]]'
  - '[[Memory Types]]'
  - '[[Concurrency]]'
---
# Smart Pointers

Heap allocation and shared ownership through pointer types.

## Overview

Smart pointers are data structures that act like pointers but have additional metadata and capabilities. They manage memory automatically and enable patterns like shared ownership and interior mutability.

## Basic Usage

### Box - Heap Allocation

```rust
// Allocate on heap
let b = Box::new(5);
println!("{}", b);  // Dereferences automatically

// Required for recursive types
enum List {
    Cons(i32, Box<List>),
    Nil,
}

let list = List::Cons(1, 
    Box::new(List::Cons(2, 
        Box::new(List::Nil))));

// For trait objects
let animal: Box<dyn Animal> = Box::new(Dog { name: "Rex".into() });
```

### Rc - Reference Counting

```rust
use std::rc::Rc;

// Shared ownership (single-threaded)
let a = Rc::new(5);
let b = Rc::clone(&a);  // Increment count, not deep clone
let c = Rc::clone(&a);

println!("Count: {}", Rc::strong_count(&a));  // 3

// When all Rc's are dropped, data is freed
```

### Arc - Atomic Reference Counting

```rust
use std::sync::Arc;
use std::thread;

// Shared ownership (thread-safe)
let data = Arc::new(vec![1, 2, 3]);

let handles: Vec<_> = (0..3).map(|i| {
    let data = Arc::clone(&data);
    thread::spawn(move || {
        println!("Thread {}: {:?}", i, data);
    })
}).collect();

for handle in handles {
    handle.join().unwrap();
}
```

### RefCell - Interior Mutability

```rust
use std::cell::RefCell;

// Mutate through immutable reference
let data = RefCell::new(5);

// Borrow at runtime
*data.borrow_mut() += 1;
println!("{}", data.borrow());  // 6

// Panics if borrowing rules violated at runtime
// let mut a = data.borrow_mut();
// let mut b = data.borrow_mut();  // Panic! Already borrowed mutably
```

### Cell - Copy Types

```rust
use std::cell::Cell;

// For Copy types, simpler than RefCell
let value = Cell::new(5);
value.set(10);
println!("{}", value.get());  // 10
```

## Key Concepts

### When to Use Each

| Type | Ownership | Thread-Safe | Mutability | Use Case |
|------|-----------|-------------|------------|----------|
| `Box<T>` | Single | Yes | Through `&mut` | Heap allocation, recursive types |
| `Rc<T>` | Shared | No | Immutable | Shared data, single thread |
| `Arc<T>` | Shared | Yes | Immutable | Shared data, multiple threads |
| `RefCell<T>` | Single | No | Runtime checked | Interior mutability |
| `Mutex<T>` | Shared | Yes | Locked access | Thread-safe mutation |
| `Cell<T>` | Single | No | Copy in/out | Simple interior mutability |

### Combining Smart Pointers

```rust
use std::rc::Rc;
use std::cell::RefCell;

// Shared ownership with mutability
let shared = Rc::new(RefCell::new(vec![1, 2, 3]));

let a = Rc::clone(&shared);
let b = Rc::clone(&shared);

a.borrow_mut().push(4);
b.borrow_mut().push(5);

println!("{:?}", shared.borrow());  // [1, 2, 3, 4, 5]
```

```rust
use std::sync::{Arc, Mutex};

// Thread-safe shared mutable state
let counter = Arc::new(Mutex::new(0));

let handles: Vec<_> = (0..10).map(|_| {
    let counter = Arc::clone(&counter);
    std::thread::spawn(move || {
        let mut num = counter.lock().unwrap();
        *num += 1;
    })
}).collect();

for handle in handles {
    handle.join().unwrap();
}

println!("Count: {}", *counter.lock().unwrap());  // 10
```

### Deref and DerefMut

Smart pointers implement `Deref` for automatic dereferencing:

```rust
use std::ops::Deref;

struct MyBox<T>(T);

impl<T> Deref for MyBox<T> {
    type Target = T;
    
    fn deref(&self) -> &Self::Target {
        &self.0
    }
}

let x = MyBox(5);
assert_eq!(5, *x);  // Calls deref()

// Deref coercion
fn print(s: &str) { println!("{}", s); }
let s = MyBox(String::from("hello"));
print(&s);  // &MyBox<String> -> &String -> &str
```

### Drop Trait

Cleanup when smart pointers go out of scope:

```rust
struct CustomPointer {
    data: String,
}

impl Drop for CustomPointer {
    fn drop(&mut self) {
        println!("Dropping: {}", self.data);
    }
}

let p = CustomPointer { data: String::from("hello") };
// "Dropping: hello" printed when p goes out of scope

// Force early drop
drop(p);  // Dropped immediately
```

## Common Patterns

### Cow - Clone on Write

```rust
use std::borrow::Cow;

fn process(input: &str) -> Cow<str> {
    if input.contains("bad") {
        // Only allocate if modification needed
        Cow::Owned(input.replace("bad", "good"))
    } else {
        Cow::Borrowed(input)
    }
}

let clean = process("hello");        // Borrowed
let modified = process("bad word");  // Owned
```

### Weak References

```rust
use std::rc::{Rc, Weak};

struct Node {
    value: i32,
    parent: RefCell<Weak<Node>>,  // Weak to avoid cycles
    children: RefCell<Vec<Rc<Node>>>,
}

// Weak doesn't prevent deallocation
let strong = Rc::new(5);
let weak = Rc::downgrade(&strong);

// Must upgrade to access
if let Some(value) = weak.upgrade() {
    println!("{}", value);
}
```

### Pin - Prevent Moving

```rust
use std::pin::Pin;
use std::marker::PhantomPinned;

struct Unmovable {
    data: String,
    _pin: PhantomPinned,
}

// Pin guarantees data won't move in memory
// Required for self-referential structs and async
let pinned = Box::pin(Unmovable {
    data: String::from("hello"),
    _pin: PhantomPinned,
});
```

## Tips

- Use `Box` when you need heap allocation or have recursive types
- Use `Rc` for shared ownership in single-threaded code
- Use `Arc` for shared ownership across threads
- Use `RefCell` when you need interior mutability
- Combine `Rc<RefCell<T>>` or `Arc<Mutex<T>>` for shared mutable state
- `Cow` is great for functions that sometimes modify, sometimes don't
- Watch out for reference cycles with `Rc`—use `Weak` to break them
- `Cell` is simpler than `RefCell` for `Copy` types

## See Also

- [[Borrowing]] — Ownership without smart pointers
- [[Memory Types]] — Stack vs heap
- [[Concurrency]] — Thread-safe pointers
- [[Rust]]
