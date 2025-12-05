

## Overview

**Paging** is a memory management scheme that allows a process's physical memory to be non-contiguous. Memory is divided into fixed-size blocks called **pages**.

**Key Concept:** Virtual memory doesn't have to be in physical memory all at once.

---

## Page Basics

### Page Size

**Typical page size: 4KB (4096 bytes)**

**Why 4KB?**
- Small enough to avoid too much internal fragmentation
- Large enough to keep page table size reasonable
- Trade-off between table size and wasted space

**Other common sizes:**
- 4KB - Most common (x86, ARM)
- 8KB - Some ARM systems
- 16KB - Apple Silicon (M1/M2)
- 2MB/4MB - "Huge pages" for special purposes

---

## Page Fault

A **page fault** occurs when a program accesses a page that is not currently in physical memory.

### When Page Faults Happen

**Valid bit = 0 (page not present):**
- Page has never been accessed
- Page was swapped out to disk
- Page is in another process's memory (shouldn't happen!)

### Page Fault Handling

**OS page fault handler:**

1. **Trap to kernel** (hardware generates page fault exception)
2. **Save process state** (registers, PC)
3. **Determine cause:**
   - Invalid address? → Segmentation fault (kill process)
   - Valid address, just not in memory? → Continue
4. **Find free physical page** (or evict one)
5. **Load page from disk** into physical memory
6. **Update page table entry:**
   - Set PPN to physical page
   - Set valid bit to 1
7. **Restart instruction** that caused the fault

### Performance Impact

**Page faults are expensive:**
- Disk I/O: ~5-10 milliseconds (millions of cycles!)
- Compare to memory access: ~100 nanoseconds

**This is why page replacement algorithms matter**

---

## Demand Paging

**Demand paging** = Load pages into memory only when needed (on first access)

### How It Works

**Process startup:**
1. Create page table with all valid bits = 0
2. Don't load any pages yet
3. When process accesses page → page fault → load page

**Benefits:**
- Faster process startup
- Use memory efficiently (only load what's needed)
- Can run programs larger than physical memory

**Lazy Loading:**
```
Process starts
  │
  ├─ Access code page → Page fault → Load code
  ├─ Access data page → Page fault → Load data
  ├─ Access stack page → Page fault → Load stack
  └─ Many pages never accessed → Never loaded!
```

### Example

```c
int main() {
    int huge_array[1000000];  // 4MB array
    
    // Array pages NOT in memory yet (demand paging)
    
    huge_array[0] = 42;       // Page fault! Load page
    huge_array[1000] = 43;    // Maybe another page fault
    
    // Only accessed pages are loaded into memory
    return 0;
}
```

---

## Page Replacement

When physical memory is full and we need to load a new page, we must **evict** an existing page.

### Common Algorithms

**1. FIFO (First In, First Out)**
- Evict oldest page
- Simple but not always effective

**2. LRU (Least Recently Used)**
- Evict page that hasn't been used for longest time
- Better performance but more complex

**3. Clock/Second Chance**
- Approximate LRU using reference bit
- Practical and widely used

**4. Random**
- Pick random page to evict
- Surprisingly effective in some cases!

### Reference Bit

Hardware sets **reference bit** when page is accessed:
- OS periodically clears all reference bits
- Pages with reference bit = 0 haven't been used recently
- Good candidates for eviction

---

## Translation Lookaside Buffer (TLB)

The **TLB** is a hardware cache that stores recent virtual → physical translations.

### Why We Need TLB

**Without TLB:**
```
Every memory access requires:
1. Read page table from memory (1 memory access)
2. Read actual data from memory (1 memory access)

Total: 2× slower!
```

**With TLB:**
```
TLB hit (95-99% of time):
1. Get translation from TLB (1 cycle)
2. Read actual data from memory (1 memory access)

Effectively same speed as no virtual memory!
```

### TLB Structure

**Typical TLB:**
- 64-512 entries
- Fully associative or set-associative
- Hardware managed (x86) or software managed (MIPS)

**TLB Entry:**
```
┌─────┬─────┬───────────┬────────────┐
│ VPN │ PPN │ Valid bit │ Protection │
└─────┴─────┴───────────┴────────────┘
```

### TLB Operation

```
Memory access with virtual address:
  │
  ├─ Check TLB for VPN
  │
  ├─ TLB Hit (95-99%)
  │   └─ Use PPN directly → Fast!
  │
  └─ TLB Miss (1-5%)
      └─ Walk page table
      └─ Update TLB
      └─ Retry access
```

### TLB Management

**On context switch:**
- **Flush TLB** (simple but slow)
- **Use ASID** (Address Space ID) to tag entries

**On page table update:**
- Invalidate affected TLB entries
- `invlpg` instruction on x86

---

## Page Table Walk

When TLB misses, hardware (or OS) must walk the page table:

### Single-Level Walk

```c
// Simplified x86-style page table walk
uint translate(uint va) {
    uint vpn = va >> 12;           // Extract VPN
    uint offset = va & 0xFFF;      // Extract offset
    
    pte_t *pt = read_ptbr();       // Get page table base
    pte_t pte = pt[vpn];           // Look up PTE
    
    if (!(pte & PTE_P)) {
        page_fault();               // Not present!
    }
    
    uint ppn = pte >> 12;          // Extract PPN
    return (ppn << 12) | offset;   // Physical address
}
```

### Multi-Level Walk (x86-64)

x86-64 uses 4-level page tables:
```
Virtual Address:
┌────┬────┬────┬────┬────────┐
│ L4 │ L3 │ L2 │ L1 │ Offset │
└────┴────┴────┴────┴────────┘

4 memory accesses to translate (without TLB)!
```

---

## Paging Performance

### Best Case (TLB Hit)
- Translation: ~1 cycle
- Memory access: ~100 cycles
- Total: ~100 cycles

### Worst Case (TLB Miss + Page Fault)
- TLB miss: ~100 cycles (page table walk)
- Page fault: ~10 million cycles (disk I/O)
- Total: ~10 million cycles

**100,000× slower!**

### Optimization Strategies

1. **Large pages** - Reduce TLB pressure
2. **Better page replacement** - Reduce page faults
3. **Prefetching** - Load pages before they're needed
4. **Page clustering** - Bring in multiple pages at once

---

## Paging in xv6

xv6 uses two-level page tables:

```c
// Set up kernel page table
pde_t* setupkvm(void) {
    pde_t *pgdir;
    
    if((pgdir = (pde_t*)kalloc()) == 0)
        return 0;
    memset(pgdir, 0, PGSIZE);
    
    // Map kernel
    if(mappages(pgdir, (void*)KERNBASE, PHYSTOP-KERNBASE, 
                0, PTE_W) < 0) {
        freevm(pgdir);
        return 0;
    }
    return pgdir;
}
```

---

## Related Concepts

- [[Page Tables]]
- [[Virtual Address Translation]]
- [[Memory Protection]]
- [[Shared Memory]]

## Tags
#computer-systems #virtual-memory #paging #page-faults #tlb #demand-paging