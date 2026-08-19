# Export Contract v2 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the ambiguous 11-token export contract with marker-based generated sections, make XeLaTeX verification reproducible, and keep all documentation and validation synchronized.

**Architecture:** Built-in templates retain four header tokens and add three named comment regions. The skill renders education, experience, and skills from the JSON schema into those regions. The structural validator owns the template contract; a smoke renderer validates that fixture output compiles with XeLaTeX.

**Tech Stack:** Markdown, LaTeX/XeLaTeX, JSON Schema, Python 3.9, pytest.

**Spec:** `docs/superpowers/specs/2026-08-19-export-contract-v2-design.md`

## Global Constraints

- Built-in templates support XeLaTeX only; do not claim `pdflatex` support.
- The only built-in tokens are `NAME`, `EMAIL`, `PHONE`, and `GITHUB_USERNAME`.
- Every built-in template contains exactly one paired region for `EDUCATION`, `EXPERIENCE`, and `SKILLS`.
- Generated values retain the authenticity rule and are escaped exactly once for LaTeX.
- Custom templates without every required region and macro are snippet-only.
- `python3 -m pytest tests/ -q`, `python3 scripts/validate.py`, and the XeLaTeX smoke command are release gates.

---

### Task 1: Establish the test and dependency baseline

**Files:**
- Create: `requirements-dev.txt`
- Modify: `tests/test_validate.py`
- Create: `tests/fixtures/minimal-cn.json`
- Create: `tests/fixtures/minimal-na.json`

**Interfaces:**
- `requirements-dev.txt` supplies `pytest>=8,<9`.
- Fixtures contain a bachelor-only, non-CS education record; the NA fixture has no language score.

- [ ] Add tests that expect v2 region validation and required template assets; run pytest and confirm they fail because v1 validation lacks those checks.
- [ ] Add the minimal dependency declaration and fixture inputs.
- [ ] Commit the red tests and baseline files.

### Task 2: Implement the template-contract validator

**Files:**
- Modify: `scripts/validate.py`
- Modify: `tests/test_validate.py`

**Interfaces:**
- `validate(root: Path = DEFAULT_ROOT) -> list[str]` remains stable.
- Module constants define the four header tokens and three region names.

- [ ] Implement exact header-token validation, required asset checks, balanced/exactly-once region checks, and HTML semantic/print checks.
- [ ] Run the focused pytest cases and confirm green.
- [ ] Commit the validator and tests.

### Task 3: Convert the schema, templates, and export instructions to v2

**Files:**
- Modify: `templates/json/resume.schema.json`
- Modify: `templates/latex/resume-cn.tex`
- Modify: `templates/latex/resume-na.tex`
- Modify: `templates/latex/TEMPLATE_GUIDE.md`
- Modify: `templates/html/resume.html`
- Modify: `templates/markdown/resume.md`
- Modify: `skills/resume-optimizer/SKILL.md`
- Modify: `skills/resume-optimizer/references/export-formats.md`

**Interfaces:**
- `education[]` is rendered as a generated region rather than an identity-token map.
- The Export mode states `xelatex` as the sole built-in compiler and exposes the three replacement regions.

- [ ] Update the docs and templates together so no source describes the old 11-token protocol.
- [ ] Ensure NA has no fixed language-score row and neither template hard-codes degree, major, or courses.
- [ ] Run the validator and commit the coherent v2 contract.

### Task 4: Add deterministic XeLaTeX smoke verification

**Files:**
- Create: `scripts/render_smoke.py`
- Create: `tests/test_render_smoke.py`
- Modify: `requirements-dev.txt`

**Interfaces:**
- `render_fixture(template: Path, data: dict, market: str) -> str` substitutes header tokens and all three regions for fixture verification.
- `find_xelatex() -> Path | None` searches `/Library/TeX/texbin/xelatex` before `PATH`.

- [ ] Write failing tests for bachelor-only/non-CS education, NA language omission, and LaTeX special-character escaping.
- [ ] Implement the smallest smoke renderer and fixture compilation command.
- [ ] Run unit tests, validator, and both XeLaTeX fixture compilations; commit the verifier.

### Task 5: Synchronize public documentation and examples

**Files:**
- Modify: `README.md`
- Modify: `README.zh-CN.md`
- Modify: `examples/README.md`
- Modify: `docs/superpowers/plans/2026-07-03-resume-skill-suite.md`

**Interfaces:**
- Public documentation names XeLaTeX only, explains marker compatibility, and does not advertise the old token count.

- [ ] Update public instructions and the original plan's completion status.
- [ ] Search for `pdflatex`, `11 token`, `LANGUAGE_SCORE`, and `<<VAR>>`; retain none except historical prose explicitly labelled obsolete.
- [ ] Run all release gates and commit the documentation pass.
