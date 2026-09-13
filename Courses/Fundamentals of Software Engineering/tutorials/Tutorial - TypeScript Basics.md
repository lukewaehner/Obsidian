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
status: raw
---
# Tutorial — TypeScript Basics

> [!info] Source
> <https://neu-se.github.io/CS4530-Fall-2026/tutorials/week1-typescript-basics>
> Scratchpad: [TypeScript Playground](https://www.typescriptlang.org/play)

**Assigned in**: [[Module 01 - Orientation and User Stories]] · [[Module 02 - From Requirements to Tests]]
**Needed for**: [[Individual Project 1]] (all five tasks)
**Prerequisite**: [[Tutorial - Development Environment Setup]]
**Style rules that apply**: [[CS4530 Code Style Guide]]

## Course Requirements Attached to This Material

- [ ] Typing is optional in TypeScript — **not optional in this course**
- [ ] Always use strict equality (`===`); enforced by the linter
- [ ] File names in kebab-case, variables/functions in camelCase, classes in PascalCase
- [ ] Private property names must start with `_`
- [ ] Prefer descriptive names over single letters
- [ ] You may **not** modify `tsconfig.json` in [[Individual Project 1]]

## Topics to Cover

### Types
- [ ] Boolean
- [ ] Number
- [ ] BigInt
- [ ] String — `charAt` / `slice` / `split` / `concat` / `indexOf`
- [ ] Arrays
- [ ] Tuples
- [ ] Enums
- [ ] `any`
- [ ] `unknown` — and why to reach for it over `any`
- [ ] Literal types

### Declarations & Data
- [ ] `var` vs `let` vs `const`
- [ ] Objects

### Control Flow
- [ ] if / else if / else
- [ ] switch
- [ ] Ternary
- [ ] `==` vs `===`
- [ ] Loops — for, while, do-while

### Array Functions
- [ ] `forEach`
- [ ] `map`
- [ ] `filter`
- [ ] `reduce`

### Functions
- [ ] Typing the function
- [ ] Invoking the function
- [ ] Optional and default parameters
- [ ] Rest parameters
- [ ] Arrow functions — and the `this` binding difference
- [ ] Function overloads

### Types & Structures
- [ ] Classes — fields, constructors, methods, access modifiers, static, readonly, getters/setters
- [ ] Abstract classes
- [ ] Type aliases
- [ ] Interfaces
- [ ] Custom types — interface vs `type`
- [ ] Generics
- [ ] Modules — `export` / `import`, default exports

### OOP
- [ ] Inheritance
- [ ] Polymorphism
- [ ] Abstraction
- [ ] Encapsulation

### Config
- [ ] `tsconfig.json` — `noImplicitAny`, `strict`, `noEmit` ([TSConfig Reference](https://www.typescriptlang.org/tsconfig/))

## Notes

## Questions / Gaps

## Related

- [[Tutorial - Development Environment Setup]]
- [[Tutorial - Unit Testing with Vitest]]
- [[CS4530 Code Style Guide]]
- [[Individual Project 1]]
- [[CS4530 Textbooks and Resources]] — "Programming TypeScript" (Cherny), "Modern JavaScript for the Impatient" (Horstmann)
