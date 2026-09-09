# LaTeX Template Guide — Export Contract v3

The built-in `resume-cn.tex` and `resume-na.tex` templates compile with **XeLaTeX only**. Both contain four auto-filled header tokens:

From this directory, either of these commands selects the correct engine:

```sh
latexmk resume-cn.tex
latexmk resume-na.tex
```

The bundled `latexmkrc` sets XeLaTeX as the default, and each template also contains a `% !TeX program = xelatex` editor directive. From another working directory, use `latexmk -xelatex path/to/resume-cn.tex` (or `resume-na.tex`).

| Token | Schema field |
|---|---|
| `<<NAME>>` | `basics.name` |
| `<<EMAIL>>` | `basics.email` |
| `<<PHONE>>` | `basics.phone` |
| `<<GITHUB>>` | `basics.githubUsername` |

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

Automatic replacement requires all four region pairs and the built-in macro interface: `\resumeEduSubheading`, `\resumeEduLine`, `\resumeProjectHeading`, `\resumeItem`, and `\resumeSkill`. A custom template without them receives copy-ready snippets only; do not promise automatic replacement.
