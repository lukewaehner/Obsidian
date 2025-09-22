- Duplicate the value is a cheap, bitwise copy, no resource ownership issues
- Integer (i64, u128,), bool, small tuples of Copy stuff, and enums without heap data are Copy
- String is not Copy because it owns heap memory.
- Moving a string transfers ownership of that buffer; implicit copying would risk double-free. Use Clone when you truly want another owned buffer

---
