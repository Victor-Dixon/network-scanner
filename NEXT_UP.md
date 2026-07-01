# NEXT UP

**Updated:** 2026-07-01

## Current focus

1. Refactor `threat_intelligence.py` so missing API keys fail at call time, not import time.
2. Add mocked unit tests for AbuseIPDB lookup.
3. Re-run pytest with optional scapy/sklearn deps documented.

## Verify

```bash
pytest -q
```
