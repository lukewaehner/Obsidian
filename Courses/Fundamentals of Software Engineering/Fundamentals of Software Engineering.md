---
tags:
  - software-engineering
  - northeastern
  - cs4530
  - typescript
  - hub
type: moc
semester_start: 2026-09-07
---
# Fundamentals of Software Engineering

**CS 4530 — Fundamentals of Software Engineering** · Fall 2026 · Northeastern (Khoury)

**Course Focus**: The tools and processes used to design, construct, and maintain programs over time — "the multi-person development of multi-version programs." Development processes that work for one developer building a one-off program break down on a codebase maintained by a team over years. The course walks the full software lifecycle with a bias toward how each decision affects resulting *quality*.

> [!info] Source
> Mirrored from <https://neu-se.github.io/CS4530-Fall-2026/> as of 2026-09-09. The site is early-semester: only Modules 1–2, Week 1 tutorials, and IP1 are published so far.

## Logistics

| Section | Instructor | Meeting Time | Location |
| --- | --- | --- | --- |
| 1 | Prof Adeel Bhutta | Mon & Thu, 11:45am–1:25pm | West Village G 104 |
| 2 | Prof Adeel Bhutta | Tue & Fri, 9:50am–11:30am | Dodge Hall 050 |
| 5 | Prof Adeel Bhutta | Tue 11:45am–1:25pm & Thu 2:50pm–4:30pm | West Village G 104 |
| 12 | Prof Mitch Wand | Wed, 6:00pm–9:20pm | Online (Zoom link on Canvas) |

Section 12 is fully virtual; all others are fully on-the-ground with no virtual option. **You must attend your registered section, and you may not partner with students in other sections for the term project.**

- **Canvas** — gradebook, SSO to Piazza, submission instructions
- **Piazza** — questions and discussion (check here first for codebase questions)
- **Pawtograder** — individual + final group project code submission ([khoury.pawtograder.com](https://pawtograder.khoury.northeastern.edu))

See [[CS4530 Staff and Office Hours]] for the instructional team (2 instructors, 16 TAs, ~64 hrs/week of TA office hours).

## Course Outcomes

- Define and describe the phases of the software engineering lifecycle (requirements, design, implementation, testing, deployment, maintenance)
- Explain the role of key processes and technologies in modern software development
- Productively apply instances of major tools used in elementary SE tasks
- Design and implement a portfolio-worthy SE project in a small team that can be publicly showcased to recruiters

## The Four Themes

```
Requirements  →  Design      →  Process       →  Quality
gathering &      for reuse,     collaborate      does it work,
specification    readability,   effectively      is it secure,
                 and scale                       does it do the
                                                 right thing
```

- **Requirements gathering and specification** — how to make sure you build the product the customer actually wants
- **Designing code for reuse, readability, and scale** — avoiding reinvention, defining readability, placing performance, knowing when to revisit and replace old design decisions
- **Organizing your development process** — communicating designs, structuring and coordinating work, measuring and tweaking process over time
- **Ensuring code works and is secure** — measuring usability/scalability/performance, minimizing defect cost, automating tests of complex systems, proving absence of defect classes

## Course Project

The assignments mirror joining a new development team: you are onboarded to an existing codebase, make several individual contributions, then form a team of 4 to propose, develop, and implement new features.

> [!success] Naming resolved — it's Game Nite
> The syllabus page calls the codebase a **"Fake Stack Overflow"** project, while
> [[Individual Project 1]] and [[Team Project Overview]] describe **GameNite**. Slide 19 of
> [[Module 01 - Orientation and User Stories|Module 01.1]] settles it: **Game Nite**, "the #1
> spot for people who want the social experience of watching Twitch™ but for turn-based games."
> The syllabus line is stale.

> [!tip] Sprint Report Template
> Canvas hosts a `Sprint Report Template.docx` under Files - it isn't linked from the course
> site. Expect weekly progress reports against it during the team project; contribution is
> judged partly on those reports.

**Stack**: TypeScript · React · Node.js · Vite · Express · Zod · Vitest · Playwright · Git · VS Code

At the end of the semester the staff select the best projects (usability, code quality, test suite quality, overall design) for the public showcase. See the [Spring 2026 showcase](https://neu-se.github.io/CS4530-Spring-2026/assignments/project-showcase).

## Grading

| Weight | Component |
| --- | --- |
| 30% | Individual projects (three deliverables, equally weighted) |
| 40% | Team project (including peer evaluations / surveys) |
| 10% | Participation in synchronous class, activities, and project work sessions |
| 20% | Exam — **Week 9 (Nov 4–6)**, no final exam |

The 40% team project itemizes as (from [[Module 01 - Orientation and User Stories|Module 01.1]]
slide 20, not on the course site):

| Share of course grade | Component |
| --- | --- |
| 8% | Planning |
| 8% | Process |
| 16% | Product |
| 8% | Reports |

Only 16 of the 40 points is the product itself — the rest is planning, process, and reports.

**Default scale for Prof Bhutta's sections** (from the Canvas "Miscellaneous Notes and Links" page):

| Grade | Range | Grade | Range |
| --- | --- | --- | --- |
| A | [94 - 100] | C | [74 - 78) |
| A- | [90 - 94) | C- | [70 - 74) |
| B+ | [88 - 90) | D+ | [68 - 70) |
| B | [84 - 88) | D | [64 - 68) |
| B- | [80 - 84) | D- | [60 - 64) |
| C+ | [78 - 80) | F | [0 - 60) |

**We don't round up** - 90 <= average < 94 is an A-, not an A. Each instructor decides their own
curve (if any) at the end of the semester; individual deliverables are never curved.

**Late policy** — Individual projects and activities: 10% off within 24 hours, zero after 24 hours. Group deliverables: no late submission at all. Work that does not compile or run receives at most 50% credit. Regrade requests must be opened within 5 days of receiving the grade — but
[[Module 01 - Orientation and User Stories|the Module 01.1 deck]] says **7 days**, plus a
**48-hour** window to appeal a closed regrade to the instructor by email. Treat 5 days as the safe
deadline. Use the regrade mechanism, not Piazza or email to your TA.

**Unequal team contribution** can cost an individual up to 50% of the team project grade (up to 100% for no contribution), judged on weekly progress reports, version control history, self-reflection, and peer evaluation.

## Deadlines

| Due | Deliverable |
| --- | --- |
| Wed 2026-09-23, 5:00pm ET | [[Individual Project 1]] |
| Fri 2026-10-02, 5:00pm ET | [[Team Formation Survey (tp1)]] |
| Week of 2026-10-05 | Project kick-off meeting with Mentor TA |
| Wed 2026-10-07, 5:00pm ET | [[Individual Project 2]] |
| Fri 2026-10-16, 5:00pm ET | [[Preliminary Project Plan (tp2)]] |
| Wed 2026-10-21, 5:00pm ET | [[Individual Project 3]] |
| Week 9, Nov 4–6 | **Exam** (20%) — exact per-section date TBD, check the calendar |
| Fri 2026-10-30, 5:00pm ET | [[Revised Project Plan (tp3)]] |
| Fri 2026-12-04, 5:00pm ET | [[Project Final Deliverable (tp4)]] |
| Mon 2026-12-14, 5:00pm ET | [[Individual Reflection (tp5)]] |

Full week-by-week breakdown per section: [[CS4530 Course Schedule]].

## Map of These Notes

Notes are filed in four subfolders; **[[CS4530 Assignments.base|CS4530 Assignments]]** is the
tracker (Upcoming / All assignments / No due date / Topics).

```
assignments/  what you turn in
topics/       modules and in-class activities
tutorials/    the week-1 setup and language references
reference/    schedule, staff, policies, style guide
```

### Schedule & Reference
- [[CS4530 Course Schedule]] — 15-module roadmap plus all four section calendars
- [[CS4530 Staff and Office Hours]] — instructors, TAs, office hour logistics
- [[CS4530 Textbooks and Resources]] — O'Reilly texts, podcasts, per-topic reading

### Modules
- [[Module 01 - Orientation and User Stories]] — what SE is, the people/processes/programs grid, course mechanics, then user stories and conditions of satisfaction
- [[Module 02 - From Requirements to Tests]] — TDD, conditions of satisfaction to testable behaviors

### Activities
- [[Activity 01 - User Stories and Conditions of Satisfaction]]
- [[Activity 02 - Test-Driven Development]]

### Assignments
- [[Individual Project 1]] — Connect4, Tic-Tac-Toe coverage, user service bugs, auth refactor
- [[Individual Project 2]] — not yet published
- [[Individual Project 3]] — not yet published
- [[Team Project Overview]] — team formation through final demo
- [[Team Formation Survey (tp1)]] · [[Preliminary Project Plan (tp2)]] · [[Revised Project Plan (tp3)]] · [[Project Final Deliverable (tp4)]] · [[Individual Reflection (tp5)]]

### Tutorials
- [[Tutorial - Development Environment Setup]] — Node 24 via nvm, VS Code, extensions
- [[Tutorial - TypeScript Basics]] — the full language reference for this course
- [[Tutorial - Unit Testing with Vitest]] — suites, matchers, AAA, mocks, async
- [[Tutorial - API Requests]] — HTTP verbs, headers, status codes, testing endpoints
- [[Tutorial - Git and GitHub Basics]] — repos, branches, forks, PRs, issues

### Standards
- [[CS4530 Code Style Guide]] — ESLint rules, naming, JSDoc requirements
- [[CS4530 Scientific Debugging]] — the 5-question debugging protocol staff will hold you to
- [[CS4530 AI Policy]] — what is forbidden where, and what you stay accountable for

## Acknowledgements

Inspired by SE courses at Columbia (COMS W4156), CMU ([17-313](https://cmu-313.github.io/)), GMU ([SWE 432](https://cs.gmu.edu/~tlatoza/teaching/swe432f19/home.html)), and NCSU ([CSC 326](https://sites.google.com/a/ncsu.edu/csc326-software-engineering/)), plus past iterations of CS4530 and CS5500 at Northeastern. Site built on [Kevin Lin's Just the Class](https://kevinl.info/just-the-class/).

---

**Course Number**: CS 4530
**Semester**: Fall 2026
**Topics**: Requirements Engineering, User Stories, Test-Driven Development, Design Patterns, React, Agile, Concurrency, Maintainability, CI/CD, Security, Cloud Deployment, SE Ethics

%% Begin Waypoint %%
- [[Activity 01 - User Stories and Conditions of Satisfaction]]
- [[Activity 02 - Test-Driven Development]]
- [[CS4530 AI Policy]]
- [[CS4530 Code Style Guide]]
- [[CS4530 Course Schedule]]
- [[CS4530 Scientific Debugging]]
- [[CS4530 Staff and Office Hours]]
- [[CS4530 Textbooks and Resources]]
- [[Fundamentals of Software Engineering]]
- [[Individual Project 1]]
- [[Module 01 - Orientation and User Stories]]
- [[Module 02 - From Requirements to Tests]]
- [[Team Project Overview]]
- [[Tutorial - API Requests]]
- [[Tutorial - Development Environment Setup]]
- [[Tutorial - Git and GitHub Basics]]
- [[Tutorial - TypeScript Basics]]
- [[Tutorial - Unit Testing with Vitest]]

%% End Waypoint %%
