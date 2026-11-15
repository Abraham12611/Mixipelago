# 02 — Feature Scope, Priority and Kill Criteria

**Principle:** A finished small game can score better than a wide broken demo. Requirements below do not imply they are implemented.

| Feature | Must (P0) | Should (P1) | Later / excluded |
|---|---|---|---|
| Base44-generated project and URL | Yes; prove new build during window | — | External host-only build |
| Guest Play | Yes | — | Registration required |
| Physics launch + merge | Yes | Trajectory hint after user tests | Tier-changing power physics |
| Eight-tier canonical catalog | Yes | Custom garnish FX | Alternate recipe trees |
| Customer orders | Two visible initial orders | 4 visually distinct customers | Deep loyalty/reputation |
| Coconut Cove campaign | 8–12 proven levels (12 target) | Chapter map animations | Hundreds of missions |
| Controls | Mobile drag, desktop pointer, pause | Keyboard + optional aim guide | Gamepad/mobile wrapper |
| Result + retry | Yes | Stars + local personal best | Ranked global board |
| Art & sound | Original coherent set | Extra polish on merge chains | Complex cutscenes |
| Progress | Local only, explicitly provisional | Export/reset | Server coin wallet |
| Festival moment | — | 1 optional polished challenge | Real-time event service |
| Earned coin display | Preview only, no purchase gate | Decorations as automatically awarded milestones | Paid/real-money store |
| Accessibility | Reduced motion, labels, hit targets, sound opt-out | More granular settings | Exclusive gestures without alternate |
| Media/promotion | Screens, authentic 15–45s gameplay clip | Short loop reel | Vote incentives |

## MVP floor vs release stretch

**Hard floor to submit:** fully playable eight-tier merge loop + 8 tested Classic Service levels + responsive navigation + authored victory/loss/retry + guest save + original art/audio + Base44 URL + compliance evidence. **Target:** 12 levels and polished island map. **Stretch:** single Festival Rush challenge and photo-worthy celebration.

## Kill conditions for scope

1. If Base44 renderer/physics proof-of-concept fails, reduce sophistication or switch to a simpler in-Base44 Canvas implementation **without changing the originality or core loop**.
2. If less than eight missions are solvable and polished, do not publish a misleading 12-node map; hide unpublished nodes and focus QA on eight.
3. If a feature requires auth/payment or third-party services, defer it.
4. If an art/asset cannot be proven owned or licensed, replace it immediately.
5. If feature implementation threatens deadline or performance, keep it disabled and prioritize play loop.
6. Do not invent a global leaderboard backed by untrusted localStorage scores. Show **Local Best** instead.

## Content flags (initial)

All advanced flags default false: GUEST_ONLY=true; CORE_SERVICE=true; MAP=true after mission proof; FESTIVAL_RUSH=false; ONLINE_RANKINGS=false; FRIENDS=false; COMMERCE=false; ACCOUNT_AUTH=false; ADS=false; SERVER_WALLET=false; SHOP_PURCHASES=false; REALTIME=false.

Any enablement needs an explicit ADR, owner approval and corresponding automated + owner manual acceptance.
