
# bootmain.c

`bootmain.c` is the second stage of the XV6 boot sequence and the first C code that runs. It's responsible for loading the actual kernel into memory.

## Purpose

After `bootasm.s` sets up a minimal C runtime environment, `bootmain.c` reads the kernel from disk and loads it into memory at the correct location.

## Responsibilities

1. **Read Kernel from Disk:**
   - Accesses the disk using simple I/O port operations
   - Reads kernel executable (ELF format)
   - No file system at this stage, just raw disk sectors

2. **Parse ELF Header:**
   - Reads the ELF (Executable and Linkable Format) header
   - Determines where each section should be loaded in memory
   - ELF describes program structure and entry point

3. **Load Kernel Segments:**
   - Copies kernel code and data into memory
   - Places each segment at its designated memory address
   - Prepares the kernel for execution

4. **Transfer Control:**
   - Jumps to the kernel's entry point
   - Next stage is `entry.s`

## Why C at This Stage

C code is now possible because `bootasm.s` has:
- Set up a stack
- Configured protected mode
- Created an environment where C calling conventions work

However, this is still very limited C with no standard library or OS services.

## Cross References

- [[XV6 Boot Sequence]]
- [[bootasm.s]]
- [[OS Boot Process]]
