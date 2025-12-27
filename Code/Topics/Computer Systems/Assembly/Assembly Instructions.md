---
## Topic:
---
This note documents x86_64 instructions with syntax, categories, and examples.  
See [[Assembly Programming]] for broader context.

---

## Data Movement
### mov
Move data between operands.

```nasm
mov   Source, Destination
movq  Source, Destination   ; quad word (64-bit)
movb  Source, Destination   ; byte (8-bit)
```

**Operands**

- Immediate: `$42`, `$0x4F`
    
- Register: `%rax`
    
- Memory reference: `(%rax)`

```nasm
movq $52, %rax      ; load immediate into register
movq %rax, %rbx     ; copy register to register
```

## Arithmetic
### Two-operand instructions

- `add`, `sub`, `imul`, `idiv`
    
- `and`, `or`, `xor`, etc.
    
- General form:
    

`OP Source, Destination Destination = Destination OP Source`

**Examples**

`addq $3, %rax       ; rax = rax + 3 imul %rax, %rbx     ; rbx = rbx * rax`

### Unary instructions

- `inc` → increment
    
- `dec` → decrement
    
- `neg` → arithmetic negation
    
- `not` → bitwise inversion  
    The single operand is also the destination.
    

### Exercise

Translate `28 - (10 + 3) * 2`

```nasm
; Compute (10 + 3)
movq $10, %rax
movq $3, %rbx          ; optional
addq %rbx, %rax        ; result in rax

; Multiply by 2
imulq $2, %rax

; Subtract from 28
movq $28, %rbx
subq %rax, %rbx        ; result now in rbx
```
---
## Jumping and Labels

### Unconditional jump

`jmp label`

- Transfers execution to the given label (address).
    

### Labels

- A label marks a location in code:
    

```nasm
start:
    movq $1, %rax
    jmp end
end:
```

---

## Conditional Branching

### cmp

`cmp Sub, Min`

- Computes `Min - Sub` but discards the result
    
- Affects flags used by jump instructions
    

**Operands**

- Sub = subtrahend
    
- Min = minuend
    

### Conditional jumps

- `je` → jump if equal
    
- `jne` → jump if not equal
    
- `jg` → jump if Min > Sub
    
- `jge` → jump if Min ≥ Sub
    
- `jl` → jump if Min < Sub
    
- `jle` → jump if Min ≤ Sub
    

️ **Important**: In GNU assembly, sense is reversed:  
`cmp a, b` → compares `b - a`.

### Example
```nasm
movq $5, %rax
cmp $3, %rax      ; compares rax - 3
je equal_case
jne not_equal
```

---
## Calling Functions
`call` instruction.
- Takes one operands: address of the function's body
	- Most often we use a symbolic name to represent the address
- Calling the function printf, we need to know where arguments go, how the return value gets passed back to the caller.

### Arguments
The first 6 args are passed in these registers:

| Argument | Register |
| -------- | -------- |
| 1        | %rdi     |
| 2        | %rsi     |
| 3        | %rdx     |
| 4        | $rcx     |
| 5        | %r8      |
| 6        | %r9      |
> A separate step is required, the register `%al` needs to be set to 0, e.g.: `mov $0, %al`


---
### Code to Call Printf

```nasm
.global main       ; make 'main' visible to linker

main:
    movq $message, %rdi  ; pointer to format string
    movq $1, %rsi         ; first %ld value
    movq $2, %rdx         ; second %ld value
    movb $0, %al           ; tell printf there are 0 floating-point args 
    call printf             ; call printf

    movq $0, %rax           ; set return value to 0
    ret                     ; return from main

message:
    .asciz "value = %ld %ld\n"

```


- **`.global main`** → Declares `main` as a symbol visible to the linker so it can be used as the entry point.
    
- **`main:`** → Defines the `main` function label (the start of the code).
    
- **`movq $message, %rdi`** → Loads the _address_ of `message` (the format string) into `%rdi`, which is the first integer/pointer argument register according to the System V AMD64 ABI calling convention.
    
- **`movq $1, %rsi` and `movq $2, %rdx`** → Place the two integer values (1 and 2) into the second and third argument registers for `printf`.
    
- **`movb $0, %al`** → Sets the lower 8 bits of `%rax` to 0. In this ABI, before calling a variadic function like `printf`, `%al` must contain the number of floating-point arguments passed in XMM registers. Since none are passed here, it must be 0.
    
- **`call printf`** → Calls the `printf` function. It will use `%rdi`, `%rsi`, and `%rdx` as its arguments.
    
- **`movq $0, %rax`** → Sets return value of `main` to 0 (conventional success status).
    
- **`ret`** → Returns to the caller (the runtime).
    
- **`message:` / `.asciz "value = %ld %ld\n"`** → Defines a null-terminated string constant in the data section, used as the format string for `printf`.

---

## Register Saving Conventions 

###  Callee-Save Registers
- **Preserved across function calls** — the callee must restore their original values before returning.
- Registers:
  - `%rbx`
  - `%rbp` (base pointer)
  - `%r12`–`%r15`
- Try **not to modify `%rbp`** unless you are explicitly using it as a frame pointer.

---

### Caller-Save Registers
- **Not preserved across function calls** — the caller must save/restore them if needed after the call.
- Used as **temporary registers** for computations.
- Registers:
	- argument registers
	- `%rax`
	- `%r10`
	- `%r11`

---
# Structure of an Assembly File

> See [[Assembly File Structure]]