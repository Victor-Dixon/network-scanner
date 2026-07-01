# AGENTS.md — network-scanner

## Role

network-scanner is a network security scanner and anomaly-detection toolkit (ARP discovery, port scan, vulnerability checks, threat intel).

## Key surfaces

- `main.py` — CLI entry
- `anomaly_detection.py`, `deep_anomaly_detection.py` — ML anomaly modules
- `threat_intelligence.py`, `vulnerability_assessment.py` — security analysis
- `tests/` — pytest suite (CI via `.github/workflows/ci.yml`)

## Current state

Security tooling repo with tests; full pytest collection may be blocked by missing dependencies and import-time credential requirements.

## Status SSOT

- `PRODUCTION_READINESS.md` — honest hire/client review checklist
- `MASTER_TASK_LOG.md` — dated execution log
- `NEXT_UP.md` — current focus (mirrors log)

## Rules

- Do not run intrusive scans without explicit target authorization.
- Keep tests offline and mocked by default.
- Do not require real API keys during test collection.
- Do not commit secrets or local venv artifacts.
- Separate ML anomaly detection, packet scanning, and threat-intelligence integrations.
- Treat outputs as defensive security diagnostics only.
