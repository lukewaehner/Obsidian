---
## Topic:
---
We work with numbers for many tasks: counting, addresses, offsets, switches, etc.  
We (mostly) use **integers** and avoid floating point here.

---

## Decimal (Base 10)
- 10 digits: `0–9`
- Positional, right-to-left: 1s, 10s, 100s, 1000s, …
- Incrementing: carry to next digit after 9
- Example: `9213`

**Formula**  
`aₙ × 10ⁿ + aₙ₋₁ × 10ⁿ⁻¹ + ... + a₀ × 10⁰`

---

## Binary (Base 2)
- 2 digits: `0` and `1`
- Computers understand binary natively
- Same positional system, base 2  
**Example:** `111101₂`

**Formula**  
`aₙ × 2ⁿ + aₙ₋₁ × 2ⁿ⁻¹ + ... + a₀ × 2⁰`

---

## Octal (Base 8)
- Digits: `0–7`
- Example: `371₈`

---

## Hexadecimal (Base 16)
- Digits: `0–9, A–F` (case-insensitive)
- 1 hex digit = 4 binary bits (nibble)

**Example**  
`88E5₁₆ = 1000 1000 1110 0101₂`

| Hex | Binary    |
|-----|-----------|
| 8   | 1000       |
| 8   | 1000       |
| E   | 1110       |
| 5   | 0101       |

---

## Links
- [[CPU Basics]] — binary is CPU-native
- [[Data & Registers]] — binary representation
