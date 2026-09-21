---
tags:
  - docker
  - containers
  - images
type: note
related:
  - '[[Docker]]'
  - '[[Dockerfile]]'
  - '[[Docker Registries]]'
---
# Images and Containers

Docker is an application that lets you **create and build containers** — a set of commands for
manipulating two things, and it is worth never confusing them.

## The Distinction

- **Image** — a complete and executable version of an application. Immutable, built from a [[Dockerfile]], stored in a registry.
- **Container** — the **instantiation** of an image. Mutable, running (or exited), has its own PID, IP, and writable layer.

> Image is to container as **class is to object**. One image, any number of containers, each
> consuming its own system resources.

## Layers

Images are built in **layers**. Each layer either

1. adds files to the image filesystem,
2. runs a command, or
3. defines an attribute of the containers built from it.

Layers are cached and shared, which is why the second build of an image takes seconds and why
reordering a `Dockerfile` changes build times dramatically.

## Lifecycle

```bash
docker build . -t myapp   # Dockerfile -> image
docker run myapp          # image -> container
docker ps -a              # containers, including exited ones
docker rm <container>     # remove container
docker rmi myapp          # remove image (only after its containers are gone)
```

Docker maintains a **repository** of images — see [[Docker Registries]].

## See Also

- [[Dockerfile]] — how images get built
- [[Inspecting Containers]] — listing both
- [[Removing Containers and Images]]
- [[Docker]]
