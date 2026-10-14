# NEXT UP

**Reconciled:** 2026-10-14  
**Domain:** defensive network security diagnostics for authorized environments.

## Current priority (2026-10-14)

### Independently review PR #6; then reconcile PR #5

- PR #6 `fix/optional-keras-test-collection-20261014` makes the optional Keras test suite and optional `psutil` placeholder test skip when their undeclared dependencies are absent. Exact-head `bc9f56f8a8d2a1b897137e89e733639736dac802`: `CI/CD Pipeline` run `38555344583` succeeded and `Tests` run `38555344636` succeeded. **PR #6 remains unmerged and requires independent review.**
- Once approved and merged, rebase/update the legacy-`main` reconciliation PR #5 and require fresh exact-head CI and review before merging. PR #5 must preserve reserved branch `main`; it does not authorize that ref's deletion.
- Keras/TensorFlow runtime packaging decisions, placeholder-test replacement, and production readiness remain open. Do not interpret the dependency-absent test skips as testing the optional deep-learning functionality.

## Historical reconciliation snapshot (2026-08-16)

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
- Current `master` has the 2026-08-14 local test-stability closure with `56 passed` recorded in repository evidence.
- `main` is 3 commits ahead and 14 commits behind current `master`.
- Its unique history includes governance/docs plus removal of a tracked virtualenv/tooling tree relative to the common ancestor.
- Existing history states the virtualenv was never tracked on `master`, so the branch cannot be treated as a required cleanup patch without further proof.
- Classify `main` as `DIVERGED_LEGACY / SALVAGE_CANDIDATE` pending semantic reconciliation.
- No open pull request owned `main` at the start of this standardization audit.

## Historical exact-head acceptance state for the 2026-08-16 planner lane

At PR head `930305f691e9001350fc99b529f67cc197ddf4ab`:

- `CI/CD Pipeline` run `31932994990`: `completed / success`.
- `Tests` run `31932994992`: `completed / failure`.
- Failing collection path: `tests/test_deep_anomaly_detection.py` -> `deep_anomaly_detection.py` -> `from keras.models import ...`.
- Concrete blocker: `ModuleNotFoundError: No module named 'keras'`.

This was the **historical** red result at head `930305f`; it was subsequently addressed for dependency-absent test collection by PR #6. At that earlier head, `CI_VERIFIED=false`; the prior local `56 passed` evidence is historical local proof, not current GitHub Actions proof.

**Blockers**

- Determine whether any of the three branch-only commits still contain value not already represented on `master`.
- Historical 2026-08-16 GitHub Actions Tests baseline was red on missing Keras. That collection issue is addressed by PR #6; green results were verified at `bc9f56f8` before documentation updates. The latest PR #6 head remains subject to its own exact-head CI and independent review; this historical error is no longer a current execution blocker.

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

2. Clarify optional deep-learning runtime packaging and coverage without making Keras/TensorFlow mandatory in the base install; the test collection fix is in PR #6, subject to review and merge.
3. Remove or replace remaining generic placeholder tests in `tests/test_basic.py`.
4. Reconcile `main.py --analyze` with the 3-feature `AnomalyDetectionModel` contract.
5. Clarify or fix stale package metadata and console entry point.
6. Add an explicit default-offline/no-network test lane.

## Verification reference

```bash
python3 -m pytest -q
```

Historical local evidence: `56 passed` on 2026-08-14. Historical August exact-head Actions Tests were red as documented above. The latest **PR #6** exact-head Actions workflow runs cited in Current priority above are green; PR #6 is not yet merged.
