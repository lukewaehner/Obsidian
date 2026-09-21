---
tags:
  - docker
  - containers
type: note
related:
  - '[[Docker]]'
  - '[[Running Containers]]'
---
# Standard Streams

> [!warning] Containers are **not mapped to stdin, stdout, stderr by default**.

A container that reads from stdin will appear to hang, and one that prints may appear silent, until
the streams are wired up explicitly.

## The Flags

| Flag | Effect |
| --- | --- |
| `-i` | Attach **stdin** — interactive, keyboard input reaches the container |
| `-t` | Allocate a **tty**, so the container behaves like a terminal session |
| `-d` | **Detached** — run the container in the background |
| `-a` | **Attach** a specific stream: `stdout`, `stdin`, or `stderr` |

```bash
docker run -i mycontainer            # prompted for keyboard input
docker run -d mycontainer            # background
docker run -a mycontainer            # attach streams
docker run -i -a STDERR mycontainer  # stdin plus stderr only
```

`-it` together is the common pair: interactive shell in a terminal.

## Buffering Gotcha

> [!tip] Line-buffered stdout in a container is a recurring source of "my program printed nothing".
> A `printf` with no trailing newline can sit in the buffer indefinitely. Always terminate output
> with `\n`, or flush explicitly, when a grader or a peer is reading your output.

## See Also

- [[Running Containers]]
- [[Docker Exec]] — getting a shell in a container that is already running
- [[Docker]]
