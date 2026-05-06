---
tags:
  - javascript
type: note
related:
  - "[[JavaScript]]"
  - "[[Classes]]"
  - "[[Objects]]"
---
# Prototypes

JavaScript's inheritance model — the foundation that classes are built on.

## The Prototype Chain

Every object has a hidden `[[Prototype]]` link to another object (or `null`). When you access a property, JS walks this chain until it finds it or reaches `null`.

```js
const animal = { breathes: true };
const dog = { barks: true };

Object.setPrototypeOf(dog, animal);  // dog's prototype is animal

dog.barks    // true  — own property
dog.breathes // true  — found on prototype
dog.flies    // undefined — not found anywhere in chain
```

### The default chain

```js
const obj = {};
//  obj  →  Object.prototype  →  null
obj.toString()  // found on Object.prototype
obj.hasOwnProperty('x')  // found on Object.prototype
```

## Object.create

Create an object with a specific prototype:

```js
const animalProto = {
  speak() { return `${this.name} makes a sound.`; }
};

const dog = Object.create(animalProto);
dog.name = 'Rex';
dog.speak();  // 'Rex makes a sound.'

// Object with no prototype (no toString, no hasOwnProperty, etc.)
const bare = Object.create(null);
```

## Constructor Functions (pre-class style)

Before ES6 classes, this was the standard pattern:

```js
function Animal(name) {
  this.name = name;
}

Animal.prototype.speak = function() {
  return `${this.name} makes a sound.`;
};

const dog = new Animal('Rex');
dog.speak();  // 'Rex makes a sound.'

// new does:
// 1. Creates a new object
// 2. Sets its [[Prototype]] to Animal.prototype
// 3. Calls Animal with this = the new object
// 4. Returns the new object
```

## How Classes Map to Prototypes

Classes are syntactic sugar:

```js
class Animal {
  constructor(name) { this.name = name; }
  speak() { return `${this.name} makes a sound.`; }
}

// Equivalent to:
function Animal(name) { this.name = name; }
Animal.prototype.speak = function() { return `${this.name} makes a sound.`; };
```

Methods defined in a class body live on the prototype, not on each instance. This is efficient — one copy of each method shared across all instances.

```js
const a = new Animal('Cat');
const b = new Animal('Dog');

a.speak === b.speak  // true — same function, on Animal.prototype
```

## Prototype Inspection

```js
class Foo {}
class Bar extends Foo {}

const b = new Bar();

Object.getPrototypeOf(b) === Bar.prototype  // true
Object.getPrototypeOf(Bar.prototype) === Foo.prototype  // true

b instanceof Bar  // true
b instanceof Foo  // true

// Own vs inherited properties
b.hasOwnProperty('x')  // false
Object.hasOwn(b, 'x')  // false — modern equivalent

// All property names (own + inherited, enumerable)
for (const key in b) { console.log(key); }

// Own enumerable keys only
Object.keys(b)
```

## Extending Built-ins

```js
class MyArray extends Array {
  sum() {
    return this.reduce((a, b) => a + b, 0);
  }
}

const arr = new MyArray(1, 2, 3);
arr.sum()   // 6
arr.map(x => x * 2)  // MyArray [2, 4, 6] — preserves subclass
```

## When This Matters in Practice

You won't usually write prototype code directly in modern JS — classes handle it. But understanding prototypes explains:

- Why methods from parent classes work on instances
- Why `instanceof` checks the chain, not just the direct class
- Why adding to `Array.prototype` affects all arrays (monkey-patching)
- What `__proto__` (deprecated) was doing

## Tips

- Use classes — don't manipulate `[[Prototype]]` directly in application code
- `Object.create(null)` is useful for pure hash maps with no inherited keys
- `hasOwnProperty` vs `in`: `in` checks the whole chain, `hasOwnProperty` only checks the object
- Methods on the prototype are shared — instance properties set in `constructor` are per-instance

## See Also

- [[Classes]] — Syntax built on top of prototypes
- [[Objects]] — Object creation and properties
- [[JavaScript]]
