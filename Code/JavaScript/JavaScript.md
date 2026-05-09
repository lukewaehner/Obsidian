---
tags:
  - javascript
type: moc
---
# JavaScript

A dynamic, interpreted language for the web and beyond (Node.js, Deno, Bun).

## Core Language

- [[Variables]] — var, let, const, scope, hoisting
- [[Types]] — primitives, coercion, equality, truthy/falsy
- [[Functions]] — declarations, expressions, arrows, this, closures
- [[Control Flow]] — if/else, loops, switch, optional chaining
- [[Destructuring]] — arrays, objects, defaults, renaming, rest

## Data Structures

- [[Arrays]] — methods, spread, Array.from
- [[Objects]] — literals, shorthand, spread, Object methods
- [[Maps and Sets]] — Map, Set, WeakMap, WeakSet

## Object Oriented

- [[Classes]] — class syntax, inheritance, private fields, static
- [[Prototypes]] — prototype chain, Object.create

## Functional

- [[Closures]] — scope chain, module pattern, memoization
- [[Iterators]] — for...of, Symbol.iterator, generators

## Async

- [[Async]] — event loop, callbacks, Promises, async/await

## Ecosystem

- [[Modules]] — ES modules, CommonJS, dynamic import
- [[Error Handling]] — try/catch, custom errors, async errors
- [[Tooling]] — Node.js, npm, package.json, common tools

## Quick Reference

```js
// Variables
const x = 5;
let y = 10;

// Arrow function
const add = (a, b) => a + b;

// Destructuring
const { name, age } = person;
const [first, ...rest] = arr;

// Async/await
const data = await fetch(url).then(r => r.json());

// Optional chaining
const city = user?.address?.city ?? 'unknown';

// Array methods
const evens = nums.filter(n => n % 2 === 0);
const doubled = nums.map(n => n * 2);
const sum = nums.reduce((acc, n) => acc + n, 0);

// Spread
const merged = { ...defaults, ...overrides };
const combined = [...arr1, ...arr2];
```

## See Also

- [[React]] — UI framework built on JavaScript
- [[Code]] — Main programming hub

%% Begin Waypoint %%
- [[Arrays]]
- [[Async]]
- [[Classes]]
- [[Closures]]
- [[Control Flow]]
- [[Destructuring]]
- [[Error Handling]]
- [[Functions]]
- [[Iterators]]
- [[Maps and Sets]]
- [[Modules]]
- [[Objects]]
- [[Prototypes]]
- [[Tooling]]
- [[Types]]
- [[Variables]]

%% End Waypoint %%
