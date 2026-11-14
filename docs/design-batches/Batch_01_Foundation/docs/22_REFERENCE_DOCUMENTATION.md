# 22 — Official Docs, Production References and Research Links

**Last checked:** 2026-11-14. Confirm APIs and terms against the version pinned in the actual lockfile. Links are working research starting points, not a statement that every product is installed or licensed.

## Core engine and browser game

- Phaser 4 download / versioned docs: https://phaser.io/download and https://www.phaser.io/oss/docs/phaser/getting-started/installation
- Phaser guides and scenes: https://www.phaser.io/oss/docs/phaser/getting-started/installation and https://phaser.io/oss/docs/
- Phaser repo and examples: https://github.com/phaserjs/phaser and https://phaser.io/learn
- Rapier JavaScript collision/events: https://www.rapier.rs/docs/user_guides/javascript/advanced_collision_detection_js/
- Rapier docs home: https://rapier.rs/docs/
- React: https://react.dev/
- Next.js App Router: https://nextjs.org/docs/app
- Next.js deployment: https://nextjs.org/docs/app/getting-started/deploying
- TypeScript handbook: https://www.typescriptlang.org/docs/handbook/intro.html

## Backend, auth, and data

- Supabase: https://supabase.com/docs
- Supabase RLS: https://supabase.com/docs/guides/database/postgres/row-level-security
- Supabase anonymous auth: https://supabase.com/docs/guides/auth/auth-anonymous
- PostgreSQL: https://www.postgresql.org/docs/
- Fastify: https://fastify.dev/docs/latest/
- Zod: https://zod.dev/
- Redis: https://redis.io/docs/latest/
- BullMQ: https://docs.bullmq.io/
- Cloudflare R2 signed URLs: https://developers.cloudflare.com/r2/api/s3/presigned-urls/

## Asset creation and audio

- FLORA: https://flora.ai/
- Tripo: https://www.tripo3d.ai/
- Meshy: https://www.meshy.ai/
- Blender: https://docs.blender.org/manual/en/latest/
- ImageMagick: https://imagemagick.org/
- TexturePacker: https://www.codeandweb.com/texturepacker
- ElevenLabs: https://elevenlabs.io/
- WeLoveIndies: https://weloveindies.com/
- Howler.js: https://howlerjs.com/
- Web Audio API: https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API
- GSAP: https://gsap.com/docs/v3/
- Rive (optional): https://rive.app/
- Spine (optional): https://esotericsoftware.com/spine-documentation

## Infrastructure, testing and native

- Vercel docs: https://vercel.com/docs
- Capacitor v8: https://capacitorjs.com/docs
- Capacitor requirements: https://capacitorjs.com/docs/getting-started/environment-setup
- Playwright: https://playwright.dev/
- Vitest: https://vitest.dev/
- PostHog: https://posthog.com/docs
- Sentry: https://docs.sentry.io/
- pnpm workspaces: https://pnpm.io/workspaces
- Turborepo: https://turborepo.com/docs
- GitHub Actions: https://docs.github.com/en/actions
- Diversion: https://diversion.dev/

## Product release/compliance references

- Web Content Accessibility Guidelines: https://www.w3.org/WAI/standards-guidelines/wcag/
- Apple App Review Guidelines: https://developer.apple.com/app-store/review/guidelines/
- Google Play policies: https://support.google.com/googleplay/android-developer/topic/9858052
- PWA installability/UX: https://web.dev/learn/pwa/
- Privacy by design: https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/accountability-and-governance/guide-to-accountability-and-governance/accountability-and-governance/data-protection-by-design-and-default/

## Research caveats

- The Phaser version changes; `4.2.1` was displayed on its download page when researched, but pin to tested version.
- Supabase anonymous users are authenticated-role users without recovery credentials until identity linking; do not assume they are durable across devices or after clearing browser storage.
- Capacitor docs indicated Node 22+ for v8 environment at this check; verify requirements when implementing.
- AI asset tools have changing licensing and API scopes; maintain a local rights audit, not just a URL.
- We intentionally do not reproduce the source game's private mechanics; screenshots support only visual/mechanical inference.
