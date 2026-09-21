---
tags:
  - docker
  - containers
  - images
type: note
related:
  - '[[Docker]]'
  - '[[Images and Containers]]'
---
# Inspecting Containers

Two listing commands, one for each half of [[Images and Containers]].

## ps — containers

```bash
docker ps [OPTIONS]

docker ps      # running only
docker ps -a   # including exited
```

**Finished containers are saved on disk.** A bare `docker ps` hides them, which is why "I only ran
it once" and "I have thirty containers" are both true. `-a` is the honest view.

## images — images

```bash
docker images [OPTIONS] [REPOSITORY[:TAG]]

docker images        # everything
docker images java   # filter by repository
```

## Reading the Output

- `docker ps` columns worth knowing: `CONTAINER ID`, `IMAGE`, `COMMAND`, `STATUS`, `PORTS`, `NAMES`
- `PORTS` shows the [[Port Mapping|host-to-container port map]], which is the fastest way to answer "why can't I reach it"
- `NAMES` is what [[Docker Networking|bridge network DNS]] resolves, and what you pass to `docker exec` and `docker stop`

## See Also

- [[Removing Containers and Images]] — cleaning up what these reveal
- [[Docker Exec]]
- [[Docker]]
