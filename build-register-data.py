#!/usr/bin/env python3
"""PANOPTES data builder.

Merges two sources into register-data.json:
1. REAL: HERMES adversarial test results (run 20260903T011051Z), all executed
   against the ARGUS reference agent. Recorded as assurance_test records.
2. SYNTHETIC: clearly labelled fictional findings against fictional systems,
   so the register, indicator and escalation views have meaningful open,
   overdue and escalated items to render.

Zero personally identifiable information. No employer data.
"""
import json
from datetime import date

TODAY = date(2026, 9, 3)

CATEGORY_MAP = {
    "prompt_injection_direct":   {"atlas": "AML.T0051",     "owasp": "LLM01:2025 Prompt Injection",                    "nist": "MEASURE 2.7 / MANAGE 2.2"},
    "prompt_injection_indirect": {"atlas": "AML.T0051.001", "owasp": "LLM01:2025 Prompt Injection",                    "nist": "MEASURE 2.7 / MANAGE 2.2"},
    "jailbreak":                 {"atlas": "AML.T0054",     "owasp": "LLM01:2025 Prompt Injection",                    "nist": "MEASURE 2.7"},
    "system_prompt_extraction":  {"atlas": "AML.T0056",     "owasp": "LLM07:2025 System Prompt Leakage",               "nist": "MEASURE 2.7 / GOVERN 1.5"},
    "data_leakage":              {"atlas": "AML.T0057",     "owasp": "LLM02:2025 Sensitive Information Disclosure",    "nist": "MEASURE 2.10 / MANAGE 1.3"},
    "excessive_agency":          {"atlas": "AML.T0048",     "owasp": "LLM06:2025 Excessive Agency",                    "nist": "GOVERN 1.7 / MANAGE 2.3"},
}

# Modelled remediation policy (see GOVERNANCE.md): 40-day application
# vulnerability service level agreement and three-rescan discipline as the
# anchor, extended with severity tiers for demonstration.
SLA_DAYS = {"critical": 14, "high": 30, "medium": 60, "low": 90}
MAX_RESCANS = 3

def real_records():
    run = json.load(open("results_20260903T011051Z.json"))
    out = []
    for r in run["results"]:
        m = CATEGORY_MAP[r["category"]]
        out.append({
            "id": f"HERMES-{r['id']}",
            "record_type": "assurance_test",
            "source": f"HERMES run {run['run_id']} (real, executed)",
            "title": r["name"],
            "category": r["category"],
            "severity": r["severity"],
            "system": "ARGUS reference agent",
            "atlas": m["atlas"], "owasp": m["owasp"], "nist": m["nist"],
            "verdict": r["verdict"],
            "status": "verified",
            "owner": "AI assurance lead",
            "treatment": "Control tested under adversarial conditions; pass criteria met.",
            "opened": "2026-09-03", "target": None, "closed": "2026-09-03",
            "rescans": 0, "escalation": "none",
        })
    return out

# ---- Synthetic findings: fictional systems and vendors only. ----
S = lambda i, title, sev, system, cat, opened, status, closed=None, rescans=0, esc="none", treatment="": {
    "id": f"SYN-{i:03d}", "record_type": "finding",
    "source": "Synthetic (fictional, for demonstration)",
    "title": title, "category": cat, "severity": sev, "system": system,
    "atlas": CATEGORY_MAP.get(cat, {}).get("atlas"),
    "owasp": CATEGORY_MAP.get(cat, {}).get("owasp"),
    "nist": CATEGORY_MAP.get(cat, {}).get("nist"),
    "verdict": None, "status": status, "owner": OWNERS[i % len(OWNERS)],
    "treatment": treatment, "opened": opened,
    "target": None, "closed": closed, "rescans": rescans, "escalation": esc,
}
OWNERS = ["Platform engineering lead", "AI assurance lead", "Vendor management lead",
          "Identity and access lead", "Data protection lead", "Application security lead"]

SYNTH = [
    S(1,  "Retrieval index ingests documents without provenance tagging", "high",   "ARGUS reference agent", "data_leakage", "2026-06-14", "closed", closed="2026-07-09", rescans=1, treatment="Provenance metadata enforced at ingestion; retest passed."),
    S(2,  "System prompt stored in world-readable configuration bucket", "critical","ARGUS reference agent", "system_prompt_extraction", "2026-07-02", "closed", closed="2026-07-11", rescans=1, treatment="Bucket policy restricted; secret moved to managed vault."),
    S(3,  "Agent tool schema permits unbounded batch case approval", "critical",    "ARGUS reference agent", "excessive_agency", "2026-08-01", "in_remediation", rescans=1, esc="regional lead", treatment="Per-call approval cap and human gate being added."),
    S(4,  "Customer notes field rendered to model without sanitisation", "high",    "ORION storefront (fictional)", "prompt_injection_indirect", "2026-08-10", "in_remediation", treatment="Input encoding and content-isolation wrapper in build."),
    S(5,  "Model output logs retain raw prompts beyond retention window", "medium", "ORION storefront (fictional)", "data_leakage", "2026-07-20", "in_remediation", treatment="Log retention policy being aligned to data classification."),
    S(6,  "Stale service accounts with production model access", "high",            "ORION storefront (fictional)", "excessive_agency", "2026-06-28", "closed", closed="2026-08-06", rescans=2, treatment="Quarterly access review cycle instituted; accounts de-provisioned."),
    S(7,  "Vendor model endpoint lacks contractual red-team clause", "medium",      "Meridian Analytics (fictional vendor)", "excessive_agency", "2026-07-15", "open", esc="owner", treatment="Contract amendment drafted for renewal cycle."),
    S(8,  "Fine-tuning dataset lineage undocumented", "medium",                     "Meridian Analytics (fictional vendor)", "data_leakage", "2026-08-18", "open", treatment="Dataset card and lineage record requested from vendor."),
    S(9,  "Jailbreak regression suite not run on model version upgrade", "high",    "ARGUS reference agent", "jailbreak", "2026-08-22", "open", treatment="Regression gate being added to release checklist."),
    S(10, "Guardrail bypass via translated instruction payloads", "high",           "ORION storefront (fictional)", "jailbreak", "2026-07-05", "closed", closed="2026-08-02", rescans=1, treatment="Language-agnostic policy classifier deployed; retest passed."),
    S(11, "Agent can amend audit ledger entries post-write", "critical",            "ARGUS reference agent", "excessive_agency", "2026-05-30", "closed", closed="2026-06-12", rescans=1, treatment="Ledger made append-only with hash chaining; retest passed."),
    S(12, "Third-party plugin requests scopes beyond declared purpose", "high",     "Meridian Analytics (fictional vendor)", "excessive_agency", "2026-08-05", "in_remediation", esc="regional lead", treatment="Scope reduction agreed; awaiting vendor release."),
    S(13, "Prompt template repository lacks change approval workflow", "medium",    "ARGUS reference agent", "prompt_injection_direct", "2026-08-25", "open", treatment="Pull-request review gate being configured."),
    S(14, "Sensitive test data used in evaluation prompts", "critical",             "ORION storefront (fictional)", "data_leakage", "2026-07-28", "in_remediation", rescans=2, esc="risk committee", treatment="Synthetic evaluation corpus being substituted; two rescans failed on residual samples."),
    S(15, "No rollback runbook for agent policy configuration", "low",              "ARGUS reference agent", "excessive_agency", "2026-06-20", "closed", closed="2026-08-14", treatment="Runbook authored and tabletop-tested."),
    S(16, "Uploaded document parser executes embedded macros", "critical",          "ORION storefront (fictional)", "prompt_injection_indirect", "2026-08-15", "in_remediation", rescans=1, esc="regional lead", treatment="Macro stripping at ingestion; retest scheduled."),
    S(17, "Model card missing intended-use and limitation statements", "low",       "Meridian Analytics (fictional vendor)", "data_leakage", "2026-07-10", "open", treatment="Documentation requested; low risk, tracked to next review."),
    S(18, "Agent responds to authority claims made in conversation", "high",        "ORION storefront (fictional)", "prompt_injection_direct", "2026-08-28", "open", treatment="Authority-claim refusal control being ported from ARGUS."),
]

def finalize(records):
    for r in records:
        if r["record_type"] == "finding":
            opened = date.fromisoformat(r["opened"])
            sla = SLA_DAYS[r["severity"]]
            target = date.fromordinal(opened.toordinal() + sla)
            r["target"] = target.isoformat()
            r["sla_days"] = sla
            if r["closed"]:
                closed = date.fromisoformat(r["closed"])
                r["days_to_close"] = (closed - opened).days
                r["within_sla"] = r["days_to_close"] <= sla
                r["days_overdue"] = 0
            else:
                r["days_to_close"] = None
                r["days_overdue"] = max(0, (TODAY - target).days)
                r["within_sla"] = r["days_overdue"] == 0
    return records

data = {
    "generated": TODAY.isoformat(),
    "scope": "Reference implementation. Real evidence: HERMES adversarial run 20260903T011051Z against the ARGUS reference agent (14 tests). All findings marked synthetic are fictional and scoped to fictional systems. Zero personally identifiable information. Independent portfolio artifact; not employer work.",
    "policy": {"sla_days": SLA_DAYS, "max_rescans": MAX_RESCANS,
               "anchor": "Modelled on a 40-day application-vulnerability service level agreement with a maximum of three rescan cycles, extended with severity tiers for demonstration.",
               "escalation_path": ["owner", "regional lead", "risk committee"]},
    "records": finalize(real_records() + SYNTH),
}
json.dump(data, open("register-data.json", "w"), indent=1)
print(f"{len(data['records'])} records written")
