# PANOPTES

AI risk governance and assurance dashboard. A reference implementation of second-line risk reporting: risk register, key risk indicators, framework coverage and escalation monitoring, computed over real adversarial test evidence from the [HERMES red-team exercise](https://github.com/vanessamiranda/hermes-redteam) plus clearly labelled synthetic findings.

**Reference implementation. Synthetic findings are fictional and scoped to fictional systems. Zero personally identifiable information. Independent portfolio artifact, not employer work.**

## Views

- **Risk register**: sortable, filterable table of all records, each tagged with its source (real HERMES evidence or synthetic), with per-record framework references, treatment, rescan usage and escalation state.
- **Key risk indicators**: five indicators computed at render time from the data file against the modelled remediation policy. Definitions in [GOVERNANCE.md](GOVERNANCE.md).
- **Framework coverage**: MITRE ATLAS, OWASP Top 10 for Large Language Model Applications (2025) and NIST AI Risk Management Framework mappings per risk category, with executed-test and pass counts from the real run, including an acknowledged MAP-function coverage gap.
- **Escalations**: policy breaches ordered by days overdue, with rescan usage and the owner / regional lead / risk committee path.

## Stack

Static site: one HTML file with embedded data, no backend, no build step, no external dependencies beyond web fonts. `findings.json` is the canonical data artifact; `build_findings.py` regenerates it from the HERMES run file and the synthetic set, then the data is embedded into `index.html`.

## Deploy

1. Create a public repository named `panoptes`.
2. Commit `index.html`, `template.html`, `findings.json`, `GOVERNANCE.md`, `README.md`, `build_findings.py`, and the HERMES run file `results_20260903T011051Z.json`.
3. Repository settings, Pages, deploy from branch `main`, root folder.
4. The dashboard is live at `https://<username>.github.io/panoptes/` within a couple of minutes.

To regenerate data after editing the synthetic set or pulling a new HERMES run:

```
python3 build_findings.py
python3 -c "d=open('findings.json').read().replace('</','<\\\\/'); t=open('template.html').read(); open('index.html','w').write(t.replace('__DATA__', d))"
```

## Part of a set

- **ARGUS**: multi-agent Know Your Customer / Customer Due Diligence review agent reference design
- **HERMES**: adversarial testing and assurance exercise against ARGUS
- **PANOPTES**: the oversight and reporting layer over both

Built by Vanessa Miranda.
