

An inode (index node) stores metadata about a file and pointers to its data blocks.

---

## I-Number

Each inode has an **i-number** (low-level identifier) which is its index in the inode table.

Given an index, the location of an inode on disk can be calculated:

```
blk = (inumber * sizeof(inode_t)) / blockSize
sector = ((blk * blockSize) + inodeStartAddr) / sectorSize
```

---

## Block Pointers

An inode contains an array of block pointers (addresses) for the file's data:

```
foo.txt:          +-+
          +------>| |
 +-+      |       |-|
 | |------+       | |
 |-|              |-|
 | |-----+  +---->| |
 |-|     |  |     |-|
 | |-----|--|---->| |
 +-+     |  |     |-|
         +--|---->| |
bar.txt:    |     |-|
 +-+        |     | |
 | |----+   |     |-|
 |-|    |   |     | |
 | |----|---+     |-|
 +-+    +-------->| |
                  +-+
```

---

## Inode Contents (ext2 Example)

| Size | Name        | Purpose                                    |
| ---- | ----------- | ------------------------------------------ |
| 2    | mode        | can this file be r/w/x                     |
| 2    | uid         | who owns the file                          |
| 4    | size        | how many bytes                             |
| 4    | time        | last access                                |
| 4    | ctime       | when was the file created                  |
| 4    | mtime       | what time was the file last modified       |
| 4    | dtime       | what time was the inode deleted            |
| 2    | gid         | which group does this file belong to       |
| 2    | links_count | how many hard links are there to this file |
| 4    | blocks      | how many blocks allocated                  |
| 4    | flags       | how should ext2 use the inode              |
| 4    | osd1        | OS-dependent field                         |
| 60   | block       | set of disk pointers (15 total for 32-bit) |
| 4    | generation  | file version (used by NFS)                 |
| 4    | file_acl    | a new permission mode beyond mode bits     |
| 4    | dir_acl     | called access control lists                |

---

## Code Example: Getting Inode Info with stat()

```c
#include <stdio.h>
#include <sys/stat.h>

int main() {
    struct stat sb;
    
    if (stat("example.txt", &sb) == 0) {
        printf("Inode number: %lu\n", sb.st_ino);
        printf("File size: %ld bytes\n", sb.st_size);
        printf("Blocks allocated: %ld\n", sb.st_blocks);
        printf("Block size: %ld\n", sb.st_blksize);
        printf("Hard links: %lu\n", sb.st_nlink);
        printf("Owner UID: %d\n", sb.st_uid);
        printf("Permissions: %o\n", sb.st_mode & 0777);
    }
    
    return 0;
}
```

---

## Limitation

There's a limited number of direct pointers in an inode. For files bigger than what direct pointers can address, see [[Multi-Level Indexing]].

---

## Related

- [[File Systems]]
- [[Blocks and Regions]]
- [[Multi-Level Indexing]]

---

#computer-systems #file-systems #inodes