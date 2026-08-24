# 程序员简历技能套件（Programmer Resume Skill Suite）设计文档

> 日期：2026-07-02
> 状态：已通过用户评审（架构 + 5 节设计）
> 前身：基于 [liyupi/coder-resume-guide](https://github.com/liyupi/coder-resume-guide) 制作的单个 `programmer-resume-optimizer` skill
>
> **历史说明（2026-08-19）：** 套件架构与六项能力仍有效；原有 LaTeX token/export 描述已由 [Export Contract v2](2026-08-19-export-contract-v2-design.md) 取代。v2 使用四个头部 token 与三个具名内容区块。

## 1. 背景与目标

现有仓库是一个基于程序员鱼皮（liyupi）写简历指南制作的**单一简历优化 skill**，包含 `SKILL.md`、`resume-rules.md` 规则库和 6 篇中文指南素材。本项目将其**扩展为一套聚焦计算机技术岗求职的简历技能套件**，覆盖 6 大能力，并同时面向个人使用与开源分发。

### 6 大能力

1. **简历润色**：输入已有简历，按 STAR 法则与最佳实践优化表述；支持整份或针对某一部分/某段项目经历。
2. **项目代码 → 简历**：Agent 阅读用户某个项目的仓库代码与历史贡献，发掘技术亮点，提炼为一段简历项目经历。
3. **点评 + 分析**：对现有简历进行专业分档点评。
4. **模拟面试**：根据简历项目经历，为每段经历生成数十道面试问题 + 参考要点/追问。
5. **中英文支持**：根据中国与北美职场差异，分别导出中文版与适合北美的英文版；**是市场重塑而非翻译**。
6. **JD 匹配**：用户提供岗位 JD，Agent 据此微调简历（后端/AI Agent 应用开发/算法岗等不同偏向）。

### 关键决策（已确认）

| 决策项 | 选择 |
|---|---|
| 受众 | 个人自用 + 开源分发，遵循 OSS skill 最佳实践 |
| 架构 | 混合：1 主 skill + 2 子 skill |
| 分发形态 | 跨平台插件，支持 **Claude Code + OpenAI Codex** |
| 代码→简历 数据来源 | 本地仓库（git 历史）优先，否则 gh CLI 读远端 GitHub |
| 输出格式 | **LaTeX 优先**（用户提供模板，留空占位；支持用户自传模板）+ Markdown/HTML/JSON 辅助 |
| 模拟面试形态 | 出题 + 参考要点/追问（主打；交互式为后续可选） |
| 点评风格 | 专业分档（🔴致命 / 🟡重要 / 🟢可选）|
| 模板占位符约定 | `<<VAR>>`（LaTeX 安全，易 find/replace）|

## 2. 整体架构与分发

改造为一个跨平台插件，`skills/` 目录为唯一真相源，两个平台清单各自指向它。

```
programmer-resume-skill/
├── .claude-plugin/plugin.json      # Claude Code 插件清单
├── .codex-plugin/plugin.json       # OpenAI Codex 插件清单（指向同一 skills/）
├── agents/openai.yaml              # 保留：Codex interface 声明（更新为套件描述）
├── skills/
│   ├── resume-optimizer/           # 【主】润色·点评·JD匹配·中英适配·导出
│   │   ├── SKILL.md
│   │   └── references/
│   │       ├── resume-rules.md         # 现有，强化
│   │       ├── cn-na-market.md         # 新增：中英市场差异（调研产出）
│   │       ├── jd-matching.md          # 新增：JD 匹配方法论 + 岗位偏向
│   │       ├── export-formats.md       # 新增：LaTeX/MD/HTML/JSON 导出说明
│   │       └── guide-*.md              # 现有 liyupi 6 篇素材（重命名为 ASCII）
│   ├── resume-from-code/           # 【子】代码 → 项目经历
│   │   ├── SKILL.md
│   │   └── references/code-mining.md
│   └── resume-mock-interview/      # 【子】简历 → 面试题 + 参考要点
│       ├── SKILL.md
│       └── references/interview-bank.md
├── templates/
│   ├── latex/
│   │   ├── resume-cn.tex.placeholder   # 空占位，用户填充
│   │   ├── resume-na.tex.placeholder   # 空占位，用户填充
│   │   └── TEMPLATE_GUIDE.md           # 占位变量约定 + 用户自传模板规范
│   ├── html/resume.html                # 单页可打印 HTML
│   ├── markdown/resume.md              # Markdown 简历骨架
│   └── json/resume.schema.json         # JSON Resume 兼容 schema
├── examples/                       # 脱敏示例：输入简历 + 各能力输出
├── docs/
│   ├── research/                       # 调研素材（中/英市场规范）
│   └── superpowers/specs/              # 本设计文档
├── README.md                       # OSS 门面（英文）
├── README.zh-CN.md                 # OSS 门面（中文）
└── LICENSE
```

### 跨平台可移植性原则

- 所有 `SKILL.md` 用**平台中立的动作描述**（"读取文件"、"运行 git/gh 命令"、"搜索文件内容"），不写死任一平台的专有工具名。
- Claude Code 通过 `.claude-plugin/plugin.json` + `skills/` 加载；Codex 通过 `.codex-plugin/plugin.json` 加载同一 `skills/`，动作映射到 Codex 的 `shell`/`apply_patch`/`web_search` 等。
- 两个清单为**同源双清单**（参考 superpowers 等成熟多平台插件做法）；`skills/` 内容不因平台而分叉。

### 迁移说明

- 现有根目录 `SKILL.md` **移动**到 `skills/resume-optimizer/SKILL.md`（根目录不再放 SKILL.md）。
- 现有 `references/*.md` 移动到 `skills/resume-optimizer/references/`；6 篇中文指南文件名改为 ASCII（`guide-1-basics.md` 等），避免跨平台文件名问题，内容保留中文。
- 保留 `LICENSE`、`agents/openai.yaml`（更新内容）。

## 3. 主 skill：`resume-optimizer`（5 个模式）

单个 skill，入口按用户意图分流到 5 个 mode，共享同一套 references。润色→点评→JD→中英→导出 是常见连招，放同一 skill 内切换最顺，也避免规则库重复。

| Mode | 触发意图 | 职责 |
|---|---|---|
| **Polish 润色** | "优化我的简历/这段经历" | 按 STAR + 14 优化维度 + 万能公式重写；支持整份或指定片段；保持真实性 |
| **Review 点评** | "点评我的简历" | 专业分档输出：🔴致命（投递前必改）/ 🟡重要（高影响）/ 🟢可选（低影响润色），逐条给理由与改法 |
| **JD-Match 匹配** | "按这个 JD 调整" | 解析 JD → 提取关键词/能力项 → 重排序、增删、调整技术偏向；内置后端/AI Agent 应用开发/算法岗等偏向策略 |
| **Localize 中英适配** | "导出适合北美的英文版/中文版" | 基于 `cn-na-market.md` 做市场重塑而非翻译：改 header 字段、bullet 风格（action-verb vs STAR 句式）、长度、技能呈现、教育细节等 |
| **Export 导出** | "导出成 LaTeX/PDF" | 将结构化简历数据填入 `templates/` 模板；LaTeX 优先，支持 `--template <用户模板路径>` |

### 内部数据流

1. **解析**：用户输入（简历文本/文件）→ 结构化中间表示（个人信息、教育、技能、项目、经历等模块）。
2. **操作**：所选 mode 在中间表示上操作（润色/点评/匹配/本地化）。
3. **导出**：中间表示 → 目标格式模板。

中间表示对齐 `templates/json/resume.schema.json`（JSON Resume 兼容 + 技术岗扩展字段），使各 mode 与导出解耦。

## 4. 子 skill

### 4.1 `resume-from-code`（代码 → 简历经历）

**流程**：
1. **定位仓库**：本地路径优先（用 git/文件工具）；否则用 `gh` 读远端 GitHub（README、代码、贡献）。
2. **挖掘贡献**：读 README/架构/关键代码；用 `git log --author=<用户>`（或 gh 的贡献视图）**只统计用户本人的提交**，识别技术亮点（性能、架构、难点、优化，对应 14 维度）。
3. **产出**：
   - 1 段可直接进简历的项目经历（STAR + 量化，遵循主 skill 规则）；
   - 一份"亮点证据清单"：每个亮点对应到具体 commit/文件，供面试防御。
4. **边界**：只基于代码中**真实存在**的证据；不编造指标；无法从代码验证的量化留占位并提示用户补充。

**references/code-mining.md**：如何从代码与 commit 提炼亮点、14 优化维度到代码信号的映射、量化来源建议。

### 4.2 `resume-mock-interview`（简历 → 面试题）

**流程**：
1. 逐个项目经历，生成分层问题（基础实现 / 技术选型 / 难点排查 / 优化深挖 / 相关八股）。
2. 每题附**参考回答要点 + 可能的追问（follow-up）**。
3. 覆盖 `resume-rules.md` 中"面试防御清单"6 问（业务流程、个人职责、最难的 bug、技术选型理由、可量化效果、是否上线）。

**references/interview-bank.md**：分层提问框架 + 面试防御清单 + 按技术领域的常见追问。

### 子 skill 自包含原则

每个子 skill 只带自己需要的规则片段（不跨目录 `../` 引用主 skill 的 references），以便独立分发与跨平台加载。主 skill 拥有完整规则库。

## 5. references 知识库

- **主 skill `resume-optimizer`**：
  - `resume-rules.md`（现有，强化：补充中英差异钩子、JD 匹配钩子）
  - `cn-na-market.md`（**新增**）：中英职场简历差异 + CN↔NA 转换规则表。调研已完成，覆盖中国侧（`docs/research/2026-07-02-cn-resume-norms.md`）与中↔北美双向转换（`docs/research/2026-07-02-cn-na-conversion-guide.md`，含 10 维度转换表 + 美/加反歧视法对 header 的约束）。实现阶段将其提炼为 skill reference。
  - `jd-matching.md`（**新增**）：JD 解析方法 + 后端/AI Agent/算法岗偏向策略。
  - `export-formats.md`（**新增**）：各格式导出说明与模板变量约定。
  - `guide-1..6.md`（现有 liyupi 6 篇，重命名为 ASCII，内容保留）。
- **`resume-from-code`**：`code-mining.md`。
- **`resume-mock-interview`**：`interview-bank.md`。

## 6. LaTeX 模板与真实性红线

### 模板

- `templates/latex/resume-cn.tex.placeholder`、`resume-na.tex.placeholder`：**空占位**，等用户填充其 LaTeX 模板。
- `templates/latex/TEMPLATE_GUIDE.md`：说明占位变量约定，使用 `<<VAR>>` 形式（如 `<<NAME>>`、`<<EDUCATION>>`、`<<PROJECTS>>`），供用户与自传模板对齐。
- Export 模式支持用户 `--template <path>` 传入自己的模板。
- 辅助格式：HTML（单页可打印）、Markdown、JSON Resume。

### 贯穿所有能力的真实性红线（延续现有 skill）

- 不编造学历、工作年限、公司身份、无法验证的指标。
- 包装措辞可以，但每个亮点都要能在面试中被 defend。
- `resume-from-code` 的每个亮点必须有代码证据支撑。
- 无法验证的量化用占位符标注并提示用户确认，而非虚构。

## 7. 分阶段实现建议

为便于增量交付与评审，建议实现分阶段：

- **阶段 A（脚手架 + 迁移）**：建立插件目录结构、双平台清单、迁移现有 SKILL.md 与 references、更新 `agents/openai.yaml`、README 骨架。产出可加载的空套件。
- **阶段 B（主 skill 5 mode）**：实现 `resume-optimizer` 的 Polish/Review/JD-Match/Localize/Export，补 `jd-matching.md`、`cn-na-market.md`（由已完成的中↔北美调研提炼）、`export-formats.md`、LaTeX 占位模板与 TEMPLATE_GUIDE。
- **阶段 C（2 子 skill）**：实现 `resume-from-code` 与 `resume-mock-interview` 及各自 references。
- **阶段 D（示例 + 打磨）**：脱敏示例、README 中英完善、跨平台加载验证。

## 8. 成功标准

- 插件在 Claude Code 与 Codex 均可加载，各 skill 触发描述精准。
- 6 大能力各有清晰入口，输出符合 `resume-rules.md` 与 `cn-na-market.md`。
- LaTeX 导出走通（用占位模板 + 一个示例真实模板验证）。
- 真实性红线在所有能力中被强制执行。
- 开源门面（README 中英、examples、LICENSE）齐备。

## 9. 非目标（YAGNI）

- 不做在线服务/网页/后端；纯本地 Agent skill。
- 不做自动投递/爬取招聘平台。
- 不内置 PDF 渲染引擎（LaTeX 编译交给用户本地 `xelatex`/`latexmk`；仅生成 `.tex`）。
- 交互式模拟面试、毒舌点评为后续可选增强，本期不实现。
