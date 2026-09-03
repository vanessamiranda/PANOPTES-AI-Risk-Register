# PANOPTES: AI Risk Register and Assurance Dashboard

A reference implementation of second-line risk reporting: risk register, key risk indicators, framework coverage and escalation monitoring, computed over real adversarial test evidence from the [HERMES red-team exercise](https://github.com/vanessamiranda/hermes-redteam) plus clearly labelled synthetic findings.

**Reference implementation. Synthetic findings are fictional and scoped to fictional systems. Zero personally identifiable information. Independent portfolio artifact, not employer work.**

## Views

- **Risk register**: sortable, filterable table of all records, each tagged with its source (real HERMES evidence or synthetic), with per-record framework references, treatment, rescan usage and escalation state.
- **Key risk indicators**: five indicators computed at render time from the data file against the modelled remediation policy. Definitions in [GOVERNANCE.md](GOVERNANCE.md).
- **Framework coverage**: MITRE ATLAS, OWASP Top 10 for Large Language Model Applications (2025) and NIST AI Risk Management Framework mappings per risk category, with executed-test and pass counts from the real run, including an acknowledged MAP-function coverage gap.
- **Escalations**: policy breaches ordered by days overdue, with rescan usage and the owner / regional lead / risk committee path.

## Stack

Static site: one HTML file with embedded data, no backend, no build step, no external dependencies beyond web fonts. `register-data.json` is the canonical data artifact; `build-register-data.py` regenerates it from the HERMES run file and the synthetic set, then the data is embedded into `index.html`.

## Deploy

1. Create a public repository (yours: `PANOPTES-AI-Risk-Register`).
2. Commit `index.html`, `dashboard-template.html`, `register-data.json`, `GOVERNANCE.md`, `README.md`, `build-register-data.py`, and the HERMES run file `results_20260903T011051Z.json`.
3. Repository settings, Pages, deploy from branch `main`, root folder.
4. The dashboard is live at `https://<username>.github.io/PANOPTES-AI-Risk-Register/` within a couple of minutes.

To regenerate data after editing the synthetic set or pulling a new HERMES run:

```
python3 build-register-data.py
python3 -c "d=open('register-data.json').read().replace('</','<\\\\/'); t=open('dashboard-template.html').read(); open('index.html','w').write(t.replace('__DATA__', d))"
```

## Part of a set

- **ARGUS**: multi-agent Know Your Customer / Customer Due Diligence review agent reference design
- **HERMES**: adversarial testing and assurance exercise against ARGUS
- **PANOPTES**: the oversight and reporting layer over both

Built by Vanessa Miranda.
