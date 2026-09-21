---
tags:
  - docker
  - containers
  - virtualization
type: note
related:
  - '[[Docker]]'
  - '[[Linux Container Primitives]]'
---
# Containers vs VMs

Three points on the same spectrum, separated by **where the kernel lives**.

## The Three Arrangements

| | What runs the guest | Kernel |
| --- | --- | --- |
| **Hypervisor** (pure VM) | A dedicated kernel-level VMM program runs *instead of* the OS kernel | Each VM has its own |
| **Hosted VM** | A VMM runs on the host OS; the guest OS runs on the VMM — e.g. VirtualBox on your laptop | Each VM has its own |
| **Container** | The host OS, directly | **Shared with the host** |

## Tradeoffs

- A VM has **fixed resources** and the overhead of running a whole kernel
- **Faster to start a container than a kernel** — container startup is process startup
- **VMs offer better isolation** — a shared kernel is a shared attack surface and a shared failure domain

## Rule of Thumb

Reach for a container when you want many cheap, fast, identical instances of *your* software.
Reach for a VM when you need to run a different kernel, or when the isolation boundary is a
security boundary you actually rely on.

## See Also

- [[Linux Container Primitives]] — how a shared kernel still isolates
- [[Why Containerize]]
- [[Docker]]
