---
type: problem
source: neetcode
number: 2
url: https://neetcode.io/problems/add-two-numbers
difficulty: Medium
pattern: Linked List
patterns: ["Linked List"]
topics: ["[[Career/Prep/topics/Data Structures/Linked Lists|Linked Lists]]"]
solved_on: 2026-09-08
attempts: 3
aid: unaided
revisit: false
time: O(max(n, m))
space: O(1) extra, excluding the output list
language: python
---

# 2 · Add Two Numbers

> [!question]- Problem
> Two non-empty linked lists represent non-negative integers with the digits stored in reverse order. Add them and return the sum as a linked list in the same form.

## Idea

The lists are already stored least-significant-digit first, which is exactly the
order long addition wants — so walk both at once and carry.

## Naive

Decode both lists into Python ints, add, re-encode:

```python
class Solution:
    def build_number(self, l):
        s = []
        while l:
            s.append(l.val)
            l = l.next
        res = 0
        i = 0
        while i < len(s):
            v = s[i]
            res += v * (10 ** i)
            i += 1
        return res

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        nv = str(self.build_number(l1) + self.build_number(l2))

        d = n = ListNode()
        for c in nv[::-1]:
            n.next = ListNode(c)
            n = n.next
        return d.next
```

> [!warning] Defect
> `for c in nv[::-1]` iterates a string, so `ListNode(c)` stores the **character**
> `'7'`, not the integer `7`. Every node in the returned list holds a `str`, and
> any judge that compares values with `==` reports a wrong answer even though the
> arithmetic was right. The fix is one call:
>
> ```python
> n.next = ListNode(int(c))
> ```
>
> The second problem is not a bug in Python but is one everywhere else: this
> approach only works because Python integers are arbitrary-precision. The same
> code in Java or C++ overflows a 64-bit integer at 20 digits, and the problem's
> constraints allow 100. **An approach that depends on the language's bignum is
> not an approach to this problem** — it is a way of not solving it.

## Optimal

```python
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        d = m = ListNode()
        c = 0

        while l1 or l2 or c:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            passVal = v1 + v2 + c
            dig = passVal % 10 # the end digit of the value
            c = passVal // 10 # if we have any carryover to move to the next digit during creation
            newNode = ListNode(dig)

            m.next = newNode
            m = m.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return d.next
```

## Why it works

Reverse storage is the gift the problem is handing you. Written on paper, addition
starts at the ones column and carries left; a list whose head *is* the ones digit
lets you do that with a single forward walk and no reversal at either end.

The loop condition is where all three edge cases collapse into one:

```python
while l1 or l2 or c:
```

- `l1 or l2` — lists of unequal length. The shorter one runs out and contributes
  `0` from then on, via the `if l1 else 0` guards. No padding pass, no length
  comparison.
- `c` — the final carry. `[9] + [1]` produces a digit `0` and a carry that has no
  column left to land in; without the `or c` the leading `1` is silently dropped.
  This is the single most common wrong answer on this problem.

`divmod` states the two lines more directly — `c, dig = divmod(v1 + v2 + c, 10)` —
and the carry is provably `0` or `1`, since the largest possible column is
`9 + 9 + 1 = 19`.

The dummy head `d` exists so the first append needs no special case. `m` walks
the tail; `d.next` is the real head, and `d` itself is discarded.

## Template

The dummy-head builder, which shows up in nearly every list-construction problem:

```python
dummy = tail = ListNode()
while ...:
    tail.next = ListNode(value)
    tail = tail.next
return dummy.next
```

## Mistakes I made

The first two attempts solved a different problem: *convert, add, convert back*.
It passes, which is the trap — the failure only shows up when the input outgrows
the machine integer, and Python hides that boundary. The digit-wise walk is not
merely tidier; it is the version that has no upper bound on input size.

Within that first approach, `ListNode(c)` on a string digit is the smaller lesson:
`str(n)` gives you characters, and a character that prints like a digit is not one.

## Related

- [[Career/Prep/problems/Linked List/21 · Merge Two Sorted Lists|21 · Merge Two Sorted Lists]] — same dummy-head build, consuming two lists in lockstep
- [[Career/Prep/topics/Data Structures/Linked Lists|Linked Lists]]
