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
HEADER_TOKENS = {"NAME", "EMAIL", "PHONE", "GITHUB_USERNAME"}
REGION_NAMES = ("EDUCATION", "EXPERIENCE", "SKILLS")
REQUIRED_EXPORT_ASSETS = (
    "templates/latex/TEMPLATE_GUIDE.md",
    "templates/latex/resume-cn.tex",
    "templates/latex/resume-na.tex",
    "templates/html/resume.html",
    "templates/markdown/resume.md",
    "templates/json/resume.schema.json",
)


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
        return None, f"{path}: invalid JSON ({e})"


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

    # 5. Export template contract
    for rel in REQUIRED_EXPORT_ASSETS:
        if not (root / rel).is_file():
            err(f"missing required export asset {rel}")

    guide = root / "templates/latex/TEMPLATE_GUIDE.md"
    if guide.is_file():
        declared = set(PLACEHOLDER_RE.findall(guide.read_text(encoding="utf-8")))
        latex_dir = root / "templates/latex"
        for tex_name in ("resume-cn.tex", "resume-na.tex"):
            tex = latex_dir / tex_name
            if not tex.is_file():
                continue
            text = tex.read_text(encoding="utf-8")
            used = set(PLACEHOLDER_RE.findall(text))
            for v in sorted(used - declared):
                err(f"{tex_name}: placeholder <<{v}>> not documented in TEMPLATE_GUIDE.md")
            for v in sorted(used - HEADER_TOKENS):
                err(f"{tex_name}: unsupported template token <<{v}>>")
            for region in REGION_NAMES:
                begin = text.count(f"% RESUME-SKILL:BEGIN {region}")
                end = text.count(f"% RESUME-SKILL:END {region}")
                if begin != 1 or end != 1:
                    err(
                        f"{tex_name}: template region {region} must have exactly one BEGIN and one END marker"
                    )

    html = root / "templates/html/resume.html"
    if html.is_file():
        text = html.read_text(encoding="utf-8").lower()
        if not all(tag in text for tag in ("<header", "<main", "<section")):
            err("HTML template missing semantic header/main/section contract")
        if "@page" not in text:
            err("HTML template missing @page print contract")

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
