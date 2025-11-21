# PROCESSES
---

**Definition:** Running instance of a program with own memory space & system stack

**CPU Core:** Fetch-decode-execute cycle

**Time-Sharing:** Multiple programs start → run briefly → switch
- **Scheduling:** Obtaining CPU
- **Descheduling:** Freeing CPU usage

### INTERRUPTS

**Async (Hardware)**
- Data arrival, Ctrl + C

**Sync**
- **Traps** → Intentional, always recoverable
	- System calls, breakpoints
- **Faults** → Unintentional, recoverable
	- Page faults, floating point exceptions
- **Aborts** → Unintentional, unrecoverable
	- Illegal instructions, RAM parity errors

### FORK/EXEC/WAIT PATTERN

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <assert.h>
#include <sys/wait.h>

int main(int argc, char **argv) {
	pid_t p = fork();
	assert(p != -1); // Check fork worked
	
	if (p == 0) { // <-- Child -->
		execl("/bin/ls", "ls", "-l", NULL); // Child turns to LS
		_exit(42); // If needed
	} else { // <-- Parent -->
		int status;
		pid_t child = wait(&status);
		printf("Parent: child %d, code %d\n", child, WEXITSTATUS(status));
	}
}
```

### SYSTEM CALLS

**wait()**:
- Parent waits for child process to finish
- Print line will NOT wait until child finishes execution

**exec()**:
- After fork, run different program with exec()
- **PID** → Stays the same
- **Address space** → Replaced with new program
- **Code, heap, stack, globals** → Discarded
- **Open FDs** → Usually preserved unless marked closed-on-exec
- **exec() will NOT return** in child process (code after exec won't run UNLESS error occurs)

### Shared Memory
- Processes are COW, so all virtual pages are duplicated on creation
- Attempting to write to anything, will then cause a private physical page to be duplicated to reduce memory duplication overhead

---
# FILE I/O
---

**Definition:** Collections of bytes that can be read, written, addressed using a name

### FILE PROPERTIES
- User owner
- Group owner
- R/W/X permission for user/group/other
- Access, modification, creation dates
- Size

### DEFAULT FILE DESCRIPTORS
- **0** → stdin (Standard input)
- **1** → stdout (Standard output)
- **2** → stderr (Standard error output)

### OPEN() SYSTEM CALL

```c
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

int open(const char *pathname, int flags);
int open(const char *pathname, int flags, mode_t mode);
```

**Access Mode Flags (Required - pick ONE):**
- `O_RDONLY` → Read only
- `O_WRONLY` → Write only
- `O_RDWR` → Read and write

**Other Flags:**
- `O_APPEND` → Write adds to end of file
- `O_CREAT` → Create if not exist (mode required)
- `O_TRUNC` → File set to 0 (restart)

**Chaining Example:**
```c
open("foo.txt", O_RDWR | O_CREAT | O_TRUNC, 0644)
```
- `0644` = `rw-r--r--` (User r/w, group read, others read)

**Return Values:**
- Success → File descriptor ≥ 0
- Error → -1 (errno variable set to error code)

**Close:** Call `close()` with file descriptor as argument

<!-- Start After Here -->

## Reading from files
`read` syscall allows for reading
Takes in a file descriptor, buffer to be written to, and maximum number of byte sto be read
```c
#include <unistd.h>
ssize_t read(int fd, void *buf, size_t count);
```
Success reurns the number of bytes actually read
Error returns -1 and errno is set to the error code

## Writing to a File
Args: file descriptor, buffer with the contents to eb written, number of byte sto write
```c
#include <unistd.h>
ssize_t write(int fd, const void *buf, size_t count);
```
Success: num bytes written
Error: returns -1 errnor set to erro code

**Important Notes:**
- `read()` returns 0 when reaching EOF
- Both `read()` and `write()` can do partial reads/writes (return fewer bytes than requested)
- `ssize_t` is signed type (can be negative for errors)
- May need to loop to ensure all bytes are read/written

### FILE DESCRIPTOR REDIRECTION

**Pattern:** Close a standard FD, then open new file → takes lowest available FD number

```c
close(1);  // Close stdout (fd 1)
int fd = open("output.txt", O_WRONLY | O_CREAT | O_TRUNC, 0644);
// fd will be 1 (takes the lowest available)
// Now all printf/write to stdout goes to output.txt!
```

**With fork/exec:**
```c
pid_t p = fork();
if (p == 0) {  // Child
    close(1);  // Close stdout
    open("output.txt", O_WRONLY | O_CREAT | O_TRUNC, 0644);
    execl("/bin/ls", "ls", "-l", NULL);
    // ls output goes to output.txt instead of terminal
}
```

**dup2() - Cleaner approach:**
```c
int fd = open("output.txt", O_WRONLY | O_CREAT | O_TRUNC, 0644);
dup2(fd, 1);  // Make fd 1 (stdout) a copy of fd
close(fd);    // Can close original fd now
```

---
# FILE I/O + PROCESSES INTERACTIONS
---

### FILE DESCRIPTORS AND fork()

**Behavior:**
- Child **inherits all open file descriptors** from parent
- Parent and child **share the same file position pointer**
  - If parent reads, child's position moves too!
- Separately opened files get **independent position pointers**

### FILE DESCRIPTORS AND exec()

**Behavior:**
- By default, FDs **remain open** across `exec()` calls
- Can mark FDs to close on exec:
  - `O_CLOEXEC` flag in `open()`
  - `fcntl(fd, F_SETFD, FD_CLOEXEC)`
- This enables shell redirection (shell sets up FDs, then execs program)

### PIPES - Inter-Process Communication (IPC)

**`pipe()` system call:**
- Creates two FDs: one for reading, one for writing
- Used for communication between processes

```c
int pipefd[2];
pipe(pipefd);  // pipefd[0] = read end, pipefd[1] = write end

pid_t p = fork();
if (p == 0) {  // Child
    close(pipefd[1]);  // Close write end
    // Read from pipefd[0]
} else {  // Parent
    close(pipefd[0]);  // Close read end
    // Write to pipefd[1]
}
```

**Pattern:** Parent writes to pipe, child reads (or vice versa)

### OTHER FILE OPERATIONS

**lseek() - Move file position:**
```c
off_t lseek(int fd, off_t offset, int whence);
// whence: SEEK_SET, SEEK_CUR, SEEK_END
```

**stat()/fstat() - Get file info without opening:**
```c
struct stat sb;
stat("file.txt", &sb);   // Using pathname
fstat(fd, &sb);          // Using file descriptor
```

**Error Handling:**
- Use `perror()` or `strerror(errno)` for error messages
- **Buffered vs Unbuffered I/O:**
  - `read()`/`write()` = unbuffered (direct system calls)
  - `fread()`/`fwrite()` = buffered (stdio library functions)

---
# VIRTUAL MEMORY
---

**Purpose:** Translate Virtual Addresses to Physical Addresses

**Key Concept:** Each process has its own virtual address space, giving the illusion of having all memory to itself

### VIRTUAL ADDRESS STRUCTURE

**Address Breakdown:**
- Virtual Address = **Virtual Page Number (VPN)** + **Offset**
- **VPN** → Used to index into page table
- **Offset** → Position within the page (stays the same in physical address)

**Example (4KB pages):**
- 32-bit address = 20 bits VPN + 12 bits offset
- 12 bits offset = 2^12 = 4096 bytes = 4KB page size

### PAGE TABLES

**Structure:**
- Maps Virtual Page Number → Physical Page Number (PPN) / Physical Frame Number (PFN)
- Each process has its own page table
- Stored in kernel memory

**Page Table Entry (PTE) contains:**
- **Valid/Present bit** → Page is in physical memory
- **Physical Page Number (PPN)** → Location in physical memory
- **Permission bits:**
  - **R** (Read) - Can read from page
  - **W** (Write) - Can write to page
  - **X** (Execute) - Can execute code from page
- **Dirty bit** → Page has been modified
- **Reference/Access bit** → Page has been accessed (for replacement algorithms)

### ADDRESS TRANSLATION PROCESS

1. Extract VPN from virtual address
2. Use VPN to index into page table
3. Check valid bit - if 0, **page fault** occurs
4. Check permission bits - if violation, **segmentation fault**
5. Get PPN from PTE
6. Combine PPN + Offset = Physical Address

**Formula:**
```
Physical Address = (PPN × Page_Size) + Offset
```

### PAGING DETAILS

**Page Size:** Typically 4KB (4096 bytes)

**Page Fault:**
- Occurs when valid bit = 0 (page not in memory)
- OS handles by:
  1. Finding page on disk
  2. Loading page into physical memory
  3. Updating page table entry
  4. Restarting instruction

**Demand Paging:**
- Pages loaded into memory only when needed (on first access)
- Not all pages of a process need to be in memory at once

**TLB (Translation Lookaside Buffer):**
- Hardware cache for page table entries
- Speeds up address translation
- Stores recent VPN → PPN translations
- TLB hit = fast translation, TLB miss = access page table

### MULTI-LEVEL PAGE TABLES

**Purpose:** Reduce memory overhead of large page tables

**Structure:**
- Instead of one large page table, use hierarchy
- Virtual address split into: **Level 1 index** + **Level 2 index** + **Offset**
- Only allocate page tables for regions actually used

**Benefits:**
- Saves memory (don't need to allocate entire page table)
- Only create second-level tables when needed

### MEMORY PROTECTION

**Permission Bits Enforce:**
- **Code segment:** R + X (read and execute, no write)
- **Data segment:** R + W (read and write, no execute)
- **Stack/Heap:** R + W (read and write, no execute)

**Protection Violations:**
- Writing to read-only page → **Segmentation fault**
- Executing non-executable page → **Segmentation fault**
- Accessing invalid page → **Page fault**

**Isolation:**
- Each process has separate page table
- Cannot access another process's memory
- Kernel memory protected from user processes

### SHARED MEMORY BETWEEN PROCESSES

**Copy-on-Write (COW):**
- After `fork()`, parent and child share same physical pages
- Pages marked read-only in both processes
- On write attempt:
  1. Page fault occurs
  2. OS creates private copy of page
  3. Updates page table to point to new copy
  4. Marks new page as writable
- **Benefit:** Reduces memory overhead - only copy pages that are modified

**Explicit Shared Memory:**
- Multiple processes can map same physical pages
- Page tables point to same physical memory
- Used for IPC (Inter-Process Communication)
- Must use synchronization (mutexes, semaphores)

**Shared Libraries:**
- Code pages of libraries (like libc) shared between processes
- Read-only pages can be safely shared
- Reduces memory usage across system

---
### CONCURRENCY VS PARALLELISM

**Concurrency:**
- Happenings at the same time through interleaving
- Sharing resources
- Example: 2 queues for a single coffee machine

**Parallelism:**
- Happening at the same time, progressing independently
- Example: 2 coffee machines, one for each line
- **Parallelism is a subset of concurrency**

### CONCURRENCY MODELS

**Process-Based:**
- Fork different processes with own private address space
- Sharing is explicitly requested
- Heavy overhead

**Event-Based:**
- Manually interleaves logical flows
- Polls for events
- All flows share same address space
- Uses I/O multiplexing

**Thread-Based:**
- Kernel automatically interleaves multiple logical flows
- Each flow shares the same address space
- Hybrid of process and event-based

### THREADS

**Why Threads?**
- Processes are heavy, sharing information is difficult
- Threads are lightweight processes
- Separate threads of execution within same address space

**What Threads Share:**
- **Heap** - Shared
- **Data segment** - Shared
- **Code segment** - Shared
- **Page table** - Shared
- **File descriptors** - Shared
- **Stack** - NOT shared (each thread has own stack)
- **Registers** - NOT shared (separate register state)

**Benefits:**
- Cheaper to create than processes
- Faster to switch between them
- Faster to reap when done
- Can still run on separate cores

### SHARED DATA: THREADS VS PROCESSES

| Variable Type              | fork() (Processes) | Threads    |
| -------------------------- | ------------------ | ---------- |
| **Global variables**       | Not shared         | Shared     |
| **Local variables**        | Not shared         | Not shared |
| **Local static variables** | Not shared         | Shared     |
| **Heap (malloc)**          | Not shared (COW)   | Shared     |

**Note:** Forked processes only share memory that is `mmap`'d with `MAP_SHARED`

### POSIX THREADS (pthreads)

**pthread_create() - Create a thread**
```c
int pthread_create(pthread_t *thread, const pthread_attr_t *attr,
                   void *(*start_routine)(void *), void *arg);
```
**Arguments:**
- `thread` - Thread handle pointer (which thread to use)
- `attr` - Attributes (NULL is default)
- `start_routine` - Function pointer (takes single void* argument)
- `arg` - Argument supplied to start routine

**Other Thread Functions:**
- `pthread_join()` - Wait for thread to complete (like `wait()` for processes)
- `pthread_self()` - Get current thread ID
- `pthread_cancel()` - Cancel a thread

### CONCURRENCY ISSUES

**Data Race:**
- Two threads read, modify, and update same data without synchronization
- No ordering or locks to protect shared data
- Results in unpredictable behavior

**Deadlock:**
- Thread 1 locks Mutex A, needs Mutex B
- Thread 2 locks Mutex B, needs Mutex A
- Both threads wait forever for the other's mutex
- **Prevention:** Always acquire locks in same order

### MUTEXES (MUTUAL EXCLUSION)

**Purpose:** Provide atomic access to shared data

**Key Operations:**
- Atomic wait + lock
- Atomic unlock

**POSIX Mutex Functions:**
```c
pthread_mutex_t mutex;

pthread_mutex_init(&mutex, NULL);      // Create/initialize mutex
pthread_mutex_lock(&mutex);            // Lock mutex (blocks if already locked)
pthread_mutex_unlock(&mutex);          // Unlock mutex
pthread_mutex_trylock(&mutex);         // Attempt lock (returns immediately)
```

**Usage Pattern:**
```c
pthread_mutex_lock(&mutex);
// Critical section - access shared data
pthread_mutex_unlock(&mutex);
```

**Important:**
- Always unlock what you lock
- Keep critical sections short
- Avoid nested locks (can cause deadlock)
---
# KERNELS & XV6
---

**Key Concepts:**
- Modern OS sets up hardware to work for it
- OS depends on interrupts to stay in control (clock, I/O)
- OS relies on HW support for memory management

### PRIVILEGE MODES

**Kernel Mode (Privileged):**
- Certain operations only available in kernel mode
- Full hardware access
- Direct memory access

**User Mode (Unprivileged):**
- Run as much code as possible in user mode
- Limited hardware access
- Must request kernel services

**Context Switching:**
- Switching between modes is expensive
- User-mode software eventually needs to ask kernel for services

---

## KERNEL ARCHITECTURES

### MONOLITHIC KERNELS

**Structure:**
- Lives as single binary - single code base
- All code runs in privileged mode
- New device drivers compiled into kernel binary, OS reloaded

**Modern Approach:**
- Drivers dynamically loaded into running kernel (module-based)

**Advantages:**
- Minimizes context switching
- Usually single code base
- Better performance

**Disadvantages:**
- Large codebase (Linux has 40M+ lines)
- Poor isolation and robustness
- Bug in driver can damage entire OS (Blue Screen of Death)

### MICROKERNELS

**Structure:**
- Kernel in privileged mode is small (only essentials)
- Device drivers run in unprivileged user space
- Drivers act as servers - userspace programs with some privileged access

**Advantages:**
- Smaller code base
- Better modularity and configurability
- Easier to add new components
- Driver bug does NOT bring down entire OS

**Disadvantages:**
- Performance penalty
- Many more context switches for message passing between drivers

### HYBRID KERNELS

**Structure:**
- Really a monolithic kernel, structured somewhat like microkernel
- Or a bigger microkernel
- Most code still runs in kernel space for performance

**Notes:**
- Often dismissed as PR stunt for monolithic kernel
- Examples: Windows NT series (modern Windows 10), OS/2, XNU (macOS)

---

## BOOT PROCESS & BOOTLOADERS

### BOOT SEQUENCE

**1. Power Button Pressed**
- Motherboard powers up

**2. BIOS Execution**
- BIOS lives on chip in motherboard
- Copied to RAM at address 0xFF
- `jmp 0xFF` written to RAM at 0xFFFF0 where CPU starts executing

**3. BIOS - Load User Settings**
- Loads settings from volatile memory on motherboard
- Backed by small battery

**4. BIOS - Hardware Initialization**
- Basic hardware checks and initialization:
  - CPU, memory, keyboard, mouse, graphics, HDD
  - Interrupt handlers
  - Run BIOSes on additional hardware
  - Test everything (POST - Power-On Self-Test)

**5. Bootstrap Sequence**
- Scan bootable devices (HDDs, CD/DVD-ROM, USB, Network)
- Find bootable Master Boot Record (MBR)
- Load code from MBR and jump to it

### MASTER BOOT RECORD (MBR)

**Structure:**
- 512 bytes at very beginning of storage device
- Contains partition table (up to 4 entries)
- 446 bytes of executable code

**Purpose:**
- Not enough space for full OS (only 446 bytes)
- MBR code loads code that loads code that loads OS (bootloader)
- Small bootloader in MBR
- Each partition might have its own bootloader

**Modern Standard:**
- GRUB is standard bootloader nowadays