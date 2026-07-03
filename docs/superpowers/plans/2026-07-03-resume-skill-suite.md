# Programmer Resume Skill Suite — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Expand the single `programmer-resume-optimizer` skill into a cross-platform (Claude Code + OpenAI Codex) plugin suite — 1 main skill (`resume-optimizer`, 5 modes) + 2 sub-skills (`resume-from-code`, `resume-mock-interview`) — covering polish / code→resume / review / mock-interview / CN↔NA localization / JD-matching, with LaTeX-first export.

**Architecture:** A plugin whose `skills/` directory is the single source of truth, surfaced identically by `.claude-plugin/plugin.json` (Claude Code) and `.codex-plugin/plugin.json` (Codex). All SKILL.md files use platform-neutral action language. A `scripts/validate.py` harness + pytest enforce the structural contracts (frontmatter, reference resolution, manifest consistency, sub-skill self-containment, template-variable consistency) and is run after every task.

**Tech Stack:** Markdown (SKILL.md + references), JSON (plugin manifests, JSON Resume schema), LaTeX/HTML (templates), Python 3 (validator), pytest (tests). No runtime code; the "program" is instruction files an AI agent follows.

## Global Constraints

Copied verbatim from the approved spec. Every task's requirements implicitly include these:

- **Platform-neutral phrasing:** SKILL.md prose describes actions ("read a file", "run a git/gh command", "search file contents"), never hard-coded Claude-only or Codex-only tool names.
- **Sub-skill self-containment:** Sub-skill SKILL.md files must NOT reference `../` (no cross-directory reference into the main skill). Each carries only the rule fragments it needs.
- **File-name ASCII rule:** All paths are ASCII (no CJK in filenames). The 6 existing `简历指南*.md` files are renamed to `guide-N-<slug>.md`; their *contents* stay Chinese.
- **LaTeX placeholder convention:** Template placeholders use `<<UPPER_CASE_VAR>>` (e.g. `<<NAME>>`). LaTeX-safe; trivial to find/replace.
- **Canonical placeholder set** (shared contract between `resume.schema.json`, the `<<VAR>>` templates, and `TEMPLATE_GUIDE.md`):
  `<<NAME>>`, `<<ROLE_OR_TITLE>>`, `<<CONTACT>>`, `<<SUMMARY>>`, `<<SKILLS>>`, `<<EXPERIENCE>>`, `<<PROJECTS>>`, `<<EDUCATION>>`, `<<AWARDS>>`.
- **Authenticity red line (all capabilities):** Never fabricate degree / years of experience / employer identity / unverifiable metrics. Packaging wording is allowed; every highlight must be defensible in interview. `resume-from-code` highlights must have code evidence. Unverifiable quantification becomes a placeholder the user confirms — never invented.
- **Output default language:** Compact, copy-ready Chinese unless the user requests another language or selects NA localization.
- **Validator command:** `python3 scripts/validate.py` must exit 0 (prints `OK: …`). Tests: `python3 -m pytest tests/ -q`.
- **Branch:** all work on branch `design/resume-skill-suite` (already checked out). Commit after every task.

## File Map

| File | Responsibility | Task |
|---|---|---|
| `skills/resume-optimizer/SKILL.md` | Main skill: 5-mode hub (Polish/Review/JD-Match/Localize/Export). Migrated first (transitional), rewritten to 5-mode later. | T1 migrate, T6 rewrite |
| `skills/resume-optimizer/references/resume-rules.md` | Core rules (structure, ratios, STAR, 14 dimensions, authenticity, checklists). Enhanced with CN/NA + JD + export hooks. | T1 migrate, T10 enhance |
| `skills/resume-optimizer/references/guide-1..6-*.md` | liyupi source material (6 files, renamed to ASCII, content unchanged). | T1 migrate |
| `skills/resume-optimizer/references/cn-na-market.md` | CN↔NA resume-market differences + transformation rules (distilled from research). | T7 |
| `skills/resume-optimizer/references/jd-matching.md` | JD parsing method + role-bias strategies (backend/AI-Agent/algorithm). | T8 |
| `skills/resume-optimizer/references/export-formats.md` | How each format (LaTeX/MD/HTML/JSON) is produced; variable conventions. | T9 |
| `skills/resume-optimizer/references/resume.schema.json` | Canonical structured intermediate representation (JSON Resume-compatible + tech extensions) consumed by Export mode and templates. **NOTE: lives under `templates/json/`** (see below) — referenced as such from Export mode. | T5 |
| `skills/resume-from-code/SKILL.md` + `references/code-mining.md` | Sub-skill: code→project-experience. | T12 |
| `skills/resume-mock-interview/SKILL.md` + `references/interview-bank.md` | Sub-skill: resume→interview questions. | T13 |
| `.claude-plugin/plugin.json` | Claude Code plugin manifest (metadata; auto-discovers `skills/`). | T2 |
| `.codex-plugin/plugin.json` | Codex plugin manifest (metadata; same `skills/`). | T2 |
| `agents/openai.yaml` | Codex `interface` declaration, updated to describe the suite. | T4 |
| `templates/json/resume.schema.json` | The canonical schema (moved here from the row above — single home). | T5 |
| `templates/latex/resume-cn.tex.placeholder` | Empty CN LaTeX template with `<<VAR>>` slots. | T11 |
| `templates/latex/resume-na.tex.placeholder` | Empty NA LaTeX template with `<<VAR>>` slots. | T11 |
| `templates/latex/TEMPLATE_GUIDE.md` | Documents the `<<VAR>>` set + how to supply your own template. | T11 |
| `templates/html/resume.html` | Single-page printable HTML skeleton. | T11 |
| `templates/markdown/resume.md` | Markdown resume skeleton. | T11 |
| `scripts/validate.py` | Structural validator (frontmatter, refs, manifests, self-containment, template vars). | T3 |
| `tests/test_validate.py` | pytest tests for the validator (fixtures exercising each check + failures). | T3 |
| `examples/` | Sanitized input resume + sample outputs per capability. | T14 |
| `README.md` / `README.zh-CN.md` | OSS facade (EN + ZH). Skeleton in T4, finalized in T15. | T4, T15 |

> The schema lives at `templates/json/resume.schema.json` (single home; Export mode + templates both reference it there). The File Map row naming it under `resume-optimizer/references/` is a cross-reference only.

---

## Phase A — Scaffold & Migrate

### Task 1: Migrate main skill into `skills/resume-optimizer/`

Move the existing root skill + references into the plugin layout, renaming the 6 Chinese guides to ASCII filenames (contents unchanged). The migrated `SKILL.md` stays valid as a transitional single skill (its 4-mode content is rewritten to 5 modes in Task 6).

**Files:**
- Move: `SKILL.md` → `skills/resume-optimizer/SKILL.md`
- Move: `references/resume-rules.md` → `skills/resume-optimizer/references/resume-rules.md`
- Move+rename (content unchanged):
  - `references/简历指南 1、基本写法.md` → `skills/resume-optimizer/references/guide-1-basics.md`
  - `references/简历指南 2、简历优化.md` → `skills/resume-optimizer/references/guide-2-optimization.md`
  - `references/简历指南 3、问题和建议汇总.md` → `skills/resume-optimizer/references/guide-3-common-issues.md`
  - `references/简历指南 4、优秀简历参考.md` → `skills/resume-optimizer/references/guide-4-good-examples.md`
  - `references/简历指南 5、项目真实性优化.md` → `skills/resume-optimizer/references/guide-5-authenticity.md`
  - `references/简历指南 6、项目亮点增加.md` → `skills/resume-optimizer/references/guide-6-highlights.md`
- Delete now-empty `references/` and root `SKILL.md`.

**Interfaces:**
- Consumes: existing root `SKILL.md`, `references/resume-rules.md`, `references/简历指南*.md`.
- Produces: `skills/resume-optimizer/SKILL.md` whose internal link `references/resume-rules.md` still resolves (same relative dir).

- [ ] **Step 1: Create the directory and move files with `git mv`**

```bash
mkdir -p skills/resume-optimizer/references
git mv SKILL.md skills/resume-optimizer/SKILL.md
git mv references/resume-rules.md skills/resume-optimizer/references/resume-rules.md
git mv "references/简历指南 1、基本写法.md"        skills/resume-optimizer/references/guide-1-basics.md
git mv "references/简历指南 2、简历优化.md"        skills/resume-optimizer/references/guide-2-optimization.md
git mv "references/简历指南 3、问题和建议汇总.md"   skills/resume-optimizer/references/guide-3-common-issues.md
git mv "references/简历指南 4、优秀简历参考.md"     skills/resume-optimizer/references/guide-4-good-examples.md
git mv "references/简历指南 5、项目真实性优化.md"   skills/resume-optimizer/references/guide-5-authenticity.md
git mv "references/简历指南 6、项目亮点增加.md"     skills/resume-optimizer/references/guide-6-highlights.md
rmdir references 2>/dev/null || true
```

- [ ] **Step 2: Verify the link inside SKILL.md still resolves**

The migrated `SKILL.md` contains `Read [resume-rules.md](references/resume-rules.md)`. After the move it is at `skills/resume-optimizer/SKILL.md`, and `resume-rules.md` is at `skills/resume-optimizer/references/resume-rules.md` — the relative path is unchanged.

Run: `test -f skills/resume-optimizer/references/resume-rules.md && grep -q "references/resume-rules.md" skills/resume-optimizer/SKILL.md && echo OK`
Expected: `OK`

- [ ] **Step 3: Verify structure + no stray files**

Run: `find skills -type f | sort`
Expected:
```
skills/resume-optimizer/SKILL.md
skills/resume-optimizer/references/guide-1-basics.md
skills/resume-optimizer/references/guide-2-optimization.md
skills/resume-optimizer/references/guide-3-common-issues.md
skills/resume-optimizer/references/guide-4-good-examples.md
skills/resume-optimizer/references/guide-5-authenticity.md
skills/resume-optimizer/references/guide-6-highlights.md
skills/resume-optimizer/references/resume-rules.md
```

Run: `ls SKILL.md references 2>&1 | head`
Expected: both report `No such file or directory` (root skill + references gone).

- [ ] **Step 4: Commit**

```bash
git add -A
git commit -m "refactor: migrate root skill into skills/resume-optimizer/ (ASCII guide names)"
```

---

### Task 2: Create the dual-platform plugin manifests

Both manifests are metadata only; Claude Code and Codex auto-discover `skills/`. Mirror the superpowers convention.

**Files:**
- Create: `.claude-plugin/plugin.json`
- Create: `.codex-plugin/plugin.json`

**Interfaces:**
- Produces: two valid JSON manifests with `name`, `description`. (Validator Task 3 checks these.)

- [ ] **Step 1: Write `.claude-plugin/plugin.json`**

```json
{
  "name": "programmer-resume-skill",
  "description": "Cross-platform skill suite for software-engineer job-search résumés: polish, code-to-resume, review, mock interview, CN<->NA localization, and JD matching, with LaTeX-first export.",
  "version": "0.1.0",
  "author": {
    "name": "NomotoK"
  },
  "homepage": "https://github.com/NomotoK/programmer-resume-skill",
  "repository": "https://github.com/NomotoK/programmer-resume-skill",
  "license": "MIT",
  "keywords": ["resume", "cv", "career", "skills", "interview", "software-engineer"]
}
```

- [ ] **Step 2: Write `.codex-plugin/plugin.json`** (same metadata; Codex reads this to register the plugin and its `skills/`)

```json
{
  "name": "programmer-resume-skill",
  "description": "Cross-platform skill suite for software-engineer job-search résumés: polish, code-to-resume, review, mock interview, CN<->NA localization, and JD matching, with LaTeX-first export.",
  "version": "0.1.0",
  "author": "NomotoK",
  "homepage": "https://github.com/NomotoK/programmer-resume-skill",
  "repository": "https://github.com/NomotoK/programmer-resume-skill",
  "license": "MIT",
  "keywords": ["resume", "cv", "career", "skills", "interview", "software-engineer"]
}
```

- [ ] **Step 3: Verify both parse as JSON and have name+description**

Run: `python3 -c "import json; [json.load(open(f)) for f in ['.claude-plugin/plugin.json','.codex-plugin/plugin.json']]; print('OK')"`
Expected: `OK`

- [ ] **Step 4: Commit**

```bash
git add .claude-plugin .codex-plugin
git commit -m "feat: add .claude-plugin and .codex-plugin manifests"
```

---

### Task 3: Build the validation harness (`scripts/validate.py` + tests)

TDD: write pytest tests (with a fixture plugin tree) first, then the validator. The validator is the red/green spine for every later task.

**Files:**
- Create: `scripts/validate.py`
- Create: `tests/test_validate.py`

**Interfaces:**
- Produces: `validate(root=None) -> list[str]` returning a list of error strings (empty = valid). `main()` calls `validate()` on the repo root and exits 1 if any errors. All later tasks run `python3 scripts/validate.py`.

- [ ] **Step 1: Write the failing tests**

`tests/test_validate.py`:

```python
import json, textwrap
from pathlib import Path
from scripts.validate import validate

VALID_SKILL = """---
name: demo
description: Use when X to do Y.
---
# Demo
See [rules](references/rules.md).
"""

def _write_tree(root: Path, files: dict):
    for rel, content in files.items():
        p = root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding="utf-8")

def _base_tree():
    return {
        ".claude-plugin/plugin.json": json.dumps({"name": "demo", "description": "d"}),
        ".codex-plugin/plugin.json":  json.dumps({"name": "demo", "description": "d"}),
        "skills/demo/SKILL.md": VALID_SKILL,
        "skills/demo/references/rules.md": "# rules\n",
    }

def test_valid_tree_has_no_errors(tmp_path):
    _write_tree(tmp_path, _base_tree())
    assert validate(tmp_path) == []

def test_missing_frontmatter_fails(tmp_path):
    files = _base_tree(); files["skills/demo/SKILL.md"] = "# Demo\nno frontmatter\n"
    _write_tree(tmp_path, files)
    errs = validate(tmp_path)
    assert any("frontmatter" in e for e in errs)

def test_name_mismatch_fails(tmp_path):
    files = _base_tree()
    files["skills/demo/SKILL.md"] = VALID_SKILL.replace("name: demo", "name: other")
    _write_tree(tmp_path, files)
    errs = validate(tmp_path)
    assert any("name 'other'" in e for e in errs)

def test_empty_description_fails(tmp_path):
    files = _base_tree()
    files["skills/demo/SKILL.md"] = VALID_SKILL.replace("description: Use when X to do Y.", "description:")
    _write_tree(tmp_path, files)
    errs = validate(tmp_path)
    assert any("empty description" in e for e in errs)

def test_missing_reference_fails(tmp_path):
    files = _base_tree()
    files["skills/demo/SKILL.md"] = "See [x](references/missing.md).\n"  # but no frontmatter -> add it
    files["skills/demo/SKILL.md"] = "---\nname: demo\ndescription: d\n---\nSee [x](references/missing.md).\n"
    _write_tree(tmp_path, files)
    errs = validate(tmp_path)
    assert any("references missing file 'references/missing.md'" in e for e in errs)

def test_parent_ref_fails(tmp_path):
    files = _base_tree()
    files["skills/demo/SKILL.md"] = "---\nname: demo\ndescription: d\n---\nSee ../other/rules.md\n"
    _write_tree(tmp_path, files)
    errs = validate(tmp_path)
    assert any("../" in e and "self-containment" in e for e in errs)

def test_bad_manifest_json_fails(tmp_path):
    files = _base_tree(); files[".claude-plugin/plugin.json"] = "{not json"
    _write_tree(tmp_path, files)
    errs = validate(tmp_path)
    assert any("invalid JSON" in e for e in errs)

def test_undocumented_template_var_fails(tmp_path):
    files = _base_tree()
    files["templates/latex/TEMPLATE_GUIDE.md"] = "Tokens: <<NAME>>"
    files["templates/latex/resume-na.tex.placeholder"] = "<<NAME>> <<SECRET>>"
    _write_tree(tmp_path, files)
    errs = validate(tmp_path)
    assert any("<<SECRET>>" in e and "TEMPLATE_GUIDE" in e for e in errs)
```

- [ ] **Step 2: Run tests to verify they fail (module not found)**

Run: `python3 -m pytest tests/test_validate.py -q`
Expected: FAIL — collection error / `ModuleNotFoundError: No module named 'scripts.validate'`.

- [ ] **Step 3: Write `scripts/validate.py`**

```python
#!/usr/bin/env python3
"""Validate the resume-skill plugin: structure + content contracts.

Exit code 0 (prints OK summary) when valid; 1 with an error list otherwise.
Run: python3 scripts/validate.py   |   tests call validate(root).
"""
import json, re, sys
from pathlib import Path

DEFAULT_ROOT = Path(__file__).resolve().parent.parent

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
REF_LINK_RE = re.compile(r"references/[\w./\-]+\.md")
PLACEHOLDER_RE = re.compile(r"<<([A-Z_]+)>>")
KV_RE = re.compile(r"^(\w+):\s*(.*)$")


def _parse_frontmatter(text):
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None, text
    fm = {}
    for line in m.group(1).splitlines():
        kv = KV_RE.match(line)
        if kv:
            fm[kv.group(1)] = kv.group(2).strip().strip('"').strip("'")
    return fm, text[m.end():]


def _load_json(path):
    try:
        return json.loads(path.read_text(encoding="utf-8")), None
    except Exception as e:  # noqa: BLE001
        return None, f"{path.relative_to(DEFAULT_ROOT) if path.is_absolute() else path}: invalid JSON ({e})"


def validate(root: Path = DEFAULT_ROOT):
    root = Path(root)
    errors = []

    def err(msg):
        errors.append(msg)

    # 1. Skill directories + frontmatter
    skills_dir = root / "skills"
    skill_dirs = []
    if not skills_dir.is_dir():
        err("skills/ directory missing")
    else:
        skill_dirs = sorted(d for d in skills_dir.iterdir() if d.is_dir())
        if not skill_dirs:
            err("no skill subdirectories under skills/")
    for d in skill_dirs:
        sm = d / "SKILL.md"
        if not sm.is_file():
            err(f"{d.name}: missing SKILL.md")
            continue
        fm, _ = _parse_frontmatter(sm.read_text(encoding="utf-8"))
        if fm is None:
            err(f"{d.name}/SKILL.md: missing YAML frontmatter")
            continue
        if fm.get("name") != d.name:
            err(f"{d.name}/SKILL.md: frontmatter name '{fm.get('name')}' != dir name '{d.name}'")
        if not fm.get("description"):
            err(f"{d.name}/SKILL.md: empty description")

    # 2. References resolve within each skill dir
    for d in skill_dirs:
        sm = d / "SKILL.md"
        if not sm.is_file():
            continue
        body = sm.read_text(encoding="utf-8")
        for m in REF_LINK_RE.finditer(body):
            rel = m.group(0)
            if not (d / rel).is_file():
                err(f"{d.name}/SKILL.md: references missing file '{rel}'")

    # 3. Sub-skill self-containment: no '../' references
    for d in skill_dirs:
        sm = d / "SKILL.md"
        if sm.is_file() and "../" in sm.read_text(encoding="utf-8"):
            err(f"{d.name}/SKILL.md: references parent path '../' (violates sub-skill self-containment)")

    # 4. Manifests valid JSON with name+description
    for rel in (".claude-plugin/plugin.json", ".codex-plugin/plugin.json"):
        p = root / rel
        if not p.is_file():
            err(f"missing manifest {rel}")
            continue
        data, e = _load_json(p)
        if e:
            err(e)
            continue
        if not data.get("name"):
            err(f"{rel}: missing 'name'")
        if not data.get("description"):
            err(f"{rel}: missing 'description'")

    # 5. Template placeholder tokens documented in TEMPLATE_GUIDE
    guide = root / "templates/latex/TEMPLATE_GUIDE.md"
    if guide.is_file():
        declared = set(PLACEHOLDER_RE.findall(guide.read_text(encoding="utf-8")))
        latex_dir = root / "templates/latex"
        for tex_name in ("resume-cn.tex.placeholder", "resume-na.tex.placeholder"):
            tex = latex_dir / tex_name
            if not tex.is_file():
                continue
            used = set(PLACEHOLDER_RE.findall(tex.read_text(encoding="utf-8")))
            for v in sorted(used - declared):
                err(f"{tex_name}: placeholder <<{v}>> not documented in TEMPLATE_GUIDE.md")

    return errors


def main():
    errors = validate()
    if errors:
        print("VALIDATION FAILED:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    n = len([d for d in (DEFAULT_ROOT / "skills").iterdir() if d.is_dir()]) if (DEFAULT_ROOT / "skills").is_dir() else 0
    print(f"OK: {n} skill(s), manifests valid, references resolve, template vars documented.")


if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python3 -m pytest tests/test_validate.py -q`
Expected: `8 passed`

- [ ] **Step 5: Run the validator on the real repo**

Run: `python3 scripts/validate.py`
Expected: `OK: 1 skill(s), manifests valid, references resolve, template vars documented.`

- [ ] **Step 6: Commit**

```bash
git add scripts/validate.py tests/test_validate.py
git commit -m "feat: add validate.py structural harness + pytest tests"
```

---

### Task 4: Update `agents/openai.yaml` + README skeletons

Update the Codex interface declaration to describe the suite; add README skeletons (finalized in Task 15).

**Files:**
- Modify: `agents/openai.yaml`
- Create: `README.md`
- Create: `README.zh-CN.md`

**Interfaces:**
- Produces: READMEs that document the 3 skills + install + examples pointer.

- [ ] **Step 1: Rewrite `agents/openai.yaml`**

```yaml
interface:
  display_name: "Programmer Resume Skill Suite"
  short_description: "Polish, review, code-to-resume, mock-interview, CN<->NA localize, JD-match for dev résumés."
  default_prompt: "Use the programmer-resume skills to optimize my developer résumé for a backend role with STAR bullets and quantified outcomes, then export a LaTeX CN version."
```

- [ ] **Step 2: Write `README.md` (skeleton)**

```markdown
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
```

- [ ] **Step 3: Write `README.zh-CN.md` (skeleton)**

```markdown
# 程序员简历技能套件

一套跨平台（Claude Code + OpenAI Codex）的插件，面向**计算机/软件技术岗求职简历**。

## 技能

| 技能 | 功能 |
|---|---|
| `resume-optimizer` | 简历润色、点评、JD 匹配、中英（中国↔北美）适配、导出（LaTeX 优先）。 |
| `resume-from-code` | 读取项目仓库 + 你的 git 历史，挖掘技术亮点，生成一段简历项目经历。 |
| `resume-mock-interview` | 把简历里的项目经历转成数十道分层面试题 + 参考要点。 |

## 安装

**Claude Code：** `/plugin` 添加本仓库，或将 `skills/*` 复制到你的 skills 目录。
**OpenAI Codex：** 作为插件安装（`.codex-plugin/plugin.json`），或将 `skills/*` 复制到 `~/.codex/skills/`。

## 使用

直接用自然语言：*"润色我的简历"*、*"从这个仓库生成一段项目经历"*、*"给我的简历项目出面试题"*、*"导出适合北美的英文版"*、*"按这个 JD 调整"*。

详见 `examples/` 与 `docs/superpowers/specs/`。

## 输出

LaTeX 优先（可在 `templates/latex/` 提供自己的 `.tex` 模板），另提供 Markdown/HTML/JSON。

## License

MIT
```

- [ ] **Step 4: Verify validator still green**

Run: `python3 scripts/validate.py`
Expected: `OK: 1 skill(s), …`

- [ ] **Step 5: Commit**

```bash
git add agents/openai.yaml README.md README.zh-CN.md
git commit -m "docs: update Codex interface + add EN/ZH README skeletons"
```

---

## Phase B — Main skill `resume-optimizer` (5 modes)

### Task 5: Canonical structured schema (`templates/json/resume.schema.json`)

The shared intermediate representation that Export mode and all templates consume. JSON Resume-compatible + tech extensions.

**Files:**
- Create: `templates/json/resume.schema.json`

**Interfaces:**
- Produces: a JSON Schema document whose top-level properties map 1:1 onto the canonical `<<VAR>>` set. Export mode (Task 6) renders each property into the matching placeholder.

- [ ] **Step 1: Write the schema**

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://nomotok.github.io/programmer-resume-skill/resume.schema.json",
  "title": "Tech Resume (JSON Resume-compatible)",
  "type": "object",
  "required": ["basics"],
  "properties": {
    "basics": {
      "type": "object",
      "description": "Maps to <<NAME>>, <<ROLE_OR_TITLE>>, <<CONTACT>>, <<SUMMARY>>.",
      "properties": {
        "name": {"type": "string"},
        "roleOrTitle": {"type": "string"},
        "targetMarket": {"type": "string", "enum": ["CN", "NA"]},
        "phone": {"type": "string"},
        "email": {"type": "string"},
        "location": {"type": "string"},
        "wechat": {"type": "string"},
        "linkedin": {"type": "string"},
        "github": {"type": "string"},
        "website": {"type": "string"},
        "workAuthorization": {"type": "string"},
        "summary": {"type": "string"}
      }
    },
    "skills": {
      "type": "array",
      "description": "Maps to <<SKILLS>>. CN: tiered (了解/熟悉/熟练掌握). NA: categorized, no tiers.",
      "items": {"type": "object", "properties": {
        "category": {"type": "string"},
        "items": {"type": "array", "items": {"type": "string"}},
        "tier": {"type": "string", "description": "CN only: 了解|熟悉|熟练掌握|精通(校招禁用)"}
      }}
    },
    "work": {
      "type": "array",
      "description": "Maps to <<EXPERIENCE>>. NA: X-Y-Z action verbs. CN: STAR + 技术栈 line.",
      "items": {"type": "object", "properties": {
        "company": {"type": "string"},
        "position": {"type": "string"},
        "startDate": {"type": "string"},
        "endDate": {"type": "string"},
        "techStack": {"type": "array", "items": {"type": "string"}},
        "highlights": {"type": "array", "items": {"type": "string"}}
      }}
    },
    "projects": {
      "type": "array",
      "description": "Maps to <<PROJECTS>>.",
      "items": {"type": "object", "properties": {
        "name": {"type": "string"},
        "description": {"type": "string"},
        "techStack": {"type": "array", "items": {"type": "string"}},
        "url": {"type": "string"},
        "highlights": {"type": "array", "items": {"type": "string"}}
      }}
    },
    "education": {
      "type": "array",
      "description": "Maps to <<EDUCATION>>.",
      "items": {"type": "object", "properties": {
        "institution": {"type": "string"},
        "area": {"type": "string"},
        "studyType": {"type": "string"},
        "startDate": {"type": "string"},
        "endDate": {"type": "string"},
        "score": {"type": "string"},
        "rank": {"type": "string", "description": "CN only, e.g. 专业排名前10%"},
        "courses": {"type": "array", "items": {"type": "string"}},
        "cet": {"type": "string", "description": "CN only, e.g. CET-6"}
      }}
    },
    "awards": {
      "type": "array",
      "description": "Maps to <<AWARDS>>.",
      "items": {"type": "object", "properties": {
        "title": {"type": "string"}, "date": {"type": "string"}, "awarder": {"type": "string"}
      }}
    }
  }
}
```

- [ ] **Step 2: Verify it parses as JSON Schema**

Run: `python3 -c "import json; s=json.load(open('templates/json/resume.schema.json')); assert s['properties']['basics']['description'].startswith('Maps to'); print('OK')"`
Expected: `OK`

- [ ] **Step 3: Verify validator still green**

Run: `python3 scripts/validate.py`
Expected: `OK: 1 skill(s), …`

- [ ] **Step 4: Commit**

```bash
git add templates/json/resume.schema.json
git commit -m "feat: add canonical tech-resume JSON schema (JSON Resume-compatible)"
```

---

### Task 6: Rewrite main skill `resume-optimizer` SKILL.md — 5 modes

The core instruction file. Platform-neutral. Defines how the agent routes intent to 5 modes and the parse→operate→export flow against the schema.

**Files:**
- Modify: `skills/resume-optimizer/SKILL.md`

**Interfaces:**
- Consumes: `templates/json/resume.schema.json` (the intermediate representation), the canonical `<<VAR>>` set.
- Produces: SKILL.md describing Polish / Review / JD-Match / Localize / Export modes and referencing `references/{resume-rules,cn-na-market,jd-matching,export-formats}.md` (these are created in Tasks 7–10; the validator resolves only the links present — so include only links to files that exist by the time this task runs. **Order note:** Tasks 7–10 must run before this task's reference links resolve, OR this task lists only `resume-rules.md` now and later tasks append their links. Simplest correct approach: this task writes SKILL.md referencing `resume-rules.md` only (exists since Task 1); Tasks 7–10 each append their own reference link. Follow the per-step instruction below.)

- [ ] **Step 1: Write the 5-mode SKILL.md (reference `resume-rules.md` only; other refs added in Tasks 7–10)**

Write the full file `skills/resume-optimizer/SKILL.md`:

````markdown
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
- LaTeX-first: fill `templates/latex/resume-{cn,na}.tex.placeholder` (or a user-supplied `--template <path>`) by substituting the canonical `<<VAR>>` tokens. Hand off the `.tex` for the user to compile with `xelatex`/`latexmk` (this skill does not compile).
- Alternatives: Markdown (`templates/markdown/resume.md`), HTML (`templates/html/resume.html`), JSON Resume (`templates/json/resume.schema.json`).

## Cross-mode rules (always apply)
- Page economy: 1 page for new grads; more only when justified. CN: avoid the 1.5-page look. NA: trim to last 10–15 yr.
- Every highlight must be defensible in interview (see the Interview Defense Checklist in resume-rules.md).
- Platform-neutral: perform file reads, git/gh commands, and searches via whatever tools the host runtime provides; do not assume a specific tool name.
````

> The links to `jd-matching.md`, `cn-na-market.md`, `export-formats.md` are written now but those files do not exist until Tasks 7–9. **Do not run the validator until Step 3** — and in Step 2 you create the first of those files so links begin resolving. To keep gates clean, this task is sequenced AFTER Tasks 7–9 in execution (see Phase B order in File Map). If executing strictly in Task-number order, run Steps 2–9 of Tasks 7, 8, 9 first, then return here to Step 3.

**Re-sequencing note (IMPORTANT):** Execute Task 6 content authoring first (this Step 1), but defer its validator + commit (Steps 2–4) until Tasks 7, 8, 9 land their reference files. Concretely:
- [ ] 6.1 Write SKILL.md (above).
- [ ] Do Tasks 7, 8, 9 (they create `cn-na-market.md`, `jd-matching.md`, `export-formats.md`).
- [ ] 6.2 Run `python3 scripts/validate.py` → expect `OK: 1 skill(s), …` (all three links now resolve).
- [ ] 6.3 `git add skills/resume-optimizer/SKILL.md && git commit -m "feat: resume-optimizer main skill — 5 modes (polish/review/jd-match/localize/export)"`.

- [ ] **Step 2: (after Tasks 7–9) Verify all reference links resolve**

Run: `python3 scripts/validate.py`
Expected: `OK: 1 skill(s), manifests valid, references resolve, template vars documented.`

- [ ] **Step 3: (after Tasks 7–9) Commit**

```bash
git add skills/resume-optimizer/SKILL.md
git commit -m "feat: resume-optimizer main skill — 5 modes (polish/review/jd-match/localize/export)"
```

---

### Task 7: `cn-na-market.md` — CN↔NA differences + transformation rules

Distill `docs/research/2026-07-02-cn-resume-norms.md`, `…-na-resume-norms.md`, and `…-cn-na-conversion-guide.md` into a skill reference (concise, actionable, sourced).

**Files:**
- Create: `skills/resume-optimizer/references/cn-na-market.md`

**Interfaces:**
- Consumes: the three research docs in `docs/research/`.
- Produces: reference consumed by the Localize mode of Task 6.

**Content outline (write each section; expand bullets into prose, citing the research docs):**
- **Header:** one-paragraph note — this reshapes, not translates; law-driven fields are conventions not optional style.
- **Quick transformation table:** copy the table from `docs/research/2026-07-02-cn-na-conversion-guide.md` (Photo, Age/personal data, Address, Work authorization, Contacts, Length, Objective, Self-eval, Education placement, GPA, Bullets, Skills, Honors, CET, Tone, File name, Channel, ATS).
- **Header fields (Dim 1):** CN minimal (姓名/电话/邮箱/求职意向/毕业时间; GitHub/blog only if content; LinkedIn rare; photo optional-contested). NA legally-driven exclusions — **never** photo/DOB/gender/marital/religion/SSN-SIN/health (Title VII/ADEA/CHRA; EEOC + Cornell LII); add city+state, LinkedIn, GitHub; work-authorization line for non-citizens. CN→NA: hard-delete the 9 fields. NA→CN: optional photo slot + 求职意向 + 毕业时间.
- **Length (Dim 2):** CN 校招 1p (≤2), 社招 ≤3; NA new-grad strict 1p, experienced 1–2p last 10–15 yr.
- **Sections & order (Dim 3):** CN school-dependent; 自我评价 optional ≤3 concrete. NA: Summary/Skills/Experience/Education/Projects; no self-eval; Objective outdated.
- **Bullets (Dim 4):** CN STAR + 技术栈 line + 负责/主导/优化. NA action verb + X-Y-Z, never "Responsible for"; front-load metric. Numbers translate directly and are gold.
- **Skills (Dim 5):** CN tiers 了解/熟悉/熟练掌握 (校招 never 精通) + JD-keyword alignment. NA compact categorized line, **no tiers**.
- **Education (Dim 7):** CN GPA top~30%, 专业排名, CET, 985/211 placement. NA GPA ≥3.5 only, no rank, delete CET.
- **Projects vs work (Dim 6):** both lead new-grad with projects; NA requires GitHub/live links (CN often omits).
- **Tone & ATS (Dim 8,10):** NA impact-first + formal ATS (single column, text-selectable PDF, standard headings, keywords); CN keyword/algorithm matching.
- **File/channel (Dim 9,11):** CN `姓名-岗位-学校-专业`, BOSS直聘/内推/校招官网/牛客; NA `FirstLast_Resume.pdf`, LinkedIn/ATS/referrals.
- **Naive-translation mistakes (Dim 10):** the CN→NA and NA→CN breakage lists.
- **Contested → options (not hardcoded):** photo, skill tiers, age/籍贯, self-eval, address, work-auth, summary.
- **Sources:** condense the per-dimension URL lists from the research docs.

**Acceptance:**
- Every section above present with concrete CN norm / NA norm / transformation rule.
- Cites at least the key sources (Tech Interview Handbook, JavaGuide, EEOC/Cornell LII, CHRC/OHRC, Canada Job Bank).
- ≤ ~450 lines.

- [ ] **Step 1: Write the file** (per outline; read the 3 research docs and distill).

- [ ] **Step 2: Content checklist**

Run: `for s in "X-Y-Z" "Responsible for" "精通" "Title VII" "单栏" "985/211" "CET" "BOSS直聘" "FirstLast_Resume"; do grep -q "$s" skills/resume-optimizer/references/cn-na-market.md && echo "found: $s" || echo "MISSING: $s"; done`
Expected: every line `found: …`.

- [ ] **Step 3: Verify validator green (resume-optimizer SKILL.md link to cn-na-market.md now resolves)**

Run: `python3 scripts/validate.py`
Expected: `OK` — but note `jd-matching.md` and `export-formats.md` links in SKILL.md (Task 6) still pending until Tasks 8–9. If executing Task 6 authoring before 8–9, validator will report those two as missing — that is expected; proceed to Tasks 8–9, then re-run (Task 6 Step 2).

- [ ] **Step 4: Commit**

```bash
git add skills/resume-optimizer/references/cn-na-market.md
git commit -m "feat(resume-optimizer): cn-na-market.md — CN<->NA resume transformation rules"
```

---

### Task 8: `jd-matching.md` — JD parsing + role-bias strategies

**Files:**
- Create: `skills/resume-optimizer/references/jd-matching.md`

**Content outline:**
- **JD parsing method:** extract (a) required/hard skills, (b) nice-to-haves, (c) responsibilities/themes, (d) seniority signals, (e) domain (backend/frontend/AI-agent/algorithm/data/infra). Tokenize exact wording for ATS/keyword alignment.
- **Match scoring:** for each resume section, rate JD relevance High/Med/Low; reorder so High leads; trim Low unless it adds a unique signal.
- **Skill-line rewriting:** mirror the JD's exact phrasing in the skills section (CN: "Java 基础扎实，熟悉 JDK 核心 API（IO、并发、集合）"). Spell out abbreviations once.
- **Role-bias strategies** (concrete re-emphasis per role):
  - **Backend (后端):** foreground concurrency/distributed systems/DB tuning/middleware; metrics = QPS, latency (P95/P99), availability; show 技术栈 line per project.
  - **AI-Agent application dev (AI Agent 应用):** foreground LLM/orchestration (RAG, tool-use, multi-agent), evaluation, prompt engineering, vector DB, cost/latency tradeoffs, deployment (frameworks, observability); metrics = accuracy/eval scores, token cost reduction, task success rate.
  - **Algorithm (算法):** foreground problem modeling, data, metrics (AUC/F1/NDCG/ Recall@k), ablations, online lift, papers/datasets; Research vs Applied framing (academic CV elements only if research role).
  - **Frontend:** perf (LCP/INP), accessibility, component/architecture, DX.
- **What to add/remove:** if JD requires an unpracticed skill, write "了解" (CN) / list it categorically (NA) only if learnable quickly — flag for user. Remove irrelevant stack to keep focus.
- **Honesty note:** matching ≠ invention; never claim skills not held beyond a clearly-flagged "了解" tier.

**Acceptance:** all role biases present with concrete metric/foreground guidance; JD-parse method reproducible.

- [ ] **Step 1: Write the file** (per outline).

- [ ] **Step 2: Content checklist**

Run: `for s in "后端" "AI Agent" "算法" "QPS" "RAG" "AUC" "任职要求" "了解"; do grep -q "$s" skills/resume-optimizer/references/jd-matching.md && echo "found: $s" || echo "MISSING: $s"; done`
Expected: every line `found: …`.

- [ ] **Step 3: Verify validator** — `python3 scripts/validate.py` (jd-matching.md link now resolves; export-formats.md may still be pending if Task 9 not done — expected).

- [ ] **Step 4: Commit**

```bash
git add skills/resume-optimizer/references/jd-matching.md
git commit -m "feat(resume-optimizer): jd-matching.md — JD parsing + role-bias strategies"
```

---

### Task 9: `export-formats.md` — rendering rules + variable conventions

**Files:**
- Create: `skills/resume-optimizer/references/export-formats.md`

**Content outline:**
- **Intermediate representation:** the resume is held as JSON per `templates/json/resume.schema.json`; Export renders each property into the matching `<<VAR>>` token.
- **Variable map** (canonical set — same as Global Constraints): `<<NAME>>`, `<<ROLE_OR_TITLE>>`, `<<CONTACT>>`, `<<SUMMARY>>`, `<<SKILLS>>`, `<<EXPERIENCE>>`, `<<PROJECTS>>`, `<<EDUCATION>>`, `<<AWARDS>>`. For each, which schema property populates it and the rendering rule.
- **LaTeX (primary):** substitute tokens into `templates/latex/resume-{cn,na}.tex.placeholder` OR a user-supplied `--template <path>`. CN uses `xelatex` (CJK-safe); emit a `.tex` the user compiles. Leave `<<CONFIRM: …>>` markers for unverified metrics. Escaping rules: `%`→`\%`, `&`→`\&`, `_`→`\_`, `#`→`\#`.
- **Markdown:** fill `templates/markdown/resume.md` skeleton (headings per section).
- **HTML:** fill `templates/html/resume.html` (single-column, print-CSS, ATS-friendly).
- **JSON Resume:** emit structured JSON conforming to the schema.
- **File naming:** CN `姓名-目标岗位-学校-专业.pdf`; NA `FirstLast_Resume.pdf`.
- **Honesty:** never invent field values to fill a template; omit empty sections rather than fabricate.

**Acceptance:** variable map matches the canonical set exactly; per-format rendering rules complete.

- [ ] **Step 1: Write the file** (per outline).

- [ ] **Step 2: Content checklist + variable-set consistency**

Run: `python3 - <<'PY'
import re
g=set(re.findall(r"<<([A-Z_]+)>>", open("skills/resume-optimizer/references/export-formats.md").read()))
canonical={"NAME","ROLE_OR_TITLE","CONTACT","SUMMARY","SKILLS","EXPERIENCE","PROJECTS","EDUCATION","AWARDS"}
print("OK" if canonical<=g else f"MISSING {canonical-g}")
PY`
Expected: `OK`

- [ ] **Step 3: Verify validator** — `python3 scripts/validate.py` → `OK: 1 skill(s), …` (all SKILL.md links now resolve).

- [ ] **Step 4: Commit**

```bash
git add skills/resume-optimizer/references/export-formats.md
git commit -m "feat(resume-optimizer): export-formats.md — rendering rules + <<VAR>> conventions"
```

- [ ] **Step 5: Complete Task 6's deferred gate** — `python3 scripts/validate.py` (expect `OK`); commit SKILL.md if not already committed in Task 6.3.

---

### Task 10: Enhance `resume-rules.md` with CN/NA + JD + export hooks

Augment the migrated core ruleset so each existing section cross-links to the new references without rewriting the substance.

**Files:**
- Modify: `skills/resume-optimizer/references/resume-rules.md`

**Content edits (append a "Cross-references" subsection + inline hooks):**
- Add a top section **"Market-aware mode"**: "These rules are the universal core. For market-specific differences (CN vs NA) see [cn-na-market.md](cn-na-market.md); for JD tailoring see [jd-matching.md](jd-matching.md); for export see [export-formats.md](export-formats.md)."
- §3 Section Priorities: add note "Page/section norms differ by market — CN new-grad 1 page; NA trim to last 10–15 yr. See cn-na-market.md."
- §4.3 Technical Skills: add "CN uses 了解/熟悉/熟练掌握 tiers (校招 never 精通); NA uses a tier-less categorized line. See cn-na-market.md."
- §5 Project Bullet Patterns: add "NA variant: action verb + X-Y-Z ('Accomplished X as measured by Y by doing Z'), never 'Responsible for'. See cn-na-market.md."
- §10 Interview Defense Checklist: add "These 6 questions are the seed for [resume-mock-interview](../../resume-mock-interview/SKILL.md)." — **NOTE:** this is a cross-skill link. It uses `../../resume-mock-interview/...` which contains `../` and would violate the self-containment check. **Therefore do NOT add this link.** Instead phrase it without a path: "These 6 questions seed the mock-interview sub-skill." (Plain text, no link.)

**Acceptance:** the 3 in-skill links resolve; no `../` reference introduced; substance unchanged.

- [ ] **Step 1: Apply the edits** (the 4 inline hooks + top "Market-aware mode" section; plain-text mention of mock-interview, no path).

- [ ] **Step 2: Verify no `../` introduced and links resolve**

Run: `grep -c "\.\./" skills/resume-optimizer/references/resume-rules.md`
Expected: `0`

Run: `python3 scripts/validate.py`
Expected: `OK: 1 skill(s), …`

- [ ] **Step 3: Commit**

```bash
git add skills/resume-optimizer/references/resume-rules.md
git commit -m "docs(resume-optimizer): add CN/NA + JD + export hooks to resume-rules.md"
```

---

### Task 11: Templates — LaTeX placeholders, TEMPLATE_GUIDE, HTML, Markdown

**Files:**
- Create: `templates/latex/resume-cn.tex.placeholder`
- Create: `templates/latex/resume-na.tex.placeholder`
- Create: `templates/latex/TEMPLATE_GUIDE.md`
- Create: `templates/html/resume.html`
- Create: `templates/markdown/resume.md`

**Interfaces:**
- Consumes: canonical `<<VAR>>` set; `templates/json/resume.schema.json`.
- Produces: templates whose placeholder tokens are exactly the documented set (validator checks this).

- [ ] **Step 1: Write `templates/latex/TEMPLATE_GUIDE.md`**

```markdown
# LaTeX Template Guide

The Export mode substitutes **canonical placeholders** into your `.tex` template. Provide a template that uses exactly these tokens (case-sensitive):

| Token | Filled from schema |
|---|---|
| `<<NAME>>` | basics.name |
| `<<ROLE_OR_TITLE>>` | basics.roleOrTitle |
| `<<CONTACT>>` | basics (phone / email / location / links, formatted) |
| `<<SUMMARY>>` | basics.summary |
| `<<SKILLS>>` | skills[] |
| `<<EXPERIENCE>>` | work[] |
| `<<PROJECTS>>` | projects[] |
| `<<EDUCATION>>` | education[] |
| `<<AWARDS>>` | awards[] |

## Providing your own template

Point Export at your file: ask for "export with template `<path>`". The mode substitutes every `<<TOKEN>>` above and leaves `<<CONFIRM: …>>` markers for values it cannot verify (fill those yourself).

## Built-in placeholders

`resume-cn.tex.placeholder` (CN, compile with `xelatex`) and `resume-na.tex.placeholder` (NA, `pdflatex`/`xelatex`) are empty skeletons demonstrating token placement.
```

- [ ] **Step 2: Write `templates/latex/resume-na.tex.placeholder`**

```latex
% North America resume template (placeholder). Compile with: xelatex resume.tex
% Export substitutes the <<TOKEN>> placeholders below. Single-column, ATS-friendly.
\documentclass[11pt,letterpaper]{article}
\usepackage[margin=0.5in]{geometry}
\usepackage{titlesec}
\titleformat{\section}{\large\bfseries}{}{0em}{}[\titlerule]
\pagenumbering{gobble}
\begin{document}

\begin{center}
{\Large \bfseries <<NAME>>}\\
<<ROLE_OR_TITLE>>\\
<<CONTACT>>
\end{center}

<<SUMMARY>>

\section*{Skills}
<<SKILLS>>

\section*{Experience}
<<EXPERIENCE>>

\section*{Projects}
<<PROJECTS>>

\section*{Education}
<<EDUCATION>>

\section*{Awards}
<<AWARDS>>

\end{document}
```

- [ ] **Step 3: Write `templates/latex/resume-cn.tex.placeholder`**

```latex
% 中国大陆简历模板（占位）。编译：xelatex resume.tex（中文需 xelatex + 中文字体）
% Export 会替换下方 <<TOKEN>> 占位符。
\documentclass[11pt,a4paper]{article}
\usepackage[margin=1.8cm]{geometry}
\usepackage{xeCJK}
\setCJKmainfont{Noto Sans CJK SC}
\usepackage{titlesec}
\titleformat{\section}{\large\bfseries}{}{0em}{}[\vspace{-0.4em}\titlerule]
\pagenumbering{gobble}
\begin{document}

\begin{center}
{\LARGE \bfseries <<NAME>>}\\
<<ROLE_OR_TITLE>>\\
<<CONTACT>>
\end{center}

\section*{专业技能}
<<SKILLS>>

\section*{项目经历}
<<PROJECTS>>

\section*{实习/工作经历}
<<EXPERIENCE>>

\section*{教育背景}
<<EDUCATION>>

\section*{荣誉奖项}
<<AWARDS>>

\end{document}
```

- [ ] **Step 4: Write `templates/markdown/resume.md`**

```markdown
# <<NAME>>
<<ROLE_OR_TITLE>> | <<CONTACT>>

<<SUMMARY>>

## Skills
<<SKILLS>>

## Experience
<<EXPERIENCE>>

## Projects
<<PROJECTS>>

## Education
<<EDUCATION>>

## Awards
<<AWARDS>>
```

- [ ] **Step 5: Write `templates/html/resume.html`**

```html
<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<title><<NAME>> Resume</title>
<style>
  body{font:11pt/1.4 Arial,Helvetica,sans-serif;max-width:7.5in;margin:.5in auto;color:#111}
  h1{font-size:18pt;margin:0} h2{font-size:12pt;border-bottom:1px solid #999;padding-bottom:1px;margin-top:12px}
  .contact{margin:.2em 0 8px} ul{margin:.2em 0;padding-left:1.1em}
  @media print{body{margin:0}}
</style></head>
<body>
  <h1><<NAME>></h1>
  <div class="contact"><<ROLE_OR_TITLE>> &middot; <<CONTACT>></div>
  <p><<SUMMARY>></p>
  <h2>Skills</h2><<SKILLS>>
  <h2>Experience</h2><<EXPERIENCE>>
  <h2>Projects</h2><<PROJECTS>>
  <h2>Education</h2><<EDUCATION>>
  <h2>Awards</h2><<AWARDS>>
</body></html>
```

- [ ] **Step 6: Verify placeholder consistency (validator check 5)**

Run: `python3 scripts/validate.py`
Expected: `OK: 1 skill(s), manifests valid, references resolve, template vars documented.`

(If it fails, a `.tex.placeholder` uses a token not in TEMPLATE_GUIDE — align them to the canonical set.)

- [ ] **Step 7: Commit**

```bash
git add templates/latex templates/html templates/markdown
git commit -m "feat: add LaTeX/HTML/Markdown resume templates + TEMPLATE_GUIDE"
```

---

## Phase C — Sub-skills

### Task 12: `resume-from-code` sub-skill (SKILL.md + code-mining.md)

**Files:**
- Create: `skills/resume-from-code/SKILL.md`
- Create: `skills/resume-from-code/references/code-mining.md`

**Interfaces:**
- Consumes: a repo path or GitHub URL; the user's git identity (author name/email).
- Produces: 1 resume project section (STAR + quantified, per resume-rules conventions) + a highlights-evidence list mapping each highlight to commit/file. Self-contained (no `../` refs; carries its own copy of the STAR formula + 14 dimensions summary).

- [ ] **Step 1: Write `skills/resume-from-code/SKILL.md`**

````markdown
---
name: resume-from-code
description: Turn a code repository into a resume project section. Use when a user points at a repo (local path or GitHub URL) and wants technical highlights extracted from their own commits/code and written as a STAR-format project experience for a software-engineer resume. Produces the section plus an interview-defense evidence list.
---

# Resume from Code

Read a project repository + the user's own contribution history; surface real technical highlights; write one resume project section that is defensible in interview.

## Inputs
- Repo: a local path (preferred) or a GitHub URL.
- The user's git identity: ask for the author name/email to filter `--author`. If unknown, ask them to confirm which commits are theirs before extracting claims.
- (Optional) target role / market to bias emphasis.

## Workflow
1. **Locate the repo.** Local path first (read files directly). If only a GitHub URL, use `gh` (e.g. `gh repo view`, `gh api repos/:owner/:repo/commits?author=<user>`) or clone shallowly. State which you used.
2. **Understand the project.** Read README, architecture docs, key entry points, config/CI, tests.
3. **Isolate the user's contributions.** `git log --author="<user>" --stat` (or gh author filter). Focus on files/commits they touched — do **not** claim work that is not theirs.
4. **Mine highlights** per [code-mining.md](references/code-mining.md): map the 14 optimization dimensions to code signals (perf, concurrency, caching, DB schema, security, observability, abstractions/design patterns, infra, tests).
5. **Quantify honestly.** Derive numbers only from evidence present (benchmarks, test files, configs, scale hints). If a metric is plausible but unverifiable, emit `<<CONFIRM: e.g. QPS before/after>>` and flag it. Never invent.
6. **Draft the section** in STAR + quantified form:
   - Project name / one-line description / tech stack line.
   - 4–6 bullets, each `为解决{问题}，基于{技术}实现{动作}，{量化结果}` (CN) or action-verb + X-Y-Z (NA).
7. **Emit the evidence list**: each bullet → the commit(s)/file(s) that support it, so the user can defend it in interview.

## Output
- The project section (copy-ready).
- A "亮点证据清单" mapping each highlight to commits/files.
- A short list of `<<CONFIRM: …>>` items the user must verify.

## Constraints
- Only real evidence from the user's own commits/code. No fabricated metrics.
- Keep it self-contained: do not reference files outside this skill.
````

- [ ] **Step 2: Write `skills/resume-from-code/references/code-mining.md`**

**Content outline:**
- **Where highlights live:** commit messages, diff hunks (new abstractions, perf-critical paths), config/CI, test files, package manifests, README claims, comments/TODOs resolved.
- **The 14 dimensions → code signals** (self-contained copy, not a `../` link): for each dimension give what to grep/read:
  - Performance → benchmarks, profiling, caching code, indexing, async/concurrency.
  - Concurrency → thread pools, locks, async/await, queues.
  - Caching → Redis/Caffeine, TTL/eviction, random-expiry (防雪崩).
  - DB/schema → migrations, indexes, sharding keys, query optimization.
  - Security → validation, auth, XSS/CSRF/SQLi guards.
  - Observability → metrics, logging, tracing, dashboards.
  - Abstraction/design → patterns, shared utils, generics, plugin points.
  - Infra/DevOps → Docker, K8s, CI/CD, IaC.
  - Tests → coverage, integration/load tests.
- **git recipes:** `git log --author --stat`, `git log -S "<symbol>"` (when a feature appeared), `git shortlog -sne`, `git log --since/--until`, `gh api .../commits?author=`.
- **Quantification sources:** benchmarks in repo, test fixtures (sizes), config (pool sizes, limits), README/diagrams, CI run artifacts; otherwise placeholder.
- **Anti-patterns:** don't claim whole-repo metrics you didn't measure; don't list tech you didn't touch in your commits.

**Acceptance:** all 14 dimensions mapped to concrete code signals; git recipes present; no `../`.

- [ ] **Step 3: Verify self-containment + structure**

Run: `grep -c "\.\./" skills/resume-from-code/SKILL.md skills/resume-from-code/references/code-mining.md`
Expected: `0` `0`

Run: `python3 scripts/validate.py`
Expected: `OK: 2 skill(s), …`

- [ ] **Step 4: Commit**

```bash
git add skills/resume-from-code
git commit -m "feat: resume-from-code sub-skill (code -> resume project section)"
```

---

### Task 13: `resume-mock-interview` sub-skill (SKILL.md + interview-bank.md)

**Files:**
- Create: `skills/resume-mock-interview/SKILL.md`
- Create: `skills/resume-mock-interview/references/interview-bank.md`

**Interfaces:**
- Consumes: a resume (project sections especially).
- Produces: per project, dozens of layered questions each with talking points + likely follow-ups; covers the 6-question defense checklist.

- [ ] **Step 1: Write `skills/resume-mock-interview/SKILL.md`**

````markdown
---
name: resume-mock-interview
description: Generate interview questions from a resume's project experience. Use when a user wants mock-interview prep: given a resume (especially its project sections), produce dozens of layered questions per project, each with reference talking points and likely follow-ups, covering implementation, tech-choice rationale, hard problems, optimization depth, and fundamentals.
---

# Resume Mock Interview

Turn each resume project into a drillable question bank.

## Inputs
- The resume text (project sections are the focus).
- (Optional) target role / market to tune depth (backend / AI-agent / algorithm / frontend).

## Workflow
1. For each project, extract: stated tech stack, claimed metrics, and architecture choices.
2. Generate questions across **5 layers** (see [interview-bank.md](references/interview-bank.md)):
   - L1 基础实现 (what does it do, how is X implemented).
   - L2 技术选型 (why this tech and not another).
   - L3 难点排查 (hardest bug / edge case / debugging).
   - L4 优化深挖 (how a metric was achieved, what would break at scale).
   - L5 相关八股 (fundamentals behind the tech used).
3. For each question, provide: **参考回答要点** (what a strong answer covers) and **可能的追问 (follow-ups)**.
4. Always include the **6-question defense set** (self-contained copy): business flow/modules, what you owned, hardest bug + resolution, why this tech over alternatives, how the metric was measured, is it deployed/demoable.
5. Flag any resume claim that is hard to defend (a question the candidate likely can't answer) — feed it back as a polish suggestion.

## Output
- A question bank grouped by project and layer, each item with talking points + follow-ups.
- A "defensibility flags" list (claims that won't survive scrutiny).

## Constraints
- Questions must be answerable from the candidate's real experience; do not invent resume content. Keep self-contained (no refs outside this skill).
````

- [ ] **Step 2: Write `skills/resume-mock-interview/references/interview-bank.md`**

**Content outline:**
- **5-layer framework** (L1–L5) with 2–3 example questions per layer per common project type (CRUD/business system, infra/middleware, AI-agent app, algorithm).
- **The 6-question defense set** (self-contained copy, not a `../` link): listed verbatim with what each tests.
- **Tech-area follow-up banks** (the common drills): Redis (缓存雪崩/击穿/穿透, 过期策略, 一致性), MySQL (索引, 事务/隔离级别, 锁, 分库分表), concurrency (线程池参数, 锁, AQS), messaging (Kafka/RabbitMQ 削峰/解耦/顺序/幂等), microservices (注册发现/熔断限流/链路追踪), AI-agent (RAG 召回/排序, tool-use 可靠性, eval/幻觉, cost/latency, multi-agent 协作), algorithm (metric definition, offline↔online gap, ablation, data leakage).
- **Scoring rubric** (what a strong vs weak answer looks like) for L2 and L4.

**Acceptance:** 5 layers + 6-question set present; ≥4 tech-area follow-up banks; no `../`.

- [ ] **Step 3: Verify self-containment + structure**

Run: `grep -c "\.\./" skills/resume-mock-interview/SKILL.md skills/resume-mock-interview/references/interview-bank.md`
Expected: `0` `0`

Run: `python3 scripts/validate.py`
Expected: `OK: 3 skill(s), …`

- [ ] **Step 4: Commit**

```bash
git add skills/resume-mock-interview
git commit -m "feat: resume-mock-interview sub-skill (resume -> question bank)"
```

---

## Phase D — Examples & Polish

### Task 14: Sanitized examples

**Files:**
- Create: `examples/README.md`
- Create: `examples/sample-resume-input.md`
- Create: `examples/output-polish.md`
- Create: `examples/output-review.md`
- Create: `examples/output-jd-match.md`
- Create: `examples/output-localize-na.md`
- Create: `examples/output-mock-interview.md`

**Interfaces:** consumes nothing; demonstrates each capability.

- [ ] **Step 1: Write `examples/sample-resume-input.md`** — a fully fabricated (clearly marked "虚构示例 / fictional") new-grad backend resume with weak bullets (so polish/review examples show real improvement). Include name "张三 / Zhang San", a project with vague bullets ("使用 Redis 优化性能"), CET-6, a 985 school.

- [ ] **Step 2: Write each output example** showing the capability applied to the sample:
  - `output-polish.md`: the same project rewritten STAR + quantified (with one `<<CONFIRM>>` marker).
  - `output-review.md`: 🔴/🟡/🟢 tiered critique of the input.
  - `output-jd-match.md`: a short backend JD + the re-emphasized resume (backend bias).
  - `output-localize-na.md`: the CN→NA reshape (photo/age/CET removed, X-Y-Z bullets, 1 page note).
  - `output-mock-interview.md`: one project → ~12 layered questions with talking points + follow-ups + 1 defensibility flag.
- [ ] **Step 3: Write `examples/README.md`** explaining each file is fictional and for illustration.

- [ ] **Step 4: Verify validator green + examples present**

Run: `ls examples/*.md | wc -l` → expect `7`.
Run: `python3 scripts/validate.py` → `OK`.

- [ ] **Step 5: Commit**

```bash
git add examples
git commit -m "docs: add sanitized fictional examples for each capability"
```

---

### Task 15: Finalize READMEs + cross-platform load verification

**Files:**
- Modify: `README.md`, `README.zh-CN.md`

- [ ] **Step 1: Expand both READMEs** from the skeletons (Task 4) to include: capabilities matrix (6 capabilities → 3 skills), the CN↔NA note ("reshapes, doesn't translate"), template section (how to supply your own `.tex`), privacy note (skill runs locally; never auto-submits), link to `examples/` and `docs/superpowers/specs/`. Keep EN in README.md, ZH in README.zh-CN.md.

- [ ] **Step 2: Final repo structure check**

Run: `find skills .claude-plugin .codex-plugin templates agents examples -type f | sort`
Expected: 3 SKILL.md + their references, 2 manifests, agents/openai.yaml, 5 template files (incl. schema), 7 example files.

- [ ] **Step 3: Full green gate**

Run: `python3 scripts/validate.py` → `OK: 3 skill(s), manifests valid, references resolve, template vars documented.`
Run: `python3 -m pytest tests/ -q` → all pass.

- [ ] **Step 4: Cross-platform sanity (manual, documented in README)** — Confirm both manifests are valid JSON pointing at the same `skills/`; confirm no SKILL.md hard-codes a host-specific tool name (grep for common offenders).

Run: `grep -rniE "Read tool|WebFetch|web_fetch" skills || echo "no host-specific tool names hardcoded"`
Expected: `no host-specific tool names hardcoded`.

- [ ] **Step 5: Commit**

```bash
git add README.md README.zh-CN.md
git commit -m "docs: finalize EN/ZH READMEs; cross-platform verification"
```

---

## Self-Review Notes (author completed)

- **Spec coverage:** All 6 capabilities mapped — polish (T6), code→resume (T12), review (T6), mock-interview (T13), CN↔NA (T7 + Localize mode T6), JD-match (T8 + mode T6). LaTeX-first export (T5 schema + T9 + T11). Cross-platform manifests (T2). OSS facade (T4/T15). Authenticity red line embedded in every relevant task.
- **Placeholder scan:** None. Every code step shows complete code; every content step gives exact outline + acceptance grep checks.
- **Type/name consistency:** Canonical `<<VAR>>` set is identical across Global Constraints, Task 5 schema descriptions, Task 6, Task 9, Task 11. Validator (Task 3) enforces template↔TEMPLATE_GUIDE consistency. Skill dir names match frontmatter `name` (validator enforces). `validate(root)` signature stable across Task 3 → tests.
- **Known sequencing caveat:** Task 6's SKILL.md links to files created in T7–T9, so T6's validator/commit is deferred until after T7–T9 (documented inline in T6). Execution in T-order with that deferral keeps every commit green.
