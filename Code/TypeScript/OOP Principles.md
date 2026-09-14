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
# OOP Principles

Object-oriented programming has four principles: **inheritance, polymorphism, abstraction, encapsulation**. This note is how each one is expressed in TypeScript.

The mechanics live in [[Classes]] and [[Interfaces]]; this is what they're *for*.

| Principle | TypeScript mechanism |
| --- | --- |
| Inheritance | `extends` |
| Polymorphism | method overriding, `super`, substitutability |
| Abstraction | `abstract class`, `interface` |
| Encapsulation | `private` / `protected`, getters and setters |

## Inheritance

The ability to create new classes from an existing class. The extended class is the **parent / super class**; the new ones are **child / sub classes**.

A class inherits with `extends`. Child classes inherit all properties and methods from the parent **except private members and constructors**. TypeScript does **not** support multiple inheritance.

```ts
class child_class_name extends parent_class_name
```

```ts
//Parent class Shape
class Shape {
 Area: number
  constructor(a: number) {
    this.Area = a
 }
}

//Child class Circle that inherits properties of Shape
class Circle extends Shape {
 disp(): void {
    console.log("Area of the circle:  " + this.Area)
 }
}
var obj = new Circle(223);
obj.disp()
```

`Circle` never declares `Area` or a constructor, but `new Circle(223)` works and `this.Area` resolves — both came from `Shape`.

The two exclusions are worth dwelling on:

- **`private` members don't cross.** A subclass cannot see the parent's private state. That's `protected`'s entire reason to exist — inheritable but not public.
- **Constructors don't cross** in the sense of being overridden; a subclass constructor must call `super()` before touching `this`.

> [!tip] No multiple inheritance — use interfaces
> One `extends`, many `implements`. When you need behavior from two places, that's composition (hold both as fields) plus interfaces for the contracts, not a hierarchy.

## Polymorphism

When multiple classes inherit from a parent and **override the same functionality**. Each child implements the property or method its own way.

It also counts when one child overrides and a sibling doesn't — accepting the parent's implementation is still polymorphic, because the siblings now behave differently.

```ts
class CheckingAccount {
  open(initialAmount: number) {
    // code to open account and save in database
  }
}

class BusinessCheckingAccount extends CheckingAccount {
  open(initialAmount: number) {
    if (initialAmount < 1000) {
      throw new Error("Business accounts must have an initial deposit of 1.000 Euros")
    }
    super.open(initialAmount);
  }
}

class PersonalCheckingAccount extends CheckingAccount {
  open(initialAmount: number) {
    if (initialAmount <= 0) {
      throw new Error("Personal accounts must have an initial deposit of more than zero Euros")
    }
    super.open(initialAmount);
  }
}
```

Both children have different business rules for opening an account — different minimum balances. Same method name, different behavior: polymorphic.

Note `super.open(initialAmount)` in both. Each child **extends** the parent's behavior rather than replacing it: validate the child-specific rule, then delegate the shared work upward. That's the pattern to copy.

The payoff is at the call site:

```ts
function openAll(accounts: CheckingAccount[]): void {
  accounts.forEach(a => a.open(5000));   // each runs its own rules
}
```

`openAll` knows nothing about business vs personal. Add a third account type and this function doesn't change. **That** is why polymorphism matters — it's the mechanism by which adding a case doesn't mean editing every caller.

### On overloading

To achieve polymorphism: inherit from a base class, then override methods and write implementation code in them. You can also **overload** methods — methods with the same name and different signatures (different types or number of arguments).

But in TypeScript, methods **aren't** overloaded by simply changing the types or number of arguments the way some other languages allow. To create an overload you either add optional arguments to a method, or overload function declarations in an interface and implement the interface. See [[Functions|function overloads]].

## Abstraction

A way to model objects that **separates duties between a type and the code that inherits it**.

A developer creates a type — a class or interface — that specifies **what** the calling code should implement, but not **how**. The abstract type defines what needs to be done; the consuming types actually do it. Enforce it by inheriting or implementing from abstract classes and interfaces.

The tutorial's example: some bank accounts have fees, but not all. So `Fee` is an interface applied to **specific classes anywhere in the hierarchy**, rather than a method pushed onto the base class.

```ts
interface Fee {
  chargeFee(amount: number );
}

// parent BankAccount and sibling SavingsAccount do not implement Fee interface
class BankAccount { ... }

class SavingsAccount extends BankAccount { ... }

// checking implements Fee
class CheckingAccount extends BankAccount implements Fee {
  chargeFee(amount: number) {}
}
```

Children inherit interface members implemented in their parent — so `BusinessChecking` extending `CheckingAccount` gets `Fee` too:

```ts
// BusinessChecking inherits CheckingAccount and therefore Fee
class BusinessChecking extends CheckingAccount { … }

// Code that uses BusinessChecking can call chargeFee
function CalculateMonthlyStatements() {
  let businessChecking = new BusinessChecking();
  businessChecking.chargeFee(100);
}
```

This is the design lesson in the section: **a capability that only some subtypes have belongs in an interface, not the base class.** Putting `chargeFee` on `BankAccount` would force `SavingsAccount` to either implement a fee it doesn't charge or throw — the classic wrong-abstraction shape. `implements Fee` applies exactly where it's true, and cuts across the hierarchy freely because a class can implement many interfaces.

See [[Classes|abstract classes]] for the other half: use an interface for a pure contract, an abstract class when subclasses need to share implementation.

## Encapsulation

Structuring code so a block of code has **specific access points** for external code. The term is **visibility** or **accessibility**: what code in one method, property, or class can call in another.

In TypeScript you enforce it with methods and properties that only allow access to data you control:

```ts
Withdraw(amount: number): boolean
{
    if (this._balance > amount)
    {
        this._balance -= amount
        return true;
    }
    return false;
}
private _balance: number;
get Balance(): number {
    return this._balance;
}
```

`_balance` is `private`. Nothing outside the class can touch it. Two controlled access points exist:

- **`Withdraw`** does the calculation and updates `_balance`, returning `false` rather than allowing an overdraft. The invariant *"balance never goes negative"* is enforced in one place and cannot be bypassed.
- **`Balance`** is a getter with no setter — readable from outside, writable only from inside.

Contrast a `public balance` field: every caller could set it directly, the invariant would have to be re-checked at every one of them, and one missed check is a bug with no single place to fix.

> [!note] Encapsulation is a design property, not a runtime guarantee
> TypeScript's `private` is erased at compile time — `(account as any)._balance = -1` works at runtime. The compiler enforces the *contract* during development, which is where the mistakes you're guarding against actually happen. JavaScript's `#balance` gives true runtime privacy if you need it.

**Course convention**: private property names start with `_`, which is why it's `_balance` and not `balance`. See [[CS4530 Code Style Guide]].

## How They Fit Together

The bank account example runs through all four:

```
BankAccount                        abstraction — the base type
  ├── SavingsAccount               inheritance — extends without Fee
  └── CheckingAccount implements Fee
        └── BusinessChecking       polymorphism — overrides open() with its own rule

private _balance + get Balance()   encapsulation — the invariant lives in one place
```

Inheritance shares code. Polymorphism lets callers ignore which subtype they hold. Abstraction states the contract without the implementation. Encapsulation keeps the invariants enforceable. Each one is a way of limiting how much a change in one place can break somewhere else — which is the actual subject of [[Fundamentals of Software Engineering|CS 4530]].

## Tips
- Prefer composition over inheritance. `extends` is permanent coupling to the parent's internals; a field holding a collaborator can be swapped.
- Override to *extend* (`super.method()`) rather than replace, unless replacement is genuinely the intent.
- If a base-class method makes sense for only some subclasses, it belongs in an interface.
- `protected` over `private` only when a subclass genuinely needs it. Start private.
- Depend on interfaces at module boundaries, never on concrete classes.

## See Also
- [[Classes]] — access modifiers, abstract classes, getters/setters, `super`
- [[Interfaces]] — contracts, `implements`, structural typing
- [[Functions]] — overloads
- [[Module 04 - Design Patterns for Web Applications]] — where these principles become patterns
- [[Tutorial - TypeScript Basics]] · [[CS4530 Code Style Guide]]
