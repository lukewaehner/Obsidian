---
tags:
  - software-engineering
  - northeastern
  - cs4530
  - react
  - frontend
  - tsx
  - module
type: lecture
course: "[[Fundamentals of Software Engineering]]"
module: 5
status: notes
---
# Module 05 — React Basics

> [!info] Source
> <https://neu-se.github.io/CS4530-Fall-2026/modules/5-react>

**Week 3** of [[Fundamentals of Software Engineering]]
**Slides**: `Module 05 React Basics` (pdf / pptx)

> [!danger] Important date
> [[Individual Project 2]] due **Wednesday Oct 7, 5:00pm ET**

## Learning Objectives

After this lecture you should be able to:

- [ ] Understand basic React concepts: components, props, and state
- [ ] Explain how a React component communicates with its parent and with its children
- [ ] Explain what happens when a React component updates its state
- [ ] Explain when a React component will be redisplayed
- [ ] Create simple React components that use state and properties

## Notes

> [!abstract] The one-sentence version
> [[Module 04 - Design Patterns for Web Applications|Module 04]] built the server; this is the
> client. A React app is a **tree of components**, each holding its own **state** and receiving
> **props** from its parent — and React re-renders a component whenever that state changes. Props
> flow down, handler calls flow up.

### Why components

Rich web UIs share a handful of properties, and each one motivates part of React's design:

| UI property | Example | What it demands |
| --- | --- | --- |
| Widgets have both visual presentation **and** logic | A like button looks a certain way and talks to the server | Bundle logic + presentation together |
| Some widgets occur more than once | Comment/like widgets on every post | Reusable units |
| Changes to data should change the widget | New images and comments show up in real time | Presentation synced to state |
| Widgets are hierarchical | The like button lives inside a post | A tree |
| Action on one widget may affect others | Clicking 'like' runs its own logic, and may update the post containing it | A way for children to tell parents |

A **component** represents a widget in object-like style. It organizes related logic and
presentation into a single unit:

- the **state** it needs, plus the logic for updating that state
- the **presentation** that renders that state into HTML
- and it keeps the two **synchronized** — whenever state changes, the HTML is rendered again

> [!example] The like button as a component
> | Question | Answer |
> | --- | --- |
> | What does it keep track of? | Whether it's liked, and which post it's associated with |
> | What logic does it have? | When the like status changes, send an update to the server |
> | How does it look? | Filled in if liked, hollow if not |

### React

A framework for components, created by Facebook. Components are constructed in the browser (the
"front-end"). Three key ideas:

1. **Embed HTML in TypeScript**
2. **Track application "state"**
3. **Automatically re-render** the page based on changes to state

**ChakraUI** is the component library used in this course — prebuilt components (`VStack`,
`Heading`, `Button`, ...) with a high level of accessibility support.

### TSX — HTML inside TypeScript

JavaScript/TypeScript is extended into **JSX/TSX**: the same language, with the extra feature that
some expressions may be HTML. HTML becomes an expression, gets syntax-checked, and `{ expr }`
drops back into TypeScript to evaluate a value.

```tsx
export function HelloMessage(props: IProps) {
	return (
	<div>
		Hello, {props.name}
	</div>
	)
}

ReactDOM.render(
<React.StrictMode>
	<HelloMessage name='Bob' />
</React.StrictMode>,
document.getElementById('root')
);
```

Browsers don't run TSX natively, so build tools compile it to JavaScript. The course version with
Chakra:

```tsx
import * as React from 'react';
import { Heading, VStack } from '@chakra-ui/react';

export default function HelloWorld() {
	return (
		<VStack>
			<Heading>Hello World</Heading>
		</VStack>
	);
}
```

> [!tip] Running the examples
> `npm run dev` in the examples repo, then open the URL Vite prints. Pick which app renders in
> `src/main.tsx`.

### Components are little machines

| A component... | |
| --- | --- |
| starts with input from its parent | **props** |
| has additional local state | **component state** |
| retains its local state when its parent's state changes | |
| may change its local state in response to external stimuli | button presses, etc. |
| re-renders when its local state changes, or when its parent re-creates it with different props | |

> [!note] Best practice
> Keep most of the state in the **parent** component.

### State

- State is created by **`useState`**
- It's accessed through **state variables** — the first is the accessor, the second the setter
- The **only** way to change a state variable is with its setter
- In general, a component's state is several variables
- Naming convention for this class: `goodVariableName`, `setGoodVariableName`

```tsx
export default function SimplestState() {
	const [count, setCount] = useState(0)
	
	function handleClick() { setCount(count + 1)}
	
	return (
		<VStack>
			<Box> count = {count} </Box>
			<Button onClick={handleClick} >
				Increment Count!
			</Button>
		</VStack>
	)
}
```

#### Components don't change state directly

1. A setter is just a **callback** — a request to React
2. Every so often, React collects all the set requests since the last redisplay, sort of like a
   queue
3. React executes all the outstanding set requests, emptying the queue
4. React redisplays the component with the new state

#### Setters are not synchronous

A setter doesn't change the state immediately; it's a request to update the state when the
component is redisplayed. So:

```tsx
function handleClick() {
	setCount( count + 1 )
	setCount( count + 1 )
	setCount( count + 1 )
}
```

> [!bug] This only adds one
> `count` is the value from *this* render, so all three calls request the same thing. The slides
> put it as "the same as saying `setCount(2)` three times" (i.e. starting from 1).
>
> Pass the setter a **function** instead — React is guaranteed to apply the transformation three
> times:
>
> ```tsx
> setCount(count => count + 1)
> ```

### The component tree

- Each component has a **single parent** (except the root)
- A component may have **children**, which are other components
- A component initializes its children by passing them **props**

#### Props flow down

Parents pass properties to children **by name**:

```tsx
import HelloWorldWithName from "./HelloWorldWithName";
import { VStack } from "@chakra-ui/react";

export default function HelloWorldWithAveryAndDave() {
  return (
    <VStack>
      <HelloWorldWithName name="Avery" />
      <HelloWorldWithName name="Dave" />
    </VStack>
  );
}
```

The child receives them as a single **record** argument, and **cannot change them**:

```tsx
export default function HelloWorldWithName(
	props: { name: string }
) {
return (
	<VStack>
		<Heading>Hello, {props.name}!</Heading>
	</VStack>
	);
}
```

#### Handler calls flow up

A child talks to its parent by calling a **handler the parent passed in as a prop**. From the
`TwoCountingButtons` example in the slides — each button keeps its own `localCount`, and also
calls `props.onClick()` so the parent can bump `globalCount`:

```tsx
function handleClick() {
	setLocalCount(localCount + 1);
	props.onClick(); // propagate to parent
}
```

### Redisplay

Setters kick off redisplay. After running the queued set requests, React rebuilds components from
the root down. A component that's **being redisplayed** keeps its (possibly updated) state from
before. A component **displayed for the first time** gets fresh state from `useState`'s initial
value.

Redisplay is fast because updating the browser DOM is slow, and React avoids doing it wholesale.
**Reconciliation** diffs the new tree against the old and only updates the parts that changed —
adding a YouTube comment shouldn't re-lay out the whole page.

### Lists with `map`

To display a list, `map` each item to a component:

```tsx
export function ToDoListDisplay(props: { items: ToDoItem[],
                                         onDelete:(id:string) => void }) {
  return (
    <Table>
      <Tbody>
        {props.items.map((eachItem) =>
          <ToDoItemDisplay item={eachItem}
            key={eachItem.id}
            onDelete={props.onDelete} />)}
      </Tbody>
    </Table>
  )
}
```

> [!important] Give every list item a unique `key`
> When you remove an item, React needs to know **which** one to target. Without stable keys,
> reconciliation can't match old items to new ones.

## Key Takeaways

- A **component** bundles a widget's state, logic, and presentation, and keeps HTML in sync with
  state.
- **TSX** is TypeScript where HTML is an expression; `{ }` drops back into TypeScript.
- **Props** come from the parent and are read-only. **State** is local, created by `useState`,
  and changed *only* through its setter.
- Setters are **asynchronous requests**, batched and applied before the next redisplay. Use the
  functional form `setX(x => ...)` whenever the new value depends on the old one.
- Data flows **down** as props; events flow **up** through handlers the parent passed in.
- React re-renders a component when its **state changes** or its parent re-creates it with **new
  props**. Reconciliation keeps that cheap.
- Lists from `map` need a **unique `key`** per item.

## Questions / Gaps

- `ReactDOM.render(...)` is the pre-React-18 API — current React uses
  `createRoot(document.getElementById('root')).render(...)`. The examples repo hides this behind a
  `Root()` component in `src/main.tsx`; check which one it calls.
- The slides' "same as `setCount(2)` three times" only holds if `count` starts at 1. The general
  rule: three calls with a stale `count` set it to `count + 1`, once.
- The ToDo app in the slides still calls `setTodolist(todoList.concat(...))` — the non-functional
  form this lecture warns about. It works for a single click, but would break under batching.
  [[Activity 05 - Enhancing a TODO Tracker in React]] builds on that code.

## Activity

[[Activity 05 - Enhancing a TODO Tracker in React]]

## Slides

| Deck | PDF | PPT |
| --- | --- | --- |
| Module 05 — React Basics | [PDF](https://neu-se.github.io/CS4530-Fall-2026/Slides/Module%2005%20React%20Basics.pdf) | [PPT](https://neu-se.github.io/CS4530-Fall-2026/Slides/Module%2005%20React%20Basics.pptx) |

Additional content: [modules/5-react](https://neu-se.github.io/CS4530-Fall-2026/modules/5-react)

## Resources

- [Code examples from slides](https://github.com/mwand/M05-M06-React-Examples-Fall-2026)
- [Official documentation for React](https://reactjs.org)
- [Official tutorial materials on React](https://react.dev/learn) (exhaustive, but really good)
- [Updating objects in state](https://react.dev/learn/updating-objects-in-state)
- [Updating arrays in state](https://react.dev/learn/updating-arrays-in-state)
- [More about rendering](https://react.dev/learn/render-and-commit)
- [Lazy loading components](https://react.dev/reference/react/lazy)

## Related

- [[Module 04 - Design Patterns for Web Applications]] — the server this client talks to
- [[Module 06 - React Hook Patterns]] — `useEffect`, custom hooks, UI testing
- [[Tutorial - React Basics]]
- [[Individual Project 2]]
- [[CS4530 Course Schedule]]
