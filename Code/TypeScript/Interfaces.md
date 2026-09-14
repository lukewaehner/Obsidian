---
tags:
  - typescript
  - javascript
type: note
related:
  - "[[TypeScript]]"
  - "[[Classes]]"
date: 2026-09-14
---
# Interfaces

**Contracts for interaction with external entities.** If an interface has a property or method, any object or class that implements it must have it too.

Interfaces are also how you define custom types for objects in TypeScript.

## Declaring and Implementing

```ts
//Interface IPerson respresents a person by attributes firstName and lastName and a method to getFullName()
interface IPerson {
    firstName: string;
    lastName: string;
    getFullName(): string;
}

//Class Person implements interface Iperson. Person class must contains all the attributes and methods of interface.
class Person implements IPerson {

    public firstName: string = '';
    public lastName: string = '';

    public getFullName(): string {
        return this.firstName + ' ' + this.lastName;
    }

    // It can contain any other properties/methods but must contain those in the interface.

}

const person: IPerson = new Person();
```

Two directions to read here:

- **The class must satisfy the interface.** Drop `getFullName` and `implements IPerson` fails to compile.
- **The class may exceed it.** Extra members are fine. The interface is a floor, not a ceiling.

And note the declaration on the last line: `const person: IPerson = new Person()`. The variable is typed by the **contract**, not the implementation. Code holding `person` can only see the three interface members, even though the object has more. That's the decoupling interfaces exist for — swap in a different `IPerson` implementation and nothing downstream changes.

## Typing Objects

An interface doesn't need a class. It's the recommended way to type any reused object shape:

```ts
interface IStudent {
    name: string;
    age: number;
    studentID: number;
    gender: string;
    isEnrolled: boolean;
}

const student: IStudent = {
    name: 'name',
    age: 20,
    studentID: 111111111,
    gender: 'hidden',
    isEnrolled: true
};
```

## Structural Typing

TypeScript's type system is **structural**, not nominal. A type matches if the shape matches — no `implements` declaration required:

```ts
interface Named { name: string }

function greet(x: Named) { console.log(x.name); }

greet({ name: 'Ada', age: 36 });     // object literal: extra property flagged
const p = { name: 'Ada', age: 36 };
greet(p);                             // fine — p's shape includes name: string
```

`implements` on a class is therefore a **check**, not a requirement. Writing it makes the intent explicit and makes the compiler tell you at the class when you break the contract, rather than at every call site.

## Optional, readonly, and Methods

```ts
interface RequestOptions {
  url: string;
  method?: 'GET' | 'POST';        // optional
  readonly retries: number;       // set once
  onError(e: Error): void;        // method
  transform: (body: string) => string;   // property holding a function
}
```

The last two are equivalent in practice; the arrow-property form is more precise about the function type and works better with `strictFunctionTypes`.

## Extending

An interface can extend one or many:

```ts
interface Animal { name: string }
interface Pet extends Animal { owner: string }
interface Service extends Animal, Pet { start(): void }
```

A class can implement **many** interfaces but extend only one class:

```ts
class Dog extends Animal implements Pet, Serializable { /* ... */ }
```

That asymmetry is why [[OOP Principles|abstraction]] is usually expressed with interfaces — you can apply one to any class anywhere in the hierarchy, which the tutorial's `Fee` example demonstrates.

## Declaration Merging

Unique to interfaces: declaring the same interface twice **merges** the declarations.

```ts
interface Window { myApp: string }
interface Window { myVersion: number }
// Window now has both
```

Useful for augmenting third-party types. A source of confusion everywhere else — [[Type Aliases|`type`]] errors on redeclaration instead, which is usually what you want.

## Interface vs Type vs Abstract Class

| Need | Use |
| --- | --- |
| Shape of an object, reused | `interface` |
| Union of different types | `type` |
| Shared implementation across subclasses | `abstract class` |
| A contract applied to unrelated classes | `interface` |

The `I` prefix (`IPerson`, `IStudent`) is the tutorial's convention and appears in the CS 4530 codebase. It is not universal in the wider TypeScript community — follow what the repo you're in already does.

## Tips
- Type variables and parameters by the interface, never by the concrete class. That's the point.
- Interfaces are fully erased — zero runtime cost, and you cannot check `x instanceof IPerson`. To discriminate at runtime, add a literal `kind` field, or use a validator (Zod in the CS 4530 stack).
- Keep interfaces small. An interface with twelve members is one no implementer can satisfy honestly.
- `implements` is optional but write it anyway. It moves the error to the class.

## See Also
- [[Classes]] — `implements`, abstract classes, access modifiers
- [[Type Aliases]] — unions and the `type` keyword
- [[OOP Principles]] — abstraction via interfaces
- [[Objects]] · [[Generics]]
- [[Tutorial - TypeScript Basics]] · [[CS4530 Code Style Guide]]
