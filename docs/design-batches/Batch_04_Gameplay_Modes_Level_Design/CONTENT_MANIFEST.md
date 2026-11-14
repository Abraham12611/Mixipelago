# Batch 4 Content Manifest

All examples under `examples/missions` are candidate content. `coconut-cove-001` is a precise carry-forward from Batch 3; all `.draft.json` files are future-only, disabled. This batch does not certify an actual winning playthrough for any sample level.

`examples/modes/mode-registry.draft.json` declares the only intended live alpha mode: `service`. The registry is a design example, not an enabled backend implementation.

Integrity can be checked with `python tools/validate_batch4.py`. Run this before handing fixtures to a game engineer. Then implement actual headless Rapier tests and obtain owner manual UI approval before calling levels shippable.
