---
type: topic
group: Design
tier: core
confidence:
sections_total: 6
sections_done: 0
coverage: 0.00
status: untouched
updated: 2026-09-01
---

# SOLID

> [!abstract]- Coverage — 0/6
> - [ ] [[#Idea]]
> - [ ] [[#How it works]]
> - [ ] [[#Implementation]]
> - [ ] [[#Complexity]]
> - [ ] [[#When to use it]]
> - [ ] [[#Gotchas]]

## Idea

Five principles for object-oriented design that keep a codebase extensible
without becoming fragile:

- **S**ingle Responsibility — a class should have one reason to change.
- **O**pen/Closed — open for extension, closed for modification.
- **L**iskov Substitution — a subtype must be usable anywhere its base type
  is expected, without breaking correctness.
- **I**nterface Segregation — don't force a client to depend on methods it
  doesn't use.
- **D**ependency Inversion — depend on abstractions, not concrete
  implementations.

## How it works

## Implementation

[[Code/OOD/OOD|OOD]] covers SOLID alongside worked examples —
[[Object-Oriented Design]].

## Complexity

## When to use it

## Gotchas

SOLID is a set of tradeoffs, not free — applying every principle
maximally (e.g. an interface for every class "just in case") produces the
overengineering these principles are supposed to prevent in the other
direction.

## Resources

- [Bob Martin - SOLID Principles of Object Oriented and Agile Design (video)](https://www.youtube.com/watch?v=TMuno5RZNeE)
- [Single Responsibility Principle](http://www.oodesign.com/single-responsibility-principle.html)
- [Single responsibility to each Object](http://www.javacodegeeks.com/2011/11/solid-single-responsibility-principle.html)
- [Single Responsibility, more flavor](https://docs.google.com/open?id=0ByOwmqah_nuGNHEtcU5OekdDMkk)
- [Open/Closed Principle](http://www.oodesign.com/open-close-principle.html)
- [Open/closed principle (Wikipedia)](https://en.wikipedia.org/wiki/Open/closed_principle)
- [Open/Closed, more flavor](http://docs.google.com/a/cleancoder.com/viewer?a=v&pid=explorer&chrome=true&srcid=0BwhCYaYDn8EgN2M5MTkwM2EtNWFkZC00ZTI3LWFjZTUtNTFhZGZiYmUzODc1&hl=en)
- [Liskov Substitution Principle](http://www.oodesign.com/liskov-s-substitution-principle.html)
- [What is the Liskov Substitution Principle? (Stack Overflow)](http://stackoverflow.com/questions/56860/what-is-the-liskov-substitution-principle)
- [Liskov Substitution, more flavor](http://docs.google.com/a/cleancoder.com/viewer?a=v&pid=explorer&chrome=true&srcid=0BwhCYaYDn8EgNzAzZjA5ZmItNjU3NS00MzQ5LTkwYjMtMDJhNDU5ZTM0MTlh&hl=en)
- [Interface Segregation Principle](http://www.oodesign.com/interface-segregation-principle.html)
- [Interface Segregation Principle in 5 minutes (video)](https://www.youtube.com/watch?v=3CtAfl7aXAQ)
- [Interface Segregation, more flavor](http://docs.google.com/a/cleancoder.com/viewer?a=v&pid=explorer&chrome=true&srcid=0BwhCYaYDn8EgOTViYjJhYzMtMzYxMC00MzFjLWJjMzYtOGJiMDc5N2JkYmJi&hl=en)
- [Dependency Inversion Principle](http://www.oodesign.com/dependency-inversion-principle.html)
- [What Is The Dependency Inversion Principle And Why Is It Important (Stack Overflow)](http://stackoverflow.com/questions/62539/what-is-the-dependency-inversion-principle-and-why-is-it-important)
- [Dependency Inversion, more flavor](http://docs.google.com/a/cleancoder.com/viewer?a=v&pid=explorer&chrome=true&srcid=0BwhCYaYDn8EgMjdlMWIzNGUtZTQ0NC00ZjQ5LTkwYzQtZjRhMDRlNTQ3ZGMz&hl=en)

## Problems

_None yet._
