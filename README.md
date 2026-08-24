# Programmer Resume Skill Suite

A cross-platform (Claude Code + OpenAI Codex) plugin of skills for **software-engineer job-search résumés** — polish, review, JD-match, CN↔NA localization, code-to-resume, and mock-interview prep, with LaTeX-first export.

## Capabilities

Six capabilities, packed into three skills:

| Capability | Skill | What it does |
|---|---|---|
| **Polish** (rewrite) | `resume-optimizer` | Rewrite vague bullets into STAR + quantified outcomes (14 optimization dimensions). Operates on the whole résumé or a single section/bullet. Emits `<<CONFIRM: …>>` for any metric it cannot verify — never fabricates. |
| **Review** (critique) | `resume-optimizer` | Tiered feedback: 🔴 Critical / 🟡 Important / 🟢 Optional. Each item quotes the offending line and gives the concrete fix. |
| **JD-Match** | `resume-optimizer` | Parse a job description, extract required keywords/capabilities, reorder/expand/trim so the strongest JD-relevant evidence leads. Built-in role bias for backend / AI-Agent application dev / algorithm roles. |
| **Localize** (CN↔NA) | `resume-optimizer` | Reshape — **not** literal translation — between a Chinese-campus-recruiting résumé and a North-America one. See *CN↔NA: reshapes, doesn't translate* below. |
| **Code → résumé** | `resume-from-code` | Read a project repo + your own git history, mine real technical highlights, draft one defensible project section (STAR / X-Y-Z) plus an evidence list. |
| **Mock interview** | `resume-mock-interview` | Turn each project into a drilled question bank across 5 layers (L1 implementation → L5 fundamentals), each with talking points + follow-ups, plus the 6-question defense set. |

`resume-optimizer` also handles **Export** (LaTeX-first; Markdown/HTML/JSON alternatives) — see *Templates & export* below.

## Install

**Claude Code:** `/plugin` → add this repo as a marketplace/plugin, or copy `skills/*` into your skills directory.

**OpenAI Codex:** install as a plugin (`.codex-plugin/plugin.json`), or copy `skills/*` into `~/.codex/skills/`.

Both manifests (`.claude-plugin/plugin.json`, `.codex-plugin/plugin.json`) point at the same `skills/` tree — one source, two runtimes. No skill hard-codes host-specific tool names (verified by `grep -rniE "Read tool|WebFetch|web_fetch" skills`).

## Usage

Ask naturally. Modes can be chained (a typical flow is Review → Polish → JD-Match → Localize → Export).

- *"Polish my resume."*
- *"Review this resume and tell me what's critical."*
- *"Tailor it to this JD: …"*
- *"Localize for North America."*
- *"Generate a project section from this repo: /path or GitHub URL."*
- *"Mock-interview my resume projects."*
- *"Export to LaTeX (CN / NA / my own template)."*

## CN↔NA: reshapes, doesn't translate

Localization between the Chinese campus-recruiting format and the North-America format is a **structural reshape**, not a sentence-by-sentence translation. Concretely:

- **CN→NA:** hard-delete photo / age / gender / ID / 籍贯 / 政治面貌 / full address / 期望薪资; replace 微信 with LinkedIn; strip skill tiers (了解/熟悉/熟练掌握); rewrite 负责-style lines as `Led / Built / Designed` + X-Y-Z ("Accomplished X as measured by Y by doing Z"); enforce one page (new grad); drop CET; reorder education below experience.
- **NA→CN:** restore 技术栈 lines + STAR; add 求职意向 + 毕业时间; re-add 了解/熟悉 tiers; optionally add 排名 / CET; reorder education by school prestige (985/211).

Full rules: [`skills/resume-optimizer/references/cn-na-market.md`](skills/resume-optimizer/references/cn-na-market.md), sourced from [`docs/research/`](docs/research/).

## Templates & export

Export is **LaTeX-first**. The repo ships two built-in templates under [`templates/latex/`](templates/latex/):

- `resume-cn.tex` — Chinese; compile with **xelatex** (needs `ctex`).
- `resume-na.tex` — English / North-America-oriented; compile with **xelatex**.

The skill substitutes four header `<<TOKEN>>`s (name, email, phone, GitHub username) and replaces the named `EDUCATION`, `EXPERIENCE`, and `SKILLS` template regions with schema-derived macros (`\resumeEduSubheading{...}{...}{...}`, `\resumeProjectHeading{...}{...}{...}`, `\resumeItem{...}`). This preserves real degree, major, course, and conditional NA content without fictional defaults. The skill **does not compile** — it hands off the `.tex` for you to run `xelatex`.

**Bring your own template:** drop your `.tex` into `templates/latex/` (or point Export at any path: *"export with template `<path>`"*). Automatic replacement requires the four header tokens, all three named regions, and compatible built-in macros; otherwise Export emits copy-ready snippets for manual paste. See [`templates/latex/TEMPLATE_GUIDE.md`](templates/latex/TEMPLATE_GUIDE.md) for the contract.

Alternatives: Markdown ([`templates/markdown/resume.md`](templates/markdown/resume.md)), HTML ([`templates/html/resume.html`](templates/html/resume.html)), JSON Resume ([`templates/json/resume.schema.json`](templates/json/resume.schema.json)).

## Privacy

These skills run **fully locally inside your agent session**. They do not upload your résumé anywhere, do not call external APIs beyond what your agent runtime already uses, and **never auto-submit** to any employer or job board. All file reads, git/gh commands, and searches go through whatever tools your host runtime provides. Export produces files in your workspace for you to review and act on.

## Authenticity red line

Every capability enforces the same rule: **package wording, never fabricate.** If a metric cannot be verified from evidence (the user's resume, repo, or git history), the skill emits a `<<CONFIRM: …>>` marker and flags it. The mock-interview skill will feed back claims that won't survive scrutiny as polish suggestions. The examples in [`examples/`](examples/) are explicitly fictional — do not copy them into a real résumé.

## Examples & specs

- **Worked examples** (one fictional new-grad backend résumé through every capability): [`examples/`](examples/) — see [`examples/README.md`](examples/README.md).
- **Design spec** (capabilities, architecture, decision rationale): [`docs/superpowers/specs/2026-07-02-resume-skill-suite-design.md`](docs/superpowers/specs/2026-07-02-resume-skill-suite-design.md).
- **Plan & progress** (15-task breakdown): [`docs/superpowers/plans/2026-07-03-resume-skill-suite.md`](docs/superpowers/plans/2026-07-03-resume-skill-suite.md).
- **CN↔NA research base:** [`docs/research/`](docs/research/).

## Repository layout

```
.claude-plugin/plugin.json        Claude Code manifest
.codex-plugin/plugin.json         OpenAI Codex manifest (same skills/)
agents/openai.yaml                Codex agent interface
skills/
  resume-optimizer/               main skill: Polish / Review / JD-Match / Localize / Export
    SKILL.md + references/        resume-rules, jd-matching, cn-na-market, export-formats, guides 1–6
  resume-from-code/               code → project section
    SKILL.md + references/        code-mining
  resume-mock-interview/          resume → interview question bank
    SKILL.md + references/        interview-bank
templates/
  latex/                          resume-cn.tex, resume-na.tex, TEMPLATE_GUIDE.md
  markdown/  html/  json/         alt export formats + JSON schema
examples/                         7 fictional files showing every capability
scripts/validate.py               structural validator (skills/refs/manifests/template vars)
tests/                            unittest suite for the validator
```

## License

MIT
