---
tags:
  - lazygit
  - learning
type: plan
related:
  - "[[Lazygit]]"
---
# Lazygit Learning Plan

A staged path from "what panel am I in" to "interactive rebase without flinching." Each task has a concrete action and the outcome you should observe.

> Tip: do these in a throwaway repo so you can rebase / drop / reset without fear.
> ```
> mkdir ~/lazygit-sandbox && cd ~/lazygit-sandbox && git init
> for i in 1 2 3 4 5; do echo "line $i" > file$i.txt && git add . && git commit -m "add file$i"; done
> ```

---

## Stage 1 — Orientation

Goal: know where you are and how to get help without panicking.

### Tasks

- [x] **1.1** Open lazygit (`lg`) in any repo. Press `1`, `2`, `3`, `4`, `5` and identify each panel by name. ✅ 2026-05-11
```
expected: panel header changes (Status / Files / Local Branches / Commits / Stash)
```

- [x] **1.2** Press `?` from each panel and skim the help. Close it with `esc`. ✅ 2026-05-11
```
expected: keybindings listed are scoped to the active panel
```

- [x] **1.3** Open the command-line popup with `:`, type `status`, hit enter. ✅ 2026-05-14
```
expected: raw `git status` output appears in the main view
```

- [x] **1.4** Quit with `q`. ✅ 2026-05-11

---

## Stage 2 — Staging & Committing

Goal: replace `git add` / `git commit` / `git push` with lazygit.

### Tasks

- [ ] **2.1** Edit two files. In Files panel (`2`), use `space` to stage one and leave the other unstaged.
```
expected: green = staged, red = unstaged. Status panel shows "1 file staged"
```

- [ ] **2.2** Stage everything with `a`, then unstage everything with `a` again (toggle).

- [ ] **2.3** Press `c` to commit. Type a message, hit enter.
```
expected: commit appears at top of Commits panel (4)
```

- [ ] **2.4** Press `C` instead of `c` to open `$EDITOR` for a multi-line commit body.

- [ ] **2.5** Make a small change, then `A` to amend the previous commit (no new commit created).

- [ ] **2.6** Push with `P`. Pull with `p`.

---

## Stage 3 — Hunk-Level Staging

Goal: commit only part of a file.

### Tasks

- [ ] **3.1** Edit a file in 3 places. In Files panel, select the file, `enter` to drill into the hunk view.
```
expected: main view shows individual hunks, separated by @@ lines
```

- [ ] **3.2** Press `space` on one hunk to stage just that hunk. Verify the file shows as both staged AND unstaged in the Files panel.

- [ ] **3.3** Press `v` on a hunk to enter line-select mode. Highlight 2 lines with `j`, then `space` to stage only those lines.

- [ ] **3.4** Commit with `c`. Confirm the diff in the new commit contains only the lines you staged.

---

## Stage 4 — Inspecting History

Goal: read the log and diffs without leaving lazygit.

### Tasks

- [ ] **4.1** In Commits panel (`4`), navigate with `j` / `k`. Watch the main view update with each commit's diff.

- [ ] **4.2** Press `enter` on a commit to see the list of files it touched. `enter` again on a file to see that file's diff in that commit.

- [ ] **4.3** With one commit selected, press `space` on a file inside it. Then select a *different* commit and press `space` on a file — this enters **diff mode** between the two commits.
```
expected: header shows "Diffing <sha1>..<sha2>". Press `esc` to exit.
```

- [ ] **4.4** Press `ctrl+s` in Commits to filter by author or path.

---

## Stage 5 — Branches

Goal: create, switch, merge.

### Tasks

- [ ] **5.1** In Local Branches (`3`), press `n` to create a new branch. Name it `feature/test`.
```
expected: branch is created AND checked out. Status panel shows new branch name.
```

- [ ] **5.2** Make a commit on `feature/test`. Switch back to `main` with `space` on the main branch.

- [ ] **5.3** With `main` checked out and `feature/test` selected, press `M` to merge `feature/test` into `main`.

- [ ] **5.4** Delete `feature/test` with `d`.

- [ ] **5.5** Create another branch, make 2 commits. Switch to main and rebase your branch on top by selecting `main` and pressing `r` (rebase current onto selected) — but first re-checkout your feature branch.

---

## Stage 6 — Interactive Rebase (the lazygit superpower)

Goal: rewrite history without `git rebase -i` syntax.

### Tasks

- [ ] **6.1** In Commits (`4`), select your latest commit and press `r` to reword.
```
expected: prompt opens, type new message, save → commit message updates
```

- [ ] **6.2** Select a commit and press `s` to **squash into the commit below**. Confirm the result is one combined commit.

- [ ] **6.3** Make a "fix typo" commit. Use `f` (fixup) to merge it into the commit below without keeping the message.

- [ ] **6.4** Select a commit and use `ctrl+j` / `ctrl+k` to reorder it.

- [ ] **6.5** Select a commit and press `d` to drop it entirely.
```
expected: commit is gone from history. If your sandbox is local-only, no force-push needed.
```

- [ ] **6.6** Press `z` immediately after to undo the drop.

- [ ] **6.7** Press `e` to mark a commit for editing. Lazygit pauses the rebase there. Make a change, stage, commit, then continue rebase with `m` → continue.

---

## Stage 7 — Stashing

Goal: shelve work mid-task.

### Tasks

- [ ] **7.1** Make uncommitted changes. From Files, press `s` to stash everything.
```
expected: changes disappear from Files; appear in Stash panel (5)
```

- [ ] **7.2** From Files, make new changes, then press `S` to stash with a custom name.

- [ ] **7.3** In Stash (`5`), select a stash. Press `space` to apply (keeps the stash) or `g` to pop (applies and deletes).

- [ ] **7.4** Drop a stash with `d`.

---

## Stage 8 — Advanced

Goal: cherry-pick, reset, GitHub integration.

### Tasks

- [ ] **8.1** Create branch `A`, commit something. Switch to branch `B`. In Commits, navigate to branch `A`'s commit, press `c` to mark for cherry-pick. Press `v` to paste it onto `B`.

- [ ] **8.2** Hard-reset to a previous commit: select the target commit, press `g`, choose "hard reset". Verify with `git log` outside lazygit.
```
warning: this is destructive on shared branches. Sandbox only.
```

- [ ] **8.3** With `gh` CLI configured, push a feature branch and press `o` in Local Branches to open a PR.

- [ ] **8.4** Open `~/.config/lazygit/config.yml`. Add a `customCommands` entry that runs `git log --oneline -20` bound to a key. Reload lazygit and try it.
```
yaml example:
customCommands:
  - key: "<c-l>"
    context: "global"
    command: "git log --oneline -20"
    output: log
```

---

## Reference

| Stage | Focus | Outcome |
| --- | --- | --- |
| 1 | Orientation | Navigate panels, find help |
| 2 | Commit flow | Replace add / commit / push |
| 3 | Hunks | Partial-file commits |
| 4 | History | Read log + diffs in-app |
| 5 | Branches | Create, switch, merge |
| 6 | Rebase | Reword, squash, drop, reorder |
| 7 | Stash | Shelve and restore |
| 8 | Advanced | Cherry-pick, reset, PR, custom commands |

## Graduation Criteria

You're done with the plan when you can do all of the following without looking at notes:
- Stage individual hunks and commit them
- Reword + squash a chain of commits via the Commits panel
- Recover from a bad rebase with `z` (or `git reflog` if `z` is gone)
- Open a PR from inside lazygit with `o`
