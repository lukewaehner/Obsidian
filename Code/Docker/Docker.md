---
tags:
  - docker
  - containers
  - tools
type: moc
---
# Docker

An application that lets you **create and build containers** — plus a set of commands for
manipulating images and containers, and a repository to store images in.

Read top to bottom the first time; after that it's a lookup table.

## Concepts

- [[Why Containerize]] — build once, run anywhere; what isolation buys you
- [[Linux Container Primitives]] — cgroups, namespaces, changing the root directory
- [[Containers vs VMs]] — hypervisor, hosted VM, container; where the kernel lives
- [[Images and Containers]] — image is to container as class is to object; layers

## Building

- [[Dockerfile]] — directives, argument passing, the `COPY`/`ADD` and exec-form gotchas
- [[Docker Registries]] — `push` / `pull`, tags, digests

## Running

- [[Running Containers]] — `run` / `stop`, the flag map, `run` vs `exec`
- [[Docker Exec]] — commands inside an already-running container
- [[Standard Streams]] — `-i`, `-t`, `-d`, `-a`, and the buffering trap
- [[Inspecting Containers]] — `ps` / `images`
- [[Removing Containers and Images]] — `rm` / `rmi` and the ordering rule

## Connecting

- [[Docker Networking]] — the three default networks; default vs user-defined bridge
- [[Port Mapping]] — `-p`, reaching a container from outside the host
- [[Volume Mapping]] — `-v`, surviving container exit
- [[Docker Compose]] — declaring a multi-container system in YAML

## Quick Reference

```bash
# images
docker build . -t <tag>                 # build image from ./Dockerfile
docker images [repo[:tag]]              # list images
docker pull <name>[:tag|@digest]        # fetch from a registry
docker push <name>[:tag]                # publish (needs an account)
docker rmi <image>                      # remove image

# containers
docker run [opts] <image> [cmd] [args]  # new container
docker run --rm -it <image> bash        # throwaway interactive shell
docker stop <container>                 # SIGTERM, 10s, SIGKILL
docker ps                               # running
docker ps -a                            # including exited
docker rm <container>                   # remove container
docker exec -it <container> bash        # shell into a running container

# wiring
docker run -v /host/path:/ctr/path      # persist data
docker run -p 8001:5000                 # expose via host port
docker run --network <net> --name <n>   # named, on a network
docker network list
docker network create --driver bridge <net>

# systems
docker compose -f <file>.yml up
docker compose -f <file>.yml up --build
docker compose -f <file>.yml down
```

## Flags Worth Memorizing

| Flag | Meaning |
| --- | --- |
| `-t` | Tag (on `build`) / allocate a tty (on `run`) |
| `-i` | Attach stdin |
| `-d` | Detached — run in background |
| `-a` | Attach a named stream |
| `-v` | Volume mapping, `host:container` |
| `-p` | Port mapping, `hostport:containerport` |
| `-f` | Compose file (required for non-default filenames) |
| `--rm` | Delete container on exit |

## Source

Distilled from CS 4730 Distributed Systems — [[Week 01 - Introduction and Networking]] (slides
85–102) and the hands-on [[Docker Tutorial]].

- [Docker CLI reference](https://docs.docker.com/reference/cli/docker/) · [Dockerfile reference](https://docs.docker.com/reference/dockerfile/) · [DockerHub](https://hub.docker.com/) · [Compose docs](https://docs.docker.com/compose/)
- [[Code]]
