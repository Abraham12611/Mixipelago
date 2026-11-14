# Batch 14 — Test Fixtures

The vectors test **pure rule semantics** only, not deployed servers. Source cases are intentionally small and readable; engineers should add property tests, concurrency tests, and actual browser/playtesting as the system is implemented. The invalid-case mutations must be rejected by sample-schema or domain validation.

Run `python tools/validate_batch14.py` from package root. You need Python 3.11+ and `jsonschema`.
