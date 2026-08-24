# Export Formats — Contract v2

Export consumes one finalized object matching [`templates/json/resume.schema.json`](../../../templates/json/resume.schema.json). It never invents values; unresolved information remains a `<<CONFIRM: …>>` content marker and is called out before submission.

## Built-in LaTeX templates

`templates/latex/resume-cn.tex` and `templates/latex/resume-na.tex` compile with **XeLaTeX only**. Do not offer `pdflatex` because the NA template uses `fontspec`.

### Header tokens

Substitute and LaTeX-escape only these four tokens:

| Token | Schema field |
|---|---|
| `<<NAME>>` | `basics.name` |
| `<<EMAIL>>` | `basics.email` |
| `<<PHONE>>` | `basics.phone` |
| `<<GITHUB_USERNAME>>` | `basics.githubUsername` |

If a value is unavailable, leave a visible `MISSING_<TOKEN>` marker and list it in the export summary. In LaTeX output, escape that marker before insertion. No other `<<TOKEN>>` is valid in a built-in template.

### Generated regions

Replace the content *between*, not including, each marker pair exactly once:

```tex
% RESUME-SKILL:BEGIN EDUCATION
% RESUME-SKILL:END EDUCATION
% RESUME-SKILL:BEGIN EXPERIENCE
% RESUME-SKILL:END EXPERIENCE
% RESUME-SKILL:BEGIN SKILLS
% RESUME-SKILL:END SKILLS
```

- `EDUCATION`: render every `education[]` item with `institution`, `studyType`, `area`, `score`, `date`, `rank`, and `courses` when present. Omit missing subfields; never substitute a fictional degree, major, or course list.
- `EXPERIENCE`: render non-empty `work[]` and `projects[]` entries using `\resumeProjectHeading{...}{...}{...}`, followed by a nested itemize and `\resumeItem{...}` bullets. Omit an entry with no highlights.
- `SKILLS`: CN groups items by `tier`; NA groups by `category`. NA has no CET, language-score, or proficiency-tier line.

Use the templates' macros and preserve their preamble. If a region is empty, leave the region body empty instead of fabricating content.

## Escaping

Escape every substituted or generated LaTeX value exactly once: `%` → `\%`, `&` → `\&`, `_` → `\_`, `#` → `\#`, `^` → `\textasciicircum{}`, `$` → `\$`, `{`/`}` → `\{`/`\}`, `\` → `\textbackslash{}`, and `~` → `\textasciitilde{}`. CJK characters need no escape under XeLaTeX + ctex.

## Other formats

Markdown and HTML use the same three named regions. HTML must retain semantic `<header>`, `<main>`, `<section>` elements and print `@page` CSS. JSON export is the finalized schema object and must not contain LaTeX macros, template tokens, or unresolved `<<CONFIRM: …>>` markers.

## Custom templates

Automatic replacement is supported only when the custom template has all three marker pairs and compatible `\resumeEduSubheading`, `\resumeEduLine`, `\resumeProjectHeading`, and `\resumeItem` macros. Otherwise emit a copy-ready region snippet and state that the user must paste it manually.

## Export summary

State the output file name, the XeLaTeX command, unresolved header tokens, every `<<CONFIRM: …>>` marker, and any section omitted because it was empty.
