---
tags: [meteora, surface]
sources:
  - meteora-dashboard/web/app
  - meteora-dashboard/web/lib/auth/policy.ts
  - meteora-dashboard/web/proxy.ts
verified: 2026-08-27
---
# Dashboard Pages

## What it is

Eleven pages under `/dashboard`, each gated by an access level and each fed by a
different upstream. This note is the map of which page shows what, from where,
and to whom.

For the app's build, toolchain and deploy, see [[meteora-dashboard]].

## The pages

| Path | Access | Shows | Fed by |
| --------------------------- | ------ | ------------------------------------- | ------------------------------------------ |
| `/dashboard` | auth | the landing charts | snapshots in [[S3]] |
| `/dashboard/login` | public | the Google SSO entry point | - |
| `/dashboard/no-access` | admin\* | the rejection page | - |
| `/dashboard/universe` | auth | the SPAC universe table | [[spacresearch.sqlite]] via the ingest feed |
| `/dashboard/memory` | auth | the memory-doc browser | [[S3]] `memory/` projections |
| `/dashboard/memory/[...name]` | auth | one memory doc | the same projections |
| `/dashboard/memory/activity` | auth | recent memory-doc activity | the same projections |
| `/dashboard/memory/questions` | auth | memory-doc questions | the same projections |
| `/dashboard/tools` | auth | the MCP tool catalog and parameters | `registry.json` from [[meteora-mcp]] |
| `/dashboard/dev` | dev | operational panels: logs, database, graph | `mcp.jsonl`, [[Neo4j]], [[Pinecone]], ingest `status.json` |
| `/dashboard/admin` | admin | user and role administration | the app's own store |

\* `no-access` matches no rule and therefore inherits the default. See below.

The Extensions view lives on the landing page rather than its own route, fed by
the `extensions` trail snapshot - the box half from [[Bloomberg]]'s split.

## How access works

`web/proxy.ts` gates every request against a longest-prefix-wins table in
`web/lib/auth/policy.ts`, matched **on segment boundaries** rather than raw
`startsWith` - otherwise `/dashboard/servers-public` would inherit `dev` from
`/dashboard/server`.

Five access levels: `public`, `token`, `auth`, `dev`, `admin`.

**A pathname matching no rule resolves to `admin`**, the most restrictive tier.
A route someone forgot to register fails closed and is noticed immediately,
rather than quietly serving to everyone. That default is the single most
important line in the file.

### The `token` level, and why some children are carved out

Three routes are read by machines rather than browsers, using the upload token
instead of a session:

- `/dashboard/api/ingest` - every producer POSTs here.
- `/dashboard/api/universe/deadlines` - the desk's yield capture.
- `/dashboard/api/extensions/latest` - the desk's extensions price pass.
- `/dashboard/api/history/panel` - the desk verifier.

Each is deliberately registered as a **child** of a browser-facing parent so the
parent keeps its session requirement. `/dashboard/api/universe` stays `auth`;
only its `deadlines` child is `token`. Reclassifying the parent would open the
browser-facing route.

`/dashboard/api/extensions/latest` exists as its own path for exactly this
reason - the snapshot route the browser fetches must stay session-gated.

The token itself is checked inside the route handler, not by the policy table.
The table only says "a session is not what gates this".

### Two operator surfaces, and a redirect

The Server and Database pages now live under `/dashboard/dev`. Both old URLs
redirect there in `proxy.ts`, ahead of the policy table. `/dashboard/server`
stays in the table anyway because `/dashboard/server/api/*` still resolves under
it.

Note that `/server` on the box is a **different thing entirely** - it is
meteora-mcp's own operational dashboard, gated by a shared secret rather than by
SSO, and Caddy routes it to the Next.js app. See [[Auth]].

### What is auth and not dev

Three read-only surfaces are deliberately available to every authenticated desk
user rather than to developers only: `/dashboard/memory`, `/dashboard/universe`
and `/dashboard/tools`. Each carries a comment saying so, because the instinct
to file them under `dev` is exactly what the comments exist to stop.

## Why it's this way

Defaulting to `admin` inverts the usual failure. Forgetting to register a route
makes it inaccessible - which someone reports within the hour - instead of
making it public, which nobody reports at all.

Carving token access out as a child path rather than reclassifying a parent
keeps the blast radius of a machine integration to exactly the endpoint that
integration reads.

## Traps

- **A new route nobody registered is admin-only.** If a page you just added
  404s or bounces, register it.
- **Match is on segment boundaries.** `/dashboard/serverless` does not inherit
  `/dashboard/server`.
- **`/dashboard/server` and `/server` are different surfaces** with different
  auth. One is a Next.js route, the other is meteora-mcp's own dashboard.
- **The token-gated children must stay children.** Promoting one to its parent
  path opens a browser-facing route to anyone holding the upload token.
- **`/dashboard/api/memory/seed` is a Playwright-only backdoor** carrying its
  own token and its own guards. It is not a general seeding endpoint.

## Where to start reading

| # | File | Why this rung |
| --- | --------------------------------- | -------------------------------------------------------- |
| 1 | `web/lib/auth/policy.ts` | The whole table, with the reasoning for every carve-out inline. |
| 2 | `web/proxy.ts` | The gate itself, plus the redirects that run before the table. |
| 3 | `web/app/dashboard/` | The pages, one directory per route. |
| 4 | `web/README.md` | Routes and the design system, from the app's own point of view. |

> **Read 1-2 to defend it. Add 3-4 before you change it.**

## Related

- [[meteora-dashboard]] - the app itself
- [[MCP Tools]] - what `/dashboard/tools` lists
- [[Auth]] - Google SSO, and the four other auth systems
- [[S3]], [[spacresearch.sqlite]] - what most of these pages read
- [[Meteora]]
- [[Glossary]] - snapshot / ingest
