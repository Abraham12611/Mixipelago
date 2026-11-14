# 22 — Normalized Competition, Skills and Leaderboard Integrity

**Batch 7 design status:** proposed · Not shipped · Interfaces and tuning subject to owner approval.

## Competitive policy
Ranked, tournament and standardized friend challenges use a **versioned canonical `competitiveProfile`** containing fixed skill effects, assistance policy, booster allowances, shop benefits and RNG seed policy. Personal shop upgrades, purchased points and temporary buffs are not imported into a competitive result.

## Session admission
1. Client requests a ranked run; server returns `missionVersion`, `rulesVersion`, `competitiveProfileVersion`, `physicsVersion`, seed, allowed assists and allowed active skills.
2. Client acknowledges and locks settings for the session.
3. Score validation uses pinned versions and, for high-stakes modes, replay or server-authoritative proof as defined by Batch 4 and later Batch 19.
4. If a personal skill becomes newly unlocked mid-run, it remains irrelevant until a future nonranked session.

## Scoreboard submissions
`competitiveProfileHash` is part of the proof; absent/stale/mismatched hash rejects entry or routes it to unranked practice. Never recalculate a competitive score by subtracting personal bonuses after play. The server must know **before** the run which assists were available.

## Transparency
UI displays `Standardized rules apply — your shop and skill bonuses are suspended for this event`. A competitive profile is accessible for preview before entering, including accessibility accommodations. Accessibility aids should be evaluated for fair and inclusive standardization, not arbitrarily removed.

## Abuse scenarios
Manipulated assist flags, forged skill points, cross-account buffs, a fake VIP shop state, time-of-check/time-of-use rank changes, replay substitution and resurrected deprecated catalogs must fail tests.
