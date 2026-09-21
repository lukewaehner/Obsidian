---
tags:
  - docker
  - containers
  - linux
type: note
related:
  - '[[Docker]]'
  - '[[Containers vs VMs]]'
---
# Linux Container Primitives

A container is not a kernel feature. It is three older Linux features used together, which is why
containers are cheap and why their isolation has holes a VM does not.

## The Three Features

### Control groups (cgroups)

Limit the resources — **memory, CPU, network input/output** — that a group of Linux processes can
use.

Security consequence: by capping what a process can consume, containers provide protection against
attacks that work by **consuming excessive resources**.

### Linux namespaces

Restrict the **visibility** of resources to a process. Put a process in a namespace and you control
which PIDs, mounts, network interfaces, and users it can even see.

Cgroups limit *how much*; namespaces limit *what*.

### Changing the root directory

Limits the set of files and directories a process can see. The root directory is changed when the
container is created, so a container **cannot see the host's entire filesystem**.

## Why This Matters

All three are enforced by the **host kernel**, which the container shares. There is no guest kernel
to hide behind — see [[Containers vs VMs]] for what that costs in isolation strength.

## See Also

- [[Containers vs VMs]]
- [[Why Containerize]]
- [[Docker]]
