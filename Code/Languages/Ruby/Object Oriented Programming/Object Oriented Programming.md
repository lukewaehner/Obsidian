---
tags:
  - ruby
  - oop
type: moc
related:
  - '[[Ruby]]'
---
# Object Oriented Programming

Object-oriented programming concepts and patterns in Ruby.

## Overview

Ruby is a purely object-oriented language—everything is an object, including primitives like numbers and booleans. Ruby's OOP model emphasizes flexibility, duck typing, and developer happiness over strict type hierarchies.

## Core Concepts

- [[Inheritance]] — Single inheritance, `super`, method overriding
- [[Modules as Mixins]] — `include`, `extend`, `prepend` for shared behavior
- [[Encapsulation]] — Controlling access with `public`, `private`, `protected`
- [[Polymorphism]] — Duck typing and flexible interfaces

## Class Design

- [[Class Methods and Variables]] — `self`, `@@` vs `@`, singleton methods
- [[Method Visibility]] — Deep dive on access control
- [[Composition]] — Building objects from other objects

## Related Notes

- [[Code/Languages/Ruby/Classes|Classes]] — Class fundamentals and syntax
- [[Modules]] — Module basics and namespacing

## Key Principles

Ruby's OOP philosophy differs from languages like Java or C++:

1. **Duck Typing** — "If it walks like a duck and quacks like a duck, it's a duck." Ruby cares about what an object *can do*, not what it *is*.

2. **Open Classes** — Classes can be reopened and modified at runtime, allowing monkey-patching and extensions.

3. **Single Inheritance + Mixins** — Ruby uses single inheritance but provides modules for sharing behavior across class hierarchies.

4. **Everything is an Object** — Even classes are objects (instances of `Class`), and methods are objects too.

5. **Message Passing** — Calling a method is really "sending a message" to an object, which can be done dynamically with `send`.

## See Also

- [[Ruby]]
