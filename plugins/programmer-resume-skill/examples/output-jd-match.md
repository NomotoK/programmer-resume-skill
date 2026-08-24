# Example Output — JD-Match Mode (虚构示例 / FICTIONAL)

> **⚠ 虚构示例 — FICTIONAL.** This is the **JD-Match mode** of `resume-optimizer` applied to [`sample-resume-input.md`](sample-resume-input.md) against a fabricated backend JD. Illustrative only.

Applies the 4-step method from [`skills/resume-optimizer/references/jd-matching.md`](../skills/resume-optimizer/references/jd-matching.md): parse → score → rewrite skill line → apply role bias. The role is classified **E0 Backend**, so the bias foregrounds **QPS / latency (P95/P99) / availability / 并发 / 分布式** metrics per the E0 section.

---

## Target JD (fabricated)

> **岗位：** Java 后端开发工程师（校招） · 杭州
>
> **岗位职责：**
> - 参与核心交易链路的高并发架构设计与落地；
> - 负责服务端业务模块的开发、压测与线上稳定性保障；
> - 排查生产环境性能瓶颈，持续优化系统可用性与成本。
>
> **任职要求：**
> - Java 基础扎实，熟悉 JDK 核心 API（IO、并发、集合、JVM 内存模型）；
> - 熟悉 Spring Boot、MyBatis，可独立完成业务模块开发；
> - 熟悉 MySQL（索引优化、分库分表）、Redis（缓存、分布式锁）；
> - 了解分布式中间件（Kafka、RocketMQ）。
>
> **加分项：** 了解 Kubernetes、有高并发压测经验。

---

## Step 0 — JD Parse Summary

```
Domain = Backend (E0)
Seniority = 校招
Hard  = {Java, JDK 核心 API, Spring Boot, MyBatis, MySQL, Redis, Kafka, RocketMQ}
Soft  = {Kubernetes, 高并发压测经验}
Thesis = "核心交易链路的高并发架构 + 线上稳定性保障"
```

Verbatim token surface preserved for Step 2: `Java`, `JDK 核心 API`, `Spring Boot`, `MyBatis`, `MySQL`, `Redis`, `Kafka`, `RocketMQ`, `Kubernetes`.

---

## Step 1 — Per-Section Relevance Scoring

| Resume section | Score | Why | Action |
|---|---|---|---|
| Skills | — | 6/8 token overlap with Hard | Rewrite (Step 2) |
| Project 1: 电商秒杀系统 | **High** | 直接命中 thesis（高并发 + 超卖 + 异步削峰）；Redis/RocketMQ/MySQL 全部 overlap | **Lead with it**，扩到 4–5 条 bullet |
| Project 2: 校园论坛 | **Med** | 同域（Java 后端），但无并发/规模信号 | Keep，rewrite bullets surface JD verbs（性能、慢查询） |
| Education (浙大 985) | High | 学校 tier 强、对口专业 | 保留靠前 |
| CET-6 / 排名前 30% | Low | 与 thesis 无 overlap | 排名信号弱，建议删；CET 移到末行 |
| 自我评价（软技能） | Low | 软技能，按 jd-matching §4 直接 cut | **Cut** |

**Reorder rule:** 校招 thin direct experience → Projects 先于 Education 是合规变体；但浙大 985 是强信号，保留 Education 在前。最终顺序：个人信息 → 教育 → 技术栈 → **电商秒杀系统（lead）** → 校园论坛。

---

## Step 2 — Skill-Line Rewrite (mirror JD phrasing verbatim)

按 JD `任职要求` 原文的 token 顺序与 casing 重写，每个 cluster 加深度线索（CN tier 词，校招不用"精通"）：

```
- 语言与基础：Java 基础扎实，熟悉 JDK 核心 API（IO、并发、集合、JVM 内存模型）
- 框架：熟悉 Spring Boot、MyBatis，可独立完成业务模块开发
- 数据库：熟悉 MySQL（索引优化、分库分表）、Redis（缓存、分布式锁）
- 中间件：熟悉 Kafka（异步解耦、削峰）；了解 RocketMQ
- 平台与工具：了解 Kubernetes；熟悉 Git、Maven、Docker、Linux 常用命令
```

注意：`Java 基础扎实，熟悉 JDK 核心 API` 是 JD 原话逐字复刻——ATS / BOSS 直聘的关键词匹配就是吃这种 overlap。`RocketMQ` 与 `Kubernetes` 在 JD 中是 Soft/Preferred，故前者保持"了解"tier、后者打 `[FLAG: 了解-tier add — verify before submit]`。

`[FLAG: 了解-tier add — verify before submit]` → Kubernetes：候选人仅有课程暴露，无项目证据，按 `jd-matching.md §4` 仅可列在"了解"tier，且必须 flag 让用户确认。**禁止**升级为"熟悉"以追关键词——那是 invention。

---

## Step 3 — Role Bias Applied (E0 Backend)

E0 metric vocabulary: **QPS（peak/steady）, latency P95/P99, availability (SLA 99.9x%), error rate, throughput, resource cost**. Bullet shape: `为解决{并发/性能问题}，基于{Redis/Kafka/分库分表}实现{动作}，将 QPS 从 X 提到 Y，P99 从 A ms 降到 B ms，可用性达 99.9x%`。

### 项目经历（按 JD 重排后）

#### 电商秒杀系统 | 2023.09 – 2024.01 | 个人项目   ← **Lead**

**技术栈：** Java 17 / Spring Boot 3 / MySQL 8 / Redis 7 / RocketMQ 5 / Sentinel

- **【并发 / 可用性 — 直接命中 thesis】** 为应对秒杀场景瞬时高并发，基于 **Redis 预扣减库存 + RocketMQ 异步下单** 实现流量削峰与解耦，将下单接口峰值 **QPS 从 500 提升至 8,000，超卖率从 ~1.2% 降至 0**，核心链路在压测下保持可用。
- **【性能 / 稳定性】** 为避免热点 key 击穿数据库，采用 **Redisson 分布式锁 + 缓存随机过期** 策略，缓存命中率由 60% 提升至 95%，**数据库峰值 QPS 下降 70%**，**接口 P95 响应由 420 ms 降至 160 ms**。
- **【容错 / 限流】** 引入 **Sentinel** 对下单接口做 QPS 限流 + 降级（阈值 `<<CONFIRM: 实际压测阈值>>`），保障核心交易链路可用性。
- **【交付】** 独立完成需求拆解、数据库设计、压测脚本，交付 6 个核心模块，迭代周期由双周缩短至 1 周。

#### 校园论坛 | 2023.03 – 2023.06 | 团队项目（3 人，后端 2 人）   ← **Keep**

**技术栈：** Java 17 / Spring Boot 3 / MySQL 8 / MyBatis

- **【性能】** 针对帖子列表高频分页查询慢查询问题，重写 **联合索引 + 覆盖索引**，列表接口 **P95 由 350 ms 降至 80 ms**，慢查询日志下降 90%。
- **【可维护性 / 复用】** 主导帖子与评论模块的接口设计与表结构评审，沉淀统一的分页 / 鉴权拦截器，被另 2 个模块复用，新接口平均开发周期由 4 天缩短至 1.5 天。
- **【协作边界】** 负责帖子、评论两个模块共 12 个接口的设计到联调上线；前端由搭档完成。

---

## Step 4 — What to Add / Remove (per `jd-matching.md §4`)

**Add（真实暴露、面试可守）：**
- 在 Skills 加 `了解 Kubernetes`（tier 严格为"了解"——候选人仅课程暴露，无项目证据）→ flag 给用户确认。
- 在秒杀项目补一条体现"线上稳定性保障"（与 thesis 第二条职责对应）的 bullet，例如 Sentinel 限流降级。

**Remove（cut，不是 demote）：**
- 自我评价的软技能堆砌——与 thesis 零 overlap，是 wasted line。
- 专业排名 "前 30%"——信号弱，无 token overlap。
- "做了前后端开发"——后端岗不该强调"做了前端"。

**Never add（out of scope）：**
- 不编造 Kubernetes 项目经验；不把"了解 K8s"升级为"熟悉"以追关键词。

---

## Honesty Check

每一条 bullet 都满足"3 分钟面试可守"：候选人在被追问"QPS 500 → 8000 怎么压测的""超卖率怎么定义 / 怎么测的""为什么用 RocketMQ 而不是 Kafka"时，必须能给出具体的工具（JMeter / wrk）、数据集、压测窗口、备选方案与权衡。`<<CONFIRM: 实际压测阈值>>` 是因为该具体数字候选人无法复现——按 `jd-matching.md` Honesty Note，宁可不写也不要凭感觉编。
