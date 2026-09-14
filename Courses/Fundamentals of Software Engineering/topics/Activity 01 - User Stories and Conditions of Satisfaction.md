---
tags:
  - software-engineering
  - northeastern
  - cs4530
  - requirements
  - user-stories
  - activity
type: activity
course: "[[Fundamentals of Software Engineering]]"
module: 1
status: raw
---
# Activity 01 — User Stories and Conditions of Satisfaction

In-class activity for [[Module 01 - Orientation and User Stories]]. Practice soliciting and documenting user requirements, refining them into conditions of satisfaction, and assigning priorities. Review the lecture slides first.

## Scenario

Consider a Learning Management System (like Canvas). Choose **one** area:

1. Sections and Enrollment
2. **Assignment Submission and Grading**
3. Gradebooks

## Requirements

1. Say which area you picked.
2. Identify at least **3 different roles** representing different classes of users for that area.
3. Choose **one** of those roles and write at least **3 user stories** for that participant, each in the form:

Chosen area: **Assignment Submission and Grading**

Three roles:
	- A student
	- A teacher
	- A TA

Chosen role: **A teacher**

As a teacher I want to be able to manage deadlines, including per-student overrides so I can accommodate individual students' scenarios.
1.1 I should be able to set a standard deadline for all students (E)
1.2 I should be able to extend / re-open a deadline for an individual student(s) (E)
1.3 I should be able to see how many times a student has submitted an assignment late (D)
1.4 I should be able to auto apply extensions for a list of accommodated students (X)

As a teacher I want to be able to leave rubric based feedback on a submission so I can keep grading feedback standardized
2.1 I should be able to fill out an attached rubric template per student's submission (E)
2.2 I should be able to make the rubric visible to students when grading is complete (E)
2.3 I should be able to leave custom comments / notes on portions of the rubric (D)

As a teacher I want to be able to assign subsets of an assignment's submissions to a TA so I can break up grading work into manageable chunks.
3.1 I should be able to select a group of submissions for an assignment and assign a TA to the submissions (E)
3.2 I should be able to track each TA's grading progress (E)
3.3 I should be able to only assign unassigned submissions to TAs (E)
3.4 I should be able to move a submission from one TA to another TA (X)

   ```
   As a <role> I want <some capability> so that I can <get some benefit>
   ```

3. For **each** user story, write **3–4 conditions of satisfaction** with appropriate priorities. Essential means the user story is not satisfied without it. There must be **at least one essential** and **at least one non-essential** condition of satisfaction.

### Deliverable Count

| Item                                         | Count |
| -------------------------------------------- | ----- |
| Area                                         | 1     |
| Roles                                        | 3     |
| User stories                                 | 3     |
| Conditions of satisfaction (with priorities) | 9–12  |

Submit as directed by your instructor — check the Canvas assignment.

## Grading — 10 pts

| Points | Criterion                                                   |
| ------ | ----------------------------------------------------------- |
| 3      | 3 roles                                                     |
| 3      | 3 user stories                                              |
| 4      | 9–12 conditions of satisfaction with appropriate priorities |

## Related

- [[Module 01 - Orientation and User Stories]]
- [[Activity 02 - Test-Driven Development]]
