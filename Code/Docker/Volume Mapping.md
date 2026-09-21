---
tags:
  - docker
  - containers
  - storage
type: note
related:
  - '[[Docker]]'
  - '[[Running Containers]]'
---
# Volume Mapping

> [!warning] When the container ends, data is **not** persistent — it is lost.

A container's writable layer dies with the container. To keep data after the container ends, mount
a volume (a file or directory) from the host into the container.

## Syntax

```bash
docker run -v /host/path:/container/path IMAGE
```

```bash
docker run -v /opt/data:/var/lib/mysql mysql
```

`/var/lib/mysql` **inside the container** is mapped to `/opt/data` **on the host**. Host path first,
container path second — getting this backwards silently shadows the container path with an empty
host directory.

## Why It Matters

- Databases: the data directory must outlive the container, or every restart is a fresh install
- Development: mounting source into the container means editing on the host without rebuilding the image
- Logs: writing to a mounted directory keeps output after a crash

## See Also

- [[Port Mapping]] — the same host-first, container-second shape for networking
- [[Running Containers]]
- [[Docker]]
