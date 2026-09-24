# NEXT UP

**Reconciled:** 2026-09-24  
**Domain:** defensive network security diagnostics for authorized environments.

## Highest-priority executable lane

### Resolve optional Keras/TensorFlow handling without making deep learning mandatory by accident

**Why it exists**

Legacy branch `main` is now semantically reconciled and requires no promotion. The remaining current blocker is the documented GitHub Actions collection failure in `tests/test_deep_anomaly_detection.py` because `deep_anomaly_detection.py` imports Keras while the canonical test environment does not install it.

**Authority/source**

- `MASTER_TASK_LIST.md`
- `MASTER_TASK_LOG.md`
- `PRODUCTION_READINESS.md`
- `deep_anomaly_detection.py`
- `tests/test_deep_anomaly_detection.py`
- exact-head historical Actions evidence recorded in the task log

**Current state**

- canonical/default branch: `master`
- legacy `main` head: `8784d670e4824fb80fd48ab7b883c678e0c3e2ca`
- legacy branch disposition: `SUPERSEDED / CONTENT_CONTAINED`
- promotion required from `main`: none
- current branch retirement gate: replacement reconciliation must merge, then exact-SHA revalidation may retire `main`
- production readiness remains unclaimed

**Done evidence**

1. Decide whether Keras/TensorFlow is an optional extra or a required runtime dependency.
2. Make test collection deterministic for the chosen contract.
3. Run targeted deep-anomaly tests and the canonical full test command.
4. Update package/dependency and readiness docs to match the proven behavior.

**Do not work concurrently on**

- live/intrusive network activity;
- unrelated scanner features;
- broad packaging rewrites;
- destructive branch deletion before exact-SHA retirement revalidation.

## Following lanes

2. Remove or replace remaining generic placeholder tests in `tests/test_basic.py`.
3. Reconcile `main.py --analyze` with the 3-feature `AnomalyDetectionModel` contract.
4. Clarify or fix stale package metadata and console entry point.
5. Add an explicit default-offline/no-network test lane.

## Completed branch-reconciliation gate

The three unique `main` commits are fully classified in `docs/reconciliation/legacy-main-20260924.md`:

- governance bundle: superseded by newer canonical docs;
- virtualenv removal: already represented on master (files absent; ignore rule present);
- CI badge fix: already represented on master.

No donor commit requires promotion.
