---
type: problem
source: neetcode
number: 150
url: https://neetcode.io/problems/evaluate-reverse-polish-notation
difficulty: Medium
pattern: Stack
patterns: ["Stack"]
topics: ["[[Career/Prep/topics/Data Structures/Stacks|Stacks]]"]
solved_on: 2026-09-01
attempts: 1
aid: unaided
revisit: false
time: O(n)
space: O(n)
language: python
---

# 150 · Evaluate Reverse Polish Notation

> [!question]- Problem
> Evaluate an arithmetic expression in Reverse Polish Notation.

## Idea

RPN has no precedence and no parentheses — an operator always applies to the two most recent values, which is exactly what a stack hands you.

## Optimal

```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ['+', '-', '*', '/']
        for t in tokens:
            if t in ops:
                val1 = stack.pop()
                val2 = stack.pop()
                res = None
                if t == '+':
                    res = val2 + val1
                if t == '-':
                    res = val2 - val1
                if t == '*':
                    res = val2 * val1
                if t == '/':
                    res = int(val2 / val1)
                print(res)
                stack.append(res)
            else:
                stack.append(int(t))
            # print(stack)
        return stack.pop()
```

> [!warning] Defect
> `print(res)` on line 18 is live debug output, not a comment — it runs on
> every operator and floods stdout. Same slip as the one in
> [[Career/Prep/problems/Two Pointers/125 · Valid Palindrome|125 · Valid Palindrome]].
> Delete it. The commented-out `# print(stack)` below it is fine.

## Why it works

The reason RPN is a stack problem and infix is not: infix needs precedence and
parentheses to know *which* operands an operator binds to. RPN removes that
question by construction — the operands are always the two most recently
produced values, whether they were literals or the results of earlier
operations. So a single left-to-right pass with a stack evaluates it exactly.

Two details are easy to get wrong and both are right here:

**Operand order.** `val1` is popped first, so it is the **right** operand;
`val2` is the left. Hence `val2 - val1` and `val2 / val1`. Getting this
backwards passes the `+` and `*` tests and fails on `-` and `/`, which is a
nasty way to lose a submission.

> [!tip] `int(val2 / val1)` is the correct choice, and `//` would be wrong
> This problem specifies truncation **toward zero**. Python's `//` floors
> toward negative infinity, so `-7 // 2 == -4` where the problem wants `-3`.
> `int(a / b)` truncates toward zero and gives `-3`. Using `//` here is one of
> the most common ways to fail this problem, and you avoided it.
>
> The caveat worth knowing: `int(a / b)` goes through a float, so it loses
> exactness beyond 2⁵³. Fine within these constraints; `int(operator.truediv)`
> has the same issue. The exact-integer version is
> `-(-a // b) if (a < 0) != (b < 0) else a // b`.

## Template

```python
for t in tokens:
    if t in OPS:
        b = stack.pop()   # right operand
        a = stack.pop()   # left operand
        stack.append(apply(a, t, b))
    else:
        stack.append(int(t))
return stack.pop()
```

## Mistakes I made

Solved unaided, but the submission index says it took a while to land. The two
likely time sinks are exactly the two details above — operand order, and the
division semantics. Both are worth recognising on sight next time rather than
rediscovering.

Also: a chain of four `if`s rather than `elif` means all four are tested on
every operator. Harmless at this size, but `elif` says "these are mutually
exclusive", which is the thing a reader wants to know.

## Related

- [[Career/Prep/problems/Stack/20 · Valid Parentheses|20 · Valid Parentheses]] — the same LIFO structure, matching instead of evaluating
- [[Career/Prep/topics/Data Structures/Stacks|Stacks]]
