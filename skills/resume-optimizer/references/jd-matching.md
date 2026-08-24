# JD Parsing & Role-Bias Strategies

> Consumed by the **JD-Match mode** of `resume-optimizer`. This reference is about *targeting* a specific job description — not about CN⇄NA localization (see [`cn-na-market.md`](cn-na-market.md) for that). The two compose: localize the *format*, then bias the *content* to the JD.
>
> **Core promise.** Give the user a reproducible JD-parse, a per-section relevance score, exact-keyword skill-line rewriting, and concrete per-role re-emphasis (backend / AI-Agent / algorithm / frontend). Matching ≠ invention — see [Honesty note](#honesty-note--matching--invention) below.

---

## Step 0 — JD Parsing Method (reproducible)

Treat the JD as a structured document. Parse it into **five buckets**, verbatim. Do not paraphrase yet — the exact wording is the ATS keyword surface; you will need it unchanged in Step 2.

For each bucket, copy the JD's own phrasing into a scratch table before writing any resume content.

| # | Bucket | What to extract | Example signals (varies by JD) |
|---|---|---|---|
| **A** | **Required / hard skills** | Pull from `任职要求` / `Required` / `Must-have` / `Qualifications` lines. Languages, frameworks, systems, tooling, degree, YOE. | "熟练掌握 Java，熟悉 Spring Boot / MyBatis"; "3+ years Go"; "BS in CS or equivalent" |
| **B** | **Nice-to-haves** | `加分项` / `Preferred` / `Bonus` / `Nice-to-have` / `Plus`. Same categories as A but soft. | "了解 Kubernetes 优先"; "experience with Ray preferred" |
| **C** | **Responsibilities / themes** | `岗位职责` / `What you'll do` / `Responsibilities`. The actual day-to-day problem area. | "负责订单链路高并发架构"; "build retrieval pipelines for billion-scale items" |
| **D** | **Seniority signals** | Title wording, scope words, team-size, "lead / own / drive / architect" vs "build / implement / participate". Decides 校招 vs 社招 framing and verb strength. | "独立负责", "带团队", "0→1", "architect and own" |
| **E** | **Domain** | Classify into one of: **backend / AI-Agent application / algorithm / frontend / data / infra**. Drives the [role bias](#step-3--role-bias-strategies) in Step 3. | Mention of LLM/RAG/agent orchestration → AI-Agent; AUC/排序/召回 → algorithm |

**Parse procedure (do this every time, in order):**

1. **Read the JD once end-to-end.** Note the company, team, and the single sentence that best describes what they actually want (the "thesis sentence" — usually the first responsibility bullet).
2. **Tokenize the `任职要求` / Required block.** Copy every noun phrase that names a technology, framework, or system, **verbatim**, preserving casing and CJK/Latin spacing (`Java` not `java`; `Spring Boot` not `springboot`). This is your **keyword surface** — ATS string-matches against this list.
3. **Tokenize the Preferred block** the same way; tag each item `[B]` so you know it's soft.
4. **Underline scope/seniority verbs** in the Responsibilities block (`own`, `lead`, `drive`, `architect`, vs `build`, `implement`, `support`). These decide whether to write `主导 / 负责` vs `参与 / 实现` (CN) or `Led/Architected` vs `Built/Implemented` (NA).
5. **Classify domain (E)** using the priority decision tree below. If multiple apply, the one tied to the *thesis sentence* wins.
6. **Output a one-line parse summary** before drafting: `Domain={…} · Seniority={校招|初级|中级|高级|资深} · Hard={…} · Soft={…} · Thesis="{…}"`. This becomes the contract for Steps 1–3.

### Domain decision tree (resolve ties by thesis sentence)

- Mentions **LLM / RAG / tool-use / function-calling / multi-agent / prompt / vector DB / LangChain / 自研 Agent** → **AI-Agent application** (E1).
- Mentions **排序 / 召回 / 推荐 / 模型 / AUC / NDCG / 建模 / 算法 / ML** (model-centric, training/iterating models) → **algorithm** (E2).
- Mentions **页面 / 端 / React / Vue / 性能 / LCP / 可访问性 / 前端** → **frontend** (E3).
- Otherwise (default for most service-side engineering: API, concurrency, storage, middleware, distributed systems) → **backend** (E0).
- Specialized: pure data engineering (ETL/warehouse/Spark/Flink pipelines) → **data**; pure infra/SRE/平台 (K8s, CI/CD, service mesh) → **infra**. Bias these like backend but foreground the pipeline/platform angle.

> **Why verbatim?** Most NA Fortune-500 ATS and most CN platform (BOSS直聘 / 拉勾) keyword matchers retrieve on **exact token overlap** with the JD. A resume that says "Golang" against a JD that says "Go" may lose retrieval score; one that says "SpringBoot" (no space) against "Spring Boot" can too. Tokenize verbatim, then choose the JD's casing/spacing when you write.

---

## Step 1 — Match Scoring (reorder before rewriting)

After parsing, score every existing resume section against bucket A (hard skills) and C (responsibilities) of the JD. Use a simple three-tier rubric:

| Score | Criteria | Action |
|---|---|---|
| **High** | Section's primary tech/scope overlaps ≥2 hard-skill tokens **or** directly demonstrates the thesis sentence. | **Lead with it.** Move to top of section order; expand to 4–6 bullets; front-load JD metrics. |
| **Med** | Adjacent tech or transferable scope (same domain, different stack). | Keep; rewrite bullets to surface JD-aligned verbs/keywords; 2–4 bullets. |
| **Low** | Unrelated domain/stack; no token overlap with A or C. | **Trim unless it adds a unique signal** (rare trophy project, brand-name company, or the only evidence of seniority). Otherwise cut. |

**Per-section scoring table (fill this in before reordering):**

```
| Resume section        | Score | Why                              | Action            |
|-----------------------|-------|----------------------------------|-------------------|
| Skills                | —     | keyword overlap with A           | rewrite (Step 2)  |
| Project 1: …          | —     | tech+scope overlap with A+C      | lead/keep/trim    |
| Project 2: …          | —     | …                                | …                 |
| Work/Internship …     | —     | …                                | …                 |
| Education             | —     | degree/校 tier relevance         | place by seniority|
| Awards / Other        | —     | relevance to thesis              | keep/cut          |
```

**Reorder rule.** After scoring, the section order should read top-to-bottom as a **decreasing relevance curve**: the first thing the reader sees is the single strongest piece of evidence for the thesis sentence. For 校招/new-grad with thin direct experience, the strongest evidence is often a project — lead with Projects, not Education. For 社招/experienced, lead with the Work Experience bullet whose tech stack matches A.

> Ties with `cn-na-market.md`: that reference decides *which sections exist and in what market order*; this scoring decides *which project/bullet within a section leads*. Apply market-order rules first, then bias within them using these scores.

---

## Step 2 — Skill-Line Rewriting (mirror JD phrasing)

The Skills / 技术栈 section is the highest-density keyword surface on the resume. Rewrite it to **mirror the JD's exact phrasing** for hard skills, then add depth cues.

**Rules:**

1. **Order follows JD order.** Whatever the JD lists first under `任职要求` goes first in your Skills line.
2. **Verbatim tokens, JD casing.** JD says "Spring Boot, MyBatis" → you write `Spring Boot, MyBatis`, not `springboot/mybatis`.
3. **Spell out abbreviations once** on first use; thereafter the abbreviation is fine. Examples: `Amazon Web Services (AWS)`, `Large Language Model (LLM)`, `Natural Language Processing (NLP)`, `Object Relational Mapping (ORM)`. After the first expansion, ATS still sees both forms because the spelled-out form is on the page.
4. **Add a depth cue after each cluster** (CN tier word or NA short qualifier) — never just a bare stack list. CN: use 了解 / 熟悉 / 熟练掌握 per `cn-na-market.md` (avoid 精通 for 校招). NA: short parenthetical scope, no self-rated stars.

**CN example (mirrored, with depth cues):**

> JD `任职要求` reads: "Java 基础扎实，熟悉 JDK 核心 API；熟悉 Spring Boot / MyBatis；了解分布式中间件（Kafka、Redis）。"

Rewritten Skills line:

```
- 语言与基础：Java 基础扎实，熟悉 JDK 核心 API（IO、并发、集合、JVM 内存模型）
- 框架：熟练掌握 Spring Boot、MyBatis，可独立完成业务模块开发
- 中间件：熟悉 Redis（缓存、分布式锁）、Kafka（异步解耦、削峰）；了解 RocketMQ
- 数据库：熟悉 MySQL（索引优化、分库分表）
```

**NA example (mirrored, with scope qualifiers):**

```
Languages:      Java (core JDK, concurrency, JVM tuning), Go (basic)
Frameworks:     Spring Boot, MyBatis (built 3 production services)
Data Stores:    MySQL (index tuning, sharding), Redis (cache, distributed locks)
Messaging:      Kafka (async decoupling, load shedding); RocketMQ (exposure)
```

> Note how the CN example reproduces the JD's exact phrase "Java 基础扎实，熟悉 JDK 核心 API" verbatim — that overlap is the ATS signal. The NA example preserves the JD's "Spring Boot, MyBatis" token order and expands JDK on first use.

---

## Step 3 — Role-Bias Strategies

After Steps 0–2 (parse, score, rewrite skills), apply the **domain-specific bias**: which bullets to foreground, which metrics to surface, what to add or remove. Pick the section matching the domain you classified in Step 0 (bucket E).

### E0 — Backend (后端)

**Foreground (lead with these in project bullets and skill clusters):**

- **Concurrency & distributed systems:** multithreading, locks, CAS, thread pools, consistency models (CAP, BASE), distributed transactions, idempotency, rate limiting.
- **DB tuning:** indexing strategy, execution plans, slow-query optimization, sharding (分库分表), read/write splitting.
- **Middleware:** cache (Redis patterns — cache penetration/avalanche/breakdown, distributed lock), message queues (Kafka/RocketMQ — exactly-once, ordering, backpressure).
- **Service frameworks:** Spring Boot / Spring Cloud / gRPC / service registry / config center / tracing.

**Metric vocabulary (front-load these in bullets):** **QPS** (peak / steady), **latency P95 / P99** (RT before→after), **availability** (SLA 99.9x%), error rate, throughput, resource cost (CPU / memory / connection-pool) reduction, capacity headroom.

**Bullet shape (CN):** `为解决{并发/性能问题}，基于{技术：Redis/Kafka/分库分表}实现{关键动作}，将 QPS 从 X 提到 Y，P99 从 A ms 降到 B ms，可用性达 99.9x%。`

**Per-project must-have:** an explicit **技术栈 line** under each project header (e.g. `技术栈：Java 17 / Spring Boot 3 / MySQL 8 / Redis 7 / Kafka`). CN recruiters expect this; NA resumes fold the stack into each bullet instead of a standalone line.

**Demote:** pure CRUD with no scale/scope number; coursework unrelated to systems.

### E1 — AI-Agent Application Dev (AI Agent 应用开发)

**Foreground:**

- **LLM orchestration:** **RAG** pipelines (chunking, hybrid retrieval, reranking), **tool-use / function-calling**, **multi-agent** coordination (planner/executor, supervisor), planning & memory (short/long-term, vector recall).
- **Prompt engineering:** structured prompts, few-shot, self-consistency, prompt versioning & regression.
- **Vector store / retrieval:** embedding model selection, ANN index (HNSW, IVF), chunk-size tuning, hybrid (BM25 + dense).
- **Evaluation:** offline eval sets, LLM-as-judge, human eval, regression gates before deploy.
- **Cost / latency tradeoffs:** model routing (small vs large), caching, prompt compression, streaming, **token-cost-per-task** reduction.
- **Deployment & observability:** serving framework (vLLM, TGI, TensorRT-LLM, LangServe), tracing (LangSmith, OpenTelemetry), guardrails (PII, jailbreak, hallucination), A/B routing.

**Metric vocabulary (front-load):** **task success rate / pass@k**, **accuracy / eval-score** (e.g. "业务自定义评测集准确率 72% → 88%"), **token cost per session −X%**, **latency TTFT / TPOT**, **recall@k / precision@k** for retrieval leg, **hallucination rate −Xpp**, **DAU / call volume** served.

**Bullet shape (CN):** `为解决{知识时效/幻觉/成本}问题，基于{RAG/工具调用/多智能体}实现{检索-生成链路}，将{准确率/任务成功率}从 X% 提到 Y%，单次调用 token 成本下降 Z%，P95 延迟控制在 A ms。`

**Demote:** generic "调用了 GPT API" bullets with no eval, no cost, no retrieval design — those read as tutorial work.

### E2 — Algorithm (算法)

**Foreground:**

- **Problem modeling:** how the business problem maps to an ML formulation (classification / ranking / sequence / generation), feature engineering, target definition.
- **Data:** scale (samples, features, sparsity), sources, labeling strategy, handling of bias / leakage / cold-start.
- **Metrics (offline):** **AUC**, **F1**, **NDCG**, **Recall@k**, **Precision@k**, **Hit Rate**, logloss, calibration. Always pair a ranking metric with a business-proxy metric.
- **Metrics (online):** A/B lift in CTR / CVR / GMV / retention; guardrail metrics (latency, diversity, p99 cost).
- **Ablations:** what was removed/added and the delta; model-size vs accuracy Pareto.
- **Papers / datasets / competitions** (Kaggle ranking, NeurIPS/ICML pubs, public benchmark leaderboard rank) — only when real.

**Research vs Applied framing (decisive):**

- **Applied algorithm role** (most industry 算法岗位): lead with **online lift + engineering delivery** (deployed model, A/B result, serving scale). Demote or omit publications; this is a résumé, not a CV.
- **Research role** (lab / 研究院 / research-scientist): academic CV elements are expected — Publications (with citation count, first-author flag), Datasets released, Benchmarks, may exceed 1 page (per `cn-na-market.md` academic-CV exception). Lead with research artifacts if they outrank the applied work.

**Bullet shape (CN, applied):** `为提升{排序/召回/转化}效果，基于{模型/特征工程}重构{链路}，离线 AUC 从 0.X 提到 0.Y，上线 A/B 实验 CTR +Z%，覆盖 W 万 DAU。`

**Demote:** model-zoo dumps ("tried ResNet, BERT, GPT") with no metric delta; coursework projects reused as if production.

### E3 — Frontend

**Foreground:**

- **Performance:** Core Web Vitals — **LCP**, **INP** (replaced FID in 2024), CLS; bundle-size reduction, code-splitting, lazy-loading, SSR/SSG, edge rendering, time-to-interactive.
- **Accessibility (a11y):** WCAG 2.1 AA, semantic HTML, ARIA, keyboard navigation, screen-reader testing, color contrast — surfaced explicitly when the JD mentions 公益/政府/教育/enterprise clients.
- **Component & architecture:** design-system contribution, component API design, state-management (Redux/Zustand/Jotai/Context), monorepo, micro-frontends, dependency injection.
- **DX / tooling:** build perf (Vite/Webpack/Rspack), HMR, test coverage (Vitest/Jest/Playwright), CI pipelines, type safety (TS strict), Storybook.

**Metric vocabulary (front-load):** **LCP ms / INP ms** before→after, **bundle size −KB / −%**, **Lighthouse score X → Y**, **test coverage X% → Y%**, **build time −s**, **a11y violations X → 0**, **DAU / page-views** served.

**Bullet shape (CN):** `为优化首屏体验，基于{代码分割/SSR/资源预加载}重构{页面}，将 LCP 从 X s 降到 Y s，包体积从 A KB 减到 B KB，Lighthouse 性能分从 C 提到 D。`

**Demote:** "熟练使用 HTML/CSS/JS" (assumed); jQuery-era stack unless the JD asks for it.

---

## Step 4 — What to Add / Remove

**Add when** a JD-required skill is missing from the resume but the candidate has *real* exposure (a project, a course, a side build) that simply wasn't surfaced:

- Promote that evidence into a bullet under the matching project; surface the token in the Skills line at the appropriate tier.
- Verify the claim is **interview-defensible** — the candidate can explain the tradeoff, the failure mode, and at least one alternative they rejected.

**Add at the "了解" tier (CN) / categorical mention (NA) only when** the JD lists a skill the candidate has *not* practiced but **could learn quickly** (a few days to a few weeks):

- CN: list it as **`了解{技术}`** — explicitly the lowest tier per `cn-na-market.md`. Never promote to 熟悉 / 熟练掌握 to chase the keyword; that is invention.
- NA: list it in the categorical Skills line without a scope qualifier (no parenthetical implying depth). Do not write a project bullet about it.
- **Always flag these additions to the user** with the literal marker `[FLAG: 了解-tier add — verify before submit]` so the user can confirm or drop the line.

**Remove (cut, not demote) when:**

- The skill/project has **zero token overlap** with buckets A, B, or C and adds no unique signal (rare trophy, brand name, seniority proof). Cutting irrelevant stack is how you keep focus — a resume that lists everything reads as focused on nothing.
- The bullet is a **soft-skill claim** ("团队协作能力强", "fast learner") — these are wasted lines in both CN and NA per `cn-na-market.md`.
- The bullet duplicates metric wording from another bullet (one strong version is enough).

**Never add (out of scope for matching):**

- A skill the candidate does not hold *and* cannot learn in the available time before submission.
- A degree, employer, YOE, or title not actually held — these are fabrication, not matching (see Honesty note).

---

## Honesty Note — Matching ≠ Invention

**Matching means rewiring emphasis, ordering, and phrasing of *real* evidence to align with a JD. It does not mean creating evidence that does not exist.**

The line is concrete:

- **Allowed (matching):** reorder, rewrite verbs, surface JD keywords verbatim, add a depth cue, promote a real project that was omitted, list a quickly-learnable skill at the 了解 / categorical tier with a user flag.
- **Not allowed (invention):** claiming 熟练掌握 / 精通 for a skill never used, fabricating a project or metric, inflating YOE or scope, listing a degree or employer not held, promoting an 了解-tier item to a higher tier to chase a keyword.

**Hard rule:** every bullet must be **interview-defensible** — the candidate can explain the problem, the alternative designs considered, the failure modes, and defend the number. If a rewritten bullet would not survive 3 minutes of interview probing, weaken or cut it; do not strengthen the wording to compensate.

When in doubt, prefer an honest `了解 X（学习中）` over a confident `熟练掌握 X`. Recruiters and hiring managers regularly reject candidates for tier-inflation ("精通 Java" who cannot explain GC tuning) — the reputational cost is larger than the keyword retrieval gain.

---

## Worked Micro-Example

**JD (truncated, AI-Agent application role, 社招):**

> 岗位职责：负责基于 LLM 的智能客服 Agent 设计与落地；构建 RAG 检索-生成链路；优化工具调用准确率与 token 成本。
>
> 任职要求：熟练掌握 Python；熟悉 LangChain / LlamaIndex；熟悉 RAG、function-calling；了解向量数据库（Milvus / Pinecone）；有评测体系经验加分。

**Parse summary (Step 0):**

```
Domain=AI-Agent application (E1) · Seniority=社招中级 ·
Hard={Python, LangChain, LlamaIndex, RAG, function-calling} ·
Soft={vector DB (Milvus/Pinecone), eval system} ·
Thesis="设计并落地 LLM 客服 Agent，优化准确率与 token 成本"
```

**Score (Step 1):** candidate's existing project "基于 LangChain 的企业知识库问答 (RAG + Milvus, 准确率 78%, 1.2k DAU)" → **High** (5-token overlap with Hard + directly demonstrates thesis). Lead with it. Demote an unrelated CRUD Java project to Low / cut.

**Skill-line rewrite (Step 2, CN):**

```
- 语言：熟练掌握 Python（FastAPI、asyncio）
- LLM 编排：熟悉 LangChain、LlamaIndex；熟悉 RAG（chunking、混合检索、rerank）、function-calling
- 向量库：了解 Milvus、Pinecone（ANN 索引选型）
- 评测：业务评测集设计、LLM-as-judge、回归门禁
```

Note: "Milvus、Pinecone" mirrors the JD order; abbreviations (none needed here) would be expanded on first use; depth cues follow `cn-na-market.md` tiers.

**Role bias (Step 3, E1):** rewrite the project's first bullet to lead with the thesis metric:

> 为提升客服回答准确率与控制调用成本，基于 LangChain + Milvus 构建 RAG 链路（混合检索 + rerank），将业务评测集准确率从 64% 提到 78%，单次会话 token 成本下降 35%，P95 延迟 1.4 s，日均服务 1.2k DAU。

This bullet foregrounds accuracy (eval score), token-cost reduction, and latency — the three metrics the AI-Agent bias calls for — and contains every Hard token from the JD verbatim.

---

## Cross-References

- [`cn-na-market.md`](cn-na-market.md) — decides *format and which sections exist* per market; this reference decides *what leads within them* per JD.
- [`resume-rules.md`](resume-rules.md) — base structure, ratios, and the authenticity checklist that overrides any matching instruction here.
- [`guide-2-optimization.md`](guide-2-optimization.md) — bullet-rewrite patterns; the role biases above select *which* pattern to apply.
