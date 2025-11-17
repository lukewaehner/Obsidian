
# XV6 Boot Sequence

XV6 is a teaching operating system developed at MIT. Its boot sequence follows a specific chain of code execution.

## Boot Chain

The XV6 system loads up through this process:

**bootasm.s → bootmain.c → entry.s → main**

Each stage prepares the system for the next stage, eventually reaching the main kernel code.

## Stage Details

### 1. bootasm.s
- First code that executes after BIOS loads the MBR
- Written in assembly language
- Handles processor mode transitions
- Sets up minimal environment for C code

### 2. bootmain.c
- First C code in the boot sequence
- Loads the kernel from disk into memory
- Prepares to transfer control to kernel

### 3. entry.s
- Assembly code that sets up the kernel environment
- Configures page tables and stack
- Transitions to kernel proper

### 4. main
- Main kernel initialization function
- Sets up system tables, devices, and processes
- System is fully operational after main completes

## Why This Sequence

The progression from assembly to C to kernel reflects increasing levels of abstraction and capability. Early boot code must be in assembly because C requires a runtime environment that doesn't exist yet. Each stage builds the foundation for the next.

## Cross References

- [[OS Boot Process]]
- [[MBR]]
- [[bootasm.s]]
- [[bootmain.c]]
