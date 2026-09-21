---
tags:
  - docker
  - containers
  - images
type: note
related:
  - '[[Docker]]'
  - '[[Inspecting Containers]]'
---
# Removing Containers and Images

## Commands

```bash
docker rm [OPTIONS] CONTAINER [CONTAINER...]
docker rmi [OPTIONS] IMAGE [IMAGE...]
```

```bash
docker rm redis
docker rmi test:latest
```

## The Ordering Rule

> [!warning] You cannot remove an image before you have removed all containers that are using it.

This includes **exited** containers, which `docker ps` hides by default. When `docker rmi` refuses,
`docker ps -a` shows you why.

## Avoiding the Problem

```bash
docker run --rm myimage   # delete the container the moment it exits
```

`--rm` is the right default for anything you run interactively or to test — the container is
disposable, and not accumulating them means `rmi` never blocks.

## See Also

- [[Inspecting Containers]] — find what is holding the image
- [[Images and Containers]]
- [[Docker]]
