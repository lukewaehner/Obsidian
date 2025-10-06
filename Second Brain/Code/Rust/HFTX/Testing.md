Unit tests colocated
```rust
#[cfg(test)]
mod tests {
  use super::*;
  #[test]
  fn bid_crosses_ask() {
    // setup book, add maker ask, submit taker bid, assert trades & rests
  }
}
```
- Property ideas
    
    - Conservation: total filled qty ≤ submitted qty
        
    - Price-time priority: earlier maker fills first at same price
        
- Use `assert_eq!`, `assert!`, and pattern matches