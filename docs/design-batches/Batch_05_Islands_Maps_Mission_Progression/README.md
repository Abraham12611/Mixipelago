# Mixipelago — Batch 5: Islands, Maps & Mission Progression

**Documentation batch:** 5/21 · **Status:** authored design + validated static examples, **not implemented**.

Start with [ENGINEER_START_HERE.md](ENGINEER_START_HERE.md), then [docs/00_INDEX_AND_README.md](docs/00_INDEX_AND_README.md).

The campaign is a versioned graph, not a list of hardcoded levels. Mission content remains in Batch 4; the map references IDs and pinned versions. Content authors can add islands/paths through data and an eventual graph editor.

**Scope:** island hierarchy, graph schema, nodes/edges, prerequisites, star progress, hidden routes, gateways, treasures, map UX, camera, art pipeline, local preview, backend migration, analytics, QA, release gates and engineering workstreams. Future narrative/economy/events are intentionally overview-only.

### Quick start

```bash
python -m pip install jsonschema
python tools/validate_batch5.py
```

Validation checks schema, references, DAG cycles, sample rules and expected failures. It cannot prove missions are winnable or the UI has been built.

### Source of truth

Prior Batch 4 mission files `coconut-cove-001.json` and `coconut-cove-002.json` are included unchanged. All new graph and API structures are **proposals requiring implementation and owner approval**.
