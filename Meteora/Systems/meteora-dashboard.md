---
tags: [meteora, system]
sources:
  - meteora-dashboard/web
  - meteora-dashboard/capture
  - meteora-dashboard/schema
  - meteora-dashboard/deploy
  - meteora-dashboard/.github/workflows/deploy.yml
verified: 2026-08-27
---
# meteora-dashboard

## What it is

The desk's internal web app - investment charts, MCP analytics, memory-doc
browsing - behind Google SSO, plus the Python CLI that runs on the Bloomberg
desks and uploads the snapshots it draws.

## Diagram

```mermaid
flowchart LR
    A[Bloomberg desk<br/>capture CLI] -->|POST snapshot| B[/dashboard/api/ingest]
    C[meteora-mcp sync jobs] -->|POST snapshot| B
    B --> D[snapshot store]
    D --> E[Next.js app in web/]
    F[schema/*.json] -.->|read at runtime| E
    G[Google SSO<br/>@meteoracapital.com] --> H[web/proxy.ts]
    H --> E
    E --> I[nginx: /dashboard, /server, /_next/]
```

## How it works

### Two halves that share no toolchain

`web/` is a Next.js 16 app in a pnpm workspace, and almost all work happens
there. `capture/` is a Python CLI managed by `uv` that runs on desk machines,
parses local Excel, and POSTs snapshots. They meet only at the ingest endpoint
and the JSON schema, and neither can build the other.

There is **no root `package.json`**. Web commands are run as
`pnpm --dir web <cmd>` from the repo root.

### Snapshots and the runtime schema

Everything the app draws arrives as a snapshot POSTed to
`/dashboard/api/ingest`, keyed by module and `as_of`, written whole. Producers
are the desk capture CLI and the sync jobs on the box.

`schema/snapshot.schema.json` and `status.schema.json` are the contract, and
this is the surprising part: they are read **at runtime** by
`web/lib/validate.ts` and `web/lib/status.ts`, not compiled in. Editing a schema
file changes what the running service accepts, with no code change and no
rebuild. The same file is validated on both sides - `jsonschema` in Python,
Ajv in TypeScript - so the two can never drift into disagreeing about a shape.

### Auth

Google SSO restricted to `@meteoracapital.com`. `web/proxy.ts` gates every
request against a longest-prefix-wins table in `web/lib/auth/policy.ts` that
**defaults to `admin`**, so a new route nobody registered is admin-only rather
than public. Fails closed by construction.

Next 16 calls the middleware file `proxy.ts`. There is no `middleware.ts` and
adding one from memory is wrong.

Locally, `AUTH_MODE=stub` exposes an endpoint that mints a session without
Google. It 404s under `NODE_ENV=production` regardless of the setting, so it
cannot be reached on the box.

### Routing and serving

No `basePath`. The app serves `/dashboard/**` by route segment and nginx proxies
by path, forwarding only `/dashboard`, `/server`, `/_next/` and `= /favicon.ico`.

### Design system

Colour, radii and type scale live as custom properties on `:root` in
`web/app/theme.css` with a `prefers-color-scheme: dark` override, so a page gets
both schemes for free and components declare no literal colours. The one
documented exception is the ECharts chrome, because ECharts paints to canvas and
cannot read CSS custom properties.

Charts split transform from option: pure data reshaping in a `*-transform.ts`,
unit-tested directly, and the ECharts config in a `*-option.ts`. That seam is
why the chart logic is testable at all.

## Why it's this way

Reading the schema at runtime rather than compiling it in is what lets one file
be the single source of truth for two languages. The cost is that a schema edit
is a production change, which is why it belongs in Traps as well as here.

Auth defaulting to `admin` inverts the usual failure. Forgetting to register a
route makes it inaccessible, which someone notices immediately, instead of
making it public, which nobody notices at all.

The desk capture CLI exists because Bloomberg data can only be read from a
machine with a terminal. Everything that _can_ move to the box has been moving
there - the universe, the spacresearch export, the Yield Model read - and what
is left on a desk is the part that genuinely cannot run anywhere else.

## Traps

- **Pushing to `main` deploys to production.** There is no staging.
- **`capture/` is not covered by CI.** The gate job is `web`-only, so a change
  under `capture/` gets no automated check at all. Run
  `uv run --directory capture pytest` yourself or it ships unverified.
- **There is no `ci.yml`, only `deploy.yml`.** The gate is a job inside the
  deploy workflow.
- **Editing `schema/*.json` changes the running service.** It is read at
  runtime, so there is no build step standing between the edit and production.
- **Always use `pnpm --dir web`, never bare from the repo root.**
  `web/lib/validate.ts` and `web/lib/status.ts` resolve `../schema/*.json` off
  `process.cwd()` and throw **at import** if it is not `web/`. A wrong cwd looks
  like a mysterious schema-not-found crash in unrelated tests.
- **The package manager is pinned to pnpm 10.27.0.** npm and yarn are wrong
  here.
- **Two different Node floors, deliberately.** The box needs 20.9 for `next@16`,
  CI needs 22.22.2 because vitest crashes below it on `jsdom@30`. The box never
  runs vitest.
- **This is not the Next.js you remember.** `next@16.3.0` differs from the
  widely published APIs. Read `web/node_modules/next/dist/docs/` rather than
  trusting recall.
- **Phantom `tsc` errors on `LayoutProps` / `PageProps` are a stale
  `.next/types`**, not your source. `next dev` writes to `.next/dev/types/`
  while `next build` writes `.next/types/`, and the tsconfig includes both.
  Build once before hunting in the route file.
- **Never serve assets from `web/public/`.** nginx does not proxy top-level
  paths, so such a URL 404s in production. Import images as modules.
- **`docs/` is empty by design.** Design docs live outside the repo at
  `docs/superpowers/meteora-dashboard/` in the workspace.
- **Any `ENTRA_*` variable is dead.** Entra SSO was replaced by Google
  Workspace SSO.

## Where to start reading

| # | File | Why this rung |
| --- | ------------------------------- | ------------------------------------------------------------------- |
| 1 | `web/README.md` | Routes, auth, local dev, the design system. Its Deployment section is stale - the deploy job is path-filtered now. |
| 2 | `schema/snapshot.schema.json` | The contract every producer and the whole app agree on. |
| 3 | `web/proxy.ts` and `web/lib/auth/policy.ts` | How every request is gated, and why an unregistered route is admin-only. |
| 4 | `web/lib/validate.ts` | The runtime schema read, and the cwd assumption behind it. |
| 5 | `capture/src/` | The desk half: what it parses and what it POSTs. |
| 6 | `deploy/README.md` | Provisioning and operations end to end. |

> **Read 1-3 to defend it. Add 4-6 before you change it.**

## Making changes

### The gate

```bash
pnpm --dir web install --frozen-lockfile
pnpm --dir web lint
pnpm --dir web test
pnpm --dir web build
```

Exactly what CI's gate job runs, in that order. None of the four needs an
environment variable or a secret - CI runs them on a bare checkout.

The Python half is separate and ungated:

```bash
uv sync --directory capture
uv run --directory capture pytest
```

### Test structure

vitest in `web/test/` (`*.test.ts`, `*.test.tsx`, jsdom) - roughly 92 files and
857 cases. Playwright lives in `web/e2e/` (`*.spec.ts`) and the vitest config
excludes it, so the two never collide. Put a unit test with its peers in
`web/test/`, not beside the source.

Playwright is deliberate, not habitual: it downloads ~150MB of Chromium and its
`webServer` binds `:3000`, so two people cannot run it at once, and outside CI
it will silently attach to whatever dev server is already on that port - with
different env and fixtures. Stop yours first.

```bash
pnpm --dir web exec playwright test
```

### CI

`deploy.yml` carries both jobs. The `gate` job runs the four web commands above
on every PR, plus Playwright when `web/**` changed. The deploy job needs the
gate and is itself path-filtered, so a docs-only push no longer redeploys.

### Deploy

On push to `main`, a self-hosted runner on the box syncs, builds `/dashboard`,
restarts the service, health-checks it, and rolls back on failure. The unit and
nginx site live in `deploy/`.

### Manual QA

```bash
cd web
UPLOAD_TOKEN=devtok SNAPSHOT_STORE=memory SESSION_SIGNING_SECRET=dev \
  AUTH_MODE=stub BOOTSTRAP_ADMIN_EMAIL=you@meteoracapital.com pnpm dev
```

`SNAPSHOT_STORE=memory` avoids needing S3 or AWS credentials, and the stub auth
endpoint mints a session with a curl. Charts stay empty until you seed a
snapshot - `web/README.md` has the command.

What you cannot exercise locally: the real Google SSO flow, a genuine upload
from a desk machine, and anything reading Bloomberg. `/dashboard/server` panels
render empty under a banner unless `MCP_LOG_DIR` points at a directory holding
`mcp.jsonl` and `registry.json`; the e2e fixture writes a usable one. The Neo4j
and Pinecone panels show an inline "not configured" state, so skipping them is
fine.

### Traps

- `.gitignore` has unanchored `build/`, `dist/` and `*.spec` patterns, partly
  reclaimed for `capture/build/`. A **new** `.spec` file under `capture/build/`
  is still ignored and will silently not commit. Check `git status` after adding
  files there.
- `web/AGENTS.md` is rewritten by `next dev`. If it shows up modified and you
  did not touch it, commit it with your work rather than reverting.
- Secrets come from `meteora-secrets`, rendered to `/etc/meteora-dashboard/env`
  on the box. Never add a plaintext env file to the tree.

## Related

- [[meteora-mcp]] - publishes the universe, deadlines and extensions feeds into
  this app's ingest endpoint
- [[spacresearch.sqlite]] - behind `/dashboard/universe`
- [[S3]] - the snapshot store the app reads
- [[Bloomberg]] - the desk-side capture half of this repo
- [[meteora-ingest]] - writes the `status.json` behind `/database`
- [[Meteora]]
- [[Glossary]] - snapshot / ingest, the two universes
