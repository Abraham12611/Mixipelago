# Fixture scope

These JSON cases test **pure rules** only: tier compatibility, score formulas, idempotent event reduction, terminal priority, active ticks, shot debits and preview coin aggregation. The included Python script can validate structural and arithmetic consistency, but cannot prove a physical shot or mission win. Engineers must create actual Rapier/Phaser golden traces and owner manual review evidence before publishing levels.

Future draft mode missions are disabled by `releaseStatus:planned` and `featureFlag`. They are examples for engineers, not player-accessible levels. `coconut-cove-001.json` is copied byte-for-byte from Batch 3, ensuring continuity.
