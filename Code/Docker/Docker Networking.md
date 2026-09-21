---
tags:
  - docker
  - networking
  - containers
type: note
related:
  - '[[Docker]]'
  - '[[Port Mapping]]'
  - '[[Docker Compose]]'
---
# Docker Networking

Installing Docker creates **three networks**.

| Network | What it is |
| --- | --- |
| `bridge` | An internal private network. Every container gets an IP on it (the `172.17.x.x` range) |
| `host` | No isolation — the container shares the host's network stack directly |
| `none` | No networking at all |

Containers on `bridge` can talk to each other **using those IPs**. To reach them from outside the
host there are several solutions; one is [[Port Mapping]].

## Default Bridge vs User-Defined Bridge

This is the distinction that actually bites.

```bash
docker network list                              # what exists
docker network create --driver bridge mynetwork  # make your own
```

> [!important] Only a **user-defined** bridge provides container name-to-IP resolution.
> On the default bridge you must know the IP, which changes every launch. On a user-defined
> network, the container **name** resolves.

That is what makes a static peer list work: hostnames stay valid across runs as long as the
container names do, instead of needing fresh IPs every launch.

## Demonstrating It

Two containers on the same user-defined network, addressing each other by name:

```bash
docker run -it --name first  --network mynetwork dockernetwork
docker run -it --name second --network mynetwork dockernetwork
```

```bash
# in `first` — listen
netcat -nvlp 3000

# in `second` — connect by container name, no IP anywhere
netcat -v first 3000
```

`netcat` switches: `-n` no DNS, `-v` verbose, `-l` listen, `-p` port.

> [!warning] On `ubuntu:24.04`, `apt-get install -y netcat` fails — `netcat` is a virtual package
> with no default provider. Install **`netcat-traditional`** (matches the `-nvlp` flag syntax
> above) or `netcat-openbsd`.

## Compose Shortcut

In [[Docker Compose]], the mere presence of a `networks:` entry creates it — no
`docker network create` step:

```yaml
networks:
  mynetwork: {}
```

## See Also

- [[Port Mapping]] — reaching a container from outside the host
- [[Docker Compose]]
- [[Docker]]
