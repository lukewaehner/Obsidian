- Prefer borrowing over cloning:
    
    - `&taker.symbol` when writing to logs/metrics
        
- When to `clone()`
    
    - Pushing owned `Order` into a deque
        
    - Emitting `Trade` with its own owned data if needed
        
- Consider `Arc<str>` for hot-path symbol deduplication