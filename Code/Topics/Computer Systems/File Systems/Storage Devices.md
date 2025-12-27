

Persistent storage devices allow storing non-volatile data. Data is stored as a sequence of bits with some physical representation.

---

## Types of Storage

**Magnetic**
- HDDs (Hard Disk Drives)
- Floppy disks
- Tape drives

**Optical**
- CDs
- DVDs

**Electronic**
- SSDs (Solid State Drives)

---

## Low-Level View

From a low-level perspective, data is stored as a sequence of bytes, usually organized in blocks.

Long-term storage in a linear array would be problematic:
- File growth becomes difficult to manage
- No clear place to add new data
- No organization structure

This is solved with [[File Systems]].

---

## Disk Organization

The beginning of a disk has standardized contents, including the Master Boot Record (MBR).

See: [[MBR|MBR (Master Boot Record)]]

---

## Related

- [[File Systems]]
- [[Blocks and Regions]]

---

#computer-systems #file-systems #storage