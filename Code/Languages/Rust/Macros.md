---
tags:
  - rust
  - macros
  - metaprogramming
type: note
related:
  - '[[Rust]]'
  - '[[Derives]]'
  - '[[Testing]]'
  - '[[Cargo]]'
---
# Macros

Metaprogramming through code generation in Rust.

## Overview

Macros write code that writes code. Rust has declarative macros (`macro_rules!`) for pattern-based generation and procedural macros for more complex transformations like custom derives.

## Basic Usage

### Using Built-in Macros

```rust
// Print macros
println!("Hello, {}!", name);
eprintln!("Error: {}", err);   // To stderr
dbg!(value);                   // Debug with file:line

// Format macro
let s = format!("{} is {}", name, age);

// Collection macros
let v = vec![1, 2, 3];
let arr = array![0; 10];  // [0, 0, 0, ...]

// Assertion macros
assert!(condition);
assert_eq!(left, right);
assert_ne!(left, right);
debug_assert!(condition);  // Only in debug builds

// Other common macros
todo!();         // Panics with "not yet implemented"
unimplemented!(); // Panics with "not implemented"
unreachable!();  // Marks unreachable code
panic!("message"); // Explicit panic
```

### Declarative Macros (macro_rules!)

```rust
// Simple macro
macro_rules! say_hello {
    () => {
        println!("Hello!");
    };
}

say_hello!();  // Prints "Hello!"

// With arguments
macro_rules! greet {
    ($name:expr) => {
        println!("Hello, {}!", $name);
    };
}

greet!("World");  // Prints "Hello, World!"
```

## Key Concepts

### Fragment Specifiers

```rust
macro_rules! example {
    // Expression
    ($e:expr) => { ... };
    
    // Identifier
    ($i:ident) => { ... };
    
    // Type
    ($t:ty) => { ... };
    
    // Pattern
    ($p:pat) => { ... };
    
    // Statement
    ($s:stmt) => { ... };
    
    // Block
    ($b:block) => { ... };
    
    // Item (function, struct, etc.)
    ($item:item) => { ... };
    
    // Literal
    ($l:literal) => { ... };
    
    // Token tree (anything)
    ($tt:tt) => { ... };
    
    // Path
    ($path:path) => { ... };
}
```

### Multiple Patterns

```rust
macro_rules! log {
    // No arguments
    () => {
        println!("[LOG]");
    };
    // Single expression
    ($msg:expr) => {
        println!("[LOG] {}", $msg);
    };
    // With level
    ($level:expr, $msg:expr) => {
        println!("[{}] {}", $level, $msg);
    };
}

log!();                    // [LOG]
log!("Starting");          // [LOG] Starting
log!("ERROR", "Failed");   // [ERROR] Failed
```

### Repetition

```rust
macro_rules! vec_of_strings {
    // Zero or more
    ($($element:expr),*) => {
        vec![$($element.to_string()),*]
    };
    
    // One or more
    ($($element:expr),+) => { ... };
    
    // Zero or one
    ($($element:expr)?)) => { ... };
}

let v = vec_of_strings!["a", "b", "c"];
// Expands to: vec!["a".to_string(), "b".to_string(), "c".to_string()]

// With separator
macro_rules! hashmap {
    ($($key:expr => $value:expr),* $(,)?) => {{
        let mut map = std::collections::HashMap::new();
        $(map.insert($key, $value);)*
        map
    }};
}

let map = hashmap! {
    "a" => 1,
    "b" => 2,
};
```

### Recursive Macros

```rust
macro_rules! count {
    () => { 0 };
    ($head:tt $($tail:tt)*) => { 1 + count!($($tail)*) };
}

let n = count!(a b c d);  // 4
```

## Common Patterns

### Builder-style DSL

```rust
macro_rules! html {
    ($tag:ident { $($inner:tt)* }) => {{
        let mut s = format!("<{}>", stringify!($tag));
        s.push_str(&html!($($inner)*));
        s.push_str(&format!("</{}>", stringify!($tag)));
        s
    }};
    ($text:expr) => {
        $text.to_string()
    };
    () => {
        String::new()
    };
}

let page = html!(div { "Hello" });
// "<div>Hello</div>"
```

### Test Generation

```rust
macro_rules! test_cases {
    ($($name:ident: $input:expr => $expected:expr),* $(,)?) => {
        $(
            #[test]
            fn $name() {
                assert_eq!(process($input), $expected);
            }
        )*
    };
}

test_cases! {
    test_empty: "" => "",
    test_hello: "hello" => "HELLO",
    test_world: "world" => "WORLD",
}
```

### Conditional Compilation Helper

```rust
macro_rules! cfg_if {
    ($(if #[cfg($cfg:meta)] { $($item:item)* })*) => {
        $(
            $(#[cfg($cfg)] $item)*
        )*
    };
}
```

## Procedural Macros

### Custom Derive

```rust
// In a proc-macro crate
use proc_macro::TokenStream;
use quote::quote;
use syn::{parse_macro_input, DeriveInput};

#[proc_macro_derive(MyTrait)]
pub fn my_trait_derive(input: TokenStream) -> TokenStream {
    let input = parse_macro_input!(input as DeriveInput);
    let name = input.ident;
    
    let expanded = quote! {
        impl MyTrait for #name {
            fn my_method(&self) -> String {
                stringify!(#name).to_string()
            }
        }
    };
    
    TokenStream::from(expanded)
}
```

```rust
// Usage
#[derive(MyTrait)]
struct Foo;

Foo.my_method()  // "Foo"
```

### Attribute Macros

```rust
#[proc_macro_attribute]
pub fn route(attr: TokenStream, item: TokenStream) -> TokenStream {
    // Transform the function
    // attr contains the attribute arguments
    // item contains the annotated item
    item
}
```

```rust
// Usage
#[route(GET, "/")]
fn index() -> &'static str {
    "Hello"
}
```

### Function-like Proc Macros

```rust
#[proc_macro]
pub fn sql(input: TokenStream) -> TokenStream {
    // Parse and transform
    input
}
```

```rust
// Usage
let query = sql!(SELECT * FROM users WHERE id = 1);
```

## Built-in Derive Macros

```rust
#[derive(Debug)]       // {:?} formatting
#[derive(Clone)]       // .clone() method
#[derive(Copy)]        // Implicit copying
#[derive(PartialEq)]   // == comparison
#[derive(Eq)]          // Total equality
#[derive(PartialOrd)]  // < > comparisons
#[derive(Ord)]         // Total ordering
#[derive(Hash)]        // Hashing
#[derive(Default)]     // Default::default()
```

## Tips

- Use `cargo expand` to see macro expansions
- Macros are hygienic—they don't pollute namespaces
- `macro_rules!` is simpler but less powerful than proc macros
- Use `$crate::` to refer to items from your crate in macros
- Proc macros must be in their own crate with `proc-macro = true`
- Use `quote` and `syn` crates for proc macro development
- Test macros with `cargo expand` and trybuild

## See Also

- [[Derives]] — Common derive macros
- [[Testing]] — Test generation macros
- [[Cargo]] — Proc macro crate setup
- [[Rust]]
