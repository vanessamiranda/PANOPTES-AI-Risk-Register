# PANOPTES: Second-Line AI Oversight, End to End

A reference implementation of the full second-line oversight cycle for AI systems, from inventory to committee. The landing view is the output that matters at leadership level: a quarterly executive report to a modelled AI risk committee, carrying a posture statement, eight indicators against prior period, and the decisions requested of the committee, each with a recommendation. Everything beneath it exists to make that page true.

**Reference implementation. Synthetic findings are fictional and scoped to fictional systems. Zero personally identifiable information. Independent portfolio artifact, not employer work.**

## The oversight model

Decision rights follow materiality. Every AI use case is inventoried and tiered; the tier decides who approves deployment, who may accept residual risk, and how often independent validation recurs. Tier 1 (regulated-domain decisioning) answers to the risk committee; tier 3 (internal drafting with human review) earns a checklist, not a committee. Proportionality is deliberate: governance that costs the same everywhere is governance nobody follows.

The cycle the artifact implements:

1. **Inventory and classify.** Use cases enter a register with materiality tier, accountable owner, approval reference and data lineage.
2. **Validate independently.** Challenge comes from outside the build: the executed HERMES adversarial run is the independent challenge evidence for ARGUS, and validation currency is itself monitored.
3. **Monitor.** Performance and drift thresholds are declared next to each use case with green, amber and red limits, not discovered after an incident.
4. **Control change.** Model-version, prompt and guardrail changes carry approval references and post-change verification; the change log deliberately shows the control catching its own gaps.
5. **Manage exceptions.** Departures from the standard are time-bound, carry residual-risk acceptance at the authority the tier matrix names, and have review dates the indicators police.
6. **Report upward.** The executive report states posture honestly, shows movement, and asks the committee for decisions, not applause. One validation is overdue, one exception is past review and one threshold sits amber by design: an oversight view that can only show green is not an oversight view.

Definitions, authority matrix and indicator methodology: [GOVERNANCE.md](GOVERNANCE.md).

## Views

- **Executive report** (landing): quarterly committee pack, print-formatted. Posture, indicators against prior period, decisions requested with recommendations, acknowledged gaps, next period.
- **Use-case inventory**: materiality tiers, owners, approval references, validation state, thresholds and data lineage, plus the approval-authority and residual-risk-acceptance matrix.
- **Risk register**: sortable, filterable records, each tagged real HERMES evidence or synthetic, with framework references, treatment, rescan usage and escalation state.
- **Key risk indicators**: eight indicators computed at render time, five remediation and three oversight, never hard-coded.
- **Framework coverage**: MITRE ATLAS, OWASP Top 10 for Large Language Model Applications (2025) and NIST AI Risk Management Framework mappings, with an acknowledged MAP-function gap.
- **Escalations**: policy breaches ordered by days overdue, with the owner / regional lead / risk committee path.
- **Change control & exceptions**: approved changes with verification records; time-bound exceptions with policed review dates.

## Implementation

Static site: one HTML file with embedded data, no backend, no external dependencies beyond web fonts. `register-data.json` is the canonical data artifact; `build-register-data.py` regenerates it from the HERMES run file and the synthetic set, then the data is embedded into `index.html`.

To regenerate after editing the data:

```
python3 build-register-data.py
python3 -c "d=open('register-data.json').read().replace('</','<\\\\/'); t=open('dashboard-template.html').read(); open('index.html','w').write(t.replace('__DATA__', d))"
```

Deploy: public repository, GitHub Pages from branch `main`, root folder. Live within a couple of minutes at `https://vanessamiranda.github.io/PANOPTES-AI-Risk-Register/`.

## Part of a set

- **ARGUS**: multi-agent Know Your Customer / Customer Due Diligence review agent reference design (first line: the system doing the work)
- **HERMES**: adversarial testing and assurance exercise executed against ARGUS (independent challenge)
- **PANOPTES**: the oversight and reporting layer over both (second line)

Built by Vanessa Miranda.
