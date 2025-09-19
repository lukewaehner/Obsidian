---
## Topic:
---
---
## Compilation steps

hello.c → Preprocessor → hello.i  
→ Compiler → hello.s  
→ Assembler → hello.o  
→ Linker → hello (executable)


- **Compiler** → turns C into assembly (mnemonics)
- **Assembler** → converts mnemonics into machine code (0s and 1s)
- **Linker** → combines object files into final binary

> Assemblers are simple and often give poor error feedback.

---

## Other languages
- Languages like Python and Java compile to **bytecode** for a **virtual machine**
- Examples:
  - JVM instructions (Java)
  - Python bytecode / `dis` module

---

## Links
- [[CPU Basics]]
- [[Assembly Programming]]
