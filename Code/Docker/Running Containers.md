---
tags:
  - docker
  - containers
type: note
related:
  - '[[Docker]]'
  - '[[Images and Containers]]'
  - '[[Standard Streams]]'
---
# Running Containers

`docker run` runs a command in a **new** container. It is the one command with enough flags to
need its own map — the flag groups each have their own note.

## Core Commands

```bash
docker run [OPTIONS] IMAGE [COMMAND] [ARG...]
docker stop [OPTIONS] CONTAINER [CONTAINER...]
```

```bash
docker run mydockerhello
docker stop mydockerhello
```

`docker stop` sends `SIGTERM`, waits ten seconds, then `SIGKILL`.

## Flag Map

| Flags | Purpose | Note |
| --- | --- | --- |
| `-v host:container` | Persist data past container exit | [[Volume Mapping]] |
| `-p hostport:containerport` | Reach the container from outside the host | [[Port Mapping]] |
| `-i`, `-t`, `-d`, `-a` | Wire up stdin/stdout/stderr, background vs foreground | [[Standard Streams]] |
| `--network <net>` | Attach to a named network, getting name resolution | [[Docker Networking]] |
| `--name <n>` | Give the container a stable name instead of a random one | |
| `--rm` | Delete the container when it exits | [[Removing Containers and Images]] |

## run vs exec

- `docker run` — **new** container from an image
- `docker exec` — command inside an **already running** container ([[Docker Exec]])

Reaching for `run` when you meant `exec` is how you end up with nine exited containers and no idea
which one had your file.

## Arguments

Anything after the image name is passed to the image's `ENTRYPOINT`:

```bash
docker run hello 4730
docker run -it --name first --network mynetwork dockernetwork
```

`-it` on an image with no `ENTRYPOINT` falls back to the base image's default — for `ubuntu`, that
is `/bin/bash`, so you land in a shell.

## See Also

- [[Dockerfile]] — where the default command comes from
- [[Docker Compose]] — the same flags, declared in YAML instead of typed
- [[Docker]]
