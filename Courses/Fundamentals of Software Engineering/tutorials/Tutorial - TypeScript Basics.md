---
tags:
  - software-engineering
  - northeastern
  - cs4530
  - typescript
  - tutorial
  - language-reference
type: tutorial
course: "[[Fundamentals of Software Engineering]]"
status: notes
---
# Tutorial — TypeScript Basics

> [!info] Source
> <https://neu-se.github.io/CS4530-Fall-2026/tutorials/week1-typescript-basics> (last updated 2026-09-12)
> Scratchpad: [TypeScript Playground](https://www.typescriptlang.org/play)

**Assigned in**: [[Module 01 - Orientation and User Stories]] · [[Module 02 - From Requirements to Tests]]
**Needed for**: [[Individual Project 1]] (all five tasks)
**Prerequisite**: [[Tutorial - Development Environment Setup]]
**Style rules that apply**: [[CS4530 Code Style Guide]]

> [!abstract] This note is a map, not the content
> The language material is written up as permanent notes in **[[Code/TypeScript/TypeScript|TypeScript]]** (`Code/TypeScript/`),
> one note per topic, so it stays useful past this course. This page is the crosswalk: every
> section of the tutorial → the note that covers it, plus what's specific to CS 4530.
>
> Read the tutorial's framing here; read the mechanics in the linked notes.

## The One-Sentence Version

TypeScript is a **superset of JavaScript** that adds *optional* typing. All valid JavaScript is valid TypeScript. Everything TypeScript adds is checked at compile time and then **erased** — with one exception ([[Code/TypeScript/Enums|enums]] emit a real object).

## Course Requirements Attached to This Material

- [x] Typing is optional in TypeScript — **not optional in this course** → [[Code/TypeScript/Tooling|Tooling]]
- [x] Always use strict equality === as enforced by the linter → [[Code/TypeScript/Control Flow|Control Flow]]
- [x] File names in kebab-case, variables/functions in camelCase, classes in PascalCase → [[Code/TypeScript/Tooling|Tooling]]
- [x] Private property names must start with `_` → [[Code/TypeScript/Classes|Classes]] · [[Code/TypeScript/OOP Principles|OOP Principles]]
- [x] Prefer descriptive names over single letters → [[Code/TypeScript/Tooling|Tooling]]
- [x] You may **not** modify `tsconfig.json` in [[Individual Project 1]] → [[Code/TypeScript/Tooling|Tooling]]

## Topic Map

Tutorial section → permanent note. All of it is covered.

### Types in TypeScript → [[Code/TypeScript/Types|Types]]

| Tutorial subsection | Note | The thing to remember |
| --- | --- | --- |
| Boolean | [[Code/TypeScript/Types\|Types]] | `const c = true` infers the literal type `true`, not `boolean` |
| Number | [[Code/TypeScript/Types\|Types]] | one 64-bit float type; use `1_000_000` separators |
| BigInt | [[Code/TypeScript/Types\|Types]] | `1234n`; `number` loses precision past 2^53 − 1 |
| String | [[Code/TypeScript/Types\|Types]] | `charAt` `slice` `split` `concat` `indexOf` — all return new strings; `indexOf` returns `-1`, not `null` |
| Arrays | [[Code/TypeScript/Arrays\|Arrays]] | **never `let x = []`** — that's `any[]` and it widens silently |
| Tuples | [[Code/TypeScript/Tuples\|Tuples]] | must be explicitly typed; length is part of the type |
| Enums | [[Code/TypeScript/Enums\|Enums]] | strings→strings or strings→numbers; a literal union is usually better |
| Any | [[Code/TypeScript/Types\|Types]] | opts out of typechecking, and it's contagious |
| Unknown | [[Code/TypeScript/Types\|Types]] | the `any` you should actually use — narrow it with `typeof` / `instanceof` |
| Literal | [[Code/TypeScript/Types\|Types]] | `let count: 10 = 10`; earns its keep in unions |

### Variable declaration → [[Code/TypeScript/Variables|Variables]]

`var` (function-scoped, avoid) · `let` (block-scoped) · `const` (block-scoped, non-reassignable, **prefer this**).

`const` freezes the binding, not the contents.

### Objects → [[Code/TypeScript/Objects|Objects]]

Three ways to type one, worst to best: `any` → inline object type → [[Code/TypeScript/Interfaces|interface]]. The tutorial explicitly names `const myObj: any` as the thing to avoid.

### Control Flow Statements → [[Code/TypeScript/Control Flow|Control Flow]]

If-else · switch (**`break` is required** or you fall through) · ternary.

**Equality vs Strict Equality** — == coerces before comparing, so the string zero equals the number zero; === checks type as well as value, so it does not. Use === in all cases; the linter enforces it. Objects and arrays compare **by reference**.

### Loops → [[Code/TypeScript/Loops|Loops]]

for · while · do-while. Entry-level loops check the condition first; `do...while` is exit-level and always runs the body once.

> The course's actual guidance: **replace explicit loops with `.map()` / `.filter()` / `.reduce()` / `.forEach()` where possible.** → [[Code/TypeScript/Array Functions|Array Functions]]

### Array Functions → [[Code/TypeScript/Array Functions|Array Functions]]

| Method | Returns |
| --- | --- |
| `forEach` | **nothing** — side effects only |
| `map` | new array, same length |
| `filter` | new array, `≤` length, order preserved |
| `reduce` | one value — **always pass `initialValue`** |

### Functions → [[Code/TypeScript/Functions|Functions]]

Typing the function · invoking it · optional `?` and default parameters · rest `...` parameters · arrow functions · overloads.

- **Annotate parameters because you must** (they'd be implicitly `any`); **annotate the return because you should**.
- Arrow functions have **lexical `this`** — the `setTimeout` / `Counter` example is the whole reason they exist.
- Overload signatures are type-level only; the implementation signature isn't callable.

### Classes → [[Code/TypeScript/Classes|Classes]]

Fields · constructors · methods · `public`/`protected`/`private` · `static` · `readonly` · getters/setters · `extends` · `implements`.

**Abstract classes** — `abstract` keyword, cannot be instantiated, subclasses must define every abstract member. The tutorial's `Person`/`Employee` example shows the payoff: a concrete `display()` on the parent calling an abstract `name` supplied by the child.

### Type Aliases → [[Code/TypeScript/Type Aliases|Type Aliases]]

A name for **any** type, including unions. The caveat that matters: `type UserInputSanitizedString = string` documents but does not enforce — any `string` satisfies it.

### Interfaces → [[Code/TypeScript/Interfaces|Interfaces]]

Contracts. If the interface has it, the implementer must too. `const person: IPerson = new Person()` — type by the contract, not the implementation.

### Custom types → [[Code/TypeScript/Interfaces|Interfaces]] · [[Code/TypeScript/Type Aliases|Type Aliases]]

The tutorial's rule: **interface for complicated types (usually objects), `type` when you need a union.**

### Generics → [[Code/TypeScript/Generics|Generics]]

`<T>` on functions, classes, and interfaces. Unlike `any`, a generic **remembers** the type it was given. The tutorial flags the payoff: HTTP requests → [[Tutorial - API Requests]].

### Modules → [[Code/TypeScript/Modules|Modules]]

Every file is a module; nothing is visible across files without `export`.

- Two export forms: `export` on the declaration, or a separate `export { subtract }`.
- **Imported types need the `type` prefix**: `import { add, type Message } from './file1.ts'`.
- At most one `default` export per module, imported without braces. **In React, the single component per file is usually a default export.**

### OOP concepts → [[Code/TypeScript/OOP Principles|OOP Principles]]

| Principle | Mechanism | Tutorial example |
| --- | --- | --- |
| Inheritance | `extends` | `Shape` → `Circle`; privates and constructors don't cross; **no multiple inheritance** |
| Polymorphism | overriding + `super` | `CheckingAccount` → Business/Personal, different minimum deposits |
| Abstraction | `abstract class`, `interface` | `Fee` applied only to accounts that charge one |
| Encapsulation | `private` + accessors | `private _balance` with `Withdraw()` and `get Balance()` |

The design lesson buried in the abstraction section: **a capability only some subtypes have belongs in an interface, not the base class.**

### General Guidelines → [[Code/TypeScript/Tooling|Tooling]]

kebab-case files · camelCase variables/functions · PascalCase classes · descriptive names · typing mandatory here · strict equality · linter · prettifier.

### tsconfig.json → [[Code/TypeScript/Tooling|Tooling]]

`noImplicitAny` and `strict` control *which errors get reported*. `noEmit` controls *what the compiler does* — typecheck only, no `.js` output, because Vite does the transpiling.

> [!important] Don't touch it
> The tutorial says you shouldn't need to. [[Individual Project 1]] says you **may not**. If the compiler complains, fix the code.

## Notes

### What's actually new relative to JavaScript

If you know [[JavaScript]], most of this tutorial is review. The genuinely new material is:

1. **Annotations and inference** — the `: type` syntax, and where inference does/doesn't reach ([[Code/TypeScript/Types|Types]], [[Code/TypeScript/Functions|Functions]])
2. **`unknown`** — the safe `any`, and the narrowing it forces ([[Code/TypeScript/Types|Types]])
3. **[[Code/TypeScript/Tuples|Tuples]]** — no JavaScript equivalent
4. **[[Code/TypeScript/Interfaces|Interfaces]] and [[Code/TypeScript/Type Aliases|Type Aliases]]** — no JavaScript equivalent
5. **[[Code/TypeScript/Generics|Generics]]** — no JavaScript equivalent
6. **Access modifiers on [[Code/TypeScript/Classes|class]] members** — JavaScript has `#private`, not `public`/`protected`
7. **[[Code/TypeScript/Enums|Enums]]** — and they're the one feature with a runtime cost
8. **Overload signatures** ([[Code/TypeScript/Functions|Functions]])
9. **[[Code/TypeScript/Tooling|tsconfig]] and the separate typecheck step**

### The thing that trips people up

**Nothing that runs your code typechecks it.** Vite strips the types and transpiles; it does not care whether they were correct. A type error will not stop the dev server. `tsc --noEmit` is a separate command and a separate CI gate — "it runs" is not evidence that it compiles clean. → [[Code/TypeScript/Tooling|Tooling]]

### Where this shows up in the course

| Coming up | Leans on |
| --- | --- |
| [[Individual Project 1]] | all of it — [[Code/TypeScript/Classes\|Classes]], [[Code/TypeScript/Interfaces\|Interfaces]], [[Code/TypeScript/Array Functions\|Array Functions]], [[Code/TypeScript/Modules\|Modules]] |
| [[Tutorial - Unit Testing with Vitest]] | [[Code/TypeScript/Functions\|Functions]], [[Code/TypeScript/Modules\|Modules]] (testing public APIs) |
| [[Tutorial - API Requests]] | [[Code/TypeScript/Generics\|Generics]] — typed responses |
| [[Module 04 - Design Patterns for Web Applications]] | [[Code/TypeScript/OOP Principles\|OOP Principles]], [[Code/TypeScript/Interfaces\|Interfaces]] |

## Questions / Gaps

- The tutorial's `Fee` interface declares `chargeFee(amount: number )` with **no return type** — implicitly `any`. Would that pass the course linter? Worth checking against [[CS4530 Code Style Guide]] before copying the pattern.
- `I`-prefixed interface names (`IPerson`, `IStudent`) are used throughout the tutorial but aren't in the stated naming conventions. Confirm whether the [[Individual Project 1]] codebase follows it.
- The tutorial never covers `async` / `await` or `Promise<T>`, but [[Tutorial - API Requests]] needs both. Gap to fill from [[Async|the JavaScript note]].
- No coverage of `never`, discriminated unions, or utility types (`Partial`, `Omit`) — all appear in real codebases. Noted in [[Code/TypeScript/Type Aliases|Type Aliases]] and [[Code/TypeScript/Generics|Generics]] anyway.

## Related

- **[[Code/TypeScript/TypeScript|TypeScript]]** — the permanent-note hub these all hang off
- [[Tutorial - Development Environment Setup]]
- [[Tutorial - Unit Testing with Vitest]]
- [[Tutorial - API Requests]]
- [[CS4530 Code Style Guide]]
- [[Individual Project 1]]
- [[JavaScript]] — the base language
- [[CS4530 Textbooks and Resources]] — "Programming TypeScript" (Cherny), "Modern JavaScript for the Impatient" (Horstmann)
