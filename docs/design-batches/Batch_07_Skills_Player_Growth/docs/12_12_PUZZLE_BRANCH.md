# 12 — Puzzle Specialist Skill Branch: Planning and Boosters

**Batch 7 design status:** proposed · Not shipped · Interfaces and tuning subject to owner approval.

## Purpose
Make deliberate technical play clearer and support advanced casual play without pay-to-win leaderboards or a separate physics reality per player.

## Proposed nodes
- `pz_next_peek`: show one additional queued spawn in supported casual modes; respects mission seed and information policy.
- `pz_contact_hint`: highlight predicted target contact area before release; preview is advisory, not an authoritative physics result.
- `pz_chain_reader`: inspect potential tier evolution after a planned legal merge; never auto-trigger it.
- `pz_booster_pocket`: extra *inventory capacity* for selected noncompetitive boosters, not free purchases or duplicated items.
- `pz_precise_workflow`: configurable aim lock, touch sensitivity settings; baseline accessibility alternatives are free regardless of talent.

## Mode gating
Ranked, tournament and friend-standardized levels use a canonical assistance policy. Depending on mode, `pz_next_peek` may be disabled, or all players may receive the same peek. Disclosure must be present before entering a normalized mode.

## Physics constraints
The aim helper consumes an immutable snapshot and computes a best-effort visual path; it does not write to Rapier bodies, modify shot impulse, force merges or override collision arbitration. A `peek` never consumes the queue or changes RNG. Proof/replay format records the mode assistance policy.
