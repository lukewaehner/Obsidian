---
tags:
  - lecture
  - distributed-systems
  - northeastern
  - cs4730
  - networking-primer
type: lecture
course: "[[Distributed Systems]]"
module: 2
week: 2
date: 2026-09-10
status: learning
---

# Week 02 — Networking Primer

Lecture for [[Distributed Systems]].

## Meetings

- **Tue Sep 15** — ~~cancelled~~. Jackson had a personal emergency and announced it the same
  afternoon. His instruction: review the Network Refresh slides on your own, they get discussed
  Thursday instead.
- **Thu Sep 17** — Network Refresh discussion, pushed from Tuesday

## Assigned Material

- [ ] Slides: [Network refresh](https://4730.network/slides/cs4730_network_primer.pptx) (pptx)
- [ ] Lecture examples: `udpecho.py`, `udpecho-timer.py`, `udpecho-wo-select.py`, `udpecho-with-select.py` — linked from the [schedule](https://4730.network/docs/schedule/)
- [ ] [Python Socket Programming HOWTO](https://docs.python.org/3/howto/sockets.html)

## Notes

### IP Addressing

**IPv4**: 32-bit address

- In a dotted notation e.g. `192.168.21.76`
- Each number is a byte
- Stored in Big Endian order

#### IP Datagrams

Like a letter:

- Self contained
- Include all necessary addressing information
- No advanced setup of connections or circuits

![[Screenshot 2026-09-17 at 3.06.38 PM.png]]

- **Version**: 4 for IPv4, 6 for IPv6
- **Header Length**: Number of 32 bit words (usually 5)
- **Datagram length**: Length of header + data in bytes
- **Time to Live (TTL)**: Determined by each router
- **Protocol**: ID of encapsulated protocol
	- 6 = TCP, 17 = UDP
- **Checksum**:
- **Source & Destination address**: In theory, must be globally unique. Violated in practice.

### Transport Layer

- Demultiplexing of data streams

**Optionally**:

- Creating long lived "connections"
- Reliable, in-order packet delivery
- Error detection
- Flow and congestion control

**Challenges**:

- Detecting and responding to congestion
- Balancing fairness against high utilization

### Multiplexing

#### The case

When delivering to an apartment building, which door do you deliver to?

#### Demultiplexing traffic

![[Screenshot 2026-09-17 at 3.19.36 PM.png]]

We can create unique connections with the object

`<src_ip, src_port, dest_ip, dest_port>`

### Protocols

#### UDP

- Simple, connectionless datagram
	- C sockets: `SOCK_DGRAM`
- Port numbers enable demultiplexing
	- 16 bits = 65535 possible ports
	- Port 0 being invalid
- Checksum for error detection
	- Detects some corrupted packets
	- Does not check for dropped, duplicated, repeated packets

![[Screenshot 2026-09-17 at 3.20.33 PM.png]]

**Usage Example**

*Sending*:

```python
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto("message", ("127.0.0.1", 3456))
```

*Receiving*:

```python
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("127.0.0.1", 3456))
data, arr = sock.recvfrom(2048)
```

Sending a buffer will produce exactly one datagram containing the data from the buffer

- Warning: UDP datagrams may hold up to 65,000 bytes of data
- If `len(UDP datagram)` > MTU (Maximum transmission unit), IP will need to fragment it

Receiving will return exactly one, full datagram

- Not a partial datagram, not >1 datagrams

#### TCP

Reliable, in-order, bi-directional byte stream

- Port numbers for demultiplexing
- Virtual circuits (connections)
- Flow control
- Congestion control, approximate fairness

![[Screenshot 2026-09-17 at 3.37.11 PM.png]]

![[Screenshot 2026-09-17 at 3.40.39 PM.png]]

*Usage*:

```python
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1", 3456))
sock.sendall("message")
```

*Receiving*:

```python
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("127.0.0.1", 3456))
sock.listen()
conn, addr = sock.accept()
data = conn.recv(2048)
```

![[Screenshot 2026-09-17 at 3.48.27 PM.png]]

We can keep reading from the buffer until the buffer returns a 0 size receive — this is how we know
we have pulled all the segments from all sent messages off the socket, and can do message
reconstruction fully

TCP tries to send 1460 bytes per segment, but this doesn't always happen

You could receive:

- A full message
- part of a message
- multiple messages..

**`send*` semantics**

```python
send(bytes)
sendto(bytes, addr)
```

*TCP*

- multiple segments are sent depending on number of bytes and max packet size in the data link

*UDP*

- A datagram up to bytes long, with max being 65535 bytes

**`recv*` semantics**

Similar to File I/O

```python
recv(size)
recvfrom(size)
```

maximum amount of data that can be read at once

*TCP*

- No guarantee all data is transmitted in a single read, but all data will arrive

*UDP*

- A single datagram is read at one time

**Asynchronous Communication**

`recv` is blocking

- it waits until the socket has something to read
- if nothing is coming, it will block permanently

This is fine if the client is synchronous, so client sends, server responds, send, respond, ...

UDP sockets bind to a port, not to address, port

- UDP bind delivers packets from any host sending to the port
- `recvfrom()` returns data and the IP it was received from

If messages are not arriving frequently, the code can lock up

- App goes idle
- Impacts performance

Addressed by:

- Using `select()` or `poll()`; single threaded solutions
	- Much simpler to debug and reason about
- Threading
	- Much better performance when tuned correctly
	- Much more challenging to debug

## Key Takeaways

- 

## Open Questions

- 

## Related

- [[Distributed Systems]]
