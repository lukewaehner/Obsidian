# Shared Memory Between Processes

## Overview

By default, processes are **isolated** - they cannot access each other's memory. However, there are controlled mechanisms for processes to share memory.

**Types of Sharing:**
1. Copy-on-Write (COW) - Automatic after fork()
2. Explicit Shared Memory - Programmer-requested
3. Shared Libraries - Code sharing across processes

---

## Copy-on-Write (COW)

### The Problem

**Naïve fork() implementation:**
```c
// fork() creates child process
// Copy ALL of parent's memory to child

Parent: 100MB of memory
Child:  100MB of memory (copied)

Total: 200MB
Fork time: Slow! (100MB to copy)
```

Often wasteful - child might exec() immediately, throwing away copied memory!

### COW Solution

**Copy-on-Write** = Share memory until someone writes to it

**After fork():**
1. Parent and child **share same physical pages**
2. Pages marked **read-only in both processes**
3. Page tables point to same physical memory
4. No copying yet!

**On write attempt:**
1. Write to read-only page → **Page fault**
2. OS handles fault:
   - Allocate new physical page
   - Copy content to new page
   - Update page table to point to new page
   - Mark new page as writable
3. Restart instruction (write succeeds now)

### Example

```c
int global = 42;

pid_t p = fork();

if (p == 0) {
    // Child reads global
    printf("%d\n", global);  // No page fault! Still shared
    
    // Child writes global
    global = 100;  // Page fault! OS makes private copy
    
    printf("%d\n", global);  // Prints 100 (child's copy)
} else {
    wait(NULL);
    printf("%d\n", global);  // Prints 42 (parent's copy)
}
```

### COW Benefits

**Memory efficiency:**
- Only copy pages that are actually modified
- If child calls exec(), no copying needed at all!

**Performance:**
- Fork is fast (no immediate copying)
- Delay copying until necessary

**When is COW most effective?**
```c
// Child execs immediately - NO copying needed!
pid_t p = fork();
if (p == 0) {
    execl("/bin/ls", "ls", NULL);  // All memory discarded
}

// Child reads but doesn't write - NO copying needed!
pid_t p = fork();
if (p == 0) {
    printf("%d\n", global);  // Just reading, no copy
    exit(0);
}
```

---

## Explicit Shared Memory

### System V Shared Memory

The traditional Unix way to share memory between processes.

#### Creating Shared Memory

```c
#include <sys/shm.h>

// Create shared memory segment
int shmget(key_t key, size_t size, int shmflg);

// Attach shared memory to process
void *shmat(int shmid, const void *shmaddr, int shmflg);

// Detach shared memory
int shmdt(const void *shmaddr);

// Control/delete shared memory
int shmctl(int shmid, int cmd, struct shmid_ds *buf);
```

#### Example

```c
#define SHM_KEY 1234
#define SHM_SIZE 4096

// Process A: Create and write
int shmid = shmget(SHM_KEY, SHM_SIZE, IPC_CREAT | 0666);
char *mem = (char*)shmat(shmid, NULL, 0);
strcpy(mem, "Hello from Process A!");
shmdt(mem);

// Process B: Attach and read
int shmid = shmget(SHM_KEY, SHM_SIZE, 0666);
char *mem = (char*)shmat(shmid, NULL, 0);
printf("Received: %s\n", mem);  // Prints: Hello from Process A!
shmdt(mem);

// Cleanup (either process)
shmctl(shmid, IPC_RMID, NULL);
```

### POSIX Shared Memory

Modern alternative using file-like interface.

```c
#include <sys/mman.h>
#include <fcntl.h>

// Create shared memory object
int shm_open(const char *name, int oflag, mode_t mode);

// Memory map
void *mmap(void *addr, size_t length, int prot, int flags, 
           int fd, off_t offset);

// Unmap
int munmap(void *addr, size_t length);

// Delete shared memory object
int shm_unlink(const char *name);
```

#### Example

```c
// Process A: Create and write
int fd = shm_open("/myshm", O_CREAT | O_RDWR, 0666);
ftruncate(fd, 4096);
char *mem = mmap(NULL, 4096, PROT_READ | PROT_WRITE, 
                 MAP_SHARED, fd, 0);
strcpy(mem, "Hello via POSIX!");
munmap(mem, 4096);
close(fd);

// Process B: Open and read
int fd = shm_open("/myshm", O_RDWR, 0666);
char *mem = mmap(NULL, 4096, PROT_READ | PROT_WRITE,
                 MAP_SHARED, fd, 0);
printf("%s\n", mem);
munmap(mem, 4096);
close(fd);

// Cleanup
shm_unlink("/myshm");
```

---

## Memory Mapping with mmap()

### Overview

`mmap()` creates a mapping between a file or memory region and the process's address space.

```c
void *mmap(void *addr,      // Preferred address (NULL = let OS choose)
           size_t length,    // Size to map
           int prot,         // Protection (PROT_READ | PROT_WRITE | PROT_EXEC)
           int flags,        // MAP_SHARED or MAP_PRIVATE
           int fd,           // File descriptor (or -1 for anonymous)
           off_t offset);    // Offset in file
```

### MAP_SHARED vs MAP_PRIVATE

**MAP_SHARED:**
- Changes visible to other processes
- Changes written to underlying file
- Used for IPC

**MAP_PRIVATE:**
- Changes private to this process
- Copy-on-Write semantics
- Used for loading executables

### Example: File Mapping

```c
// Map file into memory
int fd = open("data.txt", O_RDWR);
struct stat sb;
fstat(fd, &sb);

char *mem = mmap(NULL, sb.st_size, PROT_READ | PROT_WRITE,
                 MAP_SHARED, fd, 0);

// Now can access file like memory!
mem[0] = 'X';  // Modifies file

munmap(mem, sb.st_size);
close(fd);
```

### Anonymous Mapping (No File)

```c
// Create anonymous shared memory
char *mem = mmap(NULL, 4096, PROT_READ | PROT_WRITE,
                 MAP_SHARED | MAP_ANONYMOUS, -1, 0);

pid_t p = fork();
if (p == 0) {
    strcpy(mem, "Child writing");
} else {
    wait(NULL);
    printf("Parent reads: %s\n", mem);
}

munmap(mem, 4096);
```

---

## Shared Libraries

### Why Share Libraries?

Many processes use common libraries:
- libc (standard C library)
- libm (math library)
- libpthread (threading library)

**Without sharing:**
```
Process A: libc code at 0x1000 (physical 0x5000)
Process B: libc code at 0x1000 (physical 0x8000)
Process C: libc code at 0x1000 (physical 0xB000)

3× memory usage!
```

**With sharing:**
```
Process A: libc at 0x1000 → physical 0x5000
Process B: libc at 0x1000 → physical 0x5000 (SAME!)
Process C: libc at 0x1000 → physical 0x5000 (SAME!)

1× memory usage!
```

### How Library Sharing Works

**Library code is read-only:**
1. Load library into memory once
2. Map same physical pages into all processes
3. Mark pages as read-only (R + X)
4. Safe to share because no writes allowed

**Library data is private:**
- Each process gets own copy of global variables
- Uses MAP_PRIVATE for data sections

### Shared Library Loading

```c
// Dynamic linker loads shared libraries

// Library code (shared):
//   Virtual X → Physical P (R+X, shared)
//   Multiple processes point to same P

// Library data (private):
//   Virtual Y → Different physical pages per process
//   Each process has own copy
```

### Benefits

**Memory savings:**
- Only one copy of code in physical memory
- Hundreds of processes using libc → Save 1-2MB per process

**Page cache benefits:**
- Library code in page cache
- Warm cache when new process starts

**Updates:**
- Update library once
- All processes use new version (after restart)

---

## Synchronization Required!

### The Problem

**Shared memory without synchronization = Data races!**

```c
// Shared counter
int *counter = /* shared memory */;

// Process A
(*counter)++;  // Read, increment, write

// Process B  
(*counter)++;  // Read, increment, write

// Race condition! May lose updates
```

### Solutions

**Use synchronization primitives:**

1. **Mutexes** - Mutual exclusion locks
2. **Semaphores** - Counting semaphores
3. **Condition Variables** - Wait for conditions

```c
// Shared memory with mutex
struct shared_data {
    pthread_mutex_t lock;
    int counter;
} *data;

// Process A
pthread_mutex_lock(&data->lock);
data->counter++;
pthread_mutex_unlock(&data->lock);

// Process B
pthread_mutex_lock(&data->lock);
data->counter++;
pthread_mutex_unlock(&data->lock);

// No race condition!
```

See: [[Mutex Locks|Mutex Locks]], [[Semaphores|Semaphores]]

---

## Security Considerations

### Permissions

**Shared memory has permissions just like files:**
```c
// Create with specific permissions
shmget(KEY, SIZE, IPC_CREAT | 0600);  // Owner only
shmget(KEY, SIZE, IPC_CREAT | 0666);  // Everyone
```

### Cleanup

**Shared memory persists even after processes exit!**
- Must explicitly delete with `shmctl()` or `shm_unlink()`
- Otherwise wastes system resources

```bash
# List shared memory segments
ipcs -m

# Remove shared memory segment
ipcrm -m <shmid>
```

---

## Summary

| Mechanism | Automatic? | Read-Only? | Synchronization Needed? |
|-----------|------------|------------|-------------------------|
| **Copy-on-Write** | Yes (fork) | Initially | No (private after copy) |
| **Shared Memory** | No (explicit) | No | Yes |
| **Shared Libraries** | Yes (dynamic linker) | Yes (code) | No (read-only) |
| **mmap(SHARED)** | No (explicit) | Configurable | Yes (if writable) |

---

## Related Concepts

- [[Creating New Processes|Creating New Processes]] - fork() and COW
- [[Mutex Locks|Mutex Locks]] - Synchronizing shared memory
- [[Semaphores|Semaphores]] - Alternative synchronization
- [[Page Tables]] - How sharing is implemented
- [[Memory Protection]] - Controlling access

## Tags
#computer-systems #shared-memory #copy-on-write #ipc #mmap #virtual-memory