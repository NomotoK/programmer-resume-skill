# 程序员简历技能套件

一套跨平台（Claude Code + OpenAI Codex）的插件，面向**计算机 / 软件技术岗求职简历** —— 润色、点评、JD 匹配、中英（中国↔北美）适配、代码转简历经历、模拟面试，并以 LaTeX 为首选导出格式。

## 能力一览

六项能力，归入三个 skill：

| 能力 | 所属 skill | 做什么 |
|---|---|---|
| **润色**（重写） | `resume-optimizer` | 把空泛的描述改写为 STAR + 量化结果（14 个优化维度）。可作用于整份简历或单个项目/单条 bullet。无法核实的指标会标 `<<CONFIRM: …>>` —— 绝不编造。 |
| **点评**（评审） | `resume-optimizer` | 分层反馈：🔴 致命 / 🟡 重要 / 🟢 可选。每条都引用原文并给出具体修改建议。 |
| **JD 匹配** | `resume-optimizer` | 解析岗位 JD，提取关键词/能力项，重排序、增删、调整技术偏向。内置后端 / AI Agent 应用开发 / 算法岗偏向策略。 |
| **中英适配**（CN↔NA） | `resume-optimizer` | **重塑结构**而非逐句翻译，在中国校招简历与北美简历之间互转。详见下方 *CN↔NA：是重塑，不是翻译*。 |
| **代码 → 简历** | `resume-from-code` | 读取项目仓库 + 你自己的 git 历史，挖掘真实技术亮点，产出一段可辩护的项目经历（STAR / X-Y-Z）+ 证据清单。 |
| **模拟面试** | `resume-mock-interview` | 把每个项目转成分层题库，覆盖 L1–L5 五层（实现 → 八股），每题给参考要点 + 可能的追问，并附 6 题防御集。 |

`resume-optimizer` 同时负责**导出**（LaTeX 优先；Markdown / HTML / JSON 为备选）—— 见下方 *模板与导出*。

## 安装

**Claude Code：** `/plugin` 添加本仓库为 marketplace/plugin，或将 `skills/*` 复制到你的 skills 目录。

**OpenAI Codex：** 作为插件安装（`.codex-plugin/plugin.json`），或将 `skills/*` 复制到 `~/.codex/skills/`。

两份 manifest（`.claude-plugin/plugin.json`、`.codex-plugin/plugin.json`）指向同一棵 `skills/` 树 —— 一份源码，两个运行时。没有任何 skill 硬编码宿主专属的工具名（已用 `grep -rniE "Read tool|WebFetch|web_fetch" skills` 验证）。

## 使用方式

直接用自然语言提问。各模式可链式调用（常见连招：点评 → 润色 → JD 匹配 → 中英适配 → 导出）。

- *"润色我的简历。"*
- *"点评这份简历，告诉我哪些是致命问题。"*
- *"按这个 JD 调整：……"*
- *"导出适合北美的英文版。"*
- *"从这个仓库生成一段项目经历：/path 或 GitHub URL。"*
- *"给我的简历项目出面试题。"*
- *"导出为 LaTeX（中文 / 北美 / 我自己的模板）。"*

## CN↔NA：是重塑，不是翻译

中国校招简历与北美简历之间的"本地化"是**结构性重塑**，不是逐句翻译。具体而言：

- **CN→NA：** 硬删除照片 / 年龄 / 性别 / 身份证 / 籍贯 / 政治面貌 / 详细地址 / 期望薪资；把微信换成 LinkedIn；去掉技能分级（了解/熟悉/熟练掌握）；把"负责"类描述改写为 `Led / Built / Designed` + X-Y-Z（"通过做 Z 达成 Y，从而实现 X"）；强制一页（应届）；删除 CET；教育经历放工作之后。
- **NA→CN：** 恢复技术栈行 + STAR；加上求职意向 + 毕业时间；恢复 了解/熟悉 分级；可选加排名 / CET；按学校声誉（985/211）重排教育经历。

完整规则：[`skills/resume-optimizer/references/cn-na-market.md`](skills/resume-optimizer/references/cn-na-market.md)，原始调研见 [`docs/research/`](docs/research/)。

## 模板与导出

导出以 **LaTeX 为首选**。仓库在 [`templates/latex/`](templates/latex/) 下内置两个模板：

- `resume-cn.tex` —— 中文；用 **xelatex** 编译（需要 `ctex`）。
- `resume-na.tex` —— 英文 / 北美导向；xelatex 或 pdflatex。

skill 会替换 11 个身份/教育类 `<<TOKEN>>`（姓名、邮箱、电话、GitHub 用户名、语言成绩、学校、GPA、日期），并按模板自带的宏（`\resumeProjectHeading{...}{...}{...}` + `\resumeItem{...}` + 技能 `\item`s）生成项目/工作/技能正文，供你直接粘贴覆盖虚构示例块。skill **不负责编译** —— 它把 `.tex` 交给你运行 `xelatex`。

**使用你自己的模板：** 把 `.tex` 放进 `templates/latex/`（或给 Export 指定任意路径：*"export with template `<path>`"*）。你的模板必须使用上述同名 `<<TOKEN>>` 才能被自动填充；Export 仍会按宏格式生成正文供你粘贴。完整 token 表与正文宏约定见 [`templates/latex/TEMPLATE_GUIDE.md`](templates/latex/TEMPLATE_GUIDE.md)。

备选格式：Markdown（[`templates/markdown/resume.md`](templates/markdown/resume.md)）、HTML（[`templates/html/resume.html`](templates/html/resume.html)）、JSON Resume（[`templates/json/resume.schema.json`](templates/json/resume.schema.json)）。

## 隐私

这些 skill **完全在你本地的 agent 会话中运行**。它们不会把你的简历上传到任何地方，不调用宿主运行时之外的任何外部 API，**绝不自动投递**到任何雇主或招聘平台。所有文件读取、git/gh 命令、搜索都通过宿主运行时提供的工具完成。导出产物只落在你的工作区，由你审阅和决定后续动作。

## 真实性红线

所有能力共享同一条规则：**包装措辞，绝不编造。** 如果某个指标无法从证据（用户的简历、仓库或 git 历史）核实，skill 会发出 `<<CONFIRM: …>>` 标记并予以提示。模拟面试 skill 会把经不起推敲的claim 反馈为润色建议。[ `examples/`](examples/) 中的示例均为虚构 —— 请勿复制进真实简历。

## 示例与规格文档

- **完整示例**（用同一位虚构应届后端简历跑通每项能力）：[`examples/`](examples/) —— 入口 [`examples/README.md`](examples/README.md)。
- **设计规格**（能力定义、架构、决策依据）：[`docs/superpowers/specs/2026-07-02-resume-skill-suite-design.md`](docs/superpowers/specs/2026-07-02-resume-skill-suite-design.md)。
- **计划与进度**（15 任务拆解）：[`docs/superpowers/plans/2026-07-03-resume-skill-suite.md`](docs/superpowers/plans/2026-07-03-resume-skill-suite.md)。
- **CN↔NA 调研底稿：** [`docs/research/`](docs/research/)。

## 仓库结构

```
.claude-plugin/plugin.json        Claude Code manifest
.codex-plugin/plugin.json         OpenAI Codex manifest（同一棵 skills/）
agents/openai.yaml                Codex agent 接口
skills/
  resume-optimizer/               主 skill：润色 / 点评 / JD 匹配 / 中英适配 / 导出
    SKILL.md + references/        resume-rules、jd-matching、cn-na-market、export-formats、guides 1–6
  resume-from-code/               代码 → 项目经历
    SKILL.md + references/        code-mining
  resume-mock-interview/          简历 → 面试题库
    SKILL.md + references/        interview-bank
templates/
  latex/                          resume-cn.tex、resume-na.tex、TEMPLATE_GUIDE.md
  markdown/  html/  json/         备选导出格式 + JSON schema
examples/                         7 个虚构文件，演示每项能力
scripts/validate.py               结构校验器（skills / refs / manifests / 模板变量）
tests/                            校验器的 unittest 测试套件
```

## License

MIT
