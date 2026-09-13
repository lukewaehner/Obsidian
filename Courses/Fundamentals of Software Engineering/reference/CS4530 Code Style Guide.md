---
tags:
  - software-engineering
  - northeastern
  - cs4530
  - typescript
  - code-style
  - eslint
  - standards
type: reference
course: "[[Fundamentals of Software Engineering]]"
status: raw
---
# CS4530 Code Style Guide

> [!info] Source
> <https://neu-se.github.io/CS4530-Fall-2026/policies/style/>

All code written for [[Fundamentals of Software Engineering]] is checked by [ESLint](https://eslint.org) and **must be free of style warnings and errors**. Manually graded in [[Individual Project 1]] Tasks 1 and 5.

The rules derive from [Airbnb's JavaScript Style Guide](https://github.com/airbnb/javascript), [ESLint Recommended](https://eslint.org/docs/rules/), [TypeScript/ESLint Recommended](https://www.npmjs.com/package/@typescript-eslint/eslint-plugin), [React ESLint](https://www.npmjs.com/package/eslint-plugin-react), and [React Hooks ESLint](https://www.npmjs.com/package/eslint-plugin-react-hooks). The course advises **not** studying those lists directly — write naturally and let the IDE's checker report issues as you go.

## The Rules

### Formatting
- [ ] Indent with **spaces, not tabs** — 2 spaces per level
- [ ] String literals in **single quotes**, not double
- [ ] Maximum line length **100 characters**

### Naming (mechanical — the linter catches these)
- [ ] Variables → `lowerCamelCase`
- [ ] Types → `UpperCamelCase`
- [ ] Constants (read-only, assigned once, not reused) → `UPPER_CASE_WITH_UNDERSCORES`
- [ ] Private property names must start with `_`

### Naming (judgment — the linter can't catch these)
- [ ] Names are informative: `lineTooLong()` over `checkLineLength()`
- [ ] Type names are nouns or noun phrases. Interface names may be adjectives (`Serializable`). Class names may be noun phrases including the interface name (`CuckooClock`, `DigitalClock` for `Clock`)
- [ ] **Noun-like names for functions that return values** — `circleDiameter` over `calculateDiameter`. Exception: simple getters can start with `get`
- [ ] **Verb-like names reserved for functions that perform actions** — `addItem`
- [ ] Adjective phrases for predicates where possible — `line.tooLong()`
- [ ] Variable and property names describe what the variable is *for*, not its type (the type declaration already captures that)

### Documentation
- [ ] All public properties and methods — **except getters, setters, and constructors** — must have [JSDoc-style comments](https://devdocs.io/jsdoc/about-getting-started) describing what they do

  ```
  /** The unique identifier for this player * */
  private readonly _id: string;
  ```

  ```
  /**
   * A handler to process a remote player's subscription to updates for a room
   *
   * @param socket the Socket object that we will use to communicate with the player
   */
  ```

- [ ] Comment non-obvious behavior, or capture **why** the code is written the way it is
- [ ] Do **not** add comments that restate what the code already says

  Useful:
  ```
  // No valid session exists for this token, hence this client's connection should be terminated
  socket.disconnect(true);
  ```
  Useless:
  ```
  // Disconnect the socket
  socket.disconnect(true);
  ```

- [ ] **Do not submit commented-out code.** Comments are documentation, not a place to park old code

## Why the Rules Are Arbitrary (And Still Binding)

Many guidelines are genuinely arbitrary — single vs. double quotes, spaces vs. tabs, `new Array()` vs. `[]`. Sometimes the only difference is how it reads; other times there are unintended consequences to the seemingly-correct-but-subtly-wrong choice. The point is that organizations require a consistent style so programs are easier to read, and that automated checkers make this cheap to enforce.

## Where This Is Graded

| Where | Stakes |
| --- | --- |
| [[Individual Project 1]] CI | Up to **25%** deduction — 5% prettier, 10% TypeScript, 10% ESLint |
| [[Individual Project 1]] Task 1 | 10 pts manual TA review for code style |
| [[Individual Project 1]] Task 5 | 4 pts for correct style and documentation |
| Any IP1 submission | `eslint-disable` comments are **not allowed** |

## Related

- [[Tutorial - TypeScript Basics]]
- [[Tutorial - Development Environment Setup]] — install the ESLint and Prettier extensions *before* writing code
- [[Individual Project 1]]
- [[CS4530 Textbooks and Resources]] — Fowler's *Refactoring*, plus the readability research papers
