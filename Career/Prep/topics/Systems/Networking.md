---
type: topic
group: Systems
tier: core
confidence:
sections_total: 6
sections_done: 0
coverage: 0.00
status: untouched
updated: 2026-09-01
---

# Networking

> [!abstract]- Coverage — 0/6
> - [ ] [[#Idea]]
> - [ ] [[#How it works]]
> - [ ] [[#Implementation]]
> - [ ] [[#Complexity]]
> - [ ] [[#When to use it]]
> - [ ] [[#Gotchas]]

## Idea

Networking experience or a reliability/operations-track interview raises the
odds of these questions directly; otherwise it's good-to-know background for
system design conversations.

## How it works

- The OSI/TCP-IP model layers responsibility: physical/link, network (IP
  routing), transport (TCP/UDP), application (HTTP and friends).
- TCP is connection-oriented and reliable (ordering, retransmission); UDP is
  connectionless and unreliable but lower-overhead — the classic tradeoff
  between correctness guarantees and latency.
- HTTPS layers TLS/SSL under HTTP for confidentiality and integrity; HTTP/2
  adds multiplexing over a single connection to avoid the head-of-line
  blocking multiple HTTP/1.1 connections were used to work around.
- Sockets are the OS-level abstraction a program uses to open and use a
  network connection.

## Implementation

## Complexity

## When to use it

## Gotchas

## Resources

- [Khan Academy: Computers and the Internet](https://www.khanacademy.org/computing/code-org/computers-and-the-internet)
- [UDP and TCP: Comparison of Transport Protocols (video)](https://www.youtube.com/watch?v=Vdc8TCESIg8)
- [TCP/IP and the OSI Model Explained! (video)](https://www.youtube.com/watch?v=e5DEVa9eSN0)
- [Packet Transmission across the Internet (video)](https://www.youtube.com/watch?v=nomyRJehhnM)
- [HTTP (video)](https://www.youtube.com/watch?v=WGJrLqtX7As)
- [SSL and HTTPS (video)](https://www.youtube.com/watch?v=S2iBR2ZlZf0)
- [SSL/TLS (video)](https://www.youtube.com/watch?v=Rp3iZUvXWlM)
- [HTTP 2.0 (video)](https://www.youtube.com/watch?v=E9FxNzv1Tr8)
- [Networking video series (21 videos)](https://www.youtube.com/playlist?list=PLEbnTDJUr_IegfoqO4iPnPYQui46QqT0j)
- [Subnetting Demystified - Part 5 CIDR Notation (video)](https://www.youtube.com/watch?v=t5xYI0jzOf4)
- [Java - Sockets - Introduction (video)](https://www.youtube.com/watch?v=6G_W54zuadg&t=6s)
- [Socket Programming (video)](https://www.youtube.com/watch?v=G75vN2mnJeQ)

## Problems

_None yet._
