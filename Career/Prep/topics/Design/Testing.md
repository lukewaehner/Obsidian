---
type: topic
group: Design
tier: core
confidence:
sections_total: 6
sections_done: 4
coverage: 0.67
status: learning
updated: 2026-09-13
---

# Testing

← [[Career/Prep/topics/Design/Design|Design]]

> [!abstract]- Coverage — 4/6
> - [ ] [[#Idea]]
> - [x] [[#How it works]]
> - [x] [[#Implementation]]
> - [ ] [[#Complexity]]
> - [x] [[#When to use it]]
> - [x] [[#Gotchas]]

## Idea

Cover: how unit testing works, what mock objects are, what integration
testing is, and what dependency injection buys you (testability — swap a
real dependency for a fake/mock without changing the code under test).

## How it works

Test-first as a graded exercise rather than a slogan — [[Courses/Fundamentals of Software Engineering/topics/Activity 02 - Test-Driven Development|Activity 02 - Test-Driven Development]], [[Courses/Fundamentals of Software Engineering/topics/Module 02 - From Requirements to Tests|Module 02 - From Requirements to Tests]].

## Implementation

Three suites in three languages: Vitest ([[Courses/Fundamentals of Software Engineering/tutorials/Tutorial - Unit Testing with Vitest|Tutorial - Unit Testing with Vitest]]), `#[test]` and `#[cfg(test)]` in Rust ([[Code/Rust/Testing|Testing]]), and RSpec ([[Code/Ruby/Frameworks/Rails/RSpec Setup|RSpec Setup]]).

## Complexity

## When to use it

Designing for testability: a mock controller exists so the model can be tested without a UI, and that requirement is what forces the interface boundary in the first place — [[Code/OOD/Controllers and Mocks|Controllers and Mocks]], [[Code/OOD/Examples/Calculator Controller System|Calculator Controller System]] § How Mocks Are Supported.

## Gotchas

When a test fails, the method is hypothesis-driven, not guess-driven — the five questions and the debugging log — [[Courses/Fundamentals of Software Engineering/reference/CS4530 Scientific Debugging|CS4530 Scientific Debugging]].

## Resources

- [Agile Software Testing with James Bach (video)](https://www.youtube.com/watch?v=SAhJf36_u5U)
- [Open Lecture by James Bach on Software Testing (video)](https://www.youtube.com/watch?v=ILkT_HV9DVU)
- [Steve Freeman - Test-Driven Development (that's not what we meant) (video)](https://vimeo.com/83960706) — [slides](http://gotocon.com/dl/goto-berlin-2013/slides/SteveFreeman_TestDrivenDevelopmentThatsNotWhatWeMeant.pdf)
- [Dependency injection (video)](https://www.youtube.com/watch?v=IKD2-MAkXyQ)
- [Tao Of Testing](http://jasonpolites.github.io/tao-of-testing/ch3-1.1.html)
- [How to write tests](http://jasonpolites.github.io/tao-of-testing/ch4-1.1.html)

## Problems

_None yet._
