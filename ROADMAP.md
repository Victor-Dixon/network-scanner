# Roadmap

**Updated:** 2026-07-03  
**Domain:** defensive network security diagnostics for authorized environments.

## What this project is

`network-scanner` is a Python toolkit for authorized IPv4 host discovery,
port/banner helper functions, local vulnerability lookup, IP reputation checks,
and anomaly-detection experiments. The complete domain model is in
[`docs/DOMAIN_MODEL.md`](docs/DOMAIN_MODEL.md).

## Why it exists

The project exists to provide a small, inspectable defensive security codebase
for learning, testing, and improving local network diagnostics and related
security-signal analysis.

## Completed

- Governance artifact baseline and defensive-use rules.
- Domain model and documentation audit.
- README/PRD/status docs synchronized to current code evidence.
- IPv4 ARP discovery CLI path.
- Local SQLite vulnerability lookup CLI path with example data.
- Direct helpers for TCP port checks, banner grabbing, hostname lookup,
  encrypted-traffic heuristics, AbuseIPDB lookup, NVD keyword lookup, and two
  anomaly-detection approaches.
- Characterization tests exist for core modules.

## Current focus

Stabilize current behavior and documentation before adding new features:

1. Keep docs synchronized with implementation and mark Unknowns explicitly.
2. Treat the repository as not production-ready until tests collect offline and
   CLI paths are reconciled.
3. Preserve separation between packet scanning, ML anomaly detection,
   vulnerability lookup, and threat-intelligence integrations.

## Next

1. Refactor `threat_intelligence.py` so missing `ABUSE_IP_DB_API_KEY` fails at
   AbuseIPDB call time, not import time.
2. Update AbuseIPDB tests so they are fully mocked and do not require real
   credentials.
3. Register pytest markers (`unit`, `integration`, `slow`) in a pytest
   configuration file.
4. Remove or replace generic placeholder tests in `tests/test_basic.py`.
5. Reconcile `main.py --analyze` sample data with
   `AnomalyDetectionModel`'s 3-feature contract.
6. Document or add the missing Keras/TensorFlow dependency path for
   `deep_anomaly_detection.py`.
7. Clarify package layout and the currently stale `setup.py` console entry
   point.

## Later

These items appear in `plans.txt` or prior docs but are not implemented in the
current codebase:

- IPv6 discovery support.
- Advanced OS fingerprinting.
- Expanded threat-intelligence feeds beyond AbuseIPDB.
- Automated CVE/NVD ingestion into the local vulnerability database.
- Scan profiles.
- Compliance-oriented report templates.
- Distributed scanning and central management console.
- UEBA-style behavioral baselines.
- Plugin architecture.
- Blockchain-backed scan-result integrity.

## Unknowns to resolve before expanding scope

- Which `plans.txt` items are committed product requirements versus ideas.
- Real network-feature schema for anomaly detection.
- Production deployment and packaging expectations.
- Authorization/approval workflow for scan targets.
- Whether defensive deception concepts should remain governance-only or become
  runtime features.
