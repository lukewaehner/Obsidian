- `Vec` for compact, append-heavy lists
    
- `VecDeque` for queue semantics at price level (O(1) push_back / pop_front)
    
- `BTreeMap<i64, VecDeque<Order>>` for ordered price ladder
    
- `HashMap<OrderId, (price, pos)>` (optional) to support cancels/modify
[[Vec]]
[[VecDeque]]
[[BTreeMap]]
[[HashMap]]