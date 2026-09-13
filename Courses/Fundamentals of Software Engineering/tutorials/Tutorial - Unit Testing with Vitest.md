---
tags:
  - software-engineering
  - northeastern
  - cs4530
  - testing
  - vitest
  - tdd
  - tutorial
type: tutorial
course: "[[Fundamentals of Software Engineering]]"
status: raw
---
# Tutorial — Unit Testing with Vitest

> [!info] Source
> <https://neu-se.github.io/CS4530-Fall-2026/tutorials/week1-unit-testing>
> Run `npm i` on the handouts before running the tests.

**Assigned in**: [[Module 02 - From Requirements to Tests]]
**Needed for**: [[Activity 02 - Test-Driven Development]] · [[Individual Project 1]] (Tasks 2–5)
**Prerequisite**: [[Tutorial - TypeScript Basics]]

## Graded Requirements

> [!important] These four are explicitly used as a grading reference
> - [ ] Tests are **hermetic** — no flakiness from nondeterminism, timing, or resource availability
> - [ ] Tests are **clear** — after a failure it's obvious what went wrong
> - [ ] Tests are **scoped as small as possible**
> - [ ] Tests **call public APIs** — otherwise they're brittle and order-dependent

> [!note] Not graded, but expected
> - [ ] Test expected behavior, not your reading of the implementation
> - [ ] Assertion matches the test description
> - [ ] One thing per spec, preferably one assertion
> - [ ] Organize with suites — a suite per method
> - [ ] Use setup/teardown to cut duplication
> - [ ] Duplication in tests beats clever logic to remove it
> - [ ] Happy path → edge cases → error scenarios
> - [ ] Mock/stub external dependencies, clear mocks after each test
> - [ ] Clean up large test data
> - [ ] Coverage is deceptive — 100% coverage ≠ 100% tested

## Topics to Cover

### Fundamentals
- [ ] What unit testing is and why
- [ ] Black box vs. white box vs. gray box testing

### Vitest Basics
- [ ] Suites — `describe()`, nesting, the recommended hierarchy
- [ ] Specs — `it()` / `test()`
- [ ] File naming — `*.test.ts` vs `*.spec.ts`

### Matchers
- [ ] `.toEqual()` vs `.toBe()` vs `.toStrictEqual()`
- [ ] The common assertion set — `toHaveBeenCalled`, `toHaveBeenCalledWith`, `toBeDefined`, `.not`
- [ ] [Full expect API](https://vitest.dev/api/expect.html)

### Structure
- [ ] AAA — Assemble, Act, Assert (a.k.a. Assemble-Act-Assess in the slides)
- [ ] Setup and teardown — `beforeAll` / `beforeEach` / `afterEach` / `afterAll`
- [ ] When state forces `beforeEach` over `beforeAll`

### Test Doubles ([vi API](https://vitest.dev/api/vi.html))
- [ ] Spy — `vi.spyOn()`; real function still runs
- [ ] Mock — `mockImplementation()`; real function does not run
- [ ] Stub — `mockReturnValue()` / `mockResolvedValue()`

### Async
- [ ] Testing promises
- [ ] **Testing promise rejections** — `await expect(...).rejects.toThrowError()` and the pattern that silently passes
- [ ] Fake timers for fire-and-forget calls
- [ ] Callbacks and the `done` argument

### UI
- [ ] [React Testing Library](https://testing-library.com/docs/react-testing-library/intro/) — `render`, `screen`, `fireEvent`
- [ ] [DOM Testing Library cheatsheet](https://testing-library.com/docs/dom-testing-library/cheatsheet/)

### Tooling
- [ ] [Vitest VS Code extension](https://marketplace.visualstudio.com/items?itemName=vitest.explorer) — install and verify
- [ ] `vitest.config.ts` and package.json scripts
- [ ] Running tests from the Testing view / gutter / Command Palette
- [ ] Debugging tests with breakpoints
- [ ] Coverage reports (`coverage/index.html`)
- [ ] Monorepo workspaces
- [ ] Troubleshooting — tests not appearing, extension not finding Vitest

## Notes

## Questions / Gaps

## Related

- [[Module 02 - From Requirements to Tests]]
- [[Activity 02 - Test-Driven Development]]
- [[Individual Project 1]] — Task 2 needs full branch coverage; Task 3 is TDD against a 100%-covered service that still leaks passwords
- [[Tutorial - TypeScript Basics]]
- [[CS4530 Textbooks and Resources]] — "Effective Software Testing" (Aniche)
