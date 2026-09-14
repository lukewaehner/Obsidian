---
tags:
  - software-engineering
  - northeastern
  - cs4530
  - typescript
  - testing
  - assignment
type: assignment
course: "[[Fundamentals of Software Engineering]]"
due: 2026-09-23
status: raw
---
# Individual Project 1

> [!danger] Due Wednesday 2026-09-23, 5:00pm ET · submit code through Pawtograder · 100 points

Part of [[Fundamentals of Software Engineering]]. Changelog on the course site: *no changes yet* as of 2026-09-09.

- [ ] Individual Project 1 📅 2026-09-23

## The Premise

You are the most recent hire at **GameNite**, an interactive application for people who like playing — or commenting on — multiplayer strategy games. It got a large investment on the elevator pitch: *"what if we had a version of Twitch, but for correspondence chess?"*

GameNite is a web app with code running in each client's browser and code running on a server. This first project is about getting up to speed on the existing codebase and dev environment; no prior web development experience is assumed.

**Objectives**: get familiar with TypeScript, VS Code, and the codebase · understand how REST API requests work · read and write TypeScript · write unit tests with Vitest · translate high-level requirements into code.

## 1. Getting Started

### Pawtograder Setup

Pawtograder is the course platform for individual projects and the final group project. See the [Pawtograder Student Guide](https://docs.pawtograder.com/students/intro) for screenshots.

1. Log in at [khoury.pawtograder.com](https://pawtograder.khoury.northeastern.edu) with Northeastern credentials — click **Continue with Microsoft**
2. Connect your GitHub account — **Sign in with GitHub** and authorize Pawtograder
3. Accept the organization invitation — **Open GitHub Organization Invitation**

- Already have a GitHub account? Use it, so coursework stays on your profile if you later make repos public.
- Linked Pawtograder to GitHub in CS2100/CS3100? You still need to enroll in the CS4530 GitHub org (skip step 2).
- Course not showing up? Enrollments sync hourly. Wait an hour, then contact your instructor.
- Created your repo before the semester started? **Sync it by accepting the pull request** Pawtograder opened.

### Prerequisites

Set up [[Tutorial - Development Environment Setup]] (Node.js and npm), then clone the starter code. The repo is three directories — `client`, `server`, `shared` — wired together as a single [npm workspace](https://docs.npmjs.com/cli/v7/using-npm/workspaces). New to Git? Read [[Tutorial - Git and GitHub Basics]] first; all students are expected to manage add/commit/push.

```
ip1-me $> npm install

ip1-me $> cd server
server $> npm run dev
# visit http://localhost:8000 — you should see a message pointing you at the Vite frontend
# LEAVE THIS RUNNING

# in a NEW terminal:
ip1-me $> cd client
client $> npm run dev
# probably http://localhost:4530/
```

A login page means you're up. Create a user or use the four auto-created accounts:

| Username | Password |
| --- | --- |
| `user0` | `pwd0000` |
| `user1` | `pwd1111` |
| `user2` | `pwd2222` |
| `user3` | `pwd3333` |

### Architecture

**The server** — TypeScript on [Express](https://expressjs.com/), used only to send and receive JSON (line 19 of `server/src/app.ts` configures that).

- **HTTP GET** — what your browser sends when you type a URL. Visiting <http://localhost:8000/api/thread/list> dumps JSON. Line 37 of `app.ts` routes that to the `getList` controller in `server/src/controllers/thread.controller.ts`. **GET must never change state** — no adding comments, creating posts, or initializing games.
- **HTTP POST** — sends information and may change state. Line 36 of `app.ts` routes `/api/thread/create` to `postCreate` in the same controller.

  ```bash
  curl --location 'localhost:8000/api/thread/create' \
  --header 'Content-Type: application/json' \
  --data '{
      "auth": {
          "username": "user3",
          "password": "pwd3333"
      },
      "payload": {
          "title": "New Post",
          "text": "Text goes here"
      }
  }'
  ```

**The client** — TypeScript meant to run in a browser. Browsers only run JavaScript, so GameNite uses [Vite](https://vite.dev/) as its build tool, both for previewing during development and for producing the shippable site.

**Shared code** — types in `shared/` used by *both* sides. The POST body above has type `WithAuth<CreateThreadMessage>`, which (see `shared/src/auth.types.ts` and `shared/src/thread.types.ts`) expands to:

```typescript
type TypeOfPostRequest = {
  auth: {
    username: string;
    password: string;
  };
  payload: {
    title: string;
    text: string;
  };
}
```

These are described with [zod](https://zod.dev/) schema validators, so the client uses them for compile-time safety and the server uses **the same code** to validate at runtime. As the cURL example shows, anyone can send the server arbitrary nonsense — **the server can't trust the structure of anything it receives**.

**Testing** — server unit tests live in `server/tests/**/*.spec.ts`, written in [Vitest](https://vitest.dev/) (near-identical to Jest). Run `npm run test` in `server`, or `npm run vitest` to re-run continuously on save.

## 2. Working Recommendations

1. Open the client in a browser and interact with it while watching the **Network** tab in devtools. The request URIs teach you the server's endpoints.
2. Set up VS Code with ESLint, TypeScript, and Prettier per the tutorial. The ESLint config is strict — without in-editor feedback you will face an avalanche of errors the first time you lint.
3. Do not wait until the last minute to run `npm run lint` and `npm run build`.
4. Follow [[CS4530 Scientific Debugging]].
5. Commit frequently, so you can get back to a working state.

## 3. Submission

Push the final version to the `main` branch of your repo — **only `main`** for this assignment. Written responses and cURL commands from Task 3 go in `responses.md` in your repo. Grades and feedback come back through Canvas.

### Files You May Not Modify

`package.json` · `package-lock.json` · `.prettierrc` · `tsconfig.json` · `vitest.config.mjs` · `vite.config.mjs` · everything in `.github/`

The feedback PR's diff should show **no changes to these files**. You also may not use `eslint-disable` comments in your final submission.

### CI

```
ip1-me $> npm run check --workspaces
ip1-me $> npm run lint --workspaces
ip1-me $> npm run test --workspaces
```

The status icon by your commit goes yellow → red ❌ or green ✅. Previous runs are under the **Actions** tab. **If your action run fails to complete, your code is not submitted.** After submitting, check Autograder feedback via *Test Assignment → click on commit*.

> [!warning] CI deductions
> Up to **25%** of the total grade may be deducted for CI failures — 5% prettier, 10% TypeScript, 10% ESLint. In severe cases staff may decline to grade the assignment at all. ESLint *warnings* don't fail CI and aren't automatically penalized, but leaving lots of `console` statements around is bad practice and can cost points if it makes your code hard for a TA to read.

## 4. Implementation Tasks

### Task 1 — Connect4 · 25 pts

Start a game of Connect4 in the dev server (log in as two different users in two windows). Other games work; Connect4 does not. Fill in the missing implementation in `server/src/games/connect4.ts`.

Where to look:

| File | What it gives you |
| --- | --- |
| `server/src/games/gameLogic.ts` | The type specification — what each unimplemented function does |
| `shared/src/games/connect4.types.ts` | Detailed intent for how the game works |
| `server/src/games/` (Nim, Guessing Game) | Working implementations to compare against |
| `server/src/games/connect4.spec.ts` | Provided tests — reason about expected behavior from these |

Reference implementation: <https://summer-26-gamenite.onrender.com/> (create an account or two).

**Until the game is implemented the given tests fail. You must get all of them to pass. You may add new tests but you may not change existing ones.**

- 15 pts — automatic, from passing the test suite
- 10 pts — manual TA review for [[CS4530 Code Style Guide|code style]]; document any helper functions you add

### Task 2 — Tests for Tic-Tac-Toe · 20 pts

Write tests in `server/src/games/ticTacToe.spec.ts` achieving **full branch coverage** of the current implementation: `npm run test` in `server` should report no "Uncovered Line #s" for `src/games/ticTacToe.ts`. (Vitest also writes a readable report to `coverage/index.html`.) Other files' coverage doesn't matter here.

Use the Nim and Guessing Game tests as a guide.

| Points | Criterion |
| --- | --- |
| 5 | Tests reasonably exercise the functions in the implementation |
| 5 | Following the format and style of the Nim / Guessing Game tests |
| 6 | Full branch coverage of `ticTacToe.ts` (3 pts for 90%+) |
| 4 | Tests survive the staff's custom **mutants** |

The mutant criterion cuts both ways: your tests must **not be overspecified** — they should pass valid implementations that differ slightly from the provided one — and they must **catch buggy implementations**.

> [!warning] No autocomplete on this task
> Copilot-style LLM autocompletion is quite good at writing tests, which is exactly why using it here violates the [[CS4530 AI Policy|academic integrity policy]] and risks a failing grade — and would make the task pointless besides.

### Task 3 — Exposing Errors in the User Service · 20 pts

Several functions in the User service claim to return `SafeUserInfo` objects but actually return **passwords**, which get passed to the controller and returned over the API.

1. Investigate the five User REST endpoints in the README, the controller in `server/src/controllers/user.controller.ts`, and the service in `server/src/services/user.service.ts`. Find at least one way to expose passwords through the API. **Include a cURL command that makes the User API return passwords.** *(6 pts)*
2. These bugs exist despite the user service having **100% test coverage** — do TDD. **First**, improve or add tests so the suite *fails* on the current implementation: neither `userId` (the random id, not the username) nor `password` should ever be exposed through a REST endpoint. **Second**, fix the service so it passes. *(6 pts)*
3. Explain briefly why TypeScript allowed a `SafeUserInfo`-returning function to include a `password` field despite `SafeUserInfo` having no such field. *(6 pts)*
4. **Challenge** — find the other, harder bug in the user service that could be a security issue. Give a cURL command demonstrating it, explain why it's bad, write a failing test, and fix it. *(2 pts — don't get stuck here at the expense of other tasks)*

### Task 4 — Creating an Auth Model · 20 pts

Two connected problems with the User model:

1. Frequent for-loops over all usernames to find one matching record.
2. Storing authentication data (password) alongside profile data (display name) makes leaks like Task 3's more likely.

`server/src/services/user.service.ts` contains an unused `storedAuths` object. Use it to map **usernames → user IDs**, which then look up profile info in `storedUsers`. The `AuthRecord` type in `server/src/models.ts` holds the password.

On user creation: generate a random user ID, add `storedUsers[id] = record`, and add a `storedAuths` entry mapping the username to the `AuthRecord`. Finding a user by username then takes two steps instead of a scan.

Requirements:

- Remove the `password` field from `UserRecord`
- Maintain the invariant: whenever `storedUsers[id] === user`, then `storedAuth[user.username].user === id`
- No functions in `user.service.ts` that loop over all elements of an object to find one in particular
- All tests still pass, and `user.service.ts` still has total branch coverage

| Points | Criterion |
| --- | --- |
| 5 | Correctly modifying the User and Auth records |
| 5 | Correctly updating document comments and documenting new ones |
| 5 | Keeping stored User records and stored Auth records in sync |
| 5 | No functions looping through all usernames to find one |

### Task 5 — Refactoring the Auth Model · 15 pts

Split authentication code out of `user.service.ts` into a new `auth.service.ts`.

> [!tip] Commit first
> This task involves a lot of changes. Commit before you start so you can get back.

| Moves to `auth.service.ts` | Stays in `user.service.ts` |
| --- | --- |
| `storedAuths` *(not exported)* | `disallowedUsernames`, `storedUsers` *(not exported)* |
| `resetStoredAuth()` | `populateSafeUserInfo()` |
| `getUserByUsername()` | `createUser()` |
| `checkAuth()` | `getUsersByUsername()` |
| `enforceAuth()` | `updateUser()` |
| | `resetStoredUsers()` |

You'll need at least one new exported helper in `auth.service.ts` to create and/or update `AuthRecord` records, called from `user.service.ts`. Moving these will break a lot of the server — TypeScript, the linter, and the tests will enumerate what broke.

| Points | Criterion |
| --- | --- |
| 6 | All functions in their correct files |
| 5 | Tests pass and both files still have 100% branch coverage (−1 per missing coverage percentage, no negatives; **zero if any test fails** or TypeScript fails because of the refactor) |
| 4 | Correct [[CS4530 Code Style Guide\|code style]] and documentation on all functions |

> [!warning] No autocomplete on this task either
> Task 5 exists to get you comfortable with what TypeScript gives you — seeing red squiggles and fixing them. LLM/Copilot autocompletion here does nothing but interfere with your own learning.

## 5. Grading Summary

| Task | Points |
| --- | --- |
| 1 — Connect4 | 25 |
| 2 — Tic-Tac-Toe tests | 20 |
| 3 — User service errors | 20 |
| 4 — Auth model | 20 |
| 5 — Auth refactor | 15 |
| **Total** | **100** |

## Related

- [[Tutorial - Unit Testing with Vitest]]
- [[Tutorial - API Requests]]
- [[CS4530 Code Style Guide]]
- [[CS4530 Scientific Debugging]]
- [[Team Project Overview]]
