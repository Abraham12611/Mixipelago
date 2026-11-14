# Batch 19 test fixtures

Execute `python tools/validate_batch19.py` from this batch root. The tests check the JSON Schema (requires `jsonschema`), a safe draft catalog, uniqueness, the documented pure-rule vectors and deliberate mutations.

They do **not** test a running Next.js app, Rapier replay, GPU/audio quality, live financial settlement, actual Postgres RLS, native devices, policy compliance or owner manual acceptance. Add real integration evidence before enabling any production feature.
