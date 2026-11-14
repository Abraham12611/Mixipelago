# 26 — Architecture Decision Records, Risks and Owner Approvals

## Confirmed carry-forward decisions

| Decision | Status | Rationale |
|---|---|---|
| DRA-001: single core chain tiers 1–8 | Carry-forward baseline | Quick, recognizable merge mechanic |
| DRA-002: same-tier pair merges | Carry-forward baseline | Physical rule clarity |
| DRA-003: max tier 8 terminal | Carry-forward baseline | Defined alpha scope |
| DRA-004: output tier determines base score | Carry-forward baseline | Consistent reward math |
| DRA-005: serve newly produced item before next remerge | Carry-forward baseline | Batch 1/2 order contract |
| DRA-006: local preview coins in alpha | Carry-forward baseline | No untrusted economic minting |
| DRA-007: content hash pinned per run | Carry-forward baseline | Replay/content safety |

## Proposed decisions requiring owner approval

**DRA-008:** The full game eventually has multiple drink families and explicit named recipes rather than one global tier. Proposed because varied islands need unique content. Migration required before first multi-family mode.

**DRA-009:** Future ingredient crafting happens in a separate optional workshop, not automatically on ordinary tabletop collisions. Protects clarity of core shooter mechanics.

**DRA-010:** Secret recipes require hints and an explicit Research Mode. Avoids unexpected outcomes that sabotage normal orders.

**DRA-011:** Rarity is primarily cosmetic/collection prestige, not inherent merge power. Ranked modes normalize all special advantages.

**DRA-012:** Drink mastery XP comes only from validated results and has anti-farm caps; thresholds and numerical values remain TBD.

**DRA-013:** Avoid irreversible missable collection rewards; publish season rerun or alternative acquisition options where sensible.

**DRA-014:** Recipe themes should remain family-friendly mocktails and fantasy beverages; confirm labeling standards before native store launch.

**DRA-015:** A future catalog publisher cannot change active-session scores, priorities or recipe graph without new pinned manifest.

## Risks and controls

| Risk | Consequence | Mitigation |
|---|---|---|
| Catalog expands without IDs | Broken saves and reruns | Immutable IDs & version pinning |
| Recipe ambiguity in collision | Unpredictable merges | Offline resolver validation, explicit choices |
| Automatic service disrupts chains | Player frustration | Transparent order prompts, curated missions |
| High-tier input explosion | Grindy levels | Cost analyzer, seeded starting bodies |
| Distinct art looks identical small | Mis-shots | Distinct silhouettes, icons, accessibility labels |
| Rare collectible affects ranking | Pay-to-win | Cosmetics only or ranked normalization |
| Local preview migrated to wallet | Exploit | Reject unverified client minting |
| Content publish invalidates run | Lost progress | Session hash pinning, rollback |
| AI-generated frames inconsistent | Visual jitter | Single-source renders/asset validation |
| Optional mechanics launch too early | Delayed alpha | Feature gates and explicit release boundaries |

## Open owner questions

1. Should all eight working drink names remain as designed? The canon currently uses provisional names.
2. Should a future recipe family always be a separate mission mode, or can players choose a family per launch?
3. Should hidden discoveries influence shop cosmetics, customer reputation or only collections?
4. Will mastery grant pure cosmetic rewards at first, or bounded campaign utility?
5. When does the recipe journal become visible in the tutorial?
6. Should older event-exclusive drinks return seasonally?
7. Will ingredient research ever consume coins, and with what refund policy?
8. Should a terminal tier-8 output be recyclable in a future mode to avoid board deadlock?

Owner answers are not blockers for alpha if those systems remain gated off. Record outcomes in a central decisions log when agreed. Until then, proposed mechanics must not be presented as implemented or irreversible policy.
