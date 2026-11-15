# Mixipelago: Coconut Cove — Base44 × Nitro Contest Edition

**Status:** engineering/design documentation; **not** a deployed or submitted game.  
**Contest:** [Base44 × Nitro Web Game Contest](https://nitropay.com/base44webgame/)  
**Official binding rules:** [Terms and Conditions](https://nitropay.com/base44webgame/terms-and-conditions/)  
**Research verified:** 2026-11-15 UTC. Recheck rules at build and submission.

## Purpose

Create an **original new browser game using Base44 during the November 5–December 3, 2026 submission period**, under the Mixipelago concept, as a focused **Coconut Cove Contest Edition**. Publish it to a public **Base44 URL**. Do not embed a separately hosted legacy game inside a thin Base44 page and claim that satisfies the requirement. Obtain written organizer clarification if uncertain about using custom Phaser/Rapier code and the Base44 CLI.

This folder is **separate from** the 21-batch long-term engineering plan in [../../design-batches/](../../design-batches/). It is the contest-specific source of truth; long-term features do not become contest requirements by reference.

## Fast-track reading order

1. [00 — Rules and eligibility](00_RULES_AND_COMPLIANCE.md) — non-negotiable qualification gates.
2. [01 — Product requirements](01_CONTEST_EDITION_PRD.md) and [02 — scope matrix](02_SCOPE_FEATURE_MATRIX.md).
3. [03 — Base44 architecture](03_BASE44_BUILD_ARCHITECTURE.md) and [04 — originality/provenance](04_ORIGINALITY_IP_PROVENANCE.md).
4. [05 — gameplay contracts](05_CORE_GAMEPLAY_AND_RULE_CONTRACTS.md), [06 — missions](06_MISSIONS_BALANCING_AND_SOLVABILITY.md), and [07 — screen designs](07_UI_UX_RESPONSIVE_AND_ACCESSIBILITY.md).
5. [08 — guest persistence](08_GUEST_SAVE_PRIVACY_AND_SECURITY.md), [09 — asset pipeline](09_ART_AUDIO_ASSET_PRODUCTION.md), [10 — QA](10_TEST_STRATEGY_AND_ACCEPTANCE.md).
6. [11 — engineering tickets](11_WORKSTREAMS_ISSUES_AND_OWNERSHIP.md), [12 — delivery plan](12_RELEASE_PLAN_AND_CRITICAL_PATH.md), [13 — Base44 prompts](13_BASE44_PROMPTS_AND_STARTER_SETUP.md).
7. [14 — launch/submission](14_SUBMISSION_FREEZE_AND_EVIDENCE.md), [15 — community marketing](15_COMMUNITY_VOTE_AND_MEDIA.md), [16 — risk register](16_RISKS_ADRS_AND_OPEN_DECISIONS.md), [17 — definition of done](17_REQUIREMENTS_TRACEABILITY_AND_DOD.md).
8. [18 — implementation handoff](18_ENGINEER_START_HERE.md), [19 — feasibility spike](19_PLATFORM_FEASIBILITY_SPIKE.md), [20 — contest copy](20_CONTEST_SUBMISSION_COPY.md), [21 — release operations](21_DEPLOYMENT_RUNBOOK.md).

## Contest snapshot

- Opens **November 5, 2026 00:00 UTC**; closes **December 3, 2026 23:59 UTC**.
- Expected judging December 4–9; announcement on/about December 10.
- Play without login, payment, download, extension, installation or mandatory purchases.
- New Base44-created game, original assets/code/content or properly licensed materials.
- Public Base44-hosted link; no custom domain for submission (contest FAQ).
- Keep live through judging and at least 90 days after *actual* winner announcement.
- Gameplay Quality, Creativity and Technical Execution judged equally.
- Only one game per entrant/team. Team maximum **four natural persons** under official terms (the landing-page FAQ has conflicting simplified wording; terms govern).

## Product boundary

**Target:** 12 carefully authored, tested Coconut Cove missions (expand to 20 only if they all pass quality gates); eight drink tiers; physics shooting, deterministic same-tier merging; two active customer orders in the first classic mission; guest local progress; 1 island map; 1 classic mode and at most 1 festival challenge if polished; original sound/art; readable mobile/desktop UI.

**Disabled:** account requirement, commerce, advertisements, real-money offers, online leaderboards, real multiplayer, 21-batch future backend, insurance/debt, deep incidents, notifications, referral/paid voting.

**Important:** This repository was inspected and had documentation rather than a playable app at the time of planning. Never claim implementation or contest acceptance from the existence of these files.

## Coordination

Engineers write scoped PRs and **do not self-merge**. Coordinator reviews; owner approves merges to main when required by repo governance. **All manual UI/gameplay tests are performed or directed by the owner.** Automatic tests can be run by engineers.

## Additional contracts and fixtures

- [22 — Cross-batch compatibility](22_CROSS_BATCH_COMPATIBILITY.md) — exactly what is reused versus excluded.
- [23 — Official sources and rule change log](23_OFFICIAL_SOURCES_AND_CHANGELOG.md).
- [24 — Content authoring and validation](24_CONTENT_AUTHORING_AND_VALIDATION.md).
- [Contest draft manifest](examples/contest-plan.draft.json) — **all 12 levels are draft, unpublished**.
- [QA tracking fixtures](examples/qa-checks.draft.json) and [asset-rights template](examples/rights-inventory.template.json).
- Run the [static fixture validator](tools/validate_contest_plan.py) before editing example catalog contents.

**No Base44 contest app has been created, deployed or submitted by these documentation changes.**
