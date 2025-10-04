- Method receivers
    
    - `&self` read-only queries (`best_price`)
        
    - `&mut self` mutating ops (`pop_best`, `add`, `submit_limit`)
        
- Temporary mut borrows
    
    - Limit borrow scope with blocks so you can borrow again later
        
- Avoid moving large data accidentally
    
    - Pass `&str` vs `String` where possible
        
    - Clone only at boundaries that truly need ownership