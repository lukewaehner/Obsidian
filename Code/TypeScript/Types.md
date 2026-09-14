---
tags:
  - typescript
  - javascript
type: note
related:
  - "[[TypeScript]]"
  - "[[Variables]]"
date: 2026-09-14
---
# Types

TypeScript's type system. Every JavaScript primitive, plus the escape hatches (`any`, `unknown`) and literal types that JavaScript has no equivalent for.

TypeScript is a **superset** of JavaScript — all valid JavaScript is valid TypeScript. The thing it adds is *optional* typing. Optional to the language; **not optional in CS 4530**.

## The Annotation Syntax

A type annotation goes after the name, before the `=`:

```ts
let name: type = value;
```

Without an annotation, TypeScript **infers** the type from the initializer. Inference is real typing — `let a = true` is a `boolean`, not `any`.

## Boolean

Two values: `true` and `false`.

```ts
let a = true                // boolean
var b = false               // boolean
const c = true              // true
let d: boolean = true       // boolean
let e: true = true          // true
```

Note the difference between the three lines producing `boolean` and the two producing `true`. `const c = true` infers the **literal** type `true`, because a `const` can never be reassigned so the type can be narrowed to the exact value. `let e: true` is that same narrowing, written by hand.

**Operations**: compare with `==`, `===`, `||`, `&&`, `?`; negate with `!`.

## Number

All numbers — integers, floats, positives, negatives, `Infinity`, `NaN`. One type, 64-bit float, same as JavaScript.

```ts
var b = Infinity * 0.10     // number
const c = 5678              // 5678
let d = a < b               // boolean
let e: number = 100         // number
let f: 26.218 = 26.218      // number
```

**Operations**: `+`, `-`, `%`, `<`, and the rest of arithmetic.

Use **numeric separators** for long literals — they're ignored by the compiler and purely for readers:

```ts
const oneMillion = 1_000_000;   // same value as 1000000
```

## BigInt

Arbitrary-precision integers. Written with an `n` suffix.

```ts
let a = 1234n               // bigint
const b = 5678n             // 5678n
var c = a + b               // bigint
let d = a < 1235            // boolean
let e = 88.5n               // Error TS1353: A bigint literal must be an integer.
let f: bigint = 100n        // bigint
let g: 100n = 100n
```

**Why it exists**: `number` loses precision above 2^53 − 1 (`Number.MAX_SAFE_INTEGER`, 9007199254740991). `bigint` represents values beyond that exactly.

**Operations**: `+`, `-`, `*`, `/`, `<`.

> [!warning] `bigint` and `number` don't mix in arithmetic
> Comparison across the two works (`a < 1235` above is fine), but `1n + 1` is a type error. Convert explicitly.

## String

All strings, and the operations on them.

```ts
let a: string = 'hello'           // string
let b: string = 'world'           // string
let c: string = a + ' ' + b       // string
```

### Operations the tutorial calls out

| Method | Signature | Returns |
| --- | --- | --- |
| `charAt` | `string.charAt(index)` | Character at `index`. Indexed left to right from `0`; last index is `length - 1` |
| `slice` | `string.slice(beginSlice[, endSlice])` | New string — a section of the original |
| `split` | `string.split([separator][, limit])` | Array of substrings, cut on `separator` |
| `concat` | `string.concat(string2, string3[, ...])` | New single string |
| `indexOf` | `string.indexOf(searchValue[, fromIndex])` | Index of first occurrence, or `-1` if absent |

Every one of these **returns a new string**. Strings are immutable; nothing here mutates in place.

`indexOf` returning `-1` rather than `null` is the classic off-by-one trap — test `=== -1`, never truthiness, because index `0` is falsy:

```ts
if (haystack.indexOf(needle) !== -1) { /* found */ }   // correct
if (haystack.indexOf(needle)) { /* WRONG */ }          // misses a match at index 0
```

## Any

The supertype of all types. A dynamic type — using it **opts that variable out of type checking entirely**.

```ts
let a: any = 666            // any
let b: any = ['danger']     // any
let c = a + b               // any
```

Everything must have a type at compile time, and `any` is what you get when neither you nor the typechecker can work out what something is. It is a **last-resort type**. Avoid it.

> [!danger] `any` is contagious
> `c` above is `any` because `a` and `b` are. One `any` at a boundary silently untypes everything downstream of it, which is exactly the failure mode `noImplicitAny` in [[Tooling|tsconfig]] exists to catch.

## Unknown

The safe alternative to `any`. Also holds any value — but TypeScript won't let you *use* it until you narrow it.

```ts
let a: unknown = 30         // unknown
let b = a === 123           // boolean
```

You can compare `unknown` values (`==`, `===`, `&&`, `?`) and refine them with `typeof` and `instanceof`.

```ts
function len(x: unknown): number {
  if (typeof x === 'string') {
    return x.length;        // narrowed to string here, so .length is legal
  }
  return 0;
}
```

**Rule**: when you genuinely don't know a type ahead of time — parsing JSON, catching an error, reading an API response — reach for `unknown`, not `any`. It forces the check that `any` lets you skip.

## Literal

A type that represents **one specific value**, not a general category.

```ts
let e: true = true;            // literal type, constrained to the value true
let count: 10 = 10;            // can only ever be the number 10
let status: "pass" = "pass";   // can only ever be the string "pass"
```

These behave like constants. Reassigning throws a compile error.

Literals earn their keep in **unions**, where they become a closed set of legal values:

```ts
type Result = 'pass' | 'fail' | 'incomplete';

let outcome: Result = 'pass';
outcome = 'passed';    // Error — not one of the three
```

That is a hand-rolled enum with no runtime cost, and it's usually preferable to [[Enums|a real enum]]. See [[Type Aliases]].

## Tips

- Annotate function parameters and return types by hand; let TypeScript infer local variable types. That's the split the tutorial recommends and it reads best.
- `const` on a primitive infers the literal type; `let` widens to the general type. This matters when passing to something expecting a literal union.
- If you're about to write `any`, write `unknown` and add the narrowing check. It is nearly always three lines of work and it's the whole point of the language.
- Reach for `bigint` only when you actually exceed 2^53 − 1. It doesn't interoperate with `number` and it's slower.

## See Also

- [[Variables]] — `var` / `let` / `const` and scope
- [[Arrays]] · [[Tuples]] · [[Enums]] — the compound types
- [[Type Aliases]] — naming a type, including literal unions
- [[Tooling]] — `noImplicitAny`, `strict`, and the linter that enforces this
- [[Tutorial - TypeScript Basics]] — the CS 4530 source for these notes
