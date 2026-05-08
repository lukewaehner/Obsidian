---
tags:
  - react
  - javascript
type: moc
related:
  - "[[Code]]"
  - "[[JavaScript]]"
---
# React

Component-based UI library. Renders components when state changes.

## Core Concepts

- [[Components]] — JSX, functional components, lists, fragments, portals
- [[Props]] — Passing data down, children, spread, prop drilling
- [[State]] — useState, functional updates, derived state, lifting state

## Hooks

- [[Effects]] — useEffect, cleanup, data fetching, what not to put in effects
- [[Hooks]] — useReducer, useRef, useCallback, useMemo, useId, useTransition
- [[Context]] — createContext, useContext, provider pattern, when to use
- [[Custom Hooks]] — Reusable logic: useDebounce, useLocalStorage, useFetch

## Patterns and Architecture

- [[Patterns]] — Compound components, HOC, controlled components, error boundaries
- [[Forms]] — Controlled vs uncontrolled, validation, React Hook Form
- [[Performance]] — React.memo, useMemo, useCallback, code splitting, profiling

## Production

- [[Data Fetching]] — React Query, SWR, optimistic updates, Suspense
- [[Routing]] — React Router v6, params, nested routes, protected routes
- [[Tooling]] — Vite, Next.js, TypeScript, testing, ESLint, common libraries

## Quick Reference

```jsx
// Component
function Card({ title, children }) {
  return <div className="card"><h2>{title}</h2>{children}</div>;
}

// State
const [count, setCount] = useState(0);
setCount(prev => prev + 1);  // use functional update when depending on prev

// Effect with cleanup
useEffect(() => {
  const sub = subscribe(userId);
  return () => sub.unsubscribe();
}, [userId]);

// Context
const ctx = useContext(MyContext);

// Memoization
const result = useMemo(() => expensive(data), [data]);
const fn = useCallback(() => doThing(id), [id]);
const MemoChild = React.memo(Child);
```

```folder-overview
id: 0982c5aa-9fec-4397-a26a-1f10da4ead41
folderPath: Code/React
title: "{{folderName}} overview"
showTitle: false
depth: 1
includeTypes:
  - folder
  - markdown
style: list
disableFileTag: false
sortBy: name
sortByAsc: true
showEmptyFolders: false
onlyIncludeSubfolders: false
storeFolderCondition: true
showFolderNotes: false
disableCollapseIcon: true
alwaysCollapse: false
autoSync: true
allowDragAndDrop: true
hideLinkList: true
hideFolderOverview: false
useActualLinks: true
fmtpIntegration: false
titleSize: 1
isInCallout: false
useWikilinks: true
```
<span class="fv-link-list-start" id="0982c5aa-9fec-4397-a26a-1f10da4ead41"></span>
- [[Code/React/Components.md|Components]] <span class="fv-link-list-item"></span>
- [[Code/React/Context.md|Context]] <span class="fv-link-list-item"></span>
- [[Code/React/Custom Hooks.md|Custom Hooks]] <span class="fv-link-list-item"></span>
- [[Code/React/Data Fetching.md|Data Fetching]] <span class="fv-link-list-item"></span>
- [[Code/React/Effects.md|Effects]] <span class="fv-link-list-item"></span>
- [[Code/React/Forms.md|Forms]] <span class="fv-link-list-item"></span>
- [[Code/React/Hooks.md|Hooks]] <span class="fv-link-list-item"></span>
- [[Code/React/Patterns.md|Patterns]] <span class="fv-link-list-item"></span>
- [[Code/React/Performance.md|Performance]] <span class="fv-link-list-item"></span>
- [[Code/React/Props.md|Props]] <span class="fv-link-list-item"></span>
- [[Code/React/Routing.md|Routing]] <span class="fv-link-list-item"></span>
- [[Code/React/State.md|State]] <span class="fv-link-list-item"></span>
- [[Code/React/Tooling.md|Tooling]] <span class="fv-link-list-item"></span>
<span class="fv-link-list-end" id="0982c5aa-9fec-4397-a26a-1f10da4ead41"></span>
