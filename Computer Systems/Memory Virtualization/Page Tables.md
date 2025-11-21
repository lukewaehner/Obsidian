# Page Tables

## Overview

A **page table** is a data structure that maps virtual page numbers to physical page numbers (or physical frame numbers).

**Key Properties:**
- Each process has its own page table
- Stored in kernel memory
- Contains page table entries (PTEs)

---

## Page Table Entry (PTE)

Each entry in the page table contains:

### Essential Fields

**1. Valid/Present Bit**
- **1** = Page is in physical memory
- **0** = Page not in memory (triggers page fault)

**2. Physical Page Number (PPN) / Physical Frame Number (PFN)**
- Identifies which physical page this virtual page maps to
- Most significant bits of the physical address

**3. Permission Bits**
- **R (Read)** - Can read from this page
- **W (Write)** - Can write to this page
- **X (Execute)** - Can execute code from this page

**4. Dirty Bit**
- **1** = Page has been modified (written to)
- **0** = Page is clean (not modified)
- Used for page replacement (don't need to write clean pages back to disk)

**5. Reference/Access Bit**
- **1** = Page has been accessed (read or written)
- **0** = Page has not been recently accessed
- Used by page replacement algorithms (LRU, etc.)

### Optional Fields

- **User/Supervisor bit** - Can user-mode access this page?
- **Write-through/Write-back** - Caching policy
- **Cache disable** - Don't cache this page
- **Global bit** - Don't flush from TLB on context switch

---

## PTE Structure Example

```
┌───┬───┬───┬───┬───┬─────────────────────┐
│ V │ R │ W │ X │ D │  PPN (20 bits)      │
└───┴───┴───┴───┴───┴─────────────────────┘
 │   │   │   │   │          │
 │   │   │   │   │          └─ Physical page number
 │   │   │   │   └──────────── Dirty bit
 │   │   │   └──────────────── Execute permission
 │   │   └──────────────────── Write permission
 │   └──────────────────────── Read permission
 └──────────────────────────── Valid bit
```

---

## Page Table Organization

### Linear Page Table

**Simplest approach:**
- Array of PTEs indexed by VPN
- Size = Number of virtual pages × sizeof(PTE)

**Problem for 32-bit address space:**
```
Virtual pages = 2^32 / 4KB = 2^20 = 1M pages
Page table size = 1M × 4 bytes = 4MB per process
```

**Problem for 64-bit address space:**
```
Virtual pages = 2^64 / 4KB = 2^52 pages
Page table size = 2^52 × 8 bytes = 32 PB per process! 
```
This is infeasible!

---

## Multi-Level Page Tables

**Solution:** Use hierarchy to only allocate what's needed

### Two-Level Page Table

```
┌──────────────────────────────────┐
│      Page Directory (L1)         │
│  (1024 entries, always resident) │
└─────────┬────────────────────────┘
          │
          ├──→ Page Table (L2) #0
          ├──→ Page Table (L2) #1
          ├──→ Page Table (L2) #2
          │    ...
          └──→ Page Table (L2) #1023
```

**Virtual Address Split:**
```
┌────────────┬────────────┬────────────┐
│ L1 Index   │ L2 Index   │   Offset   │
│ (10 bits)  │ (10 bits)  │  (12 bits) │
└────────────┴────────────┴────────────┘
```

**Translation:**
1. Use L1 index to find L2 page table address
2. Use L2 index to find PPN
3. Combine PPN + offset

**Benefits:**
- Only allocate L2 tables for used regions
- Page directory is small (4KB)
- Huge savings for sparse address spaces

**Example:**
```
If process only uses:
- Code segment: 0x00400000-0x00500000
- Stack: 0xFFFF0000-0xFFFFFFFF

Only need 2 L2 page tables instead of 1024!
Savings: 4KB + 8KB vs 4MB
```

---

## Page Table Location

**Stored in physical memory (kernel space):**
- Page tables are per-process
- OS keeps track of each process's page table base address
- Page Table Base Register (PTBR) points to current process's page table

**Context Switch:**
1. Save current PTBR value
2. Load new process's PTBR
3. Flush TLB (unless using ASIDs)

---

## Accessing the Page Table

### Without TLB (Slow)

For each memory access:
1. Read PTBR to get page table base
2. Calculate PTE address = PTBR + (VPN × sizeof(PTE))
3. Read PTE from memory
4. Extract PPN
5. Calculate physical address
6. Access actual memory

**Total:** 2 memory accesses per instruction memory access!

### With TLB (Fast)

1. Check TLB for VPN
2. If hit: Get PPN directly (0 extra memory accesses)
3. If miss: Do page table walk, cache in TLB

**Typical TLB hit rate: 95-99%**
- Average extra memory accesses ≈ 0.01-0.05 per access

---

## Page Table Permissions

Different memory regions have different permissions:

| Region      | Read | Write | Execute |
|-------------|------|-------|---------|
| **Code**    | ✓    | ✗     | ✓       |
| **Data**    | ✓    | ✓     | ✗       |
| **Stack**   | ✓    | ✓     | ✗       |
| **Heap**    | ✓    | ✓     | ✗       |

**Why no execute on data/stack/heap?**
- **Security:** Prevents code injection attacks
- If attacker puts shellcode on stack, it won't execute
- Called **NX bit** (No eXecute) or **DEP** (Data Execution Prevention)

---

## Page Table in xv6

```c
// Page table entry
typedef uint pte_t;

// Page directory entry
typedef pte_t pde_t;

// Flags in PTE
#define PTE_P    0x001  // Present
#define PTE_W    0x002  // Writeable  
#define PTE_U    0x004  // User
#define PTE_PS   0x080  // Page Size
#define PTE_MBZ  0x180  // Must Be Zero

// Address in page table entry
#define PTE_ADDR(pte)   ((uint)(pte) & ~0xFFF)
#define PTE_FLAGS(pte)  ((uint)(pte) &  0xFFF)
```

---

## Related Concepts

- [[Virtual Address Translation]]
- [[Paging]]
- [[Memory Protection]]
- [[TLB and Caching]]
- [[Multi-Level Page Tables]]

## Tags
#computer-systems #virtual-memory #page-tables #paging #memory-management