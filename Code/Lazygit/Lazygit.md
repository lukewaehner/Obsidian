---
tags:
  - lazygit
  - git
  - tooling
type: moc
---
# Lazygit

A terminal UI for git that replaces most CLI workflows — staging, committing, branching, rebasing, stashing, cherry-picking — with single-key actions.

Launched via `lg` (alias) or `lazygit`. Config lives in `~/.config/lazygit/config.yml` (stowed from dotfiles).

## Mental Model

Five panels on the left, one main view on the right. Press `1`–`5` to jump panels, `?` for context-aware help, `q` to quit.

| Panel | Number | Purpose |
| --- | --- | --- |
| Status | `1` | Repo summary, current branch, ahead/behind |
| Files | `2` | Working tree — stage / unstage / discard |
| Local Branches | `3` | Switch, create, merge, rebase |
| Commits | `4` | Log — amend, reword, reorder, squash, drop |
| Stash | `5` | Stashed changes |

## Key Bindings (universal)

- `1`–`5` — jump to panel
- `tab` — cycle panels
- `j` / `k` — down / up
- `h` / `l` — left / right (also collapse / expand in trees)
- `]` / `[` — next / prev sub-tab (e.g. local → remotes → tags)
- `enter` — drill in (hunks, files in commit, etc.)
- `space` — primary action (stage, checkout, apply)
- `?` — context help
- `:` — raw git command
- `z` — undo last lazygit action
- `q` / `esc` — close popup / quit

## Workflows

### Commit + Push
1. `2` to Files
2. `space` to stage individual files, or `a` to stage all
3. `c` to commit (or `C` for full editor)
4. `P` to push (`shift+P` to force-with-lease)

### Stage Hunks
1. `2` to Files, select file, `enter` to drill in
2. `space` on a hunk to stage it
3. `v` to enter visual line-select mode for partial hunks
4. `c` to commit only what's staged

### Rewrite History
1. `4` to Commits, select target commit
2. `r` reword · `s` squash into below · `f` fixup · `d` drop · `e` edit
3. `ctrl+j` / `ctrl+k` reorder
4. `g` reset (soft / mixed / hard popup)

### Branch + PR
1. `3`, `n` for new branch, name it, work, commit
2. `P` to push (creates upstream)
3. `o` to open a GitHub PR (requires `gh` CLI)

## Related

- [[Learning Plan]] — staged exercises
- Config source: `~/Repos/dotfiles/lazygit/.config/lazygit/config.yml`
- Theme: TokyoNight Night

%% Begin Waypoint %%
- [[Learning Plan]]

%% End Waypoint %%
