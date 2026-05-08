File systems solve the problem of organizing persistent data on storage devices. Without them, long-term storage would be a linear array of bytes with no structure.

---

## Core Concepts

- [[Storage Devices]] - Physical storage mediums and their representations
- [[Blocks and Regions]] - How disk space is divided and organized
- [[Inodes]] - File metadata and block addressing
- [[Multi-Level Indexing]] - Handling large files with indirect pointers

---

## File System API

- [[File System API]] - System calls for files and directories

---

## Directory Structure

Modern file systems have two abstractions:

**File** - A collection of bytes read and written, accessed by name

**Directory** - A collection of files and other directories

This gives rise to a tree-shaped organization:

```
                   foo/
                    |
          +-----+---+---+--------+
          |     |       |        |
         bar/  baz/  info.txt hello.c        
          |     |
      img.png   |
                |
       +--------+-------+-------+-------+
       |        |       |       |       |
    meme.gif run.sh items.csv main.s letter.docx
```

---

## Key Observations

- Most files are small (2K common size)
- Average file size is growing (~200K)
- Most bytes are in large files (a few big files use most space)
- File systems contain ~100K files on average
- File systems are roughly half full
- Directories are small (most have 20 or fewer entries)

---

## Related Topics

- [[Code/Topics/Computer Systems/Processes/File IO|File I/O]] - Reading and writing files
- [[File Descriptors|File Descriptors]] - Low-level file handles
- [[Kernels|Kernels]] - Operating system core

---

#computer-systems #file-systems

```folder-overview
id: 660a5470-c7aa-4cff-9248-e13abf93a6eb
folderPath: Code/Computer Systems/File Systems
title: "{{folderName}} overview"
showTitle: false
depth: 1
includeTypes:
  - folder
  - markdown
style: list
disableFileTag: false
sortBy: name
sortByAsc: true
showEmptyFolders: false
onlyIncludeSubfolders: false
storeFolderCondition: true
showFolderNotes: false
disableCollapseIcon: true
alwaysCollapse: false
autoSync: true
allowDragAndDrop: true
hideLinkList: true
hideFolderOverview: false
useActualLinks: true
fmtpIntegration: false
titleSize: 1
isInCallout: false
useWikilinks: true
```
<span class="fv-link-list-start" id="660a5470-c7aa-4cff-9248-e13abf93a6eb"></span>
- [[Code/Computer Systems/File Systems/Blocks and Regions.md|Blocks and Regions]] <span class="fv-link-list-item"></span>
- [[Code/Computer Systems/File Systems/File System API.md|File System API]] <span class="fv-link-list-item"></span>
- [[Code/Computer Systems/File Systems/Inodes.md|Inodes]] <span class="fv-link-list-item"></span>
- [[Code/Computer Systems/File Systems/Multi-Level Indexing.md|Multi-Level Indexing]] <span class="fv-link-list-item"></span>
- [[Code/Computer Systems/File Systems/Storage Devices.md|Storage Devices]] <span class="fv-link-list-item"></span>
<span class="fv-link-list-end" id="660a5470-c7aa-4cff-9248-e13abf93a6eb"></span>
