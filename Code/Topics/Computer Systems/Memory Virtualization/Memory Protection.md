

## Overview

**Memory protection** mechanisms prevent processes from accessing memory they shouldn't, ensuring system security and stability.

**Goals:**
- Isolate processes from each other
- Protect kernel memory from user processes
- Prevent unauthorized access to data
- Enable controlled sharing when desired

---

## Permission Bits

Page table entries contain permission bits that control access:

### Standard Permission Bits

**R (Read)**
- Process can read from this page
- Load instructions allowed

**W (Write)**
- Process can write to this page
- Store instructions allowed

**X (Execute)**
- Process can execute code from this page
- Fetch instructions allowed

**U/S (User/Supervisor)**
- User bit: User-mode programs can access
- Supervisor bit: Only kernel can access

---

## Memory Segment Permissions

Different memory regions have different permission requirements:

### Code Segment
```
Permissions: R + X (Read and Execute)
             NO Write

Why? 
- Need to read instructions
- Need to execute instructions
- Should NOT modify code (security)
```

**Attempting to write to code:**
```c
void foo() {
    // Try to modify function code
    char *code = (char*)foo;
    *code = 0x90;  // Segmentation fault!
}
```

### Data Segment
```
Permissions: R + W (Read and Write)
             NO Execute

Why?
- Need to read data
- Need to write data
- Should NOT execute data (security)
```

### Stack
```
Permissions: R + W (Read and Write)
             NO Execute

Why?
- Need to read local variables
- Need to write local variables
- Should NOT execute stack (prevents attacks)
```

### Heap
```
Permissions: R + W (Read and Write)
             NO Execute

Why?
- Need to read allocated data
- Need to write allocated data
- Should NOT execute heap (security)
```

---

## Protection Violations

### Types of Violations

**1. Invalid Address Access**
- Accessing memory that doesn't belong to process
- Valid bit = 0 in page table
- **Result:** Page fault → Segmentation fault

**2. Permission Violation**
- Attempting operation without proper permissions
- Examples:
  - Writing to read-only page
  - Executing non-executable page
  - User accessing kernel page
- **Result:** Protection fault → Segmentation fault

**3. Examples**

```c
// Writing to read-only data
const int x = 42;
int *p = (int*)&x;
*p = 100;  // Segmentation fault! (write to read-only)

// Executing data
char data[] = {0x90, 0x90, 0xC3};  // Some bytes
void (*func)() = (void(*)())data;
func();  // Segmentation fault! (execute non-executable)

// Accessing kernel memory
int *kernel = (int*)0xFFFFFFFF;
*kernel = 42;  // Segmentation fault! (user accessing kernel)
```

---

## Hardware Enforcement

### MMU (Memory Management Unit)

The **MMU** enforces memory protection in hardware:

**On every memory access:**
1. Translate virtual address to physical
2. Check valid bit (is page present?)
3. Check permission bits (is operation allowed?)
4. If violation → generate exception

**Hardware support is critical:**
- Software checks would be too slow
- Can't trust user programs to check themselves

### x86 Protection Rings

x86 has 4 privilege levels (rings):
```
Ring 0 - Kernel (most privileged)
Ring 1 - Device drivers (rarely used)
Ring 2 - Device drivers (rarely used)  
Ring 3 - User applications (least privileged)
```

Most OSes only use Ring 0 (kernel) and Ring 3 (user).

---

## Process Isolation

### Separate Address Spaces

**Each process has its own page table:**
- Process A's page tables only map Process A's memory
- Process B's page tables only map Process B's memory
- No way for Process A to access Process B's memory

**Context switch:**
```
Process A running
  │
  ├─ Save A's page table pointer
  ├─ Load B's page table pointer
  └─ Flush TLB
  │
Process B running
```

Now all virtual addresses map to B's physical pages.

### Example: Isolation

```
Process A:
  Virtual 0x1000 → Physical 0x5000 (A's page)

Process B:  
  Virtual 0x1000 → Physical 0x8000 (B's page)

Same virtual address, different physical pages!
Processes are isolated.
```

---

## Kernel Protection

### Kernel vs User Mode

**User mode (Ring 3):**
- Runs application code
- Limited permissions
- Cannot access kernel memory
- Cannot execute privileged instructions

**Kernel mode (Ring 0):**
- Runs OS code
- Full permissions
- Can access all memory
- Can execute privileged instructions

### Protecting Kernel Memory

**Kernel pages marked as supervisor-only:**
```
Kernel memory (0xC0000000-0xFFFFFFFF):
  U/S bit = 0 (supervisor only)
  
User memory (0x00000000-0xBFFFFFFF):
  U/S bit = 1 (user accessible)
```

**User trying to access kernel:**
```c
// User process
int *kernel_ptr = (int*)0xC0000000;
*kernel_ptr = 42;

// Hardware checks:
// 1. Current privilege level = 3 (user)
// 2. Page U/S bit = 0 (supervisor only)
// 3. Privilege violation!
// → Generate protection fault
```

---

## NX Bit (No eXecute)

### W^X: Write XOR Execute

Modern security principle: **Memory should be writable OR executable, never both.**

**Why?**
- Prevents code injection attacks
- Attacker can't write shellcode and execute it

### How It Works

**NX bit** (AMD) / **XD bit** (Intel) in page table entry:
- **NX = 0:** Page is executable
- **NX = 1:** Page is NOT executable

**Protection:**
```
Stack (R+W, NX=1):
  Can read/write data
  Cannot execute
  
Code (R+X, NX=0):
  Can read/execute
  Cannot write
```

### Attack Prevention

**Buffer overflow attack:**
```c
void vulnerable() {
    char buffer[64];
    gets(buffer);  // Overflow!
}
```

**Without NX:**
- Attacker overflows buffer
- Overwrites return address to point to buffer
- Buffer contains malicious code
- Code executes! ❌

**With NX:**
- Attacker overflows buffer
- Overwrites return address to point to buffer
- CPU tries to execute stack
- NX bit set → Protection fault! ✅

---

## ASLR (Address Space Layout Randomization)

**ASLR** randomizes memory layout to make attacks harder.

### What Gets Randomized

- Stack location
- Heap location
- Shared library locations
- (Sometimes) Code location (PIE - Position Independent Executable)

### Why It Helps

**Without ASLR:**
```
Stack always at 0xFFFF0000
Attacker knows where to jump!
```

**With ASLR:**
```
Stack at random address
Attacker doesn't know where to jump
Attack much harder
```

---

## Controlled Sharing

Sometimes processes need to share memory:

### Read-Only Sharing

**Safe to share:**
- Code pages (program text)
- Read-only data
- Shared libraries

**Both processes map same physical pages:**
```
Process A:
  Virtual 0x1000 → Physical 0x5000 (R+X)

Process B:
  Virtual 0x2000 → Physical 0x5000 (R+X)

Same physical page, both read-only
```

### Read-Write Sharing

**Requires explicit permission:**
- Shared memory segments (`shmget`, `mmap`)
- Must use synchronization (mutexes, semaphores)

**Example:**
```c
// Process A
int shmid = shmget(KEY, SIZE, IPC_CREAT | 0666);
char *mem = shmat(shmid, NULL, 0);
strcpy(mem, "Hello");

// Process B
int shmid = shmget(KEY, SIZE, 0666);
char *mem = shmat(shmid, NULL, 0);
printf("%s\n", mem);  // Prints "Hello"
```

---

## Copy-on-Write (COW)

**COW** allows safe sharing of writable pages after `fork()`:

### How COW Works

**After fork():**
1. Parent and child share same physical pages
2. Pages marked read-only in both processes
3. Both page tables point to same physical pages

**On write attempt:**
1. Write to read-only page → page fault
2. OS creates private copy of page
3. Update page table to point to new page
4. Mark new page as writable
5. Restart instruction

**Benefits:**
- Fast fork (no copying)
- Efficient memory use (only copy modified pages)
- Still maintains isolation

---

## Security Summary

**Defense in Depth:**
1. **Hardware memory protection** - MMU enforces permissions
2. **Process isolation** - Separate page tables
3. **Kernel protection** - Supervisor/User mode
4. **NX bit** - Prevent code injection
5. **ASLR** - Randomize memory layout
6. **Stack canaries** - Detect buffer overflows

**All working together to keep system secure!**

---

## Related Concepts

- [[Page Tables]]
- [[Paging]]
- [[Virtual Address Translation]]
- [[Shared Memory]]
- [[Processes|Processes]]

## Tags
#computer-systems #memory-protection #security #virtual-memory #nx-bit #aslr