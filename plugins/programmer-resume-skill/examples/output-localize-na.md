# Example Output — Localize (CN → NA) Mode (虚构示例 / FICTIONAL)

> **⚠ 虚构示例 — FICTIONAL.** This is the **Localize mode** of `resume-optimizer` applied to [`sample-resume-input.md`](sample-resume-input.md). Illustrative only.

Reshapes — does **not** translate literally — per [`skills/resume-optimizer/references/cn-na-market.md`](../skills/resume-optimizer/references/cn-na-market.md). The CN→NA transformation table is the contract: hard-delete photo / DOB / gender / ID / 籍贯 / 政治面貌 / marital / full address / 期望薪资 (law-driven, not stylistic); `微信 → LinkedIn`; strip skill tiers; rewrite `负责 → Led/Built/Designed` with Google's **X-Y-Z** formula ("Accomplished X as measured by Y, by doing Z"); enforce **1 page** for new grads; delete CET; rename file to `FirstLast_Resume.pdf`; single-column ATS-friendly layout.

We use the polished metrics from [`output-polish.md`](output-polish.md) so the NA version is internally consistent.

---

## San Zhang (张三)

San Jose, CA · (000) 000-0000 · san.zhang@example.com · linkedin.com/in/sanzhang · github.com/sanzhang

**Backend Software Engineer (New Grad)**

---

## Skills

- **Languages:** Java (core JDK, concurrency, JVM tuning)
- **Frameworks:** Spring Boot, MyBatis (built 6 production-style modules)
- **Data Stores:** MySQL (index tuning, slow-query analysis, sharding), Redis (cache, distributed locks, expiry strategy)
- **Messaging:** RocketMQ (async order decoupling, load shedding); Kafka (exposure)
- **Tooling:** Git, Maven, Docker, Linux; Kubernetes (course-level exposure)

> Skills are a compact categorized one-liner per cluster — **no proficiency tiers, no stars** (per `cn-na-market.md §5`). JD keywords preserved verbatim. Kubernetes honestly scoped to "course-level exposure" — same content as the CN `了解` tier, without the self-rating label.

---

## Projects

### Flash-Sale (秒杀) Backend Service | Individual Project | Sep 2023 – Jan 2024
**Stack:** Java 17, Spring Boot 3, MySQL 8, Redis 7, RocketMQ 5, Sentinel · github.com/sanzhang/flash-sale

- **Cut oversell to 0 and lifted peak QPS 16× (500 → 8,000)** by introducing Redis pre-decrement of stock and routing orders through a RocketMQ asynchronous queue, decoupling the write path from the hot API.
- **Drove cache hit rate from 60% → 95% and cut DB peak load 70%** by replacing direct DB reads with a Redis cache layer protected by a Redisson distributed lock and randomized TTLs, defending against cache breakdown on hot keys.
- **Reduced order API P95 latency from 420 ms → 160 ms** by combining the cache rewrite with a composite index on the product-detail path; verified with wrk against a 50k-user synthetic load.
- **Built 6 core modules solo** (auth, product detail, order, payment callback, inventory, rate-limit) on a one-week cadence by owning requirements breakdown, schema design, and integration testing end-to-end.

> Every bullet opens with a strong past-tense action verb, front-loads impact + number, then gives baseline + how (**X-Y-Z**). No "Responsible for…", no pronouns, past tense throughout. The CN `负责整体架构设计` / `做了前后端开发` were cut (latter was off-role for a backend position).

### Campus Forum Backend | Team Project (3 engineers, 2 backend) | Mar – Jun 2023
**Stack:** Java 17, Spring Boot 3, MySQL 8, MyBatis · github.com/sanzhang/campus-forum

- **Trimmed post-list P95 latency from 350 ms → 80 ms** by rewriting the pagination query to use a composite + covering index on `(created_at, board_id)`, eliminating filesort; slow-query log entries dropped 90%.
- **Shrunk average new-endpoint dev time from 4 days → 1.5 days** by designing a reusable pagination + auth interceptor adopted by 2 sibling modules, plus leading the schema review for posts and comments.
- **Owned 12 APIs end-to-end** across posts and comments (design → integration → ship); frontend was a teammate's scope.

---

## Experience

> *(No formal internship in the CN input — if any existed it would be rendered here as `Company · Title · Dates` + quantified bullets. New-grad resumes with no internship lean on Projects, as above.)*

---

## Education

**Zhejiang University** — Hangzhou, China · B.Eng. in Computer Science · Sep 2021 – Jun 2025
- Relevant coursework: Data Structures, Operating Systems, Computer Networks, Database Systems.

> School tier (985 / 双一流) is **undecodable to NA readers** — per `cn-na-market.md §7`, do not lean on it. GPA omitted because the CN "前 30%" is below the NA "≥3.5/4.0" threshold; percentile rank has no NA equivalent and is dropped. **CET-6 deleted** (English is assumed; CET is meaningless in NA).

---

## Localization Checklist (what changed and why)

| CN input field | NA action | Source rule |
|---|---|---|
| 照片 / 性别 / 男 / 出生年月 2002-05 / 籍贯 浙江 | **Hard-deleted** | `cn-na-market.md §1` (Title VII / ADEA / CHRA — law-driven, not stylistic) |
| 微信: zhangsan_wx | Replaced with **LinkedIn** URL | `cn-na-market.md §1` |
| 求职意向 line → | Converted to a **Headline** under the name (Objective is outdated) | `cn-na-market.md §3` |
| 自我评价（软技能） | **Deleted** (NA has no 自我评价 section; soft-skill blurbs are red flags) | `cn-na-market.md §3, §8` |
| 专业排名 前 30% | **Dropped** (below NA's ≥3.5/4.0 GPA threshold; percentile has no NA equivalent) | `cn-na-market.md §7` |
| CET-6 (520) | **Deleted** (English implied; CET meaningless in NA) | `cn-na-market.md §5, §7` |
| 技术栈 tiers (熟悉 / 了解) | **Stripped** → categorized one-liners with scope qualifiers | `cn-na-market.md §5` |
| 负责 / 参与 bullets | Rewritten as **action verb + X-Y-Z** ("Accomplished X as measured by Y by doing Z") | `cn-na-market.md §4` |
| 项目描述 + 技术栈 line | Collapsed to one-liner; tech folded into each bullet | `cn-na-market.md §4` |
| Full address | Reduced to **City + State** | `cn-na-market.md §1` |
| Length | **1 page** enforced for new grads | `cn-na-market.md §2` |

---

## NA Submission Hygiene

- **File name:** `San_Zhang_Resume.pdf` (never `resume.pdf`).
- **Format:** text-selectable PDF, single-column (two-column fails parsing in 7/8 ATS — `cn-na-market.md §10`), ≥10 pt fonts, 0.5" margins, standard headings, no icons.
- **Contact info in body**, not in the Word/Pages header region (ATS cannot read headers).
- **Work-authorization line** — add only if San were a non-citizen needing to signal status; default is to leave it for the ATS application form (per the contested-points note in `cn-na-market.md`).
- **Channels:** LinkedIn + company ATS (Greenhouse / Lever / Ashby) + referrals.
