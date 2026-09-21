---
tags:
  - docker
  - images
  - registry
type: note
related:
  - '[[Docker]]'
  - '[[Images and Containers]]'
---
# Docker Registries

Docker maintains a **repository of images**. `pull` brings one down, `push` sends one up.

## Commands

```bash
docker pull [OPTIONS] NAME[:TAG|@DIGEST]
docker push [OPTIONS] NAME[:TAG]
```

```bash
docker pull debian
docker pull ubuntu:24.04
docker push registry-host:5000/myadmin/rhel-httpd
```

## Notes

- **You need a Docker account to push.** Pulling public images needs nothing.
- A name with no registry prefix defaults to DockerHub; `registry-host:5000/...` targets a private registry.
- `:TAG` defaults to `latest`. Pinning a real tag (`ubuntu:24.04`, not `ubuntu:latest`) is the difference between a reproducible build and a build that changes under you.
- `@DIGEST` pins the exact image content — stronger than a tag, which can be re-pointed.
- `docker run` pulls implicitly if the image is not present locally.

## See Also

- [[Images and Containers]]
- [[Inspecting Containers]] — `docker images` for what you already have
- [[Docker]]
