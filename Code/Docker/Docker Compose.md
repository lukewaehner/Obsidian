---
tags:
  - docker
  - compose
  - orchestration
type: note
related:
  - '[[Docker]]'
  - '[[Docker Networking]]'
  - '[[Running Containers]]'
---
# Docker Compose

Orchestrates containers: the attributes and arguments you would type as `docker run` flags,
declared statically in YAML instead.

## Example

`composition.yml` — two containers on a bridge network, each printing a message and exiting:

```yaml
services:
  one:
    image: dockernetwork
    networks:
      - mynetwork
    hostname: "host1"
    command: echo "hello, host2"
  two:
    image: dockernetwork
    networks:
      - mynetwork
    hostname: "host2"
    command: echo "hello, host1"

networks:
  # The presence of these objects is sufficient to define them
  mynetwork: {}
```

```bash
docker compose -f composition.yml up
docker compose -f composition.yml up --build   # rebuild images first
docker compose -f composition.yml down
```

```text
[+] Running 2/2
 ⠿ Container lab3-two-1  Recreated
 ⠿ Container lab3-one-1  Recreated
Attaching to lab3-one-1, lab3-two-1
lab3-one-1  | hello, host2
lab3-two-1  | hello, host1
```

## Things Worth Knowing

- **Container names** are `<project>-<service>-<index>`, where the project name defaults to the directory name
- **`command:` overrides the image's default command** — which is how one image serves as every peer in a system
- **Declaring a network object is enough to create it.** No separate `docker network create` when Compose owns the network ([[Docker Networking]])
- **`-f` is required for non-default filenames.** A bare `docker compose up` only looks for `compose.yaml` / `docker-compose.yml`

## Why It's the Contract

For a multi-container system, the compose file *is* the system definition — it is the artifact you
hand someone so they can reproduce the whole topology with one command. Course projects are
evaluated by running the supplied compose file, so the YAML, not the `docker run` incantation in
your shell history, is the deliverable.

## See Also

- [[Docker Networking]]
- [[Dockerfile]] — what Compose builds from
- [Compose docs](https://docs.docker.com/compose/)
- [[Docker]]
