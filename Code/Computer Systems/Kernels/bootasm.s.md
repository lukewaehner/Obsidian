
# bootasm.s

`bootasm.s` is the first code that executes in the XV6 boot sequence. It's written in assembly language and handles low-level processor initialization.

## Purpose

This boot assembly code transitions the processor from the limited 16-bit mode that BIOS uses into the more capable 32-bit protected mode that the kernel needs.

## 16-bit vs 32-bit Mode

**16-bit Real Mode (BIOS default):**
- Limited to 1 MB of addressable memory
- Uses segment:offset addressing
- No memory protection
- Backward compatible with original 8086 processor

**32-bit Protected Mode:**
- Can address 4 GB of memory
- Uses flat memory model
- Hardware memory protection
- Required for modern operating systems

## Address Space Expansion

The code enables an extra address line to get 20-bit addresses instead of 16-bit, expanding accessible memory.

**Address Line Math:**
- 16-bit addresses: 2^16 = 64 KB per segment
- 20-bit addresses: 2^20 = 1 MB (original PC limit)
- 32-bit addresses: 2^32 = 4 GB

This expansion was the A20 line, named because it was the 21st address line (lines are numbered from 0).

## Key Responsibilities

1. Enable A20 gate for extended addressing
2. Load Global Descriptor Table (GDT)
3. Switch from real mode to protected mode
4. Set up segment registers
5. Jump to `bootmain.c`

## Cross References

- [[XV6 Boot Sequence]]
- [[bootmain.c]]
- [[OS Boot Process]]
