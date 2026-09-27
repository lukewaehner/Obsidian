---
tags:
  - assignment
  - software-engineering
  - northeastern
  - cs4530
  - typescript
  - react
type: assignment
course: "[[Fundamentals of Software Engineering]]"
due: 2026-10-07
date: 2026-09-09
status: raw
---

# Individual Project 2

> [!danger] Due Wed 2026-10-07 · submit code through Pawtograder · 100 points
> [Open in Canvas](https://northeastern.instructure.com/courses/260680/assignments/3510209).
> Canvas lists the deadline as **1:00 PM ET**; the syllabus says 5:00 PM. Canvas stored IP1 the
> same way, so this is probably a timezone slip, but nobody has confirmed it. **Push the final
> version by 1:00 PM.** Late: 10% off within 24 hours, zero after.

Part of [[Fundamentals of Software Engineering]]. Published on Canvas 2026-09-27; changelog "NA"
as of then.

> [!note] Canvas shows 0 points
> The Canvas assignment is in the "Individual Projects / Assignments" group (30% of the final
> grade) but carries `0.0 pts`. The spec itself totals 100 points, and the syllabus weights the
> three individual projects equally. Canvas's point value is most likely a placeholder. Treat this
> as a full individual project, not ungraded work.

- [ ] Individual Project 2 📅 2026-10-07

## The Premise

Back on the Game Nite team. IP1 was server-side; this one is the **frontend**: TypeScript and
React features in the client, plus one server-side rule change in Task 5.

**Objectives**: investigate and understand a large existing codebase · implement interactive web
applications with React. Rehearsed by [[Activity 05 - Enhancing a TODO Tracker in React]].

## 1. Getting Started

Accept the assignment in Pawtograder
([pawtograder.khoury.northeastern.edu](https://pawtograder.khoury.northeastern.edu), **Continue
with Microsoft**). It creates your repo with the starter code. Account setup is the same as
[[Individual Project 1#Pawtograder Setup]]. Then `npm install` at the root. That covers
`client`, `server`, and `shared`.

### Optional but recommended: MongoDB

The starter uses a real repository layer (MongoDB through the [Keyv](https://keyv.org/) adapter),
so with Mongo running, restarting the server no longer wipes the app's state.

1. Install MongoDB Community Edition from the official docs (macOS: run it as a service), plus
   **MongoDB Compass** pointed at `mongodb://localhost:27017`. `mongosh` comes with the macOS
   install; `show dbs` confirms the server is up.
2. Create `server/.env`. The leading dot matters:

   ```
   MONGO_STR=mongodb://127.0.0.1:27017
   MONGO_DB_NAME=GameNiteLocalDev
   ```

3. Run the two halves in separate terminals:

   ```
   ip2-me $> npm run dev -w=server
   ip2-me $> npm run dev -w=client
   ```

## 2. Working Recommendations

- Keep frontend and backend running with the app open in a browser while you work.
- Commit often. **Tasks 1–3 are cumulative, and so are Tasks 4–5.** You'll want a clean Task 4
  commit to fall back to if Task 5 goes badly.
- Run `npm run lint` and `npm run check` early, not at the deadline.
- Follow [[CS4530 Scientific Debugging]].
- Task 5 is the hardest and is worth only 24%. Start it early if you mean to finish it.

## 3. Submission

Push to **`main`**. Only commits visible on `main` count. Grades come back on Canvas.

### Files You May Not Modify

`package.json` · `.prettierrc` · `tsconfig.json` · `vitest.config.mjs` · `vite.config.mjs` ·
everything in `.github/`. The feedback PR must show no changes to them. No `eslint-disable`
comments in the final submission.

### CI

```
ip2-me $> npm run prettier --workspaces
ip2-me $> npm run check --workspaces
ip2-me $> npm run lint --workspaces
ip2-me $> npm run test --workspaces
```

> [!warning] CI deductions, same as IP1
> Up to **25%** off for CI failures: 5% Prettier, 10% TypeScript, 10% ESLint. In severe cases
> staff may decline to grade at all. IP2 adds `prettier` to the check list, which IP1's did not
> include. Run it.

## 4. Implementation Tasks

### Task 1 — Navigating to Other Profiles · 10 pts

In `client/src/components/MessageList.tsx`, make a chat message's display name a `<NavLink>` to
`/profile/<theirusername>`. For example, logged in as `user0`, a message from "Yāo" (`user1`)
links to `/profile/user1`. Graded on the navigation working.

### Task 2 — Viewing Other Profiles · 25 pts

In `client/src/pages/Profile.tsx`: at `/profile/user1` while logged in as `user0`, show that
user's **username, display name, and account creation time**, read-only. Your own profile stays
editable.

- 10 pts — functionality
- 15 pts — **refactoring into multiple files** with good style. The route now serves two purposes
  (edit mine, view theirs), so split the page into two or three files.

`client/src/services/userService.ts` has a helper for fetching another user.

### Task 3 — More Profile Navigation · 15 pts

Display names appear in five more places:

| Where | Text |
| --- | --- |
| Chat | "(DisplayName) entered chat" |
| Game panel | "Player #2 is (DisplayName)" |
| Forum posts | "Posted by (DisplayName)" |
| Forum comments | "Reply by (DisplayName)" |
| Home, game list, forum list | "(DisplayName) created 1 day ago" |

Make two changes in every location:

1. Refer to the logged-in user as **"you"** instead of by display name. The header's "signed in
   as (DisplayName)" is the one exception; leave it alone.
2. Link **other** users' names to their profile. "You" does not link.

1 pt per change per location (10), plus **5 pts for organizing the code to minimize
duplication**. Five call sites doing the same you-or-link logic is the reason to write one shared
component.

### Task 4 — Checkers Frontend · 26 pts

The backend is done (`shared/src/games/checkers.types.ts`, `server/src/games/checkers.ts`,
`server/tests/games/checkers.spec.ts`). Write `client/src/games/CheckersGame.tsx` from scratch.

Starter rules: 8×8 board; red (player 1) starts on rows 5–7, black (player 2) on rows 0–2; pieces
sit only on dark squares (`row + col` odd); any piece moves one square in any of the four
diagonals; capture by jumping an adjacent enemy into the empty square beyond; **captures are
mandatory**; a player with no legal moves loses.

Conditions of satisfaction, 2 pts each unless marked:

- [ ] 8×8 grid; dark squares (`(row + col) % 2 === 1`) visibly differ from light
- [ ] Red and black pieces visually distinct; empty squares show nothing
- [ ] Current player's name, or "your turn" for the viewer, shown near the board
- [ ] Watchers: every square `cursor: default`, clicks never send a move
- [ ] On your turn with the game live: your pieces `cursor: pointer`; clicking a piece with no legal moves does nothing
- [ ] **(3)** Clicking your piece that has legal moves selects it, visibly highlighted
- [ ] With a piece selected, its legal destinations are highlighted
- [ ] **(3)** Clicking a highlighted destination submits `{ from: [fromRow, fromCol], to: [toRow, toCol] }`
- [ ] Selection clears after submitting
- [ ] Game over: all squares `cursor: default`, clicks send nothing
- [ ] Game over: winner message. Watchers see "Red wins!" / "Black wins!", players see "You won!" / "You lost!"
- [ ] Clicking an opponent's piece or a non-highlighted dark square deselects

No need to handle `"RK"` / `"BK"` yet. Visual style is free, but a TA must be able to test every
condition.

### Task 5 — Kings and Multi-Captures · 24 pts

Changes across all four Checkers files: types, server logic, server tests, and the frontend.

**New rules**

- Regular pieces move and capture **forward only**: red toward row 0, black toward row 7.
- Reaching the far back rank (row 0 for red, row 7 for black) promotes to a king: `"RK"` / `"BK"`.
- Kings move and capture in all four diagonals.
- After a **king** captures, if another capture is available from its new square, it must keep
  capturing until none remain. A regular piece captures once and its turn ends, even if a second
  jump is geometrically possible.

**New move format.** `{ from, to }` becomes `{ squares: [[r0,c0], [r1,c1], …, [rN,cN]] }`. A
simple move has two squares, and a chain has three or more. Update the Zod validator
`zCheckersMove` to match. The server's `viewAs()` exposes `legalMoves` as complete square
sequences, and the frontend should submit those sequences whole.

Conditions of satisfaction:

1. Promotion on the back rank; kings displayed distinctly (e.g. ♛)
2. `CheckersMove` uses `squares: [number, number][]`; `zCheckersMove` updated
3. Wrong-direction moves by regular pieces rejected by the server
4. Kings move and capture in all four directions
5. Server generates multi-step legal moves for a capturing king; the king must continue
6. Regular pieces limited to one capture per turn
7. All pieces captured along a chain are removed
8. Frontend submits the full sequence when `legalMoves` holds one longer than two squares
9. Existing tests in `checkers.spec.ts` updated for the new rules (e.g. the "moves in all four
   directions" test no longer holds for regular pieces), plus new tests reaching **≥95% line and
   branch coverage** of `server/src/games/checkers.ts`: promotion, forward-only, king movement,
   multi-capture

| Points | Conditions |
| --- | --- |
| 6 | 1–3 promotion and forward-only |
| 8 | 4–7 king movement and multi-capture server logic |
| 4 | 8 frontend |
| 4 | 9 tests at ≥95% coverage |
| 2 | Code style and documentation |

> [!tip] Where the Task 4 → 5 break happens
> Task 5 changes the move type that Task 4's frontend submits. Commit Task 4 working first, then
> change the type and let `npm run check` list every call site. See
> [[Tutorial - TypeScript Basics]].

## 5. Grading Summary

| Task | Points |
| --- | --- |
| 1 — Chat profile links | 10 |
| 2 — Viewing other profiles | 25 |
| 3 — "You" and profile links everywhere | 15 |
| 4 — Checkers frontend | 26 |
| 5 — Kings and multi-captures | 24 |
| **Total** | **100** |

## Notes While Working


## Related

- [[Individual Project 1]]
- [[Module 05 - React Basics]]
- [[Tutorial - React Basics]]
- [[Activity 05 - Enhancing a TODO Tracker in React]]
- [[CS4530 Code Style Guide]]
- [[CS4530 Scientific Debugging]]
- [[Fundamentals of Software Engineering]]
