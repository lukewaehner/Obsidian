
# Monolithic Kernel

A monolithic kernel is an operating system architecture where the entire OS runs in kernel space as a single large process.

## Architecture

### Kernel Space Components

**Memory Manager:**
- Handles virtual memory and physical memory allocation
- Manages page tables and memory protection

**Scheduler:**
- Decides which process runs on the CPU and when
- Implements scheduling algorithms and context switching

**Device Drivers:**
- Makes devices do things
- Provides abstraction layer between hardware and OS
- Each device type has its own driver

**File Systems:**
- Manages how data is stored and retrieved from disk
- XV6 has one file system, Linux supports many

**Program Loader:**
- Takes executables and puts them into memory
- Prepares the process for execution

### User Space Components

- App1
- App2
- Commands
- All user applications and utilities

## System Call Interface

Both kernel and user space map to the API through:
- System calls
- Interface functions like `sbrk()`

System calls are the controlled entry points from user space into kernel space, allowing applications to request OS services.

## Cross References

- [[Kernel Architecture]]
- [[System Calls]]
- [[Device Drivers]]
- [[Program Loader]]
- [[File Systems]]
