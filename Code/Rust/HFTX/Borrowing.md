### By value
Passing in value changes ownership (the borrow facade)
```rust
fn foo(val: String) {
	println!("{}", val)
}
let s = String::from("hi")
foo(s) // Prints s
foo(s) // Print is gone now, and can't be used
```

### Shared Borrow
```rust
fn foo(val: &String) {
	println!("{}", val)
}
let s = String::from("hi")
foo(&s) // Prints s
foo(&s) // Prints s, s is not borrowed
```

### Mutable borrow
```rust
fn foo(val: &mut String) {
	if (val == "hello") {
		println!("I got this already and changed it");
		return;
	}
	if (val == "hi") {
		val = "hello";
	}
	
	println!("{}", val);
}
let s = String::from("hi");
println!("{}", s); // hi
foo(s); // Prints hello
println!("{}", s); // 
```

---
[[Borrowing & Mutability in Methods]]
[[Cloning vs Referencing]]