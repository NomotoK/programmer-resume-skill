# Export Formats — Rendering Rules & Token/Macro Conventions

> Consumed by the **Export mode** of `resume-optimizer`. Export takes the finalized JSON resume (the intermediate representation) and renders it into one of four deliverable formats: **LaTeX** (primary), **Markdown**, **HTML**, or **JSON Resume**. LaTeX rendering is *split*: identity/education fields are token-substituted into the `.tex`; projects/work/skills are emitted as ready-to-paste macro calls that replace the template's fictional example block.
>
> **Core promise.** A reproducible, honesty-safe render: every identity/education token either resolves to a verified schema value or stays as a visible `<<TOKEN>>` flag; every body macro is generated from schema data with correct LaTeX escaping; nothing is fabricated to fill space.

---

## 1. Intermediate Representation

The resume is held as a single JSON object conforming to [`templates/json/resume.schema.json`](../../../templates/json/resume.schema.json). All format renders read from this object — never from free text. The schema's top-level keys:

| Key | Type | Rendered as |
|---|---|---|
| `basics` | object | Identity tokens (`<<NAME>>` … `<<LANGUAGE_SCORE>>`) + contact lines |
| `education[]` | array | Identity tokens (`<<SCHOOL_*>>` / `<<GPA_*>>` / `<<DATE_*>>`) + degree body |
| `skills[]` | array | Body macro: skill `\item` lines (CN tiered / NA categorized) |
| `work[]` | array | Body macros: `\resumeProjectHeading` + `\resumeItem` per role |
| `projects[]` | array | Body macros: `\resumeProjectHeading` + `\resumeItem` per project |
| `awards[]` | array | Body macro: optional awards `\item` lines |

**Market selection.** `basics.targetMarket` (`CN` or `NA`) decides which `.tex` template, which bullet style (CN STAR + 技术栈 line vs NA X-Y-Z action verb), which skill layout (tiered vs categorized), and which file-name convention applies. See [`cn-na-market.md`](cn-na-market.md) for the per-market content rules; this file defines only the *rendering* of already-localized content.

---

## 2. Token Map — Identity & Education (Auto-Substituted into the `.tex`)

The user-supplied LaTeX templates (`templates/latex/resume-{cn,na}.tex`) carry **11 identity/education placeholders**. Export substitutes each from the JSON resume; an unfilled token stays as `<<TOKEN>>` and is flagged in the export summary (see [Honesty](#10-honesty--matching--invention) below) — it is **never** guessed.

| # | Token | Schema field | Notes |
|---|---|---|---|
| 1 | `<<NAME>>` | `basics.name` | Full name; CN market keeps CJK ordering; NA market uses `First Last`. |
| 2 | `<<EMAIL>>` | `basics.email` | Plain `local@domain`; do not mailto-link in `.tex`. |
| 3 | `<<PHONE>>` | `basics.phone` | CN market: `+86 138-xxxx-xxxx`; NA market: `(xxx) xxx-xxxx`. |
| 4 | `<<GITHUB_USERNAME>>` | `basics.githubUsername` | Username only — the template wraps the URL. |
| 5 | `<<LANGUAGE_SCORE>>` | `basics.languageScore` | CN only (CET-6 / TOEFL / IELTS). NA market: leave token empty and drop the line — do **not** emit an English-proficiency line for NA. |
| 6 | `<<SCHOOL_MASTER>>` | `education[?level=="master"].institution` | First master-level entry. Empty if no master degree — token stays `<<SCHOOL_MASTER>>` and the line is dropped on render. |
| 7 | `<<GPA_MASTER>>` | `education[?level=="master"].score` | e.g. `3.8/4.0`. CN may pair with `rank`. |
| 8 | `<<DATE_MASTER>>` | `education[?level=="master"].date` | e.g. `2024.06` or `2022.09–2024.06`. |
| 9 | `<<SCHOOL_BACHELOR>>` | `education[?level=="bachelor"].institution` | First bachelor-level entry. |
| 10 | `<<GPA_BACHELOR>>` | `education[?level=="bachelor"].score` | e.g. `3.7/4.0`. |
| 11 | `<<DATE_BACHELOR>>` | `education[?level=="bachelor"].date` | e.g. `2018.09–2022.06`. |

**Selection rule for `education[]`.** Pick the **first** array entry whose `level` matches `master` (resp. `bachelor`); do not assume ordering. If a level is absent, the three corresponding tokens stay unfilled and the master (or bachelor) block is dropped from the rendered `.tex` rather than fabricated.

**Substitution mechanics.** Replace each `<<TOKEN>>` literally in the `.tex` source. Apply LaTeX escaping (see [§5](#5-latex-escaping-rules)) to the *value* before substitution, never to the token name.

---

## 3. Body Generation — Rendered, Not Tokenized

Projects, work, and skills are **not** tokens. Export emits them as ready-to-paste LaTeX using the template's **own** macros, which the user pastes *over* the template's fictional example block. This keeps template typography (fonts, spacing, `\resumeProjectHeading` definition) under the user's control — Export never edits macro definitions.

### 3.1 Project / Work entry

For each `projects[]` and `work[]` entry, emit one heading line followed by one `\resumeItem{...}` per highlight bullet:

```latex
\resumeProjectHeading{<name>}{<techstack joined by ` / `>}{<date>}
  \resumeItem{<highlight bullet 1, escaped>}
  \resumeItem{<highlight bullet 2, escaped>}
  \resumeItem{<highlight bullet 3, escaped>}
```

Field mapping:

| Macro slot | Project entry | Work entry |
|---|---|---|
| `{<name>}` | `projects[i].name` | `work[i].company` + ` — ` + `work[i].position` (e.g. `Acme — Backend Intern`) |
| `{<techstack>}` | `projects[i].techStack.join(" / ")` | `work[i].techStack.join(" / ")` |
| `{<date>}` | `projects[i].date` | `work[i].startDate` + `–` + `work[i].endDate` (or `Present`) |
| `\resumeItem{...}` | one per `projects[i].highlights[j]` | one per `work[i].highlights[j]` |

**Rules:**

- **Tech stack separator is ` / ` (space-slash-space)** — preserves camelCase boundaries (e.g. `Spring Boot / MyBatis / Redis`) and matches the template's existing example style. Do not use `,` or `·`.
- **Highlight bullets must already be in the correct market style** from the prior mode — Export does **not** restyle bullets. CN bullets arrive as STAR + 技术栈 phrasing (`为解决…基于…实现…将…提升…`); NA bullets arrive as X-Y-Z (`Led … as measured by …, by doing …`). See [`cn-na-market.md`](cn-na-market.md).
- **Bullet count.** Render every bullet in `highlights[]`; do not summarize or truncate. If the array is empty, omit the entry entirely (do not emit a heading with no bullets).
- **Escaping applies** to the rendered values (names, tech stack tokens, bullet text) per [§5](#5-latex-escaping-rules).
- **No fictional content.** If a field is missing (e.g. `techStack` empty), emit the macro with an empty `{}` slot rather than inventing a stack. Prefer dropping the entry if core fields (`name`/`company`, `highlights`) are absent.

### 3.2 Skill group

For each `skills[]` group, emit one `\item \small ...` line in the template's skill style. The shape differs by market (the bullets themselves arrive pre-styled from prior modes; Export only wraps them):

**CN (tiered)** — group by `tier` (`了解` / `熟悉` / `熟练掌握` / `精通` — `精通` is校招禁用, see [`cn-na-market.md`](cn-na-market.md)):

```latex
\item \small \textbf{熟练掌握}：Java / Spring Boot / MySQL / Redis
\item \small \textbf{熟悉}：Kubernetes / Docker / Kafka
\item \small \textbf{了解}：Ray / Flink
```

**NA (categorized, no tiers)** — group by `category`:

```latex
\item \small \textbf{Languages:} Python, Go, TypeScript
\item \small \textbf{Frameworks:} React, FastAPI, PyTorch
\item \small \textbf{Cloud/Tools:} AWS (ECS, S3, DynamoDB), Kubernetes, Terraform, Docker
```

Field mapping: `skills[i].category` (NA) or `skills[i].tier` (CN) → the bold label; `skills[i].items.join(", ")` (NA) or `skills[i].items.join(" / ")` (CN) → the value. NA uses `, ` separator and no proficiency tier (per hiring-manager consensus — self-rated tiers are subjective). CN uses ` / ` separator with the tier label.

### 3.3 Awards (optional)

If `awards[]` is non-empty and the market conventions allow the section (CN: always allowed; NA: only for new-grad or notable), emit one `\item` per award. The user-supplied templates define no `Awards` section and no Awards-specific macro, so Export emits only plain `\item` lines (one per award) under a section heading the template already provides or the user inserts:

```latex
% Under a section heading the template provides or the user inserts (e.g. \section{Awards})
\item \small <awards[i].title> — <awards[i].awarder>, <awards[i].date>
```

If the template has no `Awards` section, Export notes that and the user adds the heading themselves — Export must **not** invent macros (e.g. a subheading command) or sections the template doesn't define. Drop the entire section if `awards[]` is empty — never fabricate awards.

---

## 4. LaTeX (Primary) Workflow

LaTeX is the primary export target because it produces ATS-safe, recruiter-expected typography for both CN (ctex) and NA (xelatex/pdflatex) markets.

**Procedure (do this every time, in order):**

1. **Select the template.**
   - CN market → `templates/latex/resume-cn.tex` (compiled with **`xelatex`** + `ctex` for CJK).
   - NA market → `templates/latex/resume-na.tex` (compiled with `xelatex` or `pdflatex`).
   - User override: if the user passes `--template <path>`, copy that template instead and infer the market from `basics.targetMarket` for bullet/skill style.
2. **Substitute the 11 identity/education tokens** (§2) into the copied `.tex`. Apply escaping (§5) to values. Unfilled tokens stay as `<<TOKEN>>` and are listed in the export summary.
3. **Emit the generated body block** (§3) — projects, work, skills, (optional) awards — as a single fenced ```latex``` snippet, with explicit instructions:
   > Replace the template's fictional example section (between `% --- EXAMPLE START ---` and `% --- EXAMPLE END ---`, or the obvious placeholder block) with the block below. Do **not** modify the preamble or any `\newcommand` / `\renewcommand` definition.
4. **Hand off compilation.** This skill does **not** run `xelatex` / `pdflatex`. Tell the user the exact command and the expected output filename (§7). The user compiles locally — typically `xelatex resume-cn.tex` twice (for references/TOC, if any).
5. **Leave `<<CONFIRM: …>>` markers** for any unverified metric (e.g. a quantified result the user could not source). These are not LaTeX errors — they render visibly in the PDF so the user sees what to fill before submitting. Example: `\resumeItem{将 QPS 从 <<CONFIRM: baseline>> 提到 100w+，by 分库分表}`.

**What Export does NOT do:**

- Does not call `xelatex` / `pdflatex` / `latexmk`.
- Does not download CTAN packages or check the user's TeX distribution.
- Does not modify `\documentclass`, packages, or macro definitions in the template.
- Does not pick a font — fonts live in the template.

---

## 5. LaTeX Escaping Rules

Apply these escapes to **every** value before substituting into the `.tex` or inserting into a macro slot. Apply them once, at render time — do not double-escape (the JSON resume stores raw text).

| Raw char | Escaped | Where it typically appears |
|---|---|---|
| `%` | `\%` | Percent signs in metrics ("缓存命中率 95%" → `95\%`); **also inside numbers** ("QPS 提升 30%" → `30\%`). |
| `&` | `\&` | Company names ("AT&T"); tech stack ("R&D"). |
| `_` | `\_` | Identifiers, package names (`foo_bar`), GitHub repos. |
| `#` | `\#` | Issue numbers ("fixes #123"), C# (`C\#`). |
| `$` | `\$` | Currency, math-adjacent text. |
| `{` `}` | `\{` `\}` | Literal braces in prose. |
| `\` | `\textbackslash{}` | Windows paths, regex. |
| `~` | `\textasciitilde{}` | File paths, `~/`. |

**Special cases:**

- **`%` inside numbers** — the most common escaping bug. LaTeX treats `%` as a comment marker *everywhere*, including mid-number: `95%` becomes `95` + commented rest-of-line. Always escape: `95\%`.
- **URLs** — the template wraps `<<GITHUB_USERNAME>>` into a `\href{https://github.com/<username>}{...}`. Do **not** escape `~` or `_` inside the URL *argument* of `\href` (URLs are handled by the `hyperref` package's own escaping); do escape them if they appear in display text.
- **CJK content** — no escaping needed for CJK characters themselves; `xelatex` + `ctex` handle them natively. Only escape the ASCII special chars above.
- **Quotes** — use `` `` `` (two backticks) for left double quote and `''` (two apostrophes) for right double quote; do not paste smart quotes from a word processor.
- **Em dash / en dash** — `X--Y` (en dash) for date ranges (`2022--2024`); `X---Y` (em dash) for parenthetical breaks. The JSON stores `–` / `—`; normalize to `--` / `---` at render.

---

## 6. Markdown, HTML, JSON Resume (Secondary Formats)

### 6.1 Markdown

Fill `templates/markdown/resume.md` (a skeleton with the same section order as the `.tex`). Rules:

- Use `##` for section headings (Education / Skills / Experience / Projects / Awards).
- Use `-` bullets for highlights — one per `\resumeItem` equivalent.
- Inline the tech stack as `**Tech:** A / B / C` under each project/role heading.
- Inline links as `[text](url)`; GitHub URL is `https://github.com/<githubUsername>`.
- No escaping needed (Markdown is plain text).

### 6.2 HTML

Fill `templates/html/resume.html` — single-column, print-CSS, ATS-friendly. Rules:

- One `<section>` per resume block; one `<ul>` per role/project's highlights.
- Use semantic tags (`<header>`, `<main>`, `<section>`, `<ul>`, `<li>`) — no tables for layout (ATS parsers handle semantic HTML better).
- Inline all CSS in a `<style>` block in `<head>` (no external stylesheet) — the file must be a single self-contained `.html`.
- Print CSS: `@page { size: A4; margin: 0.5in; }` and `@media print` rules to hide nav, set font size to 11pt, etc.
- Escape `<`, `>`, `&` as `&lt;`, `&gt;`, `&amp;` in body text. Do not escape CJK.

### 6.3 JSON Resume

Emit structured JSON conforming to `templates/json/resume.schema.json`. This is essentially "return the intermediate representation with the body content finalized":

- Top-level keys: `basics`, `education`, `skills`, `work`, `projects`, `awards` (omit empty arrays — see [Honesty](#10-honesty--matching--invention)).
- All strings are the **final** rendered text (post-localization, post-quantification) — no macros, no tokens, no `<<...>>` markers.
- If a `<<CONFIRM: …>>` flag remains, the JSON is invalid for submission — surface it as a blocker in the export summary, do not silently strip it.
- No escaping needed (JSON handles its own string escaping).

---

## 7. File Naming

The exported file name signals market and identity. Use these conventions unless the user overrides:

| Market | Pattern | Example |
|---|---|---|
| **CN** | `姓名-目标岗位-学校-专业.pdf` | `张三-后端开发工程师-清华大学-计算机科学与技术.pdf` |
| **NA** | `FirstLast_Resume.pdf` | `JaneDoe_Resume.pdf` |

**Rules:**

- The `.tex` / `.md` / `.html` / `.json` source uses the same stem with the matching extension.
- NA: use `FirstLast` capitalized, no spaces, no middle initial unless the user's legal name uses one.
- CN: 学校 is the *most recent* (master if present, else bachelor); 专业 is the bachelor's major (master's specialty is too narrow for the file name).
- No dates in the file name (the resume itself carries dates); exception: if the user keeps multiple versions, append `-v2` etc.

---

## 8. Token-Map Completeness Check

The 11 tokens in [§2](#2-token-map--identity--education-auto-substituted-into-the-tex) are the **complete** identity/education token surface. The LaTeX templates must not introduce a 12th token without first being added to this file and to `templates/json/resume.schema.json`. The check below asserts the canonical 11 appear in this reference:

```python
# Run from repo root:
python3 - <<'PY'
import re
g=set(re.findall(r"<<([A-Z_]+)>>", open("skills/resume-optimizer/references/export-formats.md").read()))
canonical={"NAME","EMAIL","PHONE","GITHUB_USERNAME","LANGUAGE_SCORE","SCHOOL_MASTER","GPA_MASTER","DATE_MASTER","SCHOOL_BACHELOR","GPA_BACHELOR","DATE_BACHELOR"}
print("OK" if canonical<=g else f"MISSING {canonical-g}")
PY
```

Expected output: `OK`.

---

## 9. Render Order Summary (Cheat Sheet)

For a single Export run:

1. Load `basics.targetMarket` → pick template (`resume-cn.tex` / `resume-na.tex`) and file-name convention.
2. Build token map (§2): for each of the 11 tokens, look up the schema field; escape the value (§5); substitute into the `.tex`. Unfilled → leave `<<TOKEN>>`, record in summary.
3. Generate body (§3):
   - `work[]` → `\resumeProjectHeading` + `\resumeItem` block.
   - `projects[]` → `\resumeProjectHeading` + `\resumeItem` block.
   - `skills[]` → `\item \small` lines (CN tiered or NA categorized).
   - `awards[]` (optional) → `\item` lines.
4. Emit the body block fenced, with paste-over instructions (§4 step 3).
5. If secondary format requested (Markdown / HTML / JSON Resume), fill the matching template (§6).
6. Emit the file name (§7) and the compile command (`xelatex` for CN, `xelatex`/`pdflatex` for NA). Do not compile.
7. Emit the honesty summary: list every `<<TOKEN>>` still unfilled, every `<<CONFIRM: …>>` flag, and every section dropped for being empty.

---

## 10. Honesty — Matching ≠ Invention

**Hard rules:**

- **Never invent field values.** If `basics.githubUsername` is empty, `<<GITHUB_USERNAME>>` stays as-is and the line is flagged — Export does **not** generate a plausible-looking handle.
- **Omit empty sections; do not fabricate.** If `projects[]` is empty, the Projects section is dropped from the rendered `.tex` (and the JSON Resume omits the key). An empty section is honest; a fabricated project is not.
- **Unfilled identity/education tokens stay visible** as `<<TOKEN>>` in the `.tex` (and as flags in the export summary), so the user sees exactly which fields to fill before submission. They are **not** replaced with `[Your Name Here]`-style placeholder prose, and never with guessed real values.
- **`<<CONFIRM: …>>` markers must be resolved by the user**, not by Export. If a highlight bullet contains an unverified metric, Export renders the marker verbatim into the PDF; the visible flag forces the user to confirm or remove it before submitting. Do not silently strip the flag, and do not replace it with a guessed number.
- **Master/bachelor block absence is honored.** If a candidate has no master degree, the master block is dropped — not filled with "目前在读" or a projected date.

**Render-time vs. content-time.** Honesty is enforced at content time (Draft / Optimize / Tailor modes produce only defendable claims; see [`resume-rules.md`](resume-rules.md) and [`guide-5-authenticity.md`](guide-5-authenticity.md)). Export's job is to *preserve* that honesty through rendering: it does not invent, summarize away gaps, or strip flags. If Export receives JSON with a `<<CONFIRM: …>>` marker, that is a content-time signal that propagates visibly to the final PDF.

---

## References

- Schema: [`templates/json/resume.schema.json`](../../../templates/json/resume.schema.json) — canonical field names for every token and body macro slot in this file.
- Market content rules: [`cn-na-market.md`](cn-na-market.md) — CN vs NA bullet style (STAR + 技术栈 vs X-Y-Z), skill tier rules, section ordering, ATS hygiene.
- Authenticity rules: [`resume-rules.md`](resume-rules.md), [`guide-5-authenticity.md`](guide-5-authenticity.md) — what counts as defendable content before Export renders it.
- Highlight patterns: [`guide-6-highlights.md`](guide-6-highlights.md) — the bullet styles Export assumes it receives.
