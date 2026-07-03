# Master Task List

**Updated:** 2026-07-03  
**Domain:** defensive network security diagnostics for authorized environments.

## What this project is

`network-scanner` is a Python toolkit for authorized IPv4 host discovery,
port/banner helper functions, local vulnerability lookup, IP reputation checks,
and anomaly-detection experiments. See [`docs/DOMAIN_MODEL.md`](docs/DOMAIN_MODEL.md).

## Why it exists

It provides a small defensive security diagnostics codebase that contributors
can audit, test, and harden without assuming unimplemented architecture.

## P0 — Documentation and domain clarity

- [x] Add governance artifact bundle (2026-07-01).
- [x] Capture pytest blockers.
- [x] Add complete implementation-derived domain model (2026-07-03).
- [x] Replace placeholder README content with code-derived project description
      and usage (2026-07-03).
- [x] Synchronize PRD, roadmap, task list, task log, next-up, readiness, project
      structure, and agent docs (2026-07-03).
- [ ] Keep domain model updated whenever behavior changes.

## P0 — Test stability and offline safety

- [ ] Fix import-time `ABUSE_IP_DB_API_KEY` failure in `threat_intelligence.py`.
- [ ] Mock AbuseIPDB tests so pytest collection never requires real API keys.
- [ ] Register pytest markers: `unit`, `integration`, `slow`.
- [ ] Remove or replace generic placeholder tests in `tests/test_basic.py`.
- [ ] Add a no-network/default-offline test lane.
- [ ] Re-run pytest and update blocker docs after fixes.

## P0 — Current behavior consistency

- [ ] Reconcile `main.py --analyze` 5-feature sample data with the
      `AnomalyDetectionModel` 3-feature contract.
- [ ] Decide whether `main.py` should expose port scanning/banner grabbing or
      document them as helper-only APIs.
- [ ] Clarify or fix the duplicate/separate vulnerability helpers:
      local SQLite lookup in `vulnerability_assessment.py` and NVD keyword
      lookup in `threat_intelligence.py`.

## P1 — Packaging and dependency clarity

- [ ] Clarify package layout; no `network_scanner/` package currently exists.
- [ ] Fix or remove stale `setup.py` console entry point
      (`network_scanner.__main__:main`).
- [ ] Align package metadata dependencies with imported modules, especially
      `scikit-learn`, `python-dotenv`, and Keras/TensorFlow requirements.
- [ ] Decide whether `requirements.txt` should include deep-learning runtime
      dependencies or whether deep anomaly detection should be optional.

## P1 — Product hardening

- [ ] Replace static example vulnerability seed data with a documented,
      offline-safe update path or fixtures.
- [ ] Add explicit authorization/safety guidance to CLI documentation or
      command prompts.
- [ ] Add tests around `scan_port`, `scan_ports`, `banner_grab`, and invalid
      scan inputs with mocked sockets/scapy.

## Later — Future ideas from `plans.txt`

These are not implemented and should remain future scope unless accepted into a
new PRD revision:

- [ ] IPv6 discovery support.
- [ ] Advanced OS fingerprinting.
- [ ] Additional threat-intelligence feeds.
- [ ] Automated CVE/NVD ingestion into the local vulnerability database.
- [ ] Compliance report templates.
- [ ] Custom scanning profiles.
- [ ] Distributed scanning and management console.
- [ ] UEBA-style behavioral baselines.
- [ ] Plugin architecture.
- [ ] Blockchain-backed scan-result integrity.

## Unknowns to resolve

- [ ] Decide which `plans.txt` items are actual requirements.
- [ ] Define the expected anomaly-detection feature schema.
- [ ] Define production deployment and packaging expectations.
- [ ] Define scan authorization/approval workflow, if any.
- [ ] Decide whether deception concepts remain governance-only.
