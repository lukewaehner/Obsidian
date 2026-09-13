---
tags:
  - software-engineering
  - northeastern
  - cs4530
  - ai
  - academic-integrity
  - standards
type: reference
course: "[[Fundamentals of Software Engineering]]"
status: raw
---
# CS4530 AI Policy

> [!info] Source
> <https://neu-se.github.io/CS4530-Fall-2026/policies/ai>
> You said to cut the policies pages — I kept this one because it changes *how you can work* on each deliverable. Delete it if you'd rather not have it.

## Quick Reference

| Where | AI tools |
| --- | --- |
| All written work (reflections, reports, assessments) | **Do not use** |
| [[Individual Project 1]], IP2, and Activities | **Forbidden** |
| IP3 and the [[Team Project Overview\|Team Project]] | **Permitted**, with conditions (policy is a **draft**; staff are soliciting student feedback) |

## Written Work

Written reflections exist so staff understand your thought process and you practice communication — not because they want to read LLM output. Do not use LLM-based tools to generate written assignments.

## IP1, IP2, and Activities — Forbidden

The ban explicitly covers:

- Copilot and any tool suggesting the next line or few lines of code
- Natural-language-to-code tools: ChatGPT, Cursor, AugmentCode, VS Code chat modes, `/` commands in Copilot
- Chat tools that answer questions about your code ("where is the controller for the `/user/` API endpoint")

You **may** use ChatGPT or Claude as a shortcut where you'd otherwise use Google or Stack Overflow, **for learning purposes only**. You may **never** copy-paste code produced by online resources.

## IP3 and the Team Project — Permitted, With Conditions

- **You are responsible for the code you contribute and the code you review.** "I don't know, it's what the AI produced" or "I don't know, the AI said it made sense" doesn't meet the minimum expectations of the course. Repeatedly failing to be accountable for code you wrote or code reviews you signed off on **will result in failing the course**.
- **Each team needs a common AI policy.** It isn't fair for one member to use AI and the others not (or vice versa). Account for members' relative experience with AI coding tools.
- **You will still have to debug your code and tests.** These models are trained mostly on code that works, so they're generally bad at debugging code they've never seen. If you don't understand the code, you can't debug it — and neither can your TA help you. See [[CS4530 Scientific Debugging]].
- **Costs are yours.** Students are encouraged to share information about available student discounts.
- **Do your own reflections, assessments, and reports.** The point is what happens in your brain, not producing text for staff to read.

### Staff Suggestions If You Do Use It

- Don't ask for more than you can review and understand as you go
- **"Vibe" coding — the AI writing large chunks unsupervised — is strongly discouraged**
- Beware being led on wild goose chases when the first or second suggestion doesn't nail it
- Treat it like a very junior but over-eager engineer needing constant supervision and frequent correction
- Use rules files (e.g. `.cursorrules`) to set ground rules. Staff encourage sharing rulesets within your team, with other students, **and with course staff — they want to learn too**

## The Backstop

> **You are responsible for the code you submit. Staff reserve the right to interview you orally** to make sure you understand everything in your submission.

## Related

- [[Individual Project 1]] — Tasks 2 and 5 call out autocomplete specifically
- [[Team Project Overview]]
- [[CS4530 Course Schedule]] — Section 12 has a "Coding with AI" session on 12/02
