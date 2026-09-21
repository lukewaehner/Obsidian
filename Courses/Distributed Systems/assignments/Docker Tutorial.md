---
tags:
  - assignment
  - distributed-systems
  - northeastern
  - cs4730
type: assignment
course: "[[Distributed Systems]]"
due: 2026-09-15
week: 1
date: 2026-09-10
status: raw
---

# Docker Tutorial

> [!danger] Due Tue 2026-09-15, 11:59:59pm ET · submitted via Gradescope

Assignment for [[Distributed Systems]]. [Schedule on the course site](https://4730.network/docs/schedule/) · [starter repo](https://github.khoury.northeastern.edu/cs4730/docker-tutorial/)

> [!info] The only dated deliverable published so far.

- [x] Docker Tutorial 📅 2026-09-14 ✅ 2026-09-17

Local work: `~/Documents/northeastern/fall-2026/distributed-systems/work/docker-tutorial`
(`docker-hello/` and `docker-network/` built from the README's walkthrough).

## What It Covers

Not a graded protocol project — it's the infrastructure onboarding for the whole course. Every
project from [[Project 1 - HELLO-ACK Protocol]] onward is evaluated by running a Compose file, so
the four things below are the actual deliverable: you need them to be reflexes by the time a spec
is due.

1. **Images and containers** — build an image from a `Dockerfile`, run containers from it
2. **A C hello-world in a container** — `docker-hello/`
3. **Container-to-container networking** — a user-defined bridge network plus `netcat`, `docker-network/`
4. **Docker Compose** — declaring a multi-container system in YAML instead of by hand

### Image vs container

A **container** is an isolated environment running inside the host. Conceptually close to a VM,
but the internals are different — no guest kernel, no hardware emulation. An **image** is the
blueprint a container is instantiated from: image is to container as class is to object.

Images are built in **layers**. Each layer either adds files to the image filesystem, runs a
command, or defines an attribute of the containers built from it. Any number of containers can be
spun up from one image, each consuming its own system resources.

### Why the course uses it

- Submissions are **reproducible**, so they're much less likely to be graded wrong
- Running N instances of a distributed application locally is tractable once past the learning curve

Combined with the syllabus rule that everything must compile and run on **Ubuntu Linux** via
Gradescope, `ubuntu:24.04` as a base image is effectively the target platform for every project.

## Setup Notes

Install the latest stable **Docker Desktop**. It needs superuser/administrator access, so it
**will not work on Northeastern machines** like `login.khoury.northeastern.edu` — this is local-only.
[Per-OS instructions](https://docs.docker.com/install/).

### 1 — Simple application (`docker-hello/`)

`hello.c`:

```c
#include <stdio.h>

int main() {
  printf("Hello, Docker!\n");
  return 0;
}
```

`Dockerfile`:

```docker
FROM ubuntu:24.04

RUN apt-get update
RUN apt-get install -y gcc

COPY hello.c /app/
WORKDIR /app/
RUN gcc hello.c -o hello

ENTRYPOINT /app/hello
```

Line by line:

| Directive | What it does |
| --- | --- |
| `FROM ubuntu:24.04` | Base image everything else layers onto. Other options on [DockerHub](https://hub.docker.com/); this semester is standardized on `ubuntu:24.04` |
| `RUN apt-get update` | Refresh the Ubuntu package index |
| `RUN apt-get install -y gcc` | Install the C compiler. Alternatively a base image that ships gcc would skip both lines |
| `COPY hello.c /app/` | Copy from the local filesystem into the image filesystem (README uses `ADD` — see Gotchas) |
| `WORKDIR /app/` | `cd` inside the image; also the working directory for containers |
| `RUN gcc hello.c -o hello` | Compile at **build** time, so the image ships a binary |
| `ENTRYPOINT /app/hello` | What runs the instant the container starts |

Build and run, from inside `docker-hello/`:

```bash
docker build . -t "dockerhello"   # build image from ./Dockerfile, tag it dockerhello
docker run dockerhello            # instantiate a container; prints the greeting
```

The first build takes a few minutes while the base image downloads. Subsequent builds hit the
layer cache.

### 2 — Networking demo (`docker-network/`)

Containers *can* talk over Docker's default bridge, but the default bridge gives **no container
name-to-IP resolution**. A **user-defined** bridge network does. That matters for the projects:
a peer list written in terms of hostnames stays valid across runs as long as the container names
stay the same, instead of needing new IPs every launch.

```bash
docker network list                              # what already exists
docker network create --driver bridge mynetwork  # add ours
```

`Dockerfile`:

```docker
FROM ubuntu:24.04

RUN apt-get update
RUN apt-get install -y netcat-traditional iputils-ping
```

```bash
docker build . -t dockernetwork
```

Two containers, two terminals, both attached to `mynetwork`:

```bash
# terminal 1
docker run -it --name first  --network mynetwork dockernetwork
# terminal 2
docker run -it --name second --network mynetwork dockernetwork
```

`-it` = **interactive** + accept `tty` input, i.e. you can drive it from the terminal. This image
declares no `ENTRYPOINT`, so it falls back to the Ubuntu default of `/bin/bash` and drops you into
a shell. Arguments placed after the image name are passed through to the entrypoint.

Then, a TCP conversation across the bridge — listener in `first`:

```bash
netcat -nvlp 3000
```

| Switch | Meaning |
| --- | --- |
| `-n` | do not use DNS |
| `-v` | verbose |
| `-l` | listen |
| `-p` | port number |

Client in `second`, addressing the other container **by container name**:

```bash
netcat -v first 3000
```

Both ends report an established TCP connection, and anything typed in `second` followed by return
echoes out in `first`. That name resolution — `first` resolving without an IP anywhere — is the
entire point of the user-defined network.

`netcat` is worth real fluency here; it's the fastest way to poke at a socket a project is
supposed to be serving.

### 3 — Docker Compose

[Docker Compose](https://docs.docker.com/compose/) orchestrates containers: attributes and
arguments declared statically in YAML rather than typed as `docker run` flags.
[Install instructions](https://docs.docker.com/compose/install/).

`composition.yml` — two containers on a bridge network, each printing a message and exiting:

```yaml
services:
  one:
    image: dockernetwork
    networks:
      - mynetwork
    hostname: "host1"
    command: echo "hello, host2"
  two:
    image: dockernetwork
    networks:
      - mynetwork
    hostname: "host2"
    command: echo "hello, host1"

networks:
  # The presence of these objects is sufficient to define them
  mynetwork: {}
```

Note `networks: mynetwork: {}` — **declaring the object is enough to create it**. No separate
`docker network create` needed when Compose owns the network.

```bash
docker compose -f <COMPOSE_FILENAME.yml> up
```

```text
[+] Running 2/2
 ⠿ Container lab3-two-1  Recreated                                     8.7s
 ⠿ Container lab3-one-1  Recreated                                    19.0s
Attaching to lab3-one-1, lab3-two-1
lab3-one-1  | hello, host2
lab3-two-1  | hello, host1
lab3-one-1 exited with code 0
lab3-two-1 exited with code 0
```

Container names are `<project>-<service>-<index>`, where the project name defaults to the
directory name. `command:` overrides the image's default command, which is how one image serves as
both peers.

This is the piece that carries into every project: Project 1 ships a `Dockerfile` and
`proj1-compose.yml`, and **evaluation uses the supplied compose file** — so the compose file is
the contract, and `docker compose -f … up --build` is how graded runs actually happen.

## Gotchas

> [!warning] `netcat` is not installable by that name on `ubuntu:24.04`
> The README's `apt-get install -y netcat` fails — `netcat` is a virtual package with no default
> provider. Pick one explicitly: **`netcat-traditional`** or `netcat-openbsd`. Use
> `netcat-traditional`, since the README's `netcat -nvlp 3000` is traditional's flag syntax;
> openbsd's `nc` spells the same thing differently. Local `docker-network/Dockerfile` already
> corrects this.

> [!warning] `COPY`, not `ADD`
> The README uses `ADD hello.c /app/`. `ADD` additionally auto-extracts local tarballs and fetches
> remote URLs — behavior nobody wants when the intent is "copy this file in". `COPY` is the
> documented recommendation for plain file copies. Local `docker-hello/Dockerfile` uses `COPY`.

> [!warning] `ENTRYPOINT /app/hello` is shell form
> Unbracketed means Docker wraps it in `/bin/sh -c`, so the binary runs as PID 1's *child* and
> **does not receive `SIGTERM`/`SIGINT`** — `docker stop` hangs its ten seconds and then kills. Fine
> for a hello-world that exits immediately; a problem for a long-running peer that should shut
> down cleanly. Use exec form — `ENTRYPOINT ["/app/hello"]` — for anything with a socket open.

> [!tip] `printf` without a trailing newline
> The README's `printf("hello world")` leaves the shell prompt glued to the output and, worse,
> can leave the line sitting in a buffer. Local `hello.c` prints `"Hello, Docker!\n"` and returns
> `0`. Line-buffered stdout in a container is a recurring source of "my peer printed nothing" —
> relevant later, since Project 1 is graded on printing **exactly one line**.

> [!tip] Default bridge ≠ user-defined bridge
> Only a **user-defined** bridge gives name-to-IP resolution. Skipping
> `docker network create --driver bridge mynetwork` (or the Compose `networks:` block) means
> `netcat -v first 3000` can't resolve `first`.

> [!tip] `-f` is required for non-default filenames
> `docker compose up` with no `-f` only looks for `compose.yaml`/`docker-compose.yml`. Local file
> is `composition.yml`, so `-f composition.yml` is mandatory — and project specs name their own
> (`proj1-compose.yml`).

> [!bug] `No address associated with hostname`
> A DNS problem, and only when a container references **Internet** hosts — it shouldn't occur with
> course containers, which use synthetic Compose names. If it does, add a public resolver to
> `~/.docker/daemon.json` or `/etc/docker/daemon.json` (the README misspells this as `dameon.json`):
>
> ```json
> {
>   "dns": ["10.0.0.2", "1.1.1.1"]
> }
> ```
>
> Restart the Docker service afterward.

> [!note] Layer caching and `apt-get update`
> Each `RUN` is a cached layer, so an unchanged `RUN apt-get update` is reused indefinitely and can
> hand you a stale index when a later `install` line changes. Combining them
> (`RUN apt-get update && apt-get install -y …`) avoids it. The course Dockerfiles keep them split
> for readability; worth knowing when an install suddenly 404s.

## Command Reference

```bash
docker build . -t <tag>                      # build image from ./Dockerfile
docker run <image>                           # run a container
docker run -it --name <n> --network <net> <image>   # interactive, named, on a network
docker network list                          # list networks
docker network create --driver bridge <net>  # create a user-defined bridge
docker compose -f <file>.yml up              # bring up a declared system
docker compose -f <file>.yml up --build      # rebuild images first
netcat -nvlp <port>                          # listen (no DNS, verbose)
netcat -v <host> <port>                      # connect
```

## Related

- [[Distributed Systems]]
- [[Week 01 - Introduction and Networking]]
- [[Project 1 - HELLO-ACK Protocol]] — first project graded through a supplied compose file
- [Dockerfile reference](https://docs.docker.com/reference/dockerfile/) · [DockerHub](https://hub.docker.com/) · [Compose docs](https://docs.docker.com/compose/)
- Adapted by the course from [Asad Salman's](https://github.com/asadsalman/docker-tutorial) and [iowaguy's](https://github.com/iowaguy/docker-tutorial) tutorials
