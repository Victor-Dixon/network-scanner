# AGENTS.md — network-scanner

## Project

Python network discovery and security scanning toolkit (ARP discovery, port scan, vulnerability checks, threat intel).

## Key surfaces

- `main.py` — CLI entry
- `anomaly_detection.py`, `deep_anomaly_detection.py` — ML anomaly modules
- `threat_intelligence.py`, `vulnerability_assessment.py` — security analysis
- `tests/` — pytest suite (CI via `.github/workflows/ci.yml`)

## Status SSOT

- `PRODUCTION_READINESS.md` — hire/client review checklist
- `MASTER_TASK_LOG.md` — dated execution log
- `NEXT_UP.md` — current focus (mirrors log)

## Guardrails

- Educational/ethical use only; scan only authorized networks.
- Do not commit secrets or local venv artifacts.
- Update docs when shipping user-visible changes.
