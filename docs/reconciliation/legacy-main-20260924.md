# Legacy `main` reconciliation — 2026-09-24

Canonical branch: `master`  
Canonical base at lane start: `e2bcaee4f07db7bd1d0e1c348031d837a2186e80`  
Legacy branch: `main`  
Legacy head: `8784d670e4824fb80fd48ab7b883c678e0c3e2ca`  
Ancestry at review: 3 commits ahead / 17 behind current `master`

## Decision

Do not merge `main` wholesale.

All three unique legacy commits are already represented or superseded on current `master`. No file or behavior requires promotion.

Content classification: `SUPERSEDED / CONTENT_CONTAINED`.

Ref disposition: `PRESERVE / RESERVED_NAME`. Current fleet retirement policy reserves exact branch name `main`; content containment does not grant deletion authority.

## Commit-level classification

### `f095a4c57f029a031b8da23bfc9a8e97b650efff`
`docs: add client-show governance artifact bundle (9/9 contract)`

Classification: `ALREADY_PROMOTED / SUPERSEDED`.

Reason:

- current `master` has newer and more complete `AGENTS.md`, `MASTER_TASK_LIST.md`, `MASTER_TASK_LOG.md`, `NEXT_UP.md`, `PRODUCTION_READINESS.md`, `PROJECT_STRUCTURE_TREE.md`, and `ROADMAP.md`;
- current documents explicitly model the defensive-network-diagnostics domain, current test gaps, branch policy, and non-production-ready status;
- copying the July snapshots would regress planner/readiness authority.

### `9e88c4e20f35fe6c4f5f431fa0b9bbd2b333fa9a`
`chore: untrack local venv from public repo tree`

Classification: `ALREADY_PROMOTED / NO_CURRENT_DELTA`.

Evidence on current `master`:

- `network-scanner/pyvenv.cfg` is absent;
- `network-scanner/Scripts/Activate.ps1` is absent;
- `network-scanner/Scripts/network-scanner-script.py` is absent;
- `.gitignore` explicitly excludes `network-scanner/`.

Therefore there is no remaining virtualenv cleanup patch to promote.

### `8784d670e4824fb80fd48ab7b883c678e0c3e2ca`
`docs: fix CI badge URL to Victor-Dixon/network-scanner`

Classification: `ALREADY_PROMOTED`.

Current `master` README already uses:

`https://github.com/Victor-Dixon/network-scanner/actions/workflows/ci.yml/badge.svg`

The donor's July task-priority edits are historical and must not replace the current canonical queue.

## Promotion result

- `PROMOTE`: none
- `ALREADY_PROMOTED / SUPERSEDED`: all three unique commits
- `REJECT`: stale July planner/readiness snapshots as current authority

## Ref disposition

After this reconciliation lands on canonical `master`:

1. keep canonical product authority on `master`;
2. retain legacy `main` as `PRESERVE / RESERVED_NAME`;
3. do not merge `main` wholesale;
4. do not delete or repoint `main` without an explicit fleet-policy change that removes the reserved-name hold.

No branch deletion is authorized by this reconciliation PR.
