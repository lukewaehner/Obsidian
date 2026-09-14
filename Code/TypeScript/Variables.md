---
tags:
  - typescript
  - javascript
type: note
related:
  - "[[TypeScript]]"
  - "[[Types]]"
date: 2026-09-14
---
# Variables

Three declaration keywords, two scoping rules, one recommendation.

## Syntax

```ts
var   <name>: <type> = <value>;
let   <name>: <type> = <value>;
const <name>: <type> = <value>;
```

```ts
let num: number = 1;
const PI: number = 3.14;
let x: string = "This is a string";
const t: boolean = true;
const f: boolean = false;
let uninitialized: any;
```

That last line is the one to notice: a declaration with no annotation *and* no initializer has nothing to infer from, so it becomes `any`. Under `noImplicitAny` this is an error. Annotate it or initialize it.

## var — function-scoped

A `var` is accessible anywhere in its containing function, module, namespace, or global scope, **regardless of the block it was declared in**. Sometimes called var-scoping or function-scoping. Function parameters are also function-scoped.

```ts
function f() {
  if (true) {
    var leaked = 1;
  }
  console.log(leaked);   // 1 — the block did not contain it
}
```

**Avoid `var` in modern TypeScript.** It exists for backwards compatibility.

## let — block-scoped

Lexical scoping: a `let` is not visible outside its nearest containing block.

```ts
function f() {
  if (true) {
    let contained = 1;
  }
  console.log(contained);   // Error: Cannot find name 'contained'
}
```

## const — block-scoped and non-reassignable

Same scoping rules as `let`, but the binding cannot be reassigned once bound.

```ts
const PI: number = 3.14;
PI = 3.15;   // Error: Cannot assign to 'PI' because it is a constant.
```

> [!note] `const` freezes the binding, not the value
> ```ts
> const nums = [1, 2, 3];
> nums.push(4);       // fine — the array is mutated, the binding is unchanged
> nums = [5];         // Error — this is reassignment
> ```
> If you need genuine immutability of contents, that's `readonly` / `Object.freeze`, not `const`.

## Which to Use

**Prefer `const` by default. Use `let` only when you need to reassign. Never use `var`.**

The reason is not style. A `const` tells a reader "this binding never changes" — that's one fewer thing to track when reading the function. A `let` is a signal to go looking for where it gets reassigned. Using `let` everywhere destroys that signal.

## Tips

- `const` also narrows the inferred type to a literal — see [[Types]]. `const c = true` is type `true`; `let c = true` is type `boolean`.
- A `const` declared inside a loop body is fine and idiomatic; it's a fresh binding each iteration.
- In CS 4530 the linter will flag `var` and flag a `let` that's never reassigned. Write `const` first and downgrade only when the compiler makes you.

## See Also

- [[Types]] — what goes in the annotation slot
- [[Loops]] — where `let` vs `var` scoping actually bites
- [[Classes]] — `readonly` fields, the class-level analogue of `const`
- [[Tutorial - TypeScript Basics]]
