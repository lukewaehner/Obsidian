This directory contains notes about operating system kernels, their architecture, and the boot process.

## Core Concepts

- [[Kernel Architecture]] - Kernel space vs user space, protection principles
- [[Monolithic Kernel]] - OS architecture with all services in kernel space
- [[System Calls]] - Interface between user and kernel space

## Boot Process

- [[OS Boot Process]] - Complete boot sequence from power-on to running OS
- [[BIOS]] - Basic Input/Output System firmware
- [[POST]] - Power On Self Test diagnostics
- [[MBR]] - Master Boot Record structure and role

## XV6 Specific

- [[XV6 Boot Sequence]] - XV6's specific boot chain
- [[bootasm.s]] - Assembly boot code and mode transitions
- [[bootmain.c]] - C boot code that loads the kernel

## See Also

- [[Processes]]
- [[Memory Virtualization]]
- [[Concurrency]]

```folder-overview
id: fabc0cad-0cce-41a3-bfa3-3648a40c7d41
folderPath: Code/Computer Systems/Kernels
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
<span class="fv-link-list-start" id="fabc0cad-0cce-41a3-bfa3-3648a40c7d41"></span>
- [[Code/Computer Systems/Kernels/BIOS.md|BIOS]] <span class="fv-link-list-item"></span>
- [[Code/Computer Systems/Kernels/bootasm.s.md|bootasm.s]] <span class="fv-link-list-item"></span>
- [[Code/Computer Systems/Kernels/bootmain.c.md|bootmain.c]] <span class="fv-link-list-item"></span>
- [[Code/Computer Systems/Kernels/Kernel Architecture.md|Kernel Architecture]] <span class="fv-link-list-item"></span>
- [[Code/Computer Systems/Kernels/MBR.md|MBR]] <span class="fv-link-list-item"></span>
- [[Code/Computer Systems/Kernels/Monolithic Kernel.md|Monolithic Kernel]] <span class="fv-link-list-item"></span>
- [[Code/Computer Systems/Kernels/OS Boot Process.md|OS Boot Process]] <span class="fv-link-list-item"></span>
- [[Code/Computer Systems/Kernels/POST.md|POST]] <span class="fv-link-list-item"></span>
- [[Code/Computer Systems/Kernels/System Calls.md|System Calls]] <span class="fv-link-list-item"></span>
- [[Code/Computer Systems/Kernels/XV6 Boot Sequence.md|XV6 Boot Sequence]] <span class="fv-link-list-item"></span>
<span class="fv-link-list-end" id="fabc0cad-0cce-41a3-bfa3-3648a40c7d41"></span>
