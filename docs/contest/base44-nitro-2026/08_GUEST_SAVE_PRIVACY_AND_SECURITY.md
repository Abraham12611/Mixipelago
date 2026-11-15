# 08 — Guest Save, Local Data, Privacy and Security

## Data ownership

Contest build uses **guest-only progression** so anyone can play without account, registration or mandatory network API beyond delivering the Base44 app. Local progress is a convenience, **not** a trusted result or redeemable balance. Never convert it into server coins, XP or ranked rewards.

## Versioned save format

~~~ts
type GuestSaveV1 = {
  schemaVersion: 1;
  gameEdition: 'base44-contest-2026';
  contentVersion: string;
  updatedAt: string;
  completedMissionIds: string[];
  bestResults: Record<string,{stars:number;score:number;shots:number;scoreProfileId:string}>;
  settings:{music:number;sfx:number;reducedMotion:boolean};
  lastMissionId?: string;
};
~~~

Store under a namespaced key such as **mixipelago:contest:save:v1**; do not share the original 21-batch production save namespace. New edition should not import or silently overwrite other project data.

## Persistence behavior

- Load only if schema version recognized and checksum/data type validation passes.
- Corrupt or stale save: explain recovery; let guest start fresh; optionally export raw JSON for diagnostics; never crash/softlock.
- Mission result writes should be atomic as feasible: write to temporary key, verify parse, then replace stable key; ignore duplicate result IDs.
- Best stars and best score are monotonic **within the same versioned score profile**; a replay loss never erases prior best.
- Player can reset progress explicitly with confirmation; preserve settings unless user chooses full erase.
- localStorage may be unavailable in privacy modes; play should continue with ephemeral in-memory progress, with a clear warning.
- Switching devices does not sync; be transparent. Do not promise cloud persistence.

## Privacy defaults

- No user account, email, user-generated profile, device fingerprint, geolocation or contacts collection for gameplay.
- Avoid third-party analytics on the submitted version unless explicitly evaluated for privacy and contest standards. Prefer aggregate, nonidentifying telemetry if essential.
- No camera, microphone or GPS permission prompts.
- No ads or paid attribution tracking.
- No hidden tracking scripts, deceptive redirects, cryptomining or unnecessary outbound integrations.

## Client security constraints

- Treat mission JSON and URL params as untrusted; validate bounded values and recognized IDs.
- Escape/encode any dynamic text; do not inject raw HTML from URL or untrusted content.
- Limit asset URL origins and iframe embedding; if CSP is supported, use least-privilege policy compatible with Base44.
- Only publish public frontend environment values; never embed Base44 admin token or API secrets.
- No leaderboard with client-submitted authoritative scores. If public scores become a requirement, it is a new backend/security workstream requiring verified sessions and separate owner acceptance.

## Offline and fallback

Core site must load from public Base44 URL. Once loaded, a brief network outage should not crash the active stage if assets are cached; offline restart is best effort, not a contest requirement. Provide explicit retry when assets fail.
