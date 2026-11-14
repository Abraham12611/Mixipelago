# Example catalog, policies and test vectors

**No example is production data.** `draft.json` files are design fixtures; IDs and values are proposals awaiting balance review and integration.

- `catalog/skills-catalog.draft.json`: six branches, 30 illustrative nodes, six flagged as `pilot` and 24 as gated `draft`.
- `catalog/entrepreneur-xp-policy.draft.json`: level 1–20 cumulative thresholds and 19 milestone points.
- `schemas/skill-catalog.schema.json`: JSON Schema 2020-12 for syntax and data types; semantic DAG/feasibility validation requires the Python tool.
- `tests/xp-rule-vectors.json`: threshold and cap expected values.
- `tests/allocation-modifier-rule-vectors.json`: authorization, rank purchase, cap, respec and competition examples.
- `contracts/progression-api.draft.json`: shapes only; never place server secrets or grant authority in clients.
- `contracts/sample-player-projection.draft.json`: synthetic user for UI/QA, not personal data.
- `sql/progression_schema_draft.sql`: illustrative PostgreSQL schema, **not** migration-ready and must be reviewed.

Run `python tools/validate_batch7.py` from batch root. It tests static catalog, point math and sample vectors. It does not run browser UI, the real economy service, physics simulations or load tests.
