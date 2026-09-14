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
# Enums

A way to enumerate the possible values for a type. Unordered data structures that map **keys to values**.

## Numeric Enums

```ts
enum Language {
  English,
  Spanish,
  Russian
}
```

With no explicit values, members are auto-numbered from `0`:

```ts
Language.English   // 0
Language.Spanish   // 1
Language.Russian   // 2
```

You can set them yourself; unset members continue from the last one:

```ts
enum Status {
  Pending = 1,
  Active,        // 2
  Closed = 10,
  Archived       // 11
}
```

## String Enums

```ts
enum Language {
  English = 'en',
  Spanish = 'es',
  Russian = 'ru'
}
```

The tutorial's framing: there are two kinds of enum — **strings to strings**, and **strings to numbers**.

String enums are the safer default. A numeric enum member is assignable from *any* number in older TypeScript configurations, and its runtime value (`0`) is meaningless in a log or a database row. `'en'` is self-describing.

## Why Use One

Per the tutorial: when you want flexibility, when it makes intentions and use cases easier to express and document, or when you want to save compile-time and runtime with inline code.

The practical version: an enum replaces a bag of magic strings scattered across files with one named, discoverable, autocompleting set.

## The `const enum` Variant

```ts
const enum Direction { Up, Down }
```

A `const enum` is **inlined** at every use site and emits no runtime object at all. That's the "save runtime" case above. The cost is that it can't be iterated or looked up dynamically.

## Enum vs Literal Union

A plain [[Types|literal]] union does most of what an enum does, with no runtime footprint:

```ts
type Language = 'en' | 'es' | 'ru';       // no emitted JavaScript

enum LanguageEnum { English = 'en' }      // emits a real object
```

| | Literal union | Enum |
| --- | --- | --- |
| Runtime output | none | an object (unless `const enum`) |
| Iterate the members | no | yes — `Object.values(E)` |
| Reverse lookup | no | numeric enums only |
| Autocomplete | yes | yes |
| Import needed at use site | no | yes |

**Reach for a literal union first.** Reach for an enum when you need to enumerate the members at runtime, or when the name carries documentation value that the bare string doesn't.

> [!warning] Enums are a TypeScript-only construct
> Unlike everything in [[Types]], an enum is not JavaScript — it compiles to an emitted object. That makes it one of the few TS features with a runtime cost, and it's why literal unions are often preferred in modern codebases.

## Tips

- Prefer string enums over numeric ones. The runtime values end up in logs, URLs, and databases, and `2` tells you nothing.
- Use `switch` over an enum and let the compiler check exhaustiveness — see [[Control Flow]].
- Don't reach for an enum to hold two values. `boolean` or a literal union is clearer.

## See Also

- [[Types]] — literal types and unions
- [[Type Aliases]] — the union alternative
- [[Control Flow]] — `switch` over enum members
- [[Tutorial - TypeScript Basics]]
