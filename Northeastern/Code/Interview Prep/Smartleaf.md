### **1. Targeted Focus**

  

They want to see:

- You can **implement** a small structure (e.g., ArrayList, HashMap, queue) cleanly.
    
- You can **walk through your own code**, catching bugs and edge cases as you go.
    
- You can reason about **complexity and correctness**, not just syntax.
    

  

Expect the prompt to be:

|**Structure**|**Core operations**|**Edge cases to mention**|
|---|---|---|
|**Dynamic Array (ArrayList)**|append, get, resize|resizing when full/empty|
|**HashMap (Separate Chaining)**|put, get, delete|duplicate keys, hash collisions|
|**Queue (Circular Array)**|enqueue, dequeue|wrap-around, full vs empty|
|**Stack**|push, pop|underflow|
|**LRU Cache**|get, put|eviction policy, capacity 0|
  

> “Implement a simplified version of X in your preferred language and explain your design as you go.”

---

### **2. Practice these structures (Python version)**

  

They are easy to reason about in interview format:


You already have robust templates from earlier; know them cold and narrate like:

  

> “I’ll store items in an array and double capacity on overflow — that ensures amortized O(1) append. Edge case: shrinking to half only when usage < 25%.”

---

### **3. “Explain as you go” Strategy**

  

They’ll probe your reasoning, not the final code. While typing, verbalize:

- **Intent**: “This helper resizes when we exceed capacity.”
    
- **Invariant**: “Size ≤ capacity always.”
    
- **Complexity**: “Each append is O(1) amortized; resize is O(n).”
    
- **Edge Case**: “We must avoid underflow when popping an empty list.”
    
- **Test mental run**: “If I append 5 elements to a capacity-4 array, we trigger resize to 8.”
    

---

### **4. Review/Debug Component**

  

They may show you code and ask what’s wrong. Be ready to:

- Spot **off-by-one** errors in index handling.
    
- Notice **mutability** issues (e.g., shared list reference in Python).
    
- Explain **why** something has unexpected complexity (e.g., list.pop(0) = O(n)).
    
- Suggest a **fix** while explaining tradeoffs.
    

---

### **5. Minimal background topics**

  

Because Smartleaf’s stack includes Rails, PostgreSQL, and React:

- Know what **MVC** means (Model–View–Controller).
    
- Know the purpose of an **ORM** (maps DB rows to objects).
    
- Know how **REST APIs** work (endpoint, JSON response).
    
    They may use these as follow-ups to test broad literacy.
    

---

### **6. Simulation plan**

  

**Before interview:**

1. Implement a hashmap, dynamic array, and queue from scratch in Python.
    
2. Run them manually with small data to trace behavior.
    
3. Practice “thinking aloud” while coding.
    
4. Review O(1) vs. O(n) for all operations.
    

  

**In interview:**

- Ask clarifying question: “Do you want a working version or pseudocode-level?”
    
- Write concise, readable code.
    
- Explain invariants and corner cases as you type.
    
- Offer a 1–2 sentence postmortem after running through an example.
    

---

Would you like a one-page cheat sheet summarizing what to say for each of the five likely data structures (intent, invariant, complexity, edge cases)? It’s ideal for rapid recall right before the interview.