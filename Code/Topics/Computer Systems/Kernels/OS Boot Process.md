
# OS Boot Process

The boot process is the sequence of events that occurs when a computer is powered on, leading to a running operating system.

## Boot Sequence Overview

Power On → BIOS → POST → Bootstrap → OS Kernel

## Detailed Process

### 1. Power On
- Computer receives electrical power
- Motherboard initializes

### 2. BIOS Loads
- Motherboard loads BIOS (Basic Input/Output System)
- BIOS is firmware stored in ROM on the motherboard

### 3. BIOS Initialization
- BIOS loads user settings (saved configuration)
- Performs basic tests and configurations
- Establishes initial state of devices

### 4. POST (Power On Self Test)
- Tests CPU, memory, keyboard, and other handlers
- Runs sub-BIOSes on additional hardware devices
- Verifies that essential hardware is functioning

### 5. Bootstrap Sequence
- BIOS scans bootable devices in configured order
- Looks for the Master Boot Record (MBR)
- MBR is the very first block of a storage device
- MBR is a 512-byte block at the beginning of the storage device
- MBR contains boot loader code

### 6. Boot Loader Execution
- Boot loader loads the operating system kernel into memory
- Control transfers to the OS

## Cross References

- [[BIOS]]
- [[POST]]
- [[MBR]]
- [[XV6 Boot Sequence]]
