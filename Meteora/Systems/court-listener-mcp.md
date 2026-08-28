---
tags: [meteora, system]
sources:
  - court-listener-mcp/app
  - court-listener-mcp/docker-compose.yml
  - court-listener-mcp/README.md
  - meteora-mcp/tools/courtlistener
  - meteora-mcp/services/courtlistener
verified: 2026-08-27
---
# court-listener-mcp

## What it is

A third-party FastMCP server wrapping the CourtListener REST API v4 and the
eCFR. It sits in the workspace as a **reference implementation**, not as a
running service.

## The thing to know first

There are two CourtListener surfaces and only one of them is in use.

| | This repo | `meteora-mcp/tools/courtlistener/` |
| --------- | ------------------------------------------ | -------------------------------------------------- |
| Shape | standalone FastMCP server in Docker | a tool area inside the main MCP server |
| Tools | ~35, including citation verification and full eCFR | five: `caselaw-search`, `caselaw-opinion`, `docket-search`, `docket-details`, `docket-filings` |
| Auth | none of ours - `.env` and a container port | Cognito, like every other tool |
| Deployed | **no** - `meteora_apps` in meteora-infra does not name it | yes, on the box, gated on `COURTLISTENER_API_KEY` |

**The port inside meteora-mcp is what is live.** This repo was read for its API
knowledge and then left in place.

## How it works

### What was actually taken

None of the plumbing transferred. This is FastMCP - `@mcp.tool()` decorators,
sub-servers imported under name prefixes, its own lifespan and httpx client,
stdio/http/sse transports. meteora-mcp is a hand-rolled registry table behind
Starlette and Cognito, and the two have no shared abstraction.

What transferred is API knowledge: endpoint paths, the v4 `type=` search codes,
and the response shapes. Roughly 150 lines of real content spread across about
1,100 lines of source.

Two use cases were selected for the port - precedent research (how courts have
ruled on MAE clauses, specific performance, appraisal fair value) and deal
litigation tracking (antitrust suits to block, Delaware Chancery merger
challenges, appraisal actions, SPAC securities suits). Citation verification was
explicitly **not** selected, which removed the `citeurl` dependency entirely.

### What this repo still offers

The wider tool surface. If a question needs eCFR regulation search, citation
parsing, oral argument audio or judge lookup, the code for it is here and is not
in meteora-mcp. Running it means running the container.

## Why it's this way

Porting five tools rather than mounting thirty-five is a decision about surface
area. Every tool in the main server is one more thing Claude must choose between,
one more thing behind Cognito, and one more thing to keep working. The two
selected use cases are the ones the desk actually has.

Keeping the source repo rather than deleting it preserves the reference. When a
sixth tool is wanted, the endpoint knowledge is here rather than needing to be
rediscovered from the API docs.

## Traps

- **No CI.** There is no `.github/`.
- **Docker-based, not `uv`-based.** Every run and test command here looks
  nothing like the rest of the estate - there is no `uv sync`, no
  `scripts/check.py`, no `pnpm --dir`. Reaching for the muscle memory from
  another repo will not work.
- **Its README describes the tools as production-ready.** They are production
  ready _for the upstream project_. Nothing here is deployed by us.
- **The workspace design doc for the port still says "Approved, not yet
  implemented".** The port shipped - the five tools are registered in
  meteora-mcp. Believe the handlers.

## Where to start reading

| # | File | Why this rung |
| --- | ---------------------------------------- | ------------------------------------------------------- |
| 1 | `README.md` | The full tool surface, so you know what exists to be ported. |
| 2 | `meteora-mcp/tools/courtlistener/handlers.py` | What was actually taken, and its shape in our idiom. |
| 3 | `meteora-mcp/services/courtlistener/` | The live client, its cache and its quota ledger. |
| 4 | `app/tools/` | The upstream implementations, when a new endpoint is needed. |
| 5 | `docker-compose.yml` | How to run this one, if you ever need to. |

> **Read 1-3 to defend it. Add 4-5 before you change it.**

## Making changes

Almost always, the change belongs in `meteora-mcp` rather than here. Adding a
sixth CourtListener tool means writing a handler and a service function in that
repo, using this repo as the endpoint reference, and following that repo's gate.

### The gate

There isn't one here. No CI, no `scripts/check.py`, and the tests in `tests/`
are the upstream project's.

### Deploy

None. `meteora_apps` in meteora-infra does not name it, so nothing on the box
creates a user, a directory or a unit for it.

### Manual QA

```bash
docker compose up --build
```

Serves on `:8000` with a socket-connect healthcheck, reading a `.env` in the
repo root. Attach it to a client as an HTTP MCP server.

The live path is the other one: the five ported tools go through the meteora-mcp
dev server like any other tool.

## Related

- [[meteora-mcp]] - where the live CourtListener tools actually are
- [[Glossary]]
