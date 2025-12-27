---
tags:
  - rust
  - strings
  - utf8
type: note
related:
  - '[[Rust]]'
  - '[[Collections]]'
  - '[[Iterators]]'
  - '[[Memory Types]]'
---
# Strings

String types, UTF-8 handling, and text manipulation in Rust.

## Overview

Rust has two main string types: `String` (owned, growable, heap-allocated) and `&str` (borrowed string slice). Both are UTF-8 encoded, which affects how you index and iterate over them.

## Basic Usage

### String vs &str

```rust
// String - owned, mutable, heap-allocated
let mut s = String::from("hello");
s.push_str(" world");

// &str - borrowed slice, immutable
let slice: &str = "hello";  // String literal (static)
let slice: &str = &s;       // Borrow from String
let slice: &str = &s[0..5]; // Substring slice
```

### Creating Strings

```rust
// From literal
let s = String::from("hello");
let s = "hello".to_string();
let s = "hello".to_owned();

// Empty
let s = String::new();

// With capacity
let s = String::with_capacity(100);

// From other types
let s = 42.to_string();
let s = format!("{} + {} = {}", 2, 2, 4);

// From bytes (must be valid UTF-8)
let s = String::from_utf8(vec![104, 101, 108, 108, 111]).unwrap();

// From chars
let s: String = ['h', 'e', 'l', 'l', 'o'].iter().collect();
```

## Key Concepts

### UTF-8 Encoding

Strings are UTF-8, so characters can be 1-4 bytes:

```rust
let s = "hello";
s.len();         // 5 bytes

let s = "Здравствуйте";  // Russian
s.len();         // 24 bytes (not 12 characters!)
s.chars().count();  // 12 characters

// Cannot index directly
// let c = s[0];  // Error! Would be in middle of character

// Use chars() or bytes()
let first: char = s.chars().next().unwrap();
let first_byte: u8 = s.bytes().next().unwrap();
```

### Slicing Strings

```rust
let s = "hello world";

// Byte-based slicing (must be on char boundaries!)
let hello = &s[0..5];   // "hello"
let world = &s[6..11];  // "world"

// Panic if not on char boundary
let s = "Здравствуйте";
// let bad = &s[0..1];  // Panic! 'З' is 2 bytes

// Safe slicing
let safe = &s[0..2];    // "З" (first character, 2 bytes)
```

### String Modification

```rust
let mut s = String::from("hello");

// Append
s.push(' ');            // Single char
s.push_str("world");    // String slice
s += "!";               // Concat with +

// Insert
s.insert(5, ',');       // Insert char at byte index
s.insert_str(6, " dear"); // Insert str at byte index

// Remove
s.pop();                // Remove last char
s.truncate(5);          // Keep first 5 bytes
s.clear();              // Empty the string

// Replace
let s = "hello".replace("l", "L");  // "heLLo"
let s = "hello".replacen("l", "L", 1);  // "heLlo"
```

## Common Patterns

### Concatenation

```rust
// format! - most flexible
let s = format!("{} {}", "hello", "world");

// + operator (consumes left operand)
let s1 = String::from("hello");
let s2 = String::from(" world");
let s3 = s1 + &s2;  // s1 is moved, s2 is borrowed

// push_str for building
let mut s = String::new();
s.push_str("hello");
s.push_str(" world");

// collect from iterator
let s: String = vec!["hello", " ", "world"].into_iter().collect();

// join
let s = ["hello", "world"].join(" ");  // "hello world"
```

### Parsing and Converting

```rust
// Parse from string
let n: i32 = "42".parse().unwrap();
let n: f64 = "3.14".parse().unwrap();

// Handle parse errors
match "not a number".parse::<i32>() {
    Ok(n) => println!("Parsed: {}", n),
    Err(e) => println!("Error: {}", e),
}

// To string
let s = 42.to_string();
let s = format!("{:.2}", 3.14159);  // "3.14"
```

### Iteration

```rust
let s = "hello 世界";

// By char
for c in s.chars() {
    println!("{}", c);  // h, e, l, l, o,  , 世, 界
}

// By byte
for b in s.bytes() {
    println!("{}", b);  // 104, 101, 108, 108, 111, 32, 228, 184, ...
}

// With indices (byte positions)
for (i, c) in s.char_indices() {
    println!("{}: {}", i, c);
}

// By grapheme clusters (needs unicode-segmentation crate)
// use unicode_segmentation::UnicodeSegmentation;
// for g in s.graphemes(true) { ... }
```

### Searching

```rust
let s = "hello world";

s.contains("world");           // true
s.starts_with("hello");        // true
s.ends_with("world");          // true

s.find("world");               // Some(6) - byte index
s.rfind("o");                  // Some(7) - last occurrence

// Split
let words: Vec<&str> = s.split(' ').collect();
let parts: Vec<&str> = "a,b,c".split(',').collect();
let lines: Vec<&str> = "a\nb\nc".lines().collect();
```

### Trimming and Case

```rust
let s = "  hello  ";
s.trim();        // "hello"
s.trim_start();  // "hello  "
s.trim_end();    // "  hello"

let s = "hello";
s.to_uppercase();  // "HELLO"
s.to_lowercase();  // "hello"

// Trim specific chars
"##hello##".trim_matches('#');  // "hello"
```

### Common Methods Table

| Method | Description | Example |
|--------|-------------|---------|
| `len()` | Byte length | `"hello".len()` → `5` |
| `is_empty()` | Check if empty | `"".is_empty()` → `true` |
| `chars()` | Iterator over chars | `"hi".chars()` |
| `bytes()` | Iterator over bytes | `"hi".bytes()` |
| `split(pat)` | Split by pattern | `"a,b".split(',')` |
| `lines()` | Split by newlines | `"a\nb".lines()` |
| `contains(pat)` | Check contains | `"hello".contains("ell")` |
| `replace(from, to)` | Replace all | `"aa".replace("a", "b")` |
| `trim()` | Remove whitespace | `" hi ".trim()` |

## Function Parameters

```rust
// Accept &str for maximum flexibility
fn greet(name: &str) {
    println!("Hello, {}!", name);
}

greet("world");              // &str literal
greet(&String::from("world")); // &String coerces to &str
greet(&"world".to_string()); // Same

// Use String when you need ownership
fn take_ownership(s: String) {
    // s is owned here
}
```

## Tips

- Use `&str` in function parameters to accept both `&String` and `&str`
- Use `String` when you need to own or modify the string
- Remember: `len()` returns bytes, not characters
- Use `chars().count()` for character count
- Be careful with slicing—must be on UTF-8 boundaries
- Use `format!` for complex string building
- Prefer `push_str` over `+` in loops (avoids allocations)

## See Also

- [[Collections]] — String is like Vec<u8> with UTF-8 guarantee
- [[Iterators]] — String iteration patterns
- [[Memory Types]] — String heap allocation
- [[Rust]]
