# 23 — Engineer Onboarding and Day-1 Workflow

## Who this is for

Engineers/agents building the initial Mixipelago alpha under coordinator-led integration. No code repository has been created by this documentation pack; the commands below describe the **target setup once the repository is initialized**.

## Prerequisites

Node 22 LTS+ (check installed packages' current engine constraints), pnpm, Git, modern browser and devtools, a mobile device or device-lab access, optional Blender for asset producers. Credentials to preview deployment and future backend granted via secrets manager, not pasted into PRs.

## Bootstrap target

```bash
# after cloning the actual repo
corepack enable
pnpm install --frozen-lockfile
pnpm lint
pnpm typecheck
pnpm test
pnpm dev
```

Expected local app: `http://localhost:3000` (subject to final project scripts). CLI targets to implement: `pnpm dev`, `pnpm build`, `pnpm test`, `pnpm test:physics`, `pnpm test:e2e`, `pnpm content:validate`, `pnpm physics:lab`, `pnpm assets:check`.

## First five actions for a new engineer

1. Read `00`, `01`, `02`, plus the specific owned spec (`04`, `05`, `03` etc.).
2. Read `21` for approved/open decisions and `28` for shared contracts.
3. Pull latest `develop`, install packages, execute existing tests/build.
4. Claim exactly one issue, check package/file owner and dependencies, open issue-linked branch.
5. Implement code + tests, open PR to `develop`, and leave manual UI checks for owner.

## Team etiquette and permissions

- **Do not merge your own PR.** The coordinator reviews and merges into `develop`.
- **Do not merge to `main` without explicit owner approval.** Coordinator executes production release.
- Never silently invent features not in current version scope; propose an issue or ADR.
- Keep small PRs with reproducible behavior and screenshots if available.
- Manual UI tests are directed to user; attach clear instructions and expected results.
- Put important engineer-to-coordinator messages in PR or issue comments for traceability.

## Pull-request checklist

- Linked issue + scope.
- Files modified align with ownership.
- Shared contracts unchanged OR coordinated and migration documented.
- Tests added/updated; `pnpm build` and `pnpm test` pass.
- No hardcoded secrets, third-party copyrighted assets, fake backend success.
- Mobile and desktop changes explained.
- Audio rights/provenance recorded for new assets.
- Manual test steps prepared for owner.
- Flag/rollback details and migration notes included.

## Debugging pathways

- Blank canvas → confirm Phaser only loaded client-side, WASM file load, renderer context errors and asset manifest.
- Glasses fall or accelerate strangely → verify gravity zero, timestep fixed, one physics world, unit consistency.
- Double merge → check collider handle mapping, active/merging status, duplicate events, removal timing.
- Touch aims incorrectly → camera transforms, CSS scaling offsets, DPR, pointer cancel.
- Huge bundle → avoid importing entire heavy asset catalog in first chunk; lazy-load scenes.
- Audio silent on phone → user gesture unlock, sound bus state, browser tab pause.
- Save broken → content/save schema mismatch, migration/fallback logic.

## Exit criterion for engineer handoff

New contributor can reproduce at least one test scenario, explain how an event reaches the UI, and open a PR that doesn't require touching unrelated modules.
