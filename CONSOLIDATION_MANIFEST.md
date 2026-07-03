# Consolidation Manifest

**Updated:** 2026-07-03

## Repo role

`network-scanner` is a defensive network security diagnostics and
anomaly-detection toolkit for authorized environments.

## Domain modeled

- Core domain: authorized network security diagnostics.
- Subdomains: IPv4 host discovery, port/service inspection, vulnerability
  assessment, threat intelligence, anomaly detection, traffic heuristics, CLI
  orchestration, and defensive governance.
- Complete model: `docs/DOMAIN_MODEL.md`.

## Current classification

DEFENSIVE-SECURITY / DOCUMENTATION-SYNCHRONIZED / TEST-BLOCKED /
NOT-PRODUCTION-READY

## Completed

- Governance artifact baseline.
- Defensive deception principles.
- Documentation-first domain model audit.
- README/PRD/roadmap/task/readiness docs synchronized to implementation
  evidence.

## Promotion candidates

- `utils.py` TCP port, banner, hostname, formatting, and traffic heuristic
  helpers.
- `vulnerability_assessment.py` local SQLite vulnerability lookup.
- `threat_intelligence.py` AbuseIPDB/NVD helper functions after credential and
  test isolation fixes.
- `anomaly_detection.py` Isolation Forest wrapper after CLI/model contract is
  reconciled.
- `deep_anomaly_detection.py` autoencoder functions after dependency handling is
  clarified.

## Blockers

- AbuseIPDB key required at import time.
- Full pytest is not reliably offline/mocked.
- Keras/TensorFlow dependency handling is missing for deep anomaly detection.
- Pytest markers are unregistered.
- Generic placeholder tests remain in `tests/test_basic.py`.
- `main.py --analyze` appears inconsistent with the 3-feature anomaly model
  contract.
- `setup.py` package/entry-point metadata is stale for the current flat module
  layout.

## What remains

1. Stabilize tests and dependency handling.
2. Reconcile implemented CLI behavior with module contracts.
3. Clarify packaging.
4. Decide which `plans.txt` future ideas are accepted product scope.

## Rule

No intrusive scanning, unauthorized targets, offensive automation, or live API
calls in default tests.
