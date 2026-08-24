# Example Output — Mock Interview Mode (虚构示例 / FICTIONAL)

> **⚠ 虚构示例 — FICTIONAL.** This is the **resume-mock-interview** skill applied to the "电商秒杀系统" project from [`sample-resume-input.md`](sample-resume-input.md). Illustrative only; Zhang San is not a real candidate.

Applies the **5-layer framework (L1–L5)** from [`skills/resume-mock-interview/references/interview-bank.md`](../skills/resume-mock-interview/references/interview-bank.md). Each question ships with **参考回答要点** (what a strong answer covers) and **可能的追问** (likely follow-ups). The 6-question defense set is included at the end. One **defensibility flag** is surfaced and mapped to a polish action.

Target project (using the polished bullets from [`output-polish.md`](output-polish.md)):

> **电商秒杀系统** · Java 17 / Spring Boot 3 / MySQL 8 / Redis 7 / RocketMQ 5 / Sentinel · 个人项目
> - QPS 500 → 8,000, 超卖率 ~1.2% → 0
> - 缓存命中率 60% → 95%, DB 峰值 QPS −70%, P95 420ms → 160ms
> - Sentinel 限流阈值 `<<CONFIRM: 实际压测阈值>>`

---

## L1 — 基础实现 (Implementation reproduction)

### L1.1 — Q: 走一遍你秒杀下单的完整请求路径，从用户点"立即抢购"到库存扣减落库。
- **参考回答要点:** 网关 → Sentinel 限流 → 鉴权 → 商品/库存读 Redis → Redis Lua 原子预扣减 → 发 RocketMQ 异步消息 → 立即返回"排队中" → 消费者串行落库（订单表 + 库存表）→ 推送结果。明确说出每一跳的数据结构与状态机；画图能补全。
- **可能的追问:** 用户怎么拿到最终结果？（轮询 / WebSocket / 邮件）；支付在哪一步？

### L1.2 — Q: 你的库存扣减到底在哪一层做的？Redis 预扣减和 MySQL 落库之间的差额怎么处理？
- **参考回答要点:** Redis 预扣减是"逻辑库存"，用 Lua 脚本保证原子性；MySQL 落"实物库存"，二者通过 RocketMQ 解耦；消费者幂等（业务单号唯一索引 / Redis SETNX）；补偿任务对账。
- **可能的追问:** 如果 Redis 扣减成功但消息发送失败怎么办？（事务消息 / 本地消息表 / 重试 + 幂等）。

### L1.3 — Q: 你一个人做了 6 个模块，画出系统边界并指出哪些是你 100% own 的。
- **参考回答要点:** 给出模块图（登录 / 商品详情 / 库存 / 下单 / 支付回调 / 限流），明确边界与依赖；承认弱模块（如支付只是沙箱回调）。

---

## L2 — 技术选型 (Tech-choice rationale)

### L2.1 — Q: 为什么用 RocketMQ 而不是 Kafka 做异步下单？
- **参考回答要点:** 至少给出 1 个备选（Kafka）+ 1 个项目级约束。常见强答：RocketMQ 原生支持事务消息（half message + 回查），契合"扣减 + 发消息"的最终一致需求；Kafka 在单分区严格顺序下吞吐更高但事务语义更弱。承认权衡：RocketMQ 社区/运维生态比 Kafka 略弱。
- **可能的追问:** 在什么负载下你会切回 Kafka？（吞吐 > 一致性容忍度时）。

### L2.2 — Q: 为什么分布式锁用 Redisson 而不是 SETNX 自己写？
- **参考回答要点:** Redisson 提供看门狗续约（避免业务超时导致锁提前释放）、可重入、公平锁选项；手写 SETNX + EX 容易踩"误释放他人锁"和"续约缺失"两个坑。备选：Redis Redlock（多节点）、Zookeeper（CP 强一致但延迟更高）。
- **可能的追问:** 如果 Redis 主从切换时锁丢了怎么办？（Redlock 讨论 / 业务层兜底幂等）。

### L2.3 — Q: 为什么用 Sentinel 而不是 Hystrix 或 Resilience4j？
- **参考回答要点:** Hystrix 已停止维护；Sentinel 提供基于滑动窗口的实时监控 + 流控规则可热更新；Resilience4j 函数式风格更适合 Spring WebFlux 但本项目是 MVC。备选与权衡明确。

---

## L3 — 难点排查 (Hardest bug / debugging)

### L3.1 — Q: 讲一个你在这个项目里踩过的真实 bug——根因 + 修复。
- **参考回答要点:** 必须有具体场景与时间（"压测第 3 天发现的"），看到的实际信号（日志/指标/报警），假设链（不是直接跳到修复），事后动作（测试 / 报警 / 设计规则）。例：库存对账发现 Redis 与 MySQL 偏差 → 排查到 Lua 脚本里 `DECRBY` 没有判负 → 加 `if tonumber(ARGV[1]) > 0 then` 守卫 + 单测覆盖。
- **可能的追问:** 为什么你的测试之前没覆盖到？事后加了什么报警？

### L3.2 — Q: 如果用户反馈"下单一直排队中"——你怎么 triage？
- **参考回答要点:** 先看 RocketMQ 消费滞后（consumer lag）→ 看消费者线程池是否打满 / DB 慢查询 → 看 Sentinel 是否触发降级 → 看是否有死锁（Redisson 锁未释放）。给出排查路径，而不是"重启大法"。

---

## L4 — 优化深挖 (Optimization / metric depth)

### L4.1 — Q: 你说 QPS 从 500 提升到 8,000——拆解每一份增益来自哪里？
- **参考回答要点:** 给出按子步骤的归因分解（例如：异步化 +3000、缓存 +2500、连接池/线程池调优 +1500、限流削峰 +500）；说明测量工具（wrk / JMeter）、数据集（50k 用户 / 1k 商品）、压测窗口、是否多次跑取均值。
- **可能的追问:** 如果流量再 10×到 80k QPS，哪个环节先挂？（猜测：先 DB 写 / Redis 单节点 / 网卡）。

### L4.2 — Q: 你的 Sentinel 限流阈值具体是多少？怎么定出来的？
- **参考回答要点:** ⚠ **这是项目里被 flag 的点**。Polish 阶段已经把数字标成 `<<CONFIRM: 实际压测阈值>>`，意思是候选人现在给不出可信数字。诚实回答："当时压测定在 X，但具体阈值我需要在压测报告里重新确认；我可以说一下我当时是怎么算的——根据下游 MySQL 单实例写入瓶颈反推 + 安全水位 0.7 倍"。
- **可能的追问:** 压测报告现在还在吗？阈值线上有没有动态调过？

---

## L5 — 相关八股 (Fundamentals behind the tech)

### L5.1 — Q: 缓存雪崩 / 击穿 / 穿透各自的失败模式是什么？你的项目里用了哪个 mitigation？
- **参考回答要点:** 雪崩（大批 key 同时过期 → 随机过期 + 多级缓存）；击穿（单个热点 key 过期 → 互斥锁 / 逻辑过期）；穿透（查不存在的 key → 布隆过滤器 / 空值缓存）。秒杀场景主要命中**击穿**（热点库存 key），所以用了 Redisson 互斥锁 + 随机 TTL。机制讲清楚，不只是 API。

### L5.2 — Q: RocketMQ 的事务消息是怎么实现的？跟 Kafka 的事务有什么区别？
- **参考回答要点:** RocketMQ half message → 半消息对消费者不可见 → 执行本地事务 → commit/rollback → broker 回查机制；Kafka 事务是 producer 端跨分区原子写，主要解决 exactly-once 流处理，不是业务侧的最终一致。讲机制而不是"我用了它"。

---

## 6-Question Defense Set (always include)

| # | Question | What a strong answer must contain |
|---|---|---|
| 1 | 项目包含哪些业务流程与模块？ | 6 个模块的依赖图，谁是核心链路。 |
| 2 | 你具体 own / deliver 了什么？ | "我"独立完成的 6 个模块 + 哪些是搭档或 borrowed 的。 |
| 3 | 最难的 bug 与解决？ | L3.1 的具体故事。 |
| 4 | 为什么选这个技术而不是别的？ | L2.1–L2.3 的备选 + 约束 + 权衡。 |
| 5 | 量化效果怎么测的？ | L4.1 的工具 + 数据集 + 窗口；L4.2 的诚实 flag。 |
| 6 | 是否部署 / 可演示？ | GitHub 仓库 + 压测脚本 + README 架构图。 |

---

## Defensibility Flags (escalate back to Polish)

> **每条 flag 都映射到一个具体的 resume 动作。**来源规则：`interview-bank.md §5`。

### 🚩 Flag 1 — L4 score ≤ 2: Sentinel 限流阈值 `<<CONFIRM: 实际压测阈值>>`
- **触发的层:** L4.2（优化深挖）。
- **为什么是 flag:** 候选人无法复现该阈值的压测上下文（工具、数据集、窗口、阈值上下限），面试官追问 3 分钟就会暴露。按 `interview-bank.md §4` 的 L4 rubric，这属于 score ≤ 2，必须 escalate。
- **建议 resume 动作（择一）:**
  1. **首选**——把 bullet 改为定性描述："对下单接口配置 Sentinel QPS 限流 + 降级规则（阈值按下游 MySQL 写入瓶颈反推 + 安全水位）"，不写具体数字；
  2. 若用户能补做压测并拿到可复现的阈值，则把 `<<CONFIRM>>` 替换为真实数字 + 测量脚注；
  3. 若两者都做不到，**删除该条 bullet**——一条不能守的 bullet 比没有更糟。

### 🟡 暂未升级为 flag 的 watch items
- **L2.3 (Sentinel vs Hystrix):** 如果候选人对 Resilience4j 一无所知，可能被降级——建议至少能说出"Sentinel 实时监控 + 流控规则热更新"这一条差异，否则把"熟悉 Sentinel"降为"了解 Sentinel"。
- **L1.1 的支付回调模块:** 若只是沙箱回调，bullet 不应暗示"接入生产支付"。

---

## Notes

- 本示例只展开了"电商秒杀系统"一个项目；真实使用时，每个项目都应该过一遍 L1–L5 + 6-question defense set。
- 题目数量控制在 ~12 条是为了让示例可读；实际面试前建议每项目准备 15–20 条 + 完整 follow-up 链。
- Defensibility flag 的核心价值是把"面试会被戳穿"的 claim **在简历阶段就降级或删除**，而不是临时硬抗。
