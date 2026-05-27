# Kiro Skills Inventory

Summary of all active skills in `~/.kiro/skills/` as of 2026-05-23.

---

## 1. arm-skill
**Category:** Artifactory

ARM Artifactory REST API workflows for Company's ARM instances.

**Capabilities:**
- **Repositories** — list, create, update, delete repos (local, remote, virtual, federated); self-service repo creation via plugin
- **Artifacts** — upload, download, deploy, copy, move, delete artifacts; get file/folder info; manage artifact properties; Docker tag listing
- **Search** — GAVC search (group/artifact/version/classifier), property search, AQL queries, find latest version
- **Security** — manage permission targets, users, groups; check who has access; grant/revoke access; repo manager/owner lookup
- **System** — health check, version info, storage info, plugin listing, configuration management

**Supported package types:** Docker, Maven, Helm, npm, PyPI, Go, Generic, NuGet, Debian, RPM, Conan, Cargo

**Instances:** arm.tfmj.gic.company.se (primary), arm.sero.gic.company.se (secondary), armdocker.rnd.company.in (Docker registry)

**Requires:** `ARM_TOKEN` env var or `.netrc`, `curl`, `jq`

---

## 2. confluence-skill
**Category:** Confluence

Full Confluence workflows via REST API on eteamspace.

**Capabilities:**
- **Pages** — create, update, get, delete, move pages; manage child pages; add/remove labels
- **Search** — CQL queries, find pages by title/label, recent changes
- **Spaces** — list spaces, get space details, space content, space permissions
- **Comments** — add page comments, inline comments, reply to comments, list unresolved comments
- **Attachments** — upload files, download attachments, list attachments, update attachments

**Convenience commands:** `content <pageId>` (auto-fallback on rate limit), `scrape <pageId>` (rendered HTML), `find-by-title`, `get-page-id`, `update`, `create`

**Requires:** `CONFLUENCE_ETEAM_TOKEN` env var or `.netrc`, `curl`, `jq`, `python3`

---

## 3. daily-summary
**Category:** Productivity

Aggregates the user's daily activity across multiple platforms into a standup-ready summary.

**Capabilities:**
- **Jira** — issues created, updated, commented on, and closed/resolved by the user
- **GitLab MRs** — MRs authored (opened/updated) and MRs reviewed
- **GitLab Issues** — issues authored and assigned
- **Gerrit** — reviews authored and reviews where user commented/voted
- **Commit stats** — total commits pushed, additions/deletions per MR
- **Daily rank** — assigns a fun rank based on activity count (Ghost Mode → Unstoppable)
- **Fun stats** — net negative lines, perfect merge rate, cross-repo warrior, time spread, etc.

**Output format:** Date + rank header, plain-language summary paragraph, MR table with +/- stats, totals line, fun stats

**Configurable time window:** defaults to last 16 hours, supports "last 3 days", "this week", etc.

**Requires:** `GITLAB_TOKEN`, `JIRA_ETEAM_TOKEN` env vars, `.netrc` for Gerrit, `curl`, `jq`

---

## 4. ews-skill
**Category:** Infrastructure

Manage WS (Web Services) clusters and run kubectl commands.

**Capabilities:**
- **EWS API** — list clusters, get cluster status, query cluster details, check hosts, DNS records, cluster inventory
- **kubectl** — check pods, get events, view logs, list nodes/deployments/services, inspect namespaces, query CRDs

**Requires:** `EWS_API_KEY` env var, optionally `EWS_USER_ID` and `EWS_KUBECONFIG_DIR`, `kubectl`

---

## 5. gitlab
**Category:** GitLab

GitLab workflows for everyday developers.

**Capabilities:**
- **MR lifecycle** — create, push, fix, review, merge MRs; view MR diffs; handle bot comments; unblock MRs; list open MRs
- **Pipelines** — check pipeline status, watch pipeline progress, diagnose build failures
- **Issues** — create, list, close, assign issues; comment on issues; link to epics
- **CI/CD components** — create and manage reusable pipeline components
- **Project/group management** — move/transfer/rename projects, set avatars, create groups, set descriptions

**Auto-detects** GitLab host from git remote. Supports both `gitlab.sh` script and `glab` MCP tools.

**Requires:** `GITLAB_TOKEN` env var or `.netrc`, `curl`, `jq`, `git`

---

## 6. gitlab-cicd-component
**Category:** GitLab CI/CD

Create and publish reusable GitLab CI/CD components.

**Capabilities:**
- **Scaffold** — generate a ready-to-push component project (templates, CI config, README, LICENSE)
- **Write** — author component specs with typed inputs, secrets handling, Docker image references
- **Test** — verify components work via test pipelines
- **Publish** — release components to the CI/CD catalog with semantic versioning
- **Convert** — migrate existing templates into reusable components
- **Patterns** — boolean inputs, conditional jobs, component context, multi-component repos, job name prefixes

**Scaffold command:** `scripts/init-component.sh <name> [output-dir]`

**Requires:** `bash`

---

## 7. grill_me
**Category:** Design Review

Stress-test a plan or design through relentless questioning.

**Capabilities:**
- Interviews the user about every aspect of their plan/design
- Walks down each branch of the decision tree
- Resolves dependencies between decisions one-by-one
- Provides recommended answers for each question
- Explores the codebase to answer questions when possible (instead of asking the user)

**Trigger:** Say "grill me" or ask to stress-test a plan/design.

---

## 8. jira_ticket_enricher
**Category:** Jira

Enrich sparse Jira tickets into well-defined, development-ready tickets through interactive questioning.

**Capabilities:**
- **Assess completeness** — evaluates ticket state (minimal/partial/adequate) and reports gaps
- **Adaptive questioning** — asks only what's missing, in rounds of 2-4 related questions:
  - Tier 1: What & Why (expected behavior, problem being solved, who's affected)
  - Tier 2: Scope & Boundaries (in/out of scope, constraints, dependencies, edge cases)
  - Tier 3: Acceptance Criteria (verification conditions, non-functional requirements)
  - Tier 4: Light Implementation Direction (preferred approach, affected components)
- **Generate enriched description** — structured output with Summary, Background, Scope, Goals/AC, Technical Notes, Edge Cases
- **User confirmation** — presents enriched content for review before updating the ticket

---

## 9. jira-skill
**Category:** Jira

General JIRA workflows via REST API (v10.3+).

**Capabilities:**
- **Create issues** — stories, bugs, epics with all required fields including custom fields and components
- **Search** — JQL queries, find issues by criteria
- **Link issues** — epic links, issue-to-issue links (relates, blocks, duplicates, depends on)
- **Manage epics** — set/remove epic links, convert issue types
- **Format descriptions** — JIRA wiki markup patterns (italics headings, bullets, code blocks, unicode emoji)
- **Discover project fields** — find issue types, required fields, components, priorities, link types, transitions, custom fields

**Workflow:** discover fields → preview → create → add labels/links post-creation

**Requires:** `JIRA_ETEAM_TOKEN` env var or `.netrc`, `curl`, `jq`

---

## 10. jira-ticket-manager
**Category:** Jira

Opinionated ticket management with structured descriptions, DICE component, and auto-labels.

**Capabilities:**
- **Create tickets** — Initiative, Epic, Task, Sub-task with:
  - Structured description (Problem Statement + Acceptance Criteria)
  - Auto-derived labels from content (2-4, lowercase, hyphenated)
  - DICE component by default
  - Priority inference from context
  - Parent linking (epic link for tasks, parent task for sub-tasks)
  - Mandatory project key gate (asks if not provided)
- **Update tickets** — field-by-field updates with diff-style preview:
  - Updatable: summary, description, priority, labels, component, parent link
  - Not updatable: issue type, project key
  - Shows before/after for each changed field
- **Comment on tickets** — structured templates based on ticket type:
  - Tasks/Sub-tasks: Issues Identified → Resolution → Pending Items → Commits (auto-detected from git log)
  - Epics: Implemented → Pending Items → MR Link → Acceptance Criteria Status (validates against description)

**All actions require user confirmation via preview before execution.**

**Requires:** `JIRA_ETEAM_TOKEN`, `JIRA_ETEAM_URL` env vars, `curl`, `jq`, `git`

---

## 11. jira-worklog-standard
**Category:** Jira

Log work on Jira issues following a consistent team format.

**Capabilities:**
- Formats worklogs with date header, named sessions with durations, and specific activity bullets
- Enforces quality: each bullet must be specific and actionable (not vague)
- Supports multiple sessions per day (Morning, Afternoon, or by topic)
- Validates that session durations sum to total time
- Handles past dates with proper UTC formatting
- Supports multiple worklogs across different tasks in one go
- Quick-log mode for minimal input
- Always shows preview before logging

**Format:** `## Work Summary — {Date}` → `### {Session} ({duration})` → `- {specific activity}`

**Rule:** Always log on sub-tasks, never on parent Stories.

---

## 12. kata-creator
**Category:** Training

Create structured kata exercises for hackathons, coding dojos, and workshops.

**Capabilities:**
- **Interview** — gathers topic, audience, duration, tools, outcome, format
- **Design flow** — progressive sequence following install → use → create pattern
- **Generate structure** — full folder layout with README.md, kata directories, templates
- **Write katas** — each with prerequisites, step-by-step instructions, checkpoints, stretch goals
- **Audit** — review and improve existing kata content

**Output structure:** Landing README → Kata index → Preflight checklist → Progressive kata directories with instructions and starter templates

---

## 13. optimize-dockerfile
**Category:** Docker

Optimize existing Docker images for size, security, and build performance.

**Capabilities:**
- **Multi-stage builds** — separate build and runtime stages (e.g., 800MB → 10MB)
- **Layer optimization** — combine RUN commands, use `--no-install-recommends`, clean up in same layer
- **Dependency ordering** — copy dependency files first for better cache hits (package.json before source)
- **Base image selection** — recommend minimal base images (scratch, alpine, distroless)
- **Security hardening** — non-root users, minimal packages, no secrets in layers

**Does NOT create new Dockerfiles from scratch** — only optimizes existing ones.

---

## 14. readme-md-creator
**Category:** Documentation

Generate or improve README.md files following standard-readme spec and open-source best practices.

**Capabilities:**
- **Auto-analyze** — scans tech stack, build system, project structure, CI/CD, config, and media assets
- **Detect project type** — library, service, CLI, or monorepo — adapts sections accordingly
- **Generate README** — following standard-readme spec with proper section ordering
- **Improvement mode** — if README exists, enhances it rather than replacing
- **Extracts real data** — pulls scripts from package.json/Makefile, test frameworks, CI config, env vars

---

## 15. reflection-memory
**Category:** Meta / Tooling

Post-task self-assessment — record what worked, what failed, and how to improve.

**Capabilities:**
- **Store reflections** — after task completion, records: task summary, outcome (success/partial/failure), what worked, what didn't, lesson learned, next-time action
- **Query before similar tasks** — search past reflections to apply lessons and avoid repeating mistakes
- **Query failures** — filter specifically for past failures to learn from them
- **Permanent, append-only** — reflections are never updated or deleted

**Storage format:** Topic path `<agent-name>/reflections/<YYYY-MM-DD>/<slug>` with importance 8 (high)

**Key rule:** "Next time" must be a concrete action, not a vague intention.

---

## 16. skill-creator
**Category:** Meta / Tooling

Create new skills and iteratively improve them through an eval loop.

**Capabilities:**
- **Capture intent** — interview to understand what the skill should do, triggers, output format
- **Write SKILL.md** — proper frontmatter (name, description, tags, metadata, compatibility) and body
- **Progressive disclosure** — guides on when to use references vs inline content
- **Test cases** — generate realistic test prompts, run via subagents, compare with/without skill
- **Evaluate** — grade results with assertions, blind A/B comparison between versions
- **Iterate** — improve based on feedback, rerun tests, compare iterations
- **Description optimization** — generate trigger eval queries (should/shouldn't trigger), iterate on description for accuracy

**Skill anatomy:** SKILL.md (required) + optional scripts/, references/, assets/

---

## 17. sonarqube-skill
**Category:** Code Quality

SonarQube REST API workflows for code quality analysis.

**Capabilities:**
- **Quality gates** — check pass/fail status, gate conditions, new code quality
- **Issues** — view bugs, vulnerabilities, code smells, security issues, hotspots; filter by severity/type/file
- **Measures** — inspect coverage, duplication, lines of code, complexity, and other metrics
- **Projects** — search projects by name, get project info, list branches, view pull request analysis, manage settings

**Instance:** codeanalyzer2.internal.company.com

**Requires:** `.netrc` entry (token as login, empty password), `curl`, `jq`