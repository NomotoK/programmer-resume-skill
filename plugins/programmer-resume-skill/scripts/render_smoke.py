#!/usr/bin/env python3
"""Render fixed fixtures into built-in templates for export-contract smoke tests."""
import argparse
import json
import shutil
import subprocess
from pathlib import Path


HEADER_FIELDS = {
    "NAME": "name",
    "EMAIL": "email",
    "PHONE": "phone",
    "GITHUB_USERNAME": "githubUsername",
}
ESCAPES = {
    "\\": r"\textbackslash{}",
    "%": r"\%",
    "&": r"\&",
    "_": r"\_",
    "#": r"\#",
    "^": r"\textasciicircum{}",
    "$": r"\$",
    "{": r"\{",
    "}": r"\}",
    "~": r"\textasciitilde{}",
}


def escape_latex(value):
    return "".join(ESCAPES.get(char, char) for char in str(value))


def _replace_region(text, name, body):
    begin = f"% RESUME-SKILL:BEGIN {name}"
    end = f"% RESUME-SKILL:END {name}"
    start = text.index(begin) + len(begin)
    finish = text.index(end, start)
    content = f"\n{body.rstrip()}\n" if body else "\n"
    return text[:start] + content + text[finish:]


def _education_block(data):
    lines = []
    for entry in data.get("education", []):
        institution = escape_latex(entry.get("institution", ""))
        date = escape_latex(entry.get("date", ""))
        study_type = escape_latex(entry.get("studyType", ""))
        area = escape_latex(entry.get("area", ""))
        detail = " in ".join(part for part in (study_type, area) if part)
        score = entry.get("score")
        if score:
            detail = f"{detail} | GPA: {escape_latex(score)}" if detail else f"GPA: {escape_latex(score)}"
        lines.append(f"\\resumeEduSubheading{{{institution}}}{{{date}}}{{{detail}}}")
        rank = entry.get("rank")
        if rank:
            lines.append(f"\\resumeEduLine{{{escape_latex(rank)}}}")
        courses = entry.get("courses", [])
        if courses:
            course_text = " / ".join(escape_latex(course) for course in courses)
            lines.append(f"\\resumeEduLine{{\\textbf{{Core Courses:}} {course_text}}}")
    return "\n".join(lines)


def _experience_block(data):
    entries = []
    for project in data.get("projects", []):
        entries.append((project.get("name", ""), project.get("techStack", []), project.get("date", ""), project.get("highlights", [])))
    for work in data.get("work", []):
        name = " — ".join(part for part in (work.get("company", ""), work.get("position", "")) if part)
        date = " -- ".join(part for part in (work.get("startDate", ""), work.get("endDate", "")) if part)
        entries.append((name, work.get("techStack", []), date, work.get("highlights", [])))

    blocks = []
    for name, stack, date, highlights in entries:
        if not highlights:
            continue
        heading = "\\resumeProjectHeading{%s}{%s}{%s}" % (
            escape_latex(name),
            " / ".join(escape_latex(item) for item in stack),
            escape_latex(date),
        )
        bullets = "\n".join(f"  \\resumeItem{{{escape_latex(item)}}}" for item in highlights)
        blocks.append(
            "\n".join(
                [heading, "\\begin{itemize}[label={$\\bullet$},leftmargin=0.15in,topsep=0pt,itemsep=1pt]", bullets, "\\end{itemize}"]
            )
        )
    return "\n".join(blocks)


def _skills_block(data, market):
    lines = []
    for group in data.get("skills", []):
        label = group.get("tier", "") if market == "CN" else group.get("category", "")
        items = group.get("items", [])
        if not label or not items:
            continue
        separator = " / " if market == "CN" else ", "
        lines.append(
            "\\item \\small \\textbf{%s:} %s"
            % (escape_latex(label), separator.join(escape_latex(item) for item in items))
        )
    return "\n".join(lines)


def render_fixture(template, data, market):
    text = Path(template).read_text(encoding="utf-8")
    basics = data.get("basics", {})
    for token, field in HEADER_FIELDS.items():
        value = basics.get(field)
        replacement = value if value is not None else f"MISSING_{token}"
        text = text.replace(f"<<{token}>>", escape_latex(replacement))
    return _replace_region(
        _replace_region(
            _replace_region(text, "EDUCATION", _education_block(data)),
            "EXPERIENCE",
            _experience_block(data),
        ),
        "SKILLS",
        _skills_block(data, market),
    )


def find_xelatex():
    mac_tex = Path("/Library/TeX/texbin/xelatex")
    if mac_tex.is_file() and mac_tex.exists():
        return mac_tex
    path = shutil.which("xelatex")
    return Path(path) if path else None


def compile_tex(tex_path):
    xelatex = find_xelatex()
    if xelatex is None:
        raise RuntimeError("xelatex not found; install MacTeX or add xelatex to PATH")
    return subprocess.run(
        [str(xelatex), "-interaction=nonstopmode", "-halt-on-error", tex_path.name],
        cwd=tex_path.parent,
        check=True,
        text=True,
        capture_output=True,
    )


def compile_all_fixtures(root, output_dir):
    root = Path(root)
    output_dir = Path(output_dir)
    outputs = []
    for template_name, fixture_name, market in (
        ("resume-cn.tex", "minimal-cn.json", "CN"),
        ("resume-na.tex", "minimal-na.json", "NA"),
    ):
        template = root / "templates" / "latex" / template_name
        fixture = root / "tests" / "fixtures" / fixture_name
        tex_path = output_dir / template_name
        data = json.loads(fixture.read_text(encoding="utf-8"))
        tex_path.write_text(render_fixture(template, data, market), encoding="utf-8")
        compile_tex(tex_path)
        outputs.append(tex_path.with_suffix(".pdf"))
    return outputs


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("template", type=Path)
    parser.add_argument("fixture", type=Path)
    parser.add_argument("market", choices=("CN", "NA"))
    parser.add_argument("output", type=Path)
    parser.add_argument("--compile", action="store_true")
    args = parser.parse_args()
    data = json.loads(args.fixture.read_text(encoding="utf-8"))
    args.output.write_text(render_fixture(args.template, data, args.market), encoding="utf-8")
    if args.compile:
        compile_tex(args.output)


if __name__ == "__main__":
    main()
