#!/usr/bin/env python3
"""Validate the resume-skill plugin: structure + content contracts.

Exit code 0 (prints OK summary) when valid; 1 with an error list otherwise.
Run: python3 scripts/validate.py   |   tests call validate(root).
"""
import argparse
import json
import re
import sys
from pathlib import Path

DEFAULT_ROOT = Path(__file__).resolve().parent.parent
PLUGIN_NAME = "programmer-resume-skill"
MARKETPLACE_NAME = "programmer-resume"
PLUGIN_RELATIVE_PATH = Path("plugins") / PLUGIN_NAME

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
TEMPLATE_MARKER_FORMATS = (
    ("templates/latex/resume-cn.tex", "% RESUME-SKILL:BEGIN ", "% RESUME-SKILL:END ", ""),
    ("templates/latex/resume-na.tex", "% RESUME-SKILL:BEGIN ", "% RESUME-SKILL:END ", ""),
    ("templates/html/resume.html", "<!-- RESUME-SKILL:BEGIN ", "<!-- RESUME-SKILL:END ", " -->"),
    ("templates/markdown/resume.md", "<!-- RESUME-SKILL:BEGIN ", "<!-- RESUME-SKILL:END ", " -->"),
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


def _validate_template_contract(path, begin_prefix, end_prefix, suffix, declared, err):
    text = path.read_text(encoding="utf-8")
    regions = []
    used = set(PLACEHOLDER_RE.findall(text))
    for token in sorted(used - declared):
        err(f"{path.name}: placeholder <<{token}>> not documented in TEMPLATE_GUIDE.md")
    for token in sorted(used - HEADER_TOKENS):
        err(f"{path.name}: unsupported template token <<{token}>>")
    for region in REGION_NAMES:
        begin_marker = f"{begin_prefix}{region}{suffix}"
        end_marker = f"{end_prefix}{region}{suffix}"
        begin_count = text.count(begin_marker)
        end_count = text.count(end_marker)
        if begin_count != 1 or end_count != 1:
            err(f"{path.name}: template region {region} must have exactly one BEGIN and one END marker")
            continue
        begin_index = text.index(begin_marker)
        end_index = text.index(end_marker)
        if begin_index > end_index:
            err(f"{path.name}: template region {region} markers are in the wrong order")
            continue
        regions.append((begin_index, end_index, region))

    previous = None
    for begin_index, end_index, region in sorted(regions):
        if previous is not None and begin_index < previous[1]:
            err(f"{path.name}: template regions {previous[2]} and {region} overlap")
        if previous is None or end_index > previous[1]:
            previous = (begin_index, end_index, region)


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
        for rel, begin_prefix, end_prefix, suffix in TEMPLATE_MARKER_FORMATS:
            template = root / rel
            if not template.is_file():
                continue
            _validate_template_contract(template, begin_prefix, end_prefix, suffix, declared, err)

    html = root / "templates/html/resume.html"
    if html.is_file():
        text = html.read_text(encoding="utf-8").lower()
        if not all(tag in text for tag in ("<header", "<main", "<section")):
            err("HTML template missing semantic header/main/section contract")
        if "@page" not in text:
            err("HTML template missing @page print contract")

    return errors


def _marketplace_entry(payload, path, expected_name, errors):
    plugins = payload.get("plugins")
    if not isinstance(plugins, list):
        errors.append(f"{path}: missing plugins array")
        return None
    entries = [entry for entry in plugins if isinstance(entry, dict) and entry.get("name") == expected_name]
    if len(entries) != 1:
        errors.append(f"{path}: requires exactly one {expected_name!r} entry")
        return None
    return entries[0]


def validate_repository(repository_root: Path):
    """Validate the marketplace manifests that publish this plugin package."""
    repository_root = Path(repository_root)
    errors = validate(repository_root / PLUGIN_RELATIVE_PATH)

    codex_path = repository_root / ".agents/plugins/marketplace.json"
    codex, load_error = _load_json(codex_path) if codex_path.is_file() else (None, f"missing {codex_path}")
    if load_error:
        errors.append(load_error)
    else:
        if codex.get("name") != MARKETPLACE_NAME:
            errors.append(f"{codex_path}: marketplace name must be {MARKETPLACE_NAME!r}")
        if codex.get("interface", {}).get("displayName") != "Programmer Resume":
            errors.append(f"{codex_path}: interface.displayName must be 'Programmer Resume'")
        entry = _marketplace_entry(codex, codex_path, PLUGIN_NAME, errors)
        if entry is not None:
            if entry.get("source") != {"source": "local", "path": f"./{PLUGIN_RELATIVE_PATH}"}:
                errors.append(f"{codex_path}: plugin source must target ./{PLUGIN_RELATIVE_PATH}")
            if entry.get("policy") != {"installation": "AVAILABLE", "authentication": "ON_INSTALL"}:
                errors.append(f"{codex_path}: plugin policy must be AVAILABLE/ON_INSTALL")
            if entry.get("category") != "Developer Tools":
                errors.append(f"{codex_path}: plugin category must be 'Developer Tools'")

    claude_path = repository_root / ".claude-plugin/marketplace.json"
    claude, load_error = _load_json(claude_path) if claude_path.is_file() else (None, f"missing {claude_path}")
    if load_error:
        errors.append(load_error)
    else:
        if claude.get("name") != MARKETPLACE_NAME:
            errors.append(f"{claude_path}: marketplace name must be {MARKETPLACE_NAME!r}")
        entry = _marketplace_entry(claude, claude_path, PLUGIN_NAME, errors)
        if entry is not None and entry.get("source") != f"./{PLUGIN_RELATIVE_PATH}":
            errors.append(f"{claude_path}: plugin source must target ./{PLUGIN_RELATIVE_PATH}")
    return errors


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repository-root", type=Path)
    args = parser.parse_args()
    errors = validate_repository(args.repository_root) if args.repository_root else validate()
    if errors:
        print("VALIDATION FAILED:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    n = len([d for d in (DEFAULT_ROOT / "skills").iterdir() if d.is_dir()]) if (DEFAULT_ROOT / "skills").is_dir() else 0
    print(f"OK: {n} skill(s), manifests valid, references resolve, export contracts valid.")


if __name__ == "__main__":
    main()
