---
tags:
  - software-engineering
  - northeastern
  - cs4530
  - react
  - frontend
  - activity
type: activity
course: "[[Fundamentals of Software Engineering]]"
module: 5
due: 2026-10-01
status: raw
---
# Activity 05 — Enhancing a TODO Tracker in React

In-class activity for [[Module 05 - React Basics]].

> [!danger] Graded on Canvas — 10 points, due Thu 2026-10-01, 5:00 PM ET
> [Open in Canvas](https://northeastern.instructure.com/courses/260680/assignments/3218520). Part
> of the 10% participation group. **Individual submission** in Bhutta's sections: you may discuss
> it with your group, but each person submits their own zip.
> **Attendance is required to get credit.**

- [ ] Submit Activity 05 - Enhancing a TODO Tracker in React 📅 2026-10-01

> [!info] Source
> <https://neu-se.github.io/CS4530-Fall-2026/Activities/Module05%20Activity/>, retrieved
> 2026-09-24. The starter is the
> [M05-M06 examples repo](https://github.com/mwand/M05-M06-React-Examples-Fall-2026), the same
> code the slides use.

## Setup

```sh
git clone https://github.com/mwand/M05-M06-React-Examples-Fall-2026.git
cd M05-M06-React-Examples-Fall-2026
npm install
npm run dev
```

> [!warning] Two mismatches between the handout and the repo
> - **`src/main.tsx` mounts `SimpleClock` by default, not the ToDo app.** Comment that import out
>   and uncomment `import App from "./Examples/ToDoApp/App"`, or you'll be editing code you
>   can't see.
> - The handout says the app lives in `Apps/ToDoApp` and runs on `localhost:3000`. In the repo it
>   is **`src/Examples/ToDoApp/`**, and Vite serves on whatever port it prints (normally 5173).

Files you'll touch:

| File | Owns |
| --- | --- |
| `ToDoApp/App.tsx` | `todoList` state, `handleAdd`, `handleDelete` |
| `ToDoApp/ToDoItemEntryForm.tsx` | the title and priority inputs (both plain `<Input>`, both `string` state) |
| `ToDoApp/Shared/ToDoListTypes.ts` | `ToDoItem = { title: string; priority: string; key: number }` |
| `ToDoApp/Shared/ToDoListDisplay.tsx` | the `map` with `key={eachItem.key}` |

## The Work

Make three enhancements to the ToDo app:

- [ ] **Priority must be a number.** The field currently accepts any text. The hint is Chakra's
      `NumberInput`. Change `priority` to `number` in `ToDoItem` and let the compiler list every
      place that still assumes a string: the form state, the `onAdd` signature, and `handleAdd`.
- [ ] **Sort button: order items by priority, lowest first.** Don't call `todoList.sort(…)` and
      pass the result to the setter. It sorts in place and returns the same reference, so React
      sees no change and doesn't re-render. Use `[...todoList].sort((a, b) => a.priority -
      b.priority)` or `todoList.toSorted(…)`. See the cheat sheet in
      [[Module 05 - React Basics#Treat state as read-only]].
- [ ] **Entry field + button: delete every item with priority greater than N.** Priority 1 means
      "do first," so this keeps the most urgent items. A `filter` in `App.tsx`. The threshold input
      needs its own state.

> [!tip] Why the stable `key` matters here specifically
> `ToDoItemDisplay` copies its item into local state. Sorting and bulk-deleting both move items
> to new positions. Because the list is keyed by `item.key` rather than array index, each row
> keeps its own component and state as it moves. Swap in `ToDoListDisplayBad.tsx` (index keys)
> after sorting and you can watch rows show the wrong titles.

## Submitting

Copy the files from the `ToDoApp` folder into a fresh folder and **submit a zip of those files
only**. The assignment accepts zip files only.

> [!danger] Do **not** run `npm run zip` and submit its output
> The handout: "If you do, you will get 0 points."

## Grading

10 points total.

| Enhancements done | Points |
| --- | --- |
| Any 2 of the 3 | 5 |
| All 3 | 10 |

The rubric lists no credit for just one of the three.

## Related

- [[Module 05 - React Basics]]
- [[Tutorial - React Basics]]
- [[Individual Project 2]] — the graded React work this rehearses
