# 15 — VIP Guests, Premium Encounters and Transparent Risk

**Batch 9 status:** proposal · Not deployed · Cross-batch compatibility required.

## Design intent
VIP means a **fictional high-stakes customer role**, not targeting real-life wealthy players. VIP encounters can bring a larger *authored* payout and more complex targets, but the reward/difficulty proposition must be displayed before acceptance. Do not grant prestige or actual cash claims simply because a customer sprite is golden.

## Eligibility and probability
Use Batch 7's staged class probability: `vipProbability=clamp(baseVipProbability + shopModifierPp + skillModifierPp + eventModifierPp, 0, publishedCap)` where candidate cap is **0.20**. All terms are integer basis points; base and bonuses are from signed published config. In tutorial/fixed missions and standardized ranked challenges, customer composition remains fixed; no VIP roll at all.

## VIP order contract
`vipContractId`, `encounterId`, `missionId`, required tier/recipe, quantity, optional active-tick deadline, known reward policy, refusal behavior. Joining a VIP challenge is optional; declining must not create a financial penalty or block unrelated campaign progression. An eligible VIP order is still served by the canonical Batch 3 order matcher once it is active.

## Server integrity
Reserve encounter outcome before showing a claimable choice; refresh cannot reroll a premium encounter. Customer challenges must use a verified run receipt before Batch 6 ledger payout. Enforce per-day and per-encounter reward budgets, not infinite repeat farming. In case of outage after mission verification, recover the same reward receipt.

## Visibility and QA
UI marks reward, requirements, time limit, and any penalties in plain language. Test identical seeds, inactive VIP pool, cap at 0.20, no rerolls, no VIP in normalized ranked, and no impossible recipe requirements. The VIP system is explicitly **off** in the alpha and first customer/reputation release.
