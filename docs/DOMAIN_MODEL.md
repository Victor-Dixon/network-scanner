# Domain Model — network-scanner

**Updated:** 2026-07-03  
**Evidence base:** `main.py`, `utils.py`, `anomaly_detection.py`,
`deep_anomaly_detection.py`, `threat_intelligence.py`,
`vulnerability_assessment.py`, `tests/`, `plans.txt`, and current project
documentation.

## Project identity

`network-scanner` is a defensive Python network-security diagnostics toolkit
for authorized environments. The implementation currently combines:

- IPv4 ARP host discovery.
- TCP port scanning and banner-grabbing helpers.
- Local SQLite-backed vulnerability lookup seeded with example data.
- AbuseIPDB IP reputation lookup.
- Isolation Forest and Keras autoencoder anomaly-detection experiments.
- Lightweight encrypted-traffic heuristic helpers.

The repository belongs to the **defensive network security diagnostics and
research** domain. It is for contributors or operators who need a small Python
codebase for experimenting with authorized local-network discovery,
vulnerability lookup, reputation checks, and anomaly-detection components.

## Problem statement

The project addresses the need to inspect authorized networks and related
security signals from a local Python toolkit:

1. Discover active IPv4 hosts on a network range.
2. Probe TCP ports and format scan results.
3. Look up known service/version vulnerabilities from a local store.
4. Check IP reputation against AbuseIPDB when credentials are configured.
5. Experiment with tabular anomaly detection over network-like feature data.

There is no implemented web UI, persistent scan-result store, role model,
distributed scanner, compliance report generator, plugin runtime, or packaged
application boundary in the current codebase.

## Core domain

**Authorized network security diagnostics**: collecting and interpreting
network, service, vulnerability, reputation, and anomaly signals for defensive
use on networks the operator is authorized to test.

## Subdomains

| Subdomain | Current implementation | Evidence | Status |
|---|---|---|---|
| Network discovery | ARP probe over an IPv4 CIDR/range and return discovered IP addresses | `main.scan_network` | Implemented |
| Port/service inspection | TCP connect scan, hostname resolution, banner grab, result formatting | `main.scan_ports_on_device`, `utils.py` | Partially implemented; not all helpers are wired into CLI |
| Vulnerability assessment | SQLite table plus example vulnerability seed and exact service/version query | `vulnerability_assessment.py`, `main --vuln-check` | Implemented with example data only |
| Threat intelligence | AbuseIPDB IP lookup using `ABUSE_IP_DB_API_KEY` | `threat_intelligence.check_ip_abuseipdb` | Implemented as direct API helper; import currently requires API key |
| Anomaly detection | Isolation Forest over 3-feature arrays; Keras autoencoder over CSV/tabular arrays | `anomaly_detection.py`, `deep_anomaly_detection.py` | Experimental modules |
| Encrypted traffic heuristics | Byte-pattern helpers for TLS, DoH, OpenVPN, SSH-like traffic | `utils.analyze_encrypted_traffic`, `utils.detect_tls_handshake` | Implemented helper functions |
| CLI orchestration | `argparse` flags for host discovery, sample anomaly run, and local vulnerability query | `main.py` | Implemented |
| Defensive deception governance | Principles and constraints only | `docs/DECEPTION_DEFENSE_PRINCIPLES.md`, `runtime/tasks/add_deception_governance_001.yaml` | Documentation/governance only |

## Major entities

| Entity | Description | Current representation |
|---|---|---|
| Authorized target scope | The network or host range the operator is allowed to inspect | User-provided string to `--scan-ip` / `scan_network`; authorization workflow is Unknown |
| Network range | IPv4 network or address range for ARP discovery | `ipaddress.ip_network(ip_range, strict=False)` validation |
| Network device | Discovered host on the scanned range | IP address string from ARP response `received.psrc` |
| Port | TCP port on a target IP | Integer in `scan_port`, `scan_ports`, `scan_ports_on_device` |
| Port scan result | Status of a host/port probe, optionally with banner text | Tuple expected by `format_scan_results`: `(IP, Port, Status, Banner)` |
| Service identity | Service name and version to check for vulnerabilities | CLI input `name:version`; function args `service_name`, `service_version` |
| Vulnerability | CVE-style record with description and affected service/version | SQLite row and dict `{cve_id, description}` |
| Vulnerability database | Local SQLite store for vulnerability records | `vulnerabilities.db` created at runtime by `initialize_database()` |
| IP reputation report | AbuseIPDB response data for an IP | Dict returned from `check_ip_abuseipdb` |
| Feature vector / dataset | Numeric input for anomaly models | NumPy arrays or CSV-loaded pandas data |
| Anomaly index | Position of a row classified as anomalous | NumPy array of row indices |
| Traffic packet | Raw packet bytes for heuristic classification | `bytes` argument to utility helpers |

## Value objects

The code does not define explicit value-object classes. The following values
act as value objects by convention:

- IPv4 network/range string: validated with `ipaddress.ip_network`.
- IP address or hostname string: passed to socket/scapy helpers.
- Port range tuple: `(start_port, end_port)`.
- Service/version pair: split from `name:version` in the CLI.
- CVE ID string: stored in SQLite and returned in vulnerability dicts.
- Feature matrix: two-dimensional NumPy array.
- Packet bytes: immutable bytes inspected by traffic heuristics.

## Services

| Service | Responsibility | Notes |
|---|---|---|
| CLI service (`main.main`) | Parse arguments, initialize vulnerability DB, dispatch selected actions | Initializes and seeds vulnerability DB on every run |
| Discovery service (`scan_network`) | ARP discovery for IPv4 network ranges | Uses scapy `srp`, `Ether`, and `ARP` |
| Port scanning helpers (`scan_port`, `scan_ports`, `scan_ports_on_device`) | TCP connect checks over one or more ports | `scan_ports_on_device` is in `main.py`; lower-level helpers are in `utils.py` |
| Reporting helper (`format_scan_results`) | Convert scan tuples to console text | No file report output implemented |
| Vulnerability store services | Create table, seed example data, query exact service/version matches | `fetch_vulnerability_data` uses static example data despite docstring referencing future API use |
| Threat intelligence client | Query AbuseIPDB and return response `data` | Missing API key raises during module import |
| NVD query helper | Query NVD CVE API by keyword | Exists in `threat_intelligence.assess_vulnerabilities`; not used by CLI |
| Isolation Forest model | Train and predict anomaly indices | Implementation currently enforces 3 input features |
| Autoencoder functions | Load/preprocess CSV, build/train model, detect reconstruction-error anomalies | Requires Keras runtime dependency that is not listed in `requirements.txt` |
| Traffic heuristic helpers | Classify selected encrypted traffic byte patterns | Heuristic-only; no packet capture integration shown |

## Relationships

- The CLI imports scanning, threat-intelligence, vulnerability, and utility
  modules.
- `main.main` initializes the local vulnerability database before processing
  any selected CLI action.
- `scan_network` returns IP strings; those IPs can be passed to port scanning
  helpers, but the CLI does not currently chain discovery into port scanning.
- `--vuln-check name:version` queries the local SQLite vulnerability store and
  prints matching CVE IDs and descriptions.
- `threat_intelligence.check_ip_abuseipdb` can enrich an IP address with
  reputation data, but no CLI flag currently invokes it.
- `anomaly_detection.AnomalyDetectionModel` is used by `main --analyze` with
  generated sample data. Current sample data uses 5 features while the model
  enforces 3 features, so that CLI path appears inconsistent.
- `deep_anomaly_detection.py` is independent from the CLI and tests.
- `utils` provides reusable helper functions for hostname, traffic, port, and
  banner operations.
- Deception-governance documents constrain future defensive research but do
  not map to runtime code today.

## Data flow

### CLI host discovery

1. User runs `python3 main.py --scan-ip <range>` or the equivalent local Python
   launcher.
2. `main.main` initializes and seeds the local vulnerability database.
3. `scan_network` validates the range with `ipaddress`.
4. scapy sends ARP broadcast packets.
5. Responding IPs are collected and printed.

### CLI vulnerability lookup

1. User runs `python3 main.py --vuln-check <service>:<version>` or the
   equivalent local Python launcher.
2. `main.main` initializes and seeds SQLite vulnerability data.
3. CLI input is split into service name and version.
4. `vulnerability_assessment.assess_vulnerabilities` queries exact matches.
5. Matching CVE IDs/descriptions are printed.

### CLI anomaly sample

1. User runs `python3 main.py --analyze` or the equivalent local Python
   launcher.
2. `AnomalyDetectionModel` is created.
3. Random NumPy training and test matrices are generated.
4. Model is trained, predictions are converted to anomaly row indices, and
   indices are printed.
5. Current code evidence indicates this path likely raises a feature-shape
   error because generated matrices have 5 features while the model requires 3.

### Direct AbuseIPDB lookup

1. Caller imports `threat_intelligence.check_ip_abuseipdb`.
2. Module loads `.env` and reads `ABUSE_IP_DB_API_KEY`.
3. Missing key raises `ValueError` at import time.
4. When configured, `requests.get` calls AbuseIPDB and returns the `data`
   object or `None` on request/format errors.

### Direct deep anomaly detection

1. Caller loads CSV data with `load_preprocess_data`.
2. Data is scaled with `MinMaxScaler`.
3. `train_autoencoder` splits data, builds a Keras model, and writes
   `autoencoder.h5` through `ModelCheckpoint`.
4. `detect_anomalies` compares reconstruction MSE against a threshold and
   returns anomalous row indices.

## User interactions

Implemented interactions:

- CLI:
  - `python3 main.py --scan-ip <IPv4 range>`
  - `python3 main.py --analyze`
  - `python3 main.py --vuln-check <service>:<version>`
- Direct Python imports for utility, vulnerability, threat-intelligence, and
  anomaly modules.
- Pytest suite for characterization and placeholder tests.

Unknown or not implemented from current evidence:

- Web UI.
- REST API.
- Authentication/authorization system.
- Scan profile management.
- Report export workflow.
- Operator approval workflow beyond documentation rules.
- Persistent scan history.
- Installed console entry point that resolves successfully.

## External integrations and dependencies

| Integration | Purpose | Current evidence |
|---|---|---|
| scapy | ARP discovery | `main.py`, `requirements.txt` |
| socket | TCP connect checks, hostname lookup, banner grab | `utils.py` |
| SQLite | Local vulnerability store | `vulnerability_assessment.py` |
| requests | AbuseIPDB and NVD HTTP calls | `threat_intelligence.py` |
| AbuseIPDB | IP reputation lookup | `check_ip_abuseipdb` |
| NVD API | Keyword CVE search helper | `threat_intelligence.assess_vulnerabilities` |
| scikit-learn | Isolation Forest, scaling, train/test split | anomaly modules |
| pandas / NumPy | Tabular data and arrays | anomaly modules |
| Keras | Autoencoder model | `deep_anomaly_detection.py`; not listed in `requirements.txt` |
| python-dotenv | Load `.env` for AbuseIPDB key | `threat_intelligence.py` |
| GitHub Actions / Codecov | CI and coverage upload | `.github/workflows/*.yml` |

## Feature-to-domain mapping

| Feature | Domain mapping | Implementation status |
|---|---|---|
| ARP network discovery | Network discovery subdomain; entities: network range, network device | Implemented in CLI |
| TCP port scan | Port/service inspection; entities: IP address, port | Helper implemented; CLI does not expose a port-scan flag |
| Banner grabbing | Port/service inspection; entities: port scan result, service banner | Helper implemented; not wired into CLI |
| Hostname lookup | Port/service inspection; entity: network device metadata | Helper implemented |
| Local vulnerability lookup | Vulnerability assessment; entities: service identity, vulnerability, DB | Implemented in CLI with example data |
| AbuseIPDB lookup | Threat intelligence; entity: IP reputation report | Helper implemented; no CLI flag; import-time key blocker |
| NVD keyword lookup | Vulnerability/threat intelligence integration | Helper implemented; not wired into CLI |
| Isolation Forest anomaly detection | Anomaly detection; entities: feature matrix, anomaly index | Module implemented; CLI sample appears shape-inconsistent |
| Deep autoencoder anomaly detection | Anomaly detection; entities: CSV dataset, model, anomaly index | Module implemented; dependency packaging incomplete |
| Encrypted traffic analysis | Traffic heuristic classification; entity: packet bytes | Helper implemented |
| Deception defense principles | Governance for future defensive research | Documentation only |
| Plugin architecture | Extensibility | Future item only; no implementation found |
| IPv6 support | Network discovery | Future item only; no implementation found |
| Compliance reporting | Reporting/compliance | Future item only; no implementation found |
| Distributed scanning | Scanning architecture | Future item only; no implementation found |

## Repository audit findings

### Architecture

- Flat top-level Python modules, not a package directory.
- `main.py` is the CLI entry point.
- Runtime state is minimal; the vulnerability database is created in the
  working directory at runtime.
- ML, network scanning, threat intelligence, and vulnerability lookup are
  separate modules.
- Tests live under `tests/`; CI workflows run pytest but one workflow allows
  failures to continue.

### Folder structure

- `docs/` contains governance/domain documentation.
- `runtime/tasks/` contains a completed governance task YAML.
- `.dreamos_reports/` contains a historical pytest blocker report.
- `.project/` contains portfolio metadata, not runtime code.
- There is no `src/`, `network_scanner/`, or package module directory.

### Documentation mismatches found during audit

- README previously contained placeholder client/config/API examples that do
  not exist in code.
- README inventory referenced `vulnerabilities.db`, but no tracked database
  file exists; the DB is created at runtime.
- `PROJECT_STRUCTURE_TREE.md` referenced `pytest.ini`, which is absent.
- PRD listed plugin architecture as a functional requirement even though it is
  only a future item in `plans.txt`.
- `setup.py` references `network_scanner.__main__:main`, but no matching
  package module exists.
- `setup.py` dependency metadata is incomplete for current imports
  (`scikit-learn`, `python-dotenv`, and Keras-related runtime are not all in
  `install_requires`).
- Threat-intelligence tests are documented as needing mocked/offline behavior,
  but importing the module still requires a real API key.

## Unknowns

These items cannot be determined from the repository and should not be assumed:

- Intended production deployment model.
- Supported operating systems beyond Python metadata and CI Linux runners.
- Required authorization/approval workflow for scans.
- Whether `plans.txt` items are committed product requirements or brainstorming
  notes.
- Expected network-traffic feature schema for anomaly detection.
- Source of real vulnerability data for the local SQLite database.
- Intended packaging layout and installable console command.
- Whether deception concepts are planned runtime features or only governance
  constraints.
