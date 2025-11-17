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
