# CN ⇄ NA Software-Engineer Résumé Conversion Guide

> Research date: 2026-07-02. Reference for a tool that **re-shapes** (not translates) SWE/IT résumés between Mainland China (校招/社招) and North America (US/Canada). This is the source material for `skills/resume-optimizer/references/cn-na-market.md`. Companion deep-dives: CN-only detail `2026-07-02-cn-resume-norms.md`; NA-only detail `2026-07-02-na-resume-norms.md` (verified via deep-research workflow — 23/25 claims survived adversarial voting).
>
> Research note: WebSearch/WebFetch were blocked; sourcing done via curl + text extraction. Reddit/Indeed/Zety/EEOC were bot-blocked, so r/cscareerquestions consensus is represented via Tech Interview Handbook + career-service guides, and US legal claims anchored in Cornell LII + usa.gov. Google X-Y-Z attributed to Laszlo Bock via Novoresume.

## Quick-Reference Transformation Table

| Dimension | China (校招/社招) | North America (US/Canada) | CN→NA rule | NA→CN rule |
|---|---|---|---|---|
| **Photo** | Optional; pro headshot tolerated (never mandatory for tech) | **Never** (reveals race/sex/age → discrimination risk) | **Delete photo** | Optional add; only formal headshot, never mandatory |
| **Age / DOB / 性别 / 身份证 / 籍贯 / 政治面貌 / marital** | Age/籍贯 sometimes listed; ID/gender discouraged even in CN | **Forbidden** (Title VII/ADEA/CHRA) | **Strip all** | Can add age/grad-year; still skip ID/marital for tech |
| **Address** | Not needed (privacy) | City + State/Province (not full street) | Add city+region | Drop to none/city |
| **Work authorization** | Not a concept for domestic | State "Authorized to work in US/Canada" or sponsorship need if non-citizen | **Add** work-auth line if relevant | Remove |
| **Contacts** | Phone + email mandatory; 微信 optional; GitHub/blog if has content; LinkedIn ~never | Phone, email, LinkedIn, GitHub/portfolio | 微信→LinkedIn; keep GitHub | LinkedIn→(optional 微信); keep GitHub |
| **Length** | 校招 1p (≤2); 社招 2p (≤3); PDF | New-grad 1p; experienced 1–2p (10–15 yr window); PDF | Enforce 1p new-grad | Compress to 1p; PDF |
| **求职意向 / Objective** | Common & recommended (岗位+城市) | Objective **outdated**; use Summary (optional) | Convert 求职意向→ headline/summary or delete | Summary→求职意向 line |
| **自我评价 / Self-eval** | Exists, optional, must be concrete | **Does not exist**; no soft-skill blurbs | **Delete** (or fold facts into Summary) | Optionally add concrete 自我评价 ≤3 lines |
| **Education placement** | Strong school → top; weak → bottom; 社招 bottom | New grad → near top; experienced → bottom | Reorder by experience, not school prestige | New-grad: fine at top; add school tier if 985/211 |
| **GPA / rank** | GPA if top ~30%; 专业排名 前5%/10% | GPA only if ≥3.5/4.0; no percentile rank | 前X%→ drop or convert to GPA/4.0; drop if <3.5 | GPA/4.0 → keep; may add 排名 if strong |
| **Bullets** | STAR + 技术栈; 负责/参与/主导 | Action verb + X-Y-Z ("Accomplished X measured by Y by doing Z"); no "responsible for" | Rewrite 负责→Led/Built/Designed; front-load metric | Rewrite to STAR; keep 技术栈 explicit |
| **Skills** | 技术栈 with tiers 了解/熟悉/熟练掌握/精通 (校招 never "精通") | Compact categorized line; no proficiency tiers | Strip tiers → categorized list | Add tiers; align to JD keywords |
| **Honors 荣誉奖项** | Common section | Fold into Education/small "Awards" | Merge into Education | Can promote to 荣誉奖项 section |
| **CET-4/6** | Listed as English proficiency | Meaningless; drop (English implied) | **Delete CET** | Add CET if targeting CN |
| **Tone** | Evidence-based, humble; no puffery | Impact-first self-promotion, confident | Amplify ownership/impact | Soften; avoid "精通"/puffery |
| **File name** | `姓名-岗位-学校-专业` (校招) | `FirstLast_Resume.pdf` / `FirstLast_SWE_Resume.pdf` | Rename to English convention | Rename to CN convention |
| **Channel** | BOSS直聘 / 内推 / 校招官网 / 牛客 | LinkedIn, company ATS, referrals | — | — |
| **ATS** | HR keyword-matches manually/algorithmically | Formal ATS parsing dominant | Aggressive JD keyword alignment; plain layout | Keep JD-keyword alignment |

## Dimension 1 — Personal Info / Header

**China.** Minimal header: 姓名、电话、邮箱、求职意向(岗位+城市)、毕业时间/学历. Phone/email mandatory and must be correct. GitHub/博客 only if real content. 微信 optional; **LinkedIn essentially never used**. Age/籍贯 contested → can omit. 性别/身高/身份证/住址/政治面貌/民族/期望薪资 discouraged (期望薪资 goes in platform field). Photo optional & contested; tech trend is none-or-formal-headshot, never mandatory.

**North America.** name, phone, professional email, city + state/province, LinkedIn, GitHub/portfolio. No full street address. **Legally-driven exclusions** (photo, DOB/age, gender, marital/family, religion, nationality, SSN/SIN, health/disability) — Title VII, ADEA (40+), ADA, GINA (US); Canadian Human Rights Act + provincial codes (Ontario OHRC; Quebec adds civil status, political convictions, language, social condition). Convention is omission because employers can't solicit/consider them. **Work authorization** acceptable/expected for non-citizens ("Authorized to work in US" / "Will require visa sponsorship" / "Eligible to work in Canada"). Canada Job Bank: never SIN, no photo, omit age/marital/religion/political.

**Transform. CN→NA:** hard-delete photo, DOB/age, 性别, 身份证, 籍贯, 政治面貌, 民族, marital, full address, 期望薪资; reduce address to city+region; 微信→LinkedIn (prompt to create); keep GitHub; add work-auth line if non-citizen; flag old grad years as age signal. **NA→CN:** photo optional (offer slot, never force); may add 求职意向 + 毕业时间; age/籍贯 optional (off for tech ok); GitHub kept; LinkedIn→optional 微信; never carry SSN-type fields either way.

Sources: [字节](https://juejin.cn/post/6844904120734711815), [JavaGuide](https://juejin.cn/post/7289239226024804409) / [javaguide.cn](https://javaguide.cn/interview-preparation/resume-guide.html), [云舒](https://juejin.cn/post/7292948455550238732), [Cornell LII](https://www.law.cornell.edu/wex/employment_discrimination), [usa.gov](https://www.usa.gov/job-discrimination-harassment), [Canadian Human Rights Act](https://laws-lois.justice.gc.ca/eng/acts/h-6/page-1.html), [Job Bank](https://www.jobbank.gc.ca/findajob/resources/write-good-resume), [OHRC](https://www.ohrc.on.ca/en/human-rights-work-2008-third-edition/appendix-d-sample-application-employment), [CDPDJ](https://www.cdpdj.qc.ca/en/your-rights/grounds-of-discrimination).

## Dimension 2 — Length & Page Norms

**China.** 校招 1 page (≤2); 社招 ≤3; avoid the awkward 1.5-page look ("要么一页，要么两页铺满"). **NA.** New grad/<5–8 yr → 1 page (strict); experienced → 1–2 pp, last 10–15 yr only; 3+ pp = academic CV/exec. **Transform CN→NA:** enforce 1p for new grads, trim experienced to last 10–15 yr, drop the "fill two pages" instinct. **NA→CN:** 1p fine for 校招, ≤2 for 社招; PDF.

Sources: [JavaGuide](https://juejin.cn/post/7289239226024804409), [Tech Interview Handbook](https://www.techinterviewhandbook.org/resume/), [Enhancv](https://enhancv.com/resume-examples/software-engineer/), [Job Bank](https://www.jobbank.gc.ca/findajob/resources/write-good-resume).

## Dimension 3 — Section Ordering & Which Sections Exist

**China.** Modules: 求职意向、个人信息、教育背景、专业技能/技术栈、项目经历、实习/工作经历、荣誉奖项、校园经历、自我评价. Order school-dependent (strong school → Education top; weak → down; 社招 → 工作经历 first). 自我评价 optional; if kept ≤3 concrete lines. **NA.** (optional Summary/headline) → Contact → Skills → Work Experience → Education → Projects → (optional Awards/Certs). Students/<3 yr → Education above Work. **No self-evaluation section**, no soft-skill blurb; objectives outdated; reverse-chronological expected (ATS).

**Transform CN→NA:** delete 求职意向 & 自我评价 (fold concrete facts into Summary); reorder by experience not school; merge 荣誉奖项; use standard English headings (no symbols). **NA→CN:** Summary→求职意向 (+optional concrete 自我评价); reorder education by prestige if 985/211; promote awards to 荣誉奖项.

Sources: [字节](https://juejin.cn/post/6844904120734711815), [Tech Interview Handbook](https://www.techinterviewhandbook.org/resume/), [Resume Worded](https://resumeworded.com/software-engineer-resume-examples), [Enhancv](https://enhancv.com/resume-examples/software-engineer/).

## Dimension 4 — Bullet Writing Style

**China.** STAR (背景-任务-行动-结果) + FAB. Per project: 项目名称 / 描述(1–2 lines) / 技术栈 line / 工作内容 6–8 bullets. Emphasize what YOU did; every bullet carries its tech. Verbs 负责/参与/主导/优化/实现/排查并解决. Quantify with system metrics (QPS 从 x 到 y, 响应时间 3.5s→1s, QPS 30w+, 单表 <500w). **NA.** Every bullet = strong past-tense action verb (Led, Built, Designed, Reduced, Optimized) — **never "Responsible for"**. Google **X-Y-Z**: "Accomplished [X] as measured by [Y], by doing [Z]" — front-load impact+metric. No pronouns, past tense (present only for current role). Tech tied to outcomes, not a bare dump.

**Transform CN→NA:** rewrite 负责/参与 → `ActionVerb + what + [tech] + quantified result`, move metric to front (X-Y-Z), collapse 项目描述 to a one-liner, delete "学到了很多"/"认识到重要性", past tense, strip "I"; keep the numbers (translate directly, gold in NA). **NA→CN:** regroup under STAR, restore explicit 技术栈 line, expand terse verbs into 负责/主导/优化, keep numbers, add short 项目描述.

Sources: [云舒](https://juejin.cn/post/7292948455550238732), [JavaGuide](https://juejin.cn/post/7289239226024804409), [字节](https://juejin.cn/post/6844904120734711815), [Tech Interview Handbook](https://www.techinterviewhandbook.org/resume/), [Novoresume X-Y-Z](https://novoresume.com/career-blog/how-to-write-a-cv).

## Dimension 5 — Skills Section

**China.** 技术栈 with tiers low→high: 了解 → 熟悉 → 熟练掌握 → 精通 (使用过 substitutes middle). **"精通" is a tripwire — 校招/实习 never use it.** 字节 per-item tagging for students: "HTML（熟悉），CSS（熟悉），React（了解）". Backend grouped: 基础/数据库/框架/分布式中间件/工具. Explicit JD keyword alignment (HR matches keywords/algorithms). Casing: java→Java, spring boot→Spring Boot, space between CJK and Latin. Contested: 字节 front-end 2024 → drop tiers, list mainstream stack names. **NA.** Compact **categorized line, no proficiency tiers**: `Languages: … · Frameworks: … · Cloud/Tools: …`. Match exact JD keywords, spell out abbreviations once ("Amazon Web Services (AWS)"). Don't bury skills on page 2.

**Transform CN→NA:** strip tiers, regroup into categorized one-liners, keep JD keywords, spell out abbrevs, delete CET/普通话/计算机二级. **NA→CN:** add tiers (default 熟悉 / 了解; avoid 精通 for junior), regroup under CN categories, align to JD, fix casing & spacing.

Sources: [juejin/7022927620689887263](https://juejin.cn/post/7022927620689887263), [juejin/7277804250024427557](https://juejin.cn/post/7277804250024427557), [字节](https://juejin.cn/post/6844904120734711815), [字节前端](https://juejin.cn/post/6844903894305210376), [Tech Interview Handbook](https://www.techinterviewhandbook.org/resume/), [Resume Worded](https://resumeworded.com/software-engineer-resume-examples).

## Dimension 6 — Projects vs Work Experience Emphasis

**China.** 工作经历=社招 term; 实习经历=校招 term. New grads: 项目经历 primary. Value: 商业项目 > 毕业设计 > 课程设计/竞赛. Simulate scope ("项目规模：约20模块，3人3个月"). Internships: big-company ≥3 months; drop after 3+ yr. **NA.** Same: new grads lead with Projects (personal builds, OSS, hackathons, capstones), Skills high, internships as real jobs quantified; experienced → Work Experience first, Projects smaller. Link projects to GitHub.

**Transform CN→NA:** ~1:1; ensure each project has GitHub/live link (NA expects, CN omits); 实习经历→"Experience" with company/title/dates + quantified bullets; 课程设计/毕业设计→"Academic Projects". **NA→CN:** split into 实习经历 vs 项目经历, restore 技术栈 lines, if thin add 竞赛/毕业设计 + scale descriptors.

Sources: [字节](https://juejin.cn/post/6844904120734711815), [9-yr interviewer](https://juejin.cn/post/6907146327043129352), [Tech Interview Handbook](https://www.techinterviewhandbook.org/resume/), [Enhancv](https://enhancv.com/resume-examples/software-engineer/).

## Dimension 7 — Education Details

**China.** School, degree, major, dates, optional GPA/rank, courses, CET. GPA/rank = 扬长避短 (GPA if top ~30%; 专业排名 前5%/10%/30%). School tier (985/211/双一流) is a real signal → strong school to top. CET-4/6 standard English marker. Courses selectively per JD; blind listing is a red flag. Sub-bachelor sometimes omit degree. **NA.** Degree, university, location, grad year (or expected). **GPA only if ≥3.5/4.0; no percentile rank.** Coursework optional for new grads. **No CET / no English-proficiency line** (English assumed; list other languages only). Drop high-school after a degree; avoid old grad years (age signal).

**Transform CN→NA:** 专业排名前X% → GPA/4.0 (if ≥3.5) or drop; drop GPA if <3.5; **delete CET**; keep degree/major/school/dates; don't rely on 985/211 framing; trim coursework; consider removing grad year for experienced. **NA→CN:** keep GPA as X.X/4.0; optionally add 专业排名; add CET; add relevant coursework; if 985/211 new-grad move Education up.

Sources: [JavaGuide](https://juejin.cn/post/7289239226024804409), [云舒](https://juejin.cn/post/7292948455550238732), [字节](https://juejin.cn/post/6844904120734711815), [Tech Interview Handbook](https://www.techinterviewhandbook.org/resume/), [Novoresume](https://novoresume.com/career-blog/what-to-put-on-a-resume), [The Muse](https://www.themuse.com/advice/how-long-should-a-resume-be).

## Dimension 8 — Tone & Cultural Expectations

**China.** Balance: avoid empty boasting (精通/吃苦耐劳) AND excessive modesty; speak through evidence/quantified data. Red flags: exaggerating/unpracticed tech; overusing 精通; empty 自我评价; irrelevant info (hobbies/height/人生格言/格局小 campus roles); irrelevant certs (Office/普通话二级/计算机二级); stack mismatch/outdated tech; copy-paste template sameness; typos/casing/mixed punctuation/Word-breaks-on-Mac. ATS reality: no US-style ecosystem but big-firm HR + platforms keyword/algorithm-match → JD-exact wording is CN's ATS equivalent. Seconds-long scan. **NA.** Impact-first self-promotion expected (confident, not arrogant). ATS optimization central & formal: standard headings, PDF, standard fonts, no headers/footers/tables/graphics, JD keywords woven in, abbrevs spelled out. Red flags: "responsible for" duty-lists, objectives, photos/personal data, typos, functional formats, buzzword soft-skill dumps, >1p for new grad.

**Transform CN→NA:** raise confidence register (参与→ownership verbs, impact first), keep CN evidence/quantification (aligns with NA), remove humility hedges & soft-skill blurbs, apply ATS hygiene. **NA→CN:** soften absolute self-promotion, back claims with numbers, avoid 精通, keep JD alignment (works both ways).

Sources: [9-yr interviewer](https://juejin.cn/post/6907146327043129352), [字节前端](https://juejin.cn/post/6844903894305210376), [JavaGuide](https://juejin.cn/post/7289239226024804409), [Tech Interview Handbook](https://www.techinterviewhandbook.org/resume/), [Novoresume (~75% big firms use ATS)](https://novoresume.com/career-blog/what-to-put-on-a-resume).

## Dimension 9 — File Format, Naming & Channels

**China.** PDF iron rule (Word breaks on Mac). Builders: 木及简历, 超级简历, 极简简历, resume.mdnice.com. Naming: `姓名+目标岗位` minimum; 校招 add 学校/专业/毕业时间 ("张三-Java开发-同济大学-信息安全"); 社招 add 优势点; never "简历.pdf"; follow recruiter format if specified. Channels: **BOSS直聘 dominant (64.5%)**, 智联(~17%), 51job(~13%), 内推, 校招官网, 牛客, 猎聘, 脉脉. **拉勾 bankrupt/delisted 2025–26 — do not recommend.** **NA.** PDF from Word/Google Docs (text-selectable for ATS), standard fonts ≥10pt, 0.5" margins, no headers/footers. Naming `FirstLast_Resume.pdf` / `FirstLast_SoftwareEngineer_Resume.pdf`. Channels: company ATS (Workday/Greenhouse/Lever), LinkedIn (+Easy Apply), referrals (strongest), university portals. Don't apply to many roles at one company.

**Transform CN→NA:** keep PDF but text-selectable, no photo/table/graphic; rename → `FirstLast_Resume.pdf`; target LinkedIn/ATS/referrals. **NA→CN:** keep PDF; rename → `姓名-目标岗位-学校-专业`; target BOSS直聘/内推/校招官网/牛客.

Sources: [JavaGuide](https://juejin.cn/post/7289239226024804409), [字节前端](https://juejin.cn/post/6844903894305210376), [云舒](https://juejin.cn/post/7292948455550238732), [平台份额](https://juejin.cn/post/7642267656926969866), [Tech Interview Handbook](https://www.techinterviewhandbook.org/resume/), [Enhancv](https://enhancv.com/resume-examples/software-engineer/).

## Dimension 10 — Common Naive-Translation Mistakes

**CN→NA (literal translation) breaks:**
1. Leaving in photo, 性别, 出生年月, 婚姻状况, 身份证号, 籍贯, 政治面貌 → unprofessional + discrimination-liability discomfort.
2. Keeping 求职意向/Objective and 自我评价 → outdated/nonexistent; self-eval reads as filler.
3. "Responsible for …" duty lists (literal 负责) with no metrics → #1 weak-bullet pattern.
4. Translating proficiency tiers ("Master of Java" from 精通) → sounds off.
5. CET-4/6 line → meaningless, wastes space.
6. 专业排名前10% literal → no NA equivalent; convert to GPA/4.0 or drop.
7. Two dense pages for a new grad → NA wants 1 tight page.
8. 985/211 prestige framing → undecodable to NA readers.
9. Full home address / 期望薪资 → never on NA résumés.

**NA→CN breaks:**
1. Dropping explicit 技术栈 line → CN interviewers expect per-project tech.
2. No 求职意向, no photo slot, no education-prestige positioning.
3. Over-terse verbs without STAR context → CN wants 背景/描述 first.
4. Missing CET / 毕业时间 / 应届生 status → needed for 校招 eligibility.
5. English file name / Word format → rename to `姓名-岗位-…`, keep PDF.
6. US-style "no proficiency levels" → CN (esp. backend) expects 了解/熟悉/熟练掌握 tiers.

## Contested Points → Expose as Tool Options (not hard-code)

- **Photo (CN):** tolerated (社招) vs discouraged (字节 tech). Default off; optional formal headshot.
- **Skill tiers (CN):** ladder (backend) vs bare stack names (字节 front-end 2024). Switch by role.
- **Age/籍贯 (CN):** "basic" (JavaGuide) vs omit (most). Default omit.
- **自我评价 (CN):** keep-if-concrete vs drop. Default optional, ≤3 concrete lines.
- **Full address vs city-only (NA):** US → city+state; Canada Job Bank/OHRC tolerate mailing address. Default city+region.
- These are conventions derived from anti-discrimination law, not statutory "résumé rules" — surface in tool messaging.

## Key Sources by Market

**CN:** JavaGuide ([javaguide.cn](https://javaguide.cn/interview-preparation/resume-guide.html) / [juejin/7289239226024804409](https://juejin.cn/post/7289239226024804409)), 字节 ADFE ([juejin/6844904120734711815](https://juejin.cn/post/6844904120734711815)), 字节前端 ([juejin/6844903894305210376](https://juejin.cn/post/6844903894305210376)), 云舒编程 ([juejin/7292948455550238732](https://juejin.cn/post/7292948455550238732)), 柠檬哥 ([juejin/6964664853218721823](https://juejin.cn/post/6964664853218721823)), Java 后端 ([juejin/7277804250024427557](https://juejin.cn/post/7277804250024427557)); liyupi/编程导航, 牛客 corroborate.
**NA:** [Tech Interview Handbook](https://www.techinterviewhandbook.org/resume/), [Resume Worded](https://resumeworded.com/software-engineer-resume-examples), [Enhancv](https://enhancv.com/resume-examples/software-engineer/), [The Muse](https://www.themuse.com/advice/how-long-should-a-resume-be), [Novoresume](https://novoresume.com/career-blog/what-to-put-on-a-resume), [freeCodeCamp](https://www.freecodecamp.org/news/how-to-write-a-resume-that-works/).
**Law:** [Cornell LII](https://www.law.cornell.edu/wex/employment_discrimination), [usa.gov](https://www.usa.gov/job-discrimination-harassment), [Canadian Human Rights Act](https://laws-lois.justice.gc.ca/eng/acts/h-6/page-1.html), [Job Bank](https://www.jobbank.gc.ca/findajob/resources/write-good-resume), [OHRC](https://www.ohrc.on.ca/en/human-rights-work-2008-third-edition/appendix-d-sample-application-employment), [CDPDJ Quebec](https://www.cdpdj.qc.ca/en/your-rights/grounds-of-discrimination).
