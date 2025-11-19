Processes:
	Process management
	Creating processes
	Understanding system calls
	How the OS manages a process, behavior that is available
	Memory access, what is available and what is not

Virtual Memory Management:
	Paging
	Address Translation
	

Concurrency:
	What is shared between threads vs processes
	Basic mechanics of mutexes

File I/O:

Some Kernels.


No repeats from Exam 1, but assumed knowing C + Assembly, state of stack at this point, etc.

---
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
# Virtual Memory
---
- Translate Virtual Addresses to Physical Addresses
- Page table holds Virtual Page Number -> Physical Page Address translation units
- Offsets are stored as the same for direct recovery
- Page table holds virtual -> physical maps with R/W/X permission bits
- Pages are 4KB in size