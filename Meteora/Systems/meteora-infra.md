---
tags: [meteora, system]
sources:
  - meteora-infra/terraform
  - meteora-infra/ansible
  - meteora-infra/Makefile
  - meteora-infra/docs
verified: 2026-08-27
---
# meteora-infra

## What it is

The infrastructure as code for everything the other repos run on - Terraform
owns AWS, Ansible owns the box, and the two meet at exactly one seam.

## Diagram

This repo draws its own, and they are committed as Mermaid beside the code so
they diff in review. Read `meteora-infra/docs/architecture.md` - the layer
boundary, the AWS footprint, and how a request reaches an app - rather than a
copy here that would go stale independently.

## How it works

### One boundary, one direction

**Terraform never writes a file on the box. Ansible never calls an AWS API.**

The single seam runs one way: Terraform emits the instance address into a
generated Ansible inventory, and nothing flows back. That is ADR-0001, and it is
the decision the whole repo is arranged around.

Terraform owns EC2, the Elastic IP, the security group, IAM, S3, Cognito, SNS,
CloudWatch, the snapshot policy and the budget, in account `309128776621`,
region `us-east-2`. The VPC and subnets are deliberately **data sources rather
than managed resources**, so `terraform destroy` cannot reach them.

Ansible owns users and groups, the FHS layout, systemd units and timers,
sudoers, Caddy, Neo4j, the self-hosted runners and the ops scripts. Its roles
are `base`, `identity`, `layout`, `apps`, `caddy`, `neo4j`, `runners`, `ops` and
`secrets_render`.

### The "Neither" column

The part a reader assumes is covered and is not. Three things sit outside both
tools by design:

- **`meteora-secrets` SOPS values.** Ansible installs the renderer and never the
  values. That is ADR-0005.
- **`/etc/meteora/age.key`**, placed by hand. Without it the renderer cannot
  decrypt anything.
- **`/srv/<app>` contents**, owned by each application repo's own `deploy.yml`.

So a from-scratch rebuild of the box gets you a correct machine with no
application code and no secrets on it. That is the intended shape, not a gap.

### The correctness gate

There is no test suite. The gate is a **from-scratch staging box diffed against
prod** - build a second machine from the same playbook, collect facts from both,
and diff them through an allowlist of legitimate differences. ADR-0006. That is
what `stage-up`, `stage-build`, `stage-diff` and `stage-down` exist for.

## Why it's this way

Splitting by tool rather than by environment means neither tool needs to
understand the other's model. Terraform does not know what a systemd unit is,
Ansible does not know what an IAM role is, and the one-directional seam means
there is no reconciliation loop to get wrong.

Keeping the VPC as a data source is a small line of HCL that removes an entire
class of catastrophic mistake. The default VPC is shared with everything in the
account, and a `terraform destroy` that could reach it would be unrecoverable.

Excluding secrets from Ansible is what lets the playbook be run by anyone,
re-run freely, and read in a PR without any of it being sensitive.

## Traps

- **SSH is still open to `0.0.0.0/0`.** `ssh_allowed_cidrs` defaults to it in
  both prod and staging. The SSM Session Manager migration that would close it
  is planned and **not executed** - the plan is on disk in the workspace at
  `docs/superpowers/meteora-infra/plans/`. Ports 80 and 443 are open to the
  world too, but those are Caddy's front door and are meant to be.
- **`terraform apply` from CI is manual-trigger only, and that is the gate.**
  Required-reviewer protection on environments needs a paid GitHub plan, so the
  prod environment carries no protection rules. Someone pressing Run is the
  whole approval. Do not add a push trigger without a working approval rule - it
  would apply to production unattended on every merge.
- **The apply workflow refuses a plan containing a delete.** Adoption is
  complete, so a destroy from CI means something is wrong rather than intended.
- **The AWS provider cannot drive an MFA prompt.** The Makefile exports the
  profile's session into the environment first, which needs
  `aws sts get-caller-identity --profile luke-admin` run once per session to
  refresh it.
- **ADRs are immutable once accepted.** A changed mind is a new ADR that
  supersedes the old one. Editing an accepted ADR destroys the thing it exists
  for.

## Where to start reading

| # | File | Why this rung |
| --- | ---------------------------- | ----------------------------------------------------------------- |
| 1 | `docs/architecture.md` | Three Mermaid diagrams: the layer boundary, the AWS footprint, the request path. |
| 2 | `docs/adr/README.md` | Eight decisions with their status. Read 0001 and 0005 at minimum. |
| 3 | `Makefile` | Every supported operation, and the MFA wrapper around all of them. |
| 4 | `ansible/group_vars/all.yml` | `meteora_apps` - the per-app users, uids, and FHS paths the whole box is built from. |
| 5 | `ansible/roles/` | What is actually configured, role by role. |
| 6 | `terraform/envs/prod/` | The root that composes the modules, and the variables that gate ingress. |

> **Read 1-3 to defend it. Add 4-6 before you change it.**

## Making changes

### The gate

```bash
make fmt      # terraform fmt -recursive
make plan     # terraform plan against prod
make check    # ansible-playbook --check --diff, read-only, never applies
```

There is **no pytest and no unit suite**. `make plan` and `make check` are the
gate, and both are read-only.

For a real change, the honest gate is the staging cycle:

```bash
make stage-up      # terraform apply staging, write its inventory
make stage-build   # run the playbook against it
make stage-diff    # collect facts from both boxes, diff through the allowlist
make stage-down    # terraform destroy staging
```

`stage-diff` prints `IDENTICAL` when the only differences are allowlisted.

### Test structure

Facts, not assertions. `ansible/scripts/collect_facts.sh` snapshots a box and
`ansible/scripts/allowlist.txt` enumerates the differences that are legitimate
between prod and a fresh staging build. Anything outside that list is a finding.

### CI

Four workflows, no test job:

- **`terraform-plan.yml`** on PR. Shows the plan.
- **`terraform-apply.yml`** on manual dispatch only, requiring the literal
  string `apply` as confirmation, and refusing any plan containing a delete.
- **`drift.yml`** daily at 06:00 Eastern during EDT. Reports drift between the
  state and reality.
- **`snapshot-check.yml`** daily, three hours after the DLM policy fires so a
  slow snapshot has time. Fails on stale backups.

CI authenticates by OIDC into `meteora-infra-ci`, so there is no long-lived AWS
key anywhere.

### Deploy

Applying _is_ the deploy. `make apply` from a laptop, or the manual-dispatch
workflow. Ansible changes are applied by running the playbook without `--check`.

### Manual QA

`make plan` and `make check` are the manual QA - both read-only, both safe to
run any time, and both worth running before touching anything. For a change
whose blast radius is the box itself, build staging and diff it rather than
reasoning about the playbook.

### Traps

- The staging box costs money while it is up. `stage-down` is part of the cycle,
  not an optional cleanup.
- `make check` reports what _would_ change. A long diff after someone edited the
  box by hand is the expected way that gets discovered.

## Related

- [[meteora-mcp]], [[meteora-dashboard]], [[meteora-ingest]], [[meteora-scripts]] -
  the applications whose users, paths and units this repo creates, and whose
  code it deliberately does not deploy
- [[Glossary]] - the box, meteora-secrets
