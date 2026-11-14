# 28 — Parallel Engineering Tickets and Coordination Rules

**Status:** Batch 6 design/engineering handoff · 2026-11-14 · Proposed, not shipped.

## Workstreams
A — contracts and economic model; B — PostgreSQL and ledger; C — reward adapters and proof; D — shops, upgrades and modifiers; E — React/Phaser shop art/UI; F — economy admin/content tools; G — analytics, automation and QA. These can run in parallel after interfaces are accepted.

## Ticket backlog
| ID | Owner workstream | Ticket | Depends on |
|---|---|---|---|
| ECO-001 | A | Canonical currency, wallet and ledger types | B1–B5 |
| ECO-002 | A | Catalog schema + JSON validator | 001 |
| ECO-003 | B | Wallet and immutable ledger migrations | 001 |
| ECO-004 | B | Atomic credit/debit service | 003 |
| ECO-005 | B | Idempotency command journal and replay | 004 |
| ECO-006 | C | Verified Batch 4 mission reward adapter | 001,004 |
| ECO-007 | C | First-clear unique payout semantics | 006 |
| ECO-008 | C | Batch 5 treasure claim integration | 006 |
| ECO-009 | D | Shop and owned-upgrade tables | 002,003 |
| ECO-010 | D | Upgrade resolver and prerequisites | 002,009 |
| ECO-011 | D | Purchase transaction command | 004,010 |
| ECO-012 | D | Pure modifier resolver, ranked guard | 010 |
| ECO-013 | E | Shop overview/detail responsive UI | 002 |
| ECO-014 | E | Upgrade preview and confirmation sheet | 013 |
| ECO-015 | E | Wallet and history UI | 004 |
| ECO-016 | E | Cosmetics equipment and shop art slots | 009,013 |
| ECO-017 | F | Draft/publish immutable upgrade catalog | 002 |
| ECO-018 | F | Reward policy authoring and dry run | 006,017 |
| ECO-019 | G | Integration QA: double spends/claims | 004,011 |
| ECO-020 | G | Ledger reconciliation job + alerting | 003 |
| ECO-021 | G | API contract, RLS and authentication tests | 003,011 |
| ECO-022 | G | Dashboard faucet/sink metrics | 006,011 |
| ECO-023 | D | VIP customer modifier integration | 012,B3 |
| ECO-024 | E | Owner-led manual UI review preparation | 013–016 |
| ECO-025 | F | Feature-gate kill switches and rollback drills | 017,020 |

## PR ownership and merge rules
Engineers work in isolated branches, submit PRs with test evidence, risks, migration paths and any blocked contracts; **engineers do not merge their own PRs**. Coordinator reviews and merges into development integration branch. Production/main promotion requires owner approval. No speculative new product scope without an ADR.
