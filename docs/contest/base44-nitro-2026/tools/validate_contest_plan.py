#!/usr/bin/env python3
"""Static validation of contest *documentation fixtures*, not the game or eligibility."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
def load(name):
    return json.loads((ROOT / "examples" / name).read_text(encoding="utf-8"))

plan = load("contest-plan.draft.json")
qa = load("qa-checks.draft.json")
rights = load("rights-inventory.template.json")

assert plan["schemaVersion"] == 1
assert plan["edition"] == qa["edition"] == rights["edition"]
assert plan["status"] == "draft_not_implemented"
assert plan["platform"]["required"] == "Base44"
assert plan["platform"]["publicUrl"] is None, "Draft manifest must not claim a live Base44 URL"
assert plan["platform"]["base44ProjectCreatedAt"] is None
assert plan["content"]["drinkTiers"] == 8
missions = plan["content"]["missions"]
assert len(missions) == 12
assert len({m["id"] for m in missions}) == len(missions)
assert all(m["status"] == "draft" and m["published"] is False for m in missions)
assert all(m["verifiedWinReplay"] is None and m["ownerManualAccepted"] is False for m in missions)
flags = plan["features"]
assert flags["registrationRequired"] is False
assert flags["paymentsEnabled"] is False
assert flags["shopPurchaseFlows"] is False
assert flags["adsEnabled"] is False
assert flags["remoteLeaderboard"] is False
assert flags["trustedWallet"] is False
assert plan["release"]["submissionConfirmation"] is None
assert plan["release"]["ownerAccepted"] is False
assert len({c["id"] for c in qa["checks"]}) == len(qa["checks"])
assert all(c["status"] == "pending" for c in qa["checks"])
assert rights["assets"] == []
print("PASS: draft contest manifest structure and conservative feature gates")
print("NOTE: does NOT certify Base44 compliance, deployed gameplay, rights, or QA")
