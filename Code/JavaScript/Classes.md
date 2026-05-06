---
tags:
  - javascript
type: note
related:
  - "[[JavaScript]]"
  - "[[Prototypes]]"
  - "[[Functions]]"
---
# Classes

ES6 class syntax for object-oriented JavaScript.

## Basic Class

```js
class Animal {
  constructor(name) {
    this.name = name;  // instance property
  }

  speak() {
    return `${this.name} makes a noise.`;
  }
}

const a = new Animal('Dog');
a.speak();  // 'Dog makes a noise.'
```

## Inheritance

```js
class Dog extends Animal {
  constructor(name) {
    super(name);         // must call super() before using this
    this.type = 'dog';
  }

  speak() {
    return `${this.name} barks.`;
  }

  parentSpeak() {
    return super.speak();  // call parent method
  }
}

const d = new Dog('Rex');
d.speak();       // 'Rex barks.'
d instanceof Dog     // true
d instanceof Animal  // true
```

## Static Methods and Properties

Belong to the class itself, not instances:

```js
class MathUtils {
  static PI = 3.14159;

  static circle(r) {
    return MathUtils.PI * r * r;
  }
}

MathUtils.PI         // 3.14159
MathUtils.circle(5)  // 78.53...
new MathUtils().circle(5)  // TypeError — not on instance
```

## Private Fields

Prefixed with `#` — truly private, not accessible outside the class:

```js
class BankAccount {
  #balance = 0;           // private field
  #transactionCount = 0;  // private field

  deposit(amount) {
    if (amount <= 0) throw new Error('Invalid amount');
    this.#balance += amount;
    this.#transactionCount++;
  }

  get balance() { return this.#balance; }
}

const account = new BankAccount();
account.deposit(100);
account.balance       // 100
account.#balance      // SyntaxError — cannot access private field
```

## Getters and Setters

Computed properties with get/set:

```js
class Temperature {
  #celsius;

  constructor(celsius) { this.#celsius = celsius; }

  get fahrenheit() {
    return this.#celsius * 9/5 + 32;
  }

  set fahrenheit(f) {
    this.#celsius = (f - 32) * 5/9;
  }

  get celsius() { return this.#celsius; }
}

const t = new Temperature(0);
t.fahrenheit       // 32
t.fahrenheit = 212;
t.celsius          // 100
```

## Field Declarations

Class fields can be declared at the top — no constructor needed for simple cases:

```js
class User {
  name = '';          // public field with default
  #id = Math.random(); // private field
  role = 'user';

  constructor(name) {
    this.name = name;
  }
}
```

## Static Blocks

Run initialization code once when the class is defined:

```js
class Config {
  static debug;
  static version;

  static {
    Config.debug = process.env.NODE_ENV !== 'production';
    Config.version = '1.0.0';
  }
}
```

## instanceof and Type Checking

```js
class Cat extends Animal {}

const c = new Cat('Whiskers');
c instanceof Cat     // true
c instanceof Animal  // true — checks prototype chain
c instanceof Dog     // false
typeof c             // 'object' — not useful for classes
c.constructor === Cat  // true
```

## Class Expressions

```js
const Foo = class {
  greet() { return 'hello'; }
};

// Named class expression
const Bar = class BarInternal {
  // BarInternal only accessible inside the class
};
```

## Mixins — Multiple Inheritance Pattern

JavaScript classes have single inheritance. Mixins compose behavior:

```js
const Serializable = (Base) => class extends Base {
  serialize() { return JSON.stringify(this); }
  static deserialize(json) { return Object.assign(new this(), JSON.parse(json)); }
};

const Timestamped = (Base) => class extends Base {
  constructor(...args) {
    super(...args);
    this.createdAt = new Date();
  }
};

class User extends Timestamped(Serializable(class {})) {
  constructor(name) {
    super();
    this.name = name;
  }
}
```

## Tips

- Classes are syntactic sugar over prototypes — they compile to the same prototype-based system
- Always call `super()` first in a subclass constructor
- Private fields (`#`) are the only true encapsulation in JS — naming conventions like `_private` are not enforced
- Static methods work well for factory functions and utility methods that don't need instance state
- Prefer composition over deep inheritance chains

## See Also

- [[Prototypes]] — The underlying prototype chain
- [[Functions]] — this binding and constructors
- [[JavaScript]]
