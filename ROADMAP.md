# Roadmap

**Updated:** 2026-08-14  
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
- Default pytest now passes offline with mocked AbuseIPDB behavior.
- Pytest markers are registered in `pytest.ini`.

## Current focus

Stabilize current behavior and documentation before adding new features:

1. Keep docs synchronized with implementation and mark Unknowns explicitly.
2. Treat the repository as not production-ready until packaging/dependency
   boundaries and CLI paths are reconciled.
3. Preserve separation between packet scanning, ML anomaly detection,
   vulnerability lookup, and threat-intelligence integrations.

## Next

1. Remove or replace remaining generic placeholder tests in `tests/test_basic.py`.
2. Reconcile `main.py --analyze` sample data with
   `AnomalyDetectionModel`'s 3-feature contract.
3. Document or add the missing Keras/TensorFlow dependency path for
   `deep_anomaly_detection.py`.
4. Clarify package layout and the currently stale `setup.py` console entry
   point.
5. Add an explicit no-network/default-offline test lane.

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
