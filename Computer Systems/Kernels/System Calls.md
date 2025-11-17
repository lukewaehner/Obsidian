
# System Calls

System calls are the interface between user space and kernel space. They provide a controlled way for user programs to request services from the operating system.

## Purpose

System calls allow user programs to:
- Request OS services without direct hardware access
- Maintain system security and stability
- Access privileged operations in a controlled manner

## How They Work

When a user program needs to perform a privileged operation, it:
1. Makes a system call (e.g., `sbrk()`)
2. CPU switches from user mode to kernel mode
3. Kernel validates the request and performs the operation
4. Control returns to user space with the result

## Example System Calls

**`sbrk()` (set program break):**
- Adjusts the program's data segment size
- Used for dynamic memory allocation
- Expands or contracts the heap

## Cross References

- [[Kernel Architecture]]
- [[Monolithic Kernel]]
- [[Processes]]
