---
type: problem
source: neetcode
number: 271
url: https://neetcode.io/problems/string-encode-and-decode
difficulty: Medium
pattern: Arrays & Hashing
patterns: ["Arrays & Hashing"]
topics: ["[[Career/Prep/topics/Strings/String Manipulation|String Manipulation]]", "[[Career/Prep/topics/Data Structures/Arrays|Arrays]]"]
solved_on: 2026-08-31
attempts: 2
aid: unaided
revisit: false
time: O(n) both ways, over total characters
space: O(n)
language: python
---

# 271 · Encode and Decode Strings

> [!question]- Problem
> Encode a list of strings to a single string, and decode it back. The strings may contain any characters.

## Idea

Prefix each string with its length and a delimiter — then the decoder never has to guess where a string ends, so the content is free to contain anything.

## Optimal

The first accepted version:

```python
class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res 
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j+= 1
            length = int(s[i:j])
            i = j+1
            j = i + length
            res.append(s[i:j])
            i = j
        return res
```

A later pass, same scheme with the decode pointer arithmetic written out
step by step instead of reusing `i` and `j`:

```python
class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for i in range(len(strs)):
            ret += str(len(strs[i]))
            ret += "#"
            ret += strs[i]
        return ret
    
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            res.append(s[j+1 : j+1+length])
            i = j + 1 + length
        return res
```

## Why it works

The trap in this problem is reaching for a delimiter alone — `","` or `"#"` —
which breaks the moment a string contains that character. No choice of
delimiter is safe, because the input is unrestricted.

Length-prefixing sidesteps it entirely. The decoder reads digits until it hits
`#`, and that count tells it exactly how many characters to consume next,
*without interpreting them*. A `#` inside the payload is just a character,
because the decoder is counting rather than scanning for a terminator. The `#`
is unambiguous only because it is always preceded by a length and never
searched for inside the payload.

This is the same principle as length-prefixed framing in network protocols —
worth naming in an interview, since it shows the idea generalises past the
puzzle.

## Template

```python
# encode
"".join(str(len(s)) + "#" + s for s in strs)

# decode
i = 0
while i < len(s):
    j = i
    while s[j] != '#':
        j += 1
    length = int(s[i:j])
    res.append(s[j + 1 : j + 1 + length])
    i = j + 1 + length
```

## Mistakes I made

Nothing wrong in either accepted version — both are correct and the same
complexity. The second is arguably the one to keep: computing
`s[j+1 : j+1+length]` in a single slice avoids the pointer reshuffling of the
first, and there is one less place to make an off-by-one.

The high submission count was mostly the fight to get the framing idea, not
bugs in the framing once it clicked.

## Related

- Length-prefixed framing appears again in serialisation problems — see [[Career/Prep/topics/Design/Messaging, Serialization, and Queues|Messaging, Serialization, and Queues]]
