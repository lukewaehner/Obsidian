

## What Are File Descriptors?

**File descriptors** are integers that represent open files in a process. They are the fundamental mechanism used by the POSIX File API to reference open files.

## How They Work

- Each process has its own **file descriptor table**
- File descriptors are indices into this table
- The table contains pointers to open file structures

## Implementation

### In xv6
```c
struct proc {
  // ...
  struct file *ofile[NOFILE];  // Open files
  // ...
};
```

### In Linux
```c
struct task_struct {
  // ...
  /* Open file information: */
  struct files_struct *files;
  // ...
}
```

The file descriptor number is typically the literal index into the `ofile` array.

## Default File Descriptors

Every process starts with 3 standard file descriptors:

| Descriptor | Purpose | Name |
|------------|---------|------|
| 0 | Standard input | stdin |
| 1 | Standard output | stdout |
| 2 | Standard error output | stderr |

These are automatically opened when a process starts.

## File Descriptor Lifecycle

1. **Opening**: Call `open()` to get a new file descriptor
   - Returns the lowest available unused descriptor number
   - Typically starts at 3 (after stdin, stdout, stderr)

2. **Using**: Pass file descriptor to operations like:
   - `read(fd, buf, count)`
   - `write(fd, buf, count)`
   - `lseek(fd, offset, whence)`

3. **Closing**: Call `close(fd)` when done
   - Frees the descriptor for reuse
   - Important to prevent file descriptor leaks

## Key Properties

- **Per-process**: Each process has its own file descriptor table
- **Small integers**: Typically start at 0 and increment
- **Reusable**: Closed descriptors can be reassigned
- **Limited**: Maximum number defined by `NOFILE` (system limit)

## Example

```c
// Open a file - returns fd >= 3 (assuming stdin/stdout/stderr are 0,1,2)
int fd = open("data.txt", O_RDONLY);
if (fd < 0) {
    perror("open failed");
    return -1;
}

// Use the file descriptor
char buffer[100];
ssize_t bytes_read = read(fd, buffer, sizeof(buffer));

// Close when done
close(fd);
```

## Common Pitfalls

- **Forgetting to close**: Leads to file descriptor leaks
- **Using after close**: Undefined behavior
- **Exceeding limits**: Process can run out of available descriptors
- **Not checking return values**: `open()` returns -1 on error

## Related Concepts
- [[Code/Topics/Computer Systems/Processes/File IO]]
- [[Processes]]
- [[Creating New Processes]]

## Tags
#computer-systems #file-descriptors #unix #system-calls #processes