# Production Readiness

## Current Status

Not production-ready.

## Blocking Issues

- Full pytest does not pass.
- `threat_intelligence.py` fails at import when API key is missing.
- sklearn and scapy dependencies are missing in current environment.
- Tests need mock boundaries for network/API operations.

## Required Gates

- `pytest -q` passes without live API keys.
- Network scanning requires explicit authorized targets.
- API integrations are mocked in unit tests.
