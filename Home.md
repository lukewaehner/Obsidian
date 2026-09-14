---
tags:
  - home
  - hub
type: moc
aliases:
  - Index
  - Start Here
---
# Home

Fall 2026 · five active courses · interview prep in flight.

**Jump to** — [[Fall 2026 Calendar]] · [[Deadlines.base|All deadlines]] · [[Career/Prep/Problems.base|Problems]] · [[Career/Prep/Topics.base|Topics]] · [[Courses]] · [[Career/Prep/Prep|Prep]]

---

## Overdue and due today

```tasks
not done
due before tomorrow
path includes Courses
sort by due
short mode
```

## Next two weeks

```tasks
not done
due after today
due before in 2 weeks
path includes Courses
sort by due
short mode
```

> [!tip] Nothing showing?
> Deadlines come from the `- [ ] … 📅 YYYY-MM-DD` line inside each assignment note.
> Eight of the fifty assignment notes don't have one yet — [[Deadlines.base|All deadlines]]
> lists everything regardless, and its *No due date* view shows the gaps.

---

## Pick up where you left off

```dataview
TABLE WITHOUT ID
  file.link AS "Note",
  course AS "Course",
  dateformat(file.mtime, "EEE MMM d, h:mm a") AS "Touched"
FROM "Courses" OR "Career/Prep"
WHERE type != "moc"
SORT file.mtime DESC
LIMIT 12
```

> [!info] Why not a "this week" view?
> `date:` in lecture notes is the day the note was *mirrored from the course site*,
> not the day the session meets — every ORGB lecture reads `2026-09-09`, every DS
> lecture `2026-09-10`. And `week:` is missing on all 26 ORGB and both FSE lectures.
> The hand-built grid in [[Fall 2026 Calendar]] is the accurate week-by-week source.
> If you ever backfill true meeting dates onto `date:`, this block can become a real
> seven-day window.

---

## Courses

| Code | Course | Instructor | Assignments |
| --- | --- | --- | --- |
| CS 4530 | [[Fundamentals of Software Engineering]] | Bhutta | [[CS4530 Assignments.base\|Tracker]] |
| CS 4730 | [[Distributed Systems]] | Jackson | [[CS4730 Assignments.base\|Tracker]] |
| ENGW 3302 | [[Advanced Writing in Tech]] | DeCamp | [[ENGW3302 Assignments.base\|Tracker]] |
| FINA 4335 | [[Computational Methods in Finance]] | Kong | [[FINA4335 Assignments.base\|Tracker]] |
| ORGB 3201 | [[Organizational Behavior]] | Liao | [[ORGB3201 Assignments.base\|Tracker]] |

Week-by-week grid across all five: [[Fall 2026 Calendar]].
Past coursework: [[Strategy and Action]].

> [!note] `status:` is not completion
> In course notes `status:` tracks how far *the note* has been processed
> (`raw` → `learning` → `solid`), not whether the work is done. Done-ness lives on
> the task checkbox.

---

## Prep

![[Career/Prep/Prep#Progress]]

![[Career/Prep/Prep#Weakest topics]]

![[Career/Prep/Prep#Needs revisit]]

Drill in via [[Career/Prep/Topics.base|Topics]] and [[Career/Prep/Problems.base|Problems]].
`/prep:next` recommends what to study · `/prep:review` quizzes weak topics ·
`/prep:sync` rebuilds the numbers above after you add problems.

---

## Map

**Active**
- [[Courses]] — Fall 2026 coursework, retired to [[Code]] / [[Finance]] on completion
- [[Career]] — [[Career/Prep/Prep|Prep]], resume, interview bank, job sites
- [[Meteora]] — work: the eight repos, the box, and where the data comes from

**Reference**
- [[Code]] — languages, tools, and CS fundamentals across 13 sub-topics
- [[Finance]] — Corporate Finance, Financial Accounting, Investments, Managerial Accounting
- [[Northeastern]] — class planning and university resources
- [[Archive]] — retired notes, queued for cleanup

Templates live in `templates/` (daily, meeting, MOC, lecture, course, per-language).
