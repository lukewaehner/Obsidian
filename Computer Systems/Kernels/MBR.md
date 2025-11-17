
# MBR (Master Boot Record)

The Master Boot Record is a special 512-byte block located at the very first sector of a storage device. It plays a critical role in the boot process.

## Location

- Very first block of a storage device
- Located at sector 0, cylinder 0, head 0
- Present on bootable disks (hard drives, SSDs, USB drives)

## Size

512 bytes exactly - a constraint from early PC architecture that persists today.

## Contents

The MBR typically contains:

**Boot Loader Code (446 bytes):**
- Small program that loads the actual OS boot loader
- Limited by the 512-byte constraint
- Often just loads a larger, more capable boot loader

**Partition Table (64 bytes):**
- Describes disk partitions
- Up to 4 primary partition entries

**Boot Signature (2 bytes):**
- Magic number `0x55AA` at the end
- Indicates this is a valid boot sector

## Role in Boot Process

1. After POST completes, BIOS scans bootable devices
2. BIOS reads the first 512 bytes (MBR) from each device
3. Checks for valid boot signature
4. If valid, executes the boot loader code from the MBR
5. Boot loader then loads the full operating system kernel

## Cross References

- [[OS Boot Process]]
- [[BIOS]]
- [[XV6 Boot Sequence]]
