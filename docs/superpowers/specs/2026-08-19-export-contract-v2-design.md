# Export Contract v2 Design

## Goal

Make every built-in export structurally correct for the supplied resume data, reproducible with XeLaTeX, and guarded against template-contract regressions.

## Decision

Built-in templates use four stable header tokens only:

`<<NAME>>`, `<<EMAIL>>`, `<<PHONE>>`, and `<<GITHUB_USERNAME>>`.

All variable-length or conditional content is generated inside named comment regions:

```tex
% RESUME-SKILL:BEGIN EDUCATION
% RESUME-SKILL:END EDUCATION
```

The required regions are `EDUCATION`, `EXPERIENCE`, and `SKILLS`. The Export mode emits replacement content for each region. It does not use tokens for education, language scores, projects, work history, or skills.

## Rendering rules

- `education[]` renders every supplied degree using its `institution`, `studyType`, `area`, `score`, `date`, `rank`, and `courses` values when present. It never hard-codes a degree, major, or course list.
- `work[]` and `projects[]` jointly render inside `EXPERIENCE`; empty entries and empty sections are omitted.
- CN skills can include `tier`; NA skills are grouped by `category` and never include a language-score/CET line.
- Values are escaped once at render time using the existing LaTeX escaping rules.
- The built-in templates require **XeLaTeX**. `pdflatex` is not advertised because the templates use `fontspec`.

## Custom templates

Automatic section replacement is supported only when a custom template supplies all three region pairs and compatible `\resumeEduSubheading`, `\resumeEduLine`, `\resumeProjectHeading`, and `\resumeItem` macros. Other templates receive copy-ready snippets only; the skill must say that automatic replacement is unavailable.

## Validation and test boundary

`scripts/validate.py` is the structural gate. It must reject missing required template assets, unsupported header tokens, missing/duplicate/unbalanced regions, and HTML templates that lack the declared semantic/print contract.

Pytest is the supported test runner and is declared in `requirements-dev.txt`. A deterministic smoke renderer creates CN and NA fixture `.tex` files and compiles them with XeLaTeX when `/Library/TeX/texbin/xelatex` (or `xelatex` on PATH) is available. The smoke renderer is verification infrastructure, not an end-user resume generator.

## Compatibility

This is a deliberate breaking change from the former 11-token contract. The repository documentation, examples, validator, and templates move together; no compatibility shim is retained because it would preserve the ambiguous conditional-rendering path.
