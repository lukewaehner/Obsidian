---
type: problem
source: neetcode
number: 20
url: https://neetcode.io/problems/validate-parentheses
difficulty: Easy
pattern: Stack
patterns: ["Stack"]
topics: ["[[Career/Prep/topics/Data Structures/Stacks|Stacks]]", "[[Career/Prep/topics/Strings/String Manipulation|String Manipulation]]"]
solved_on: 2026-09-01
attempts: 2
aid: unaided
revisit: false
time: O(n)
space: O(n)
language: python
---

# 20 · Valid Parentheses

> [!question]- Problem
> Determine if a string of `()[]{}` is validly nested and closed.

## Idea

The most recently opened bracket is always the one that must close next — which is the definition of a stack.

## Naive

The first version. Correct, with the matching written out longhand:

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closes = [')', '}', ']']
        opens = ['(', '[', '{']
        for c in s:
            if c in opens:
                stack.append(c)
                continue
            if not stack:
                return False
            curr = stack[-1]
            if c == ')' and curr == '(':
                stack.pop()
            elif c == '}' and curr == '{':
                stack.pop()
            elif c == ']' and curr == '[':
                stack.pop()
            else:
                return False
        if not stack:
            return True
        else:
            return False
```

## Optimal

The second pass, same algorithm with the three-way comparison replaced by a
lookup:

```python
class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', ']': '[', '}': '{'}
        stack = []

        for c in s:
            if c in pairs:
                if not stack or stack.pop() != pairs[c]:
                    return False
            else:
                stack.append(c)

        return not stack
```

## Why it works

Nesting is last-in-first-out by definition — `([)]` is invalid precisely
because the `)` tries to close something that is not on top. So the stack is
not a trick here, it is the direct encoding of what "properly nested" means.

Three conditions have to hold, and the compact version checks all of them:

- a closer with an **empty stack** has nothing to match → `not stack`
- a closer whose top **does not correspond** → `stack.pop() != pairs[c]`
- a **leftover** open bracket at the end → `return not stack`

The refactor is worth studying as a refactor. The first version encodes the
pairing as *control flow* — one branch per bracket type, so adding a fourth
bracket means adding a branch. The second encodes it as *data*, so a fourth
bracket is one more dict entry and no new code. The `if c in pairs` test also
does double duty: membership in the dict is what identifies a closer, so the
separate `closes` list disappears.

`return not stack` replacing `if not stack: return True else: return False` is
the same move at smaller scale — the expression already *is* the boolean.

> [!tip] A behavioural difference worth noticing
> The first version returns `False` on any character that is not a bracket; the
> second **pushes** it, then fails at the end because the stack is non-empty.
> Both reject, by different routes, and the problem's constraints guarantee
> only brackets appear. But if the input were ever widened, the first one is
> the one that stays honest.

## Template

```python
pairs = {')': '(', ']': '[', '}': '{'}
stack = []
for c in s:
    if c in pairs:
        if not stack or stack.pop() != pairs[c]:
            return False
    else:
        stack.append(c)
return not stack
```

## Related

- [[Career/Prep/problems/Stack/150 · Evaluate Reverse Polish Notation|150 · Evaluate Reverse Polish Notation]] — the same LIFO reasoning applied to operands
- [[Career/Prep/topics/Data Structures/Stacks|Stacks]]
