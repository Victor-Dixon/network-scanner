# AGENTS.md — network-scanner

## Role

`network-scanner` is a defensive Python network security diagnostics toolkit
for authorized environments. Its implemented domain covers IPv4 ARP host
discovery, TCP port/banner helper functions, local vulnerability lookup,
AbuseIPDB reputation lookup, anomaly-detection experiments, and traffic
heuristic helpers.

It is not an exploitation framework, unauthorized scanner, production SIEM,
compliance platform, distributed scanner, or plugin runtime.

## Domain model

- Core domain: authorized network security diagnostics.
- Complete model: `docs/DOMAIN_MODEL.md`.
- Product scope: `PRD.md`.
- Roadmap and current status: `ROADMAP.md`, `MASTER_TASK_LIST.md`,
  `MASTER_TASK_LOG.md`, `NEXT_UP.md`, `PRODUCTION_READINESS.md`.

If architecture, intent, or behavior cannot be verified from code or docs, mark
it as **Unknown** instead of guessing.

## Key surfaces

- `main.py` — CLI entry point (`--scan-ip`, `--analyze`, `--vuln-check`) and
  ARP discovery orchestration.
- `utils.py` — socket helpers, hostname lookup, port scanning, banner grabbing,
  scan-result formatting, and encrypted-traffic heuristics.
- `vulnerability_assessment.py` — local SQLite vulnerability table, example
  data seed, and exact service/version lookup.
- `threat_intelligence.py` — AbuseIPDB IP reputation helper and NVD keyword
  helper; currently requires `ABUSE_IP_DB_API_KEY` at import time.
- `anomaly_detection.py` — Isolation Forest anomaly model wrapper with a
  3-feature training contract.
- `deep_anomaly_detection.py` — Keras autoencoder anomaly-detection functions.
- `docs/DECEPTION_DEFENSE_PRINCIPLES.md` — governance constraints for any
  future deception-related research.
- `tests/` — pytest/unittest suite; contains both characterization tests and
  generic placeholders.
- `.github/workflows/` — CI/test workflows.

## Current state

The repository is documentation-synchronized as of 2026-07-03 but remains **not
production-ready**. Full pytest collection may be blocked by:

- import-time `ABUSE_IP_DB_API_KEY` validation in `threat_intelligence.py`;
- missing or optional deep-learning dependencies for `deep_anomaly_detection.py`;
- unregistered pytest markers;
- placeholder tests in `tests/test_basic.py`;
- possible `main.py --analyze` mismatch between 5-feature sample data and the
  3-feature anomaly model contract.

## Completed

- Governance artifact baseline.
- Defensive deception principles.
- Implementation-derived domain model.
- README/PRD/roadmap/task/readiness docs synchronized to current code evidence.

## Next work

1. Refactor AbuseIPDB credential handling to avoid import-time failure.
2. Keep threat-intelligence tests mocked and offline.
3. Register pytest markers and remove placeholder tests.
4. Reconcile anomaly CLI sample data with the model contract.
5. Clarify Keras/TensorFlow and packaging metadata gaps.

## Rules

- Do not run intrusive scans without explicit target authorization.
- Keep tests offline and mocked by default.
- Do not require real API keys during test collection.
- Do not commit secrets, `.env` files, runtime databases, scan artifacts, or
  local virtualenvs.
- Separate ML anomaly detection, packet scanning, vulnerability lookup,
  defensive-governance docs, and threat-intelligence integrations.
- Treat outputs as defensive security diagnostics only.
- Do not invent architecture, product requirements, or implemented features.
