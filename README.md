# Network-Scanner

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
![CI/CD](https://github.com/Victor-Dixon/network-scanner/actions/workflows/ci.yml/badge.svg)

Defensive Python network-security toolkit for authorized environments: ARP
IPv4 host discovery, TCP port/banner helpers, local vulnerability checks,
AbuseIPDB reputation lookup, and ML anomaly-detection experiments.

> Use this project only on networks and systems you own or are explicitly
> authorized to test.

## What this project is

`network-scanner` is a small Python codebase in the defensive network security
diagnostics domain. It models the early stages of local security assessment:
finding hosts, probing ports, checking service/version vulnerability records,
looking up IP reputation, and experimenting with anomaly detection over
network-like feature data.

The full domain model is documented in [`docs/DOMAIN_MODEL.md`](docs/DOMAIN_MODEL.md).

## What problem it solves

The repository gives contributors a local, inspectable toolkit for combining:

- authorized IPv4 network discovery;
- TCP port and banner helper functions;
- local vulnerability lookup for service/version pairs;
- optional AbuseIPDB IP reputation checks;
- tabular anomaly-detection model experiments;
- defensive governance notes for any future deception-related research.

It is not a production-ready enterprise scanner, attack framework, exploitation
toolkit, compliance platform, or distributed scanning system.

## Repository description

Recommended GitHub repository description:

> Defensive Python network-security toolkit for authorized environments: ARP
> IPv4 host discovery, TCP port/banner helpers, local vulnerability checks,
> AbuseIPDB reputation lookup, and ML anomaly-detection experiments.

## Implemented features

| Feature | Where it lives | Status |
|---|---|---|
| IPv4 ARP discovery | `main.scan_network` | CLI-exposed via `--scan-ip` |
| TCP port scanning | `utils.scan_port`, `utils.scan_ports`, `main.scan_ports_on_device` | Helper functions; no dedicated CLI flag |
| Banner grabbing | `utils.banner_grab` | Helper function |
| Hostname lookup | `utils.get_host_name` | Helper function |
| Scan result formatting | `utils.format_scan_results` | Helper function |
| Local vulnerability DB | `vulnerability_assessment.py` | CLI-exposed via `--vuln-check`; uses example seed data |
| AbuseIPDB lookup | `threat_intelligence.check_ip_abuseipdb` | Direct helper; requires `ABUSE_IP_DB_API_KEY` at import time |
| NVD keyword lookup helper | `threat_intelligence.assess_vulnerabilities` | Direct helper; not wired into CLI |
| Isolation Forest anomaly detection | `anomaly_detection.py` | Module and sample CLI path; sample path appears shape-inconsistent |
| Keras autoencoder anomaly detection | `deep_anomaly_detection.py` | Direct module; packaging dependencies incomplete |
| Encrypted traffic heuristics | `utils.analyze_encrypted_traffic`, `utils.detect_tls_handshake` | Direct helper functions |
| Deception-defense constraints | `docs/DECEPTION_DEFENSE_PRINCIPLES.md` | Documentation only |

## Not implemented or unknown

- No web UI or REST API is present.
- No user account, role, authentication, or approval workflow is implemented.
- No scan history store or report export workflow is implemented.
- No plugin runtime is implemented.
- No IPv6 discovery implementation was found.
- No distributed scanning architecture was found.
- No compliance report generator was found.
- The intended production deployment model is Unknown.
- The expected real anomaly-detection feature schema is Unknown.

## Installation

```bash
git clone https://github.com/Victor-Dixon/network-scanner.git
cd network-scanner
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Notes from the current audit:

- `requirements.txt` includes the main scanner/test dependencies that are
  known to the repository.
- `deep_anomaly_detection.py` imports Keras, but no Keras/TensorFlow dependency
  is listed in `requirements.txt`.
- `setup.py` metadata does not currently define a working package layout; this
  repository is most accurately run from the source tree with `python main.py`.

## Configuration

The only documented runtime credential in code is:

```bash
export ABUSE_IP_DB_API_KEY=your_abuseipdb_key
```

`threat_intelligence.py` currently raises `ValueError` during import if
`ABUSE_IP_DB_API_KEY` is missing. This is a known blocker for offline test
collection and should be fixed before treating the test suite as stable.

No `config.json`, `.env.example`, `DATABASE_URL`, `--config`, `--api-key`, or
`--database-url` implementation was found.

## Usage

Show CLI help:

```bash
python main.py --help
```

Discover hosts on an authorized IPv4 range:

```bash
python main.py --scan-ip 192.168.1.0/24
```

Check the local vulnerability database for an exact service/version pair:

```bash
python main.py --vuln-check nginx:1.16.1
```

Run the sample anomaly-detection path:

```bash
python main.py --analyze
```

Known issue: `--analyze` currently generates 5-feature random data while
`AnomalyDetectionModel.train` enforces 3 features, so this path appears
inconsistent with the model contract.

## Direct Python helpers

```python
from utils import scan_ports, banner_grab, format_scan_results
from vulnerability_assessment import assess_vulnerabilities

open_ports = scan_ports("192.168.1.10", (1, 1024))
banner = banner_grab("192.168.1.10", 80)
vulnerabilities = assess_vulnerabilities("nginx", "1.16.1")

print(open_ports)
print(banner)
print(vulnerabilities)
```

## Architecture

The project currently uses a flat module layout:

- `main.py` — CLI entry point and ARP scan orchestration.
- `utils.py` — socket helpers, formatting, banner grabbing, and traffic
  heuristics.
- `vulnerability_assessment.py` — runtime-created SQLite vulnerability store.
- `threat_intelligence.py` — AbuseIPDB and NVD HTTP helpers.
- `anomaly_detection.py` — Isolation Forest anomaly model wrapper.
- `deep_anomaly_detection.py` — Keras autoencoder anomaly functions.
- `tests/` — pytest/unittest characterization and placeholder tests.
- `docs/` — domain and defensive-governance documentation.

See [`PROJECT_STRUCTURE_TREE.md`](PROJECT_STRUCTURE_TREE.md) for the current
tree summary.

## Testing

```bash
pytest -q
```

Known test and verification blockers:

- Importing `threat_intelligence.py` requires `ABUSE_IP_DB_API_KEY`.
- Some tests rely on optional or missing dependencies depending on the
  environment, including Keras/TensorFlow for `deep_anomaly_detection.py`.
- `tests/test_basic.py` contains generic placeholder tests and pytest marks
  that are not registered in a `pytest.ini`.
- The CI workflow `.github/workflows/ci.yml` allows test failures to continue;
  `.github/workflows/tests.yml` runs pytest as a stricter test workflow.

Historical blocker details are captured in
`.dreamos_reports/pytest_blocker.txt`.

## Current project status

Status source-of-truth documents:

- [`PRD.md`](PRD.md) — product scope and domain requirements.
- [`ROADMAP.md`](ROADMAP.md) — current, next, and later work.
- [`MASTER_TASK_LIST.md`](MASTER_TASK_LIST.md) — task backlog and completion
  state.
- [`MASTER_TASK_LOG.md`](MASTER_TASK_LOG.md) — dated project execution log.
- [`NEXT_UP.md`](NEXT_UP.md) — immediate next work.
- [`PRODUCTION_READINESS.md`](PRODUCTION_READINESS.md) — honest readiness
  gates.
- [`AGENTS.md`](AGENTS.md) — contributor/agent operating rules.

Current readiness: **not production-ready**. The codebase is useful as a
defensive security diagnostics and research toolkit, but documentation,
packaging, offline tests, and some CLI paths need hardening.

## Roadmap summary

Immediate work should focus on making the current behavior reliable before
adding new product scope:

1. Remove import-time API-key failure from `threat_intelligence.py`.
2. Make threat-intelligence tests offline and mocked by default.
3. Register pytest markers and remove placeholder tests.
4. Fix or document missing runtime dependencies for deep anomaly detection.
5. Reconcile CLI anomaly sample data with the 3-feature model contract.
6. Clarify or fix package metadata and console entry point.

Future ideas from `plans.txt` include IPv6 support, OS fingerprinting,
additional threat-intelligence feeds, automated vulnerability data ingestion,
compliance reporting, scanning profiles, distributed scanning, UEBA, and plugin
architecture. These are not implemented unless explicitly noted above.

## Contributing

- Keep scans and tests offline/mocked unless a target is explicitly authorized.
- Do not commit API keys, `.env` files, local databases, virtualenvs, or scan
  artifacts.
- Update the domain model and status docs whenever behavior or scope changes.
- Prefer small, evidence-backed changes over broad rewrites.

## License

This project is licensed under the MIT License. See [`LICENSE`](LICENSE).
