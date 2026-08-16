# NEXT UP

**Reconciled:** 2026-08-16  
**Domain:** defensive network security diagnostics for authorized environments.

## Highest-priority executable lane

### Reconcile divergent legacy branch `main` against canonical `master`

**Why it exists**

The repository default and current product authority is `master`, but a separate `main` branch remains diverged. Historical task-log evidence says governance work and tracked-virtualenv cleanup occurred on `main` and governance commits were later cherry-picked to `master`; current Git ancestry still shows unique commits on `main`, so branch deletion or wholesale merge is not justified without semantic review.

**Authority/source**

- `AGENTS.md` salvage-before-delete contract
- `MASTER_TASK_LOG.md` 2026-07-01 branch history
- `MASTER_TASK_LIST.md`
- current Git branch/commit comparison
- current `master` implementation/tests

**Current state**

- `master` is canonical/default.
- Current `master` has the 2026-08-14 test-stability closure with `56 passed` recorded in repository evidence.
- `main` is 3 commits ahead and 14 commits behind current `master`.
- Its unique history includes governance/docs plus removal of a tracked virtualenv/tooling tree relative to the common ancestor.
- Existing history states the virtualenv was never tracked on `master`, so the branch cannot be treated as a required cleanup patch without further proof.
- Classify `main` as `DIVERGED_LEGACY / SALVAGE_CANDIDATE` pending semantic reconciliation.
- No open pull request owned `main` at this standardization audit.

**Blockers**

- Determine whether any of the three branch-only commits still contain value not already represented on `master`.

**Done evidence**

1. Each unique `main` commit/file change is classified `ALREADY_PROMOTED`, `HISTORICAL_REFERENCE`, `PROMOTE`, or `REJECT`.
2. Any retained value is ported onto a fresh branch based on current `master`; do not merge the divergent branch wholesale.
3. `main` is not deleted until all unique value is accounted for and canonical branch policy is explicit.
4. `MASTER_TASK_LIST.md`, `MASTER_TASK_LOG.md`, and `NEXT_UP.md` are reconciled after the decision.

**Do not work concurrently on**

- destructive branch cleanup;
- new scanner features;
- live/intrusive network activity;
- anomaly-model expansion;
- packaging rewrites unrelated to branch reconciliation.

## Following lanes

2. Remove or replace remaining generic placeholder tests in `tests/test_basic.py`.
3. Reconcile `main.py --analyze` with the 3-feature `AnomalyDetectionModel` contract.
4. Clarify Keras/TensorFlow handling for `deep_anomaly_detection.py`.
5. Clarify or fix stale package metadata and console entry point.
6. Add an explicit default-offline/no-network test lane.

## Verification reference

```bash
python3 -m pytest -q
```

Latest verified repository evidence before this planner-only lane: `56 passed` on 2026-08-14. No new CI/pass claim is created by this documentation-only reconciliation.
