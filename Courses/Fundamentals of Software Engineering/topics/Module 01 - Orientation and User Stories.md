---
tags:
  - software-engineering
  - northeastern
  - cs4530
  - requirements
  - user-stories
  - module
type: lecture
course: "[[Fundamentals of Software Engineering]]"
module: 1
status: notes
---
# Module 01 — Orientation and User Stories

> [!info] Source
> <https://neu-se.github.io/CS4530-Fall-2026/modules/1-user-stories>

**Week 1** of [[Fundamentals of Software Engineering]] · Two lessons: *Course Introduction* and *User Stories*
**Slides**: `Module 01.1 Course Introduction` · `Module 01.2 User Stories` (pdf / pptx)

> [!danger] Important date
> [[Individual Project 1]] due **Wednesday Sep 23, 5:00pm ET**

## Learning Objectives

After this lecture you should be able to:

- [x] Explain in general terms what software engineering is
- [x] List your weekly obligations as a student
- [x] List the requirements for completing the course
- [ ] Explain requirement gathering
- [ ] Explain the structure of a user story
- [ ] Identify and fix user stories that don't have the correct structure
- [ ] Define the relationship between conditions of satisfaction and user stories, and the difference between **essential**, **desired**, and **extension** conditions of satisfaction
- [ ] Identify functional and non-functional requirements, and give examples of each

## Notes

### 01.1 — Course Introduction

Slides 1–30. This lesson is half "what is software engineering" and half "how this course runs."
The conceptual half is short and worth actually knowing — it's the frame the whole semester hangs
on, and the two-axis grid on slide 12 is the single most useful slide in the deck.

#### Where the term comes from

| Who | When | What |
| --- | --- | --- |
| **Margaret Hamilton** | ~1963, NASA | Led the Apollo Guidance Computer software; the famous photo is her standing next to a stack of its printed source, roughly her own height. Credited with coining "software engineering." |
| **Anthony Oettinger** | Aug 1966, *Comm. of the ACM* p. 546 | ACM President's call to "recognize ourselves . . . as members of an *engineering* profession, be it hardware engineering or software engineering, a profession without artificial and irrelevant boundaries like that between 'scientific' and 'business' applications." |
| **1968 NATO Conference** | Garmisch, Germany, Oct 7–11 1968 (report Jan 1969) | The founding event. Chaired by **Friedrich Bauer**; **Barry Boehm** among the outcomes/figures. This is where the discipline gets named and scoped. |

The through-line: the label was a deliberate *aspiration* — make software production look like an
engineering discipline rather than a craft.

> [!note] Definition
> **Software engineering** — the **design**, **construction**, and **maintenance** of *large*
> programs, *over time*. The two qualifiers at the end are doing all the work; drop either one
> and it's just programming.

#### "Large" is relative (slide 5)

The scale-of-space gag: *Software Engineering at Google* (Winters, Manshreck, Wright) is the sun.
The Apollo Guidance Computer's software, almost any pre-series-B startup, and **your 4-person
project in this class** are the small planets off to the side. The point isn't that your project
is trivial — it's that the problems start biting well below Google scale, and the course is
calibrated to "medium-sized web applications," not to Google.

#### The two problems that make it hard

Both are about humans, not machines:

1. **Programs need to be read by people.**
   > "Any fool can write code that a computer can understand. Good programmers write code that
   > humans can understand." — **Martin Fowler**
2. **People need to talk to each other.**
   > "Adding manpower to a late software project makes it later." — **Fred Brooks, 1975**
   > (*The Mythical Man-Month*; the reason is communication overhead growing faster than the
   > headcount, plus ramp-up time stolen from the people already on the project.)

→ Therefore software engineering has to cover **PEOPLE, PROCESSES, & PROGRAMS** (slide 8).

#### Two axes, one grid

**Axis 1 — the three objects** (slide 9):

| | The course covers |
| --- | --- |
| **People** | how to organize software teams and make them function effectively; how SE teams work inside larger organizations |
| **Processes** | how to divide a large project into engineering tasks; how to coordinate those tasks into a coherent whole |
| **Programs** | how to write programs people can understand and maintain — focused on one domain, **medium-sized web applications** |

**Axis 2 — the three scales of design** (slide 10). Note the slide's labels and questions are
mismatched relative to what you'd expect — copied as-is:

| Scale              | Key questions (as printed)                                                          |
| ------------------ | ----------------------------------------------------------------------------------- |
| **Planning**       | How do we make software artifacts "good"? What does that mean? Who decides?         |
| **Organizational** | What are people's needs? How do we design software artifacts that meet those needs? |
| **Implementation** | How do we design software artifacts that are easy to test, understand, and modify?  |

→ **PLANNING, ORGANIZING, & IMPLEMENTING** (slide 11).

**The grid (slide 12)** — 3 objects × 3 scales, with the course's scope drawn on it:

```
              PEOPLE        PROCESSES      PROGRAMS
PLANNING    |  . . . . . mostly out of scope . . . . |
            +---------------------------------------+
ORGANIZING  |                                       |
            |        THIS CLASS IS HERE-ISH         |
IMPLEMENTING|                                       |
            +---------------------------------------+
                                      previous classes (OOD)
```

- **Top row (planning)** — mostly out of scope.
- **Middle band (organizing → implementing, across all three columns)** — this course.
- **Bottom-right corner (implementing programs)** — already covered by prior classes, i.e.
  Object-Oriented Design.

> [!tip] Why this grid is worth remembering
> It's the answer to "why are we doing team surveys and sprint reports in a *programming* class."
> The course deliberately sits in the band where the object is a team and a process, not just a
> program — and it deliberately skips the strategy/planning row and the OOD corner you already
> have.

#### Course-level learning objectives (slide 13)

Bhutta flags the first four as "normal learning goals for a course at a university" and the last
one as "maybe a little different":

- define and describe the phases of the SE lifecycle
- explain the role of key processes and technologies in modern software development
- demonstrate the ability to **use** those key processes
- demonstrate application of key technologies and major tools in elementary SE tasks
- **design and implement a portfolio-worthy SE project in a small team that can be showcased to
  recruiters** ← the different one

#### Delivery: three channels (slide 14)

| Channel                            | What it is                                                                                                                                    |
| ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| **Lectures + in-class discussion** | In person. Slides posted on the course site.                                                                                                  |
| **Activities**                     | Practice with the course technologies; often *started in class*, sometimes in groups; **submitted on Canvas and graded**; attendance required |
| **Tutorials**                      | Background on processes and technologies at more depth than class allows — the **primary "reading" for the course in lieu of a textbook**     |

> [!warning] Tutorials are not optional supplements
> The deck calls them the primary reading. That reframes [[Tutorial - TypeScript Basics]],
> [[Tutorial - Unit Testing with Vitest]], [[Tutorial - API Requests]],
> [[Tutorial - Git and GitHub Basics]], and [[Tutorial - Development Environment Setup]] as the
> textbook, not as setup docs.

#### Mechanics and policies

**Attendance (slide 15).** Required — *especially* for activities and project work: "work on
project" sessions, project meetings, and demos. Bring your laptop. Excused absence requires
emailing the instructor, *preferably in advance*.

**Deliverables and weights (slide 16).**

| Weight | Deliverable |
| --- | --- |
| 30% | Individual project, done **individually**, in 3 deliverable stages |
| 40% | Group project, teams of *about* **4** |
| 20% | **Exam during Week 9 (Nov 4–6)** — no final exam. "Check the calendar for exact date!" |
| 10% | Completion of activities |

**Team project internal breakdown (slide 20)** — this is not on the course website:

| Share of course grade | Component |
| --------------------- | --------- |
| 8%                    | Planning  |
| 8%                    | Process   |
| 16%                   | Product   |
| 8%                    | Reports   |

That's the 40% itemized. Note **Product is only 16 of the 40** — more than half the team grade is
planning, process, and reports. Also: peer evaluation surveys may be used, and individual
contribution **will** scale your project grade anywhere in **0–100%**.

**Hard gates to pass the course (slide 17).** Beyond the numeric grade you must *also*:

- do most of the individual projects
- demonstrate understanding of concepts on the midterm
- demonstrate ability to do software development & engineering in the group project
- **present your final project**

With two consequences stated in red:

- don't complete the individual projects → **you might not be assigned to a project team**
- don't present your final project → **you might not pass the class**

**Grade appeals (slide 21).** Use the provided regrade mechanism — **do not post on Piazza or
email your TA/instructor**. Requests within **7 days** of receiving the graded work. If a regrade
is closed and the response is unsatisfactory, appeal to the instructor by email within **48
hours**.

**Late policy (slide 22).** Matches the site: individual work −10% within 24 hours, **zero** after
24 hours; **no late submission at all for group work**. Two additions the site doesn't state:

- If you have a **Disability Access Services** accommodation you must request it from the
  instructors **separately for each assignment or exam**.
- DAS accommodations are "usually NOT available for Group Assignments" — work with the instructor.

#### Technology (slide 18)

TypeScript · Vitest · VS Code · React · **GitHub Projects** for project management ·
**GitHub Actions / Render** for CI/CD · **Pawtograder** as LMS (grading, submission).

Worth noting the hub's stack list adds Node.js/Vite/Express/Zod/Playwright from elsewhere on the
site; the deck's own list is the one above, and it's the first mention of **Render** as the deploy
target and **GitHub Projects** as the PM tool.

#### The framing device: "Welcome to the Game Nite team!" (slides 19–20)

> Game Nite wants to be "the #1 spot for people who want the social experience of watching
> Twitch™ but for turn-based games."

- **CS 4530 is part traditional academic course, part "having a new software job" simulation.**
- The **individual projects are "onboarding" projects** — the kind of scoped starter tickets you'd
  get in your first two weeks on a real team.
- The **group project is a scaled-down version of actual product delivery**, on a feature *you*
  propose.
- **Course staff have a secondary role as part of this simulation** — TAs are mentors/leads, not
  just graders. Read staff interactions accordingly.
- Teams are formed **by the instructors, with your input** (via [[Team Formation Survey (tp1)]]).

> [!success] Resolves the naming question
> Slide 19 says **Game Nite** outright, with a Number Guesser game-room screenshot. That settles
> the "Fake Stack Overflow vs GameNite" ambiguity flagged in
> [[Fundamentals of Software Engineering]] — the syllabus line is stale.

#### Academic integrity (slides 23–24)

- Work **individually** on all homework. High-level discussion with classmates is encouraged;
  turning in anything copied from another student's assignment is prohibited.
- Small snippets of publicly posted code are allowed **with attribution**.
- **Steal someone else's work → you fail the class.** And: "You are responsible for protecting
  your work. If someone uses your work, with or without your permission, you fail the class."
- If attributing reused code makes you worried it'll look like you didn't do the assignment, raise
  it with the instructor rather than hiding it.
- **Default when unsure: assume it is NOT allowed** unless the instructors confirm otherwise.

#### AI policy as delivered in class (slides 25–28)

Consistent with [[CS4530 AI Policy]]; the deck adds the reasoning and the tone.

- **IP1 and IP2: no LLM tools.** No Copilot autocomplete, no natural-language-to-code, no
  chatbot-assisted code understanding.
- **The stated reason** (slide 26): VS Code's TypeScript-powered navigation tools are sophisticated
  and free, and they want you to *also* have real experience with those. The slide literally
  points at the button in the VS Code status bar that turns Copilot off.
- **IP3:** exploration of generative tools is "**gently encouraged**."
- **Final project:** AI permitted — **create a group policy on AI**.
- **You are responsible for your code and must understand it**, and you **must document uses of
  LLM-based tools**. Staff "reserve the right to **interview** you to gauge your understanding
  (with possible grade adjustments)."
- **No LLM tools for writing** (slide 28): "When we ask you to write English text, it's because we
  want you to write it and because we're going to read it. You're just disrespecting yourself and
  us by having us read LLM-generated text."
- Slide 25 quotes a Sam Halpert post as the framing: using AI in education is "like using a
  forklift at the gym. The weights do not actually need to be moved from place to place. That is
  not the work. The work is what happens within you."

#### Communication (slide 29)

| Channel | Use it for |
| --- | --- |
| [Course site](https://neu-se.github.io/CS4530-Fall-2026/) | Source of truth; Canvas mirrors it, assignments and notices appear in both |
| **Piazza** | Anything about content, policies, assignments, projects — asked here so everyone gets the same answer |
| **Email the instructor directly** | Private questions about your individual situation. **Do NOT use Canvas messages** — they sometimes don't reach instructors. **Put "CS4530" in the subject line.** |
| **Office hours** | Schedule on the [staff page](https://neu-se.github.io/CS4530-Fall-2026/staff/); TA hours run through the **Khoury Office Hours App** |

### 01.2 — User Stories

Requirement Analysis - understanding what we are building so we can build the correct thing.

Problems with requirement analysis:
- Problems in understanding:
	- Do users know what they want?
	- Do users know what we don't know?
	- Do we know who our users are?
- Problems of scope:
	- What are we building?
	- What non-functional
- Problems of volatility
	- Changing requirements over time

Common Elements:
- Meet with stakeholders
- Devise common language
- Collect system behaviors that offer value
- Document desired behavior
- Iteration

### Formula:
As a _role_
I want _capability_
So that I can _get some benefit_

>**Example:**
As a(n) *active outdoor park-goer*
 I want *a safe way to fly through the air under a tree*
so that I can *feel the wind in my hair*

#### Roles:
Positions or functions that people inhabit - it is the user, not the customer
As a 'Web Server' - not a user
As a 'Human being' - not a role
As a 'user' - a cop-out

#### Capabilities:
A *specific* thing one wants to be able to do
- Usually an action we can provide by using software
It relates to a role
It is not a product

#### Benefit
Key for user stories is actually focusing on what matters to the user
Features that do not relate to the user story either:
1. Are not worth building
2. Belong to a different user story that may need to be prioritized

>**Properties:**
>Fits on 3x5 card
>May have prerequisites
>Conditions of satisfaction that expand on the details
>satisfies INVEST+E

### Conditions of Satisfaction
- Describes a testable behavior from the user's point of view
- Must have a priority
- Should be numbered within its user story
- There may be multiple options 
#### Priorities
- **Essential (E)** - The product is useless without it
- **Desirable (D)** - The product is less usable without it, but still useable
- **Extension (X)** -  A condition that is not within the current project's scope, potentially for the next version

**Example**:
As a car commuter, I want to be able to quickly report potholes to the city so the town can move quickly to keep me safe.
- **1.1** I should be able to report the location of a pothole to the system *(E)*
- **1.2** I should be able to see if the pothole I reported has been repaired *(E)*
- **1.3** I should be able to see if others near me have reported potholes *(D)*
- **1.4** I should be able to see an estimated time of when the pothole will be fixed *(X)*

As a pothole-repair-truck driver, I want the system to display
the potholes I should be working on today, so that I can view
and report my progress for the day.
- **2.1** I should be able to see my list of potholes for today *(E)*
- **2.2** I should be able to report that I repaired a given pothole *(E)*
- **2.3** I should be able to report that I was unable to repair a given pothole, and to supply a reason *(E)*
- **2.4** My daily list of potholes should be listed in an order that cuts down the time I spend driving from job to job *(D)*

### Invest + E
- Independent 
- Negotiable
- Valuable (has value to the client)
- Estimate (able to estimate development effort)
- Small
- Testable

Ethical (connects with our & users’ values)

- User stories roughly describe **functional requirements**
- The **non-functional requirements** are other properties that are also important to users and to other stakeholders

**Non functional requirement types:**

| Verbiage        |                |
| --------------- | -------------- |
| Availability    | Capacity       |
| Response Time   | Scalability    |
| Efficiency      | Security       |
| Extensibility   | Supportability |
| Maintainability | Testability    |
| Performance     | Privacy        |
| Usability       | Response Time  |

### Minimum Viable Product:
A set of user stories are decided on, the Essential (E) conditions of satisfaction across all stories constitute to the MVP
A user story is implemented when all Essential COSs are implemented

#### Invest Framework
As a user I want function so that value.

Above is a very simple user story template.  How can something so simple be so hard to get right?  User stories make up the heart of agile development.  They are the primary input to the team.  The team takes the user stories and creates product increments based on completing those stories.  Unfortunately, getting user stories “right” is difficult to do right away.  The Product Owner (or other product facing role) needs to learn how to create user stories which meet the needs of the team.  This is a skill which can be learned over time, but I’m about to save you a bit of learning curve.

In order to create good user stories, start by remembering to INVEST in good user stories.  INVEST is an acronym which encompasses the following concepts which make up a good user story:

- Independent
- Negotiable
- Valuable
- Estimable
- Small
- Testable

Let’s cover each of them with a simple explanation.

**Independent:**  Stories should be as independent as possible.  When thinking of independence it is often easier to think of “order independent.”  In other words, stories can be worked on in any order.  Why is this important?  It allows for true prioritization of each and every story.  When dependencies come into play it may not be possible to implement a valuable story without implementing other much less valuable stories.

**Negotiable:**  A story is not a contract.  A story IS an invitation to a conversation.  The story captures the essence of what is desired.  The actual result needs to be the result of collaborative negotation between the customer (or customer proxy like the Product Owner), developer and tester (at a minimum).  The goal is to meet customer needs, not develop something to the letter of the user story if doing so is insufficient!  Remember, you can always [ask the magic question](https://agileforall.com/2009/02/20/when-in-doubt-ask-how-will-i-know-ive-done-that/) to help drive the conversation.

**Valuable:**  If a story does not have discernable value it should not be done.  Period.  Hopefully user stories are being prioritized in the backlog according to business value, so this should be obvious.  Some people say each story should be valuable to the customer or user.  I don’t like that way of thinking because business value encompasses more than just customer or user facing value.  It includes internal value which is useful for things which are normally called “non-functional requirements” or something similar.  I prefer to say the story has value to the “user” in the user story.  In this way it is clear who is to be satisfied.  Finally, remember the “so that value” clause of the user story.  It is there for a reason – it is the exact value we are trying to deliver by completing the story!

**Estimable:**  A story has to be able to be estimated or sized so it can be properly prioritized.  A value with high value but extremely lengthy development time may not be the highest priority item because of the length of time to develop it.  What happens if a story can’t be estimated?  You can split the story and perhaps gain more clarity.  Sometimes splitting a story doesn’t help though.  If this situation occurs it may be necessary to do some research about the story first.  Please, please, please timebox the research!  If you do not, it will take all available time thereby depriving the product of something else which could have been done instead.

**Small:**  Obviously stories are small chunks of work, but how small should they be?  The answer depends on the team and the methodology being used.  I teach agile and suggest two week iterations which allow for user stories to average 3-4 days of work – TOTAL!  This includes all work to get the story to a “done” state.  Also remember not to goldplate user stories.  You should [do the simplest thing that works – then stop](https://agileforall.com/2009/04/27/new-to-agile-do-the-simplest-thing-that-works-then-stop/)!

[Check out our extensive resources on how to split user stories.](https://agileforall.com/splitting-user-stories/)

**Testable:**  Every story needs to be testable in order to be “done.”  In fact, I like to think of testable meaning acceptance criteria can be written immediately.  Thinking this way encourages more collaboration up front, builds quality in by moving QA up in the process, and allows for easy transformation to an acceptance test-driven development (ATDD) process.  As with negotiable above, [asking the magic question](https://agileforall.com/2009/02/20/when-in-doubt-ask-how-will-i-know-ive-done-that/) can help ensure the user story is testable as well.

If Product Owners and their teams work together to INVEST in good user stories the learning curve of working together will be much shorter.  INVEST encourages good habits which eliminate some of the bigger problems of user stories like dependencies, being too big, hard to test, etc.  Take the time to INVEST in good stories and see the dramatic change in how effective planning will become, as well as how productive the team will become.

Until next time I’ll be INVESTing in good user stories because doing so definitely helps in Making Agile a Reality™.

## Key Takeaways

- SE = design + construction + **maintenance** of **large** programs **over time**. The scale and
  time qualifiers are what separate it from programming.
- Both core difficulties are human: code is read by people (Fowler), and coordination costs grow
  with team size (Brooks).
- The scope grid: **3 objects** (people / processes / programs) × **3 scales** (planning /
  organizing / implementing). This course = the organizing–implementing band across all three
  columns. Planning row out of scope; implementing-programs corner already done in OOD.
- The course is a **job simulation**: individual projects = onboarding tickets, group project =
  product delivery, staff = mentors playing a role.
- **Tutorials are the textbook**, not optional setup docs.
- More than half the team grade is planning, process, and reports — only 16 of the 40 points is
  the product itself.
- Four non-negotiable gates: most IPs done, midterm understanding, demonstrated group
  contribution, **and present the final project**.

## Activity

[[Activity 01 - User Stories and Conditions of Satisfaction]]

## Tutorials Assigned

- [[Tutorial - Development Environment Setup]]
- [[Tutorial - TypeScript Basics]]
- [[Tutorial - API Requests]]

## Slides

Posted on Canvas as module items; the decks live on the course site.

| Deck                              | PDF                                                                                               | PPT                                                                                                |
| --------------------------------- | ------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| Module 01.1 — Course Introduction | [PDF](https://neu-se.github.io/CS4530-Fall-2026/Slides/Module%2001.1%20Course%20Introduction.pdf) | [PPT](https://neu-se.github.io/CS4530-Fall-2026/Slides/Module%2001.1%20Course%20Introduction.pptx) |
| Module 01.2 — User Stories        | [PDF](https://neu-se.github.io/CS4530-Fall-2026/Slides/Module%2001.2%20User%20Stories.pdf)        | [PPT](https://neu-se.github.io/CS4530-Fall-2026/Slides/Module%2001.2%20User%20Stories.pptx)        |

Additional content: [modules/1-user-stories](https://neu-se.github.io/CS4530-Fall-2026/modules/1-user-stories)

## Resources

- Class syllabus → [[Fundamentals of Software Engineering]]
- [INVEST criteria for user stories](https://agileforall.com/new-to-agile-invest-in-good-user-stories/) — intro to both user stories and INVEST
- [Domain Modeling Made Functional](https://onesearch.library.northeastern.edu/permalink/01NEU_INST/i2gqis/alma9952083043301401) — Chapter 2's first section, "Interview with a Domain Expert," is a worked example of soliciting a client's needs
- [[Team Project Overview]]

## Related

- [[Module 02 - From Requirements to Tests]]
- [[CS4530 Course Schedule]]
