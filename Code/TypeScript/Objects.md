---
tags:
  - typescript
  - javascript
type: note
related:
  - "[[TypeScript]]"
  - "[[Interfaces]]"
date: 2026-09-14
---
# Objects

Key-value pairs, like dictionaries. ([[Arrays|Arrays]] are iterable objects whose keys are numbers.)

## Three Ways to Type One — Worst to Best

### 1. `any` — don't

```ts
// Avoid using 'any' type for objects
const myObj: any = {
    key1: 'value1',
    key2: 'value2'
};

console.log(myObj.key1); // prints 'value1'
```

`myObj.key3` compiles. `myObj.kye1` compiles. Every typo is a runtime `undefined`. This is the pattern the tutorial explicitly names as the thing to avoid.

### 2. Inline object type — fine for one-offs

```ts
// Better: explicitly type your objects
const myTypedObj: { key1: string; key2: string } = {
    key1: 'value1',
    key2: 'value2'
};

console.log(myTypedObj.key1); // prints 'value1'
```

Note the separator: **semicolons inside a type literal**, commas inside a value literal. Both are accepted in the type position, but semicolons are conventional.

### 3. Interface — for anything reused

```ts
// For reusable objects, use interfaces
interface Person {
    name: string;
    age: number;
}

const person: Person = {
    name: 'John',
    age: 30
};
```

Now `Person` is a name you can use in parameter types, return types, and `implements` clauses. See [[Interfaces]].

## Inference

An object literal with no annotation infers its own shape:

```ts
const p = { name: 'John', age: 30 };   // { name: string; age: number }
p.name = 'Jane';                        // fine
p.email = 'x@y.com';                    // Error: Property 'email' does not exist
```

Inference is usually enough for a local. The annotation earns its keep when the object crosses a boundary — a function parameter, a return value, an exported constant.

## Optional and readonly Properties

```ts
interface Config {
  host: string;
  port?: number;              // optional — may be absent
  readonly apiKey: string;    // cannot be reassigned after construction
}

const c: Config = { host: 'localhost', apiKey: 'abc' };
c.apiKey = 'def';   // Error: Cannot assign to 'apiKey', it is a read-only property
```

An optional property is typed `number | undefined`, so you have to narrow it before use:

```ts
const port = c.port ?? 8080;
```

## Excess Property Checking

TypeScript flags extra properties on a **fresh object literal** assigned to a typed target:

```ts
const person: Person = { name: 'John', age: 30, email: 'x@y.com' };
// Error: Object literal may only specify known properties
```

This catches typos at the assignment site. It does *not* fire when the object comes in via a variable — that's structural typing doing its job, and it's intentional.

## Accessing Properties

```ts
person.name           // dot — preferred, typo-checked
person['name']        // bracket — for dynamic or non-identifier keys

const user = { address: { city: 'Boston' } };
user.address?.city    // optional chaining — undefined instead of a throw
```

## Index Signatures

When the keys aren't known ahead of time but the value type is:

```ts
interface ScoreBoard {
  [playerName: string]: number;
}

const scores: ScoreBoard = { alice: 10, bob: 7 };
scores.carol = 3;     // fine — any string key, number value
```

Use this sparingly — it trades away key checking, which is most of the value of typing the object in the first place. A `Map` is often the better structure.

## Tips
- Never `const x: any = { ... }`. If the shape is known, write it; if it's reused, make it an [[Interfaces|interface]].
- Objects are compared by reference. `{ a: 1 } === { a: 1 }` is `false` — see [[Control Flow]].
- Spread copies one level deep: `{ ...defaults, ...overrides }` shares nested objects with the originals.
- For a type that must be constructed and validated at a boundary (an API response), type it *and* validate it — Zod in the CS 4530 stack does both.

## See Also
- [[Interfaces]] — the reusable form
- [[Type Aliases]] — `type Point = { x: number; y: number }`
- [[Classes]] — objects with behavior and access control
- [[Arrays]] · [[Types]]
- [[Tutorial - TypeScript Basics]]
