# Production Readiness — network-scanner

**Status:** NOT production-ready (honest baseline)  
**Updated:** 2026-08-14  
**Domain:** defensive network security diagnostics for authorized environments.

## What this project is

`network-scanner` is a Python toolkit for authorized IPv4 host discovery,
port/banner helper functions, local vulnerability lookup, IP reputation checks,
and anomaly-detection experiments.

## Why it exists

It exists as an inspectable defensive security diagnostics and research codebase,
not as a production scanner or offensive tool.

## Readiness gates

| Gate | Status | Evidence |
|---|---|---|
| Domain model | PASS | `docs/DOMAIN_MODEL.md` |
| README | PASS | `README.md` now describes implemented features, Unknowns, and blockers |
| PRD | PASS | `PRD.md` separates current requirements from future ideas |
| Roadmap/status docs | PASS | `ROADMAP.md`, `MASTER_TASK_LIST.md`, `MASTER_TASK_LOG.md`, `NEXT_UP.md` |
| Agent/contributor rules | PASS | `AGENTS.md` |
| Project tree docs | PASS | `PROJECT_STRUCTURE_TREE.md` |
| CI workflows present | PASS | `.github/workflows/ci.yml`, `.github/workflows/tests.yml` |
| Tests | PASS | `python3 -m pytest -q`: `56 passed` |
| Packaging metadata | BLOCKED | flat modules; stale console entry point documented |
| License | PASS | `LICENSE` (MIT) |
| No committed secrets | REVIEW | no secrets observed in docs audit; continue to keep API keys in env only |
| Runtime DB handling | REVIEW | `vulnerabilities.db` is created at runtime and should not be committed |

## Completed

- Governance artifact baseline.
- Defensive deception principles.
- Documentation-first domain model audit.
- README, PRD, roadmap, master task list/log, next-up, readiness, structure,
  consolidation, and agent docs synchronized to current implementation evidence.
- Recommended GitHub repository description documented in README.

## Blocking issues

- Latest local verification on 2026-08-14:
  - `python3 -m pytest -q`: `56 passed`.
  - `git diff --check`: PASS.
- `deep_anomaly_detection.py` imports Keras, but Keras/TensorFlow dependency
  handling is not documented in package metadata.
- `tests/test_basic.py` contains generic placeholder tests.
- `main.py --analyze` appears inconsistent: it generates 5-feature sample data
  while `AnomalyDetectionModel` enforces 3 features.
- `setup.py` references a non-existent `network_scanner.__main__:main` package
  entry point.

## What remains

1. Resolve dependency and package metadata gaps.
2. Reconcile anomaly CLI behavior with model contract.
3. Replace remaining placeholder tests with product-specific tests.
4. Add an explicit no-network/default-offline test lane.
5. Decide which future `plans.txt` items become accepted product scope.

## Client-show criteria

The public repository should present:

- clear defensive purpose and target user;
- explicit domain model and feature mapping;
- install/run steps that match code;
- honest limitations and Unknowns;
- CI badge and license;
- no claims for unimplemented architecture or features.
