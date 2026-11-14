# 06 — Tech Stack, Runtime Architecture, Module Boundaries

## Decision summary

Browser-first TypeScript monorepo. **Phaser 4** for the real-time game scene, **Rapier 2D WASM** for low-friction contacts, **React/Next.js** for app UI and routes, **Supabase Auth/PostgreSQL** for later trusted persistence, **Fastify** as optional dedicated API service when server-owned transactions launch, **Cloudflare R2/CDN** for large assets, **Redis/worker** when rankings and scheduled events demand it. **Capacitor** for later native wrappers. Verify actual package APIs against lockfile and official docs before use.

### Immediate v0.1.0 dependencies

`typescript`, `next`, `react`, `react-dom`, `phaser`, `@dimforge/rapier2d-compat`, `zod` (content/save validation), test runner `vitest`, `playwright` for browser smoke; Tailwind optionally. Use a game/audio adapter abstraction; Howler can be adopted if it improves multi-sound management. Avoid Redis, queue, full auth and multi-service deployment on day 1.

### Later dependencies (feature gates)

Supabase client, PostgreSQL migrations, Fastify API, R2 asset tooling, job workers, Redis, server replay verification, PostHog, Sentry, Capacitor. No external dependency should be deployed just to satisfy a long-term diagram.

## Architecture layers

```
Browser:
  Next.js UI shell (React)
      ↕ typed UI-game adapter
  Phaser renderer + input + camera + particles + audio
      ↕ typed commands / events
  TypeScript SimulationCore + Rapier WASM
      ↕ typed events
  SessionReducer / Orders / Score / MissionEvaluator
      ↕ local persistence gateway OR authenticated API client
Backend (later):
  Fastify command gateway → Domain services → PostgreSQL transactions
                                     ↘ Outbox/jobs → Redis rankings/event worker
Static assets:
  CDN / R2 → content manifests, sprites, audio, video
```

Never let a React re-render become the physics update loop. Mount game canvas once in a client component. In Next.js, prevent Phaser import during SSR by dynamically loading a client-only host component and cleaning up listeners, Phaser Game, audio, and Rapier on unmount.

## Monorepo target structure

```
apps/
  web/                 # Next.js shell, views, component navigation
  api/                 # Fastify later, no need on first alpha day
  admin/               # Internal content dashboard later
  mobile/              # Capacitor later
packages/
  game-core/           # pure TS session state, commands, scoring, merge decisions
  physics-rapier/      # simulation adapters, collider creation, stepping
  game-renderer/       # Phaser scenes, sprites, camera, FX, input
  game-ui/             # React components, tokens, responsive shell
  content-schema/      # Zod + JSON schema + content manifest versions
  domain-contracts/    # events, IDs, statuses, commands, data types
  save-local/          # versioned local persistence
  services/            # clients/repositories, auth/ledger future
  audio/               # SFX/music contracts & runtime director
content/
  missions/ drinks/ customers/ islands/ audio-manifests/
assets/
  src/ processed/ atlases/ manifests/
tests/
  unit/ physics/ contract/ e2e/ performance/
tools/
  physics-lab/ content-validator/ atlas-builder/
```

Keep *one* source of truth for contracts and JSON schemas; app and server import package versions, no copy-paste types.

## Rendering and physics integration

Phaser owns display scene and scaled camera. Rapier owns world pose and contacts. An adapter maps rigid body ID to sprite ID, updates transformations every render tick, and sends collision data to a pure rules layer. Avoid enabling two simultaneous physics engines on the same objects. Phaser Arcade/Matter are not used on the drink bodies if Rapier is chosen.

Shader effects should degrade gracefully; the primary art pipeline uses 2D sprites drawn from consistent 2.5D renders. No full-scene WebGPU dependency in the first release. All needed visual components must work over WebGL. Include canvas/context-loss recovery path.

## Data ownership & trust boundary

| Data | Owner in v0.1.0 | Long-term trusted owner |
|---|---|---|
| Body coordinates/contact state | Browser physics runtime | Browser runtime; server verification for ranked |
| Aim, shot input, seed | Local session | Local + validated session record |
| Current score | Session reducer/local | Validated score service |
| Preview coins | Local save (explicitly untrusted) | Server wallet + ledger |
| Real shop inventory | Not active | Server economy service |
| Player identity | Local ephemeral ID | Supabase Auth user ID |
| Campaign completion | Local demo | Server progression service |
| Leaderboard rankings | Not active | Server ranking service |
| Art/audio | Local static/CDN | Versioned asset manifests/CDN |

## Dependency management and compatibility

- Use pnpm workspace and Turborepo (optional on day 1; add as needed).
- Pin major/minor dependency versions in `pnpm-lock.yaml`, avoid unreviewed mass upgrades.
- Minimum toolchain: current supported Node LTS suitable for Next + Capacitor; Capacitor v8 docs require Node 22+ at time of drafting (see `22`).
- Use ESLint + Prettier, TS `strict`, no `any` in public contracts.
- Use Zod for data boundaries, and tests to keep content schema backward compatible.
- Do not share server secrets via `NEXT_PUBLIC_*` environment variables.

## API architecture (post-alpha)

When an authoritative economy is introduced, use command endpoints rather than accepting arbitrary wallet balances. Example `POST /v1/shop-upgrades/purchase` with upgrade ID and `Idempotency-Key`; server derives cost, checks user/shop ownership and balance and commits atomically. Read models can be cached. See `07`, `08`.

## Feature flag strategy

`FEATURE_ISLAND_MAP`, `FEATURE_PERSISTENT_ACCOUNT`, `FEATURE_SHOP_ECONOMY`, `FEATURE_SKILLS`, `FEATURE_LEADERBOARDS`, `FEATURE_DYNAMIC_EVENTS`, `FEATURE_CREWS`, `FEATURE_RANKED`, `FEATURE_NATIVE_WRAPPER`. Default all future systems OFF until corresponding acceptance gates pass. Client-visible flags are display gates; server still enforces authorization and rules.

## Deployment separation

- `apps/web` → Vercel with CDN/static assets where possible.
- Auth/DB → Supabase when enabled.
- Long-running workers / Fastify API → dedicated container/runtime (do **not** deploy a permanent game loop on serverless functions).
- Artwork/audio → R2 and CDN, immutable hashed filenames.
- Preview environment on every PR; staging before production.

## Security / performance / accessibility

RLS on exposed tables, server-only economy writes, rate limiting, secret rotation; pooled sprites and audio voices; dynamic render resolution; preloading per mission; reduced motion/mute; keyboard input; no PII or precise location for alpha. Details: `14`, `15`, `25`.

## Architecture fitness tests

1. Can we change rendering without changing score logic? Yes if events/adapter isolated.
2. Can we run game offline? Alpha yes; trusted economy deferred until network.
3. Can we add an island via JSON and assets without changing engine code? Target yes.
4. Can we invalidate score claims made by untrusted clients? Future server must do so.
5. Can we deploy one new mission without repackaging the entire native app? Yes via versioned content manifests with suitable platform policy review.
6. Can we cap memory and device quality? Yes via manifest, asset lifecycle, and quality profile.
