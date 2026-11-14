# Engineering Kickoff — Batch 7

1. Read Batch 6 authoritative ledger/modifier contracts; Batch 4 verified result receipts; Batch 5 mission claim identities.
2. Read [Batch 7 index](docs/00_INDEX_AND_README.md), then sections 03–05, 14–18 and 30–37.
3. Run `python tools/validate_batch7.py` (optionally install `jsonschema` to validate JSON Schema syntactically).
4. Implement **trusted player XP and point allocation**, not an empty 30-node clickable tree. Six `pilot` nodes in the fixture are candidate first-slice options, and still need dependency gates.
5. Do not grant XP from client events, local preview balances, raw merge actions or unverifiable mission clears.
6. No self-merges: each engineer opens PRs to an integration branch; coordinator reviews. Main branch and manual UI acceptance remain owner-controlled under established policies.

**Deliver**: verified mission->XP adapter, atomic point allocation, version-pinned modifier snapshot, minimally usable React UI, security/race tests, owner test instructions, flag-based rollback.
