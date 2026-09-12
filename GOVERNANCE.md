# PANOPTES governance model

PANOPTES is the oversight layer of a three-part reference portfolio:

- **ARGUS**: a multi-agent Know Your Customer / Customer Due Diligence review agent reference design (first line: the system doing the work)
- **HERMES**: an adversarial testing and assurance exercise executed against ARGUS (assurance activity: testing the controls)
- **PANOPTES**: the risk register, key risk indicators, framework coverage and escalation views over that evidence (second-line oversight: monitoring and reporting)

Named for Argus Panoptes, the all-seeing watchman.

## Scope, stated plainly

This is a **reference implementation** built as an independent portfolio artifact. It is not employer work and describes no real organisation's incidents, systems or data.

Two data sources, always distinguishable in the interface:

1. **Real evidence.** The 14 adversarial test results from HERMES run `20260903T011051Z`, executed against the ARGUS reference agent. Verdicts, categories, severities and framework mappings are taken directly from the published run artifact. These drive the retest pass rate indicator and the framework coverage matrix.
2. **Synthetic findings.** Eighteen fictional findings scoped to fictional systems (the ARGUS reference deployment, the fictional ORION storefront, the fictional vendor Meridian Analytics). They exist so the register, indicator and escalation views have open, overdue, escalated and closed items to render. Every synthetic record is labelled as such in the data file and the interface.

Zero personally identifiable information in either source.

## Modelled remediation policy

The policy rulebook is modelled, not copied from any employer. Its anchor is a real-world discipline the author has operated: a 40-day service level agreement for application vulnerabilities with a maximum of three rescan cycles. For demonstration, that anchor is extended into severity tiers:

| Severity | Remediation service level agreement |
|---|---|
| Critical | 14 days |
| High | 30 days |
| Medium | 60 days |
| Low | 90 days |

Rescan discipline: a finding may consume at most **three rescan cycles**. A failed third rescan, a breached service level agreement, or an ageing open critical triggers escalation.

Escalation path: **accountable owner, then regional lead, then risk committee.**

## Key risk indicator definitions

All indicators are computed from the data file at render time. None are hard-coded.

1. **Findings closed within service level agreement.** Closed findings whose days-to-close were at or under their severity's agreement, as a percentage of all closed findings. Threshold: green at 90 percent or above, amber at 75 to 89, red below 75.
2. **Open critical findings.** Count of unresolved critical-severity findings. Threshold: green at zero, red otherwise.
3. **Overdue remediation actions.** Open findings past their target date. Threshold: green at zero, red otherwise.
4. **Adversarial retest pass rate.** Passed tests as a percentage of executed tests in the HERMES evidence run. Real data.
5. **Mean days to remediate.** Average days from opened to closed across closed findings. Reported without a threshold; trend matters more than level.

## Use-case inventory and materiality classification

Oversight starts with knowing what is running. Every AI use case is an inventory entry carrying its materiality tier, accountable owner, approval reference, validation state, thresholds and data lineage. One entry (ARGUS) is the real reference artifact; the others are fictional systems that exist to exercise every inventory state, and say so.

Materiality tiers, modelled:

| Tier | Definition | Example |
|---|---|---|
| Tier 1 | Customer-impacting or regulated-domain decisions; errors carry financial-crime, regulatory or customer-harm consequence | ARGUS KYC/CDD review agent |
| Tier 2 | Customer-facing or vendor-supplied capability without direct regulated decisioning | ORION support assistant; Meridian vendor scoring |
| Tier 3 | Internal productivity with mandatory human review of outputs; no customer exposure | HESTIA drafting assistant |

Proportionality is the point of the tiering: tier 3 earns a checklist, not a committee.

## Approval authorities and residual-risk acceptance

Authority follows materiality. The tier decides who approves deployment, who may accept residual risk, and how often independent validation recurs:

| Tier | Deployment approval | Residual-risk acceptance | Independent validation |
|---|---|---|---|
| Tier 1 | AI risk committee | AI risk committee | Before production, annually, and on material change |
| Tier 2 | Regional lead, committee notified | Regional lead | Before production and on material change |
| Tier 3 | Accountable owner | Accountable owner | Owner self-assessment against checklist |

Residual-risk acceptance is a signed, time-bound decision recorded in the exceptions register, never an email thread.

## Independent validation and challenge

First line builds and operates; challenge comes from outside the build. In this reference set, the HERMES adversarial run is the independent challenge evidence for ARGUS: a separately executed test exercise whose verdicts the first line does not author. Modelled second-line design review completes the validation record. Validation currency is an oversight indicator, and an overdue validation (ORION, deliberately) turns it amber.

## Performance and drift thresholds

Each inventory entry carries explicit performance and drift metrics with green, amber and red limits: false-negative tolerance and human-override rate for ARGUS, input-distribution drift and complaint rates for ORION, labelled-sample agreement for the vendor model. Thresholds are declared next to the use case, not discovered after an incident. One amber drift state (ORION input-topic distribution) is authored in so the monitoring visibly works.

## Change control

Model-version upgrades, prompt and guardrail changes each carry an approval reference and a post-change verification record. The change log deliberately shows the control catching its own gaps: CHG-002 shipped a model upgrade without re-running the jailbreak regression suite and raised finding SYN-009; CHG-003 is blocked on the approval-workflow gap raised as SYN-013.

## Exceptions

An exception is a time-bound departure from the control standard with a residual-risk rating, compensating controls, acceptance by the authority the tier matrix names, and a review date the indicators police. An exception without an expiry is an unapproved policy change. One exception (EXC-002) is authored past its review date so the discipline is demonstrated, not asserted.

## Oversight indicator definitions

Computed from the inventory and exceptions sections at render time:

6. **Use cases with current independent validation.** Entries whose validation state is current, out of all inventory entries.
7. **Active exceptions past their review date.** Green at zero, red otherwise.
8. **Thresholds outside green.** Count of performance and drift metrics in amber or red across the inventory.

## Management reporting

The executive report is the artifact the rest of the system exists to produce, and it is the dashboard's landing view. Its discipline, modelled on committee practice:

- **Posture before detail.** An honest overall statement first, including what worsened.
- **Movement, not snapshots.** Every indicator is shown against prior period. The prior period here is authored for demonstration and labelled as such; the current values are recomputed at render time.
- **Decisions, not information.** Each escalated matter arrives as a request with a recommendation: for decision, for approval, for reaffirmation. A committee that is only informed is an audience.
- **Gaps stated.** What the evidence does not cover appears in the report, not only in the methodology page.

The report is print-formatted; printing that tab yields the committee pack.

## Framework coverage method

Each risk category carries the mapping encoded in the HERMES attack library: a MITRE ATLAS technique, an OWASP Top 10 for Large Language Model Applications (2025) entry, and NIST AI Risk Management Framework subcategories. The coverage matrix reports, per category: tests executed, tests passed, and open register findings.

The NIST AI Risk Management Framework function band reports which of GOVERN, MAP, MEASURE and MANAGE the test suite exercises. **MAP is an acknowledged gap**: system-context mapping sits upstream of adversarial testing and is not evidenced by this suite. Reporting what the evidence does not cover is part of the method; an assurance view that only shows green is not an assurance view.

## Limitations

- Synthetic findings are illustrative. Their volumes, dates and closure patterns were authored to exercise every interface state (open, in remediation, closed, overdue, escalated, rescan-exhausted), not to represent any real risk profile.
- The policy tiers beyond the 40-day anchor are demonstration values, not a recommendation.
- Single evidence run: trend views over multiple runs are the natural next iteration, alongside a negative-control run demonstrating that the harness can detect failures.
