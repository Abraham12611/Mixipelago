# Batch 9 Rule Tests

`customer-rule-vectors.json` defines expected outputs for pure candidate policies, not proof that gameplay, backend or browser features are implemented. Run `python tools/validate_batch9.py` from the batch root (requires `jsonschema`).

Scenarios cover VIP chance caps, verified-only satisfaction, per-encounter/run reputation caps, loyalty visits and tiers, canonical weighted customer selection, oldest matching order priority and source deduplication.

**Important:** Static order priority tests do not prove a mission can be physically completed. Actual Rapier winning-trace checks and owner-directed manual UI gameplay tests are required before publishing dynamic orders.
