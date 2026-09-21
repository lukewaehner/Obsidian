---
tags:
  - docker
  - containers
type: note
related:
  - '[[Docker]]'
  - '[[Running Containers]]'
---
# Docker Exec

Runs a command in an **already running** container. The counterpart to
[[Running Containers|docker run]], which always makes a new one.

## Syntax

```bash
docker exec [OPTIONS] CONTAINER COMMAND [ARG...]
```

```bash
docker run --name ubuntu_bash --rm -i -t ubuntu bash
docker exec -d ubuntu_bash touch /tmp/execWorks
```

The result is a new file `/tmp/execWorks` inside the running container `ubuntu_bash`, created in
the background (`-d`).

## The Workhorse Form

```bash
docker exec -it <container> bash
```

A shell inside a live container. This is the debugging tool: check what the process actually sees —
which files, which environment, which network — rather than what the `Dockerfile` claims it should.

## Notes

- The container must be **running**. `docker exec` on an exited container fails; start it first.
- Changes made with `exec` live in the container's writable layer and **vanish when it is removed**. To make a change permanent, edit the [[Dockerfile]] and rebuild.
- `-d` backgrounds the exec'd command, not the container.

## See Also

- [[Running Containers]]
- [[Standard Streams]] — what `-i` and `-t` are doing
- [[Docker]]
