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
status: notes
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

- [x] **Priority must be a number.** The field currently accepts any text. The hint is Chakra's
      `NumberInput`. Change `priority` to `number` in `ToDoItem` and let the compiler list every
      place that still assumes a string: the form state, the `onAdd` signature, and `handleAdd`.
- [x] **Sort button: order items by priority, lowest first.** Don't call `todoList.sort(…)` and
      pass the result to the setter. It sorts in place and returns the same reference, so React
      sees no change and doesn't re-render. Use `[...todoList].sort((a, b) => a.priority -
      b.priority)` or `todoList.toSorted(…)`. See the cheat sheet in
      [[Module 05 - React Basics#Treat state as read-only]].
- [x] **Entry field + button: delete every item with priority greater than N.** Priority 1 means
      "do first," so this keeps the most urgent items. A `filter` in `App.tsx`. The threshold input
      needs its own state.

> [!tip] Why the stable `key` matters here specifically
> `ToDoItemDisplay` copies its item into local state. Sorting and bulk-deleting both move items
> to new positions. Because the list is keyed by `item.key` rather than array index, each row
> keeps its own component and state as it moves. Swap in `ToDoListDisplayBad.tsx` (index keys)
> after sorting and you can watch rows show the wrong titles.

## What I Built

All three enhancements are done and work in the browser. Zipped for submission as
`week-3/Activity05-ToDoApp.zip`: the 8 files of `src/Examples/ToDoApp/`, including the new
`Shared/ToDoListDelete.tsx`.

The app's shape didn't change. `App` still owns the list, and the children still only report
events back up:

```
App.tsx                 owns todoList, itemKey; handleAdd, handleDelete,
 │                      sortByPriority, deleteLowerPriorityItems
 ├─ Sort button         calls sortByPriority(todoList)
 ├─ ToDoListDelete      owns threshold; calls onDeleteLowerPriority(threshold)   ← new
 ├─ ToDoItemEntryForm   owns title, priority; calls onAdd(title, priority)
 └─ ToDoListDisplay     draws items in the order it receives them
     └─ ToDoItemDisplay one row, keyed by item.key
```

### 1. Priority is a number

**What changed.** `ToDoItem.priority` went from `string` to `number`. The form's priority
`<Input>` became a Chakra `NumberInput` limited to 0–10. Its state starts at `0` and resets to
`0` after each add.

```tsx
<NumberInput value={priority} onChange={(_, n: number) => setPriority(n)} min={0} max={10}>
  <NumberInputField />
  <NumberInputStepper>
    <NumberIncrementStepper />
    <NumberDecrementStepper />
  </NumberInputStepper>
</NumberInput>
```

**What it means.** Chakra's `onChange` passes two arguments: the value as a string, then as a
number. `(_, n)` ignores the string and keeps the number, so the state never holds text.
`NumberInputField` is the box you type in, and `NumberInputStepper` adds the arrows.

**Why this way.**
- *I changed the type first and let the compiler find the rest.* After editing `ToDoItem`,
  TypeScript flagged every place that still assumed a string: the form state, the `onAdd`
  signature, and `handleAdd`. That's a complete to-do list instead of grepping and guessing.
- *`NumberInput` rather than `<Input type="number">`.* The plain HTML input still gives you a
  string in `event.target.value`, so you'd need `Number(...)` everywhere. Chakra hands over the
  number directly and enforces `min`/`max`.
- *A number is needed for sorting.* Strings sort letter by letter, so `"10"` would come before
  `"9"`. With numbers, `a.priority - b.priority` just works.

### 2. Sort button: lowest priority first

```tsx
function sortByPriority(list: ToDoItem[]): void {
  const newList = list.slice().sort((a, b) => a.priority - b.priority);
  setTodolist(newList);
}
...
<Button onClick={() => sortByPriority(todoList)}>Sort by Priority</Button>
```

**What it means.** `slice()` with no arguments copies the array. `sort` then reorders the copy.
The comparator returns a negative number when `a` should come first, so `a - b` gives
ascending order: priority 1 (do first) at the top.

**Why this way.**
- *Copy before sorting.* `.sort()` changes the array it's called on and returns that same
  array. `setTodolist(todoList.sort(...))` would pass React the same reference it already has.
  React compares by reference, sees no change and skips the re-render, and the state has been
  changed behind its back. `slice()`, `[...todoList]` and `toSorted()` all avoid this.
- *The `onClick` is an arrow function.* `onClick={sortByPriority(todoList)}` would sort during
  every render instead of on click.
- *Sorting the stored state vs. sorting only for display.* I sort the stored list once per
  click. The other option was to keep `todoList` in the order items were added and sort a copy
  each render behind an on/off toggle. The spec asks for "a sort button", so the one-shot
  version is the closest match and the simplest.
  - Tradeoff: items added after a sort go at the end, out of order, until you click again.
    You also can't get back the original order.

### 3. Delete every item with priority greater than N

New component `Shared/ToDoListDelete.tsx`:

```tsx
export function ToDoListDelete(props: { onDeleteLowerPriority: (threshold: number) => void }) {
  const [threshold, setThreshold] = React.useState<number>(0);

  function handleButtonPress() {
    props.onDeleteLowerPriority(threshold);
    setThreshold(0);
  }
  // Button + NumberInput (same pattern as the entry form)
}
```

In `App.tsx`:

```tsx
function deleteLowerPriorityItems(threshold: number): void {
  const newList = todoList.filter((item) => !(item.priority > threshold));
  setTodolist(newList);
}
...
<ToDoListDelete onDeleteLowerPriority={deleteLowerPriorityItems} />
```

**What it means.** `filter` builds a new array of the items for which the test is true. The
test keeps items whose priority is *not* greater than N, which is the same as removing those
greater than N. "Lower priority" in the button label means a bigger number, because 1 means
"do first".

**Why this way.**
- *The threshold lives in the child, the list lives in the parent.* State goes in the lowest
  component that needs it. Only the delete control cares about the number being typed, so
  `threshold` lives there. Only `App` can change `todoList`, so the filtering lives there.
  This copies `ToDoItemEntryForm`, which owns `title`/`priority` and only calls
  `onAdd(title, priority)`.
- *Data goes up through a callback.* A parent can't read a child's `useState`. The child gets
  the value up by **calling a function the parent passed down** and giving the value as the
  argument.
- *A separate component rather than more state in `App`.* `App` would otherwise hold
  `threshold` even though it only uses it at the moment of the click. Keeping it in the child
  keeps `App` about the list.
- *`!(p > N)` rather than `p <= N`.* Both are the same for real numbers. Writing it as "not
  greater than" matches the spec's wording, so it's easy to check against the spec.

> [!bug] The mistake I made, and what it taught me
> My first version was `onDeleteLowerPriority={deleteLowerPriorityItems(threshold)}`. Two things
> were wrong:
> 1. **`threshold` doesn't exist in `App`.** It's the child's state, and a parent can't reach
>    into a child.
> 2. **Parentheses call the function immediately, during render.** The prop received its return
>    value (`undefined`) instead of a function. Because the call also ran `setTodolist`, it
>    would trigger a re-render that calls it again, an infinite loop.
>
> The fix is to pass the function itself, `onDeleteLowerPriority={deleteLowerPriorityItems}`,
> and let the child call it with its own `threshold`. The test to apply: *does this prop need a
> function, and am I giving it one, or the result of calling one?*
>
> I also forgot `NumberInputField` at first, so only the stepper arrows rendered. There was no
> box to type in.

### Why stable keys keep this correct

Sorting and bulk delete are the first features that **move** rows. `ToDoItemDisplay` copies
`props.item` into its own `useState`, and that copy is only made when the row component is
first created. Because `ToDoListDisplay` uses `key={eachItem.key}`, React moves each row
component along with its item, so the copied state stays matched. With
`ToDoListDisplayBad.tsx` (`key={index}`), React would keep the components in place and only
change their props. The rows would keep showing their old titles in the new positions.

### Small cleanups along the way

- `handleDelete` now uses `!==` instead of `!=`: strict comparison, no type coercion.
- I removed the unused imports from `App.tsx` (`React`, `useEffect`, `Table`, `Th`, …).
- `src/main.tsx` now mounts the ToDo app instead of `SimpleClock`. That file is not submitted.

### Known limitations (not required by the spec)

- If you clear a `NumberInput`, Chakra passes `NaN`, so an item can be added with priority
  `NaN`. Guard with `Number.isNaN(n)` if it ever matters.
- Sort is a one-shot action, not a mode. See the tradeoff above.
- Changing `ToDoItem.priority` to `number` breaks `ToDoAppWithCustomHooks/useToDoItemList.ts`,
  which imports the same type and still passes a string. That example isn't part of this
  submission.

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
