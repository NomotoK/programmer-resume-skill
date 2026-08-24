# Example Output — Polish Mode (虚构示例 / FICTIONAL)

> **⚠ 虚构示例 — FICTIONAL.** This is the **Polish mode** of `resume-optimizer` applied to [`sample-resume-input.md`](sample-resume-input.md). Output is illustrative only; Zhang San is not a real person.

Applies the **STAR bullet pattern** + the **14 optimization dimensions** from [`skills/resume-optimizer/references/resume-rules.md`](../skills/resume-optimizer/references/resume-rules.md). Vague lines are rewritten into `{problem} → {tech/action} → {metric} → {business value}`. Authenticity rule: package wording, never fabricate — any unverifiable number is flagged `<<CONFIRM: …>>`.

Bullet formula (CN default): `为解决{问题}，基于{技术/方案}实现{关键动作}，将{指标}提升/降低{量化结果}，并带来{业务价值}`。

Only the rewritten Project + Skills sections are shown (Personal Info / Education carry over unchanged).

---

## 专业技能（重写后）

- **语言与基础：** Java 基础扎实，熟悉 JDK 核心 API（集合、并发、JVM 内存模型）；了解 JVM 调优基本参数。
- **服务框架：** 熟悉 Spring Boot、MyBatis，可独立完成业务模块开发与单元测试。
- **数据库：** 熟悉 MySQL（索引优化、慢查询排查、explain 执行计划分析）；熟悉 Redis（缓存、分布式锁、过期策略）。
- **中间件：** 熟悉 Kafka（异步解耦、削峰）；了解 RocketMQ。
- **工具与部署：** Git、Maven、Docker 基本使用，Linux 常用命令。

---

## 项目经历（重写后）

### 电商秒杀系统 | 2023.09 – 2024.01 | 个人项目

**技术栈：** Java 17、Spring Boot 3、MySQL 8、Redis 7、RocketMQ 5、Sentinel

- **【并发 / 可用性】** 为应对秒杀场景瞬时高并发请求，基于 **Redis 预扣减库存 + RocketMQ 异步下单** 实现流量削峰与解耦，将下单接口峰值 QPS 从 500 提升至 8,000，超卖率从约 1.2% 降至 0，核心链路在压测下保持可用。
- **【稳定性 / 性能】** 为避免热点 key 击穿打垮数据库，采用 **Redisson 分布式锁 + 缓存随机过期时间** 的策略，并将库存查询走 Redis 缓存，缓存命中率由 60% 提升至 95%，数据库峰值 QPS 下降 70%，接口 P95 响应时间由 420 ms 降至 160 ms。
- **【容错 / 限流】** 引入 **Sentinel** 对下单接口配置 QPS 限流 + 降级规则（阈值 `<<CONFIRM: 秒杀场景实际压测阈值，需根据真实压测结果填写>>`），超过阈值时返回"活动太火爆"降级页，保障核心链路不被拖垮。
- **【交付效率】** 独立完成需求拆解、数据库设计、接口联调与压测脚本，交付登录 / 商品详情 / 下单 / 支付回调 6 个核心模块，迭代周期由双周缩短至 1 周。

### 校园论坛 | 2023.03 – 2023.06 | 团队项目（3 人，后端 2 人）

**技术栈：** Java 17、Spring Boot 3、MySQL 8、MyBatis

- **【性能】** 针对帖子列表高频分页查询的慢查询问题，重写 **联合索引 + 覆盖索引** 并按 `created_at` 倒序优化，列表接口 P95 响应时间由 350 ms 降至 80 ms，慢查询日志条目下降 90%。
- **【可维护性】** 主导帖子与评论模块的接口设计与表结构评审，沉淀统一的分页 / 鉴权拦截器组件，被另外 2 个模块复用，新接口平均开发周期由 4 天缩短至 1.5 天。
- **【协作边界】** 负责帖子、评论两个模块共 12 个接口从设计到联调上线；前端由搭档完成。

---

## Polish Notes（本次重写的取舍）

- **Metric 改写：** 原文 "使用 Redis 优化了性能" → 拆为"做了什么（预扣减 + 异步下单 + 分布式锁 + 缓存随机过期）+ 量化结果（QPS / 超卖率 / 命中率 / P95）"，对应 14 维中的 **性能 / 稳定性 / 可用性 / 容错**。
- **`<<CONFIRM>>` 标记：** 候选人无法在面试中复现秒杀压测的精确阈值，按真实性规则该数字不写死，留给用户确认。面试时若被追问"为什么是这个阈值"会无法回答，符合 `resume-rules.md §7` 的不可伪造约束。
- **删除：** 原 "做了前后端开发"（范围模糊、与项目无关）、自我评价的软技能堆砌（按 `cn-na-market.md` 与 `resume-rules.md` 一致建议删除或替换为证据型 Summary）。
- **术语修正：** `java` → `Java`；`spring boot` → `Spring Boot`；CJK 与 Latin 之间补空格。
