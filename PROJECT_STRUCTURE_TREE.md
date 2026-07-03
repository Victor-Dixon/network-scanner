# Project Structure Tree

**Updated:** 2026-07-03  
**Domain:** defensive network security diagnostics for authorized environments.

## What this project is

`network-scanner` is a flat-module Python toolkit for authorized IPv4 host
discovery, port/banner helper functions, local vulnerability lookup, IP
reputation checks, and anomaly-detection experiments.

## Current tree summary

```text
network-scanner/
├── main.py                         # CLI entry point and ARP discovery
├── utils.py                        # socket, banner, formatting, traffic helpers
├── vulnerability_assessment.py     # local SQLite vulnerability lookup
├── threat_intelligence.py          # AbuseIPDB and NVD HTTP helpers
├── anomaly_detection.py            # Isolation Forest anomaly model
├── deep_anomaly_detection.py       # Keras autoencoder anomaly functions
├── requirements.txt                # source-tree dependency list
├── setup.py                        # package metadata; entry point is currently stale
├── README.md                       # project overview, usage, status
├── PRD.md                          # implementation-derived requirements
├── ROADMAP.md                      # current/next/later work
├── MASTER_TASK_LIST.md             # backlog and completed work
├── MASTER_TASK_LOG.md              # dated execution log
├── NEXT_UP.md                      # immediate next work
├── PRODUCTION_READINESS.md         # honest readiness gates
├── AGENTS.md                       # agent/contributor rules
├── CONSOLIDATION_MANIFEST.md       # portfolio/consolidation status
├── LICENSE
├── docs/
│   ├── DOMAIN_MODEL.md
│   └── DECEPTION_DEFENSE_PRINCIPLES.md
├── tests/
│   ├── test_anomaly_detection.py
│   ├── test_basic.py
│   ├── test_check_ip_abuseipdb.py
│   ├── test_deep_anomaly_detection.py
│   ├── test_main.py
│   ├── test_threat_intelligence.py
│   ├── test_utils.py
│   └── test_vulnerability_assessment.py
├── .github/workflows/
│   ├── ci.yml
│   └── tests.yml
├── .dreamos_reports/
│   └── pytest_blocker.txt
├── .project/
│   └── tasks.json
└── runtime/tasks/
    └── add_deception_governance_001.yaml
```

## Important absences

- No `pytest.ini` is present.
- No `src/` directory is present.
- No `network_scanner/` package directory is present.
- No tracked `vulnerabilities.db` file is present; SQLite DB files are created
  at runtime by `vulnerability_assessment.initialize_database()`.
- No web UI, REST API, plugin runtime, distributed scanner, scan-profile store,
  or compliance-reporting directory is present.

## Documentation status

The domain model, PRD, roadmap, task list/log, next-up, production-readiness,
README, and AGENTS docs were synchronized on 2026-07-03. Future file additions
should update this structure summary and `docs/DOMAIN_MODEL.md`.

Note: local virtualenv directories are gitignored and are not part of the public
tree.
