---
type: topic
group: Systems
tier: extra
confidence:
sections_total: 6
sections_done: 1
coverage: 0.17
status: learning
updated: 2026-09-13
---

# Compilers

← [[Career/Prep/topics/Systems/Systems|Systems]]

> [!abstract]- Coverage — 1/6
> - [ ] [[#Idea]]
> - [ ] [[#How it works]]
> - [x] [[#Implementation]]
> - [ ] [[#Complexity]]
> - [ ] [[#When to use it]]
> - [ ] [[#Gotchas]]

## Idea

A compiler translates source code into a lower-level form (machine code,
bytecode, or another language) through a pipeline of distinct passes rather
than a single transformation.

## How it works

The classic pipeline: lexing (characters into tokens), parsing (tokens into
an AST), semantic analysis (type checking, scope resolution), optimization,
and code generation. [[Code/Computer Systems/Assembly/Assembly & Compilation Pipeline|Assembly & Compilation Pipeline]]
covers the later stages concretely.

## Implementation

The preprocessor is the first compiler pass and the one you can actually read: `#include` textual expansion, macros, conditional compilation, and header guards — [[Code/Computer Systems/C/The Preprocessor/The Preprocessor|The Preprocessor]], [[Code/Computer Systems/C/The Preprocessor/Include|Include]], [[Code/Computer Systems/C/The Preprocessor/Macros|Macros]], [[Code/Computer Systems/C/The Preprocessor/Header Files|Header Files]]. Compiler output is assembly, which the assembler and linker take from there — [[Code/Computer Systems/Assembly/Assembly & Compilation Pipeline|Assembly & Compilation Pipeline]].

## Complexity

## When to use it

## Gotchas

Optimizations can change observable behavior in the presence of undefined
behavior (classic C/C++ pitfall) — "the compiler is allowed to assume UB
never happens" surprises people who expect optimization to be strictly
behavior-preserving.

## Resources

- [How a Compiler Works in ~1 minute (video)](https://www.youtube.com/watch?v=IhC7sdYe-Jg)
- [Harvard CS50 - Compilers (video)](https://www.youtube.com/watch?v=CSZLNYF4Klo)
- [C++ (video)](https://www.youtube.com/watch?v=twodd1KFfGk)
- [Understanding Compiler Optimization (C++) (video)](https://www.youtube.com/watch?v=FnGCDLhaxKU)

## Problems

_None yet._
