# AGENTS.md

## Role

network-scanner is a network security scanner and anomaly-detection prototype.

## Current State

Security tooling repo with tests, but full pytest collection is blocked by missing dependencies and import-time credential requirements.

## Rules

- Do not run intrusive scans without explicit target authorization.
- Keep tests offline and mocked by default.
- Do not require real API keys during test collection.
- Separate ML anomaly detection, packet scanning, and threat-intelligence integrations.
- Treat outputs as defensive security diagnostics only.
