---
tags: [meteora, glossary]
sources:
  - meteora-mcp/docs/operations
  - meteora-mcp/CLAUDE.md
  - meteora-mcp/services/arbjournal
  - meteora-mcp/services/skills
verified: 2026-08-27
---
# Glossary

Words that mean two things, and words the desk uses without defining.

## universe

**Two different databases, and they are not interchangeable.** Someone who does
not know there are two will write a correct query against the wrong one and get
plausible wrong numbers.

| | `universe.sqlite` | `spacresearch.sqlite` |
| ------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| Comes from | a vendor workbook uploaded by hand to Drive | spacresearch.com native exports |
| Shape | one sheet flattened to one table, ~50 columns, ~1880 rows | relational: `spacs`, `sponsors`, `_meta` |
| On the box | `/var/lib/meteora-mcp/universe/current.sqlite` | `/var/lib/meteora-mcp/spacresearch/current.sqlite` |
| Synced by | `scripts/sync_universe.py`, `universe-sync.timer` | `scripts/sync_spacresearch.py`, `spacresearch-sync.timer` |
| Refreshed when | a human uploads a new dated workbook | a human runs the weekly-update skill |
| Feeds | `universe-query`, `universe-schema`, the deadlines feed | `/dashboard/universe` |

Only `spacresearch.sqlite` carries `warrant_strike`, `counsel`, and the
free-text `unit_specs` / `warrant_specs` / `right_specs` the structural screens
are built on. The workbook cannot substitute for it, which is why both syncs
exist. They are separate systemd units on purpose: a broken SPAC Research
export must not stop the desk's deadlines map from publishing.

A third thing is also called the universe in conversation - the set of live
SPACs itself, independent of which file you read it out of. Harmless in speech,
expensive in a query.

Full detail: `meteora-mcp/docs/operations/universeSync.md` and
`spacresearchSync.md`.

## CIT

Cash in trust, per share. The trust balance divided by shares outstanding -
`121,464,805 / 12,075,000 = 10.06`.

Two independent sources carry it and they disagree on purpose. The
[[#yield model]] holds the desk's last-known figure, VLOOKUP'd by ticker. EDGAR
holds whatever the newest 10-Q or 10-K reported. Comparing them is the point:
the trust accrues 9-11 cents a quarter, so a new figure that has not moved that
much is the signal, not the noise.

Two things legitimately break the accrual and both need noting rather than
correcting. A working-capital withdrawal, visible in the filing as language
about withdrawing up to 10% of trust earnings for tax and regulatory purposes.
And taxes, which apply to the roughly 5% of names domiciled in Delaware or
Nevada rather than the Cayman Islands or BVI. Taxes come strictly off the
balance sheet.

## trust

The trust account itself. In a filing it reads as "cash and marketable
securities held in trust account", and as of the balance-sheet date it is held
either in US Treasury bills or in demand deposits.

The trust is the denominator of nearly everything the desk does: it sets the
redemption floor, it is what [[#CIT]] divides into shares, and it is the `trust`
term in the yield formula.

## yield model

The desk spreadsheet, `Yield Model v<N>.xlsx`, in the Drive folder
`1TMQVtyTWieGKDtiDWt5RXkEcwIqtvwZB`. It is the desk's own book of record for
per-name trust and yield figures, and the universe workbook is VLOOKUP'd
against it.

The version integer is the selector, not the filename order - `v9` sorts after
`v127` as a string, and the live series spans `v64` to `v127`. The pattern is
anchored to exactly `Yield Model v<N>.xlsx` so that a personal copy saved into
the same folder cannot silently drive the team's chart.

The yield itself is `(trust / price - 1) * 360 / days`. It is **360, not 365**.
The 360 is verified to zero error against 953 real leg-observations. 365 would
introduce about 7.5bp on every derived row while still looking plausible.

Detail: `meteora-mcp/docs/operations/extensionsSync.md`.

## extension

A SPAC's deadline extension - pushing out the date by which it must complete a
deal or liquidate. Each name is carried at three liquidation horizons: next
call, fully extended, and Meteora's own estimate. Plotting a name's yield at all
three as a connected trail is what makes the effect of an extension readable,
which is the `extensions` snapshot module and the dashboard's Extensions tab.

In this estate "extension" never means a Claude Desktop extension or a browser
extension. See [[#skill]] for the artifact-shaped thing.

## skill

**Two unrelated systems, both called skills, with two different sync paths.**

- **Meteora skills.** Drive-backed zips in the `GPT` Shared Drive under
  `Dev/Skills/`, one zip per skill plus a `backups/` folder. Served by
  `/skills-api/*` on the MCP server, browsed and uploaded at
  `/dashboard/skills`. Consumed entirely by hand: someone downloads a zip and
  drops it into Claude Desktop. Nothing loads one automatically.
- **The git skills.** `~/.claude/skills`, distributed through dotfiles. A
  different, more technical audience and a different consumption model.

They are deliberately not connected. `s1-filing-handler` and
`s1-filing-handler-old` sitting side by side is the version-history problem the
Drive-backed system exists to stop.

A skill is a folder - `SKILL.md` plus optional `references/`, `scripts/` and
`assets/` - which is why the Drive side stores each one as a single zip rather
than mirroring the tree.

Detail: `meteora-mcp/docs/operations/skillsApi.md`.

## memory doc

A Google Drive `.docx` in the firm knowledge base, projected into Pinecone so it
is semantically searchable, and optionally projected into S3 so the dashboard
can render it.

The Drive copy is the original. Everything else is a projection, which is why
`delete-memory-doc` has to remove the S3 object too - a deleted doc that keeps
its projection stays readable on the dashboard forever.

Drift has two causes the write path cannot see: a doc edited directly in the
Google Docs UI, and a publish interrupted by a restart. A background reconcile
loop covers both, reprojecting only docs whose Drive `modifiedTime` moved.

Detail: `meteora-mcp/docs/operations/memoryProjection.md`.

## arbjournal

The merger-arb deal corpus, and the `arbjournal-precedents` tool over it. Given
a set of regulatory regimes written as `<family>:<jurisdiction>` - `fdi:france`,
`antitrust:ec` - it returns duration statistics over comparable historical
deals. Families are `fdi`, `antitrust`, `sec` and `other`.

It defaults to closed deals, because only a closed deal has a realized
announce-to-close duration, which is the whole point of a precedent.

The namespace and index are fixed in code rather than exposed as parameters.
These statistics are meaningless against any other corpus, so making the corpus
selectable would only invite a query that silently returns nothing.

## RLST

The restricted list. An Excel workbook with `Sheet1` for active restrictions and
`Sheet2` for cleansed history, read and amended by the `rlst-read`,
`rlst-update`, `rlst-remove` and `rlst-check` tools.

It lives in one of two places and the switch is a single setting. With
`rlst_drive_file_id` empty it is the on-prem Windows mount at
`G:\Shared drives\Investments\RLST\RLST.xlsx`. With the id set it is that Drive
file, read and written over the Drive API.

**No MCP tool creates a restriction.** `rlst-add` is the only one that would,
and it is archived because its related-securities enrichment needs Bloomberg.
Rows are added by hand.

## the box

The single production EC2 instance every server-side thing runs on. Systemd
units, timers, Caddy routes and all four deployed repos share it.

## meteora-secrets

The SOPS-encrypted store that **is** the environment for every service. A
per-repo `.env` is a derived artifact, not a parallel system.
`meteora-secrets-render` materializes it onto the box, so anything edited
directly there survives only until the next render.

Its `manifest.yaml` lists the whole env file, not just the secret values, so a
key the manifest does not name is simply absent and the app falls back to that
setting's default.

## snapshot / ingest

How the dashboard receives data. A producer POSTs a snapshot to
`/dashboard/api/ingest`, keyed by module and `as_of`, and the write is
**whole-record** - the new snapshot replaces the old one for that key rather
than merging into it.

That is the constraint behind several otherwise-odd behaviours. It is why the
extensions sync publishes only when the workbook checksum moves, so it does not
keep reverting the desk's Bloomberg price patch. And it is why the `universe`
branch is gated on its own token, so a desk machine running a stale config
cannot replace the server-published universe with a six-week-old one.

## the deadlines feed

The `(ticker, deadline)` map published out of the universe sync and served back
at `/dashboard/api/universe/deadlines` for the desk's yield capture.

Pairs go out raw and unselected. A ticker legitimately carries several deadlines
- 82 of 1449 do, and `AAC` has three - and the consumer picks the earliest still
in the future relative to _its own_ today. Resolving that here would pin the
answer to the hour the sync ran.

## Related

- [[Raw Notes 2026-08]] - where the CIT, trust and yield-model vocabulary comes
  from, unprocessed
