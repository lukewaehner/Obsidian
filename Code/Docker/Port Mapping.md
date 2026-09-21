---
tags:
  - docker
  - containers
  - networking
type: note
related:
  - '[[Docker]]'
  - '[[Docker Networking]]'
---
# Port Mapping

> [!warning] Containers are **not accessible via networking from outside the host** by default.

Port mapping exposes a container port through a host port.

## Syntax

```bash
docker run -p HOSTPORT:CONTAINERPORT IMAGE
```

```bash
docker run -p 8001:5000 mycontainer1
docker run -p 8002:5000 mycontainer2
```

Accessing host port `8001` reaches `mycontainer1`; `8002` reaches `mycontainer2`. Both containers
listen on their own port 5000 internally and neither knows about the remapping.

## The Constraint

You can run multiple instances, but **each host port can be mapped only once**. That is the host's
own TCP rule, not a Docker one — it is why scaling a service to N replicas on one host needs N
distinct host ports (or a proxy in front).

## When You Don't Need It

Container-to-container traffic on a shared network does **not** need port mapping — containers
reach each other directly by name and internal IP. See [[Docker Networking]]. Map ports only when
something *outside* the host has to get in.

## See Also

- [[Docker Networking]] — the inside view
- [[Volume Mapping]]
- [[Docker]]
