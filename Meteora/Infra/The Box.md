---
tags: [meteora, infra]
sources:
  - meteora-infra/ansible/group_vars/all.yml
  - meteora-infra/ansible/roles
  - meteora-infra/terraform
verified: 2026-08-27
---
# The Box

## What it is

One `t3.xlarge` in `us-east-2`, account `309128776621`, behind an Elastic IP.
Everything server-side the firm runs is on it: four applications, Neo4j, Caddy,
five GitHub Actions runners, and a set of timers and cron jobs.

Sixteen GiB of RAM, one 50 GiB root volume, and no second machine.

## Diagram

The estate's own three-diagram set is in [[Meteora]] - diagram 3 is this box.
`meteora-infra/docs/architecture.md` has the AWS footprint and the request path
as committed Mermaid.

## How it works

### One machine, four tenants, pinned identities

Each application gets a service user and a deploy user, an FHS layout, and
numeric ids that are **pinned rather than arbitrary**:

| App | Service user | Deploy user | Checkout |
| --------------- | ------------ | ------------- | ----------------------- |
| meteora-mcp | `mmcp` | `mmcp-deploy` | `/srv/meteora-mcp` |
| meteora-dashboard | `mdash` | `mdash-deploy` | `/srv/meteora-dashboard` |
| meteora-ingest | `ming` | `ming-deploy` | `/srv/meteora-ingest` |
| meteora-scripts | `mscr` | `mscr-deploy` | `/srv/meteora-scripts` |

Plus `/etc/<app>` for configuration, `/var/lib/<app>` for state, and
`/var/log/<app>` for logs.

The uids and gids are pinned because **ownership on `/srv` and `/etc/<app>` is
by numeric id**. A staging box built with different ids would diff against prod
on every path and mask the real drift the staging comparison exists to find.

Three irregularities are deliberate and documented as such: `scripts` is the
only app whose deploy user has its own group rather than sharing the service
group, `mscr` and `mscr-deploy` have home directories that break the naming
pattern, and `mmcp` is a secondary member of the `mscr` group.

### The service/deploy split

The reason there are two users per app rather than one is the same everywhere,
and [[meteora-scripts]] states it most plainly: the deploy runs the repo's own
test suite on the box, so landing a commit on `main` is code execution as
whatever account runs it. The service account meanwhile reads production
credentials and ingests untrusted content. The runner account must be able to do
neither.

So a service account typically has **no write access to its own checkout**.
Everything it writes at run time lives outside: locks in `/run/lock`, logs in
`/var/log/<app>`, state in `/var/lib/<app>`.

### Caddy is the only ingress

One domain, TLS terminated by Caddy, routing by path to two loopback services:

- `/dashboard`, `/dashboard/*`, `/server`, `/server/*`, `/_next`, `/_next/*`,
  `/favicon.ico` go to the Next.js app on `127.0.0.1:3000`.
- **Everything else** goes to meteora-mcp on `127.0.0.1:8000`, with
  `flush_interval -1` because SSE needs it.

The dashboard match uses `handle`, not `handle_path`, and names both the bare
`/dashboard` and `/dashboard/*` so the canonical URL does not fall through to
the MCP. Access logs for both apps are JSON at `/var/lib/caddy/access.log`,
which is where an ingest problem is debugged.

Note the shape: the MCP server is the **default**, not a registered route. A new
path is meteora-mcp's unless somebody adds it to the dashboard matcher.

### What is scheduled

Timers, all with `OnFailure=alert-on-failure@%n.service` so a break emails:

| Unit | When |
| ------------------- | ---------------------------------- |
| `universe-sync` | hourly, `RandomizedDelaySec=300` |
| `spacresearch-sync` | hourly, `RandomizedDelaySec=600` |
| `extensions-sync` | hourly, `RandomizedDelaySec=900` |
| `neo4j-backup` | 03:00 UTC |
| `cert-expiry-check` | 04:00 UTC |
| `disk-space-check` | every 6 hours |

The three Drive syncs stagger their randomized delay so they do not contend for
the same Drive credential on the hour.

Cron, separately: the [[meteora-ingest]] dispatcher every five minutes, and the
[[meteora-scripts]] harvest at three Eastern hours on weekdays.

### Neo4j is a co-tenant, and it is capped for a reason

Neo4j runs on the same box with bolt bound to `127.0.0.1` only. Its memory caps
- 2g heap, 1g pagecache - are **load-bearing rather than tuning**: without them
the JVM claims whatever RAM is available and starves meteora-mcp. At those
values the JVM footprint is about 4-5 GiB, leaving roughly 10 GiB for everything
else. See [[Neo4j]].

### Five runners

Self-hosted GitHub Actions runners, one per repo except ingest which has two:
`meteora-prod-aws` (mcp), `meteora-box` (dashboard), `ingest-runner` and
`ingest-runner-2`, and `meteora-scripts`. Each runs as its repo's deploy user.

## Why it's this way

One box rather than several is a cost and complexity decision, and the whole
identity scheme is what makes it survivable. Separate users, separate FHS
paths, and separate deploy accounts mean the four applications share hardware
without sharing blast radius.

Pinning the numeric ids turns "the boxes match" from an assertion into something
a fact diff can check. That check is [[meteora-infra]]'s only real gate.

## Traps

- **There is no second box.** No staging that stays up, no failover. The staging
  box is built from scratch, diffed, and destroyed.
- **A new Caddy path belongs to meteora-mcp by default.** The dashboard matcher
  is an allowlist.
- **Removing Neo4j's memory caps starves the MCP server.** They are not there
  for Neo4j's benefit.
- **`meteora-ingest`'s own status doc names `ubuntu` and
  `/home/ubuntu/meteora-ingest/status`**, while the infra repo provisions
  `ming` under `/srv/meteora-ingest`. One of the two is stale - almost certainly
  the app doc, which predates the FHS multi-tenant layout. Check the box before
  following either, because this specific fact is a permission grant and getting
  it wrong silently blanks a dashboard page.
- **SSH is open to `0.0.0.0/0`.** See [[meteora-infra]].
- **`/run` is a tmpfs wiped at boot.** Lock files there are recreated by
  systemd-tmpfiles, not by a one-time mkdir.

## Where to start reading

| # | File | Why this rung |
| --- | ------------------------------------------ | -------------------------------------------------- |
| 1 | `meteora-infra/docs/architecture.md` | The layer boundary, the AWS footprint, the request path. |
| 2 | `meteora-infra/ansible/group_vars/all.yml` | `meteora_apps` - every user, uid and path, with the irregularities called out. |
| 3 | `meteora-infra/ansible/roles/caddy/templates/Caddyfile.j2` | The whole ingress, in twenty lines. |
| 4 | `meteora-infra/ansible/roles/` | `base`, `identity`, `layout`, `apps`, `ops`, `runners`. |
| 5 | `meteora-infra/docs/operations/box-rebuild.md` | What a rebuild actually involves. |

> **Read 1-3 to defend it. Add 4-5 before you change it.**

## Related

- [[meteora-infra]] - the repo that builds all of this
- [[Deploys]] - what lands on it, and how each path differs
- [[Auth]] - what guards the two services Caddy fronts
- [[Neo4j]] - the co-tenant with the memory cap
- [[Meteora]]
- [[Glossary]] - the box
