---
tags:
  - typescript
  - javascript
type: moc
related:
  - "[[Code]]"
---
# TypeScript

A **superset of JavaScript** that adds optional static typing. All valid JavaScript is valid TypeScript; what TypeScript adds is a typechecker that runs at compile time and emits nothing at runtime.

Typing is optional to the language. It is **not optional in [[Fundamentals of Software Engineering|CS 4530]]** — these notes are written against [[Tutorial - TypeScript Basics]] and follow the [[CS4530 Code Style Guide]].

## The Type System

- [[Types]] — boolean, number, bigint, string, `any`, `unknown`, literal types
- [[Variables]] — `var` vs `let` vs `const`, scoping
- [[Arrays]] — typed collections, and why `let x = []` is a trap
- [[Tuples]] — fixed-length arrays with per-index types
- [[Enums]] — key-to-value maps, and when a literal union is better
- [[Objects]] — key-value pairs, three ways to type one

## Control

- [[Control Flow]] — if/else, switch, ternary, == vs === narrowing
- [[Loops]] — for, while, do-while, and why to prefer array operators
- [[Array Functions]] — `forEach`, `map`, `filter`, `reduce`

## Functions

- [[Functions]] — typing, optional/default/rest params, arrow functions, overloads

## Types & Structures

- [[Classes]] — fields, constructors, access modifiers, static, readonly, getters/setters, abstract
- [[Interfaces]] — contracts, `implements`, structural typing
- [[Type Aliases]] — naming any type, unions, discriminated unions
- [[Generics]] — type parameters over functions, classes, and interfaces

## Design

- [[OOP Principles]] — inheritance, polymorphism, abstraction, encapsulation

## Ecosystem

- [[Modules]] — `export` / `import`, `import type`, default exports
- [[Tooling]] — `tsconfig.json`, `strict`, naming conventions, linter and formatter

## Quick Reference

```ts
// Annotated declarations — prefer const
const count: number = 0;
let name: string = 'ada';

// Functions: annotate params (required) and return (good practice)
function add(a: number, b: number): number {
  return a + b;
}

// Optional, default, rest
function log(msg: string, userId = 'anon', ...tags: string[]): void {}

// Arrow function — lexical `this`, the default for callbacks
const double = (n: number): number => n * 2;

// Always type an empty array
const items: string[] = [];

// Tuple — fixed length, per-index types
const entry: [string, number] = ['age', 30];

// Literal union — an enum with no runtime cost
type Status = 'pending' | 'active' | 'closed';

// Interface for a shape, type for a union
interface IUser { id: string; name: string; email?: string }
type ID = string | number;

// Class with encapsulation
class Account {
  private _balance: number = 0;
  public get balance(): number { return this._balance; }
  public withdraw(amount: number): boolean {
    if (this._balance <= amount) return false;
    this._balance -= amount;
    return true;
  }
}

// Generic — remembers the type, unlike `any`
function identity<T>(value: T): T { return value; }

// unknown, not any — then narrow
function len(x: unknown): number {
  return typeof x === 'string' ? x.length : 0;
}

// Array operators over loops
const evens = nums.filter(n => n % 2 === 0);
const total = nums.reduce((sum, n) => sum + n, 0);   // always pass the initial value

// Strict equality, always
if (a === b) {}

// Modules — named exports, `type` prefix for types
export function add(x: number, y: number): number { return x + y; }
import { add, type IUser } from './math';
```

## Differences from JavaScript

Everything TypeScript adds is erased before the code runs. The full list of constructs with **no JavaScript equivalent**:

| Construct | Runtime cost |
| --- | --- |
| Type annotations, aliases, interfaces | none — erased |
| `Generics` type parameters | none — erased |
| `public` / `protected` / `private` | none — erased ([[Classes]]) |
| `readonly`, `abstract` | none — erased |
| Function overload signatures | none — one function emitted |
| **`enum`** | **emits a real object** ([[Enums]]) |

Enums are the single exception worth remembering. Everything else you write in TypeScript that isn't JavaScript disappears — which is why you cannot check `x instanceof IPerson` and why runtime validation (Zod) is a separate job from typing.

## Course Context

- [[Tutorial - TypeScript Basics]] — the CS 4530 tutorial these notes map to
- [[CS4530 Code Style Guide]] — kebab-case files, camelCase members, `_` private prefix
- [[Individual Project 1]] — first use of all of this; `tsconfig.json` is off-limits
- [[Tutorial - Unit Testing with Vitest]] — testing the code you type
- [[Tutorial - API Requests]] — where [[Generics]] pays off

## See Also

- [[JavaScript]] — the language TypeScript extends
- [[React]] — TSX, components, and the default-export convention
- [[Code]] — main programming hub

%% Begin Waypoint %%
- [[Array Functions]]
- [[Arrays]]
- [[Classes]]
- [[Control Flow]]
- [[Enums]]
- [[Functions]]
- [[Generics]]
- [[Interfaces]]
- [[Loops]]
- [[Modules]]
- [[OOP Principles]]
- [[Objects]]
- [[Tooling]]
- [[Tuples]]
- [[Type Aliases]]
- [[Types]]
- [[Variables]]

%% End Waypoint %%
