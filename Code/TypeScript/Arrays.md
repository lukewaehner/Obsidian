---
tags:
  - typescript
  - javascript
type: note
related:
  - "[[TypeScript]]"
  - "[[Array Functions]]"
date: 2026-09-14
---
# Arrays

Typed collections. Special objects that support concatenation, pushing, searching, and slicing — iterable objects whose keys are numbers.

## Declaring and Inferring

```ts
let a = [1, 2, 3]           // number[]
var b = ['a', 'b']          // string[]
let c: string[] = ['a']     // string[]
let d = [1, 'a']            // (string | number)[]
const e = [2, 'b']          // (string | number)[]

let f = ['red']
f.push('blue')
```

A mixed-type literal infers a **union element type**, not `any`. `[1, 'a']` is `(string | number)[]` — you can push either, and reading an element gives you a union you have to narrow before use.

## Always Type an Empty Array

This is the one real trap in the section:

```ts
// Avoid declaring arrays without types
let g = []                  // any[] - not recommended
g.push(1)                   // number[]
g.push('red')               // (string | number)[]

// Best practice: explicitly type empty arrays
let h: number[] = []        // number[] - recommended approach
h.push(1)                   // number[]
```

An empty literal has nothing to infer from. TypeScript starts it as `any[]` and *widens* the type as you push — so it accepts anything and you get no error where you wanted one. `h.push('red')` fails; `g.push('red')` does not.

## Two Equivalent Spellings

```ts
let a: number[] = [1, 2, 3];
let b: Array<number> = [1, 2, 3];   // identical
```

`T[]` is the conventional form. `Array<T>` is the same type written with [[Generics|generic]] syntax — useful when the element type is itself complex.

## readonly

```ts
const scores: readonly number[] = [1, 2, 3];
scores.push(4);     // Error: Property 'push' does not exist on type 'readonly number[]'
```

`readonly number[]` removes the mutating methods from the type. This is the contents-level immutability that `const` alone doesn't give you.

## Working With Arrays

Don't loop over them by index. Use the array functions:

```ts
const numbers = [1, 2, 3, 4, 5];
const doubled = numbers.map(n => n * 2);
```

See [[Array Functions]] for `forEach` / `map` / `filter` / `reduce`, and [[Loops]] for why the explicit `for` loop is the fallback rather than the default.

## Tips

- Never write `let x = []`. Write `let x: T[] = []`. This is the single most common source of accidental `any` in a codebase.
- Prefer `const` for arrays you mutate — the binding shouldn't change even when the contents do.
- Reading `arr[10]` on a 3-element array returns `undefined` at runtime but is typed `T`, not `T | undefined`, unless `noUncheckedIndexedAccess` is on. Don't trust the index.
- Fixed-length, heterogeneous data isn't an array — it's a [[Tuples|tuple]].

## See Also

- [[Array Functions]] — `forEach`, `map`, `filter`, `reduce`
- [[Tuples]] — arrays with a fixed length and per-index types
- [[Loops]] — the explicit alternative and when it's justified
- [[Types]] · [[Generics]]
- [[Tutorial - TypeScript Basics]]
