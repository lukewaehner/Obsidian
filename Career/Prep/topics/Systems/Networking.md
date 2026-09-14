---
type: topic
group: Systems
tier: core
confidence:
sections_total: 6
sections_done: 3
coverage: 0.50
status: learning
updated: 2026-09-13
---

# Networking

← [[Career/Prep/topics/Systems/Systems|Systems]]

> [!abstract]- Coverage — 3/6
> - [ ] [[#Idea]]
> - [ ] [[#How it works]]
> - [x] [[#Implementation]]
> - [ ] [[#Complexity]]
> - [x] [[#When to use it]]
> - [x] [[#Gotchas]]

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

HTTP verbs, status codes, headers, and JSON encode/decode as actually used from an app — [[Code/iOS/Communicate Over the Internet/HTTP|HTTP]], [[Code/iOS/Communicate Over the Internet/JSON|JSON]], [[Code/iOS/Communicate Over the Internet/Async Await|Async Await]]. REST resource modelling and URL design from the server side — [[Code/Ruby/Frameworks/Rails/The Web/REST|REST]], [[Code/Ruby/Frameworks/Rails/The Web/URLs|URLs]], [[Code/Ruby/Frameworks/Rails/The Web/APIs|APIs]].

## Complexity

## When to use it

Request/response versus a persistent stream, and when each is right: the exchange serves REST for commands and WebSockets for the market-data firehose — [[Code/Rust/HFT-Ledger/05 - API and WebSocket Layer|API and WebSocket Layer]], [[Code/Rust/HFTX/WebSockets|WebSockets]], [[Code/Rust/HFTX/Rest API|Rest API]].

## Gotchas

Transport security is not optional and the platform will enforce it — [[Code/iOS/Communicate Over the Internet/App Transport Security|App Transport Security]]. HTTP is stateless, so sessions are a thing you build on top — [[Code/Ruby/Frameworks/Rails/The Web/Cookies and Sessions|Cookies and Sessions]].

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
