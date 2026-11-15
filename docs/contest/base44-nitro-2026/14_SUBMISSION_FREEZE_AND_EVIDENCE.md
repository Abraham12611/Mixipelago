# 14 — Submission, Freeze and Evidence Playbook

## Official process

Per [contest page](https://nitropay.com/base44webgame/) and [terms](https://nitropay.com/base44webgame/terms-and-conditions/): build new game in Base44, publish on a Base44 URL, submit through official form before **2026-12-03 23:59 UTC**, then share and (optionally) enter valid community voting on Base44 Launchpad. Submission is **human-performed**; automated form submissions are prohibited by the terms.

## Before filling the form

- [ ] Entrant meets section 4 eligibility and one-submission restriction.
- [ ] Base44 project created within submission period; project history available.
- [ ] Submitted URL is Base44-hosted, direct, public, and tested without authentication.
- [ ] Can finish the first mission on mobile and desktop without registration/payment.
- [ ] Every published mission has a recorded solution, asset rights and QA sign-off.
- [ ] Original code/art/audio review complete; all source third-party licences fulfilled.
- [ ] Contest title, short description and thumbnail show actual experience.
- [ ] Correct credited contributors and team representative (team size ≤4).
- [ ] Official rules checked for last-minute changes.
- [ ] Owner provides manual approval.

## Form values (fill actual values, never invent)

- Entrant full legal name: **owner enters in secure form**.
- Email: **owner enters**, not committed to GitHub.
- Base44 account: **owner enters**.
- Team names: only confirmed participating eligible team members as required.
- Game title: **Mixipelago: Coconut Cove** (proposal).
- Live URL: **actual published Base44 URL**, not a mock/example.
- Summary: use [20_CONTEST_SUBMISSION_COPY.md](20_CONTEST_SUBMISSION_COPY.md) after confirming shipped features.
- Optional short gameplay video/screenshots: genuine current build, no fabricated states.

## Submission ceremony

1. Release manager pins build commit, Base44 project ID, deployment time and URL.
2. Owner performs manual guest mobile+desktop playtest and records result.
3. Owner submits official form manually and captures screenshot/confirmation ID.
4. Save confirmation and deployed build evidence securely; store a **non-sensitive checklist** in repo issue.
5. Publish Launchpad listing as instructed by platform and verify visibility.
6. Record freeze point as of Dec 3 23:59 UTC. After close, do not materially change until announcement; emergency changes require assessing terms and organizer contact.
7. Schedule availability checks through at least 90 days from **actual winner announcement** (tentatively Mar 10 2027 if Dec 10 announcement).

## Evidence package

- Base44 creation date and editor screenshot.
- Sanitized Base44 edit/prompt history and GitHub commit list.
- Public Base44 deployment link and anonymous browser capture.
- Asset rights manifest, contributors' licence/assignment evidence references.
- Test evidence with browser/device, pass/fail and owner manual signoff.
- Submitted game description, thumbnail, screenshots, video.
- Form confirmation and contact email (keep private where appropriate).

## Freeze/rollback

Always preserve the exact submitted build and assets. If production failure occurs after submission and before cutoff, fix and re-test promptly. During judging, do not push a material redesign. For service-restoring fixes, consult organizer if changes could be material. A Base44 outage does not automatically extend the contest—monitor availability and retain evidence.

## Team ownership conflict

Landing FAQ calls entry 'individual', official terms allow teams up to four with one representative. Apply the official terms, and get organizer clarification if form fields conflict. Do not secretly list an AI agent as a natural-person team member.
