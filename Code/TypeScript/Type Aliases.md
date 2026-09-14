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
# Type Aliases

**A name for any type.** Nothing more than that — but the "any type" part is the whole feature.

Writing object types and union types directly in annotations is convenient, but it's common to want the same type more than once and refer to it by a single name.

## Naming an Object Type

```ts
type Point = {
  x: number;
  y: number;
};

function printCoord(pt: Point) {
  console.log("The coordinate's x value is " + pt.x);
  console.log("The coordinate's y value is " + pt.y);
}

printCoord({ x: 100, y: 100 });
```

## Naming a Union

This is the case an [[Interfaces|interface]] cannot do at all:

```ts
type ID = number | string;
```

```ts
type StringOrNumber = string | number;

let x: StringOrNumber = 1; // initialized with a `number`
x = 'some string'; // can be reassigned to be a `string`
```

You can alias **any** type — a union, a primitive, a [[Tuples|tuple]], a function type, a [[Generics|generic]] instantiation:

```ts
type Callback = (err: Error | null, data: string) => void;
type Pair = [string, number];
type Status = 'pending' | 'active' | 'closed';
type Scores = Record<string, number>;
```

The literal union (`Status`) is the workhorse. It's a closed set of legal values with zero runtime cost — usually a better choice than [[Enums|an enum]].

## Aliases Are Only Aliases

The critical caveat from the tutorial:

> Note that aliases are only aliases — you cannot use type aliases to create different/distinct "versions" of the same type. When you use the alias, it's exactly as if you had written the aliased type.

```ts
type UserInputSanitizedString = string;

function sanitizeInput(str: string): UserInputSanitizedString {
  return sanitize(str);
}

// Create a sanitized input
let userInput = sanitizeInput(getInput());

// Can still be re-assigned with a string though
userInput = "new input";
```

This looks like it should be illegal. It isn't, because `UserInputSanitizedString` **is** `string` — the alias carries documentation, not enforcement. Any `string` satisfies it, sanitized or not.

> [!tip] Branded types, if you actually need the distinction
> The standard workaround is to intersect a phantom property that no real value has:
> ```ts
> type Sanitized = string & { readonly __brand: 'sanitized' };
>
> function sanitize(s: string): Sanitized {
>   return s.replace(/</g, '&lt;') as Sanitized;   // the cast is the trust boundary
> }
>
> let input: Sanitized = sanitize(getInput());
> input = "new input";   // Error — plain string is not Sanitized
> ```
> Now only `sanitize` can mint the type. Worth it for security-relevant distinctions; overkill for most things.

## Type vs Interface

Both name an object shape and both are erased at compile time. The differences that matter:

| | `type` | `interface` |
| --- | --- | --- |
| Object shapes | yes | yes |
| Unions, primitives, tuples, function types | **yes** | no |
| `implements` on a class | yes (if object-shaped) | yes |
| Extension | intersection `A & B` | `extends` |
| Declaration merging | **no** | yes — reopens and adds |
| Error messages | inlines the definition | shows the name |

The tutorial's guidance:

- **For complicated types (usually objects), use an [[Interfaces|interface]].**
- **Use `type` when you need a union of different types.**

That's a good default. `interface` for the shape of a thing, `type` for a set of alternatives.

## Composing Aliases

```ts
type Point = { x: number; y: number };
type Labeled = { label: string };

type LabeledPoint = Point & Labeled;   // intersection — has x, y, and label

const p: LabeledPoint = { x: 1, y: 2, label: 'origin' };
```

Intersection (`&`) is the `type` analogue of `interface extends`. Aliases can also be generic:

```ts
type Result<T> = { ok: true; value: T } | { ok: false; error: string };
```

That's a **discriminated union** — the `ok` field tells the compiler which branch you're in, so a check on `ok` narrows `value` into existence. It's the idiomatic TypeScript way to model "succeeded or failed" without throwing.

## Tips
- Alias any type you write more than twice. The name is the documentation.
- `PascalCase` for type names, matching classes. See [[CS4530 Code Style Guide]].
- An alias of a primitive documents but does not enforce. Don't mistake `type UserId = string` for type safety.
- Prefer a literal union over an enum unless you need to enumerate the members at runtime.

## See Also
- [[Interfaces]] — the other way to name a shape
- [[Types]] — literal types, unions, the primitives being aliased
- [[Enums]] — the runtime alternative to a literal union
- [[Generics]] — generic aliases
- [[Tutorial - TypeScript Basics]]
