---
type: topic
group: Design
tier: core
confidence:
sections_total: 6
sections_done: 3
coverage: 0.50
status: learning
updated: 2026-09-13
---

# Object-Oriented Design

← [[Career/Prep/topics/Design/Design|Design]]

> [!abstract]- Coverage — 3/6
> - [ ] [[#Idea]]
> - [x] [[#How it works]]
> - [ ] [[#Implementation]]
> - [ ] [[#Complexity]]
> - [x] [[#When to use it]]
> - [x] [[#Gotchas]]

## Idea

Modeling a system as objects with encapsulated state and behavior, related
by inheritance, composition, and well-defined interfaces — [[SOLID]] and
[[Career/Prep/topics/Design/Design Patterns|Design Patterns]] are the vocabulary for talking about whether a
particular design is good.

## How it works

The four pillars with runnable examples in a second language, which is the useful way to see what is a language feature and what is the idea — encapsulation, inheritance, polymorphism, composition, and mixins — [[Code/Ruby/Object Oriented Programming/Object Oriented Programming|Object Oriented Programming]], [[Code/Ruby/Object Oriented Programming/Composition|Composition]], [[Code/Ruby/Object Oriented Programming/Polymorphism|Polymorphism]], [[Code/Ruby/Object Oriented Programming/Modules as Mixins|Modules as Mixins]].

## Implementation

[[Code/OOD/OOD|OOD]] is the coursework hub for this material —
[[Code/OOD/Encapsulation and Invariants|Encapsulation and Invariants]] and
[[Code/OOD/Model, View, and Controller|Model, View, and Controller]] cover
the core ideas, and [[Code/OOD/Examples Index|Examples Index]] links worked
systems (chess pieces, a calculator controller, MVC) that apply them.

## Complexity

## When to use it

Cohesion and coupling as the actual objective — one purpose per component, and swapping a component should not disturb the rest — [[Code/OOD/Model, View, and Controller|Model, View, and Controller]].

## Gotchas

Composition over inheritance, worked as a comparison rather than asserted — [[Code/OOD/Examples/Design Patterns|Design Patterns]] § Code Reuse: Inheritance vs Composition. Class invariants are what encapsulation is *for*; a public setter that can break one is the bug — [[Code/OOD/Encapsulation and Invariants|Encapsulation and Invariants]].

## Resources

- [Object-oriented design (Wikipedia)](https://en.wikipedia.org/wiki/Object-oriented_design)

## Problems

_None yet._
