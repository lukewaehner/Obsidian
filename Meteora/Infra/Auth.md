---
tags: [meteora, infra]
sources:
  - meteora-mcp/services/auth
  - meteora-mcp/docs/operations/dashboardAuth.md
  - meteora-mcp/docs/operations/skillsApi.md
  - meteora-dashboard/web/lib/auth
verified: 2026-08-27
---
# Auth

## What it is

**Five separate auth systems, none of which knows about the others.** Which one
applies depends entirely on which URL you are hitting, and the failure modes are
all different.

This is the note to read before asking "why can this person not get in".

## The five

| Surface | Guarded by | Identity | Fails as |
| ----------------------------- | ------------------------ | ---------------------- | -------- |
| `/mcp` | Cognito bearer token | a person or a machine | 401 |
| `/dashboard/**` | Google SSO | a person's Workspace account | redirect to login |
| `/server` (on the box) | `DASHBOARD_SECRET` | none - a shared secret | 401 |
| `/skills-api/*` | `SKILLS_API_SECRET` | none - a shared secret | 401 |
| `/dashboard/api/ingest` etc. | `UPLOAD_TOKEN` | none - a shared secret | 401/409 |

Four of the five are on the same host, fronted by the same Caddy. See
[[The Box]].

## How each works

### Cognito, for `/mcp`

Every `/mcp` request carries a bearer token verified before the MCP session
manager sees it. The server also serves two OAuth discovery documents under
`/.well-known/`, which is what lets claude.ai run a normal login flow against
Cognito and come back with a token - that facade is why a person can add the
server as a custom connector without anyone handing them a credential.

Authorization is two orthogonal checks, both re-run at dispatch: an ordered
**tier** ladder (`intern`, then `analyst`, where the tier name is the Cognito
group name) and exact-membership **compartments**, which a high tier does not
grant. See [[MCP Tools]].

Machine clients authenticate by client credentials rather than a user login and
are listed in their own setting.

`AUTH_ENABLED=false` disables all of it, which is what the dev server does. On
the box, a startup log line records the pool, client, callback list and secret
fingerprint - every "why can this person not sign in" investigation starts by
asking what the process thinks its identity config is.

### Google SSO, for the dashboard

Restricted to `@meteoracapital.com`. `web/proxy.ts` gates every request against
a longest-prefix-wins policy table that **defaults to `admin`**, so an
unregistered route fails closed. Five access levels, and a `token` level for
machine callers. Full detail in [[Dashboard Pages]].

Any `ENTRA_*` variable you find is dead - Entra SSO was replaced by Google
Workspace SSO.

### Two shared secrets, deliberately separate

`DASHBOARD_SECRET` gates meteora-mcp's own `/server` operational dashboard -
tool-call logs, per-user activity, errors, Neo4j and Pinecone status.
`SKILLS_API_SECRET` gates `/skills-api/*`.

They are **not** the same secret on purpose: `/server` is read-only operational
data, `/skills-api` **writes to Drive**, and the two should be independently
rotatable.

Both fail closed with no bypass flag - unset or empty rejects everything with
401 regardless of the header sent - and both compare with `hmac.compare_digest`
rather than `==`, so a wrong guess leaks no timing information.

### The upload tokens, and the pair people mix up

Two tokens guard the dashboard's ingest endpoint, and the distinction is the one
most likely to bite:

- **`UPLOAD_TOKEN`** is held by every desk machine and by the sync jobs. It
  covers the ordinary ingest branches.
- **`UNIVERSE_UPLOAD_TOKEN`** gates the `universe` branch alone, and is held
  **only** in the dashboard's env on the box, never in a desk config.

The reason is that `/api/ingest` does a **whole-record replace** on a `universe`
post. Before the second token, a desk running a stale config could silently
replace the server-published universe with a six-week-old one. Presenting the
desk token on that branch is refused with a 409, and the refusal surfaces
readably in the run summary rather than as a silent no-op.

`UPLOAD_TOKEN` is shared rather than copied under a second name - one key, two
consumers, one place to rotate. See [[SPACResearch Export]].

## Why it's this way

Five systems rather than one is not accident so much as accepted cost. The
identities are genuinely different: a person in Claude, a person in a browser, a
machine on the same box, and a desk laptop. Unifying them would mean giving a
desk laptop a person-shaped identity, which is worse.

Every one of them fails closed, and that consistency is the thing that actually
holds the estate together. Unset secret, unregistered route, unresolved group -
all of them deny rather than allow.

Splitting the universe token off is the clearest example of the general rule
here: when one credential can do something irreversible, give that thing its own
credential and hold it in fewer places.

## Traps

- **"Connected, but nothing works" is an empty-groups problem.** A caller whose
  Cognito groups resolve empty drops to the lowest tier and gets a truncated
  tool list, which the client reports as a successful connection.
- **`/server` and `/dashboard/server` are different surfaces** with different
  auth - one is meteora-mcp's, gated by a shared secret; the other is a Next.js
  route gated by SSO.
- **A new dashboard route nobody registered is admin-only.**
- **Presenting `UPLOAD_TOKEN` on the `universe` ingest branch is a 409**, not a
  401, and not a silent no-op.
- **A blank JSON-typed auth variable takes the box down at import.**
  `COGNITO_MACHINE_CLIENT_IDS` and `OAUTH_EXPECTED_REDIRECT_URIS` are in that
  set. See [[Secrets]].
- **There is no unauthenticated bypass anywhere**, including locally. The dev
  server disables Cognito outright rather than weakening it.

## Where to start reading

| # | File | Why this rung |
| --- | ------------------------------------------ | ----------------------------------------------------- |
| 1 | `meteora-mcp/services/auth/cognito.py` | Token verification, groups, the discovery metadata. |
| 2 | `meteora-dashboard/web/lib/auth/policy.ts` | The route table and its admin default. |
| 3 | `meteora-mcp/docs/operations/dashboardAuth.md` | The `/server` secret, stated completely and briefly. |
| 4 | `meteora-mcp/docs/operations/skillsApi.md` | The second secret, and why it is separate. |
| 5 | `meteora-mcp/registry.py` | `_caller_allowed` - where tier and compartment are actually enforced. |

> **Read 1-3 to defend it. Add 4-5 before you change it.**

## Related

- [[MCP Tools]] - tiers, compartments, and the per-caller catalog
- [[Dashboard Pages]] - the route table in full
- [[Skills API]] - the write surface with its own secret
- [[Secrets]] - where every one of these values comes from
- [[The Box]]
- [[Meteora]]
