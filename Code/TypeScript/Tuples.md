---
tags:
  - typescript
  - javascript
type: note
related:
  - "[[TypeScript]]"
  - "[[Arrays]]"
date: 2026-09-14
---
# Tuples

Subtypes of [[Arrays|array]]. A way to type arrays that have **fixed lengths**, where the value at each index has a specific, known type.

## Declaring

Unlike most types, **tuples must be explicitly typed**. There is no inference path to a tuple — a matching literal infers as an array.

```ts
let a: [number] = [1]

// A tuple of [first name, last name, birth year]
let b: [string, string, number] = ['malcolm', 'gladwell', 1963]
```

Without the annotation, `['malcolm', 'gladwell', 1963]` infers as `(string | number)[]` — length unknown, every element a union. The annotation is what buys you the length and the per-position types.

## What the Type Gives You

```ts
let b: [string, string, number] = ['malcolm', 'gladwell', 1963]

b[0]                  // string
b[2]                  // number
b[3]                  // Error — length is 3
b = ['a', 'b']        // Error — wrong length
b = [1963, 'a', 'b']  // Error — wrong type at index 0
```

The length is part of the type. That's the whole point: a tuple safely encodes a **heterogeneous list** *and* captures how long it is.

## Optional Elements

Like in object types, `?` means optional:

```ts
let point: [number, number, number?] = [1, 2];      // z is optional
point = [1, 2, 3];                                  // also fine
```

## Rest Elements

Use a rest element to type a tuple with a **minimum** length:

```ts
// at least one string, then any number of numbers
let row: [string, ...number[]] = ['header'];
row = ['header', 1, 2, 3];
```

## Where Tuples Actually Show Up

Anywhere a function returns two related-but-different things, or a config pair travels together:

```ts
function divide(a: number, b: number): [number, number] {
  return [Math.floor(a / b), a % b];   // [quotient, remainder]
}

const [quotient, remainder] = divide(7, 2);
```

This is exactly the shape React hooks use — `useState` returns `[value, setValue]`, a tuple.

> [!tip] Name the positions when there are more than two
> `[string, string, number]` needs a comment to be readable. Past two elements, a typed object or [[Interfaces|interface]] with named keys is almost always clearer than a tuple.

## Tips

- If you find yourself writing `tuple[2]` in application code, the positions have stopped being obvious. Destructure with names, or switch to an object.
- A tuple is assignable *to* an array type but not the reverse — `number[]` cannot be assigned to `[number, number]`, because the compiler doesn't know the length.
- `readonly [string, number]` gives you a tuple that can't be mutated in place.

## See Also

- [[Arrays]] — the supertype
- [[Interfaces]] · [[Type Aliases]] — the named-field alternative
- [[Functions]] — returning multiple values
- [[Tutorial - TypeScript Basics]]
