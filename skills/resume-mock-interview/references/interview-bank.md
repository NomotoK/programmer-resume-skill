# Interview Question Bank

Drillable question patterns for resume-driven mock interviews. Used by `resume-mock-interview/SKILL.md`.

---

## 1. Five-Layer Question Framework (L1–L5)

Each project on a resume should be drillable across five depths. For every generated question, produce **参考回答要点** (what a strong answer covers) + **可能的追问** (likely follow-ups). Layers go from shallow reproduction to underlying fundamentals — interviewers descend through them when probing a claim.

| Layer | Name | What it tests | Weak signal |
|-------|------|---------------|-------------|
| L1 | 基础实现 | Can you reproduce what's on the resume? | Candidate can't describe their own project. |
| L2 | 技术选型 | Did you choose the tech deliberately, or cargo-cult it? | "It's what the team used." |
| L3 | 难点排查 | Have you actually bled on it? | "Nothing was particularly hard." |
| L4 | 优化深挖 | Do you understand the metric you claimed? | Number can't be explained or reproduced. |
| L5 | 相关八股 | Do you understand the principle behind the tech? | Only knows the API, not the mechanism. |

### L1 — 基础实现 (Implementation reproduction)

> Verify the candidate actually built the thing. Ask for end-to-end flow, module boundaries, key data structures.

**CRUD / business system**
- Q: Walk me through the full request path of your "place order" API, from controller to DB write.
- Q: How is your permission model implemented? Where is it enforced?
- Q: Draw the module structure of your system and tell me which parts you owned.

**Infra / middleware**
- Q: How does your gateway route a request to a backend instance? What happens if the instance is down?
- Q: Describe the lifecycle of a cache entry in your system from write to eviction.
- Q: What does a typical config-deploy pipeline look like, and where can it roll back?

**AI-agent application**
- Q: Walk me through one full turn of your agent: user input → tool call → response.
- Q: How is your prompt structured? Where do tool schemas live?
- Q: What does your retrieval pipeline look like end-to-end (ingest → embed → query → rerank → prompt)?

**Algorithm**
- Q: Explain your model architecture and why this input feature set.
- Q: What's the training pipeline — data source, labels, loss, baseline?
- Q: How is the model served at inference time (batch / online, latency budget)?

参考回答要点: precise component names, real numbers (table sizes, QPS, latency), clear ownership boundary ("I owned X, teammate owned Y"), no hand-waving through the hard steps.
可能的追问: "What type is this field?", "Why JSON not protobuf here?", "Where does retry logic live?".

### L2 — 技术选型 (Tech-choice rationale)

> Why this and not the alternative? Tests deliberateness.

**CRUD / business system**
- Q: Why PostgreSQL over MySQL for this service? (Or vice versa.)
- Q: Why did you pick RabbitMQ instead of Kafka here?
- Q: Why a monolith instead of microservices at your scale?

**Infra / middleware**
- Q: Why Redis and not Memcached for this cache?
- Q: Why gRPC instead of HTTP/JSON internally?
- Q: Why a custom scheduler instead of Kubernetes defaults?

**AI-agent application**
- Q: Why a vector DB (e.g. Milvus/Pinecone) instead of Postgres pgvector at your corpus size?
- Q: Why this embedding model and not a cheaper one?
- Q: Why function-calling instead of a structured-output JSON grammar?

**Algorithm**
- Q: Why this loss instead of vanilla cross-entropy?
- Q: Why fine-tune instead of prompt-engineer (or vice versa)?
- Q: Why this baseline — what would you have compared against if you had more time?

参考回答要点: names at least one concrete alternative; cites a project-specific constraint (latency, cost, team familiarity, ecosystem); acknowledges the trade-off they paid (e.g. "Kafka gives us replay but ops cost was higher").
可能的追问: "What would have to change for you to revisit that choice?", "Did you benchmark both?".

### L3 — 难点排查 (Hardest bug / debugging)

> Surface real debugging war stories. Fabricated projects collapse here.

**CRUD / business system**
- Q: Tell me about the worst production bug in this project. Root cause + fix.
- Q: A user reports intermittent 500s — how do you triage?
- Q: Describe a data-inconsistency bug and how you found it.

**Infra / middleware**
- Q: A cache stampede hit you once — what did you see and what did you change?
- Q: Describe a partial-failure / network-partition bug.
- Q: Tell me about a memory leak you tracked down.

**AI-agent application**
- Q: The agent got stuck calling the wrong tool repeatedly — how did you debug and fix it?
- Q: Describe a hallucination you caught post-deployment. How?
- Q: A retrieval change improved eval on one set but regressed another — what did you do?

**Algorithm**
- Q: Describe a training run that diverged. What did you change?
- Q: An offline metric improved but online didn't — how did you investigate?
- Q: Tell me about a label-leakage / data-snooping bug you caught.

参考回答要点: a specific incident with date/scale context, the actual signal they saw (log line, metric, user report), the hypothesis chain (not just the fix), the post-mortem action (test, alert, design rule). "We restarted it" is a fail.
可能的追问: "Why didn't your tests catch it?", "What alert did you add afterwards?", "How would you reproduce it?".

### L4 — 优化深挖 (Optimization / metric depth)

> Probe the numbers on the resume. Every quantified claim should survive this layer.

**CRUD / business system**
- Q: Your resume says "P99 latency from 800ms → 200ms". Walk me through every change that got you there.
- Q: You claim "10× throughput". What was the bottleneck before? What did you measure with?
- Q: What would break first if traffic 10×'d again tomorrow?

**Infra / middleware**
- Q: "Cache hit rate 70% → 95%" — what did you change, and what's the theoretical ceiling?
- Q: How did you measure the memory footprint reduction? What tool?
- Q: Where is the next bottleneck after this optimization?

**AI-agent application**
- Q: You claim "cost reduced 40%". Decompose: prompt shortening, model downgrade, caching, or routing?
- Q: "Latency from 6s → 2.5s" — which sub-stage ate the most, and what did you change there?
- Q: How do you measure retrieval relevance, and did your optimization move it the wrong way?

**Algorithm**
- Q: Your resume claims "AUC 0.78 → 0.85". Was that on the same test set? Same time window?
- Q: Decompose the gain: features, model class, training data, calibration?
- Q: What was the online lift, and over what traffic fraction?

参考回答要点: a decomposition (which sub-step contributed which fraction of the gain), the measurement setup (load tool, dataset, time window, traffic %), a ceiling argument ("we're now bound by DB disk I/O"), and a clear answer to "what breaks at 10× scale".
可能的追问: "Could you have gotten 80% of that gain with a one-line change?", "Was the baseline measured before you started?", "Statistical significance?".

### L5 — 相关八股 (Fundamentals behind the tech)

> Strip the brand off — does the candidate know the principle?

**CRUD / business system**
- Q: What isolation level does your DB default to, and what anomalies does that permit?
- Q: How does an MVCC snapshot actually get created?
- Q: What's the difference between optimistic and pessimistic locking, and when does each win?

**Infra / middleware**
- Q: How does Redis persistence (RDB / AOF) actually work, and what's the durability/perf trade-off?
- Q: Explain the Kafka ISR / leader-follower replication model.
- Q: How does consistent hashing work, and why do virtual nodes help?

**AI-agent application**
- Q: How is cosine similarity affected by vector magnitude, and why do we usually normalize?
- Q: What's the difference between BM25 and dense retrieval, and where does each lose?
- Q: Explain the tool-use decision boundary in function-calling — what does the model actually output?

**Algorithm**
- Q: Derive cross-entropy from MLE. Why is it the default for classification?
- Q: What is label leakage and how do you detect it?
- Q: Explain precision-recall trade-off and how your choice of threshold maps to business cost.

参考回答要点: mechanisms not APIs, diagrams-on-whiteboard clarity, can name the failure mode the design exists to prevent.
可能的追问: depend on the candidate's answer — drill the next layer of "why" until they hit bedrock or admit the limit.

---

## 2. The 6-Question Defense Set (self-contained copy)

Every project on the resume must survive these six. They are the minimum survival set — any bullet that can't answer all six should be downgraded or cut from the resume. Include them **always**, in addition to the layered bank above.

| # | Question | What it tests |
|---|----------|---------------|
| 1 | What business flow and modules does the project include? | Real ownership — can you describe the system end-to-end, not just your corner. |
| 2 | What exactly did you own and deliver? | Boundary clarity — your contribution vs the team's. Catches "we built X" → "I built a small part of X". |
| 3 | What was the hardest issue/bug and how did you resolve it? | Authenticity — fabricated projects collapse on debugging detail. |
| 4 | Why choose this technical solution instead of alternatives? | Deliberateness — did you choose or cargo-cult? Must name an alternative. |
| 5 | What is the measurable effect and how was it measured? | Metric honesty — every number on the resume must be reproducible: setup, baseline, tool, time window. |
| 6 | Is the project deployed or demonstrable? | Reality — a repo link, a demo URL, a user count. "Local only, never shipped" is a yellow flag. |

**Defense-set rubric (per question):**
- Strong: answers in <60s with specifics (numbers, names, alternatives).
- Weak: vague ("we used X because it's popular"), redirects to teammates, or cannot reproduce the metric.
- Auto-fail: cannot describe the module, cannot name any alternative, or the "deployed" claim turns out to be local-only when the resume says production.

---

## 3. Tech-Area Follow-up Banks

Common drills interviewers reach for when a project touches these areas. Use them as fallback follow-ups during L2–L5 probing. Each bullet is a question; pair with 参考回答要点 expectations.

### 3.1 Redis (缓存 / 数据结构 / 持久化)

- What are 缓存雪崩 / 击穿 / 穿透, and which mitigation fits each? (雪崩: 随机过期 + 多级; 击穿: 互斥锁/逻辑过期; 穿透: 布隆过滤器 / 空值缓存.)
- Redis 过期策略 and 淘汰策略 — what's the difference? (惰性删除 + 定期删除; 8 种 maxmemory-policy.)
- How do you keep cache and DB consistent? (Cache-Aside / Write-Through / Write-Behind; 双删延迟; binlog 订阅.)
- When is Redis not the right cache? (large values, scan-heavy workloads, strong durability needs.)
- Persistence: RDB vs AOF — which would you pick at what dataset size / durability SLA?
- Cluster mode: how does resharding affect in-flight requests? Hash tag use cases?

### 3.2 MySQL (索引 / 事务 / 锁 / 分库分表)

- 索引: composite index leftmost-prefix; covering index; index condition pushdown (ICP); when does an index fail to be used (function on column, type cast, OR, leading wildcard).
- 事务隔离级别: four levels + the anomalies each permits (dirty read, non-repeatable read, phantom). What's the InnoDB default and why?
- MVCC: how does a read view get constructed? What's the difference between RC and RR view creation timing?
- 锁: record lock / gap lock / next-key lock; intention locks; when do deadlocks happen and how do you detect them (`SHOW ENGINE INNODB STATUS`, `information_schema.innodb_trx`)?
- 分库分表: when do you actually need it? Vertical vs horizontal; sharding-key choice and the join/transaction problem it creates.
- 慢查询: how do you find and read `EXPLAIN` output? What's the difference between `rows`, `filtered`, and `Extra: Using filesort / Using temporary`?

### 3.3 Concurrency (Java/JVM-flavored, transferable)

- 线程池: 7 parameters; rejection policies; how do you size core/max pool for CPU-bound vs IO-bound?
- `synchronized` vs `ReentrantLock` — monitor inflation, fairness, interruptibility, tryLock timeout.
- AQS: how does it work (state + CLH queue + exclusive/shared)? Name 3 JDK classes built on it.
- `volatile` semantics: visibility, happens-before, prohibition of reorderings — but no atomicity for `++`.
- `ThreadLocal`: memory-leak risk, why weak references + `remove()`.
- `CompletableFuture`: chaining, exception handling (`handle`/`exceptionally`/`whenComplete`), default ForkJoinPool pitfall.
- Virtual threads (Loom): when do they beat platform threads? Pinning risk in `synchronized`.

### 3.4 Messaging (Kafka / RabbitMQ)

- 削峰 / 解耦 / 异步 — name the project's actual use case, not all three.
- Kafka: partition + consumer-group rebalance; how is offset committed; at-least-once vs exactly-once semantics; idempotent producer and transactional producer.
- RabbitMQ: exchange types (direct/fanout/topic/headers); DLX / TTL for retry queues.
- 顺序消费: when is it actually needed? How (single partition / single queue + hash)?
- 幂等: business-id dedup table, Redis SETNX, DB unique index — pick one and justify.
- 消息堆积 and 消息丢失: where in the pipeline can each happen, and the corresponding fix.

### 3.5 Microservices

- 注册发现: CP (Zookeeper/Consul/etcd) vs AP (Nacos/Eureka) — why does service discovery usually want AP?
- 熔断限流: Hystrix / Sentinel / Resilience4j; what state machine does a circuit breaker follow (closed/open/half-open)? Rate limit algorithms (token bucket, leaky bucket, sliding window).
- 链路追踪: trace_id / span_id propagation; how does sampling work at high throughput.
- 网关: auth, rate limit, routing, protocol translation — where should each live?
- Service mesh (Istio): when is the sidecar cost worth it?
- Distributed transaction: Saga / TCC / 2PC / local-message-table / outbox — which fits which consistency need?

### 3.6 AI-Agent Application

- RAG: chunk-size / overlap trade-off; embedding model selection; vector index (HNSW vs IVF); rerank (cross-encoder) vs pure vector recall; hybrid (BM25 + dense) fusion (RRF).
- Tool use / function calling: how do you handle malformed tool output? Retry budget? Loop detection? Fallback to clarification?
- Hallucination mitigation: grounding in retrieved context, citation, confidence threshold, refusal policy.
- Eval: how do you measure retrieval quality (recall@k, MRR, NDCG)? How do you measure end-to-end answer quality (LLM-judge rubric, golden set, A/B)?
- Cost / latency: prompt caching, model routing (cheap model for easy queries), speculative decoding, streaming, batch.
- Multi-agent: orchestration pattern (supervisor / swarm / pipeline); how is state shared; failure isolation; avoiding the "agents talking past each other" failure mode.
- Memory: short-term (context window) vs long-term (vector store / summary); when does summarization lose information?

### 3.7 Algorithm / ML

- Metric definition: is the resume's metric the right one for the business problem? (AUC vs PR-AUC vs NDCG vs lift.)
- Offline ↔ online gap: distribution shift, position bias, feedback loop bias — what was the gap and how was it closed?
- Ablation: can you decompose the gain by feature group / model component? Did you run ablations or just compare end-to-end?
- Data leakage: time-based vs random split; feature leakage from target; future information in features.
- Calibration: are predicted probabilities reliable? Platt / isotonic.
- Cold start: how does the model handle a new user / item?
- Inference cost: model compression (quantization / distillation / pruning), latency budget, batch vs online.

---

## 4. Scoring Rubric (L2 and L4)

Use to grade candidate answers during mock interviews. Score 1–5 per cell.

### L2 — 技术选型 (Tech-choice rationale)

| Score | Signal |
|-------|--------|
| 5 | Names ≥2 alternatives, cites a project-specific constraint with numbers, acknowledges the trade-off paid, and the choice clearly fits the constraint. |
| 4 | Names 1 alternative, cites a constraint, acknowledges a trade-off. |
| 3 | Right choice but generic justification ("industry standard", "team familiarity"). No alternatives named. |
| 2 | Cannot articulate why; "we always use X". |
| 1 | Wrong choice and cannot recognize it; defends with buzzwords. |

What "alternative" means: a real second option the candidate could have picked (Kafka vs RabbitMQ, Postgres vs MySQL, gRPC vs HTTP/JSON), not "this vs nothing".

### L4 — 优化深挖 (Optimization / metric depth)

| Score | Signal |
|-------|--------|
| 5 | Decomposes the gain by sub-step with fractions; states baseline + measurement setup (tool, dataset, time window, traffic %); names the new bottleneck; answers "what breaks at 10× scale" concretely; addresses statistical significance. |
| 4 | Decomposes the gain and gives measurement setup; one of {next bottleneck, scale failure mode, significance} is weak. |
| 3 | Reproduces the before/after numbers but can't decompose; measurement tool named but setup vague. |
| 2 | Number on resume, but cannot reproduce how it was measured or what the baseline was. |
| 1 | Number is decorative — no measurement, no decomposition, no understanding. Resume should be cut. |

**Hard rule:** any L4 score of ≤2 should produce a **defensibility flag**, and the corresponding resume bullet should be softened, re-quantified, or removed before submission.

---

## 5. Defensibility Flags (when to escalate back to polish)

Surface these whenever an interviewer would likely expose a weakness the resume can't survive. Each flag maps to a concrete resume action.

- L3 has no real bug story → downgrade the "高并发/复杂" claim wording.
- L4 score ≤2 → cut or `<<CONFIRM: metric>>` the number.
- L2 score ≤2 → drop the named tech from the skill line if it's decorative.
- Defense Q2 ("what you owned") is fuzzy → rephrase the bullet from "we" to "I", or scope the bullet down.
- Defense Q6 ("deployed?") is "local only" → remove any "上线/生产" wording; keep it as a demo / side project.

Emit the flags in the skill's "defensibility flags" output section, one per claim, with the layer that surfaced it and the suggested action.
