---
tags:
  - rust
  - unsafe
  - ffi
type: note
related:
  - '[[Rust]]'
  - '[[Smart Pointers]]'
  - '[[Concurrency]]'
  - '[[Memory Types]]'
---
# Unsafe

Bypassing Rust's safety guarantees when necessary.

## Overview

Unsafe Rust allows operations the compiler can't verify as safe. It doesn't disable the borrow checker—it just unlocks additional capabilities. Use it sparingly and carefully.

## Basic Usage

### Unsafe Blocks

```rust
let mut num = 5;
let r1 = &num as *const i32;  // Raw pointer (safe to create)

unsafe {
    println!("r1 is: {}", *r1);  // Dereferencing requires unsafe
}
```

### Unsafe Functions

```rust
unsafe fn dangerous() {
    // Entire function body is unsafe
}

unsafe {
    dangerous();  // Must call in unsafe block
}
```

## Key Concepts

### What Unsafe Allows

1. **Dereference raw pointers**
2. **Call unsafe functions**
3. **Access mutable statics**
4. **Implement unsafe traits**
5. **Access union fields**

```rust
// 1. Raw pointers
let mut value = 42;
let ptr = &mut value as *mut i32;
unsafe {
    *ptr = 100;
}

// 2. Unsafe functions
unsafe fn peek(addr: *const i32) -> i32 {
    *addr
}

// 3. Mutable statics
static mut COUNTER: u32 = 0;
unsafe {
    COUNTER += 1;
}

// 4. Unsafe traits
unsafe trait Dangerous {}
unsafe impl Dangerous for i32 {}

// 5. Unions
union IntOrFloat {
    i: i32,
    f: f32,
}
let u = IntOrFloat { i: 42 };
unsafe {
    println!("{}", u.f);  // Reinterpret bits
}
```

### Raw Pointers

```rust
let mut x = 5;

// Create raw pointers (safe)
let r1 = &x as *const i32;    // Immutable raw pointer
let r2 = &mut x as *mut i32;  // Mutable raw pointer

// Can have both at same time (unlike references)
// Can point to invalid memory
// Can be null
// No automatic cleanup

unsafe {
    // Dereference (unsafe)
    println!("r1: {}", *r1);
    *r2 = 10;
    
    // Pointer arithmetic
    let arr = [1, 2, 3];
    let ptr = arr.as_ptr();
    println!("{}", *ptr.add(1));  // 2
}
```

### Null and Validity

```rust
use std::ptr;

let null_ptr: *const i32 = ptr::null();
let null_mut: *mut i32 = ptr::null_mut();

// Check for null
if !null_ptr.is_null() {
    unsafe { println!("{}", *null_ptr); }
}

// NonNull for non-null pointers
use std::ptr::NonNull;
let mut x = 5;
let ptr = NonNull::new(&mut x as *mut i32).unwrap();
```

## Common Patterns

### Safe Abstraction Over Unsafe

```rust
pub fn split_at_mut(slice: &mut [i32], mid: usize) -> (&mut [i32], &mut [i32]) {
    let len = slice.len();
    let ptr = slice.as_mut_ptr();
    
    assert!(mid <= len);
    
    unsafe {
        (
            std::slice::from_raw_parts_mut(ptr, mid),
            std::slice::from_raw_parts_mut(ptr.add(mid), len - mid),
        )
    }
}
```

### FFI - Foreign Function Interface

```rust
extern "C" {
    fn abs(input: i32) -> i32;
    fn strlen(s: *const i8) -> usize;
}

fn main() {
    unsafe {
        println!("abs(-3) = {}", abs(-3));
    }
}

// Export Rust function for C
#[no_mangle]
pub extern "C" fn rust_function(x: i32) -> i32 {
    x * 2
}
```

### Interfacing with C Strings

```rust
use std::ffi::{CStr, CString};
use std::os::raw::c_char;

// Rust string to C string
let rust_str = "Hello";
let c_string = CString::new(rust_str).unwrap();
let ptr: *const c_char = c_string.as_ptr();

// C string to Rust string
unsafe {
    let c_str = CStr::from_ptr(ptr);
    let rust_str = c_str.to_str().unwrap();
}
```

### Transmute

```rust
use std::mem::transmute;

// Reinterpret bits (very unsafe!)
let x: u32 = 42;
let y: f32 = unsafe { transmute(x) };

// Prefer safer alternatives when possible
let y = f32::from_bits(x);  // Safe!
```

### MaybeUninit

```rust
use std::mem::MaybeUninit;

// Uninitialized memory
let mut arr: [MaybeUninit<i32>; 3] = unsafe {
    MaybeUninit::uninit().assume_init()
};

// Initialize
arr[0].write(1);
arr[1].write(2);
arr[2].write(3);

// Convert to initialized
let arr: [i32; 3] = unsafe {
    std::mem::transmute(arr)
};
```

### Implementing Send and Sync

```rust
struct MyPointer(*mut i32);

// Tell compiler this is safe to send between threads
unsafe impl Send for MyPointer {}

// Tell compiler this is safe to share between threads
unsafe impl Sync for MyPointer {}
```

## Guidelines

### When to Use Unsafe

**Good reasons:**
- FFI with C libraries
- Performance-critical code where safe version is too slow
- Implementing low-level abstractions
- Hardware access
- Building safe abstractions that can't be expressed safely

**Bad reasons:**
- Avoiding borrow checker errors (fix your design instead)
- Premature optimization
- Not understanding safe alternatives

### Safety Documentation

```rust
/// Dereferences the given pointer.
/// 
/// # Safety
/// 
/// - `ptr` must be valid and properly aligned
/// - `ptr` must point to initialized memory
/// - No other code must be mutating the memory
pub unsafe fn read_ptr(ptr: *const i32) -> i32 {
    *ptr
}
```

### Minimize Unsafe Scope

```rust
// Bad: entire function is unsafe
unsafe fn process(data: *const u8, len: usize) -> Vec<u8> {
    let slice = std::slice::from_raw_parts(data, len);
    slice.to_vec()
}

// Good: minimal unsafe block
fn process(data: *const u8, len: usize) -> Vec<u8> {
    let slice = unsafe { 
        std::slice::from_raw_parts(data, len) 
    };
    slice.to_vec()  // Safe code outside unsafe block
}
```

## Tips

- Unsafe doesn't turn off the borrow checker
- Create safe abstractions around unsafe code
- Document safety requirements with `# Safety` doc comments
- Use `#[deny(unsafe_op_in_unsafe_fn)]` to require unsafe blocks even in unsafe functions
- Prefer safe alternatives: `from_bits` over `transmute`
- Use `MaybeUninit` for uninitialized memory
- Use Miri (`cargo miri`) to detect undefined behavior
- Test unsafe code extensively

## See Also

- [[Smart Pointers]] — Safe memory management
- [[Concurrency]] — Send and Sync traits
- [[Memory Types]] — Memory layout
- [[Rust]]
