---
tags:
  - finance
  - python
  - northeastern
  - hub
type: moc
semester_start: 2026-09-07
---
# Computational Methods in Finance

**FINA 4335 — Computational Methods and Their Applications in Finance** · Fall 2026 · Northeastern (D'Amore-McKim)

**Course Focus**: Python as a tool for financial data analytics. The first half is programming
fundamentals and the core data libraries (NumPy, Pandas, SciPy); the second half implements
financial models in Python — stock returns, single- and multi-factor models, portfolio
optimization, and quantitative trading.

> [!info] Source
> Logistics and schedule from `FINA 4335_Syllabus_Fall 2026_Kong.pdf` on Canvas, retrieved
> 2026-09-09. Section 02 (19002).

## Logistics

|  |  |
| --- | --- |
| **Instructor** | Professor Lingfei Kong — l.kong@northeastern.edu |
| **Office** | 409C Hayden Hall |
| **Time** | Tuesdays & Fridays, 1:35–3:15 PM |
| **Room** | 231 Richards Hall |
| **Office Hours** | Tue 3:30–5:00 PM (in person or online) · Fri 5:00–6:30 PM (online) |
| **Office Hours Zoom** | [northeastern.zoom.us/j/95336682566](https://northeastern.zoom.us/j/95336682566?pwd=CemPy4281abWL9S6CLSl00S9tZw0xZ.1) |

## Setup

- **Laptop required at every class.**
- **Anaconda Distribution** — runs JupyterLab locally. [Download](https://www.anaconda.com/download/success) (graphical installer recommended).
- **CodeGrade** — homework and after-topic exercises, accessed inside Canvas. Costs ~$40/semester. CodeGrade files are simplified `.ipynb` notebooks; write code in the required cells. **Unlimited submissions before the deadline.**
- **DataCamp** — free through the class. Register with your Northeastern email via the [class invitation link](https://www.datacamp.com/groups/shared_links/5b92d3541617254b5dea2776f2f59562ea5b3998cd1e848538cf5463441694d1).
- **Textbook** — Wes McKinney, *Python for Data Analysis*, 3rd ed. Free at [wesmckinney.com/book](https://wesmckinney.com/book/).

## Grading

| Weight | Component |
| --- | --- |
| 28% | Exam |
| 28% | Quizzes |
| 21% | Group project |
| 10% | Homework |
| 7% | After-class practice |
| 5% | DataCamp |
| 1% | Attendance |

**Late policy** — 10% penalty per day unless specified otherwise. The final group project takes
10% per day and is not accepted after two days.

**Quizzes** — the **lowest quiz is dropped, including a 0**; that drop is the accommodation for
illness, interviews, and the like (tell Kong 3 business days ahead). **Missing the midterm** with a
documented reason Kong accepts gets it scored at 80% of your quiz score — that is where the
80% figure comes from; it is not a quiz penalty.

**After-class practice** (7%) — Canvas renamed the group "after-topic practice-will drop 2" between
2026-09-21 and 2026-09-25: the two lowest after-topic sets are dropped.

## Deadlines

| Due | Deliverable |
| --- | --- |
| Sun 2026-09-20 | [[DataCamp Classroom Enrollment]] |
| Thu 2026-09-24 | [[Topic 1 Extra Practice]] — *extended from Sep 20* |
| Fri 2026-09-25 | [[Quiz 1]]: **10/10** · [[Quiz 1 Prep]] (practice, 0%): 9.5/14 |
| Fri 2026-10-02 | [[Quiz 2]] (in class, 1:37–2:00pm, 18 min, LockDown Browser) · [[Quiz 2 Prep]] (practice, 0%, open to Oct 4) |
| Sun 2026-10-04 | [[HW1]] · [[DataCamp Assignment 1]] · [[Topic 2 Extra Practice]] — *extended from Sep 27* |
| Fri 2026-10-16 | [[Exam 1]] (in class) |
| Sun 2026-10-18 | [[Topics 3-4 Extra Practice]] · [[Group Project Sign-Up]] |
| Tue 2026-10-27 | [[Quiz 3]] (in class) |
| Sun 2026-11-01 | [[HW2]] |
| Sun 2026-11-08 | [[Topics 5-8 Extra Practice]] |
| Tue 2026-11-17 | [[Quiz 4]] (in class) |
| Sun 2026-11-22 | [[HW3]] · [[DataCamp Assignment 2]] |
| Fri 2026-12-11 | [[Topics 9-12 After-Topic Practice]] |
| Thu 2026-12-17 | [[Final Group Project]] |

## Map of These Notes

**[[FINA4335 Assignments.base|FINA4335 Assignments]]** is the tracker — Upcoming, All
assignments, No due date, and Topics views.

```
assignments/  homework, practice sets, quizzes, exams, group project
topics/       one note per topic, with its class meetings
```

### Topics

- [[Topic 00 - Course Intro and Setup]]
- [[Topic 01 - Python Basics]] — notebooks Part I & Part II written up
- [[Topic 02 - Data Structures and Functions]]
- [[Topic 03 - NumPy]] — `Topic 3 NumPy Basics.ipynb` written up, exercise answers worked
- [[Topic 04 - Pandas Introduction]]
- [[Topic 05 - Pandas Group Operations]]
- [[Topic 06 - Pandas Data Wrangling]]
- [[Topic 07 - Pandas Time Series]]
- [[Topic 08 - Stock Returns]]
- [[Topic 09 - Portfolio Risk and Return]]
- [[Topic 10 - Factor Models]]
- [[Topic 11 - Portfolio Optimization]]
- [[Topic 12 - Quant Trading Strategies]]

## Canvas Files

*As of 2026-09-27.* Canvas renamed the "Lecture notes" module to **"Notes: python basics"** and
added a **"Notes: numpy"** module.

- `FINA 4335_Syllabus_Fall 2026_Kong.pdf`
- `FINA 4335_Course introduction-Fall 2026.pdf`
- `Introduction to CodeGrade.pdf`
- `Topic 1 Python Language Basics-Part I.ipynb` / `.pdf`
- `Topic 1 Python Language Basics-Part II.ipynb` / `.pdf` — control flow and imports
- `Topic 2 Built-in Data Structures and Functions-Part I.ipynb` / `.pdf` — posted 2026-09-19
- `Topic 2 Built-in Data Structures and Functions-Part II.ipynb` / `.pdf`
- **`with solution/`** — new folder, added 2026-09-20. Currently holds
  `Topic 1 Python Language Basics-Part I-with Solution.pdf` and (first seen 2026-09-25)
  `Topic 1_ Python Language Basics-Part II-with Solution.pdf`. Worked solutions to the topic
  notebooks land here. First seen 2026-09-27: `Topic 2 Built-in Data Structures and
  Functions-Part I-with Solution.pdf` and `…-Part II-with solution.pdf`. Those two cover all of
  [[Quiz 2]] except NumPy.
- `Topic 3 NumPy Basics.ipynb` / `Topic 3 - NumPy Basics.pdf` — first seen 2026-09-27, before
  the Sep 29 lecture

---

**Course Number**: FINA 4335
**Semester**: Fall 2026
**Topics**: Python, NumPy, Pandas, Time Series, Stock Returns, Portfolio Theory, Factor Models, Portfolio Optimization, Quantitative Trading

%% Begin Waypoint %%
- **assignments**
	- [[DataCamp Assignment 1]]
	- [[DataCamp Assignment 2]]
	- [[DataCamp Classroom Enrollment]]
	- [[Exam 1]]
	- [[Final Group Project]]
	- [[Group Project Sign-Up]]
	- [[HW1]]
	- [[HW2]]
	- [[HW3]]
	- [[Quiz 1 Prep]]
	- [[Quiz 1]]
	- [[Quiz 2 Prep]]
	- [[Quiz 2]]
	- [[Quiz 3]]
	- [[Quiz 4]]
	- [[Topic 1 Extra Practice]]
	- [[Topic 2 Extra Practice]]
	- [[Topics 3-4 Extra Practice]]
	- [[Topics 5-8 Extra Practice]]
	- [[Topics 9-12 After-Topic Practice]]
- **topics**
	- [[Topic 00 - Course Intro and Setup]]
	- [[Topic 01 - Python Basics]]
	- [[Topic 02 - Data Structures and Functions]]
	- [[Topic 03 - NumPy]]
	- [[Topic 04 - Pandas Introduction]]
	- [[Topic 05 - Pandas Group Operations]]
	- [[Topic 06 - Pandas Data Wrangling]]
	- [[Topic 07 - Pandas Time Series]]
	- [[Topic 08 - Stock Returns]]
	- [[Topic 09 - Portfolio Risk and Return]]
	- [[Topic 10 - Factor Models]]
	- [[Topic 11 - Portfolio Optimization]]
	- [[Topic 12 - Quant Trading Strategies]]
- [[Computational Methods in Finance]]
- [[FINA4335 Assignments.base|FINA4335 Assignments]]

%% End Waypoint %%
