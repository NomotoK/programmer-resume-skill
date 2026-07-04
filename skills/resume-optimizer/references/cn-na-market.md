# CN ⇄ NA Résumé Market Reference

> Distilled from three research docs in `docs/research/`:
> [`2026-07-02-cn-resume-norms.md`](../../../docs/research/2026-07-02-cn-resume-norms.md) (CN),
> [`2026-07-02-na-resume-norms.md`](../../../docs/research/2026-07-02-na-resume-norms.md) (NA, deep-research verified — 23/25 claims survived adversarial voting),
> [`2026-07-02-cn-na-conversion-guide.md`](../../../docs/research/2026-07-02-cn-na-conversion-guide.md) (conversion).
>
> **What this reference is.** Localize mode **reshapes**, it does not translate. Verbs, ordering, file name, and length are rewired to market conventions; facts and metrics are preserved. Several NA fields (photo / DOB / gender / marital / religion / SSN-SIN / health) are **law-driven exclusions**, not optional style — anchored in **Title VII / ADEA / ADA / GINA** (US) and the **Canadian Human Rights Act + provincial codes (OHRC)**. Law aside, most rules below are strong conventions surfaced as tool guidance, not statutory "résumé law".

## Quick-Reference Transformation Table

| Dimension | China (校招/社招) | North America (US/Canada) | CN→NA rule | NA→CN rule |
|---|---|---|---|---|
| **Photo** | Optional; formal headshot tolerated (never mandatory for tech) | **Never** (reveals race/sex/age → bias risk) | **Delete photo** | Optional slot; formal headshot only, never force |
| **Age / DOB / 性别 / 身份证 / 籍贯 / 政治面貌 / marital** | Age/籍贯 sometimes listed; ID/gender discouraged even in CN | **Forbidden** (Title VII / ADEA / CHRA) | **Hard-strip all nine fields** | May add age/grad-year; still skip ID/marital for tech |
| **Address** | Not needed (privacy) | City + State/Province (not full street) | Add city + region | Drop to none or city |
| **Work authorization** | Not a concept for domestic CN | "Authorized to work in US/Canada" or sponsorship need if non-citizen | **Add** work-auth line if non-citizen | Remove |
| **Contacts** | Phone + email mandatory; 微信 optional; GitHub/blog if has content; LinkedIn ~never | Phone, email, LinkedIn, GitHub/portfolio | 微信 → LinkedIn; keep GitHub | LinkedIn → (optional 微信); keep GitHub |
| **Length** | 校招 1p (≤2); 社招 ≤3; PDF | New-grad 1p; experienced 1–2p (10–15 yr window); PDF | Enforce 1p for new-grad | Compress to 1p; PDF |
| **求职意向 / Objective** | Common & recommended (岗位+城市) | Objective **outdated**; optional Summary | Convert 求职意向 → headline/Summary or delete | Summary → 求职意向 line |
| **自我评价 / Self-eval** | Exists, optional, must be concrete (≤3 lines) | **Does not exist**; no soft-skill blurbs | **Delete** (or fold facts into Summary) | Optionally add concrete 自我评价 ≤3 lines |
| **Education placement** | Strong school → top; weak → bottom; 社招 bottom | New grad → near top; experienced → bottom | Reorder by experience, not school prestige | New-grad fine at top; add tier if 985/211 |
| **GPA / rank** | GPA if top ~30%; 专业排名 前5%/10% | GPA only if ≥3.5/4.0; no percentile rank | 前 X% → drop or convert to GPA/4.0; drop if <3.5 | GPA/4.0 keep; may add 排名 if strong |
| **Bullets** | STAR + 技术栈 line; 负责/参与/主导 | Action verb + **X-Y-Z**; never "Responsible for" | Rewrite 负责 → Led/Built/Designed; front-load metric | Rewrite to STAR; keep 技术栈 explicit |
| **Skills** | Tiers 了解/熟悉/熟练掌握/精通 (校招 never 精通) | Compact categorized line; **no tiers** | Strip tiers → categorized list | Add tiers; align to JD keywords |
| **Honors 荣誉奖项** | Common section | Fold into Education or small "Awards" | Merge into Education | Can promote to 荣誉奖项 section |
| **CET-4/6** | Listed as English proficiency | Meaningless; drop (English implied) | **Delete CET** | Add CET if targeting CN |
| **Tone** | Evidence-based, humble; no puffery | Impact-first self-promotion, confident | Amplify ownership/impact | Soften; avoid 精通 / puffery |
| **File name** | `姓名-岗位-学校-专业` (校招) | `FirstLast_Resume.pdf` (or `FirstLast_SWE_Resume.pdf`) | Rename to English convention | Rename to CN convention |
| **Channel** | **BOSS直聘** / 内推 / 校招官网 / 牛客 | LinkedIn, company ATS, referrals | — | — |
| **ATS** | HR keyword-matches manually/algorithmically | Formal ATS parsing dominant (~99% of Fortune 500) | Aggressive JD keyword alignment; **单栏** plain layout | Keep JD-keyword alignment |

## Dimension 1 — Personal Info / Header

**CN norm.** Minimal: 姓名、电话、邮箱、求职意向 (岗位+城市)、毕业时间/学历. Phone/email mandatory (must be correct). GitHub/博客 only when there is real content. 微信 optional. **LinkedIn essentially never used** in mainland tech. Age/籍贯 contested → omitting is fine. 性别 / 身高 / 身份证 / 住址 / 政治面貌 / 民族 / 期望薪资 discouraged (期望薪资 goes in the platform field). Photo optional & contested; tech trend is none or formal headshot, never mandatory.

**NA norm.** name, phone, professional email, **city + state/province** (not full street), LinkedIn (mandatory in tech), GitHub/portfolio (recommended). **Never** photo, DOB/age, gender, marital/family, religion, nationality/birthplace, SSN/SIN, health/disability/gene info. No personal pronouns (I / me / we). Work-authorization line acceptable for non-citizens ("Authorized to work in the U.S. for any employer without sponsorship" / "Will require visa sponsorship for employment." / "Authorized to work in Canada without sponsorship."). Opt/STEM-OPT F-1 holders: "authorized" ≠ "no sponsorship needed" — three years later H-1B is still required; wording must be honest.

**Law anchors.** US federal law enforced by the EEOC prohibits discrimination on race, color, religion, sex (incl. sexual orientation, gender identity, pregnancy), national origin, age (40+, ADEA), disability (ADA), genetic info (GINA); protected-class data must not be solicited or considered pre-offer ([EEOC Prohibited Employment Policies/Practices](https://www.eeoc.gov/prohibited-employment-policiespractices), [Cornell LII — Title VII](https://www.law.cornell.edu/wex/title_vii)). Canada: the **Canadian Human Rights Act** lists 13 federal grounds (race, national/ethnic origin, color, religion, age, sex, sexual orientation, gender identity/expression, marital status, family status, disability, genetic characteristics, pardoned conviction) — [CHRC About Discrimination](https://www.chrc-ccdp.gc.ca/individuals/human-rights/about-discrimination). Ontario **OHRC** mirrors these and lists employment as a protected social area ([OHRC](https://www.ohrc.on.ca/en/ontario-human-rights-code)); Quebec CDPDJ adds civil status, political convictions, language, social condition ([CDPDJ](https://www.cdpdj.qc.ca/en/your-rights/grounds-of-discrimination)). [Canada Job Bank](https://www.jobbank.gc.ca/findajob/resources/write-good-resume): never SIN, no photo, omit age/marital/religion/political.

**CN→NA transform.** Hard-delete: photo, DOB/age, 性别, 身份证, 籍贯, 政治面貌, 民族, 婚姻状况, 完整家庭住址, 期望薪资 (nine fields). Reduce address to city + state/province. Replace 微信 → LinkedIn (prompt user to create one if absent). Keep GitHub/portfolio. Add a work-auth line if the candidate is a non-citizen needing to signal status. Flag old graduation years as an age signal for experienced candidates — consider dropping grad-year if 15+ years out.

**NA→CN transform.** Photo slot optional (offer the slot, never force). May add 求职意向 (岗位+城市) and 毕业时间/届别. Age/籍贯 optional — omitting is fine and increasingly common for tech. Keep GitHub. LinkedIn → optional 微信. SSN/SIN-type fields are never carried in either direction.

Sources: [字节 ADFE](https://juejin.cn/post/6844904120734711815), [JavaGuide](https://juejin.cn/post/7289239226024804409), [javaguide.cn](https://javaguide.cn/interview-preparation/resume-guide.html), [云舒](https://juejin.cn/post/7292948455550238732), [Stanford Career Education](https://careered.stanford.edu/sites/g/files/sbiybj22801/files/media/file/resume-and-cover-letter-examples.pdf), [MIT CAPD](https://capd.mit.edu/channels/make-a-resume-cover-letter-cv/).

## Dimension 2 — Length

**CN norm.** 校招 1 page (≤2 if dense); 社招 2 pages (≤3); avoid the "1.5 页" half-empty look — "要么一页，要么两页铺满".

**NA norm.** New grad / <5–8 yr experience → **strictly 1 page** (harvard FAS confirms even a GSAS PhD targeting industry — non-research — uses a résumé, not a CV). Experienced → 1–2 pages, **only the last 10–15 years**. Academic CV (publications / presentations / references, no page limit) is reserved for research / academic roles only.

**Verified rejection.** The claim that "tech/engineering can break to a second page by exception" was rejected 1-2 in adversarial voting — experienced technical candidates follow standard length norms with **no special multi-page exemption**.

**CN→NA transform.** Enforce 1 page for new grads; trim experienced to last 10–15 yr; drop the "fill two pages" instinct. **NA→CN transform.** 1 page is fine for 校招; ≤2 pages for 社招; always PDF.

Sources: [JavaGuide](https://juejin.cn/post/7289239226024804409), [Tech Interview Handbook](https://www.techinterviewhandbook.org/resume/), [Harvard FAS Career Services](https://careerservices.fas.harvard.edu/channels/create-a-resume-cv-or-cover-letter/), [Enhancv](https://enhancv.com/resume-examples/software-engineer/).

## Dimension 3 — Section Ordering & Which Sections Exist

**CN norm.** Standard modules: 求职意向、个人信息、教育背景、专业技能/技术栈、项目经历、实习/工作经历、荣誉奖项、校园经历、自我评价. Ordering is **school-dependent**: strong school (985/211) → Education near top; weak school → Education sinks; 社招 → 工作经历 first. 自我评价 optional and a "重灾区" — never write "勤奋/吃苦/学习能力强"; if kept, ≤3 concrete FAB lines.

**NA norm.** Standard modules: (optional Summary / Headline) → Contact → Skills → Experience → Education → Projects → (optional Awards / Certifications). **Reverse-chronological is a hard expectation** (ATS + recruiters). In-school or <3 yr experience → Education above Experience; otherwise Experience first, Education sinks. **No 自我评价 section**, no soft-skill blurbs. **Objective is outdated** (employer already knows you want a job). Section headings in standard English (Experience / Education / Skills / Projects), no icons — for ATS parsing.

**CN→NA transform.** Delete 求职意向 and 自我评价 (fold concrete facts into a one-line Summary if useful). Reorder by experience years, not school prestige. Merge 荣誉奖项 into Education or a small Awards sub-section. Use standard English headings, no symbols.

**NA→CN transform.** Summary → 求职意向 line (+ optional concrete 自我评价 ≤3 lines). Reorder Education by prestige if 985/211 and 校招. Promote awards to a 荣誉奖项 section.

Sources: [字节 ADFE](https://juejin.cn/post/6844904120734711815), [Tech Interview Handbook](https://www.techinterviewhandbook.org/resume/), [Resume Worded](https://resumeworded.com/software-engineer-resume-examples), [MIT CAPD](https://capd.mit.edu/channels/make-a-resume-cover-letter-cv/).

## Dimension 4 — Bullets

**CN norm.** STAR (背景-任务-行动-结果) + FAB. Per project: 项目名称 / 描述 (1–2 lines) / 技术栈 line / 工作内容 6–8 bullets. Emphasize what **you** did, not what the project was; every bullet carries its tech point. Verbs: 负责 (main module) / 参与 (collaborate) / 主导 / 优化 / 实现 / 排查并解决. Quantify with system metrics — examples: "QPS 从 30w 提到 100w+", "响应时间 3.5s → 1s", "Redis+Caffeine 两级缓存，查询毫秒级，QPS 30w+", "Sharding-JDBC 按用户 ID 后 4 位分库分表，单表 <500w".

**NA norm.** Every bullet opens with a **strong past-tense action verb** (Led / Built / Designed / Reduced / Optimized / Shipped / Migrated / Automated) — **never "Responsible for…" / "Duties included…"** (the #1 weak-bullet pattern, per Stanford + hiring-manager consensus). Follow Google's **X-Y-Z** formula: *"Accomplished [X] as measured by [Y], by doing [Z]"* ([Bock 2014](https://www.linkedin.com/pulse/20140929001534-24454816-my-personal-formula-for-a-better-resume)). Front-load impact and a number, then give a baseline and the how. No pronouns. Past tense throughout — present tense only for the current role. Tech is tied to outcomes, not dumped.

**CN→NA transform.** Rewrite 负责 / 参与 → `ActionVerb + what + [tech] + quantified result`. Move the metric to the front (X-Y-Z). Collapse 项目描述 to a one-liner. Delete "学到了很多" / "认识到重要性". Past tense, strip "I". **Keep the numbers — CN metrics translate directly and are gold in NA.**

**NA→CN transform.** Regroup bullets under STAR. Restore the explicit 技术栈 line per project. Expand terse verbs into 负责 / 主导 / 优化. Keep all numbers. Add a short 项目描述 (背景/规模).

Sources: [云舒](https://juejin.cn/post/7292948455550238732), [JavaGuide](https://juejin.cn/post/7289239226024804409), [字节 ADFE](https://juejin.cn/post/6844904120734711815), [Tech Interview Handbook](https://www.techinterviewhandbook.org/resume/), [Bock 2014](https://www.linkedin.com/pulse/20140929001534-24454816-my-personal-formula-for-a-better-resume), [Stanford Career Education](https://careered.stanford.edu/sites/g/files/sbiybj22801/files/media/file/resume-and-cover-letter-examples.pdf), [Resume Worded — Action Verbs](https://resumeworded.com/software-engineer-resume-action-verbs).

## Dimension 5 — Skills Section

**CN norm.** 技术栈 with tiers low → high: **了解 → 熟悉 → 熟练掌握 → 精通** (使用过 substitutes for the middle). **"精通" is a tripwire** — 校招 / 实习 **never** use it; senior candidates rarely do either. 字节 per-item tagging example: `HTML（熟悉），CSS（熟悉），React（了解）`. Backend groups by 基础 / 数据库 / 框架 / 分布式中间件 / 工具. Casing: java → Java, spring boot → Spring Boot; add a space between CJK and Latin/numbers. **Contested**: 字节 front-end 2024 prefers dropping tiers entirely and listing mainstream stack names — switch by role.

**NA norm.** Compact **categorized one-liner**, **no proficiency tiers, no stars/progress bars**: `Languages: Python, Go, TypeScript · Frameworks: React, FastAPI, PyTorch · Cloud/Tools: AWS (ECS, S3, DynamoDB), Kubernetes, Terraform, Docker`. Hiring-manager consensus (Stack Overflow Blog, interviews with ~24 Google/FB/Microsoft recruiters): *"Don't bother labeling proficiency — if you list it, recruiters assume you're competent enough."* Self-rated tiers are subjective and meaningless. Match exact JD keywords (ATS retrieves by word). Spell out abbreviations on first use: *"Amazon Web Services (AWS)"*. Don't bury skills on page 2.

**CN→NA transform.** Strip tiers → categorized one-liners. Keep JD keywords. Spell out abbreviations. Delete CET / 普通话二级 / 计算机二级 (irrelevant certs).

**NA→CN transform.** Add tiers (default 熟悉 / 了解; **avoid 精通 for junior**). Regroup under CN categories (基础 / 数据库 / 框架 / 中间件 / 工具). Align to JD keywords verbatim. Fix casing and CJK-Latin spacing.

Sources: [juejin/7022927620689887263](https://juejin.cn/post/7022927620689887263), [juejin/7277804250024427557](https://juejin.cn/post/7277804250024427557), [字节 ADFE](https://juejin.cn/post/6844904120734711815), [字节前端](https://juejin.cn/post/6844903894305210376), [Stack Overflow Blog — hiring-manager](https://stackoverflow.blog/2020/11/25/how-to-write-an-effective-developer-resume-advice-from-a-hiring-manager/), [Tech Interview Handbook](https://www.techinterviewhandbook.org/resume/).

## Dimension 6 — Projects vs Work Experience

**CN norm.** 工作经历 is the 社招 term; 实习经历 is the 校招 term. New grads: 项目经历 is the primary weapon. Value ranking: 商业项目 > 毕业设计 > 课程设计/竞赛. Simulate scope when thin: "项目规模：约 20 模块，3 人 3 个月". Internships: big-company and ≥3 months is ideal; drop after 3+ years of work experience.

**NA norm.** Same logic: new grads lead with Projects (personal builds, OSS contributions, hackathons, capstones), Skills section high, internships treated as real Experience with company/title/dates + quantified bullets. Experienced candidates → Work Experience first, Projects shrunk or omitted. **NA expects every project to carry a GitHub / live link** — CN often omits this. For AI/ML roles, Hugging Face Spaces can host an interactive demo ("ML's GitHub", 500k+ models). OSS contribution is the portfolio substitute for new grads and career-switchers — recruiters can directly verify production-grade coding (docs / structure / tests / PR quality).

**CN→NA transform.** Roughly 1:1. **Ensure each project has a GitHub or live link** (NA expects, CN omits). 实习经历 → "Experience" with company / title / dates + quantified bullets. 课程设计 / 毕业设计 → "Academic Projects" with a link.

**NA→CN transform.** Split into 实习经历 vs 项目经历. Restore explicit 技术栈 lines per project. If thin, add 竞赛 / 毕业设计 with scale descriptors.

Sources: [字节 ADFE](https://juejin.cn/post/6844904120734711815), [9-yr interviewer](https://juejin.cn/post/6907146327043129352), [Tech Interview Handbook](https://www.techinterviewhandbook.org/resume/), [MIT CAPD](https://capd.mit.edu/channels/make-a-resume-cover-letter-cv/), [Comet — Open-Source AI](https://www.comet.com/site/blog/contributing-to-open-source-ai/).

## Dimension 7 — Education Details

**CN norm.** Required: 学校、学历、专业、起止时间、(optional) GPA / 排名、相关课程、CET. GPA/rank = 扬长避短 — **GPA only if top ~30%**, otherwise omit; rank uses "专业排名前 5% / 10% / 30%". **School tier (985/211/双一流) is a real signal** — strong school moves Education up. **CET-4/6** is a standard English-proficiency marker (foreign-enterprise weighting higher). Courses listed selectively per JD; blind listing is a red flag. Sub-bachelor candidates sometimes omit the degree to compete.

**NA norm.** Degree, university, location, graduation year (or expected). **GPA only if ≥3.5/4.0**; below, drop. **No percentile rank** (no NA equivalent). Coursework optional, new-grad only (4–8 targeted courses). **No CET / no English-proficiency line** — English is assumed; list other languages only. Drop high school after a degree. Avoid very old graduation years (age signal) for experienced candidates. CS/SWE-specific: GPA weight is lower than other fields (projects/internships/skills often matter more), but Google + finance/quant have hard GPA filters — if targeting those and ≥3.5, write it.

**CN→NA transform.** 专业排名前 X% → GPA/4.0 (only if ≥3.5) or drop. Drop GPA if <3.5. **Delete CET.** Keep degree / major / school / dates. Don't rely on 985/211 framing (undecodable to NA readers). Trim coursework. Consider dropping grad year for experienced candidates.

**NA→CN transform.** Keep GPA as X.X/4.0. Optionally add 专业排名 if strong. Add CET. Add relevant coursework selectively. If 985/211-equivalent and new-grad, move Education up.

Sources: [JavaGuide](https://juejin.cn/post/7289239226024804409), [云舒](https://juejin.cn/post/7292948455550238732), [字节 ADFE](https://juejin.cn/post/6844904120734711815), [Tech Interview Handbook](https://www.techinterviewhandbook.org/resume/), [Resume Worded — GPA](https://resumeworded.com/gpa-on-resume-key-advice), [Forage](https://www.theforage.com/blog/basics/gpa-on-resume).

## Dimension 8 — Tone & Cultural Expectations

**CN norm.** Balance: avoid empty boasting ("精通"/"吃苦耐劳") **and** excessive modesty; speak through evidence and quantified data. Red flags: exaggerating/unpracticed tech; overusing 精通; empty 自我评价; irrelevant info (hobbies / height / 人生格言 / 格局小 campus roles); irrelevant certs (Office / 普通话二级 / 计算机二级); stack mismatch or outdated tech (jQuery/Bootstrap pile-on for front-end); copy-paste template sameness; typos / casing / mixed punctuation / Word-breaks-on-Mac.

**NA norm.** **Impact-first self-promotion is expected** (confident, not arrogant). Use numbers and evidence. Put ownership verbs and impact up front. Delete humility hedges and soft-skill blurbs. Scan time: ~7.4 seconds for the initial rejection sweep (TheLadders 2012 eye-tracking, updated cite), then 30 sec–1 min for surviving résumés — so the name / target role / most-recent role / strongest impact must be visible at a glance. Red flags: "Responsible for…" duty lists, Objective statements, photos / personal data, functional (skill-based) formats, buzzword dumps, >1 page for new grads.

**CN→NA transform.** Raise the confidence register (参与 → ownership verbs, impact first). Keep CN evidence/quantification (it aligns with NA). Remove humility hedges and soft-skill blurbs. Apply ATS hygiene (below).

**NA→CN transform.** Soften absolute self-promotion. Back claims with numbers. Avoid 精通. Keep JD-keyword alignment (works both ways).

Sources: [9-yr interviewer](https://juejin.cn/post/6907146327043129352), [字节前端](https://juejin.cn/post/6844903894305210376), [JavaGuide](https://juejin.cn/post/7289239226024804409), [Tech Interview Handbook](https://www.techinterviewhandbook.org/resume/), [HR Dive — 7.4 seconds](https://www.hrdive.com/news/eye-tracking-study-shows-recruiters-look-at-resumes-for-7-seconds/541582/).

## Dimension 10 — ATS Hygiene (NA "physics")

**Prevalence.** ~99% of Fortune 500 use an ATS (MIT CAPD; Jobscan 2024: 98.4%). More importantly, **75%+ of US résumés are filtered out by AI/ATS before a human sees them** — Workday / Greenhouse / Lever / iCIMS narrow applicants to a ~10–15 person shortlist. ATS and résumé databases retrieve by keyword, so JD-exact wording must be woven into the résumé.

**Hard constraints (NA):**

| Do | Don't |
|---|---|
| Text-**selectable** PDF (export from Word/Google Docs) | Scanned PDF / image PDF |
| **单栏** (single-column) layout | Two/three-column (parse-failure #1 cause) |
| Standard black fonts, ≥10 pt, 0.5" margins | Fancy fonts, color, icons |
| Standard section headings (Experience/Education/Skills) | Custom headings / icon headings |
| Contact info in **body top** | In Word/Google Docs **header region** (ATS can't read headers) |
| Abbreviations spelled out once, JD keywords verbatim | Buried on page 2 / unexpanded acronyms |

**Two-column failure evidence.** Across 8 ATS systems tested, two-column layouts **failed in 7/8** (parsers read line-by-line left-to-right and merge columns into garble). Single-column is the single largest parse-success factor (+32 percentage points). Workday mis-matched fields in **41% of two-column résumés**. June-2026 benchmark of 6 layouts: single-column 100/100 perfect parse; two-column 85/100 and the only one triggering a critical parse warning. Default tool position: **single-column, even when modern ATS can sometimes parse two columns**.

**CN ATS analogue.** No US-style standalone ATS ecosystem, but big-firm HR + platforms (BOSS直聘, 牛客) do keyword/algorithm-match scoring — JD-exact wording is CN's equivalent.

Sources: [MIT CAPD](https://capd.mit.edu/channels/make-a-resume-cover-letter-cv/), [QuickCV — 8 ATS systems tested](https://quickcv.io/blog/i-tested-8-ats-systems-to-see-how-they-actually-parse-resumes), [Resume Optimizer Pro — ATS-friendly](https://resumeoptimizerpro.com/blog/what-makes-a-resume-ats-friendly), [ATS Verification — two-column](https://atsverification.com/blog/two-column-resume-ats-friendly/), [iReformat](https://ireformat.com/blog/ats-resume-formatting-guide), [ORISE — format for AI screening](https://orise.orau.gov/internships-fellowships/blog/how-to-format-your-resume-for-ai-screening.html).

## Dimension 9 & 11 — File Format, Naming & Channels

**CN norm.** **PDF is the iron rule** (Word breaks on Mac). Builders: 木及简历 / 超级简历 / 极简简历 / 简单简历 / resume.mdnice.com. Naming: `姓名 + 目标岗位` minimum; 校招 adds 学校/专业/毕业时间 (`张三-Java开发-同济大学-信息安全`); 社招 adds 优势点; never "简历.pdf". If the recruiter specifies a format, follow it. Channels (priority): **BOSS直聘 dominant (~64.5% market share, 6360万 MAU 2025)** → 智联(~17%) / 前程无忧 51job(~13%) → 内推 (strong for big-firms) → 校招官网 → **牛客** (校招 题库 / 面经 / 内推 / 在线笔试). **拉勾网 bankrupt/delisted 2025–26 — do not recommend.** 脉脉 / 猎聘 for mid/senior.

**NA norm.** PDF exported from Word/Google Docs (text-selectable for ATS), standard fonts ≥10 pt, 0.5" margins, no headers/footers. Naming: **`FirstLast_Resume.pdf`** (minimum) or `FirstLast_SWE_Resume.pdf` (role-targeted); underscore or hyphen separator; never `resume.pdf` / `resume_final(5).pdf`. Channels (priority consensus): **Referral (highest conversion)** → company ATS direct (Greenhouse / Lever / Ashby — `site:boards.greenhouse.io [title] [location]` Google search finds fresh direct roles) → Workday (big enterprise, clunky UX) → **LinkedIn Easy Apply** (fastest one-click, but highest competition and lowest reply rate). **Do not apply to many roles at the same company.** PDF occasionally parses worse than .docx in some ATS — if the employer specifies .doc/.docx, follow it.

**CN→NA transform.** Keep PDF but ensure text-selectable; no photo / table / graphic / header-region contact info. Rename → `FirstLast_Resume.pdf`. Target channels: LinkedIn + company ATS + referrals.

**NA→CN transform.** Keep PDF. Rename → `姓名-目标岗位-学校-专业` (校招) or `姓名-目标岗位-优势点` (社招). Target channels: **BOSS直聘** / 内推 / 校招官网 / 牛客.

Sources: [JavaGuide](https://juejin.cn/post/7289239226024804409), [字节前端](https://juejin.cn/post/6844903894305210376), [云舒](https://juejin.cn/post/7292948455550238732), [平台份额](https://juejin.cn/post/7642267656926969866), [Tech Interview Handbook](https://www.techinterviewhandbook.org/resume/), [ORISE](https://orise.orau.gov/internships-fellowships/blog/how-to-format-your-resume-for-ai-screening.html), [r/ResumeCoverLetterTips — file naming](https://www.reddit.com/r/ResumeCoverLetterTips/comments/1qlrb5j/please_stop_naming_your_resume_file_resume/).

## Naive-Translation Mistakes

**CN→NA literal translation breaks:**
1. Leaving in **photo, 性别, 出生年月, 婚姻状况, 身份证号, 籍贯, 政治面貌** → unprofessional + discrimination-liability discomfort.
2. Keeping 求职意向 / Objective and 自我评价 → outdated / nonexistent; self-eval reads as filler.
3. **"Responsible for …"** duty lists (literal translation of 负责) with no metrics → #1 weak-bullet pattern.
4. Translating proficiency tiers ("Master of Java" from 精通) → sounds off.
5. **CET-4/6** line → meaningless, wastes space.
6. 专业排名前 10% literal → no NA equivalent; convert to GPA/4.0 or drop.
7. Two dense pages for a new grad → NA wants 1 tight page.
8. **985/211** prestige framing → undecodable to NA readers.
9. Full home address / 期望薪资 → never on a NA résumé.

**NA→CN literal translation breaks:**
1. Dropping explicit 技术栈 line → CN interviewers expect per-project tech.
2. No 求职意向, no photo slot, no education-prestige positioning.
3. Over-terse verbs without STAR context → CN wants 背景 / 描述 first.
4. Missing CET / 毕业时间 / 应届生 status → needed for 校招 eligibility.
5. English file name or Word format → rename to `姓名-岗位-…`, keep PDF.
6. US-style "no proficiency levels" → CN (esp. backend) expects 了解 / 熟悉 / 熟练掌握 tiers.

## Contested Points → Expose as Options (do not hard-code)

These are conventions derived from anti-discrimination law and ATS technology, not statutory "résumé rules". Surface them in tool messaging and let the user decide.

- **Photo (CN):** tolerated (社招) vs discouraged (字节 tech). Default off; optional formal headshot.
- **Skill tiers (CN):** ladder 了解 / 熟悉 / 熟练掌握 (backend) vs bare stack names (字节 front-end 2024). Switch by role.
- **Age / 籍贯 (CN):** "basic info" (JavaGuide) vs omit (most). Default omit.
- **自我评价 (CN):** keep-if-concrete vs drop. Default optional, ≤3 concrete lines.
- **Full address vs city-only (NA):** US → city + state; Canada Job Bank / OHRC tolerate a mailing address. Default city + region.
- **Work-auth line (NA):** write (foreign-name / sponsorship-needed reduces false rejects) vs leave in ATS form (Texas Tech / Georgetown). Default: write one line if non-citizen and needing to signal "no sponsorship required".
- **Summary vs no Summary (NA):** 3+ yr experienced → Summary recommended; new-grad → Headline or omit. Default accordingly.
- **Objective:** basically obsolete; only career-switchers / new-grads may use, and only framed around value delivered. Default: don't use.

## Sources (condensed)

**CN — recruiter / community consensus:**
- JavaGuide (Snailclimb) — [javaguide.cn/interview-preparation/resume-guide.html](https://javaguide.cn/interview-preparation/resume-guide.html) / [juejin/7289239226024804409](https://juejin.cn/post/7289239226024804409)
- 字节 ADFE — [juejin/6844904120734711815](https://juejin.cn/post/6844904120734711815); 字节前端 — [juejin/6844903894305210376](https://juejin.cn/post/6844903894305210376)
- 云舒编程 — [juejin/7292948455550238732](https://juejin.cn/post/7292948455550238732)
- 决战BAT柠檬哥 — [juejin/6964664853218721823](https://juejin.cn/post/6964664853218721823); 9-yr interviewer — [juejin/6907146327043129352](https://juejin.cn/post/6907146327043129352)
- Java 后端 — [juejin/7277804250024427557](https://juejin.cn/post/7277804250024427557); 项目写法 — [juejin/7022927620689887263](https://juejin.cn/post/7022927620689887263); 牛客网 nowcoder.com corroborate.

**NA — recruiter / career-center / hiring-manager:**
- Tech Interview Handbook (Yangshun Tay, ex-Meta Staff Engineer) — [techinterviewhandbook.org/resume](https://www.techinterviewhandbook.org/resume/)
- Laszlo Bock (ex-Google SVP People Ops) X-Y-Z — [LinkedIn Pulse 2014](https://www.linkedin.com/pulse/20140929001534-24454816-my-personal-formula-for-a-better-resume)
- Stack Overflow Blog hiring-manager (Gergely Orosz) — [stackoverflow.blog](https://stackoverflow.blog/2020/11/25/how-to-write-an-effective-developer-resume-advice-from-a-hiring-manager/)
- Stanford Career Education — [resume-and-cover-letter-examples.pdf](https://careered.stanford.edu/sites/g/files/sbiybj22801/files/media/file/resume-and-cover-letter-examples.pdf)
- MIT CAPD — [capd.mit.edu](https://capd.mit.edu/channels/make-a-resume-cover-letter-cv/); Harvard FAS — [careerservices.fas.harvard.edu](https://careerservices.fas.harvard.edu/channels/create-a-resume-cv-or-cover-letter/)
- Commercial corroboration: [Resume Worded](https://resumeworded.com/software-engineer-resume-examples), [Enhancv](https://enhancv.com/resume-examples/software-engineer/), [The Muse](https://www.themuse.com/advice/how-long-should-a-resume-be), [Novoresume](https://novoresume.com/career-blog/what-to-put-on-a-resume), [freeCodeCamp](https://www.freecodecamp.org/news/writing-a-killer-software-engineering-resume-b11c91ef699d/).
- ATS testing: [QuickCV — 8 ATS systems](https://quickcv.io/blog/i-tested-8-ats-systems-to-see-how-they-actually-parse-resumes), [Resume Optimizer Pro](https://resumeoptimizerpro.com/blog/what-makes-a-resume-ats-friendly), [ATS Verification — two-column](https://atsverification.com/blog/two-column-resume-ats-friendly/), [iReformat](https://ireformat.com/blog/ats-resume-formatting-guide), [ORISE](https://orise.orau.gov/internships-fellowships/blog/how-to-format-your-resume-for-ai-screening.html).

**US law (primary government / law-school):**
- EEOC — [Prohibited Employment Policies/Practices](https://www.eeoc.gov/prohibited-employment-policiespractices)
- Cornell LII — [Title VII](https://www.law.cornell.edu/wex/title_vii), [Employment Discrimination](https://www.law.cornell.edu/wex/employment_discrimination)
- usa.gov — [job-discrimination-harassment](https://www.usa.gov/job-discrimination-harassment)

**Canada law (primary):**
- CHRC — [About Discrimination](https://www.chrc-ccdp.gc.ca/individuals/human-rights/about-discrimination) (CHRA 13 grounds)
- [Canadian Human Rights Act](https://laws-lois.justice.gc.ca/eng/acts/h-6/page-1.html)
- OHRC — [Ontario Human Rights Code](https://www.ohrc.on.ca/en/ontario-human-rights-code)
- Quebec CDPDJ — [grounds of discrimination](https://www.cdpdj.qc.ca/en/your-rights/grounds-of-discrimination)
- Canada Job Bank — [write-good-resume](https://www.jobbank.gc.ca/findajob/resources/write-good-resume)
