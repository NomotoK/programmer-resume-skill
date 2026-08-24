# Code Mining Reference

> Consumed by the **resume-from-code** sub-skill. A self-contained playbook for turning a repository + the user's own commit history into resume highlights. Carries its own copy of the STAR bullet formula + the 14 optimization dimensions so this skill can run without any file outside `skills/resume-from-code/`.
>
> **Authenticity boundary (non-negotiable).** Every claim must trace back to a commit, file, config, or artifact authored (or demonstrably owned) by the user. If a number is plausible but unverifiable, emit `<<CONFIRM: …>>` rather than inventing it. Never claim whole-repo metrics you did not measure; never list tech you didn't touch in your own commits.

---

## 1. Where highlights live

Mine these surfaces in priority order. Each is a candidate source of one or more bullets.

| Surface | What it reveals | How to read it |
|---|---|---|
| **Commit messages** | Intent, problem solved, scale hints, migration scope. | `git log --author=<user> --stat`. Look for verbs: *optimize, refactor, migrate, fix perf, cache, shard, async, parallelize*. |
| **Diff hunks** | New abstractions, perf-critical paths, error handling, concurrency primitives. | `git show <sha>` / `git log -p --author=<user> -- <path>`. Look at added lines, not just file lists. |
| **Config / CI** | Infra reality — pool sizes, replicas, resource limits, timeouts, env tiers, deployed services. | `Dockerfile`, `docker-compose.yml`, `.github/workflows/*`, `k8s/*.yaml`, `terraform/`, `helm/`, application config files. |
| **Test files** | Coverage scope, integration/load tests, fixture sizes (= scale evidence), benchmark numbers. | `*_test.go`, `test/*.py`, `__tests__/*`, JUnit / pytest / Jest; `Benchmark_*`, `locustfile`, `k6` scripts. |
| **Package manifests** | Real tech stack (no name-dropping). | `package.json`, `go.mod`, `pom.xml`, `requirements.txt`, `Cargo.toml`, `build.gradle`. Cross-check against `--author` files. |
| **README / docs** | Stated architecture, throughput claims, user-visible features. | Treat as a *lead*, never as measured truth — corroborate with code/config before quoting a number. |
| **Comments / resolved TODOs** | Latent design decisions, prior vs. after states. | `git log -S "TODO"`; look for comments explaining *why* a path is non-obvious. |
| **Migrations** | Schema evolution, indexing decisions, sharding keys. | `migrations/*.sql`, Alembic, Flyway, Liquibase, Prisma migrate. |

---

## 2. STAR bullet formula (self-contained copy)

Every bullet takes this shape — write it once per highlight, then merge into the project section.

**Base formula (CN default):**
```
为解决{问题}，基于{技术/方案}完成{关键动作}，使{指标} 提升/下降 {量化结果}，并带来{业务价值}。
```

**STAR compact expansion:**
- **Situation / Task** — the business context or engineering challenge (one short clause).
- **Action** — the technical decision and what you built (the bulk of the bullet).
- **Result** — a measurable change, with units (latency, throughput, error rate, cost, delivery cycle, business conversion).

**NA variant:** action verb + X-Y-Z — *"Accomplished X as measured by Y, by doing Z."* Never *"Responsible for …"*.

**Rewrite example (weak → strong):**
- Weak: `使用 Redis 优化了性能。`
- Strong: `针对高频查询场景引入 Redis 缓存并设置随机过期策略，接口 P95 响应由 420ms 降至 160ms，数据库峰值压力下降 65%。`

> Every bullet must survive the **interview-defense test**: can the candidate, in interview, explain (a) the business flow, (b) what they personally owned, (c) the hardest bug and its fix, (d) why this approach over alternatives, (e) how the metric was measured, (f) whether it's deployed/demoable? If a bullet can't answer all six, downgrade or cut it.

---

## 3. The 14 optimization dimensions → code signals

When expanding highlights, each bullet should hit one or more of these dimensions. The table is the canonical, self-contained list — for each dimension it gives the code/config signals to grep or read. **Do not name a dimension without a concrete method and measured effect.**

| # | Dimension | What to grep / read in the repo | Quantification angle |
|---|---|---|---|
| 1 | **Performance** | Benchmark files (`*_test.go` `Benchmark_*`, `pytest-benchmark`, JMH); profiling output; caching code; DB indexes; async/concurrency primitives; batch/bulk APIs. | P50/P95/P99 latency, RPS, throughput, allocations/op, GC pause, row scan → index lookup. |
| 2 | **Cost** | Right-sizing configs (replicas, CPU/memory limits in k8s/compose); spot/preemptible usage; storage tiering (hot/warm/cold); batching to cut API calls. | $/month, $/request, infra cost −X%, calls merged by N×. |
| 3 | **Availability** | Health checks, readiness/liveness probes, multi-AZ/region, failover configs, retry+timeout policies, circuit breakers, graceful shutdown. | Uptime %, MTTR, failover RTO/RPO, deploy-rollback time. |
| 4 | **Reliability** | Retry/backoff, idempotency keys, deduplication, dead-letter queues, transactions, 2PC/Saga, exactly-once semantics. | Error rate %, retry success %, duplicate rate ↓, data-loss events = 0. |
| 5 | **Stability** | Rate limiting, backpressure, bulkheads, queue depth caps, shedding, circuit breakers; load test artifacts (k6/Locust/wrk). | Spike survival (N× normal), dropped-request %, p99 under load. |
| 6 | **Fault tolerance** | Try/catch/except scope, panic recovery, fallbacks (cache stale, default value), bulkhead isolation, timeout budgets, chaos test configs. | Recovery time, % requests served via fallback, blast-radius (# shards affected). |
| 7 | **Robustness** | Input validation (regex, schema, protobuf validate), boundary checks, fuzz tests, property tests, nil/null guards, SQLi/XSS escaping. | Crash count, invalid-input rejection rate, fuzz iterations w/o crash. |
| 8 | **System complexity** | Module boundaries, layering, plugin/extension points, generics, DSLs; number of integrated subsystems; protocol breadth. | # components integrated, # protocols, data flow depth; describe complexity qualitatively when no number exists. |
| 9 | **Maintainability** | Shared utilities, generics, code dedup, abstraction layers, design patterns, lint config, type coverage. | Code −N lines / −N duplicates, onboard time, review turnaround, type coverage %. |
| 10 | **Scalability** | Sharding keys, partitioning, read replicas, horizontal scaling flags, stateless design, queue-based decoupling, cache layering. | QPS ceiling, scale from X→Y users, shard count, partition count. |
| 11 | **Observability** | Metrics (Prometheus/OTel/StatsD), structured logging, tracing (OpenTelemetry/Jaeger/Zipkin), dashboards (Grafana JSON), alert rules, SLO/SLI definitions. | # metrics, # dashboards, MTTD, alert precision/recall, log-volume reduction. |
| 12 | **Elasticity** | Autoscaling (HPA/KEDA), dynamic pool sizing, queue-driven scale, warmup, serverless config, connection-pool tuning. | Scale-up time, warm→cold transition, # instances min↔max, idle cost. |
| 13 | **User experience** | Frontend perf budgets, lazy-loading, prefetching, skeletons, optimistic UI, accessibility, error copy, client caching. | TTI, FCP, perceived latency ↓, error-rate on UI, a11y score. |
| 14 | **Security** | AuthN/AuthZ middleware, JWT/OAuth, RBAC, input validation, parameterized queries, XSS/CSRF guards, secret management (Vault/SOPS), audit logs, dependency scanning config. | Vuln count = 0, # auth checks enforced, # dependencies patched, CVEs remediated. |

**Rule:** name the dimension → cite the file/commit → give the measured effect. No effect, no bullet.

---

## 4. Git recipes

Concrete commands. `<USER>` is the user's git identity (name or email); `<REPO>` is the local path or `owner/name`.

### Identify the user's footprint
```bash
# Confirm the user's author identities in this repo
git shortlog -sne
# Total files / commits the user touched
git log --author="<USER>" --oneline | wc -l
git log --author="<USER>" --name-only --pretty=format: | sort -u | grep .
```

### Per-commit evidence (the workhorse)
```bash
# Commits + per-file stat (lines added/removed) for the user
git log --author="<USER>" --stat --pretty=format:"%h %ad %s" --date=short
# Full diffs (abstractions, perf paths, error handling)
git log -p --author="<USER>" -- <path>
```

### Locate when a feature/symbol appeared or evolved
```bash
# When was symbol X (function/type/string) introduced or removed?
git log -S "<symbol>" --oneline -- <path>
# Show the diff at that introduction
git show $(git log -S "<symbol>" --format="%H" -- <path> | tail -1)
```

### Scope by time / branch
```bash
# Only the user's commits in a window
git log --author="<USER>" --since="2024-01-01" --until="2024-12-31" --stat
# Commits on a feature branch not yet on main
git log --author="<USER>" main..feature/<branch> --stat
```

### Blame-driven ownership (when a file is shared)
```bash
# Which lines of <path> did the user author?
git blame -e <path> | grep "<USER>" | head
```

### Remote-only (GitHub URL) via `gh`
```bash
# Repo overview
gh repo view <owner/name>
# User's commits, paginated
gh api "repos/<owner/name>/commits?author=<USER>&per_page=100" \
  --jq '.[] | {sha: .sha[0:7], date: .commit.author.date, msg: .commit.message | split("\n")[0]}'
# Pull requests the user authored (design/intent evidence)
gh pr list --repo <owner/name> --author <USER> --state all --limit 50
# Issues the user closed (problem-finding evidence)
gh issue list --repo <owner/name> --author <USER> --state closed --limit 50
```

### Cross-check tech stack against the user's files
```bash
# Files the user touched, grouped by directory
git log --author="<USER>" --name-only --pretty=format: | sort | uniq -c | sort -rn | head -30
```

---

## 5. Quantification sources

When a number lands in a bullet, it must come from one of these. Otherwise it becomes `<<CONFIRM: …>>`.

| Source | Example | Confidence |
|---|---|---|
| **In-repo benchmark** | `Benchmark_ProcessOrder` output in CI logs, JMH report, `pytest-benchmark` JSON. | High — cite the file/test name. |
| **Test fixtures** | `tests/fixtures/orders_1m.jsonl` (1M rows), load-test `--rps 5000`. | High — fixture size = scale evidence. |
| **Config** | `maximum-pool-size: 200`, `replicas: 6`, `--max-concurrency 64`, `limits.cpu: 4`. | High — file:line citation. |
| **CI run artifacts** | `.github/workflows/bench.yml` recorded timings; uploaded reports; grafana annotations. | Medium-High — link the workflow + run. |
| **README / architecture doc** | "handles ~3k QPS at peak". | Low — **lead only**. Demote to `<<CONFIRM: …>>` unless corroborated by code/config/monitoring. |
| **Monitoring / external** | Grafana snapshot, Datadog, CloudWatch. | High — but only if the user can show the screenshot/dashboard; otherwise `<<CONFIRM: …>>`. |
| **Business metrics** | "conversion +12%". | Only if the user can produce the analytics source; otherwise `<<CONFIRM: …>>`. |

**Placeholder rule.** Emit `<<CONFIRM: e.g. P95 before/after>>` whenever a number is plausible but unverified. Aggregate the placeholders into a single short list at the end of the output and tell the user explicitly: *"these claims need a source before submission."*

---

## 6. Anti-patterns

Each anti-pattern is a hard *don't*. If tempted, emit a `<<CONFIRM: …>>` or drop the bullet.

- **Don't claim whole-repo metrics you didn't measure.** "Serves 1M users" is forbidden unless a config/monitoring artifact proves it.
- **Don't list tech you didn't touch.** If the repo's `pom.xml` lists Kafka but the user never authored a Kafka-touching file, Kafka does not appear in the user's bullets.
- **Don't claim team work as solo work.** Use `git blame`/PR review to scope; say "drove" or "owned X within a team of N" when others contributed.
- **Don't quote README numbers as fact.** README is a *lead*. Cross-check against code/config before quoting.
- **Don't invent before/after metrics.** No benchmark file → no "P95 dropped 60%" claim. Use `<<CONFIRM: …>>`.
- **Don't hide the unit.** "Improved 60%" is meaningless; "P95 latency 420ms → 160ms (−62%)" is a bullet.
- **Don't conflate dimensions.** A caching bullet is *Performance* + *Scalability*; don't relabel it *Availability* unless it has failover evidence.
- **Don't over-bulletize.** 4–6 strong bullets beat 10 vague ones. Cut anything that fails the interview-defense test.
- **Don't reuse identical wording across projects.** Each bullet must present distinct value.
- **Don't fabricate seniority signals.** If the commits show implementation, don't write "architected" or "led".

---

## 7. End-to-end checklist (run before emitting the section)

- [ ] User's git identity confirmed; every cited commit is theirs.
- [ ] Each bullet maps to ≥1 dimension in §3 and cites a file/commit.
- [ ] Every number traces to a source in §5, or is `<<CONFIRM: …>>`.
- [ ] STAR shape (Situation/Action/Result) is present in every bullet.
- [ ] 4–6 bullets total; no duplicate wording.
- [ ] Tech stack line lists only tech the user actually touched (verified by `git log --author`).
- [ ] Evidence list (亮点证据清单) maps each bullet → commit(s)/file(s).
- [ ] `<<CONFIRM: …>>` items collected and flagged for the user.
