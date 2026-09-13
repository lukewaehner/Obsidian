---
tags:
  - software-engineering
  - northeastern
  - cs4530
  - typescript
  - tooling
  - setup
  - tutorial
type: tutorial
course: "[[Fundamentals of Software Engineering]]"
status: raw
---
# Tutorial — Development Environment Setup

> [!info] Source
> <https://neu-se.github.io/CS4530-Fall-2026/tutorials/week1-getting-started>
> Stuck? Post a **non-private** question on Piazza.

**Assigned in**: [[Module 01 - Orientation and User Stories]] · [[Module 02 - From Requirements to Tests]]
**Blocks**: [[Individual Project 1]] · [[Activity 02 - Test-Driven Development]]

## Hard Requirements

- [ ] **Node.js 24** (v24.12.0 current at time of writing; any 24.x/25.x should work)
- [ ] Installed via **nvm** — strongly recommended even if Node is already installed
- [ ] *An* IDE is required; VS Code is the only **supported** one (staff will help with the linter there, not elsewhere)
- [ ] Prettier extension
- [ ] ESLint extension
- [ ] Vitest extension

## Checklist

### Node via nvm
- [x] macOS/Linux — [nvm](https://github.com/nvm-sh/nvm) install script ✅ 2026-09-13
- [ ] fish shell — [`nvm.fish`](https://github.com/jorgebucaran/nvm.fish) instead (standard nvm is unsupported on fish)
- [ ] Windows — [nvm-windows](https://github.com/coreybutler/nvm-windows/releases); kill VS Code first
- [ ] `nvm install 24` / `nvm use 24`
- [ ] Set the default (`nvm alias default 24`, or `exec nvm use 24` in fish config)
- [ ] Verify: `node -v` → 24.x.x, `npm -v` → v11.x.x

### VS Code
- [x] Install ([download](https://code.visualstudio.com/download); macOS — drag to `/Applications`; Linux — snap works) ✅ 2026-09-13
- [x] Install the three extensions above ✅ 2026-09-13
- [x] Recommended settings: Files Auto Save `afterDelay` · Format On Save · Prettier Document Selectors `*.ts` `*.tsx` · Bracket Pair Colorization ✅ 2026-09-13

### Hello World
- [ ] Write and run `hello-world.ts` with `node hello-world.ts`
- [ ] Introduce a type error (assign a `number` to a `string`), observe the message, run again — **what happens?**

## Gotchas Worth Recording

> [!tip] "Command not found" for npm in VS Code
> If VS Code was open while you installed nvm it won't see the install. Close it completely and reopen. On Windows, `echo %PATH%` in the VS Code shell should contain something like `C:\Program Files\nodejs`.

- [ ] Why the ESLint extension matters before you write code, not after → [[CS4530 Code Style Guide]]

## Notes

## Related

- [[Tutorial - TypeScript Basics]]
- [[Tutorial - Unit Testing with Vitest]]
- [[CS4530 Code Style Guide]]
- [[Individual Project 1]]
