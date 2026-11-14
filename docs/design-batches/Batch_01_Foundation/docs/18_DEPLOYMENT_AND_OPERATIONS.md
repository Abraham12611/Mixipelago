# 18 — Environments, Deployment, CI/CD and Operations

## Environment architecture

- `local`: developer laptop/VM; hot reload, fixture content, physics lab.
- `preview`: per-PR Vercel deployments; local/non-authoritative save only in early alpha, seeded demo data later.
- `staging`: stable release candidate, production-like integrations, separate test credentials.
- `production`: public website, protected backend data and approved content.

No development or staging systems share a production database by accident. Never use production keys in PR preview builds. Feature flags are environment-scoped.

## Deployment providers

`apps/web`: Next.js on Vercel, WebGL game loaded only on client. Static art/audio on CDN (local `/public` for alpha; Cloudflare R2 + CDN as assets grow). Future `apps/api`: persistent runtime with Fastify, dedicated process/container if background processing needed. Database/auth: Supabase. Redis + worker optional after events/leaderboards scale.

Native wrappers: Capacitor after web proof; use supported native project packaging, no direct assumption that server-rendered routes work offline in wrapper without design. Keep actual playable game assets packaged/cached properly.

## `.env.example` (illustrative names)

```bash
# client-safe, public (values are not secrets)
NEXT_PUBLIC_APP_ENV=local
NEXT_PUBLIC_GAME_BUILD=v0.1.0
NEXT_PUBLIC_FEATURE_MAP=false
NEXT_PUBLIC_FEATURE_SHOP=false
NEXT_PUBLIC_CONTENT_MANIFEST_URL=/content/manifest.json
# only when backend integration is enabled:
NEXT_PUBLIC_SUPABASE_URL=
NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY=

# server-only: never expose to client
SUPABASE_SERVICE_ROLE_KEY=
DATABASE_URL=
R2_ACCESS_KEY_ID=
R2_SECRET_ACCESS_KEY=
R2_BUCKET=
REDIS_URL=
ERROR_TRACKING_AUTH_TOKEN=
```

Security: use per-env credentials, least privilege and secret manager. The client-safe publishable key is not a substitute for RLS.

## CI workflow

For each PR:

1. `pnpm install --frozen-lockfile`.
2. Typecheck every affected package, ESLint/Prettier.
3. `vitest` unit/physics/content contract tests.
4. Build `apps/web` production mode; ensure no Phaser SSR import errors.
5. Run basic Playwright desktop smoke and mobile viewport interaction tests.
6. Generate bundle/asset size report; fail on severe regression (budget thresholds tuned).
7. Optional preview deployment with demo environment, attach link in PR.

For `develop`: integration tests and staging deploy after approved merges. For `main`: protected release workflow with explicit owner approval, tag, smoke, monitor and rollback capacity.

## Startup and runtime health

Web health: route responds, static manifest present, WASM loads, canvas can initialize and session start. Backend health when introduced: DB connectivity, migration version, queue lag, event publisher status. Monitoring: JS errors, blank canvas crashes, asset 404, slow loading, WebGL context loss, session abandonment, latency.

## Asset publishing

All production assets use immutable content-hashed names. Manifest is versioned; publish assets first, then manifest, then application version. Maintain previous manifest/assets for rollback while active sessions exist. CORS and CSP rules explicitly allow valid CDN. Prefer private source art bucket and public optimized output bucket, with time-limited signed URLs for secure uploads.

## Save and release migrations

Local save migrations are pure, tested and idempotent; versioned storage key or upgrade path. Once Postgres is live, schema migrations run before frontend features depending on them, use backward-compatible expand/contract migrations and staged feature flags. No destructive changes until old clients are no longer supported.

## Incident response

Severity P0 = cannot play, data loss, wallet exploit; disable feature/rollback immediately with owner notification. Severity P1 = widespread crashes/performance regression; rollback or rapid patch. Severity P2 = cosmetic isolated problems; patch release. Preserve logs and regression repro. Create blameless incident record and add tests.

## Release notes template

```
Version: v0.x.y
Date:
Highlights:
Fixes:
Gameplay balance changes:
Data/save migrations:
Known limitations:
Feature flags:
Manual owner QA evidence:
Rollback version:
```

## Future operational concerns

Ranked worker backlogs, delayed prize grants, idempotent event workers, missing-region leaderboards, account deletion, moderation reports, mobile store review, privacy policy updates, staged rollout.
