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

## Current state

The repository remains **not production-ready**. Full pytest collection may be
blocked by credential handling, optional deep-learning dependencies,
unregistered markers, placeholder tests, and anomaly CLI/model mismatch.

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

## Standard Repository Working Contract
1. Read `AGENTS.md`, `NEXT_UP.md`, `MASTER_TASK_LIST.md`, `MASTER_TASK_LOG.md`, any repo SSOT/state manifest, branch/HEAD, and relevant tests before editing.
2. Work one bounded lane with explicit **TARGET, ACTION, VERIFY, COMMIT**. Do not mix unrelated cleanup, features, migrations, or speculative rewrites.
3. Use Fast TDD: smallest acceptance test, smallest safe change, targeted verification, then broad verification.
4. When repo state changes, update `NEXT_UP.md` and `MASTER_TASK_LIST.md` in the same lane, plus the execution-state SSOT when present.
5. Append `MASTER_TASK_LOG.md` only after verification proves closure. Never record planned or merely implemented work as completed.
6. For non-trivial work, create/update `runtime/tasks/*.yaml` with objective, scope, acceptance, verification, holds, and next lane when supported.
7. Trust but verify: targeted tests, repo validators, `git diff --check`, and final status/diff review. PASS/COMPLETE/deployed/merged claims require evidence.
8. Salvage before destructive cleanup. Classify variants/donor material before delete/reset/rewrite; preserve canonical source unless evidence proves it stale.
9. End code or repo-structure work with a clean scoped commit. Planning-only work still requires synchronized task surfaces and verification.
10. Leave the next executable step in `NEXT_UP.md` with its verification gate so the next agent does not rediscover the lane.

### Canonical Planning Names
Fleet-standard root planning names are `NEXT_UP.md`, `MASTER_TASK_LIST.md`, and `MASTER_TASK_LOG.md`. Existing explicit repo SSOTs remain authoritative until deliberately migrated; compatibility mirrors must not become competing authorities.
