---
## Topic:
---
### The Stack vs Heap

- **Heap**
    
    - For dynamic memory (malloc/new)
        
    - Grows upward (toward higher addresses)
        
    - Manual allocation + freeing
        
- **Stack**
    
    - For local variables, function calls
        
    - Grows downward (toward lower addresses)
        
    - Auto freed on return
        

Registers:

- `%rsp` — stack pointer (top of stack)
    
- `%rbp` — base pointer (start of frame)
    

---

### Stack Frames

- Created on function call
    
- Released on return
    
- Set up using:
    

```nasm
enter $16, $0        
; make a frame with 16 bytes 
; equivalent to: 
pushq %rbp movq %rsp, %rbp
```
- Tear down using:
    

```nasm
leave                 
; equivalent to: 
movq %rbp, %rsp 
popq %rbp
```

- Locals stored as negative offsets from `%rbp`:
    

```
movq $42, -8(%rbp)    ; a = 42 
movq $1, -16(%rbp)    ; b = 1 
addq $12, -16(%rbp)   ; b += 12
```

---

### Writing Functions (Assembly Design Recipe)

>  see also `[[Assembly Instructions]]` and `[[Assembly Programming]]`

**Structure:**

`# long double(long x) # x -> %rdi double:   enter $0, $0        ; prologue   movq %rdi, %rax   addq %rdi, %rax      ; body   leave   ret                  ; epilogue`

**`ret`** jumps to return address saved on stack by the `call` instruction.

**Design Steps:**

1. Signature
    
2. Pseudocode
    
3. Variable mappings
    
4. Skeleton (prologue/epilogue)
    
5. Body
    

---

### Recursive Example: Factorial

**Pseudocode**

`long fact(long n){   if (n < 2) return 1;   else return n * fact(n-1); }`

**Skeleton**

`# n -> %rsi fact:   enter $0, $0   ; body   leave   ret`

(Use call to `fact` recursively; push args and handle base case)
See: [[Memory & Addressing]]
