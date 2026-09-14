---
type: topic
group: Systems
tier: extra
confidence:
sections_total: 6
sections_done: 1
coverage: 0.17
status: learning
updated: 2026-09-13
---

# Unix and Linux Command Line

← [[Career/Prep/topics/Systems/Systems|Systems]]

> [!abstract]- Coverage — 1/6
> - [ ] [[#Idea]]
> - [ ] [[#How it works]]
> - [x] [[#Implementation]]
> - [ ] [[#Complexity]]
> - [ ] [[#When to use it]]
> - [ ] [[#Gotchas]]

## Idea

A working set of core tools: `bash`, `cat`, `grep`, `sed`, `awk`, `curl`/
`wget`, `sort`, `tr`, `uniq`, plus `strace` and `tcpdump` for when you need
to see what a process or the network is actually doing.

## How it works

## Implementation

What the shell is driving underneath: file descriptors and the `open`/`read`/`write`/`close` calls that pipes and redirection are built from — [[Code/Computer Systems/Processes/File Descriptors|File Descriptors]], [[Code/Computer Systems/Processes/File IO|File IO]]. Shell-side keybindings and config — [[Code/Zsh/Keybinds|Keybinds]]. Git driven from the terminal — [[Code/Lazygit/Lazygit|Lazygit]].

## Complexity

## When to use it

`strace` for "what syscalls is this process making" debugging; `tcpdump`
for "what's actually on the wire" debugging — both are the tools that answer
questions logging can't.

## Gotchas

## Resources

- [strace (Wikipedia)](https://en.wikipedia.org/wiki/Strace)
- [tcpdump](https://danielmiessler.com/study/tcpdump/)
- [Essential Linux Commands Tutorial](https://labex.io/tutorials/practice-linux-commands-hands-on-labs-398420)

## Problems

_None yet._
