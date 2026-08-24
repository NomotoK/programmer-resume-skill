# LaTeX Template Guide — Export Contract v2

The built-in `resume-cn.tex` and `resume-na.tex` templates compile with **XeLaTeX only**. Both contain four auto-filled header tokens:

| Token | Schema field |
|---|---|
| `<<NAME>>` | `basics.name` |
| `<<EMAIL>>` | `basics.email` |
| `<<PHONE>>` | `basics.phone` |
| `<<GITHUB_USERNAME>>` | `basics.githubUsername` |

All other resume content is generated from the schema into these paired comment regions, exactly once per template:

```tex
% RESUME-SKILL:BEGIN EDUCATION
% RESUME-SKILL:END EDUCATION
% RESUME-SKILL:BEGIN EXPERIENCE
% RESUME-SKILL:END EXPERIENCE
% RESUME-SKILL:BEGIN SKILLS
% RESUME-SKILL:END SKILLS
```

Education is generated from every `education[]` entry, so a bachelor-only, master, PhD, or non-CS resume never inherits fictional degree or course text. NA skills never render a CET or language-score line.

## Custom templates

Automatic replacement requires all three region pairs and the built-in macro interface: `\resumeEduSubheading`, `\resumeEduLine`, `\resumeProjectHeading`, and `\resumeItem`. A custom template without them receives copy-ready snippets only; do not promise automatic replacement.
