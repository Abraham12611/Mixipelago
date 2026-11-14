# 41 — Engineer Kickoff, Build Order and Handoff Rules

**Batch 7 design status:** proposed · Not shipped · Interfaces and tuning subject to owner approval.

## Mission
Implement a small, correct, server-authoritative progression slice rather than an enormous empty skill tree. Do not implement skill points in the v0.1.0 browser physics alpha; target the v0.4.0 trusted-integration milestone after prerequisite verified campaign and wallet services exist.

## Day-zero read order
1. Batch 6 sections on trusted rewards, wallet/ledger and modifiers.
2. Batch 4 verified result receipt and mode scoring, Batch 5 campaign claim identity.
3. Batch 7 chapters 03–05, 14–18, 22, 30–36; review six branch briefs before touching UI.
4. Load catalog, schema, vectors and run `python tools/validate_batch7.py`.

## P0 execution
Parallel teams: schema/XP pure rules, trusted grant/DB transactions, catalog validator, and minimal mobile/desktop profile UI. Integrate only after CI passes unit property tests. Security reviewer verifies no direct client-write XP table; game director tests actual first-point comprehension and point spending.

## Branch discipline
Use PR per workstream, documented dependencies and feature flags; engineers **must not merge their own PRs**. Coordinator reviews and merges to integration branch; main requires owner's explicit approval where project policy applies. All manual UI/play-feel tests are routed to owner.

## Acceptance and next handoff
Provide test account with validated first-clear entitlement, observed transaction receipts and screenshots or demo URL for owner. Record any unresolved decision as an ADR. This batch is a specification; don't claim XP or skill trees are live because this repository contains documentation.
