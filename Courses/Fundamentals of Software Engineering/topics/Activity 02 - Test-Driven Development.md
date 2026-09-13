---
tags:
  - software-engineering
  - northeastern
  - cs4530
  - testing
  - tdd
  - vitest
  - activity
type: activity
course: "[[Fundamentals of Software Engineering]]"
module: 2
status: raw
---
# Activity 02 — Test-Driven Development

In-class activity for [[Module 02 - From Requirements to Tests]]. Requires a working dev environment — see [[Tutorial - Development Environment Setup]].

## Setup

1. Clone [`transcript-service-m02`](https://github.com/neu-se/transcript-service-m02).
2. Run `npm install` in the created directory.
3. Every member of the group should be able to run each of these and see the stated result:

   | Command | Expected |
   | --- | --- |
   | `npx vitest --run src/types.spec.ts` | 1 failing, 1 passing |
   | `npx vitest --run src/transcript.service.spec.ts` | 5 passing |
   | `npm run test` | 6 passing, 1 failing (all files at once) |

4. Every member should be able to see the **ESLint error** in `src/transcript.service.ts`. Discuss how to fix it.

## The Work

Working in `src/transcript.service.spec.ts`:

1. Write down **two testable behaviors** for `addGrade` corresponding to the condition of satisfaction *"the user can add a new grade for an existing student."* Write them as empty specs:

   ```ts
   it("<testable behavior>", () => {})
   ```

2. Come up with **at least two ways** `addGrade` is *not completely specified* by the conditions of satisfaction given in lecture. Document these in the same `it(...)` format.

3. Add real Vitest assertions to your testable behaviors. There should be **at least four new tests** for `addGrade` by this point.

> [!note] These tests are supposed to fail
> `addGrade` is not implemented. You are **not** required to implement or submit `addGrade` — the point of the exercise is the tests.

Submit the modified `src/transcript.service.spec.ts` as directed by your instructor.

## Grading — Specification Grading

Only two non-zero grades:

| Grade | Points | Requirement |
| --- | --- | --- |
| **Satisfactory** | 10 | Deliver everything listed in the instructions |
| **Minimal** | 5 | At least two meaningful tests for `addGrade` |

Grading is manual — TAs will read your solution and may or may not run it.

## Related

- [[Module 02 - From Requirements to Tests]]
- [[Tutorial - Unit Testing with Vitest]]
- [[CS4530 Code Style Guide]]
