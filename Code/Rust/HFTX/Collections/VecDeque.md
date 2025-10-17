- double-ended queue
    
- O(1) push_back / pop_front
    
- used in price levels for FIFO matching at a price
    
- avoids shifting like a `Vec` when popping front
  ```rust
  use std::collections::VecDeque;
let mut dq = VecDeque::new();
dq.push_back("order1");
dq.push_back("order2");
let first = dq.pop_front();
  ```