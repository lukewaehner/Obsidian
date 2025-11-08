---
## Topic:
---
---

### Main Memory Model

- Main memory ≈ giant byte array: addresses from `0` to `2^64 - 1`.
    
- Assembly rarely uses absolute addresses — uses registers or labels.
    

```nasm
movq $1234, (%rax)    ; store 1234 at address in %rax 
movq (%rax), %rbx     ; load value from address in %rax into %rbx
```

- Can add **offsets** (displacement):
    

```nasm
movl -8(%rax), %ebx   ; load 4 bytes from %rax-8 
movl %ebx, 4(%rax)    ; store to %rax+4
```

️ Cannot move memory→memory in one instruction:

```nasm
movl -8(%rax), 4(%rax) ;  invalid
```

---

### Base-Index-Scale Addressing

For arrays of fixed-size elements:

```nasm
movl (%rax,%rbx,4), %ecx
```
- `%rax` = base (array start)
    
- `%rbx` = index
    
- `4` = scale (element size)
    

---

### Program Address Space Layout

```diff
High addr 
+---------------------------+ 
| Env vars & args           | 
+---------------------------+ 
| STACK (grows ↓)           | 
| ...                       | 
| HEAP (grows ↑)            | 
+---------------------------+
| .bss (uninitialized)      |
+---------------------------+
| .data (initialized)       |
+---------------------------+
| .text (code)              |
+---------------------------+
| OS stuff                  |
Low addr
```
