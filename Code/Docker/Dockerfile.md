---
tags:
  - docker
  - dockerfile
  - images
type: note
related:
  - '[[Docker]]'
  - '[[Images and Containers]]'
  - '[[Running Containers]]'
---
# Dockerfile

A `Dockerfile` tells Docker **how to build an image**. Each directive is one cached
[[Images and Containers|layer]].

## Canonical Example

```docker
FROM ubuntu:24.04

RUN apt-get update
RUN apt-get install -y gcc

COPY hello.c /app/
WORKDIR /app/
RUN gcc hello.c -o hello

ENTRYPOINT ["/app/hello"]
```

## Directives

| Directive | What it does |
| --- | --- |
| `FROM` | Base image everything else layers onto. Pick from [DockerHub](https://hub.docker.com/) |
| `RUN` | Execute a command at **build** time and commit the result as a layer |
| `COPY` | Copy from the local filesystem into the image filesystem |
| `ADD` | Like `COPY`, but also auto-extracts local tarballs and fetches remote URLs |
| `WORKDIR` | `cd` inside the image; also the working directory for containers |
| `ENTRYPOINT` | What runs the instant the container starts |
| `CMD` | Default arguments, overridable by `docker run <image> <args>` |

Build work belongs at build time: compiling in a `RUN` means the image ships a **binary**, not
source plus a toolchain.

## Passing Arguments

Arguments can be baked into the `ENTRYPOINT`:

```docker
ENTRYPOINT /app/hello classnumber
```

…or supplied at run time, after the image name:

```bash
docker run hello 4730
```

Anything after the image name in `docker run` is passed through to the entrypoint.

## Gotchas

> [!warning] `COPY`, not `ADD`
> `ADD` additionally auto-extracts tarballs and fetches URLs — behavior nobody wants when the
> intent is "copy this file in". `COPY` is the documented recommendation for plain file copies.

> [!warning] Exec form, not shell form
> `ENTRYPOINT /app/hello` (unbracketed) is **shell form**: Docker wraps it in `/bin/sh -c`, so the
> binary runs as PID 1's *child* and **never receives `SIGTERM`/`SIGINT`**. `docker stop` then
> hangs its ten seconds and kills. Use `ENTRYPOINT ["/app/hello"]` for anything holding a socket.

> [!note] Split `apt-get update` caches badly
> An unchanged `RUN apt-get update` layer is reused indefinitely, so a later `install` line can hit
> a stale index and 404. `RUN apt-get update && apt-get install -y …` in one layer avoids it.

## See Also

- [[Images and Containers]]
- [[Running Containers]]
- [[Docker Compose]] — declaring the containers built from this image
- [Dockerfile reference](https://docs.docker.com/reference/dockerfile/)
- [[Docker]]
