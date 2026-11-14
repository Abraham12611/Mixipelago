# 95 — Official Technical References and Source Precedence

**Research checked:** 2026-11-14. Vendor policy and software APIs change. Source links do not imply this game is certified, approved or deployed.

- [Apple App Store Review Guidelines](https://developer.apple.com/app-store/review/guidelines/) — External official guide, verify latest version and feature applicability before implementation.
- [Google Play Billing overview](https://developer.android.com/google/play/billing) — External official guide, verify latest version and feature applicability before implementation.
- [Apple privacy disclosures](https://developer.apple.com/app-store/user-privacy-and-data-use/) — External official guide, verify latest version and feature applicability before implementation.
- [Google Play User Data policy](https://support.google.com/googleplay/android-developer/answer/10144311) — External official guide, verify latest version and feature applicability before implementation.

## Internal source-of-truth precedence

1. User-approved product decisions and active ADRs.
2. Existing Batches 1–15 authoritative domain contracts for physics, orders, wallets, XP, ranks and privacy.
3. This batch's explicitly owned design/technical surfaces.
4. Sample catalogs and templates, all intentionally draft and not deployed.
5. External SDK and platform docs at implementation/submission time, with actual versions pinned.

If a current Apple/Google policy, security standard or third-party license conflicts with a proposed sample, follow current applicable law/platform policy and record the resulting design ADR. Do not silently mutate previously completed score and financial records.
