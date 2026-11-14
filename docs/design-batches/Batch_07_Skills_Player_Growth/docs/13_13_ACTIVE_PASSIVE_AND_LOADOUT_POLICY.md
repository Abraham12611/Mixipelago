# 13 — Active Skills, Passive Skills and Loadout Constraints

**Batch 7 design status:** proposed · Not shipped · Interfaces and tuning subject to owner approval.

## Types
- **Passive:** server-validated effect from purchased ranks when source is eligible in the current activity. Shop/customer economy effects are server-consumed; UI display effects are client-rendered from trusted entitlement.
- **Active:** explicit player invocation with cooldown/resource rule (e.g., later hint pulse), governed by mode permissions; no alpha active skills.
- **Cosmetic:** visual title, theme or celebration style only. Do not encode gameplay effect under a cosmetic tag.
- **Knowledge aid:** optional information projection with accessibility-reviewed baseline.

## Loadout proposal
From the later active-skill rollout onward, each player can equip **up to three active slots** in casual mode, with no duplicated active ID. Passive skills are automatically applied from invested ranks unless disabled by context. Unowned, unpublished or mode-disallowed skills cannot be equipped. A disallowed equipped skill is temporarily *suspended*, never automatically sold or refunded.

## Active execution
Client sends `{skillId, loadoutRevision, sessionId, clientRequestId}`. Server or a validated local session rule checks mode, cooldown, charges, session state and entitlement; returns `APPLIED`, `COOLDOWN`, `DISALLOWED_MODE`, or `STALE_LOADOUT`. In standardized ranked sessions the allowed active list is fixed; effects are versioned into replay proof.

## Scope
Shop-aiding passives apply only to a designated owned shop; board-UI passives apply to local casual sessions; world-map passives apply to authorized discovery info. Never let a generic `getModifiers` service return secrets for unauthorized shops or campaign nodes.
