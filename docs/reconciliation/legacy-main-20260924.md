# Legacy `main` reconciliation — 2026-09-24

Canonical branch: `master`  
Canonical base at lane start: `e2bcaee4f07db7bd1d0e1c348031d837a2186e80`  
Legacy branch: `main`  
Legacy head: `8784d670e4824fb80fd48ab7b883c678e0c3e2ca`  
Ancestry at review: 3 commits ahead / 17 behind current `master`

## Decision

Do not merge `main` wholesale.

All three unique legacy commits are already represented or superseded on current `master`. No file or behavior requires promotion.

Overall classification: `SUPERSEDED / CONTENT_CONTAINED`.

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

## Retirement gate

After this reconciliation lands on canonical `master`:

1. verify no open PR owns `main`;
2. re-read `main` and require exact head `8784d670e4824fb80fd48ab7b883c678e0c3e2ca`;
3. verify `master` remains the repository default;
4. retire `main` only if all gates remain true;
5. verify remote ref absence.

No branch deletion is performed by this reconciliation PR.
