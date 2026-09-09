# LaTeX Template Guide — Export Contract v3

The built-in `resume-cn.tex` and `resume-na.tex` templates compile with **XeLaTeX only**. Both contain five auto-filled header tokens:

| Token | Schema field |
|---|---|
| `<<NAME>>` | `basics.name` |
| `<<SCHOOL>>` | First non-empty `education[].institution` |
| `<<EMAIL>>` | `basics.email` |
| `<<PHONE>>` | `basics.phone` |
| `<<GITHUB_USERNAME>>` | `basics.githubUsername` |

All other resume content is generated from the schema into these paired comment regions, exactly once per template:

```tex
% RESUME-SKILL:BEGIN EDUCATION
% RESUME-SKILL:END EDUCATION
% RESUME-SKILL:BEGIN WORK
% RESUME-SKILL:END WORK
% RESUME-SKILL:BEGIN PROJECTS
% RESUME-SKILL:END PROJECTS
% RESUME-SKILL:BEGIN SKILLS
% RESUME-SKILL:END SKILLS
```

Education is generated from every `education[]` entry, so a bachelor-only, master, PhD, or non-CS resume never inherits fictional degree or course text. `work[]` and `projects[]` are rendered into separate Internship Experience and Personal Projects sections. NA skills never render a CET or language-score line.

## Custom templates

Automatic replacement requires all four region pairs and the built-in macro interface: `\resumeEduSubheading`, `\resumeEduLine`, `\resumeProjectHeading`, and `\resumeItem`. A custom template without them receives copy-ready snippets only; do not promise automatic replacement.
