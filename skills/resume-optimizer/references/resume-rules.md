# Programmer Resume Rules

## Market-aware mode

These rules are the universal core. For market-specific differences (CN vs NA) see [cn-na-market.md](cn-na-market.md); for JD tailoring see [jd-matching.md](jd-matching.md); for export see [export-formats.md](export-formats.md).

## Table of Contents

1. Scope
2. Resume Structure
3. Section Priorities and Ratios
4. Writing Rules by Section
5. Project Bullet Patterns
6. Optimization Dimensions for Highlights
7. Authenticity and Trust Signals
8. Common Problems and Fixes
9. Submission Checklist
10. Interview Defense Checklist

## 1. Scope

Use this reference to write or optimize resumes for software engineers, including internships and full-time roles.
Keep content concise, role-oriented, and measurable.

## 2. Resume Structure

Required sections:
- Personal Information
- Education
- Technical Skills
- Project Experience

Optional sections:
- Internship/Work Experience
- Awards/Competitions
- Campus/Research Experience
- Personal Strengths (only when content is concrete)

Default ordering:
1. Personal Information
2. Education
3. Technical Skills
4. Internship/Work Experience (if present)
5. Project Experience
6. Other sections

Reorder by strengths when needed:
- Put the strongest evidence above weaker sections.
- Keep target-role-relevant sections earlier.

## 3. Section Priorities and Ratios

Recommended ratio for campus/new-grad resumes:
- Personal Information: 5%-10%
- Education: 10%-15%
- Technical Skills: 20%-30%
- Experience (project/intern/research/campus): 30%-50%
- Other: 0%-20%

Length guidance:
- One page is preferred for most campus resumes.
- More than one page is acceptable only when content is truly strong and dense.
- Ensure highest-value content appears on page one.

Market note: Page/section norms differ by market — CN new-grad 1 page; NA trim to last 10–15 yr. See [cn-na-market.md](cn-na-market.md).

## 4. Writing Rules by Section

### 4.1 Personal Information

Include:
- Name
- Job intention (target role)
- Contact methods (phone, email, optional WeChat/QQ by JD requirement)
- Optional links: GitHub, blog, portfolio, project demo

Rules:
- Keep compact; merge related info into one line.
- Prefer short and easy-to-type links.
- Do not include expected salary unless explicitly required.

### 4.2 Education

Include:
- School, major, degree/status
- Start and end date
- Ranking only when competitive (for example top 20% or better)
- Relevant coursework only when major-role mismatch exists

Rules:
- Keep facts truthful.
- Add high scores only when they strengthen the target role narrative.

### 4.3 Technical Skills

Rules:
- Group by domain (backend, frontend, database, middleware, devops, cloud).
- Do not write long "name-dropping" sentences.
- Avoid mixing unrelated technologies in one line.
- Avoid obvious fundamentals with low signal.
- For each key skill, add proof of application context.

Preferred pattern:
- `掌握/熟悉 {技术}，在 {项目场景} 中用于 {目标}，实现 {结果}`。

Market note: CN uses 了解/熟悉/熟练掌握 tiers (校招 never 精通); NA uses a tier-less categorized line. See [cn-na-market.md](cn-na-market.md).

### 4.4 Project Experience

Rules:
- Keep project intro short; focus on personal contribution.
- Avoid feature-only description.
- Avoid repeating identical statements across projects.
- Use professional wording; reduce colloquial expressions.
- Prefer quantified outcomes whenever possible.

## 5. Project Bullet Patterns

Base formula:
- `为解决 {问题}，基于 {技术/方案} 完成 {关键动作}，使 {指标} 提升/下降 {量化结果}，并带来 {业务价值}`。

STAR-like compact pattern:
- Situation/Task: business context or challenge
- Action: technical action and design choices
- Result: measurable impact

Rewrite examples:
- Weak: `使用 Redis 优化了性能。`
- Better: `针对高频查询场景引入 Redis 缓存并设置随机过期策略，接口 P95 响应由 420ms 降至 160ms，数据库峰值压力下降 65%。`

- Weak: `做了前后端开发。`
- Better: `独立完成需求拆解、数据库设计与前后端联调，交付 6 个核心模块并将迭代周期从双周缩短至 1 周。`

Market note: NA variant: action verb + X-Y-Z ('Accomplished X as measured by Y by doing Z'), never 'Responsible for'. See [cn-na-market.md](cn-na-market.md).

## 6. Optimization Dimensions for Highlights

When expanding project highlights, prioritize one or more of these dimensions:
- Performance
- Cost
- Availability
- Reliability
- Stability
- Fault tolerance
- Robustness
- System complexity
- Maintainability
- Scalability
- Observability
- Elasticity
- User experience
- Security

Rule:
- Do not mention optimization category without concrete method and effect.
- Use metrics such as latency, throughput, error rate, resource usage, delivery cycle, or business conversion.

## 7. Authenticity and Trust Signals

High-trust evidence:
- Live demo URL
- Open-source repo URL with meaningful commit history
- Project documentation with architecture and key decisions
- Clear ownership boundaries in team projects

Rules:
- Package wording, not core facts.
- Do not fabricate degree, years of experience, company identity, or hard-verified timeline data.
- If writing a claim, ensure candidate can defend it in interview.

## 8. Common Problems and Fixes

Common issue: resume too long and diluted
- Fix: remove low-signal lines, keep strongest evidence, compress descriptions.

Common issue: no clear role focus
- Fix: state target role and reorder content toward that direction.

Common issue: skill list is generic and unconvincing
- Fix: add depth and use-context per key skill.

Common issue: project bullets too broad
- Fix: narrow to personal actions, architecture choices, and measurable outcomes.

Common issue: repeated wording across projects
- Fix: deduplicate templates; each bullet must present distinct value.

Common issue: unprofessional or inaccurate terms
- Fix: enforce technical precision and proper casing (for example `MySQL`, `Redis`, `Spring Boot`).

Common issue: typo and grammar errors
- Fix: run at least 3 proofreading passes before submission.

## 9. Submission Checklist

Before final output, verify all items:
- Target role is explicit and consistent.
- Required sections exist.
- Section ratio is reasonable.
- Project/intern sections are evidence-heavy.
- Bullets are concise and mostly quantifiable.
- Repetitive lines are removed.
- Terminology casing is correct.
- No obvious typos or ambiguous phrasing.
- File naming follows JD rule when provided.
- Export format recommendation includes PDF.

## 10. Interview Defense Checklist

For each highlighted project, prepare answers to:
- What business flow and modules does the project include?
- What exactly did you own and deliver?
- What was the hardest issue/bug and how did you resolve it?
- Why choose this technical solution instead of alternatives?
- What is the measurable effect and how was it measured?
- Is the project deployed or demonstrable?

These 6 questions seed the mock-interview sub-skill.
