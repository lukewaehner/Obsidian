# Virtual Address Translation

## Overview

**Virtual Address Translation** is the process of converting virtual addresses (used by programs) into physical addresses (actual RAM locations).

**Purpose:**
- Isolate processes from each other
- Give each process the illusion of having all memory to itself
- Enable memory protection and sharing

---

## Virtual Address Structure

A virtual address is split into two parts:

### Components

**Virtual Address = Virtual Page Number (VPN) + Offset**

- **VPN (Virtual Page Number)** → Used to index into the page table
- **Offset** → Position within the page (stays the same in physical address)

### Example (4KB pages, 32-bit address)

```
32-bit virtual address:
┌─────────────────────┬────────────┐
│   VPN (20 bits)     │ Offset (12)│
└─────────────────────┴────────────┘
```

**Why 12 bits for offset?**
- 12 bits = 2^12 = 4096 bytes = 4KB page size
- Remaining 20 bits = 2^20 = 1M pages possible

**Address breakdown:**
```
Address 0x00403004:
  Binary: 0000 0000 0100 0000 0011 0000 0000 0100
  
  VPN:    0000 0000 0100 0000 0011 = 0x403
  Offset: 0000 0000 0100           = 0x004
```

---

## Translation Process

### Step-by-Step

1. **Extract VPN** from virtual address
2. **Index into page table** using VPN
3. **Check valid bit** - if 0, page fault occurs
4. **Check permission bits** - if violation, segmentation fault
5. **Get PPN** (Physical Page Number) from page table entry
6. **Combine PPN + Offset** = Physical Address

### Translation Formula

```
Physical Address = (PPN × Page_Size) + Offset
```

**Example:**
```
Virtual Address:  0x00403004
  VPN:    0x403
  Offset: 0x004

Page Table Lookup:
  VPN 0x403 → PPN 0x2A7

Physical Address = (0x2A7 × 4096) + 0x004
                 = 0x2A7004
```

---

## Hardware Support

### Translation Lookaside Buffer (TLB)

**TLB** is a hardware cache that stores recent VPN → PPN translations.

**Purpose:** Speed up address translation
- Avoids expensive page table lookup for every memory access
- Stores most recently used translations

**Operation:**
1. Check TLB for VPN
2. **TLB Hit:** Use cached PPN (fast!)
3. **TLB Miss:** Look up page table (slow), update TLB

**Performance Impact:**
- TLB hit: ~1 cycle
- TLB miss: ~100s of cycles (memory access)
- TLB hit rate: typically 95-99%

### Page Table Base Register (PTBR)

- Special register that points to the page table location in memory
- OS loads PTBR on context switch
- Each process has different page table → different PTBR value

---

## Address Translation with TLB

```
┌─────────────────┐
│ Virtual Address │
└────────┬────────┘
         │
         ▼
    ┌────────┐
    │  TLB   │
    └────┬───┘
         │
    ┌────┴────┐
    │  Hit?   │
    └─┬────┬──┘
 Yes  │    │  No
      ▼    ▼
   ┌─────┐ ┌──────────┐
   │ PPN │ │Page Table│
   └──┬──┘ └─────┬────┘
      │          │ PPN
      └──────┬───┘
             ▼
    ┌─────────────────┐
    │Physical Address │
    └─────────────────┘
```

---

## Multi-Level Translation

For large address spaces, use **multi-level page tables**:

### Two-Level Example

```
Virtual Address:
┌──────────┬──────────┬────────┐
│ L1 Index │ L2 Index │ Offset │
└──────────┴──────────┴────────┘
```

**Translation:**
1. Use L1 Index to find L2 page table
2. Use L2 Index to find PPN
3. Combine PPN + Offset

**Benefit:** Only allocate page tables for used memory regions

---

## Related Concepts

- [[Page Tables]]
- [[Paging]]
- [[Memory Protection]]
- [[TLB and Caching]]

## Tags
#computer-systems #virtual-memory #address-translation #paging #tlb