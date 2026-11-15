# 00 — Rules, Eligibility & Compliance Matrix

**Primary authority:** [Official Terms](https://nitropay.com/base44webgame/terms-and-conditions/), particularly sections 3–8, 11, 13 and 18. The terms supersede contest-page FAQ wording when they conflict. Reviewed 2026-11-15; sponsor may change terms.

## Must-pass eligibility gates

| Gate | Rule from official terms / contest page | Evidence required | Owner |
|---|---|---|---|
| Entrant | Age 18+, lawful participation, good-standing Base44 account; sanctions and jurisdiction restrictions apply | Entrant confirms eligibility privately; never put ID docs in repo | Entrant |
| Team | Up to four eligible natural persons; one designated representative | Contributor/rights roster; named entrants only as required in form | Entrant |
| New build | Built **during Nov 5–Dec 3, 2026** using Base44; no pre-existing project/republication/reskin or substantially copied game | Base44 creation timestamp, prompt/edit history, source commits, originality ledger | Build lead |
| Hosting | Public stable **Base44 URL**, not custom-domain-only | URL + incognito video and network test | Release lead |
| Full access | No mandatory login, registration, download, install, extension, payment, purchase or paywall | End-to-end unauthenticated playthrough | QA/owner |
| Originality | No unlicensed third-party art/audio/game assets, logos, character likenesses | Per-asset rights record and approvals | Art lead |
| Availability | Live without disallowed material change through judging and 90 days after actual announcement | Uptime plan, frozen release SHA and archive | Release lead |
| One entry | One submission per entrant or team; bots/automated submissions disallowed | Human submission and confirmation record | Entrant |
| Content standard | No illegal/hateful/sexual/harmful or under-13 directed collection; no gambling for value | Content review | Owner |
| Vote integrity | No bots, purchased votes, vote exchanges, incentives, fake accounts | Community outreach logs and rules | Marketing owner |

## Exact calendar

- **2026-11-05 00:00 UTC:** submission opens.
- **2026-12-03 23:59 UTC:** submission and community voting close. This is the hard deadline.
- **2026-12-04 through 2026-12-09:** judging period (subject to official changes).
- **On/about 2026-12-10:** winner announcement.
- **90 days after actual announcement:** minimum public availability. If announcement is Dec 10, tentative date is Mar 10, 2027; calculate again from actual date.
- Per section 6.3, entries can be updated until the submission window closes; **no material changes after close before winner announcement**. Avoid unnecessary changes between submission and cutoff; capture approved final version.

## Critical ambiguity to resolve before major investment

The official terms require a game **built using the Base44 platform**, and permit requesting project creation/edit history. Base44 offers a CLI and sync, but this does **not prove** that an externally coded Phaser/Rapier app linked to Base44 qualifies. Create the new app within Base44 during the period. Implement meaningful game logic/screens in that project and preserve that history. Ask [base44xnitro@overwolf.com](mailto:base44xnitro@overwolf.com) whether the intended CLI/custom-renderer integration is acceptable. Record reply verbatim in a private issue or secure record. **Do not assert compliance before organizer confirmation or substantive Base44 build evidence.**

## Other important terms

- Section 5: the official page/form may request name, email, Base44 account, URL, description, and team names. Submit **manually**; do not use scripts to submit.
- Section 8: judges weigh gameplay, creativity, execution equally. Community shortlist is top 25 eligible valid-upvote entries; the Community Panel chooses winners among shortlist.
- Section 11: entrants retain IP but grant substantial promotion/hosting licences. Secure contributor assignments/licences in writing.
- Ad monetization with Nitro is **not** a required part of entry; no ad gate or monetized requirement in the contest build.
- Do not publish sensitive proof of residence, tax data, government IDs, accounts, or secrets in GitHub.
- If conflict persists between landing page and official terms, rely on **terms** and ask organizer rather than inventing an exception.

## Signoff worksheet

- [ ] Entrant/legal/team eligibility confirmed by entrant (private).
- [ ] New Base44 creation date and history captured.
- [ ] Platform integration acceptability clarified if using external toolchain.
- [ ] One game, stable Base44 URL, public guest test.
- [ ] Rights inventory complete; no prohibited source assets.
- [ ] No paywall/account/paid advantage.
- [ ] User-run manual desktop and mobile playtests.
- [ ] Submission evidence and screenshots saved securely.
- [ ] Deadline and freeze timer configured.
- [ ] Availability/rollback owner assigned through post-award period.
