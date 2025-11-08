---
tags: [algorithms, dynamic-programming, sequences, strings]
---

# Sequences and Subsequences

## Definitions

### Sequence
Collection of things where **order matters** and **repetitions are allowed**.

**Examples**:
- Strings: "MARY", "BOOKKEEPER", "AIBOHPHOBIA", "20250926"
- Number sequences: [0, 1, 1, 2, 3, 5, 8, ...], [..., 256, 512, 1024, 2048, ...], [2, 0, 2, 4, 1, 0, 0, 1]

**Other names**:
- **Lists/Arrays** (usually finite)
- **Streams** (usually infinite)
- **Strings** (for characters)

### Subsequence
Take a sequence, delete some elements, **without changing order**.

**Examples**:
- "BOOKKEEPER" → "OOEEE" or "BKKPR" or "BOOK" or "OOKEE"
- "AIEMCKGOBJF" → "ACGJ" or "IEKG" or "EBJ" or "AMKO"
- (0, 1, 1, 2, 3, 5, 8, ...) → (0, 2, 8, 34, 144, ...) (even Fibonacci numbers)
- $(2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, ...)$ → $(4, 16, 64, 256, 1024, ...)$ ($2^n \to 4^n$)

## Common Subsequences
A subsequence common to a set of sequences.

### Example: 'ACIDES' and 'AICHES'
- **Length 1**: 'A', 'I', 'C', 'E', 'S'
- **Length 2**: 'AC', 'AI', 'AE', 'AS', 'CE', 'ES', 'CS'
- **Length 3**: 'ACE', 'CES', 'AES'
- **Length 4**: 'ACES', 'AIES' ← **Longest Common Subsequences (LCS)**

## Longest Common Subsequence (LCS)
We often care about the **Longest Common Subsequence**.

### Applications
- `diff` between files
- Computational Linguistics
- **Bioinformatics**: Similarity between DNA, RNA, protein sequences
- `git merge`

## Related Topics
- [[Longest Increasing Subsequence]]
- [[Edit Distance and Sequence Alignment]]
- [[Dynamic Programming]]
