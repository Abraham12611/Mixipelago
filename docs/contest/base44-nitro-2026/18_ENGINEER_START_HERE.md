# 18 — Engineer Kickoff and Immediate Implementation Handoff

**Build objective:** an **original, self-contained Mixipelago: Coconut Cove contest edition** created and meaningfully built in Base44, publicly playable without account or payment. Do not interpret this document as authorization to submit on the owner's behalf or to add working code to the 21-batch main roadmap.

## Start sequence

1. Read [Rules](00_RULES_AND_COMPLIANCE.md) and [PRD](01_CONTEST_EDITION_PRD.md).
2. Build platform proof before broad implementation: [Base44 feasibility](19_PLATFORM_FEASIBILITY_SPIKE.md), then [architecture](03_BASE44_BUILD_ARCHITECTURE.md).
3. Review original eight-tier drinks and physics/serving contracts: [gameplay rules](05_CORE_GAMEPLAY_AND_RULE_CONTRACTS.md).
4. Implement first complete level before drawing the whole map; [mission proof](06_MISSIONS_BALANCING_AND_SOLVABILITY.md).
5. Read [responsive UI](07_UI_UX_RESPONSIVE_AND_ACCESSIBILITY.md), [assets](09_ART_AUDIO_ASSET_PRODUCTION.md), [guest data](08_GUEST_SAVE_PRIVACY_AND_SECURITY.md).
6. Follow [issue breakdown](11_WORKSTREAMS_ISSUES_AND_OWNERSHIP.md) and [critical path](12_RELEASE_PLAN_AND_CRITICAL_PATH.md).
7. Bring finished code to automated test + owner manual validation; [QA](10_TEST_STRATEGY_AND_ACCEPTANCE.md).

## First deliverables

**First integration checkpoint**: public new Base44 game with Home / Play / Map / Results, a playable tutorial shot and one merge. Developer must show the real Base44 project history and published URL, plus a short proof that it loads in an incognito browser. If that fails, engineering should not proceed into 12 mission authoring.

**Second checkpoint**: one full two-order mission with score and win/loss/retry, save and basic original art. Run unit tests for same-tier eligibility, serve priority, duplicate events and same-tick win.

**Third checkpoint**: at least 8 solvable and owner-approved missions, complete map and device QA. The target is 12 if feasible, not 12 fake buttons.

## PR and merge discipline

- Branch name includes CE ticket and short description.
- Engineers do not self-merge; coordinator reviews PRs and communicates merge order. Main branch integrations require owner approval where existing repo practice dictates.
- Code and docs are different deliverables. Do not claim features shipped because specs are merged.
- All **manual UI and gameplay tests** are directed to owner. Engineers may conduct non-UI automation and create exact manual acceptance instructions for the owner.
- Add test seeds, screenshots with real game source, actual browser logs, licence records and measured performance.
- Never commit secrets, account details, prize documentation or unlicensed art.

## Source ownership

The 21 long-term design batches remain unchanged. The contest codebase is **new Base44 app code**, preferably in its own source repository or a carefully isolated source folder with explicit Base44 sync rules. The contest docs live here; do not automatically sync the whole GitHub documentation tree into the Base44 app.

## Handoff messages

Engineer → coordinator:
> CE ticket complete on branch ..., PR ..., automated test summary ..., published Base44 preview ..., unresolved risks ..., owner manual tests required: ...

Coordinator → owner:
> Contested behavior to validate: ...; environment: ...; actions: ...; expected: ...; pass/fail box ...; reviewer will not mark manual QA passed without your result.

## Hard guardrails

NO required login; NO real-money/in-game purchase gating; NO source game asset copying; NO custom-domain-only URL; NO externally hosted game iframe masquerading as Base44; NO unverifiable "official" leaderboard; NO paid/incentivized voting.
