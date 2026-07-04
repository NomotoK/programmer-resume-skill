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
4. Always include the **6-question defense set** (self-contained copy in interview-bank.md): business flow/modules, what you owned, hardest bug + resolution, why this tech over alternatives, how the metric was measured, is it deployed/demoable.
5. Flag any resume claim that is hard to defend (a question the candidate likely can't answer) — feed it back as a polish suggestion.

## Output
- A question bank grouped by project and layer, each item with talking points + follow-ups.
- A "defensibility flags" list (claims that won't survive scrutiny).

## Constraints
- Questions must be answerable from the candidate's real experience; do not invent resume content. Keep self-contained (no refs outside this skill).
