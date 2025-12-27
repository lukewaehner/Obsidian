

System calls for interacting with files and directories.

---

## File Operations

| Call      | Description                                      |
| --------- | ------------------------------------------------ |
| `open`    | Open a file, returns file descriptor             |
| `close`   | Close a file descriptor                          |
| `read`    | Read bytes from a file                           |
| `write`   | Write bytes to a file                            |
| `lseek`   | Move position within a file                      |
| `fsync`   | Flush buffer to file (force write to disk)       |
| `rename`  | Rename a file                                    |
| `stat`    | Get metadata about a file                        |
| `link`    | Associate another name with file data (hardlink) |
| `unlink`  | Remove a reference to a file / delete            |

---

## Directory Operations

| Call       | Description                    |
| ---------- | ------------------------------ |
| `mkdir`    | Create a directory             |
| `rmdir`    | Remove a directory             |
| `opendir`  | Open a directory for reading   |
| `readdir`  | Read directory entries         |
| `closedir` | Close a directory              |

---

## Code Example: Basic File Operations

```c
#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>

int main() {
    // Open file (create if needed)
    int fd = open("test.txt", O_RDWR | O_CREAT | O_TRUNC, 0644);
    if (fd < 0) {
        perror("open");
        return 1;
    }
    
    // Write to file
    const char *msg = "Hello, File Systems!";
    write(fd, msg, strlen(msg));
    
    // Seek back to beginning
    lseek(fd, 0, SEEK_SET);
    
    // Read from file
    char buf[100];
    ssize_t n = read(fd, buf, sizeof(buf) - 1);
    buf[n] = '\0';
    printf("Read: %s\n", buf);
    
    // Close file
    close(fd);
    
    return 0;
}
```

---

## Code Example: Reading a Directory

```c
#include <stdio.h>
#include <dirent.h>

int main() {
    DIR *dir = opendir(".");
    if (dir == NULL) {
        perror("opendir");
        return 1;
    }
    
    struct dirent *entry;
    while ((entry = readdir(dir)) != NULL) {
        // d_type: DT_REG = file, DT_DIR = directory
        char type = (entry->d_type == DT_DIR) ? 'd' : 'f';
        printf("[%c] %s (inode: %lu)\n", type, entry->d_name, entry->d_ino);
    }
    
    closedir(dir);
    return 0;
}
```

---

## Code Example: Creating Hard Links

```c
#include <stdio.h>
#include <unistd.h>
#include <sys/stat.h>

int main() {
    // Create original file
    FILE *f = fopen("original.txt", "w");
    fprintf(f, "Shared content\n");
    fclose(f);
    
    // Create hard link (same inode, different name)
    if (link("original.txt", "hardlink.txt") == 0) {
        printf("Hard link created\n");
    }
    
    // Both files share the same inode
    struct stat sb1, sb2;
    stat("original.txt", &sb1);
    stat("hardlink.txt", &sb2);
    
    printf("original.txt inode: %lu\n", sb1.st_ino);
    printf("hardlink.txt inode: %lu\n", sb2.st_ino);
    printf("Same inode: %s\n", (sb1.st_ino == sb2.st_ino) ? "yes" : "no");
    
    // Unlink removes one reference
    unlink("hardlink.txt");
    // File still exists via original.txt
    
    return 0;
}
```

---

## File System Implementation

File systems are implemented as drivers, but they don't abstract hardware directly:

- **Block device drivers** fill the layer below file systems
- Provide software abstraction over lower-level storage APIs

**File system responsibilities:**

1. **Translation** - Translate name + offset to appropriate disk partition
2. **Free space management** - Track where to store data

**Designing a file system requires deciding:**
- Data structures
- Access methods

---

## Related

- [[File Systems]]
- [[Code/Topics/Computer Systems/Processes/File IO|File I/O]]
- [[File Descriptors|File Descriptors]]
- [[Inodes]]

---

#computer-systems #file-systems #system-calls