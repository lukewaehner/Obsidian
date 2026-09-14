---
tags:
  - typescript
  - javascript
type: note
related:
  - "[[TypeScript]]"
  - "[[Loops]]"
date: 2026-09-14
---
# Control Flow

If-else, switch, the ternary operator, and the equality rule the CS 4530 linter enforces.

## If / Else If / Else

```ts
if (condition) {
    // executed when condition is true
}

if (condition) {
    // executed when condition is true
} else {
    // executed when condition is false
}

if (condition) {
    // executed when condition is true
} else if (condition2) {     // checked only if condition is false
    // executed when condition2 is true
} else {
    // executed if every condition in the ladder is false
}
```

The `else if` chain short-circuits: `condition2` is only evaluated when `condition` was false.

```ts
const str: string = "ABCD";

if (str === "ABCD") {
    console.log("it was true");
} else {
    console.log("it was false");
}
```

## Switch

```ts
switch (variable) {
    case <case1>:
        // executed when value of variable matches <case1>
        break; // Break is required to prevent all subsequent cases from executing
    case <case2>:
        // executed when value of variable matches <case2>
        break;
    default:
        // executed if variable does not match any prior cases
}
```

```ts
switch (str) {
    case "ABCD":
        console.log('It was ABCD');
        break;
    case "WXYZ":
        console.log('It was WXYZ');
        break;
    default:
        console.log('It was something completely different')
}
```

> [!warning] `break` is not optional
> Omit it and execution **falls through** into every subsequent case body until it hits a `break` or the end of the switch. This is the single most common switch bug. A deliberate fall-through deserves a comment saying so.

`switch` matches with **strict equality** (===), so it has none of the coercion problems below.

### Exhaustiveness

Switching over a [[Enums|enum]] or a literal union lets the compiler prove you handled every case:

```ts
type Status = 'pending' | 'active' | 'closed';

function label(s: Status): string {
  switch (s) {
    case 'pending': return 'Pending';
    case 'active':  return 'Active';
    case 'closed':  return 'Closed';
  }
  // no default needed — TypeScript knows this is unreachable
}
```

Add a fourth member to `Status` and this function stops compiling. That's the feature.

## Ternary Operator

Shorthand for if-else that **returns a value**.

```ts
let x = (condition) ? /* when true */ : /* when false */;
```

```ts
let y: string = (str.includes("A")) ? "The string contains A" : "The string does not contain A";
// y now contains "The string contains A"
```

Use it for a single expression you're assigning. Don't nest ternaries — that's an `if` ladder wearing a disguise, and it reads terribly.

## Equality vs Strict Equality

Two equality operators:

- == — compares only the **value**. Performs implicit type coercion, which can produce surprising results.
- === — compares the **type and value**.

```ts
// Evaluates to true despite comparing string to number due to type coercion.
if (0 == '0') {
  console.log("String '0' is coerced to number 0");
}

if (0 == false) {
    console.log("false is coerced to 0");
}

if (0 === '0') {
  console.log("Will not print because types are different");
} // Evaluated to false because types are different.
```

For objects and arrays, === compares **by reference** — two structurally identical objects are not equal:

```ts
{ a: 1 } === { a: 1 }     // false — different references
[1, 2] === [1, 2]         // false
```

> [!important] Course requirement
> **Use strict equality (===) in all cases.** The CS 4530 linter enforces this. See [[CS4530 Code Style Guide]].

TypeScript's typechecker also helps here: `0 === '0'` is a *compile* error (`This comparison appears to be unintentional`) when both operands are typed, because the types don't overlap. Loose equality bypasses that protection.

## Narrowing

Control flow is also how TypeScript refines types. Inside a guarded branch, the compiler knows more than it did outside:

```ts
function describe(x: string | number): string {
  if (typeof x === 'string') {
    return x.toUpperCase();   // x is string here
  }
  return x.toFixed(2);        // x is number here — the only remaining option
}
```

This is what makes `unknown` usable in place of `any` (see [[Types]]). The guards are `typeof`, `instanceof`, `in`, truthiness, and equality against a literal.

## Tips
- Use === always. The only defensible == is `x == null`, which catches `null` and `undefined` together — and `x === null || x === undefined` says it more plainly.
- Prefer `switch` over a long `if/else if` ladder on a single value: you get exhaustiveness checking, which the ladder can't give you.
- Guard clauses beat nesting. Return early on the invalid case rather than wrapping the happy path in three `if`s.
- Use `??` (nullish coalescing) rather than `||` for defaults — `||` also replaces `0` and `''`.

## See Also
- [[Loops]] — for, while, do-while
- [[Types]] — narrowing `unknown`, literal unions
- [[Enums]] — the exhaustive-switch use case
- [[CS4530 Code Style Guide]] — the linted rules
- [[Tutorial - TypeScript Basics]]
