## Overview

File operations are one of the most fundamental operations on Unix-like systems. The POSIX File API provides system calls to interact with the file system through [[File Descriptors]].

## Unix Philosophy: Everything is a File

In Unix, files (and directories) are one of the most fundamental abstractions:
- They represent data stored on disks
- Some files in the Unix filesystem tree don't correspond to anything stored on disk
- This abstraction makes file operations universally applicable

## Files and Directories

Modern file systems have two main abstractions:

### File
- A collection of bytes that can be read and written
- Addressed using a name
- Contains associated metadata

### Directory
- A collection of files and other directories
- Creates a tree-shaped organization

### File/Directory Properties
- User owner
- Group owner
- Access permissions (read/write/execute for user/group/others)
- Access/modification/creation dates
- Size
- Other metadata

## Opening Files

Use the `open()` system call:

```c
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

int open(const char *pathname, int flags);
int open(const char *pathname, int flags, mode_t mode);
```

### Parameters
- `pathname`: Path to the file
- `flags`: Specifies how the file should be opened
- `mode`: (Optional) File permissions when creating new files

### Access Mode Flags (Required - Choose One)
- `O_RDONLY` - Open for reading only
- `O_WRONLY` - Open for writing only
- `O_RDWR` - Open for both reading and writing

### Other Flags (Optional)
- `O_APPEND` - Write to end of file (append mode)
- `O_CREAT` - Create file if it doesn't exist (requires `mode` argument)
- `O_TRUNC` - Truncate file to 0 and write from beginning

### Combining Flags
Multiple flags are combined using the bitwise OR operator `|`:

```c
// Create file if needed, truncate if exists, open for read/write
// Permissions: rw-r--r-- (0644)
int fd = open("foo.txt", O_RDWR | O_CREAT | O_TRUNC, 0644);
```

### Return Value
- **Success**: Returns a file descriptor ≥ 0
- **Error**: Returns -1 and sets `errno`

### File Permissions
When using `O_CREAT`, you must specify permissions (e.g., `0644` = `rw-r--r--`)

See: [Linux File Permissions](https://www.linuxfoundation.org/blog/blog/classic-sysadmin-understanding-linux-file-permissions)

Reference: `man 2 open`

## Closing Files

```c
#include <unistd.h>

int close(int fd);
```

Closes an open file descriptor.

## Reading from Files

```c
#include <unistd.h>

ssize_t read(int fd, void *buf, size_t count);
```

### Parameters
- `fd`: [[File Descriptors|File descriptor]] to read from
- `buf`: Buffer to write data into
- `count`: Maximum number of bytes to read

### Return Value
- **Success**: Number of bytes actually read
- **Error**: Returns -1 and sets `errno`

## Writing to Files

```c
#include <unistd.h>

ssize_t write(int fd, const void *buf, size_t count);
```

### Parameters
- `fd`: [[File Descriptors|File descriptor]] to write to
- `buf`: Buffer containing data to write
- `count`: Number of bytes to write

### Return Value
- **Success**: Number of bytes actually written
- **Error**: Returns -1 and sets `errno`

### Example Usage
You can trace system calls with `strace`:
```bash
strace cat foo
```

## Other File Operations

### `lseek`
Move the file position within a file (seek to different location)

### `fsync`
Flush buffer to file - forces data to be written to disk

### `rename`
Rename a file

### `stat`
Get metadata about a file

### `link`
Associate another name with file data (create hard link)

### `unlink`
Remove a reference to a file / delete a file

## Related Concepts
- [[File Descriptors]]
- [[Processes]]
- [[Creating New Processes]]

## Tags
#computer-systems #file-io #unix #system-calls #processes

---

## File Descriptor Redirection

### Pattern: Redirecting Standard Streams

You can redirect standard file descriptors (stdin, stdout, stderr) by closing them and opening a new file. The new file will take the **lowest available file descriptor number**.

```c
// Redirect stdout to a file
close(1);  // Close stdout (fd 1)
int fd = open("output.txt", O_WRONLY | O_CREAT | O_TRUNC, 0644);
// fd will be 1 (takes the lowest available)
// Now all printf/write to stdout goes to output.txt!
```

### With fork/exec

This is commonly used when spawning child processes:

```c
pid_t p = fork();
if (p == 0) {  // Child
    close(1);  // Close stdout
    open("output.txt", O_WRONLY | O_CREAT | O_TRUNC, 0644);
    execl("/bin/ls", "ls", "-l", NULL);
    // ls output goes to output.txt instead of terminal
}
```

### Using dup2() - Cleaner Approach

The `dup2()` system call provides a cleaner way to redirect file descriptors:

```c
#include <unistd.h>

int dup2(int oldfd, int newfd);
```

**Purpose:** Makes `newfd` a copy of `oldfd`

**Example:**
```c
int fd = open("output.txt", O_WRONLY | O_CREAT | O_TRUNC, 0644);
dup2(fd, 1);  // Make fd 1 (stdout) a copy of fd
close(fd);    // Can close original fd now

// Now stdout is redirected to output.txt
printf("This goes to the file\n");
```

---

## Pipes - Inter-Process Communication

### What are Pipes?

Pipes provide a way for processes to communicate by creating a **unidirectional data channel**.

```c
#include <unistd.h>

int pipe(int pipefd[2]);
```

**Creates two file descriptors:**
- `pipefd[0]` - **Read end** of the pipe
- `pipefd[1]` - **Write end** of the pipe

**Return Value:**
- Returns 0 on success
- Returns -1 on error

### How Pipes Work

- Data written to the write end can be read from the read end
- Data flows in **one direction only**
- Acts as a **FIFO buffer** (First In, First Out)

### Example: Parent-Child Communication

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

int main() {
    int pipefd[2];
    pipe(pipefd);  // Create pipe
    
    pid_t p = fork();
    
    if (p == 0) {  // Child process
        close(pipefd[1]);  // Close write end (child only reads)
        
        char buffer[100];
        read(pipefd[0], buffer, sizeof(buffer));
        printf("Child received: %s\n", buffer);
        
        close(pipefd[0]);
        exit(0);
        
    } else {  // Parent process
        close(pipefd[0]);  // Close read end (parent only writes)
        
        const char *msg = "Hello from parent!";
        write(pipefd[1], msg, strlen(msg) + 1);
        
        close(pipefd[1]);
        wait(NULL);
    }
    
    return 0;
}
```

### Common Pattern

**Best Practice:** Close unused ends of the pipe
- Parent writes → Close read end in parent
- Child reads → Close write end in child
- This prevents deadlocks and ensures proper EOF signaling

---

## File Descriptors and fork()

### Inheritance

When a process calls `fork()`:
- Child **inherits all open file descriptors** from parent
- Both processes have descriptors pointing to the **same file table entry**

### Shared File Position

**Important behavior:**
- Parent and child **share the same file position pointer**
- If parent reads 10 bytes, child's position also advances 10 bytes
- Both point to the same underlying file structure in kernel

**Example:**
```c
int fd = open("data.txt", O_RDONLY);

pid_t p = fork();

if (p == 0) {
    // Child reads - advances shared position
    char buf[10];
    read(fd, buf, 10);
} else {
    // Parent's read starts where child left off!
    char buf[10];
    wait(NULL);
    read(fd, buf, 10);  // Reads next 10 bytes, not first 10
}
```

### Independent File Positions

If you want independent positions, open the file **separately** in each process:

```c
pid_t p = fork();

if (p == 0) {
    int child_fd = open("data.txt", O_RDONLY);
    // Child has its own position
} else {
    int parent_fd = open("data.txt", O_RDONLY);
    // Parent has its own position
}
```

---

## File Descriptors and exec()

### Behavior Across exec()

**Default:** File descriptors **remain open** across `exec()` calls
- The new program inherits all open file descriptors
- This is how shell redirection works

### Closing on exec

You can mark file descriptors to **close automatically** on exec:

**Using O_CLOEXEC flag:**
```c
int fd = open("file.txt", O_RDONLY | O_CLOEXEC);
```

**Using fcntl():**
```c
int fd = open("file.txt", O_RDONLY);
fcntl(fd, F_SETFD, FD_CLOEXEC);
```

### Why This Matters

This enables **shell redirection**:
1. Shell sets up file descriptors (redirects stdin/stdout/stderr)
2. Shell calls `exec()` to run the program
3. Program inherits redirected file descriptors
4. Program's I/O automatically goes to redirected locations

**Example:**
```bash
ls -l > output.txt
```

Shell does:
```c
int fd = open("output.txt", O_WRONLY | O_CREAT | O_TRUNC, 0644);
dup2(fd, 1);  // Redirect stdout
close(fd);
execvp("ls", ["ls", "-l", NULL]);
// ls writes to stdout, which now points to output.txt
```

---

## Advanced File Operations

### lseek() - Move File Position

```c
#include <unistd.h>

off_t lseek(int fd, off_t offset, int whence);
```

**Move the file position:**
- `SEEK_SET` - Offset from beginning of file
- `SEEK_CUR` - Offset from current position
- `SEEK_END` - Offset from end of file

**Example:**
```c
// Seek to byte 100
lseek(fd, 100, SEEK_SET);

// Skip forward 50 bytes
lseek(fd, 50, SEEK_CUR);

// Go to end of file
lseek(fd, 0, SEEK_END);
```

### stat()/fstat() - Get File Metadata

```c
#include <sys/stat.h>

int stat(const char *pathname, struct stat *buf);
int fstat(int fd, struct stat *buf);
```

**Get file information without opening:**
- `stat()` - Uses pathname
- `fstat()` - Uses file descriptor

**Example:**
```c
struct stat sb;

// Using pathname
if (stat("file.txt", &sb) == 0) {
    printf("File size: %ld bytes\n", sb.st_size);
    printf("Permissions: %o\n", sb.st_mode & 0777);
}

// Using file descriptor
int fd = open("file.txt", O_RDONLY);
fstat(fd, &sb);
```

---

## Error Handling

### Using perror()

```c
int fd = open("missing.txt", O_RDONLY);
if (fd < 0) {
    perror("Failed to open file");
    // Prints: "Failed to open file: No such file or directory"
}
```

### Using strerror()

```c
#include <string.h>
#include <errno.h>

int fd = open("missing.txt", O_RDONLY);
if (fd < 0) {
    fprintf(stderr, "Error: %s\n", strerror(errno));
}
```

---

## Buffered vs Unbuffered I/O

### Unbuffered (System Calls)
- `read()`, `write()`, `open()`, `close()`
- Direct system calls to kernel
- No automatic buffering
- Each call crosses user-kernel boundary

### Buffered (Standard I/O Library)
- `fread()`, `fwrite()`, `fopen()`, `fclose()`
- Part of C standard library (`stdio.h`)
- Maintains internal buffer
- Reduces number of system calls
- Better performance for small reads/writes

**Example:**
```c
// Unbuffered - each write is a system call
write(fd, "a", 1);
write(fd, "b", 1);
write(fd, "c", 1);  // 3 system calls

// Buffered - accumulates in buffer
fputc('a', fp);
fputc('b', fp);
fputc('c', fp);  // May be 0 system calls until flush
```

---

## Related Concepts

- [[File Descriptors]]
- [[Processes]]
- [[Creating New Processes]]
- [[Concurrency|Concurrency]] - Shared resources

## Tags
#computer-systems #file-io #unix #system-calls #processes #pipes #redirection