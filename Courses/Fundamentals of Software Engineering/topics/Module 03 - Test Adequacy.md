---
tags:
  - software-engineering
  - northeastern
  - cs4530
  - testing
  - test-adequacy
  - coverage
  - mutation-testing
  - module
type: lecture
course: "[[Fundamentals of Software Engineering]]"
module: 3
status: notes
---
# Module 03 — Test Adequacy

**Week 3** of [[Fundamentals of Software Engineering]]
**Slides**: `Module 03 Unit Testing` (pdf / pptx)

## Learning Objectives

After this lecture you should be able to:

- [ ] Explain three general ways of judging whether we've written enough tests
- [ ] Explain how contracts provide better guidance than types in choosing test cases
- [ ] Explain various measures of code coverage — statements, branches, functions, and lines
- [ ] Explain how adversarial testing helps gauge whether our tests are sensitive enough to detect likely bugs

## Notes

> [!abstract] The question this module answers
> [[Module 02 - From Requirements to Tests]] showed how to turn a requirement into a test. It left
> a hole: you can always write *one more* test, so when do you stop? This module gives three
> independent answers, and they're independent on purpose — each one catches gaps the others miss.
>
> | Lens | Asks | Derived from |
> | --- | --- | --- |
> | **Contracts** | Have I tested everything the spec obliges me to handle? | The docstring |
> | **Coverage** | Have I exercised every part of the code? | The implementation |
> | **Adversarial testing** | Would my tests actually *notice* a bug? | Deliberately broken code |

### Vocabulary first

Two axes that get conflated. **Scope**:

| Kind | Tests |
| --- | --- |
| **Unit test** | A single function in isolation |
| **Integration test** | How parts of a program work together — where we check that other functions respect our function's contracts |

And **purpose** — the same test can serve any of these:

| Kind | The question it answers |
| --- | --- |
| **Test-driven development** | If we start from tests, passing tests tell us we've met the conditions of satisfaction |
| **Acceptance testing** | Does the *customer* agree we've met the conditions of satisfaction? |
| **Regression testing** | Did something break relative to a previous version? |

Regression testing is the one that pays off over time: it stops bugs from **re-entering** during
maintenance. A good suite catches faults introduced months after the code was written, by someone
who never read it.

### Lens 1 — Contracts

A **contract** is a promise spelled out in the docstring: what the caller must guarantee going in,
and what the function guarantees in return. It's strictly more informative than the type
signature, because types can only express *shape*, never *validity*.

```ts
/**
 * Adds a message to a chat, updating the chat
 *
 * @param chatId - Ostensible chat id
 * @param user - Authenticated user
 * @param messageId - Valid message id
 * @returns the updated chat info object
 * @throws if the chat id is not valid
 */
export function addMessageToChat(
  chatId: string,
  user: UserWithId,
  messageId: string
): ChatInfo { ... }
```

All three parameters are `string` or near enough — the types tell you nothing about which ones you
can trust. The **adjectives** do all the work.

#### Parts of the contract

> [!info] Preconditions (the caller's job)
> - `messageId` is a **valid** message id
> - `user` is an **authenticated** user
>
> The function may **assume** these and doesn't need to check them. If a caller violates them, that's the caller's bug, and behavior is **undefined** (it could crash, corrupt data, or appear to work).

> [!warning] No precondition, so the function must check
> `chatId` is only an **ostensible** chat id: it looks like one but may not be real. The caller isn't promising validity, so the **function must validate it**.

> [!success] Postconditions (the function's job)
> - Valid inputs → returns the updated `ChatInfo`
> - Invalid `chatId` → **throws** (per `@throws`)

#### How contracts determine test cases

| Test case                                                 | Write it? | Why                                                |
| --------------------------------------------------------- | --------- | -------------------------------------------------- |
| Valid `chatId` → returned `ChatInfo` includes the message |  Yes      | Core postcondition                                 |
| Invalid `chatId` → throws                                 | Yes       | Specified by `@throws`, so it's required behavior  |
| Invalid `messageId`                                       | No        | Precondition violation; no defined result to check |
| Unauthenticated `user`                                    | No        | Precondition violation; no defined result to check |

> [!tip] The rule
> **Don't test precondition violations.** Not because they can't happen, but because the contract
> defines no correct answer — so there's nothing to assert. Any test you write there is really
> asserting an implementation detail, and it will break the moment someone changes it.
>
> This is also the answer to [[Module 02 - From Requirements to Tests]]'s open questions
> (*"what to do about errors??"*). Decide, write it in the docstring, and the test case falls out.

#### Contracts also pick your values

```ts
/** Returns number of repeated 'hi's'
* @params n - the number of hi's to return, must be an integer >= 0
*/
function helloNTimes(n: number): string[] {
	const arr: string[] = [];
	for(let i = n; i != 0; i--) {
	arr.push("hi")
	} 
	return arr;
}
```

The precondition *an integer at least 0* hands you the test set directly: **0** (the boundary), a
typical integer, and the **maximum integer** (the other boundary). No inspection of the body
required.

#### Where preconditions stop being safe

The contract says `n` must be a non-negative integer, and TypeScript's `number` doesn't enforce
"integer" or "non-negative". Worse, the type can be lied about outright:

```ts
helloNTimes({ lol: 'owned' } as unknown as number)

```

**Untrusted inputs** are those arriving from web sites or typed in by users — anything crossing
your system's boundary. Preconditions are a promise between *your* functions; an external caller
never agreed to them.

> [!danger] Rule for the boundary
> Receive untrusted input as `unknown`, then **type-check it at the boundary** before any method is
> called on it. Inside the boundary you may assume preconditions; outside it you may assume
> nothing.

### Lens 2 — Code coverage

Code coverage is the industry standard measure of how much of the code a suite actually executes.
Work through one function at all three strengths:

```ts
export function f(x: number) {      // 1
  if (x === 0) {                    // 2
    return 3;                       // 3
  }                                 // 4
  const y = x > 4 ? 2 : 3;          // 5
  const z = x % 2 === 0 ? 1 : 2;    // 6
  return x / (y - z);               // 7
}                                   // 8
```

#### Line coverage — is every line run at least once?

Two inputs suffice:

| Input | Lines reached |
| --- | --- |
| x = 0 | 2, 3 |
| x = 10 | 2, 5, 6, 7 |

100% line coverage from two test cases — which should tell you how weak a signal it is.

#### Branch coverage — is every decision taken both ways?

> [!success] The gold standard
> Branch coverage is the measure worth targeting in practice. There are three decisions here, two
> of them hidden inside ternaries rather than `if` statements.

| Decision | Needs |
| --- | --- |
| line 2 — x is zero | one zero and one non-zero input |
| line 5 — x greater than 4 | one input above 4 and one at or below |
| line 6 — x is even | one even and one odd input |

The set **{ -2, 0, 1, 10 }** gets full branch coverage:

| Input | x is zero | x > 4 | x is even |
| --- | --- | --- | --- |
| 0 | yes | — | — |
| 10 | no | yes | yes |
| 1 | no | no | no |
| -2 | no | no | yes |

#### Path coverage — is every *combination* of branches run?

Infeasible in general (the paths multiply), but instructive here — after the zero check there are
2 × 2 = 4 combinations, and the branch-covering set above only reaches three of them:

| Path | x > 4 | x is even | y - z | Returns | Covered by |
| --- | --- | --- | --- | --- | --- |
| 1 | — | — | — | 3 | x = 0 |
| 2 | yes | yes | 2 - 1 = 1 | x / 1 | x = 10 |
| 3 | yes | no | 2 - 2 = 0 | **x / 0** | **nothing** |
| 4 | no | yes | 3 - 1 = 2 | x / 2 | x = -2 |
| 5 | no | no | 3 - 2 = 1 | x / 1 | x = 1 |

> [!warning] The missing path is the interesting one
> x = 5 is above 4 **and** odd, so y - z is 0 and the function divides by zero. In
> JavaScript that doesn't throw — it evaluates to `Infinity`. So the bug is silent: full branch
> coverage, no error, wrong answer.
>
> This is the case *against* treating any coverage number as a stopping rule. Coverage tells you
> what you definitely haven't tested; it never tells you you're done.

#### Two things coverage doesn't measure

**Edge cases.** Always reason about them explicitly — empty collections, zero, negatives, maximum
values, duplicates. Coverage tooling won't prompt you.

**Test isolation.** A test exercises everything its subject transitively calls, not just the
function you named. Two consequences:

- When a test fails, the fault may be anywhere in the code the test executed — not necessarily in
  the function under test.
- A "unit" test of a function that calls three others is really testing all four, so its coverage
  numbers and its failures both over-attribute.

Isolating the subject with test doubles is the fix — see
[[Tutorial - Unit Testing with Vitest]].

### Lens 3 — Adversarial testing

The first two lenses examine your code. This one examines **your tests**: would they actually
notice if the code were wrong?

The method is to run the suite against multiple **mutated** versions of the code:

- Some mutations change behavior in ways that are genuinely **acceptable** — your suite should
  still pass.
- Some mutations introduce real **bugs** — your suite must fail.
- **You decide** which mutants are buggy. That judgement is yours, not the tool's.

> [!note] The pass condition
> Catch **every** bugged mutant, and pass **every** acceptable version. A suite that misses a
> bugged mutant has a blind spot the mutant just located for you. A suite that fails an acceptable
> mutant is over-fitted to the implementation.

**Stryker** automates this: it generates the mutations, runs the suite against each, and reports
which mutants **survived** — i.e. which bugs your tests failed to detect. A surviving mutant is a
much more actionable finding than an uncovered line, because it names a specific wrong behavior
nobody would have caught. Hands-on in [[Activity 03 - Mutation Testing with Stryker]].

## Key Takeaways

- Three independent stopping rules, and you need all three: **contracts** (what the spec obliges),
  **coverage** (what the code contains), **mutation testing** (whether the tests are sensitive).
- Contracts beat types for choosing test cases, because types express shape and contracts express
  **validity**. The adjectives in the docstring — *valid*, *authenticated*, *ostensible* — are the
  specification.
- **Preconditions are the caller's job and must not be tested** — behavior is undefined, so there's
  no correct answer to assert. Parameters with *no* precondition must be validated by the function,
  and that validation *does* get tested.
- Preconditions only hold inside your system. Take **untrusted input as `unknown`** and type-check
  it at the boundary; `as unknown as T` shows the type system is no defense.
- **Branch coverage is the practical target.** Line coverage is trivially gamed (two inputs hit
  every line of `f`); path coverage is infeasible.
- Coverage is a **lower bound on your ignorance, not a definition of done**: {-2, 0, 1, 10} gives
  full branch coverage of `f` and still misses x = 5 dividing by zero — silently, as `Infinity`.
- A test exercises everything its subject calls, so failures don't localise on their own. Isolate
  with test doubles.
- **Mutation testing inverts the question** from "did my tests run this code" to "would my tests
  notice if this code were wrong." Surviving mutants are the actionable output.

## Questions / Gaps

- The learning objectives list **statements, branches, functions, and lines** as coverage measures.
  Lecture notes cover lines, branches, and paths — **statement** and **function** coverage weren't
  worked through. How do statement and line coverage differ in practice (multiple statements on one
  line, one statement spanning lines)?
- Does Stryker's default mutant set map onto the "acceptable vs. buggy" distinction, or does it
  report every survivor and leave the judgement entirely to you? Resolve during
  [[Activity 03 - Mutation Testing with Stryker]].
- What coverage threshold, if any, does the team project's CI enforce? See [[Team Project Overview]].

## Activity

[[Activity 03 - Mutation Testing with Stryker]]

## Slides

| Deck | PDF | PPT |
| --- | --- | --- |
| Module 03 — Unit Testing | [PDF](https://neu-se.github.io/CS4530-Fall-2026/Slides/Module%2003%20Unit%20Testing.pdf) | [PPT](https://neu-se.github.io/CS4530-Fall-2026/Slides/Module%2003%20Unit%20Testing.pptx) |

Additional content: [modules/3-test-adequacy](https://neu-se.github.io/CS4530-Fall-2026/modules/3-test-adequacy)

## Resources

- [Go Testing By Example — Rob Pike](https://research.swtch.com/testing)
- [*Software Engineering at Google*, ch. 11 "Testing"](https://learning.oreilly.com/library/view/software-engineering-at/9781492082781/ch11.html)
- [StrykerJS — mutation testing tool](https://stryker-mutator.io)
- [Are mutants a valid substitute for real faults in software testing?](https://homes.cs.washington.edu/~mernst/pubs/mutation-effectiveness-fse2014-abstract.html)

## Related

- [[Module 02 - From Requirements to Tests]] — how to write the tests this module counts
- [[Module 04 - Design Patterns for Web Applications]]
- [[Tutorial - Unit Testing with Vitest]] — matchers, fixtures, and test doubles
- [[CS4530 Course Schedule]]
