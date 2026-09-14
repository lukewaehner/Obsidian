---
tags:
  - typescript
  - javascript
type: note
related:
  - "[[TypeScript]]"
  - "[[Functions]]"
date: 2026-09-14
---
# Generics

Pass **types** to a function or class the way you pass values, making it work over many types instead of one.

The tutorial's note on where this pays off: *"especially useful when working with HTTP requests."* A `get<T>(url)` that returns `T` is the difference between a typed API client and one that hands you `any`.

## Generic Functions

```ts
function myFunc<T>(data: T): T {
    console.log(data);
    return data
}

let x: string = myFunc<string>('some string');
let y: number = myFunc<number>(5);
```

`<T>` declares a **type parameter**. At each call site it's bound to a concrete type, and the `: T` return annotation ties the output type to the input type.

Usually you can omit the explicit `<string>` — TypeScript infers it from the argument:

```ts
let x = myFunc('some string');   // T inferred as string
let y = myFunc(5);               // T inferred as number
```

## Why Not `any`

This is the comparison that makes generics click:

```ts
function identityAny(data: any): any { return data; }
function identityGeneric<T>(data: T): T { return data; }

const a = identityAny('hello');       // a: any     — .toUpperCase() unchecked, .toFixed() also "fine"
const b = identityGeneric('hello');   // b: string  — .toFixed() is an error
```

Both accept anything. Only the generic one **remembers what it was given**. `any` throws the type away; `T` carries it through.

## Generic Classes and Interfaces

```ts
class myClass<T> {

}

interface IMyInterface<T> {

}
```

Filled in, a generic container looks like:

```ts
class Box<T> {
  private _items: T[] = [];

  public add(item: T): void {
    this._items.push(item);
  }

  public get(index: number): T | undefined {
    return this._items[index];
  }
}

const numbers = new Box<number>();
numbers.add(1);
numbers.add('two');      // Error: not assignable to parameter of type 'number'
```

The type parameter is fixed when the instance is created and applies across every member.

## Multiple Type Parameters

```ts
function pair<K, V>(key: K, value: V): [K, V] {
  return [key, value];
}

const p = pair('age', 30);    // [string, number]
```

Conventional single letters: `T` (type), `K` (key), `V` (value), `E` (element), `R` (result). Past two or three, name them properly — `<TRequest, TResponse>` reads better than `<T, U>`.

## Constraints

An unconstrained `T` can be anything, so you can't do much with it. `extends` narrows what's allowed:

```ts
function longest<T extends { length: number }>(a: T, b: T): T {
  return a.length >= b.length ? a : b;
}

longest('abc', 'de');        // fine — strings have length
longest([1, 2], [3]);        // fine — arrays have length
longest(1, 2);               // Error: number has no 'length'
```

Now the body can read `.length` because the constraint guarantees it, and the *return* type is still the caller's exact type — not the constraint.

## Defaults

```ts
interface ApiResponse<T = unknown> {
  status: number;
  data: T;
}

const r1: ApiResponse = { status: 200, data: 'anything' };          // T = unknown
const r2: ApiResponse<string[]> = { status: 200, data: ['a'] };     // T = string[]
```

Note `= unknown` rather than `= any` — the same [[Types|reasoning]] applies to defaults.

## Generics You Already Use

Most of the standard library is generic:

```ts
Array<T>                  // number[] is Array<number>
Promise<T>                // await gives you T
Map<K, V> / Set<T>
Record<K, V>              // { [key in K]: V }
Partial<T>                // all properties optional
Readonly<T>               // all properties readonly
Pick<T, K> / Omit<T, K>   // subset / complement of a shape
```

```ts
interface User { id: string; name: string; email: string }

type UserUpdate = Partial<User>;              // every field optional
type PublicUser = Omit<User, 'email'>;        // id and name only
```

`map` on an array is `map<U>(fn: (x: T) => U): U[]` — that's how `string[].map(s => s.length)` produces `number[]` in [[Array Functions]].

## The HTTP Case

```ts
async function getJson<T>(url: string): Promise<T> {
  const response = await fetch(url);
  return response.json() as T;
}

const user = await getJson<User>('/api/user/1');   // user: User
```

One function, typed results everywhere it's called. Without the type parameter, the return is `Promise<any>` and every caller is untyped.

> [!warning] The cast is a promise you're making
> `as T` asserts a shape the compiler cannot verify — the server could return anything. In the CS 4530 stack, **Zod** does the runtime validation that makes the claim true. A generic signature over an unvalidated response is a lie with good autocomplete.

## Tips
- Let inference do the work. Write the explicit `<T>` at a call site only when inference gets it wrong or there's no argument to infer from.
- Constrain type parameters as soon as the body needs a capability. `<T extends { id: string }>` is more useful than `<T>` plus a cast.
- A type parameter used only once in a signature probably isn't doing anything — check whether you wanted a plain union.
- Generics are compile-time only. There's no runtime `T`, so you can't write `new T()` or `x instanceof T`.

## See Also
- [[Functions]] — signatures and overloads
- [[Classes]] · [[Interfaces]] — where `<T>` attaches
- [[Type Aliases]] — generic aliases and discriminated unions
- [[Arrays]] · [[Array Functions]] — `Array<T>` and `map<U>`
- [[Tutorial - TypeScript Basics]] · [[Tutorial - API Requests]]
