---
tags:
  - software-engineering
  - northeastern
  - cs4530
  - debugging
  - process
  - standards
type: reference
course: "[[Fundamentals of Software Engineering]]"
status: raw
---
# CS4530 Scientific Debugging

> [!info] Source
> <https://neu-se.github.io/CS4530-Fall-2026/policies/debugging/>
> Based on Andreas Zeller's [guide to scientific debugging](https://www.debuggingbook.org/html/Intro_Debugging.html#The-Scientific-Method) in *The Debugging Book*.

One objective of [[Fundamentals of Software Engineering]] is writing new code for large existing codebases. Staff expect you to hit debugging difficulty, and they will help — but with the specific goal of teaching you *scientific debugging*, not pointing out bugs they've seen before.

## The Five Questions

> [!important] If you come to staff for debugging help, they will ask you to answer these five
> Keep a **debugging note file** tracking:
>
> 1. What was the input / application state that caused the bug?
> 2. What was the behavior that I expected?
> 3. What was the behavior that I observed?
> 4. What are possible hypotheses for that behavior?
> 5. How have I tested those hypotheses, and what was the result?

## The Method

- If you can't debug an issue in the first few minutes "just by looking at it," you won't be able to hold all the relevant information in your head at once. A formal process for generating and refining guesses about *why* something is wrong becomes immensely useful.
- The goal of hypothesis formulation is to come up with possible causes. As long as hypotheses are **testable**, you can prove or disprove them.
- **Most hypotheses are of the form: "did I make an incorrect assumption about how a library or API works?"** The difficulty is enumerating all the incorrect assumptions you might have made, and testing them.
- Start by testing **high-level, general assumptions**, then refine.

## Hypothesis-Testing Strategies

Students have found it useful to vary the strategy to fit the hypothesis. Staff are happy to demonstrate any of these:

- [ ] Using a debugger
- [ ] Creating a minimized test case
- [ ] Measured application of `console.log`
- [ ] Internet research

## What Staff Will and Won't Do

They **will** discuss the problematic behavior you're observing, possible hypotheses for why it's occurring, and strategies to test those hypotheses. They may **not** be able to stay with you while you refine hypotheses and fix the bug — but they'll follow up if you get stuck again.

## Debugging Log

## Related

- [[Individual Project 1]] — recommendation #4 is explicitly "follow the debugging policy"
- [[Tutorial - Unit Testing with Vitest]] — a minimized failing test *is* a hypothesis test
- [[CS4530 Textbooks and Resources]] — Spinellis, *Effective Debugging: 66 Specific Ways to Debug Software and Systems*
