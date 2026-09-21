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
status: notes
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
- [x] What unit testing is and why ✅ 2026-09-16
- [x] Black box vs. white box vs. gray box testing ✅ 2026-09-16

### Vitest Basics
- [x] Suites — `describe()`, nesting, the recommended hierarchy ✅ 2026-09-16
- [x] Specs — `it()` / `test()` ✅ 2026-09-16
- [x] File naming — `*.test.ts` vs `*.spec.ts` ✅ 2026-09-16

### Matchers
- [x] `.toEqual()` vs `.toBe()` vs `.toStrictEqual()` ✅ 2026-09-16
- [x] The common assertion set — `toHaveBeenCalled`, `toHaveBeenCalledWith`, `toBeDefined`, `.not` ✅ 2026-09-16
- [x] [Full expect API](https://vitest.dev/api/expect.html) ✅ 2026-09-16

### Structure
- [x] AAA — Assemble, Act, Assert (a.k.a. Assemble-Act-Assess in the slides) ✅ 2026-09-16
- [x] Setup and teardown — `beforeAll` / `beforeEach` / `afterEach` / `afterAll` ✅ 2026-09-16
- [x] When state forces `beforeEach` over `beforeAll` ✅ 2026-09-16

### Test Doubles ([vi API](https://vitest.dev/api/vi.html))
- [x] Spy — `vi.spyOn()`; real function still runs ✅ 2026-09-16
- [x] Mock — `mockImplementation()`; real function does not run ✅ 2026-09-16
- [x] Stub — `mockReturnValue()` / `mockResolvedValue()` ✅ 2026-09-16

### Async
- [x] Testing promises ✅ 2026-09-17
- [x] **Testing promise rejections** — `await expect(...).rejects.toThrowError()` and the pattern that silently passes ✅ 2026-09-17
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

### What a unit test is

An automated test that checks a portion of the application matches its design and behaves as expected.

| Approach | Knowledge of the implementation | Why you'd pick it |
| --- | --- | --- |
| **Black box** | none — validate input → output only | tests survive refactors; this is the default |
| **White box** | full — exercise internal code paths | uncovers unidentified behavior |
| **Gray box** | partial | lowers the tester's reliance on a developer for every minor issue |

> [!important] The graded requirement pulls toward black box
> "Tests call public APIs" is the same rule stated from the other side — reach into internals and the tests become brittle and order-dependent.

### Suites — `describe()`

The unit under test, `src/services/math/calculator.ts`:

```typescript
export default class Calculator {
	public add(num1: number, num2: number): number {
		const result: number = num1 + num2;
		console.log("The result is: ", result);
		return result;
	}
}
```

Alongside it we put `calculator.test.ts`.

Every test file starts with a suite — a logical grouping of tests. `describe()` takes two arguments: a description, and a callback.

```typescript
describe("Description of suite", () => {
	// Tests go here
});
```

A suite breaks down further into **setup**, **teardown**, and **tests**.

Suites make debugging easier once you have a large number of tests. The recommended hierarchy:

1. Top level — the file path after `src`
2. Second `describe` — the class/file being tested
3. Subsequent `describe` blocks — the functions being tested

```typescript
describe("services > math", () => {
	describe("Calculator", () => {
		describe("add()", () => {
			// Tests for add go here
		});
	});
});
```

### Specs — `it()` / `test()`

A spec is the actual test: it executes some code and asserts a result. Like `describe`, `it()` takes a description and a callback.

```typescript
it("should check a specific behavior", () => {});
```

Describe what the code *should do* in the description, then assert exactly that behavior in the body — using the AAA pattern (Assemble, Act, Assert).

```typescript
describe("services > math", () => {
	describe("Calculator", () => {
		describe("add()", () => {
			it("should return 2 when inputs are 1 and 1", () => {
				const calculator: Calculator = new Calculator();

				const result: number = calculator.add(1, 1);

				expect(result).toEqual(2);
			});
		});
	});
});
```

### Matchers — `.toEqual()` vs `.toBe()` vs `.toStrictEqual()`

All three test equality, with slight but important differences. The unit under test for all three:

```typescript
export default class Store {
	private static _data: any = null;

	public static getData(): any {
		return Store._data;
	}

	public static setData(data: any): void {
		Store._data = data;
	}
}
```

**`.toEqual()`** — compares all properties of object instances, recursively.

```typescript
import { describe, it, expect, beforeEach } from 'vitest';

describe("utils > store", () => {
	describe("Store", () => {
		beforeEach(() => {
			Store["_data"] = undefined;
		});

		describe("setData()", () => {
			it("should assign the input data to Store._data", () => {
				const mockData = { key: "value" };

				Store.setData(mockData);

				expect(Store["_data"]).toEqual(mockData);
			});
		});

		describe("getData()", () => {
			it("should return an object equal to Store._data", () => {
				const mockData = { key: "value" };
				Store["_data"] = mockData;

				const returnedValue = Store.getData();

				expect(returnedValue).toEqual(mockData);
			});
		});
	});
});
```

**`.toBe()`** — compares primitive values, or checks referential identity of object instances.

```typescript
describe("getData()", () => {
	it("should return an object with the same reference as Store._data", () => {
		const mockData = { key: "value" };
		Store["_data"] = mockData;

		const returnedValue = Store.getData();

		expect(returnedValue).toEqual(mockData);
		expect(returnedValue).toBe(mockData); // Same reference
		expect(Store["_data"]).toBe(mockData);
	});
});
```

**`.toStrictEqual()`** — tests that objects have the same types as well as the same structure.

```typescript
it("should return an object strictly equal to the object stored in Store._data", () => {
	const mockData = { key: "value" };
	const mockDataWithUndefined = { key: "value", key2: undefined };
	Store["_data"] = mockData;

	const returnedValue = Store.getData();

	expect(returnedValue).toStrictEqual(mockData);
	expect(returnedValue).toEqual(mockDataWithUndefined);
	expect(returnedValue).not.toStrictEqual(mockDataWithUndefined);
});
```

The middle assertion is the point: `.toEqual()` ignores an explicitly-`undefined` property, `.toStrictEqual()` does not.

### The common assertion set

| Assertion | Meaning |
| --- | --- |
| `expect(actual).toEqual(expected)` | Expects both entities to have the same value |
| `expect(actual).toBe(expected)` | Expects both entities to be the same |
| `expect(spy/stub/mock).toHaveBeenCalled()` | Expects a function being spied/stubbed/mocked to be invoked |
| `expect(spy/stub/mock).toHaveBeenCalledWith([arguments])` | Expects a function being spied/stubbed/mocked to be invoked with specified arguments |
| `expect(actual).toBeDefined()` | Expects the entity to be defined |
| `expect(actual).not.` | Negates the assertion |
| `await expect(promise-returning code that errors).rejects.toThrowError()` | Waits for the error-throwing code that returns a promise (API call) to throw, and asserts the error was thrown |

Full list: [expect API](https://vitest.dev/api/expect.html).

### Setup and teardown

Two setup methods and two teardown methods:

| Method         | Purpose                                   |
| -------------- | ----------------------------------------- |
| `beforeAll()`  | Runs once before all the tests in a suite |
| `beforeEach()` | Runs before every test in a suite         |
| `afterEach()`  | Runs after every test in a suite          |
| `afterAll()`   | Runs once after all the tests in a suite  |

Use `beforeEach()` / `afterEach()` when the function or class **stores state** and each test needs a clean instance.

### Test doubles ([vi API](https://vitest.dev/api/vi.html))

Needed once the function under test has dependencies — other functions, network requests, database connections, or built-ins.

#### Spy — the real function still runs

A watcher on a function that tracks how it was used:

- whether it was invoked
- how many times
- what arguments it was invoked with

```typescript
const spy = vi.spyOn(object, 'methodName');
```

```typescript
it("invokes console.log() with the result 2 when adding 1 and 1", () => {
	const logSpy = vi.spyOn(console, "log");

	const result: number = calculator.add(1, 1);

	expect(logSpy).toHaveBeenCalledWith("The result is: ", result);

	logSpy.mockRestore();
});
```

#### Mock — replaces the function body

```typescript
spy.mockImplementation(() => {
	// New function body here
});
```

```typescript
it("should invoke console.log", () => {
	const logSpy = vi.spyOn(console, "log");
	logSpy.mockImplementation(() => {
		// No longer prints to console
	});

	const result: number = calculator.add(1, 1);

	expect(logSpy).toHaveBeenCalledWith("The result is: ", result);

	logSpy.mockRestore();
});
```

#### Stub — returns a value you specify

A special kind of mock that needs no alternate implementation, just a return value.

```typescript
spy.mockReturnValue(someValue);
```

To return a promise:

```typescript
spy.mockResolvedValue(someValue);
```

Especially handy for stubbing Axios requests.

```typescript
it("should invoke console.log", () => {
	const logSpy = vi.spyOn(console, "log");
	logSpy.mockReturnValue();

	const result: number = calculator.add(1, 1);

	expect(logSpy).toHaveBeenCalledWith("The result is: ", result);

	logSpy.mockRestore();
});
```

### Testing asynchronous code

#### Promises

```typescript
import axios from "axios";
import Store from "../../utils/store/store";

export default class HttpService {
	public getData(): Promise<any> {
		return axios.get("/myUrl");
	}
}
```

```typescript
import { describe, it, expect, vi } from 'vitest';

describe("getData()", () => {
	it('should invoke axios.get() with "/myUrl"', async () => {
		const getStub = vi
			.spyOn(axios, "get")
			.mockResolvedValue({ status: 200, data: {} });

		await httpService.getData();

		expect(getStub).toHaveBeenCalledWith("/myUrl");

		getStub.mockRestore();
	});

	it("should return the status as 200", async () => {
		const getStub = vi
			.spyOn(axios, "get")
			.mockResolvedValue({ status: 200, data: {} });

		const response = await httpService.getData();

		expect(response.status).toEqual(200);

		getStub.mockRestore();
	});
});
```

The spec callback is `async` and the call is `await`ed — otherwise the assertion runs before the promise settles.

#### Promise rejections

For async functions expected to throw or reject, use `await expect(...).rejects.toThrowError()`.

An auth function that validates users:

```typescript
export async function enforceAuth(credentials: { username: string; password: string }): Promise<{ _id: string; username: string }> {
	const user = await validateCredentials(credentials);
	if (!user) {
		throw new Error('Invalid credentials');
	}
	return { _id: user.id, username: credentials.username };
}
```

```typescript
import { describe, it, expect } from 'vitest';
import { enforceAuth } from '../../src/services/auth.service';

describe('enforceAuth', () => {
	it('should return a user and id on good auth', async () => {
		const user = await enforceAuth({ username: 'user1', password: 'pwd1111' });

		expect(user).toStrictEqual({ _id: expect.any(String), username: 'user1' });
	});

	it('should raise on bad auth', async () => {
		await expect(enforceAuth({ username: 'user1', password: 'no' })).rejects.toThrowError();
	});
});
```

> [!warning] The pattern that silently passes
> Drop the `await` in front of `expect(...)` and the assertion becomes a floating promise — the spec finishes and reports green whether or not the error was ever thrown.

### UI testing

*Not yet covered — see the unchecked items under [[#Topics to Cover]].*

## Questions / Gaps

## Related

- [[Module 02 - From Requirements to Tests]]
- [[Activity 02 - Test-Driven Development]]
- [[Individual Project 1]] — Task 2 needs full branch coverage; Task 3 is TDD against a 100%-covered service that still leaks passwords
- [[Tutorial - TypeScript Basics]]
- [[CS4530 Textbooks and Resources]] — "Effective Software Testing" (Aniche)
