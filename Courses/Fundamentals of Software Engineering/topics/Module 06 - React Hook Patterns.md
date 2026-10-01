---
tags:
  - software-engineering
  - northeastern
  - cs4530
  - react
  - frontend
  - tsx
  - hooks
  - ui-testing
  - module
type: lecture
course: "[[Fundamentals of Software Engineering]]"
module: 6
status: notes
---
# Module 06 — React Hook Patterns

> [!info] Source
> <https://neu-se.github.io/CS4530-Fall-2026/modules/6-patterns-of-react>

**Week 4** of [[Fundamentals of Software Engineering]]
**Slides**: `Module 06 React Hook Patterns` (pdf / pptx)

> [!danger] Important dates
> [[Team Formation Survey (tp1)]] due **Friday Oct 2, 5:00pm ET**
> [[Individual Project 2]] due **Wednesday Oct 7, 5:00pm ET**

## Learning Objectives

After this lecture you should be able to:

- [ ] Explain the basic uses of `useEffect`
- [ ] Explain when a `useEffect` is executed, and when its return value is executed
- [ ] Construct simple custom hooks and explain why they are useful
- [ ] Map the three core steps of a test (assemble, act, assess) to UI component testing

## Notes

> [!abstract] The one-sentence version
> [[Module 05 - React Basics|Module 05]] gave components state. This module connects them to
> everything *outside* React: **`useEffect`** subscribes on mount and cleans up on unmount,
> **custom hooks** pull that logic out of the display code, and **Playwright** tests the result in
> a real browser with the same AAA shape as unit tests.

### `useEffect` — synchronizing with an external system

`useEffect` is the mechanism for keeping a component in sync with an **external system**, meaning
any code that isn't inside your component: a timer, a socket or chat subscription, a fetch to an
API, an animation library, business logic that lives elsewhere.

```tsx
export default function ClockDisplay(props: ClockDisplayProps) {
	const clock = props.clock;
	const [localTime, setLocalTime] = useState(0);
	
	useEffect(() => {
		const listener1 = () => setLocalTime(time => time + 1)  // on first render: subscribe
		clock.addListener(listener1);
		
		return () => {clock.removeListener(listener1);};       // on dismount: unsubscribe
	}, []);                                                    // [] = first render only
}
```

Three parts to read off every `useEffect`:

| Part | Here | Meaning |
| --- | --- | --- |
| Body | `clock.addListener(listener1)` | What to do when the effect runs |
| Return value | `() => clock.removeListener(listener1)` | The **cleanup** |
| Dependency array | `[]` | **When** the effect runs |

Note the listener uses the functional setter, `time => time + 1` — the lesson from Module 05. The
listener fires long after this render, so a captured `localTime` would be stale.

### Worked example — the clock display

#### The props

```tsx
export interface ClockDisplayProps{
	name: string;
	key: number;
	clock: ITicker;
	handleDelete?: () => void;
	handleAdd?: () => void;
	noisyDelete?: boolean;
}
```

#### The component and its handlers

```tsx
import { useState, useEffect } from "react";
import { Box, Button, HStack, VStack } from "@chakra-ui/react";
import type { ClockDisplayProps } from "../types";

// this version simply imports a clock from its parent
export default function ClockDisplay(props: ClockDisplayProps) {
  const clock = props.clock;
  const [localTime, setLocalTime] = useState(0);

  useEffect(() => {
    const listener1 = () => {setLocalTime((localTime) => localTime + 1)};
    clock.addListener(listener1);
    return () => {
      clock.removeListener(listener1);
    };
  }, []);

  function handleStart() { clock.start(); }
  function handleStop() { clock.stop(); }
  function handleReset() { setLocalTime(0); }
  // ...display: name, time, listener count, Start/Stop/Reset buttons
```

`handleStart` and `handleStop` act on the **external** clock, while `handleReset` changes only
**local** state. Reset zeroes this display without touching the shared ticker.

#### Running it

```tsx
import { useState, useEffect } from "react";
import { type ITicker } from "../../Shared/types";
import Ticker from '../../Shared/Classes/Ticker'
import ClockDisplay from "../../Shared/Components/SimpleClockDisplay";

export default function App() {
  const [clock, _] = useState<ITicker>(new Ticker(1000));

  return (
   <ClockDisplay name="demo1" key={1} clock={clock} />
  )
}
```

> [!tip] Modularity pays off
> Because the clock comes in as a prop, the same `ClockDisplay` drops into a different parent
> unchanged — the slides' `ThreeClocks` app renders Clock A, B, and C all sharing one `Ticker`.
> That only works because the component was designed not to own its clock.

### Dependencies control execution

`useEffect` takes an optional **array of dependencies**. The effect runs only if one or more of
those values changed since the last render (e.g. because a setter was called).

| Dependency array | Effect runs |
| --- | --- |
| `[]` | Only on the **first render** |
| `[i]` | On first render, then whenever `i` changes |
| `[i, j]` | On first render, then whenever **either** `i` or `j` changes |
| *omitted* | On **every** render |

```tsx
export default function App() {
  const [i, setI] = useState(0);
  const [j, setJ] = useState(0);

  // runs only on first render.
  useEffect(() => {
    console.log('useEffect #1 is run only on first render');
  }, []);

  useEffect(() => {
    console.log('useEffect #2I is run when i changes');
  }, [i]);

  useEffect(() => {
    console.log('useEffect #2J is run when j changes');
  }, [j]);

  useEffect(() => {
    console.log('useEffect #2IJ is run when either i or j changes');
  }, [i,j]);

  // runs on every render
  useEffect(() => {
    console.log('useEffect #3 is called on every render');
  });

  function onClickI() {
    console.log('Clicked i!');
    setI(lastI => lastI+1);
    // bound variable name doesn't matter, of course
    // setI(i+1) is a bug, because value of i may not
    // be current.
  }

  function onClickJ() {
    console.log('Clicked j!');
    setJ(j => j+1);
  }

  return (
    <VStack>
      <Heading>useEffect demo #1IJ</Heading>
      <Text> i is {i} </Text>
      <Button onClick={onClickI}>Increment i</Button>
      <Text> j is {j} </Text>
      <Button onClick={onClickJ}>Increment j</Button>
    </VStack>
  );
}
```

### When the cleanup runs

The cleanup function runs **sometime before the next time the hook runs**. For the
first-render-only case (`[]`) there is no next time, so that means **when the component is
dismounted**.

> [!warning] Skip the cleanup and you leak
> Without `removeListener`, a deleted `ClockDisplay` stays subscribed to the ticker and keeps
> calling the setter of a component that no longer exists. The same goes for closing sockets and
> clearing intervals.

### Custom hooks

React lets you combine `useState` and `useEffect` into your own hooks. The payoff is
**separating business logic from display logic**: the component renders, the hook owns the state
and the rules for changing it.

```tsx
export default function useToDoItemList () {
  const [todoList,setTodolist] = useState<ToDoItem[]>([])
  const [itemKey,setItemKey] = useState<number>(0)   // first unused key

  function handleAdd (title:string, priority:string) {
    if (title === '') {return}   // ignore blank button presses
    setTodolist(todoList.concat({title: title, priority: priority, key: itemKey}))
    setItemKey(itemKey + 1)
  }

  function handleDelete(targetKey:number) {
    const newList = todoList.filter(item => item.key !== targetKey)
    setTodolist(newList)
  }

  return {todoList: todoList, handleAdd: handleAdd, handleDelete: handleDelete}
}
```

This is the ToDo app's state from Module 05, lifted out of the component. The component now just
calls `const { todoList, handleAdd, handleDelete } = useToDoItemList()`.

#### The rules of hooks

| Rule | Not allowed | Why |
| --- | --- | --- |
| 1. Only call hooks at the **top level** | Inside loops, conditions, or nested functions | React identifies hooks by call **order**, which must be the same on every render |
| 2. Only call hooks from **React components or custom hooks** | From helper functions or classes | React must know which component the hook call belongs to |

#### Other hooks

| Hook | Use |
| --- | --- |
| `useContext` | Share state between nested components without threading props |
| `useRef` | Hold a value that's not needed for rendering |
| `useEffectEvent` | Extract non-reactive logic from an Effect into a reusable function |

### Testing React components

**AAA still applies** — assemble, act, assess. What's new is that you need a **test double for
the React system**: render the components into a virtual DOM, or into a captive web browser. This
course uses **Playwright**, which drives a real browser (read the tutorial).

#### Playwright commands

| Command | Purpose |
| --- | --- |
| `.goto()` | Navigate to a URL |
| `.getByLabel()` | Find form elements by associated label text |
| `.getByRole()` | Find based on ARIA role (button, textbox, ...) |
| `.getByText()` | Find based on text content |
| `.waitForURL()` | Wait for navigation to complete to a specific URL |
| `.fill()` | Type text into an input field |

#### A typical test

```tsx
test('should allow an existing user to log in', async ({ page }) => {
  await page.goto('/login');

  await page.getByLabel('Username') 
   .fill("Frau Drei"); // Assemble

  await page.getByLabel('Password',
  { exact: true }).fill(password); // Act

  await page.getByRole('button',
  { name: 'Log In' }).click(); // Act

  await page.waitForURL('/');
  await expect(page.getByText
  ('signed in as Frau Drei')).toBeVisible(); // Assess
});
```

Locators find elements the way a **user** would — by label, role, and visible text — not by CSS
class or component internals. That keeps the test tied to behavior rather than implementation.

> [!note] Keep E2E tests few
> End-to-end tests take a long time. They should be roughly **5%** of a full project's suite.

## Key Takeaways

- `useEffect` syncs a component with an **external system**. Body = subscribe, return value =
  cleanup, dependency array = when.
- `[]` runs once, `[a, b]` runs when `a` or `b` changes, no array runs every render.
- Cleanup runs **before the effect's next run**, or on **dismount** for `[]`. Always undo what the
  effect did — listeners, sockets, intervals.
- Callbacks that fire later (listeners, timers) must use the **functional setter**, or they read
  stale state.
- **Custom hooks** move business logic out of display components. Two rules: top level only, and
  only from components or other hooks.
- UI tests are still **AAA**. Playwright locators work by label, role, and text, the way a user
  finds things. Keep E2E to ~5% of the suite.

## Questions / Gaps

- **`key` in `ClockDisplayProps`.** React reserves `key` — it's consumed by reconciliation and is
  **not** passed through to the component, so `props.key` is always `undefined`. Declaring it in
  the props interface is misleading.
- `useState<ITicker>(new Ticker(1000))` constructs a new `Ticker` on **every** render and throws
  all but the first away. The lazy form `useState(() => new Ticker(1000))` builds it once.
- `ClockDisplay`'s effect uses `clock` but declares `[]`, so it won't re-subscribe if the parent
  swaps in a different clock. The `react-hooks/exhaustive-deps` lint rule would flag it —
  `[clock]` is the correct array.
- `useToDoItemList` still uses `setTodolist(todoList.concat(...))` and `setItemKey(itemKey + 1)`,
  the non-functional setters that Module 05 and the `onClickI` comment above both call a bug. The
  Module 05 slides' version of the ToDo app does use `itemKey => itemKey + 1`.
- In the Playwright example, filling the username is labelled *Assemble* and filling the password
  *Act*. Arguably both fields are assembly, and only the click is the act.

## Slides

| Deck | PDF | PPT |
| --- | --- | --- |
| Module 06 — React Hook Patterns | [PDF](https://neu-se.github.io/CS4530-Fall-2026/Slides/Module%2006%20React%20Hook%20Patterns.pdf) | [PPT](https://neu-se.github.io/CS4530-Fall-2026/Slides/Module%2006%20React%20Hook%20Patterns.pptx) |

Additional content: [modules/6-patterns-of-react](https://neu-se.github.io/CS4530-Fall-2026/modules/6-patterns-of-react)

## Resources

- [Code examples from lecture](https://github.com/mwand/M05-M06-React-Examples-Fall-2026)
- [React reference for `useEffect`](https://react.dev/reference/react/useEffect)
- [Working with Playwright testing](https://playwright.dev/docs/intro)
- [How to fetch data with React](https://www.robinwieruch.de/react-hooks-fetch-data/)
- Tutorial: [UI Testing with Playwright](https://neu-se.github.io/CS4530-Fall-2026/tutorials/week3-uitesting)

## Related

- [[Module 05 - React Basics]] — components, props, state, and the functional-setter rule
- [[Tutorial - React Basics]]
- [[Tutorial - Unit Testing with Vitest]] — AAA, which carries over to UI tests
- [[Individual Project 2]]
- [[CS4530 Course Schedule]]
