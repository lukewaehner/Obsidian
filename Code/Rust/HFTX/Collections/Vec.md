- contiguous, growable array on heap
    
- O(1) push/pop at end (amortized)
    
- great for compact, append-heavy lists
    
- access by index O(1)
```rust
let mut v = Vec::new();
v.push(10);
println!("{}", v[0]);
```