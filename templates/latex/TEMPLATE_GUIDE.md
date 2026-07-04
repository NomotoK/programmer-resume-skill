# LaTeX Template Guide

The built-in templates are `resume-cn.tex` (Chinese, compile with **xelatex** — needs `ctex`) and `resume-na.tex` (English / North-America-oriented, xelatex or pdflatex). They share layout, macros, and section order.

## Identity / education tokens (auto-filled)

Export substitutes these `<<TOKEN>>` placeholders directly:

| Token | Schema field |
|---|---|
| `<<NAME>>` | basics.name |
| `<<EMAIL>>` | basics.email |
| `<<PHONE>>` | basics.phone |
| `<<GITHUB_USERNAME>>` | basics.githubUsername |
| `<<LANGUAGE_SCORE>>` | basics.languageScore |
| `<<SCHOOL_MASTER>>` | education[level=master].institution |
| `<<GPA_MASTER>>` | education[level=master].score |
| `<<DATE_MASTER>>` | education[level=master].date |
| `<<SCHOOL_BACHELOR>>` | education[level=bachelor].institution |
| `<<GPA_BACHELOR>>` | education[level=bachelor].score |
| `<<DATE_BACHELOR>>` | education[level=bachelor].date |
| `<<VAR>>` | Generic placeholder referenced in the templates' usage comments — stands for "any value the user is filling in by hand". Not auto-substituted by Export; left as a documentation marker. |

## Project / experience / skills body (generated for paste)

The templates ship with a **fictional example** project block (clearly marked). Export does NOT auto-replace it; instead it generates a ready-to-paste block in the templates' own macros for you to swap in:

- Project/work entry:
  `\resumeProjectHeading{<name>}{<tech stack, joined by " / ">}{<date>}`
  followed by one `\resumeItem{...}` per bullet (already in CN-STAR or NA-X-Y-Z style from the prior mode).
- Skill group: one `\item \small ...` line per the template's skill style.

## Providing your own template

Ask Export to use a custom file: *"export with template `<path>`"*. Your template must use the same `<<TOKEN>>` names above for auto-fill; Export will still emit the macro-formatted body for you to paste. Leave `<<CONFIRM: …>>` markers for any value Export cannot verify — fill those yourself.
