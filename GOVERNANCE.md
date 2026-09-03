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

## Framework coverage method

Each risk category carries the mapping encoded in the HERMES attack library: a MITRE ATLAS technique, an OWASP Top 10 for Large Language Model Applications (2025) entry, and NIST AI Risk Management Framework subcategories. The coverage matrix reports, per category: tests executed, tests passed, and open register findings.

The NIST AI Risk Management Framework function band reports which of GOVERN, MAP, MEASURE and MANAGE the test suite exercises. **MAP is an acknowledged gap**: system-context mapping sits upstream of adversarial testing and is not evidenced by this suite. Reporting what the evidence does not cover is part of the method; an assurance view that only shows green is not an assurance view.

## Limitations

- Synthetic findings are illustrative. Their volumes, dates and closure patterns were authored to exercise every interface state (open, in remediation, closed, overdue, escalated, rescan-exhausted), not to represent any real risk profile.
- The policy tiers beyond the 40-day anchor are demonstration values, not a recommendation.
- Single evidence run: trend views over multiple runs are the natural next iteration, alongside a negative-control run demonstrating that the harness can detect failures.
