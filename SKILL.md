---
name: programmer-resume-optimizer
description: Write, rewrite, and optimize software engineer resumes for internship or full-time applications with role-targeted positioning, STAR-based project bullets, quantified outcomes, and authenticity safeguards. Use when users ask to draft a new developer resume, improve an existing resume, tailor resume content to a JD, polish project/skills sections, increase interview reply rate, or run a quality review checklist before submission.
---

# Programmer Resume Optimizer

## Overview

Produce concise, role-focused, and interview-ready programmer resume content.
Prioritize project evidence, technical clarity, measurable impact, and authenticity.

## Workflow

1. Collect inputs:
- Ask for target role, seniority, and JD keywords.
- Ask for base resume text or source facts (education, skills, projects, internships, links).
- If details are missing, proceed with conservative assumptions and mark placeholders.

2. Decide output mode:
- `Draft mode`: create a full resume from raw facts.
- `Optimize mode`: rewrite existing resume sections.
- `Tailor mode`: map content to a specific JD and reorder priorities.
- `Review mode`: audit resume quality and return fixes.

3. Build section plan:
- Enforce required blocks: personal info, education, technical skills, project experience.
- Keep page economy: usually one page for campus/new grads; allow more only when justified.
- Allocate emphasis with project-first strategy when experience is limited.

4. Rewrite content with strong evidence:
- Use concise, professional wording.
- Use STAR-like bullet pattern: context/problem -> action/tech -> measurable result.
- Convert vague statements to concrete technology, responsibility, and outcome.
- Remove repetitive or generic claims.

5. Run authenticity and risk checks:
- Avoid unverifiable fabrication (degree, work duration, employer identity).
- Keep packaging reasonable: can strengthen framing but do not produce deceptive claims.
- Ensure every highlight is defendable in interview Q&A.

6. Final quality gate:
- Verify terminology casing and typo-free output.
- Verify role alignment and keyword coverage for target JD.
- Return final version plus a short list of interview prep questions for each highlighted project.

## Output Templates

Use compact, copy-ready Chinese unless user requests another language.

For project bullets, prefer:
- `为解决{问题/目标}，基于{技术/方案}实现{关键动作}，将{指标}提升/降低{量化结果}，并带来{业务价值}`。

For skill lines, prefer:
- `熟悉/掌握{技术栈}，可独立完成{场景/任务}，并在{项目}中实践{关键点}`。

For resume review feedback, return:
- Critical issues (must fix before submission)
- Important improvements (high impact)
- Optional polish (low impact)

## References

Read [resume-rules.md](references/resume-rules.md) before drafting or reviewing.

Apply all rules in this order:
1. Required structure and section ratio.
2. Role-focus and ordering strategy.
3. Bullet rewriting and quantification.
4. Authenticity and interview-defensibility checks.
5. Delivery format and final checklist.

## Constraints

- Do not output fake achievements, fake timelines, or unverifiable employer credentials.
- Do not overuse buzzwords without technical details.
- Do not generate long narrative paragraphs when bullet points are better.
