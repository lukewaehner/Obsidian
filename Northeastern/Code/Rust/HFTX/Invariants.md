- Core invariants
    
    - No negative/zero `qty`
        
    - Prices in ticks within allowed range
        
    - `Bid` never matches at price `< best ask`; `Ask` never matches at `> best bid`
        
- Debug checks
```rust
debug_assert!(order.qty > 0);
debug_assert!(matches!(order.side, Side::Bid | Side::Ask));

```