---
tags:
  - rust
  - types
  - patterns
type: note
related:
  - "[[Rust]]"
  - "[[Pattern Matching]]"
  - "[[Structs]]"
  - "[[Enums]]"
  - "[[Slices]]"
---
# Destructuring

Unpacking values out of compound types using patterns.

## Tuples

```rust
let point = (3, 7);
let (x, y) = point;        // x = 3, y = 7

let rgb = (255, 128, 0);
let (r, g, b) = rgb;

// Ignore fields with _
let (first, _, third) = (1, 2, 3);

// In function parameters
fn print_point(&(x, y): &(i32, i32)) {
    println!("{}, {}", x, y);
}
```

## Arrays & Slices

```rust
// Fixed-size array — must match exactly
let [a, b, c] = [1, 2, 3];

// Slice patterns with rest (..)
let v = vec![1, 2, 3, 4, 5];
if let [first, rest @ ..] = v.as_slice() {
    println!("first: {}, rest: {:?}", first, rest);
}

// Match head and tail
if let [first, .., last] = v.as_slice() {
    println!("first: {}, last: {}", first, last);
}

// Exact length required for irrefutable
let arr = [10, 20, 30];
let [x, y, z] = arr;   // x=10, y=20, z=30
```

## Structs

```rust
struct Point { x: i32, y: i32 }

let p = Point { x: 3, y: 7 };

// Destructure into variables matching field names
let Point { x, y } = p;

// Rename while destructuring
let Point { x: px, y: py } = p;

// Ignore remaining fields
struct Config { host: String, port: u16, timeout: u64 }
let Config { host, .. } = config;   // only extract host
```

### In match

```rust
match p {
    Point { x: 0, y } => println!("on y-axis at {}", y),
    Point { x, y: 0 } => println!("on x-axis at {}", x),
    Point { x, y }    => println!("at ({}, {})", x, y),
}
```

### Nested structs

```rust
struct Line { start: Point, end: Point }

let Line { start: Point { x: x1, y: y1 }, end: Point { x: x2, y: y2 } } = line;
```

### Grabbing both layers
```rust
 #[derive(Debug)]
  struct Point {
      x: f64,
      y: f64,
  }

  #[derive(Debug)]
  struct Line {
      start: Point,
      end: Point,
  }

  fn main() {
      let line = Line {
          start: Point { x: 0.0, y: 0.0 },
          end:   Point { x: 3.0, y: 4.0 },
      };

      // `start @ Point { ... }` binds the
   whole Point *and* destructures it.
      // Because we destructure `&line`,
  every binding is a reference:
      //   start, end : &Point
      //   x1, y1, x2, y2 : &f64
      let Line {
          start: start @ Point { x: x1, y:
   y1 },
          end:   end   @ Point { x: x2, y:
   y2 },
      } = &line;

      let dx = x2 - x1;
      let dy = y2 - y1;
      let length = (dx * dx + dy *
  dy).sqrt();

      println!("start: {:?}", start);
      println!("end:   {:?}", end);
      println!("({x1}, {y1}) -> ({x2},
  {y2}), length = {length}");

      // line is untouched
      println!("{:?}", line);
  }

```

## Enums

```rust
enum Message {
    Quit,
    Move { x: i32, y: i32 },
    Write(String),
    Color(u8, u8, u8),
}

match msg {
    Message::Quit                 => println!("quit"),
    Message::Move { x, y }       => println!("move to {},{}", x, y),
    Message::Write(text)          => println!("write: {}", text),
    Message::Color(r, g, b)       => println!("color: {},{},{}", r, g, b),
}
```

### if let for single variant

```rust
if let Message::Write(text) = msg {
    println!("{}", text);
}

// With guard
if let Message::Move { x, y } = msg if x > 0 {
    println!("moving right to {},{}", x, y);
}
```

### let-else to extract or return

```rust
fn get_text(msg: Message) -> String {
    let Message::Write(text) = msg else {
        return String::new();
    };
    text
}
```

## References

Destructuring through references — the `&` must mirror the pattern:

```rust
let points = vec![Point { x: 1, y: 2 }, Point { x: 2, y: 3}];

// &Point comes from iter(), match with &
for &Point { x, y } in &points { }

// Or use ref in the pattern
for Point { x, y } in &points { }   // x and y are &i32
```

## Nested & Complex

```rust
let ((a, b), c) = ((1, 2), 3);

// Mixed: enum containing struct
enum Shape {
    Circle { center: Point, radius: f64 },
    Rect(Point, Point),
}

match shape {
    Shape::Circle { center: Point { x, y }, radius } => { }
    Shape::Rect(Point { x: x1, .. }, Point { x: x2, .. }) => { }
}
```

## @ Bindings

Name a value while also testing it:

```rust
match value {
    n @ 1..=9  => println!("single digit: {}", n),
    n @ 10..=99 => println!("double digit: {}", n),
    n           => println!("large: {}", n),
}

// Bind inside enum variant
match msg {
    Message::Write(text @ ref s) if s.len() > 10 => println!("long: {}", text),
    Message::Write(text) => println!("short: {}", text),
    _ => {}
}
```

## In Function Parameters

```rust
fn sum(&(a, b): &(i32, i32)) -> i32 { a + b }

fn print_coords(&Point { x, y }: &Point) {
    println!("{}, {}", x, y);
}

// Closures too
let pairs = vec![(1, 2), (3, 4)];
pairs.iter().map(|(a, b)| a + b).collect::<Vec<_>>();
```

## Tips

- `..` ignores remaining fields in structs or middle elements in slices
- `_` ignores a single field without binding it
- Slice patterns (`[first, rest @ ..]`) require a `match` or `if let` — they're refutable
- Use `let-else` to destructure and early-return in one line
- Nested destructuring works but gets hard to read — consider splitting into multiple `let`s

## See Also

- [[Pattern Matching]] — Match expressions, guards, exhaustiveness
- [[Slices]] — Array and slice operations
- [[Structs]] — Struct types
- [[Enums]] — Enum types
- [[Rust]]
