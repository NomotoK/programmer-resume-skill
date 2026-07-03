# Programmer Resume Skill Suite

A cross-platform (Claude Code + OpenAI Codex) plugin of skills for **software-engineer job-search résumés**.

## Skills

| Skill | What it does |
|---|---|
| `resume-optimizer` | Polish, review, JD-match, CN<->NA localization, and export (LaTeX-first). |
| `resume-from-code` | Read a project repo + your git history, surface technical highlights, draft a resume project section. |
| `resume-mock-interview` | Turn resume projects into dozens of layered interview questions + talking points. |

## Install

**Claude Code:** `/plugin` → add this repo as a marketplace/plugin, or copy `skills/*` into your skills directory.
**OpenAI Codex:** install as a plugin (`.codex-plugin/plugin.json`) or copy `skills/*` into `~/.codex/skills/`.

## Usage

Ask naturally: *"Polish my resume"*, *"Generate a project section from this repo"*, *"Mock-interview my resume projects"*, *"Localize for North America"*, *"Tailor to this JD"*.

See `examples/` and `docs/superpowers/specs/` for details.

## Output

LaTeX-first (supply your own `.tex` template via `templates/latex/`), with Markdown/HTML/JSON alternatives.

## License

MIT
