# CS3650 - Computer Systems

**Course Focus**: Understanding how computer systems work from the ground up - assembly language, C programming, operating system concepts, and hardware-software interaction.

 [Course Website](https://khoury-cs3650.github.io)

##  Core Topics

### Fundamentals

#### Low-Level Programming
- **Terminal & Command Line**: Heavy terminal usage for system interaction
- **[[Assembly]]**: x86-64 assembly language (Intel architecture)
- **[[C]]**: Systems programming language
- **Compiler Toolchain**: gcc, make, debugging tools

#### Hardware Architecture
- **[[CPU Basics]]**: Processor architecture and execution
- **[[Data & Registers]]**: Data representation and register usage
- **[[Number Bases]]**: Binary, hexadecimal, and data encoding

### Operating System Concepts

#### CPU Virtualization
**[[Processes]]** - Running programs and process management
- Process creation and lifecycle
- Process control and communication
- Context switching

#### [[Memory Virtualization]]
Efficient and protected use of main memory
- Virtual memory and address spaces
- Memory protection mechanisms
- Paging and segmentation
- Memory allocation strategies

#### [[Concurrency]]
Parallel execution and synchronization
- **Threads**: Lightweight processes
- **Synchronization Primitives**: Locks, mutexes, semaphores
- **Parallelism**: Multi-threaded programming
- **Race Conditions**: Avoiding data races
- **Deadlock**: Detection and prevention

#### Persistence
Long-term data storage
- **Storage Devices**: Hard drives, SSDs
- **File Systems**: Organization and access
- **File I/O**: Reading and writing data

### Development Tools
- **Debugging**: gdb, valgrind, debugging techniques
- **Instrumentation**: Performance analysis and profiling
- **Build Systems**: Makefiles and compilation

##  Detailed Topics

### Assembly Language
**[[Assembly]]** subfolder contains:
- Instruction set architecture
- Registers and addressing modes
- Control flow in assembly
- Function calls and stack frames
- [[Stack & Functions]] - Stack management

### C Programming
**[[C]]** subfolder contains:
- C syntax and semantics
- Pointers and memory management
- Structs and arrays
- Dynamic memory allocation
- System calls

### Process Management
**[[Processes]]** subfolder contains:
- Process API (fork, exec, wait)
- Process scheduling
- Inter-process communication (IPC)

### Memory Systems
**[[Memory Virtualization]]** subfolder contains:
- Address translation
- Page tables
- TLB (Translation Lookaside Buffer)
- Swapping and paging

### Concurrent Programming
**[[Concurrency]]** subfolder contains:
- Thread API (pthread)
- Mutual exclusion
- Condition variables
- Lock implementations
- Concurrent data structures

##  Key Concepts

### The System Stack
- Function call overhead
- Stack frames and activation records
- Calling conventions
- [[Stack & Functions]]

### Memory Hierarchy
```
Registers (fastest, smallest)
    ↓
L1 Cache
    ↓
L2 Cache
    ↓
L3 Cache
    ↓
Main Memory (RAM)
    ↓
Disk Storage (slowest, largest)
```

### Abstraction Layers
```
Application Programs
    ↓
System Libraries
    ↓
Operating System
    ↓
Hardware
```

##  Learning Objectives

1. **Low-Level Programming**: Write efficient C and assembly code
2. **System Understanding**: Understand how hardware and OS interact
3. **Performance**: Analyze and optimize system performance
4. **Concurrency**: Write correct concurrent programs
5. **Debugging**: Debug complex systems-level issues

## ️ Tools & Technologies

**Languages**: C, x86-64 Assembly
**Compilers**: gcc, clang
**Debuggers**: gdb, lldb
**Memory Tools**: valgrind, AddressSanitizer
**Build Tools**: make, cmake
**Version Control**: git

##  Major Themes

### 1. Hardware-Software Interface
Understanding how software runs on real hardware
- Instruction execution
- Memory addressing
- I/O operations

### 2. Abstraction & Virtualization
OS provides abstractions over hardware
- Virtual memory
- Virtual CPU (processes)
- Virtual storage (file systems)

### 3. Performance & Efficiency
Making programs fast and resource-efficient
- Cache-friendly code
- Avoiding system call overhead
- Lock-free data structures

### 4. Correctness & Safety
Writing bug-free systems code
- Memory safety
- Thread safety
- Resource management

##  Related Topics

### From Other Courses
- [[Algorithms]] - Algorithm implementation efficiency
- [[DSA]] - Data structure implementation
- [[OOD]] - Higher-level design patterns

### Advanced Topics
- Operating system implementation
- Network systems
- Distributed systems
- Computer architecture

##  Study Resources

### Core Concepts
- [[Number Bases]] - Binary, hex, data representation
- [[CPU Basics]] - Processor fundamentals
- [[Data & Registers]] - Data types and registers
- [[Stack & Functions]] - Call stack and functions

### Implementation
- [[Assembly]] - Low-level programming
- [[C]] - Systems programming language

### OS Concepts  
- [[Processes]] - Process management
- [[Memory Virtualization]] - Virtual memory
- [[Concurrency]] - Parallel programming

---

**Course Number**: CS3650
**Prerequisites**: Data Structures, Computer Organization
**Topics**: Systems Programming, Operating Systems, Assembly, C, Concurrency