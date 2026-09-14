---
tags:
  - typescript
  - javascript
type: note
related:
  - "[[TypeScript]]"
  - "[[OOP Principles]]"
date: 2026-09-14
---
# Classes

Blueprints for creating objects.

A class can contain **properties, methods, and a constructor**. Beyond that:

- All members can have an **access modifier**: `public`, `protected`, `private`.
- Members can be **`static`** (shared across all instances) and **`readonly`** (immutable).
- Properties may have **getters and setters**.
- Classes can **`extend`** other classes.
- Classes can **`implement`** [[Interfaces|interfaces]].

## Anatomy

A class definition can include:

- **Fields** — any variable declared in a class. Fields represent data pertaining to objects.
- **Constructors** — responsible for allocating memory for the objects of the class.
- **Functions** — actions an object can take. Also called methods.

## The Full Example

```ts
class Person {

    private _firstName: string = '';
    protected middleName!: string;
    public _lastName: string = '';

    private static readonly NeverGonnaGiveYouUp: any;
    protected static readonly NeverGonnaLetYouDown: any;
    public static readonly isRickRolled: boolean = true;

    constructor() {
        // I execute when you call new Person().
        // No access modifier === public by default.
        // Make me private if implementing a singleton.
    }

    public anyoneCanCallMe(): void {
        this.childClassesCanCallMe();
    }

    protected childClassesCanCallMe(): void {
        this.onlyAccessibleInsidePerson();
    }

    private onlyAccessibleInsidePerson(): void {
        // I lied, anyone can call me if you know how.
        // Welcome to JavaScript :p
    }

    public get firstName(): string {
        return this._firstName;
    }

    public set firstName(firstname: string) {
        this._firstName = firstname;
    }

}

const person = new Person();
person.firstName = 'first';
console.log(person.firstName);
person.anyoneCanCallMe();

class SpecialPerson extends Person {
    // I contain everything person has, and can extend/override it.

    constructor() {
        super() // I call the constructor for Person.
    }

}
```

## Access Modifiers

| Modifier | Visible from |
| --- | --- |
| `public` | anywhere — **the default** when you write nothing |
| `protected` | the declaring class and its subclasses |
| `private` | only inside the declaring class |

The example's chain demonstrates exactly this: `anyoneCanCallMe` (public) calls `childClassesCanCallMe` (protected), which calls `onlyAccessibleInsidePerson` (private). Each level can reach inward; nothing outside can reach past `public`.

> [!warning] `private` is compile-time only
> The comment in the example — *"I lied, anyone can call me if you know how"* — is the important part. TypeScript's `private` is erased at compile time. At runtime it's an ordinary property, reachable via `(person as any).onlyAccessibleInsidePerson()`. It stops honest mistakes, not determined callers.
>
> If you need runtime privacy, JavaScript's `#field` syntax gives it. `private` gives you a *design* contract, which is what [[OOP Principles|encapsulation]] is actually about.

> [!important] Course convention
> Private property names must start with `_` — `_firstName`, `_balance`. See [[CS4530 Code Style Guide]].

## static and readonly

- **`static`** — belongs to the class, not to instances. `Person.isRickRolled`, never `person.isRickRolled`.
- **`readonly`** — assignable at declaration or in the constructor, never after.

They combine with access modifiers freely, which is what the three `NeverGonna*` lines are showing: `private static readonly`, `protected static readonly`, `public static readonly`.

```ts
class Config {
  public static readonly VERSION = '1.0';    // a class-level constant
  private readonly _id: string;

  constructor(id: string) {
    this._id = id;       // legal — constructor assignment to readonly
  }
}
```

## The `!` Definite Assignment Assertion

```ts
protected middleName!: string;
```

The `!` tells the compiler *"I promise this gets assigned before anyone reads it — stop warning me."* Under `strictPropertyInitialization`, a field with no initializer and no constructor assignment is an error; `!` suppresses that check.

It's an assertion, not a guarantee. If nothing ever assigns it, the field is `undefined` at runtime and the type says `string`. Use it sparingly — a default value or a constructor parameter is almost always better.

## Getters and Setters

```ts
public get firstName(): string {
    return this._firstName;
}

public set firstName(firstname: string) {
    this._firstName = firstname;
}
```

Accessed as a property, not a method — `person.firstName = 'first'`, no parentheses. The pair wraps the private `_firstName` field.

The point isn't the pass-through shown here, it's that the accessor is a **seam**: you can add validation, logging, or a computed value later without changing a single caller.

```ts
public set age(value: number) {
    if (value < 0) {
      throw new Error(`Age cannot be negative, got ${value}`);
    }
    this._age = value;
}
```

A getter with no setter gives you a read-only property from the outside and a mutable field inside — the standard encapsulation shape.

## Constructors

```ts
constructor() {
    // No access modifier === public by default.
    // Make me private if implementing a singleton.
}
```

A `private constructor` blocks `new` from outside the class, which is how you force construction through a static factory method (`Person.create(...)`) or enforce a singleton.

**Parameter properties** are a TypeScript shorthand worth knowing — an access modifier on a constructor parameter declares *and* assigns the field:

```ts
class Point {
  constructor(private readonly _x: number, private readonly _y: number) {}
  // no separate field declarations, no this._x = _x needed
}
```

## Inheritance

```ts
class SpecialPerson extends Person {
    constructor() {
        super()   // I call the constructor for Person.
    }
}
```

A subclass contains everything the parent has and can extend or override it. **`super()` must be called before any use of `this`** in a subclass constructor. Full treatment in [[OOP Principles]].

## Abstract Classes

Declared with the `abstract` keyword. Abstract classes are **mainly for inheritance** — other classes derive from them, and **you cannot create an instance of one**.

An abstract class typically includes one or more abstract methods or property declarations. **The class that extends it must define all the abstract members.**

```ts
abstract class Person {
 abstract name: string;
 display(): void {
     console.log(this.name);
 }
}

class Employee extends Person {
 name: string;
 empCode: number;

 constructor(name: string, code: number) {
     super(); // must call super()
     this.empCode = code;
     this.name = name;
 }
}

let emp: Person = new Employee("James", 100);
emp.display(); //James
```

Notice what this buys: `display()` is **concrete** and lives on the parent, but it uses `this.name`, which is **abstract** and supplied by the child. The parent defines the algorithm; the child fills in the piece only it knows. That's the difference between an abstract class and an [[Interfaces|interface]] — the abstract class can ship shared implementation.

Notice also `let emp: Person = new Employee(...)`. You can't *instantiate* `Person`, but you can hold an `Employee` in a `Person`-typed variable. That's the substitutability that makes [[OOP Principles|polymorphism]] work.

## Abstract Class vs Interface

| | `abstract class` | `interface` |
| --- | --- | --- |
| Can hold implementation | yes | no |
| Can hold state (fields) | yes | no (shape only) |
| A class can have how many | one (`extends`) | many (`implements`) |
| Exists at runtime | yes | no — fully erased |
| Access modifiers | yes | no — all public |

Use an interface for a contract. Use an abstract class when subclasses need to **share code**, not just a shape.

## Tips
- Default to `private` and widen only when required. Minimize the public surface.
- Back every public getter/setter with a `_`-prefixed private field. That's both the course convention and the encapsulation pattern.
- Prefer composition to inheritance. `extends` couples the child to the parent's internals permanently; a field holding a collaborator does not.
- Use parameter properties (`constructor(private readonly _x: number)`) to cut the declare-then-assign boilerplate.
- Arrow-function class members capture `this` correctly — see the `setTimeout` example in [[Functions]].

## See Also
- [[OOP Principles]] — inheritance, polymorphism, abstraction, encapsulation
- [[Interfaces]] — the contract you `implement`
- [[Functions]] — methods, `this`, arrow functions
- [[Generics]] — `class MyClass<T>`
- [[Objects]] · [[CS4530 Code Style Guide]]
- [[Tutorial - TypeScript Basics]]
