<div align="center">

# ⚖️ turkiye-legal

**Open-source AI toolkit for Turkish law**

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Release](https://img.shields.io/badge/release-v0.1.0%20stable-brightgreen.svg)](CHANGELOG.md)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-compatible-5A67D8.svg)](https://code.claude.com)

*[Türkçe README →](README.md)*

</div>

---

## What is this?

`turkiye-legal` is an open-source AI toolkit for lawyers, in-house counsel and law
students working in Turkish law. It is built on Claude Code's plugin system.

It is not a plain prompt archive. It does three things at once:

1. **Structured tasks** — Petition review, contract screening, deadline calculation
   and similar work are defined as individual, repeatable skills.
2. **Source verification** — Every legal citation is checked automatically against a
   verified statute ledger in the repository. Fabricated article references are
   caught in CI.
3. **Deterministic calculation** — Deadline and holiday arithmetic is never left to a
   language model; it is delegated to Python code.

---

## Installation

```bash
claude plugin marketplace add https://github.com/mesutcandemir39/turkiye-legal
claude plugin install kvkk-veri-koruma@turkiye-legal
```

Then invoke a skill directly:

```
/kvkk-veri-koruma:aydinlatma-yukumlulugu
```

> **⚠️ Updates are not automatic.** Claude Code pins a plugin to the version you
> installed. Run `claude plugin update <name>@turkiye-legal` to stay current.

Step-by-step guide (Turkish): [`docs/KURULUM.md`](docs/KURULUM.md)

---

## Scope

| | Count |
|---|---|
| Installable plugins | **91** (81 practice areas + 10 infrastructure) |
| Structured skills | **923** |
| Practice areas | **81** |
| MCP servers | **2** (legislation, case law) |
| Verified statutes in ledger | **58** |

Practice areas range from family law and employment law to energy, healthcare,
customs and AI law. Full list: [`.claude-plugin/marketplace.json`](.claude-plugin/marketplace.json)

> **Honesty note:** The 10 infrastructure plugins (`cekirdek`, `kvkk-uyum`,
> `is-hukuku`, `sozlesme`, `icra-iflas`, `mevzuat-takip`, `dava-takip`,
> `ticaret-sirketler`, `fikri-mulkiyet`, `idare-vergi`) currently ship hooks,
> scripts and reference material but their `skills/` directories are still empty.
> This gap is tracked under milestone `M7 — Eklenti Bütünlüğü`. The skills live in
> the practice-area plugins listed above.

---

## How correctness is enforced

| Layer | What it does |
|---|---|
| **Statute ledger** | `sources/mevzuat/kanunlar.yaml` — verified statute records. A citation to a statute absent from the ledger is rejected. |
| **CI validation** | `validate_skills.py` and `validate_sources.py` run on every PR. A PR containing an unverifiable citation cannot be merged. |
| **Static tests** | `evaluations/static/` — no LLM required, mandatory gate on every PR. |
| **Golden tests** | `evaluations/golden/` — regression scenarios against a real model. |
| **`[DOĞRULANMADI]` protocol** | Information that cannot be verified is explicitly labelled, never stated as fact. |
| **Deterministic arithmetic** | `cekirdek/scripts/sure_hesapla.py` handles all deadline and judicial-recess calculation. |

Automated PR review is **fully deterministic** — it makes no external API calls and
requires no API key. See `scripts/validate/pr_review.py`.

---

## ⚖️ Legal disclaimer

**`turkiye-legal` is an assistive tool. It is not a lawyer and does not provide legal services.**

- ✅ Use it for preliminary review, drafting and research
- ✅ Verify every output against the primary source
- ✅ Final decisions must always be made by a qualified lawyer
- ❌ Creates no attorney–client relationship
- ❌ Is not a substitute for legal advice
- ❌ The maintainer and contributors accept no liability for resulting damage

**Take particular care** with criminal, pension, tax and deadline-bound matters.
A missed deadline causes irreversible loss of rights.

---

## Contributing

Contributions from lawyers and software engineers are equally welcome.

- [`CONTRIBUTING.md`](CONTRIBUTING.md) — how to contribute
- [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) — code of conduct
- [`GOVERNANCE.md`](GOVERNANCE.md) — governance
- [`SECURITY.md`](SECURITY.md) — security policy (do **not** open a public issue)

---

## License

Apache License 2.0 — see [`LICENSE`](LICENSE) and [`NOTICE`](NOTICE).
Attribution and upstream declarations: [`CREDITS.md`](CREDITS.md).

---

<div align="center">

Maintainer: [Mesut Can Demir](https://github.com/mesutcandemir39) · Telegram [@MesutCan](https://t.me/MesutCan)

</div>
