---
tags:
  - javascript
type: note
related:
  - "[[JavaScript]]"
  - "[[Destructuring]]"
  - "[[Prototypes]]"
  - "[[Classes]]"
---
# Objects

Working with objects — the foundation of JavaScript's data model.

## Creating Objects

```js
// Object literal
const point = { x: 1, y: 2 };

// Property shorthand — when variable name matches key
const x = 1, y = 2;
const point = { x, y };   // same as { x: x, y: y }

// Computed property names
const key = 'name';
const obj = { [key]: 'Alice', [`${key}Upper`]: 'ALICE' };

// From entries
Object.fromEntries([['a', 1], ['b', 2]])  // { a: 1, b: 2 }
```

## Accessing Properties

```js
const user = { name: 'Alice', address: { city: 'NYC' } };

user.name            // 'Alice' — dot notation
user['name']         // 'Alice' — bracket notation (dynamic keys)

const key = 'name';
user[key]            // 'Alice' — use bracket when key is a variable
```

### Optional chaining `?.`

Access nested properties without throwing if intermediate value is null/undefined:

```js
user.address?.city         // 'NYC'
user.phone?.number         // undefined — doesn't throw
user.getInfo?.()           // undefined — optional method call
arr?.[0]                   // optional index access
```

### Nullish coalescing `??`

Return right side only when left is `null` or `undefined` (not `0`, `''`, `false`):

```js
user.nickname ?? 'Anonymous'  // 'Anonymous' if null or undefined
user.age ?? 0                 // 0 if null/undefined, not if 0
user.age || 0                 // 0 if falsy — different behavior!
```

## Modifying Objects

```js
const obj = { a: 1 };

obj.b = 2;            // add property
obj.a = 10;           // update property
delete obj.a;         // remove property

// Check if property exists
'a' in obj            // false — checks prototype chain too
obj.hasOwnProperty('b')  // true — own properties only
Object.hasOwn(obj, 'b')  // true — modern alternative
```

## Spread and Merging

```js
const defaults = { color: 'red', size: 'medium' };
const overrides = { size: 'large', weight: 10 };

const merged = { ...defaults, ...overrides };
// { color: 'red', size: 'large', weight: 10 }
// rightmost wins on conflict

const copy = { ...obj };     // shallow copy
const extended = { ...obj, newProp: 'value' };
```

## Destructuring

```js
const { name, age } = user;
const { name: userName, age: userAge } = user;  // rename
const { name, role = 'guest' } = user;          // default value
const { address: { city } } = user;             // nested
const { name, ...rest } = user;                 // rest
```

## Object Static Methods

### Iteration

```js
const obj = { a: 1, b: 2, c: 3 };

Object.keys(obj)    // ['a', 'b', 'c']
Object.values(obj)  // [1, 2, 3]
Object.entries(obj) // [['a',1], ['b',2], ['c',3]]

// Iterate
for (const [key, value] of Object.entries(obj)) {
  console.log(`${key}: ${value}`);
}

// Transform
const doubled = Object.fromEntries(
  Object.entries(obj).map(([k, v]) => [k, v * 2])
);
```

### Copying and merging

```js
Object.assign({}, defaults, overrides)  // like spread, mutates first arg
```

### Freezing and sealing

```js
Object.freeze(obj)   // no add/modify/delete — shallow
Object.seal(obj)     // no add/delete, can modify existing
Object.isFrozen(obj) // true
```

### Property descriptors

```js
Object.defineProperty(obj, 'x', {
  value: 42,
  writable: false,    // can't change value
  enumerable: false,  // won't show in for...in or Object.keys
  configurable: false // can't delete or redefine
});

Object.getOwnPropertyDescriptor(obj, 'x')
// { value: 42, writable: false, enumerable: false, configurable: false }
```

## Computed and Dynamic Patterns

```js
// Build object from array
const keys = ['a', 'b', 'c'];
const obj = Object.fromEntries(keys.map((k, i) => [k, i]));
// { a: 0, b: 1, c: 2 }

// Conditional properties
const includeAge = true;
const user = {
  name: 'Alice',
  ...(includeAge && { age: 30 }),  // only added if true
};

// Group by (ES2024)
const grouped = Object.groupBy(people, p => p.department);
```

## Tips

- Use `?.` to safely access deeply nested data from APIs
- Prefer `??` over `||` for defaults — `||` treats `0` and `''` as missing
- `Object.freeze` is shallow — nested objects can still be mutated
- `in` operator checks the prototype chain — use `Object.hasOwn` for own properties only
- Spread creates a shallow copy — nested objects are still shared references

## See Also

- [[Destructuring]] — Object destructuring in depth
- [[Prototypes]] — Prototype chain and inheritance
- [[Classes]] — Object-oriented patterns
- [[Maps and Sets]] — When to use Map instead of plain objects
- [[JavaScript]]
