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