# NEXT UP

**Updated:** 2026-08-14  
**Domain:** defensive network security diagnostics for authorized environments.

## What this project is

`network-scanner` is a Python toolkit for authorized IPv4 host discovery,
port/banner helper functions, local vulnerability lookup, IP reputation checks,
and anomaly-detection experiments.

## Why it exists

It provides an inspectable defensive security diagnostics codebase for local
network/security-signal experimentation.

## Completed most recently

- Removed the AbuseIPDB import-time API-key failure and kept missing credentials
  as a call-time `None` result.
- Updated AbuseIPDB tests to use mocked credentials and mocked HTTP calls.
- Lazily imported `scapy` only when ARP scanning is invoked.
- Registered pytest markers in `pytest.ini`.
- Verified `python3 -m pytest -q`: `56 passed`.
- Added a complete domain model in `docs/DOMAIN_MODEL.md`.
- Replaced placeholder README content with implementation-derived project
  documentation.
- Synchronized PRD, roadmap, master task list/log, production readiness,
  project structure, consolidation, and AGENTS docs.
- Recorded Unknowns instead of assuming missing architecture or requirements.

## Current focus

Stabilize existing behavior and tests before adding new features.

## Work next

1. Remove or replace remaining generic placeholder tests in `tests/test_basic.py`.
2. Reconcile `main.py --analyze` with the 3-feature model contract in
   `AnomalyDetectionModel`.
3. Clarify Keras/TensorFlow dependency handling for `deep_anomaly_detection.py`.
4. Clarify or fix stale package metadata and console entry point.
5. Add an explicit no-network/default-offline test lane.

## Verify

Expected verification command:

```bash
python3 -m pytest -q
```

Latest verification on 2026-08-14 passed:

- `python3 -m pytest -q`: `56 passed`
- `git diff --check`: PASS
