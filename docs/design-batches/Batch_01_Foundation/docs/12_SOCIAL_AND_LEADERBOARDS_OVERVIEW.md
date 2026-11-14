# 12 — Leaderboards, Friends, Crews and Competitive Play (Overview)

**Status:** Design overview only, to be specified thoroughly before v0.5.0. Nothing here implies the first alpha has real verified rankings.

## Proposed scopes

Global; country; region; optionally city/local; friends; and crew competition. Location-based boards must be opt-in, use coarse voluntarily chosen region, provide privacy controls, and avoid exposing precise addresses or inferring actual location from the client.

## Ranking categories

- Best score in standardized mission challenge (skill-first).
- Seasonal tournament score.
- Campaign mission/mastery progress (separate from skill rankings).
- Shop prestige/business achievements (separate leaderboard).
- Crew contribution/completion (later).

Avoid a single universal metric that rewards time spent or purchased boosters over actual skill.

## Architecture

Auth → validated session submission → verification pipeline → persisted score → ranking materialization/cache (Redis sorted sets or SQL for smaller population) → leaderboard API → UI. Season scheduler freezes rankings and distributes rewards through idempotent `reward_grants`/wallet ledger. Historical seasons remain queryable.

## Anti-cheat requirements

Browser scores are untrusted. Record mission seed, content hash, physics/rule versions and player input sequence; verify with a hardened replay algorithm or server-authoritative gameplay when competition matters. Fixed seed/identical equipment for ranked brackets; match-level progression perks disabled or standardized. Cross-platform deterministic physics requires proof, not assumption.

## Rewards philosophy

Favor titles, profile frames, podium decorations, shop cosmetics, limited but capped coin bonuses, unique island monuments and collectible badges. Do not promise cash prizes or real-money winnings without separate legal review.

## Friend/crew UX

Invite/accept/block/report, friends leaderboard, friendly challenge links, optional crew creation, task contributions, cooperative island projects. Moderation tools and abuse/rate limits from day one of social feature launch.

## Rollout order

v0.5.0 verified single global weekly score challenge → country/region filtering → friend challenges → season rewards → crews → optional live head-to-head. Each unlock is behind a server flag, with abuse monitoring.

## Later detail batch must cover

Ranking tie-break rules, privacy and anti-cheat, season clocks/time zones, leaderboard sharding/retention, reward schedules, tournaments, matchmaking, blocking/reporting, crew governance, fraud playbooks.
