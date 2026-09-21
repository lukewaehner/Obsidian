---
tags:
  - docker
  - containers
type: note
related:
  - '[[Docker]]'
  - '[[Containers vs VMs]]'
  - '[[Images and Containers]]'
---
# Why Containerize

*Build once, run anywhere.*

A container packs together an application and **all of its dependencies**, and isolates the
application from the rest of the machine it runs on.

## What That Buys You

| Benefit | Why it follows from isolation |
| --- | --- |
| **Reproducibility** | The image carries its own dependencies, so "works on my machine" and "works on the grader's machine" are the same claim |
| **Running multiple instances** | Dependencies are isolated from each other, so many containers run on one machine without interfering |
| **Automated installation on clusters** | Orchestrators (Kubernetes) distribute containerized apps across a fleet, so you never install by hand |

## Why Distributed Systems Courses Care

Running N instances of a distributed application on one laptop is the whole point. Each peer is a
container with its own filesystem view, its own IP on a [[Docker Networking|bridge network]], and
its own process tree — which is what makes a five-node protocol testable locally.

## See Also

- [[Containers vs VMs]] — what you give up versus a real VM
- [[Linux Container Primitives]] — the kernel features that make the isolation real
- [[Docker]]
