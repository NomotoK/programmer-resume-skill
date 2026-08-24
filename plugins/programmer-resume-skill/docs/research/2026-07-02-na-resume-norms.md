# 北美（美国 + 加拿大）软件 / 计算机 / AI 岗位简历规范研究报告

> 研究日期：2026-07-02。本文件是 `skills/resume-optimizer/references/cn-na-market.md` 的**北美侧原始素材**，与中国侧 `2026-07-02-cn-resume-norms.md` 对称；双向转换见 `2026-07-02-cn-na-conversion-guide.md`。
>
> 研究方法：经 deep-research 多智能体工作流（5 检索角度 → 抓取 24 源 → 112 条断言 → 25 条三票对抗式核验），**23/25 通过、2 条被否决**，另对工作流标注的覆盖空白（工作授权、文件命名/渠道、GPA 阈值、扫描时长、AI/ML 专项、求职信）做了补充检索。法律类断言锚定一手政府/法学院源（EEOC、Cornell LII、加拿大 CHRC、OHRC）；实务类锚定招聘方与高校职业中心（Stanford、MIT、Harvard、Tech Interview Handbook、Stack Overflow Blog hiring-manager、Google/Bock）。每条结论附 URL。

## 落地清单（TL;DR）

- **头部字段**：姓名、电话、专业邮箱、城市+州/省、LinkedIn、GitHub/作品集（技术岗推荐）。**绝不放**照片、出生日期/年龄、性别、婚姻/家庭状况、宗教、国籍/出生地、SSN/SIN、健康/残疾——这不是"客气"，而是美/加反歧视法使雇主不能索要/考量这些字段，写了只增偏见风险无任何收益。
- **工作授权**：非公民可加一行，如 *"Authorized to work in the U.S. for any employer without sponsorship"*；是否写有争议（有高校职业中心建议不写、留在 ATS 表单），但对外国姓名/需 H-1B 者是有效信号。
- **篇幅**：新毕业生 / 经验少者**严格 1 页**；有经验者 1–2 页，只保留最近 10–15 年；学术 CV（含论文/演讲/推荐人，无页数限制）只在科研/学术岗用——Harvard 明确即使 PhD 找工业界也用 résumé 而非 CV。
- **分区顺序**：(可选 Summary/Headline) → Contact → Skills → Experience → Education → Projects → (可选 Awards/Certs)；倒序；在校学生或 <3 年经验把 Education 放 Work 之上。**无"自我评价"段、无软技能空话、Objective 已过时**。
- **子弹点**：每条以**强动词过去式开头**（Led / Built / Designed / Reduced / Optimized），**绝不用 "Responsible for"**。遵循 Google X-Y-Z 公式：*"Accomplished [X] as measured by [Y], by doing [Z]"*——先抛影响+数字，再给基线与方法。
- **技能区**：紧凑的分类单行（Languages / Frameworks / Cloud / Tools），**不分级、不画星级/进度条**；列了即默认你会。精确匹配 JD 关键词，缩写首次展开。
- **教育**：学位 + 学校 + 地点 + 毕业年份；**GPA 仅当 ≥3.5/4.0 才写**，无专业排名、无 CET/英语等级（英语默认会）；相关课程仅新毕业生写 4–8 门；拿到学位后删高中；有经验者避免过旧的毕业年份（年龄信号）。
- **项目 vs 工作**：新毕业生以 Projects 打头（个人项目、OSS、hackathon、capstone），**必须带 GitHub/可访问链接**；有经验者 Experience 在前。
- **语气**：自信、impact-first 的自我推销是**预期**（不是傲慢）；用数字说话；6–7.4 秒初筛，关键信息一眼可见。
- **ATS**：~99% 的财富 500 强用 ATS，**75%+ 简历在被人看之前已被 AI/ATS 过滤**。文本可选中 PDF、单栏、标准黑色字体、标准小节标题、无表格/图表/页眉页脚、关键词织入；联系信息放在正文顶部**而非 Word/Google Docs 的"页眉"区**（ATS 读不到页眉）。
- **文件与投递**：PDF（文本可选中），标准字体 ≥10pt，0.5" 边距；命名 `FirstLast_Resume.pdf`（忌 `resume.pdf` / `resume_final(5).pdf`）。渠道优先级：**内推 > 公司 ATS 直投（Greenhouse/Lever/Ashby）> LinkedIn Easy Apply**；同公司勿海投多岗。

## 维度 1：个人信息 / 头部（法律驱动）

北美的头部字段**由反歧视法定形**——不是风格选择，而是法律使雇主不能在录用前索要或考量受保护类别信息，故写了无收益且引偏见。

**必写**：姓名（醒目）、专业邮箱（醒目）、电话、城市 + 州/省（**非完整街道地址**）、LinkedIn、GitHub/作品集（技术岗）。
**绝不写**：照片、出生日期/年龄、性别、婚姻/家庭状况、宗教、国籍/出生地、SSN/SIN、健康/残疾/基因信息。不使用人称代词（I / me / we）。

| 字段 | 北美惯例 | 根因 |
|---|---|---|
| 姓名 / 邮箱 / 电话 | 必写，醒目 | 基本联系方式 |
| 城市 + 州/省 | 写；完整街道地址不写 | 隐私 + 反歧视（住址可暴露阶层/种族） |
| LinkedIn | **必写**（≈中国不用 LinkedIn 的镜像） | 北美技术简历标配 |
| GitHub / 作品集 | 技术岗**推荐**（profile 体面才放） | 可直接验证代码能力 |
| 照片 | **绝不**（外貌类岗位如演员/模特属 BFOQ 例外，与 SWE/ML 无关） | EEOC：录用前"不应"索要照片 |
| 出生日期 / 年龄 | 绝不 | ADEA（40 岁以上）/ CHRA / OHRC 均禁 |
| 性别 / 婚姻 / 家庭 / 宗教 / 性取向 | 绝不 | Title VII / CHRA 受保护类别 |
| 国籍 / 出生地 / SSN / SIN | 绝不 | 国籍歧视 + 反欺诈 |
| 健康 / 残疾 / 基因 | 绝不 | ADA / GINA |

**美国法律锚点**：EEOC 执行的联邦法禁止基于种族、肤色、宗教、性别（含跨性别状态、性取向、怀孕）、原国籍、年龄（40+）、残疾、基因信息的歧视；录用前询问须限于"判定资格所必需"，种族/性别/原国籍/年龄/宗教被明确判为无关；雇主不得在 offer 前做残疾询问、不应在 offer 前索要照片（照片仅可在 offer 接受后获取）。基于受保护特征拒聘属 Title VII（42 U.S.C. § 2000e-2(a)(1)）下的不利雇佣行为。
来源：[EEOC Prohibited Employment Policies/Practices](https://www.eeoc.gov/prohibited-employment-policiespractices) · [Cornell LII — Title VII](https://www.law.cornell.edu/wex/title_vii) · [Stanford Career Education](https://careered.stanford.edu/sites/g/files/sbiybj22801/files/media/file/resume-and-cover-letter-examples.pdf)

**加拿大法律锚点**：《加拿大人权法》（CHRA）列举 13 项联邦禁止理由——种族、民族/原国籍、肤色、宗教、年龄、性别、性取向、性别认同/表达、婚姻状况、家庭状况、残疾、基因特征、已获赦免的定罪——与简历上惯例删除的字段一一对应。省级法典镜像：安省 OHRC 列举年龄、血统/肤色/种族、公民身份、族裔/原籍、信仰、残疾、家庭状况、婚姻状况（含单身）、性别认同/表达、性别、性取向，并明确把"就业"列为受保护社会领域，故简历筛选落在法条范围内。魁省 CDPDJ 在此基础上另加民事状况、政治信念、语言、社会条件等。
来源：[CHRC — About Discrimination](https://www.chrc-ccdp.gc.ca/individuals/human-rights/about-discrimination) · [OHRC — Ontario Human Rights Code](https://www.ohrc.on.ca/en/ontario-human-rights-code)

> **与中国侧的关键差异**：中国技术岗照片可选、年龄/籍贯有争议但常见、LinkedIn 基本不用；北美这些字段要么绝不放、要么是必写。CN→NA 转换时须**硬删**照片/年龄/性别/身份证/籍贯/政治面貌/婚姻/完整地址/期望薪资。

## 维度 2：工作授权 / 签证说明（NA 专有概念）

中国大陆境内求职无此概念；北美对非公民是真实信号。

**常见措辞**（放头部或 Summary 末一行）：
- *"Authorized to work in the U.S. for any employer without sponsorship."*
- *"No visa sponsorship required."*（公民 / 绿卡）
- *"Authorized to work in Canada without sponsorship."*
- 需 H-1B 等：*"Will require visa sponsorship for employment."*（或仅在 ATS 表单勾选）

**争议**：Texas Tech 大学职业中心**建议不写**签证状态、留在投递表单；Georgetown 指出雇主的标准两问（"是否合法授权在美工作？""现在或将来是否需要签证担保？"）通常在 ATS 表单而非简历上回答。但对外国姓名、OPT/STEM-OPT 期内的 F1、或需赞助者，简历上一行明确措辞可减少被误筛。
来源：[CV Wizard — Citizenship in Resume](https://www.cvwizard.com/en/articles/citizenship-in-resume) · [Georgetown Career Center — Sharing Immigration Status](https://careercenter.georgetown.edu/diversity-career-resources/international-students/job-search-in-the-us/sharing-your-immigration-status/) · [Texas Tech International Student Resources](https://www.depts.ttu.edu/careercenter/careerdevelopment/international.php) · [Workplace SE — work authorizations on resume](https://workplace.stackexchange.com/questions/14972/where-to-show-local-work-authorizations-in-a-resume) · [r/f1visa 社区讨论](https://www.reddit.com/r/f1visa/comments/1knjxwj/should_i_mention_authorized_to_work_in_the_usa_no/)

> 注意：OPT/STEM-OPT 期间"授权工作"≠"不需赞助"——三年后仍需 H-1B，雇主看长期。措辞要诚实。

## 维度 3：篇幅与 CV vs Resume

**Industry résumé**：密集、基于事实、篇幅受限的"教育+经验+技能+成就"摘要。**Academic CV**：无篇幅限制，加论文/演讲/推荐人，仅用于学术/科研岗。

| 阶段 | 篇幅 |
|---|---|
| 新毕业生 / 经验少 | **严格 1 页** |
| 有经验 | 1–2 页，只留最近 10–15 年 |
| 学术 / 科研岗 | CV，无限制 |

Harvard FAS Mignone Center 明确：**即使 GSAS PhD 找工业界（非科研）也用 résumé 而非 CV**。
来源：[MIT CAPD](https://capd.mit.edu/channels/make-a-resume-cover-letter-cv/) · [Stanford Career Education](https://careered.stanford.edu/sites/g/files/sbiybj22801/files/media/file/resume-and-cover-letter-examples.pdf) · [Harvard FAS Career Services](https://careerservices.fas.harvard.edu/channels/create-a-resume-cv-or-cover-letter/)

> **被核验否决的断言**：有说法称"技术/工程岗因项目多可破例占第二页"——经 1-2 票被否决，**有经验的技术候选人遵循标准篇幅规范，无特殊多页豁免**。校招/新毕业生仍是 1 页铁律。

> 与中国侧一致点：校招 1 页、社招 2 页、PDF。差异：北美没有"两页要铺满"的执念，更看密度而非凑页；学术 CV 是北美独有区分。

## 维度 4：分区与顺序

**标准模块**：(可选 Summary / Headline) → Contact → Skills → Experience → Education → Projects → (可选 Awards / Certifications)。

- **倒序**（reverse-chronological）是 ATS 与招聘方的硬预期。
- **在校学生或 <3 年经验**：Education 放 Work Experience **之上**；否则 Experience 优先，Education 下沉。
- **无"自我评价"段**，无软技能空话；**Objective 已过时**（雇主已知你的目标是找工作）。
- 小节标题用**标准英文**（Experience / Education / Skills / Projects），不用符号/图标——为 ATS 解析。

来源：[Tech Interview Handbook — Resume Guide](https://www.techinterviewhandbook.org/resume/) · [Stanford Career Education](https://careered.stanford.edu/sites/g/files/sbiybj22801/files/media/file/resume-and-cover-letter-examples.pdf) · [MIT CAPD](https://capd.mit.edu/channels/make-a-resume-cover-letter-cv/)

> 与中国侧差异：中国有"求职意向"（推荐）与"自我评价"（可选，需具体）；北美两者都不要——求职意向过时，自我评价不存在。中国校招按"学校强弱"决定 Education 位置；北美按"经验年限"决定。

## 维度 5：子弹点写法（X-Y-Z，impact over responsibility）

**铁律**：每条以**强动词过去式开头**（Led / Built / Designed / Reduced / Optimized / Shipped / Migrated / Automated），**绝不用 "Responsible for…" / "Duties included…"**（职责清单是北美简历头号弱弹模式）。当前在任角色才用现在时；不用人称代词（I / we）。

**Google X-Y-Z 公式**（Laszlo Bock，前 Google 人力高级副总裁，2014 原始表述，核验 3-0 通过）：

> *"Accomplished [X] as measured by [Y], by doing [Z]."*
> 以主动动词开头 → 数字化结果 → 给比较基线 → 说明实现路径。

范例对比：
- ❌ *"Responsible for maintaining the API."*
- ✅ *"Reduced API p99 latency from 800ms to 120ms by introducing a Redis read-through cache, cutting infra cost 18%."*

Bock 原文佐证：加 "12% ($1.2M)" 让子弹更有力，"(美元金额)" 提前回答评审"这是不是大事"的疑问，"如何做到"增加可信度并展示强项。Stanford 独立给出同款建议：用动词、避免 "duties included"、量化（如 "membership increased by 25%"）。
来源：[Bock — My Personal Formula for a Better Resume (LinkedIn Pulse, 2014)](https://www.linkedin.com/pulse/20140929001534-24454816-my-personal-formula-for-a-better-resume) · [Stanford Career Education](https://careered.stanford.edu/sites/g/files/sbiybj22801/files/media/file/resume-and-cover-letter-examples.pdf) · [Resume Worded — Action Verbs](https://resumeworded.com/software-engineer-resume-action-verbs) · [freeCodeCamp — SE Resume](https://www.freecodecamp.org/news/writing-a-killer-software-engineering-resume-b11c91ef699d/)

> 与中国侧：中国用 STAR + 技术栈行 + "负责/参与/主导"动词；NA 用 action-verb + X-Y-Z、数字前置、删 "Responsible for"。CN 的数字（QPS、响应时间）翻译过来在 NA 是**金子**，直接保留。

## 维度 6：技能区（不分级）

**紧凑的分类单行**，**不标熟练度等级、不画星级/进度条**：

```
Languages: Python, Go, TypeScript  ·  Frameworks: React, FastAPI, PyTorch
Cloud/Tools: AWS (ECS, S3, DynamoDB), Kubernetes, Terraform, Docker
```

Hiring-manager 共识（Stack Overflow Blog，访谈 ~24 位 Google/Facebook/Microsoft 招聘方，核验 3-0）：**"别费心标你的熟练度——你列了，招聘经理就默认你够熟。"** 自评等级主观且无意义（DEV Community、r/EngineeringResumes、Workplace SE 印证）。商业简历站偶尔建议 Expert/Proficient/Familiar 文本分组，属轻微让步而非反证。

- **精确匹配 JD 关键词**（ATS 按词检索）。
- 缩写首次展开一次：*"Amazon Web Services (AWS)"*。
- 别把技能埋在第二页。
来源：[Stack Overflow Blog — Effective Developer Resume](https://stackoverflow.blog/2020/11/25/how-to-write-an-effective-developer-resume-advice-from-a-hiring-manager/) · [MIT CAPD](https://capd.mit.edu/channels/make-a-resume-cover-letter-cv/) · [Stanford Career Education](https://careered.stanford.edu/sites/g/files/sbiybj22801/files/media/file/resume-and-cover-letter-examples.pdf)

> 与中国侧最大差异之一：中国后端用"了解/熟悉/熟练掌握/精通"分级（校招禁"精通"）；**北美不分级**。CN→NA 须剥掉等级。

## 维度 7：教育背景

**必含**：学位、学校、地点、毕业年份（或预计毕业）。

| 项 | 北美惯例 |
|---|---|
| GPA | **仅当 ≥3.5/4.0 才写**；<3.5 一律不写 |
| 专业排名 / 百分比 | **不写**（NA 无此概念） |
| CET / 英语等级 | **不写**（英语默认会；只列其他语种） |
| 相关课程 | 仅新毕业生写，精选 4–8 门对口课程；有 1–2 年经验后删 |
| 高中 | 拿到学位后删 |
| 毕业年份 | 写；但有经验者避免过旧年份（年龄信号） |

**SWE 特例**：相对其他行业，CS 的 GPA 权重更低——项目、实习、技能常比 GPA 更重要（社区共识）。但 Google 等大厂及金融/量化机构有**硬性 GPA 过滤**，故目标若是这些且 ≥3.5 则必写。GPA 取整：3.48 → 3.50（两位小数）一般可接受。
来源：[Tech Interview Handbook](https://www.techinterviewhandbook.org/resume/) · [Resume Worded — GPA on Resume](https://resumeworded.com/gpa-on-resume-key-advice) · [Forage](https://www.theforage.com/blog/basics/gpa-on-resume) · [Coursera](https://www.coursera.org/articles/gpa-on-resume) · [Indeed](https://www.indeed.com/career-advice/resumes-cover-letters/gpa-on-resume) · [r/EngineeringResumes](https://www.reddit.com/r/EngineeringResumes/comments/17hgu9n/how_low_is_too_low_to_not_put_gpa_on_resume_when/)

> 与中国侧：中国 GPA 前 30% 才写、可写"专业排名前 5%/10%"、CET-4/6 是标配加分项；北美 GPA≥3.5 才写、不写排名、删 CET。CN→NA：前 X% → 转 GPA/4.0（若 ≥3.5）或删；删 CET。

## 维度 8：项目 vs 工作经历

- **新毕业生**：以 Projects 打头——个人项目、开源贡献（OSS）、hackathon、课程 capstone。Skills 靠前，实习当作真实工作（带公司/头衔/日期 + 量化子弹）。
- **有经验者**：Experience 在前，Projects 缩小或省略。
- **NA 预期每个项目带 GitHub / 可访问链接**（CN 常省略）——NA 把链接视为可验证证据。
- 开源贡献对 AI/ML 新毕业生与转行者是"作品集替代品"：代码公开，招聘方可直接看文档/结构/测试覆盖/PR 质量，无需此前工作经验即可验证生产级编码能力。
来源：[Tech Interview Handbook](https://www.techinterviewhandbook.org/resume/) · [MIT CAPD](https://capd.mit.edu/channels/make-a-resume-cover-letter-cv/) · [Comet — Contributing to Open-Source AI](https://www.comet.com/site/blog/contributing-to-open-source-ai/)

> 与中国侧一致（新毕业生项目为主、实习 >3 个月、工作 3 年后不写实习）；差异：NA 强制带链接。

## 维度 9：语气、文化与扫描时长

**自信、impact-first 的自我推销是预期**——不是傲慢。用数字与证据说话，把所有权（ownership）动词与影响前置；删除谦辞与软技能空话。这是与中国"忌空泛自夸、也忌过度谦虚、用客观证据"的平衡点不同的地方：NA 更偏向**放大**成就与影响。

**扫描时长**：著名的"6 秒"说法源自 TheLadders 2012 眼动研究，更新引用值为**平均 7.4 秒**——但这只是**初筛淘汰扫描**：通过初筛的简历会获 30 秒–1 分钟更细审阅。含义：关键信息（姓名/目标岗位/最近 role/最强影响）须一眼可见，简单干净布局胜出。
来源：[HR Dive — eye-tracking 7.4 seconds](https://www.hrdive.com/news/eye-tracking-study-shows-recruiters-look-at-resumes-for-7-seconds/541582/) · [Hughes Recruiting — 6-second review](https://hughesrecruiting.com/2024/06/17/what-is-the-6-second-resume-review-and-how-to-pass-it/) · [Distinct Recruitment — myth debunk](https://www.distinctrecruitment.com/uk/resources/blog/the-6-second-cv-recruitments-biggest-myth/)

**红旗（减分项）**：
1. "Responsible for…" 职责清单（头号弱弹）
2. 照片 / 受保护类别个人信息（法律风险 + 不专业）
3. Objective statement（过时）
4. 软技能空话堆砌（"team player / hard worker"）
5. 功能型格式（functional résumé，按技能而非时间组织）——ATS 与招聘方都反感
6. 错别字 / 标点混用 / 大小写不规范
7. 新毕业生超 1 页
8. 技术栈与岗位不匹配 / 过时技术
来源：[Inc — Google's 5 resume tips](https://www.inc.com/bill-murphy-jr/google-recruiters-say-these-5-resume-tips-including-x-y-z-formula-will-improve-your-odds-of-getting-hired-at-google.html) · [Stanford Career Education](https://careered.stanford.edu/sites/g/files/sbiybj22801/files/media/file/resume-and-cover-letter-examples.pdf)

## 维度 10：ATS（申请人追踪系统）—— 北美简历的"物理定律"

** prevalence**：约 **99% 的财富 500 强**使用某种 ATS（MIT CAPD；Jobscan 2024 给 98.4%，独立印证）。更关键：**75%+ 的美国简历在被人看之前已被 AI/ATS 过滤**，Workday / Greenhouse / Lever / iCIMS 把申请人收敛到约 10–15 人的短名单。

**为什么格式服从 ATS**：ATS 与简历库**按关键词检索**，故须把 JD 原词织入简历。ATS 与人类招聘方都**从上到下、从左到右读**——这是单栏布局的根本原因。

**ATS 友好的硬约束**：

| 做 | 不做 |
|---|---|
| 文本**可选中**的 PDF（从 Word/Google Docs 导出） | 扫描件 PDF / 图片 PDF |
| **单栏**布局 | 双栏/三栏（解析失败 #1 原因） |
| 标准黑色字体、≥10pt、0.5" 边距 | 花式字体、彩色、图标 |
| 标准小节标题（Experience/Education/Skills） | 自创标题 / 图标标题 |
| 联系信息放**正文顶部** | 放 Word/Google Docs 的**"页眉"区**（ATS 读不到页眉） |
| 缩写首次展开、JD 关键词原词 | 埋在第二页 / 缩写不展开 |

**双栏失败实证**（多源一致）：8 个 ATS 系统实测，双栏在 **7/8** 解析失败（解析器逐行从左到右读，把两栏合并成乱串）；单栏是解析成功率最大单一因子（+32 个百分点）；双栏侧边栏在 **Workday 上 41% 的简历**字段错配；2026 年 6 种布局基准测试中，单栏 100/100 完美解析，双栏降至 85/100 且唯一触发 critical 解析警告。
来源：[MIT CAPD](https://capd.mit.edu/channels/make-a-resume-cover-letter-cv/) · [Stanford Career Education](https://careered.stanford.edu/sites/g/files/sbiybj22801/files/media/file/resume-and-cover-letter-examples.pdf) · [Stack Overflow Blog](https://stackoverflow.blog/2020/11/25/how-to-write-an-effective-developer-resume-advice-from-a-hiring-manager/) · [QuickCV — I Tested 8 ATS Systems](https://quickcv.io/blog/i-tested-8-ats-systems-to-see-how-they-actually-parse-resumes) · [Resume Optimizer Pro — What makes a resume ATS-friendly](https://resumeoptimizerpro.com/blog/what-makes-a-resume-ats-friendly) · [ATS Verification — two-column](https://atsverification.com/blog/two-column-resume-ats-friendly/) · [iReformat — ATS formatting guide](https://ireformat.com/blog/ats-resume-formatting-guide)

> 与中国侧：中国无美式独立 ATS 生态，但大厂+平台有关键词/算法匹配打分。NA 的 ATS 是硬物理约束，**单栏 + 文本可选中 PDF + 标准标题**是底线。

## 维度 11：文件格式、命名与投递渠道

**格式**：文本可选中的 PDF；用 bullet 而非长段落；黑色文字、干净一致的标准字体；严格校对错别字；跳过过时的 Objective（以上为 Google 自家面向申请者的基础格式建议，Inc 引述）。

> PDF 偶发解析问题：部分 ATS 对 PDF 解析仍吃力，若雇主指定 .doc/.docx，**严格从其指定格式**（ORISE 2026）。

**命名**：`FirstLast_Resume.pdf`（最小）；可加目标岗位 `Jane_Doe_SWE_Resume.pdf`；用连字符或下划线分隔；**绝不** `resume.pdf` / `resume_final(5).pdf` / `简历.pdf`——招聘方下载数百份，清晰命名防丢件并显专业。

**投递渠道（优先级共识）**：

| 渠道 | 特点 |
|---|---|
| **内推（Referral）** | 转化率最高；内部背书。最强渠道 |
| **公司 ATS 直投**（Greenhouse / Lever / Ashby） | 直达 ATS，岗位最新、噪音少于 LinkedIn |
| Workday | 大企业常用；UX 笨重、常需重填资料、高量 |
| LinkedIn Easy Apply | 最快一键投，但**竞争最大、回复率最低**（"投递越易、申请人越多"） |

**技巧**：Google 搜索黑魔法 `site:boards.greenhouse.io [title] [location]` 或 `site:jobs.lever.co` 找直投岗位，比 LinkedIn 聚合更新更鲜、竞争更小。**同公司勿海投多岗**。
来源：[Inc — Google's resume tips](https://www.inc.com/bill-murphy-jr/google-recruiters-say-these-5-resume-tips-including-x-y-z-formula-will-improve-your-odds-of-getting-hired-at-google.html) · [ORISE — format your resume for AI screening](https://orise.orau.gov/internships-fellowships/blog/how-to-format-your-resume-for-ai-screening.html) · [r/ResumeCoverLetterTips — file naming](https://www.reddit.com/r/ResumeCoverLetterTips/comments/1qlrb5j/please_stop_naming_your_resume_file_resume/) · [Greenhouse — LinkedIn Apply integration](https://support.greenhouse.io/hc/en-us/articles/115005389566-LinkedIn-Apply-integration)

> 与中国侧：中国 BOSS 直聘霸主（64.5%）/ 内推 / 校招官网 / 牛客；LinkedIn 基本不用。NA 主力是公司 ATS + LinkedIn + 内推。命名 CN→NA：`姓名-岗位-学校-专业` → `FirstLast_Resume.pdf`。

## 维度 12：AI / ML 专项

**角色细分**（北美 2014 后从笼统 "data scientist" 分化出独立角色，简历关键词须对症）：**Data Scientist / Applied Scientist / Research Scientist / ML Engineer** 各自定位不同——投递须按具体角色调关键词。
来源：[Eugene Yan — Data Science Roles](https://eugeneyan.com/writing/data-science-roles/)

**Research vs Applied 框架**：
- **Research Scientist / 科研岗**：重视 arXiv 论文、顶会发表（NeurIPS / ICML / ACL / CVPR）、对开源模型的贡献——此处**学术 CV 格式**（含 Publications / Presentations / References）变得可取。
- **Applied / ML Engineer / 应用岗**：强调部署过的项目——GitHub、Kaggle 竞赛成绩、**Hugging Face Spaces 可交互 demo**（免费公开链接，简历可直接放）、模型卡（model card）。

**作品集载体**：Hugging Face Spaces 是托管交互式 ML 作品集的首选（"ML 的 GitHub"，50 万+ 模型）；GitHub 开源贡献是新毕业生与转行者的作品集替代品，招聘方可直接验证生产级编码能力（文档/结构/测试/PR 质量）。
来源：[Towards AI — ML Portfolio with HF Spaces](https://pub.towardsai.net/build-your-machine-learning-portfolio-using-hugging-face-spaces-a223aa57d813) · [Comet — Open-Source AI](https://www.comet.com/site/blog/contributing-to-open-source-ai/) · [Hugging Face 开岗](https://apply.workable.com/huggingface/?lng=en)

> 注：工作流对 AI/ML 专项的"论文权重 vs 量化影响子弹"权衡、arXiv/HF/Kaggle 的相对分量，核验证据偏薄，列为**开放问题**见末节。

## 维度 13：求职信与 Summary vs Objective（2026 演化中）

**求职信（Cover Letter）2026**：未死，但"写就要写好"。约 **89% 的招聘方仍期望随简历附求职信**；在 AI 生成申请泛滥的时代，**个性化、真实的**求职信让真人脱颖而出（泛泛或 AI 生成的反而减分）。**不再是默认必交**——一键 Easy Apply 与招聘方过载使其常为可选。**平均水平的求职信不如不写**。SWE 特例：技术岗常不要求，若要会在 JD 写明。
来源：[Forbes — why cover letters aren't dead](https://www.forbes.com/sites/josephliu/2025/11/11/hiring-experts-reveal-why-cover-letters-arent-dead-yet/) · [Intuit — SWE cover letter](https://www.intuit.com/blog/social-responsibility/job-readiness/software-engineer-cover-letter-examples/) · [r/jobsearchhacks — cover letters in 2026](https://www.reddit.com/r/jobsearchhacks/comments/1qi03iz/are_cover_letters_necessary_in_2026/)

| 写的情况 | 可跳过的条件 |
|---|---|
| JD 明确要求 | 标 optional 且无独特内容可加 |
| 转行 / 非传统背景 | 一键 Easy Apply 无提示 |
| 有内推/特定连接可提 | 简历已讲清全部故事 |
| 小公司/创业（fit 重要） | 高量技术岗（FAANG 鲜读） |
| 需解释空窗/搬迁/转型 | 海投 100+ 岗 |

**Summary vs Objective**：**Objective 已基本过时**；**Summary（经验者）/ Headline 受推荐**。Summary 回看成就（量化），Objective 前瞻"你想要什么"——后者雇主不关心。3+ 年经验用 Summary（如 *"Backend engineer with 6 years building scalable APIs in Go and Python; led migration to microservices serving 10M+ daily requests."*）；新毕业生/转行者若用 Objective，须围绕"你能带来的价值"而非"你想要什么"。也可用 "Profile" 标题规避过时的 "Objective" 字样。
来源：[r/resumes — skip objective/summary?](https://www.reddit.com/r/resumes/comments/1pg5tnk/should_i_skip_objective_and_summary_on_a_resume/) · [AiApply — objective vs summary](https://aiapply.co/blog/resume-objective-vs-summary)

## 维度 14：后 2023 的演化（AI 筛选 / 2024–2026 市场）

- **AI 驱动的简历/面试筛选工具不可靠且有偏见**：记者 Hilke Schellmann（《The Algorithm》）实测，一 AI 视频面试系统对一位**只说德语**的候选人按英语岗位评出 **73% 合格**（NPR 2025-10）。含义：通过 AI 初筛不保证公正，但**不通过则必死**——故 ATS 友好 + 关键词 + 量化仍是必须。
- **量化子弹在 2026 被强化而非削弱**：LLM 筛选工具倾向抽取指标/影响，X-Y-Z 风格更易被"读懂"。
- 2024–2026 科技招聘收缩是否改变了 1 页规则、referral vs Easy Apply 权重、双栏/图形设计的容忍度——核验证据不足，列为开放问题。
来源：[NPR — Are AI hiring tools any good? (2025-10)](https://www.npr.org/2025/10/03/nx-s1-5534959/are-ai-hiring-tools-any-good-this-journalist-found-widespread-bias-and-bugs) · [Resume Optimizer Pro — optimize resumes for AI](https://resumeoptimizerpro.com/blog/how-to-optimize-resumes-for-ai)

## 争议点（建议做成工具可配置项）

1. **工作授权行**：写（外国姓名/需赞助者减误筛）vs 不写（Texas Tech 建议留在表单）。默认：非公民且需表明"不需赞助"时写一行。
2. **Summary vs 无 Summary**：经验者用 vs 新毕业生可省。默认：3+ 年经验写 Summary，新毕业生用 Headline 或省。
3. **Objective**：基本过时，仅转行/新毕业生可用且须围绕"价值"。默认：不用。
4. **GPA**：≥3.5 写 vs SWE 一般权重低。默认：≥3.5 且新毕业生/目标大厂量化岗则写。
5. **单栏 vs 双栏设计**：ATS 友好铁定单栏 vs 现代 ATS（如部分 2026 系统）渐能解析双栏。默认：单栏（安全）。
6. **求职信**：默认不强制；JD 要求或转行/小公司才写且要个性化。
7. **完整地址 vs 仅城市**：美国仅城市+州；加拿大 Job Bank/OHRC 容许邮寄地址。默认：城市+地区。

> 这些多为源自反歧视法与 ATS 技术的**惯例**，非法定"简历法规"——在工具中以提示信息呈现，不硬编码。

## 核验中被否决的断言（排除）

- ❌ *Title VII 的一段宽泛转述*（0-3 票被否）：被否是**措辞/援引精度**问题，非 Title VII 本身有误——法律核心由 EEOC.gov + Cornell LII 一手源另立正确断言（见维度 1）。
- ❌ *技术/工程岗可破例占第二页*（1-2 票被否）：**有经验的技术候选人遵循标准篇幅规范**，无特殊多页豁免。

## 权威来源

**实务（招聘方 / 高校职业中心 / hiring-manager）**
- Tech Interview Handbook（Yangshun Tay，ex-Meta Staff Engineer）[techinterviewhandbook.org/resume](https://www.techinterviewhandbook.org/resume/)
- Laszlo Bock（前 Google SVP People Ops）X-Y-Z 原始公式 [LinkedIn Pulse 2014](https://www.linkedin.com/pulse/20140929001534-24454816-my-personal-formula-for-a-better-resume)
- Google 面向申请者的格式建议（经 Inc 引述）[Inc.com](https://www.inc.com/bill-murphy-jr/google-recruiters-say-these-5-resume-tips-including-x-y-z-formula-will-improve-your-odds-of-getting-hired-at-google.html)
- Stack Overflow Blog hiring-manager（Gergely Orosz，访谈 Google/FB/Microsoft 招聘方）[stackoverflow.blog](https://stackoverflow.blog/2020/11/25/how-to-write-an-effective-developer-resume-advice-from-a-hiring-manager/)
- Stanford Career Education [resume-and-cover-letter-examples.pdf](https://careered.stanford.edu/sites/g/files/sbiybj22801/files/media/file/resume-and-cover-letter-examples.pdf)
- MIT CAPD [capd.mit.edu](https://capd.mit.edu/channels/make-a-resume-cover-letter-cv/)
- Harvard FAS Career Services [careerservices.fas.harvard.edu](https://careerservices.fas.harvard.edu/channels/create-a-resume-cv-or-cover-letter/)
- freeCodeCamp [SE Resume](https://www.freecodecamp.org/news/writing-a-killer-software-engineering-resume-b11c91ef699d/) · Resume Worded · The Muse · Enhancv · Novoresume（商业印证源）

**ATS 实测**
- QuickCV [I Tested 8 ATS Systems](https://quickcv.io/blog/i-tested-8-ats-systems-to-see-how-they-actually-parse-resumes) · Resume Optimizer Pro [ATS-friendly](https://resumeoptimizerpro.com/blog/what-makes-a-resume-ats-friendly) / [for AI](https://resumeoptimizerpro.com/blog/how-to-optimize-resumes-for-ai) · ATS Verification [two-column](https://atsverification.com/blog/two-column-resume-ats-friendly/) · iReformat [formatting guide](https://ireformat.com/blog/ats-resume-formatting-guide) · ORISE [format for AI screening](https://orise.orau.gov/internships-fellowships/blog/how-to-format-your-resume-for-ai-screening.html)

**美国法律（一手政府 / 法学院）**
- EEOC [Prohibited Employment Policies/Practices](https://www.eeoc.gov/prohibited-employment-policiespractices) · Cornell LII [Title VII](https://www.law.cornell.edu/wex/title_vii) · usa.gov（反歧视）

**加拿大法律（一手）**
- CHRC [About Discrimination](https://www.chrc-ccdp.gc.ca/individuals/human-rights/about-discrimination)（CHRA 13 项理由）· OHRC [Ontario Human Rights Code](https://www.ohrc.on.ca/en/ontario-human-rights-code) · 魁省 CDPDJ · 加拿大 Job Bank [jobbank.gc.ca](https://www.jobbank.gc.ca/findajob/resources/write-good-resume)

**AI/ML 专项**
- Eugene Yan [Data Science Roles](https://eugeneyan.com/writing/data-science-roles/) · Towards AI [HF Spaces portfolio](https://pub.towardsai.net/build-your-machine-learning-portfolio-using-hugging-face-spaces-a223aa57d813) · Comet [Open-Source AI](https://www.comet.com/site/blog/contributing-to-open-source-ai/) · NPR [AI hiring tools (2025-10)](https://www.npr.org/2025/10/03/nx-s1-5534959/are-ai-hiring-tools-any-good-this-journalist-found-widespread-bias-and-bugs)

## 开放问题（证据不足，待后续补充）

1. LLM 简历筛选/排名（区别于传统关键词 ATS）在 2024–2026 如何改变关键词、格式、量化的最佳实践？是偏好还是惩罚 X-Y-Z 影响风格？
2. 非公民的最优工作授权措辞，该放简历还是仅放 ATS 表单？
3. 对 ML/AI 工程师与 Research Scientist，论文 / arXiv / Hugging Face model card / Kaggle 成绩 相对于 SWE 式量化子弹各占多大权重？何时学术 CV 反超？
4. 2024–2026 科技招聘收缩是否改变了 1 页规则、referral vs Easy Apply 的权重、或对双栏/图形设计的容忍度？
