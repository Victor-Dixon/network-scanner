# NEXT UP

**Updated:** 2026-07-03  
**Domain:** defensive network security diagnostics for authorized environments.

## What this project is

`network-scanner` is a Python toolkit for authorized IPv4 host discovery,
port/banner helper functions, local vulnerability lookup, IP reputation checks,
and anomaly-detection experiments.

## Why it exists

It provides an inspectable defensive security diagnostics codebase for local
network/security-signal experimentation.

## Completed most recently

- Added a complete domain model in `docs/DOMAIN_MODEL.md`.
- Replaced placeholder README content with implementation-derived project
  documentation.
- Synchronized PRD, roadmap, master task list/log, production readiness,
  project structure, consolidation, and AGENTS docs.
- Recorded Unknowns instead of assuming missing architecture or requirements.

## Current focus

Stabilize existing behavior and tests before adding new features.

## Work next

1. Refactor `threat_intelligence.py` so missing `ABUSE_IP_DB_API_KEY` fails at
   `check_ip_abuseipdb` call time, not import time.
2. Update AbuseIPDB tests to be fully mocked and offline-safe.
3. Register pytest markers (`unit`, `integration`, `slow`) in pytest config.
4. Remove or replace generic placeholder tests in `tests/test_basic.py`.
5. Reconcile `main.py --analyze` with the 3-feature model contract in
   `AnomalyDetectionModel`.
6. Clarify Keras/TensorFlow dependency handling for `deep_anomaly_detection.py`.
7. Clarify or fix stale package metadata and console entry point.

## Verify

Expected verification command:

```bash
python3 -m pytest -q
```

Latest verification on 2026-07-03 after installing `requirements.txt` failed
during collection because:

- `threat_intelligence.py` validates `ABUSE_IP_DB_API_KEY` during import;
- `deep_anomaly_detection.py` imports Keras, which is not installed by
  `requirements.txt`;
- pytest markers `slow`, `unit`, and `integration` are not registered.
