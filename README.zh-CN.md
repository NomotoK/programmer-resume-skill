# 程序员简历技能套件

一套跨平台（Claude Code + OpenAI Codex）的插件，面向**计算机/软件技术岗求职简历**。

## 技能

| 技能 | 功能 |
|---|---|
| `resume-optimizer` | 简历润色、点评、JD 匹配、中英（中国↔北美）适配、导出（LaTeX 优先）。 |
| `resume-from-code` | 读取项目仓库 + 你的 git 历史，挖掘技术亮点，生成一段简历项目经历。 |
| `resume-mock-interview` | 把简历里的项目经历转成数十道分层面试题 + 参考要点。 |

## 安装

**Claude Code：** `/plugin` 添加本仓库，或将 `skills/*` 复制到你的 skills 目录。
**OpenAI Codex：** 作为插件安装（`.codex-plugin/plugin.json`），或将 `skills/*` 复制到 `~/.codex/skills/`。

## 使用

直接用自然语言：*"润色我的简历"*、*"从这个仓库生成一段项目经历"*、*"给我的简历项目出面试题"*、*"导出适合北美的英文版"*、*"按这个 JD 调整"*。

详见 `examples/` 与 `docs/superpowers/specs/`。

## 输出

LaTeX 优先（可在 `templates/latex/` 提供自己的 `.tex` 模板），另提供 Markdown/HTML/JSON。

## License

MIT
