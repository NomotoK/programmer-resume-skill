# Example Output — Review Mode (虚构示例 / FICTIONAL)

> **⚠ 虚构示例 — FICTIONAL.** This is the **Review mode** of `resume-optimizer` applied to [`sample-resume-input.md`](sample-resume-input.md). Tiered critique using the 🔴 Critical / 🟡 Important / 🟢 Optional format defined in [`skills/resume-optimizer/SKILL.md`](../skills/resume-optimizer/SKILL.md). Each item states the problem → gives the concrete fix, quoting the offending line.

---

## 🔴 致命 / Critical — must fix before submission

### C1. 项目子弹没有任何量化数据
> 原文：`使用 Redis 优化了性能。` / `解决了高并发下的超卖问题。`

问题：审阅者无法判断"优化了多少""并发多高""超卖是否真的为 0"。这条子弹等同于零信息，面试官会立刻判定项目不可信。

修复：改为 STAR + 量化（参考 [`resume-rules.md §5`](../skills/resume-optimizer/references/resume-rules.md) 的 bullet 公式），例如："基于 Redis 预扣减 + 异步下单，峰值 QPS 从 500 提升至 8,000，超卖率 0"。若数字无法核实，写 `<<CONFIRM: 指标>>` 而不是凭感觉编。

### C2. 自我评价是纯软技能堆砌
> 原文：`学习能力强，有责任心，团队协作好，能抗压。`

问题：根据 `cn-na-market.md` 与多份招聘方共识，这类描述是 CN 简历的"重灾区"——读作 filler，反而拉低信号密度。

修复：直接删除，或替换为 ≤3 行证据型 Summary（"Java 后端方向，2 个独立项目，QPS 千级压测经验，GitHub xxx"）。绝对不要保留无证据的形容词。

### C3. "做了前后端开发"是模糊的职责描述
> 原文：`做了前后端开发。`

问题：审阅者不知道候选人具体做了哪些模块、是否真的独立完成、技术深度在哪。`负责 / 参与 / 做了` 这类动词在 NA 是 #1 weak-bullet 模式，在 CN 同样是低信号。

修复：写出"我"具体做了什么——"独立完成需求拆解、数据库设计、登录/下单/支付 6 个模块的接口与联调"，并去掉非主营方向（如后端岗不该强调"做了前端"）。

---

## 🟡 重要 / Important — high impact

### I1. 技术栈列表过于笼统
> 原文：`熟悉 MySQL、Redis` / `了解消息队列 Kafka`

问题：没有应用上下文，招聘方无法判断深度。`cn-na-market.md §5` 与 `resume-rules.md §4.3` 都要求"每个关键技术给出应用场景与结果"。

修复：按域分组（基础 / 框架 / 数据库 / 中间件 / 工具），每个关键词后接一个深度线索，如 `熟悉 MySQL（索引优化、慢查询排查、explain 执行计划）`。

### I2. 缺少 GitHub / demo / 文档等可信链接
> 原文：全篇无任何仓库或在线链接。

问题：`resume-rules.md §7` 将"开源仓库 / live demo / 项目文档"列为高可信证据。校招尤其依赖 GitHub 验证"我真的做过"。

修复：至少给秒杀项目补一个 GitHub 仓库链接（哪怕只有 README + 关键代码），有 demo URL 更佳。

### I3. 专业排名 "前 30%" 信号弱
> 原文：`专业排名：前 30%`

问题：`resume-rules.md §4.2` 与 `cn-na-market.md §7` 一致建议——GPA / 排名只在拔尖时写（CN 校招一般 前 10% 才有显著信号，NA 对应 GPA ≥ 3.5/4.0）。前 30% 反而暴露平庸。

修复：删掉排名行；若相关课程分数拔尖，改为"数据库原理 95 / 操作系统 92"等点状高分证据。

### I4. 项目子弹用词雷同
> 原文：两个项目都以 `负责... / 参与...` 开头。

问题：模板化用词让两个独立项目看起来像复制粘贴。`resume-rules.md §8` 明确把"repeated wording across projects"列为常见问题。

修复：每个项目至少有 1 条差异化的、可量化的小标题（如一个突出"高并发 + 超卖"，另一个突出"慢查询优化 + 复用组件"）。

### I5. CET-6 列在教育里信号弱
> 原文：`英语：CET-6（520 分）`

问题：CET 分数对国内大厂后端岗几乎无加分；若投外企才有少量价值。

修复：保留但移到技能最后一行；若目标岗位是外企且无其他英语证据（如托福 / 海外经历），可保留；否则可删。

---

## 🟢 可选 / Optional — polish

### O1. 术语大小写
> 原文：`java` / `spring boot`（应分别为 `Java` / `Spring Boot`）

修复：全篇统一为官方拼写：MySQL、Redis、Spring Boot、MyBatis、Kafka。`resume-rules.md §8` 把"casing 不规范"列为常见问题。

### O2. 技术栈按域分组
当前是一条扁平 bullet 列表。建议拆为：`语言与基础 / 框架 / 数据库 / 中间件 / 工具与部署`，便于招聘方扫读。

### O3. CJK 与 Latin/数字之间加空格
> 原文：`熟悉Spring Boot、MyBatis框架`

修复：`熟悉 Spring Boot、MyBatis 框架`。这是 CN 简历的排版细节但常见于字面排版错误清单。

### O4. 模块顺序
按 `resume-rules.md §2`，校招默认顺序：个人信息 → 教育 → 技术栈 → 项目 → 其他。当前已合规；若学校非 985，则应把项目经历提到教育之前。

### O5. 文件名与格式
当前未给文件名。提交时按 `cn-na-market.md §9`：CN 校招 `张三-Java后端-浙江大学-计算机科学与技术.pdf`；务必 PDF，不要 Word。

---

## 总结

- 🔴 致命 3 条，全部围绕"无量化 + 软技能 + 模糊动词"——这是项目可信度的核心。
- 🟡 重要 5 条，集中在技能深度、可信链接、信号弱的排名 / CET。
- 🟢 可选 5 条，属于排版 / 拼写细节。
- 修复优先级：**先 C 后 I 再 O**。C1 + C3 不修，简历基本无法通过 30 秒初筛。
