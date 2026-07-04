---
name: resume-optimizer
description: Write, rewrite, review, localize, JD-match, and export software-engineer résumés. Use when users ask to polish or draft a developer résumé, review/rate an existing one, tailor it to a job description, produce a China or North-America version, or export to LaTeX/Markdown/HTML/JSON. Enforces STAR + quantified outcomes + authenticity safeguards.
---

# Resume Optimizer (main skill)

Produce concise, role-focused, interview-ready résumé content for software / CS roles.
Prioritize project evidence, technical clarity, measurable impact, and authenticity.

## How to use this skill

1. Read [resume-rules.md](references/resume-rules.md) — the core ruleset (structure, ratios, STAR, 14 optimization dimensions, authenticity, checklists). Apply it in every mode.
2. Detect the user's intent and route to a mode (you may chain modes — e.g. Review → Polish → JD-Match → Localize → Export).
3. Operate on a **structured intermediate representation** aligned to `templates/json/resume.schema.json`: parse the user's resume into `basics / skills / work / projects / education / awards`, transform in the chosen mode, then export.

## Modes

### Polish (润色 / rewrite)
- Rewrite existing content with the STAR bullet pattern and the 14 optimization dimensions.
- Operate on the whole resume OR a single section / one project bullet — accept a target like "just the second project".
- Convert vague lines into concrete technology + responsibility + measurable result; deduplicate; fix terminology casing (MySQL, Spring Boot, etc.).
- Authenticity: package wording, never fabricate metrics. If a number can't be verified, emit `<<CONFIRM: metric>>` and flag it.
- Bullet formula (CN default): `为解决{问题}，基于{技术/方案}实现{关键动作}，将{指标}提升/降低{量化结果}，并带来{业务价值}`。

### Review (点评 / analysis)
- Output a professional, tiered critique. Three tiers:
  - 🔴 致命 / Critical — must fix before submission (missing required section, fabricated claim, wrong format like Word, generic role-less resume).
  - 🟡 重要 / Important — high impact (weak bullets, no metrics, repeated wording, skill list too generic).
  - 🟢 可选 / Optional — low-impact polish (casing, spacing, ordering tweaks).
- Each item: state the problem → give the concrete fix. Quote the offending line.

### JD-Match (按 JD 调整)
- Read the JD; see [jd-matching.md](references/jd-matching.md) for the method and role-bias strategies (backend / AI-Agent application dev / algorithm).
- Extract required keywords/capabilities; reorder, expand, or trim so the strongest JD-relevant evidence leads; align skill lines to JD's exact wording (the CN/NA "ATS" equivalent).

### Localize (中英 / CN↔NA 适配)
- Reshape — never translate literally. See [cn-na-market.md](references/cn-na-market.md).
- CN→NA: hard-delete photo/age/gender/ID/籍贯/政治面貌/full address/期望薪资; 微信→LinkedIn; strip skill tiers; rewrite 负责→Led/Built/Designed with X-Y-Z ("Accomplished X as measured by Y by doing Z"); enforce 1 page (new grad); delete CET; reorder education by experience.
- NA→CN: restore 技术栈 lines + STAR; add 求职意向 + 毕业时间; add 了解/熟悉 tiers; may add 排名/CET; reorder education by school prestige (985/211).

### Export (导出)
- Render the structured representation into the requested format. See [export-formats.md](references/export-formats.md).
- LaTeX-first: take `templates/latex/resume-{cn,na}.tex` (or a user-supplied `--template <path>`); substitute the 11 identity/education `<<TOKEN>>`s; then render projects/work/skills as ready-to-paste lines in the template's own macros (`\resumeProjectHeading{...}{...}{...}` + `\resumeItem{...}` + skill `\item`s) to replace the fictional example block. Hand off the `.tex` for the user to compile with `xelatex` (CN needs ctex) — this skill does not compile.
- Alternatives: Markdown (`templates/markdown/resume.md`), HTML (`templates/html/resume.html`), JSON Resume (`templates/json/resume.schema.json`).

## Cross-mode rules (always apply)
- Page economy: 1 page for new grads; more only when justified. CN: avoid the 1.5-page look. NA: trim to last 10–15 yr.
- Every highlight must be defensible in interview (see the Interview Defense Checklist in resume-rules.md).
- Platform-neutral: perform file reads, git/gh commands, and searches via whatever tools the host runtime provides; do not assume a specific tool name.
