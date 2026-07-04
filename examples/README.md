# Examples

> **⚠ 所有文件均为虚构示例，仅用于演示 / All files here are FICTIONAL, for illustration only.**
>
> "张三 / Zhang San" is a fabricated person. The school (浙江大学 / Zhejiang University), the projects (电商秒杀系统 / 校园论坛), every metric, every contact detail, and every GitHub / LinkedIn URL are invented. Nothing in this directory is a real candidate's record or a real job description. Do not copy these bullets into a real resume — they exist only to show **what each capability of the resume-skill suite produces**.

## What's in here

The same fictional new-grad backend resume is fed through each capability so the outputs are mutually consistent (same projects, same metrics, same person).

| File | Capability demonstrated | What it shows |
|---|---|---|
| [`sample-resume-input.md`](sample-resume-input.md) | (the input) | A weak CN-style new-grad resume — vague bullets, no metrics, generic skill list, photo/age/CET fields, soft-skill self-eval. |
| [`output-polish.md`](output-polish.md) | `resume-optimizer` · **Polish** | Bullets rewritten with the STAR pattern + 14 optimization dimensions, including one `<<CONFIRM: …>>` marker for an unverifiable metric. |
| [`output-review.md`](output-review.md) | `resume-optimizer` · **Review** | 🔴 Critical / 🟡 Important / 🟢 Optional tiered critique, each item quoting the offending line and giving the concrete fix. |
| [`output-jd-match.md`](output-jd-match.md) | `resume-optimizer` · **JD-Match** | A fabricated backend JD + the 4-step method (parse → score → rewrite skill line → E0 backend role bias). |
| [`output-localize-na.md`](output-localize-na.md) | `resume-optimizer` · **Localize (CN→NA)** | The CN input reshaped to a North-America 1-page resume: photo/age/gender/籍贯/CET deleted, X-Y-Z bullets, LinkedIn in place of 微信, single-column ATS hygiene. |
| [`output-mock-interview.md`](output-mock-interview.md) | `resume-mock-interview` | One project drilled across the L1–L5 five-layer framework (~12 questions with talking points + follow-ups) + the 6-question defense set + 1 defensibility flag escalated back to Polish. |

## How to read these

1. Start with [`sample-resume-input.md`](sample-resume-input.md) to see the weaknesses each output is reacting to.
2. Pick the capability you care about — each `output-*.md` is self-contained and links back to the reference it applies.
3. Cross-check metrics across files: the same `QPS 500 → 8,000`, `P95 420 → 160 ms`, `cache 60% → 95%` numbers appear in Polish, JD-Match, Localize-NA, and Mock-Interview so you can see how one fact is re-shaped per capability.

## What these files are NOT

- **Not templates to copy.** Real resumes must be written from the candidate's own evidence; copying these bullets would be fabrication.
- **Not exhaustive.** Each example is trimmed for readability — real outputs are often longer (more bullets per project, more follow-up questions, fuller Localize checklists).
- **Not legal advice.** The CN↔NA rules cited come from the research in `docs/research/`; for individual cases consult the source references linked in [`cn-na-market.md`](../skills/resume-optimizer/references/cn-na-market.md).

## Related

- [`skills/resume-optimizer/SKILL.md`](../skills/resume-optimizer/SKILL.md) — the main skill with all 5 modes.
- [`skills/resume-optimizer/references/resume-rules.md`](../skills/resume-optimizer/references/resume-rules.md) — the core ruleset (structure, STAR, 14 dimensions, authenticity).
- [`skills/resume-optimizer/references/jd-matching.md`](../skills/resume-optimizer/references/jd-matching.md) — JD parsing + role-bias strategies.
- [`skills/resume-optimizer/references/cn-na-market.md`](../skills/resume-optimizer/references/cn-na-market.md) — CN↔NA transformation rules.
- [`skills/resume-mock-interview/references/interview-bank.md`](../skills/resume-mock-interview/references/interview-bank.md) — the L1–L5 framework + defense set.
