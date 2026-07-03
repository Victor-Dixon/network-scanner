# Product Requirements Document (PRD)

**Updated:** 2026-07-03  
**Domain model:** [`docs/DOMAIN_MODEL.md`](docs/DOMAIN_MODEL.md)

## Overview

The **Network Scanner** is a defensive Python network-security diagnostics
toolkit for authorized environments. It currently implements IPv4 ARP host
discovery, TCP port/banner helper functions, local SQLite vulnerability lookup,
AbuseIPDB IP reputation lookup, Isolation Forest anomaly detection, Keras
autoencoder anomaly-detection functions, and lightweight encrypted-traffic
heuristics.

This PRD describes the implementation-derived product scope. Future ideas from
`plans.txt` are listed separately and must not be treated as implemented
features.

## Why this project exists

The project exists to provide an inspectable Python toolkit for defensive
security experimentation around local network discovery, service inspection,
known-vulnerability lookup, threat-intelligence enrichment, and anomaly
detection.

## Domain

- **Core domain:** authorized network security diagnostics.
- **Subdomains:** network discovery, port/service inspection, vulnerability
  assessment, threat intelligence, anomaly detection, traffic heuristics, CLI
  orchestration, and defensive governance.
- **User:** a contributor or operator working in an owned lab, local network, or
  other explicitly authorized environment.

Unknown from current evidence:

- Intended production deployment model.
- Formal operator authorization workflow.
- Real anomaly-detection feature schema.
- Whether all `plans.txt` items are committed requirements.

## Goals

- Provide a clear CLI for implemented host discovery, sample anomaly detection,
  and local vulnerability lookup.
- Keep network/security behavior defensive and authorization-bound.
- Maintain separate modules for scanning, vulnerability lookup, threat
  intelligence, anomaly detection, and utility helpers.
- Keep tests offline and mocked by default.
- Keep documentation synchronized with code and mark unknowns explicitly.

## Non-goals

- Unauthorized scanning, exploitation, persistence, payload deployment, or
  offensive automation.
- Replacing enterprise vulnerability scanners or SIEM platforms.
- Claiming plugin architecture, compliance reporting, distributed scanning,
  scan profiles, web UI, REST API, or production readiness before code exists.

## Current functional requirements

### 1. Network discovery

- Validate a user-provided IPv4 range or address with `ipaddress`.
- Use ARP to discover active hosts.
- Return and print discovered IP addresses.
- Require explicit authorization for target networks.

Evidence: `main.scan_network`, `main --scan-ip`.

### 2. Port and service inspection

- Provide TCP connect scanning helpers for individual ports and port ranges.
- Provide hostname resolution and HTTP-like banner-grabbing helpers.
- Provide formatted console output for scan-result tuples.

Evidence: `utils.py`, `main.scan_ports_on_device`.

Current limitation: port scanning and banner grabbing are helper functions; no
dedicated CLI flag wires them into `main.py`.

### 3. Vulnerability assessment

- Create a local SQLite `vulnerabilities` table at runtime.
- Seed example vulnerability data.
- Query vulnerabilities by exact service name and service version.
- Print matching CVE IDs and descriptions from `--vuln-check name:version`.

Evidence: `vulnerability_assessment.py`, `main --vuln-check`.

Current limitation: automated CVE/NVD ingestion into the local database is not
implemented; the current seed data is static example data.

### 4. Threat-intelligence lookup

- Provide an AbuseIPDB helper for IP reputation checks.
- Load `ABUSE_IP_DB_API_KEY` from the environment.
- Return AbuseIPDB response `data` or `None` on request/format errors.

Evidence: `threat_intelligence.check_ip_abuseipdb`.

Current limitation: the module raises at import time if the API key is missing,
which blocks offline test collection and any import path that does not need a
live AbuseIPDB call.

### 5. NVD keyword lookup helper

- Provide a function that queries NVD CVE data by keyword and returns CVE IDs
  and descriptions.

Evidence: `threat_intelligence.assess_vulnerabilities`.

Current limitation: this helper is not wired into the CLI and is separate from
the local SQLite vulnerability assessment module.

### 6. Anomaly detection

- Provide an Isolation Forest wrapper that trains on 2D NumPy arrays and
  returns anomaly row indices.
- Provide Keras autoencoder functions for CSV preprocessing, model creation,
  training, and reconstruction-error anomaly detection.

Evidence: `anomaly_detection.py`, `deep_anomaly_detection.py`.

Current limitations:

- `AnomalyDetectionModel.train` enforces 3 features, while the CLI sample
  generates 5-feature arrays.
- Keras/TensorFlow runtime dependency handling is incomplete.
- The expected real network-feature schema is Unknown.

### 7. Traffic heuristics

- Provide byte-pattern helpers for selected encrypted traffic signals such as
  TLS handshake, potential DoH, OpenVPN-like bytes, and SSH-like bytes.

Evidence: `utils.analyze_encrypted_traffic`, `utils.detect_tls_handshake`.

Current limitation: no packet capture workflow feeds these helpers.

### 8. Defensive governance

- Document that future deception concepts must remain defensive, isolated,
  authorized, observable, and non-offensive.

Evidence: `docs/DECEPTION_DEFENSE_PRINCIPLES.md`.

Current limitation: deception concepts are documentation/governance only; no
runtime deception subsystem is implemented.

## Major entities and relationships

See [`docs/DOMAIN_MODEL.md`](docs/DOMAIN_MODEL.md) for the complete entity,
relationship, data-flow, user-interaction, external-integration, and
feature-to-domain mapping.

Summary:

- Authorized target scope contains network ranges or hosts.
- Network ranges produce discovered device IPs through ARP discovery.
- Device IPs can be used by direct port, hostname, and banner helpers.
- Service/version pairs map to local vulnerability records.
- IP addresses can map to AbuseIPDB reputation reports.
- Numeric feature matrices map to anomaly index outputs.
- Raw packet bytes map to heuristic traffic classifications.

## Documentation requirements

Every public status document must answer:

- What is this project?
- Why does it exist?
- What domain does it model?
- What problems does it solve?
- What has been completed?
- What remains?
- What should be worked on next?

Required synchronized documents:

- `README.md`
- `docs/DOMAIN_MODEL.md`
- `PRD.md`
- `ROADMAP.md`
- `MASTER_TASK_LIST.md`
- `MASTER_TASK_LOG.md`
- `NEXT_UP.md`
- `PRODUCTION_READINESS.md`
- `PROJECT_STRUCTURE_TREE.md`
- `AGENTS.md`

## Roadmap

The authoritative roadmap is [`ROADMAP.md`](ROADMAP.md). Immediate work should
stabilize the currently implemented product before new feature expansion:

1. Remove import-time credential failure from `threat_intelligence.py`.
2. Keep threat-intelligence tests mocked/offline.
3. Register pytest markers and remove generic placeholder tests.
4. Reconcile anomaly CLI sample data with the model feature contract.
5. Clarify Keras/TensorFlow dependency handling.
6. Clarify or fix packaging metadata and console entry point.

Future ideas from `plans.txt` include IPv6 support, OS fingerprinting,
additional threat feeds, automated vulnerability ingestion, compliance
reporting, scanning profiles, distributed scanning, blockchain-backed integrity,
UEBA, and plugin architecture. These remain future or Unknown until implemented.

## Success metrics

Current success metrics should measure implemented behavior only:

- **Documentation clarity:** new contributors can identify the domain, entities,
  feature mappings, Unknowns, and current blockers from repo docs.
- **Safety:** tests and examples avoid unauthorized scans and live API calls by
  default.
- **CLI reliability:** implemented CLI paths run with documented inputs and
  failure modes.
- **Test stability:** pytest collection does not require real API keys or
  unavailable optional dependencies.
- **Module separation:** scanning, vulnerability assessment, threat
  intelligence, anomaly detection, and governance remain decoupled.

## Completed

- Governance artifact baseline.
- Defensive deception principles.
- README and domain-model documentation audit.
- Status documents for roadmap, master task list/log, next-up, and production
  readiness.
- Tests exist for core modules, though not all are stable or product-specific.

## Remaining work

- Fix import-time AbuseIPDB key failure.
- Mock or isolate live external calls in tests.
- Register pytest markers.
- Remove or replace placeholder tests.
- Resolve anomaly CLI/model feature mismatch.
- Resolve deep-anomaly dependency packaging.
- Clarify package layout and console entry point.
- Decide whether future `plans.txt` items are product commitments.

## Appendix

- Python version metadata: Python 3.8+.
- Dependencies: `requirements.txt`; note known gaps above.
- License: MIT.

---

## Defensive deception research

Future defensive research MAY include honeypot telemetry, deception
environments, padded-cell detection concepts, simulated service layers, and
anomaly-triggered alerting.

Constraints:

- defensive only;
- isolated environments only;
- no offensive automation;
- no persistence, exploitation, or payload tooling;
- explicit authorization required.

