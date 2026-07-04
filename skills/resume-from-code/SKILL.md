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
