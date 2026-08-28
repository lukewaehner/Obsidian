---
tags: [meteora, infra]
sources:
  - meteora-mcp/.github/workflows/deploy.yml
  - meteora-dashboard/.github/workflows/deploy.yml
  - meteora-ingest/.github/workflows/deploy.yml
  - meteora-scripts/.github/workflows/deploy.yml
  - meteora-infra/.github/workflows/terraform-apply.yml
verified: 2026-08-27
---
# Deploys

## What it is

Six repos ship six different ways. Nothing here is shared - no common script, no
common workflow - so the answer to "what happens when I merge" depends entirely
on which repo you are in, and guessing wrong costs a broken deploy.

This note is the comparison. Each repo's own note has its detail.

## The table

| Repo | Trigger | Gate on the box | Restart? | Rollback |
| ------------------- | ------------------- | ------------------------------ | ------------------------- | ---------------------------- |
| [[meteora-mcp]] | push to `main` | full pytest suite, in place | yes, then health-check | hard reset to previous commit |
| [[meteora-dashboard]] | push to `main`, path-filtered | lint + test + build in CI first | yes, then health-check | hard reset |
| [[meteora-ingest]] | push to `main` | smoke test in place | **no** - cron picks it up | hard reset |
| [[meteora-scripts]] | push to `main` | pytest + bats + ruff + shellcheck, in place | **no** - cron picks it up | hard reset |
| [[meteora-infra]] | **manual dispatch only** | `terraform plan`, refuse deletes | n/a | none - re-apply |
| [[meteora-core]] | **nothing** | n/a | n/a | n/a |

All four application deploys run on **self-hosted runners on the box itself**,
as that app's deploy user. See [[The Box]].

## The four shapes, and why they differ

### Restart-and-health-check: mcp and dashboard

These are long-running services, so a deploy has a moment where the new code is
loaded and might not work.

meteora-mcp fast-forwards the checkout, re-syncs dependencies, and **re-runs the
whole test suite in place against the exact tree systemd serves from** - not
against a CI checkout. Only then does it restart, then curls `/health` on
loopback for up to twenty seconds. Any failure hard-resets to the previous
commit and restarts that.

The property that makes this safe: **the live process keeps last-known-good code
in memory right up until the restart step.** A commit that fails the box-level
suite never reaches production at all.

The dashboard's gate runs in CI rather than on the box - lint, test, build, plus
Playwright when `web/**` changed - and the deploy job is path-filtered, so a
docs-only push no longer redeploys.

### No restart at all: ingest and scripts

Both are cron jobs, not daemons. There is no service to restart and no health
endpoint. The deploy installs and runs the suite, and **the next tick uses the
new code**.

That has two consequences worth internalizing:

- **Success means the suite passed, not that the job works.** Nothing about the
  actual work is confirmed until the next real tick, so watch the first run
  after a deploy.
- **A tick firing between the fast-forward and the end of the suite runs the
  new, not-yet-verified commit.** Inherent to deploying a cron job in place.

meteora-scripts additionally **waits for the harvest lock** before touching
anything, and fails without changing a thing if it cannot take it within 420
seconds. It would rather do nothing than reset the tree underneath a running
job. Re-run the workflow once the harvest finishes.

### Manual only: infra

`terraform apply` runs on **workflow dispatch only**, requiring the literal
string `apply` as confirmation, and it plans first and **refuses any plan
containing a delete**.

There is no push trigger, and the comment in the workflow says not to add one:
required-reviewer protection on environments needs a paid GitHub plan, so the
prod environment carries no protection rules and gates nothing. **Someone
pressing Run is the entire approval.** A push trigger would apply to production
unattended on every merge.

### Nothing at all: core

[[meteora-core]] is a library. Merging to `main` reaches nobody. Shipping is
cutting a git tag and then bumping the pin in a consumer's `pyproject.toml`, in
that consumer's repo, through that consumer's PR and deploy.

So a meteora-core change reaches production through **two** of the deploys
above, at whatever times those two consumers each choose to adopt it.

## Why it's this way

Running the suite on the box rather than trusting CI's green tick is the common
thread across all four application deploys, and it is not redundancy. CI tests a
clean checkout on a GitHub runner; the box has the real Python, the real
lockfile resolution, and the real environment file. The failures this catches
are environmental, and they are exactly the ones that would otherwise be
discovered by users.

Rolling back the working tree rather than the service is what makes a failed
deploy cheap. The previous commit is always one `git reset --hard` away, and for
the two daemons the old process is still running while that happens.

## Traps

- **`main` deploys to production in five of six repos, and nothing mechanically
  stops a direct push.** The org is on GitHub's free plan, so branch protection
  is unavailable on private repos. The rule is convention held by the committer.
- **A green CI does not mean a green deploy**, and for meteora-mcp a green local
  gate does not mean green CI either - CI adds a blocking secret scan the local
  gate cannot reproduce.
- **Rollback cannot save you from a bad environment file.** The env file is not
  in any repo, so restoring the previous commit restarts old code against the
  same bad config. A blank JSON-typed variable takes meteora-mcp down and keeps
  it down. See [[Secrets]].
- **For the two cron repos, "deploy succeeded" is a weaker claim than it
  sounds.** Watch the next tick.
- **A meteora-scripts deploy that reports a lock timeout changed nothing.**
  Re-run it.
- **`meteora-tape` and `court-listener-mcp` have no deploy at all**, and
  meteora-tape has no CI either.

## Where to start reading

| # | File | Why this rung |
| --- | ------------------------------------------- | ---------------------------------------------- |
| 1 | `meteora-mcp/.github/workflows/deploy.yml` | The fullest shape: in-place suite, restart, health-check, rollback. |
| 2 | `meteora-scripts/.github/workflows/deploy.yml` | The cron shape, plus the lock wait. |
| 3 | `meteora-infra/.github/workflows/terraform-apply.yml` | Manual dispatch and the refuse-deletes step, with the reasoning inline. |
| 4 | `meteora-dashboard/.github/workflows/deploy.yml` | The path filter and the CI-side gate. |
| 5 | each repo's `CONTRIBUTING.md` or `CLAUDE.md` | The branch and PR conventions that sit in front of all of this. |

> **Read 1-3 to defend it. Add 4-5 before you change it.**

## Related

- [[The Box]] - the runners and deploy users all of this runs as
- [[Secrets]] - the one thing a rollback cannot restore
- [[meteora-infra]] - the only repo that deploys infrastructure rather than code
- [[Meteora]]
