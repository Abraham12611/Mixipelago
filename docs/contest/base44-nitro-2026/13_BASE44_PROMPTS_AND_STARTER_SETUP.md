# 13 — Base44 Build Prompts and Technical Kickoff

The following prompts are **templates for a new Base44 project**. They are not proof that Base44 has built an app. Save actual Base44 prompt/edit history and source changes as eligibility evidence.

## Prompt A — Create the original contest project

> Create a **new** public browser game application called **Mixipelago: Coconut Cove — Contest Edition**. The app has an original illustrated tropical 2.5D visual identity. It must be playable immediately by guests, without login, registration, paywall, purchases, ads, external app, download or browser extension. Use a responsive React application shell with routes Home, Play, Coconut Cove Map, Results, Settings and Credits. All screens must have real, accessible navigation. Keep the gameplay component as an in-project canvas integration, not an iframe pointing to another hosted game. Set up a clean project and versioned local guest progress; no backend requirement for core play. Do not copy any existing game's assets or interface.

Check public/private app setting and deployment path; do not assume Base44 default is anonymous. Record project ID/creation timestamp.

## Prompt B — Game shell and controls

> Implement the playable table in the Base44 project with a game board that remains readable on 320px mobile portrait and desktop landscape. Support touch drag/release and desktop pointer aiming, an optional keyboard alternative, pause, retry, next shot preview, two active orders, a danger line and text labels. Use Phaser/Rapier **only if the Base44 project genuinely supports and deploys them**, otherwise a simpler original Canvas-based physics layer with versioned rules. Core simulation is 60Hz fixed step, separate from frame rendering. The UI never directly mutates the physics state except through typed commands.

Test touch pointer capture and custom dependencies in the published Base44 app.

## Prompt C — First playable loop

> Use the canonical eight-tier Mixipelago drink progression: same-tier levels 1–7 merge into the next tier, level 8 is terminal. Distinct tiers bounce/slide. New merge outputs that match an active customer request automatically serve the oldest eligible request and cannot remerge. First tutorial mission displays two scripted orders and ends on two completions. Award score and preview-only nonspendable coins locally; no server wallet or online leaderboard. Include retry, win, loss and recovery states.

The builder's generated implementation **must be reviewed against the reducer tests**; prose instructions alone do not prove correctness.

## Prompt D — Campaign + polish

> Build a small Coconut Cove route map showing only published playable missions, a three-chapter progression with 8–12 real missions, score/stars and local bests. Create results and settings screens, 3–4 original fictional customers, original tropical audio and original drink sprite identities. All interactive features must work; hide draft paths and empty social/shop buttons. Use high contrast, large touch targets, reduced motion and meaningful audio mute.

Avoid claiming 12 levels exist until actual content is authored, verified and enabled.

## Prompt E — QA/final publish

> Make every route public and testable without authentication. Add error/retry handling for unsupported WebGL/wasm, missing asset, browser visibility loss and disabled localStorage. Optimize assets for mobile. Add a Credits screen for licences. Ensure the game is hosted on a Base44 URL, never requiring an external app or hosted iframe. Do not introduce payments, ads or guest-blocking popups. Preserve prompt/edit history and an asset rights manifest.

## Engineering setup notes

- Verify Node and Base44 CLI support against **current official docs at execution**; CLI documentation currently describes Node 20.19+, base44 create/link/deploy and React/Vite starter.
- Do not push all historical repo files into the Base44 project. Only the newly created contest app code should link/deploy.
- Pick an explicit source synchronization direction; two-way Base44/GitHub sync can conflict with simultaneous AI engineer edits.
- The contest app may be stored in a new scoped source folder or a **separate code repository**. This existing GitHub repo's design docs should remain stable and linked as reference, not automatically deployed as the app.
- After every Base44 prompt, examine generated code and run actual browser validation. Never assume Base44 generated the requested physical behavior from text alone.
