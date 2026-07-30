# gstack — AI Engineering Workflow

gstack is a collection of SKILL.md files that give AI agents structured roles for
software development. Each skill is a specialist: CEO reviewer, eng manager,
designer, QA lead, release engineer, debugger, and more.

## 프로젝트 필수 개발 및 운영 규칙 (Project Mandatory Rules)

본 프로젝트는 엔터프라이즈 코딩 에이전트 및 AI 솔루션 패키지 개발 시 다음 13가지 수칙과 가드레일을 100% 준수합니다:

1. **시연용 MVP 개발 폴더 분리**: 코딩 에이전트 MVP부터 시작하며, 코드 및 아티팩트는 `mvp/coding-agent/` 및 지정 디렉터리에 분리하여 개발한다.
2. **Vibe Coding (바이브 코딩) 플랫폼 정의 & 도입**: 
   - *Vibe Coding 정의*: 개발자가 구체적 코딩 문법이나 보일러플레이트에 얽매이지 않고, 자연어 수준의 아이디어와 도메인 의도("Vibe")를 제시하면, AI 에이전트가 요구사항 분석, 스키마 정의, 다중 파일 생성, 샌드박스 테스트, 셀프코렉션까지 전 과정을 자율 완성하는 **'의도 중심 자율 개발 패러다임(Intent-Driven Autonomous Coding)'**.
3. **Desktop-First ➔ Cloud ➔ On-Premise 3단계 배포**: 
   - 개발자의 로컬 데스크톱(Desktop/Workstation) 환경에서 먼저 100% 동작 가능한 버전을 만든 후, 구글 클라우드(GCP) 및 온프레미스(Red Hat OpenShift AI)로 단계별 이식한다.
4. **GCP 기반 개발 & Git 브랜치 체계**: 개발은 GCP 및 로컬 환경에서 시작하며, Git 저장소는 `main`, `staging`, `feature/*` 브랜치 전략을 준수한다.
5. **작업 트라이어드 (Plan-Code-Doc)**: 작업이 시작되면 반드시 **[작업계획서] - [개발된 코드] - [상세명세서]**를 1:1:1 쌍으로 작성한다.
6. **개발-배포-테스트 가드레일 & 워크플로우**: PR 제출 전 테스트 통과, 코드 스타일 및 SAST 보안 검사를 거치는 가드레일을 준수한다.
7. **개발자별 워크스페이스 부여**: 멀티 테넌시 및 개발자별 격리된 개발 워크스페이스(Workspace/Sandbox) 제공 구조를 구현한다.
8. **Cloud to On-Prem 하드웨어 포팅 전략**: 데스크톱/GCP에서 테스트 완료 후 10월/11월 온프레미스 HW(RHOAI) 준비 시 1-Click 이식을 실행한다.
9. **Agentic CLI (Codex, Claude Code, Antigravity) 연동**: MCP(Model Context Protocol)를 통해 CLI 및 IDE(VS Code/Jupyter)와 즉시 연동되도록 바인딩 인터페이스를 개발한다.
10. **개발 기간 비용 최적화 (OpenRouter / Direct API Call)**: 온프레미스 GPU 전 단계에서는 OpenRouter API 및 직접 모델 호출을 활용하여 인프라 비용을 최소화한다.
11. **시연용 샘플 준비**: 행사에 직접 관람객이 시연할 수 있는 파이썬/자바 실시간 Vibe 코딩 및 FIM 샘플 코드를 준비한다.
12. **기초/상세 설계서 작성**: 플랫폼 전반의 기본설계서(`docs/coding_agent_basic_design.html`) 및 상세설계서를 수립한다.
13. **UI/UX 초안 HTML 작성**: 개발자 대시보드 및 워크스페이스 관리 웹 UI/UX 초안을 모던 HTML로 작성하여 제공한다.

---

## Available skills

Skills live in `.agents/skills/`. Invoke them by name (e.g., `/office-hours`).

| Skill | What it does |
|-------|-------------|
| `/office-hours` | Start here. Reframes your product idea before you write code. |
| `/plan-ceo-review` | CEO-level review: find the 10-star product in the request. |
| `/plan-eng-review` | Lock architecture, data flow, edge cases, and tests. |
| `/plan-design-review` | Rate each design dimension 0-10, explain what a 10 looks like. |
| `/design-consultation` | Build a complete design system from scratch. |
| `/review` | Pre-landing PR review. Finds bugs that pass CI but break in prod. |
| `/debug` | Systematic root-cause debugging. No fixes without investigation. |
| `/design-review` | Design audit + fix loop with atomic commits. |
| `/qa` | Open a real browser, find bugs, fix them, re-verify. |
| `/qa-only` | Same as /qa but report only — no code changes. |
| `/ship` | Run tests, review, push, open PR. One command. |
| `/document-release` | Update all docs to match what you just shipped. |
| `/retro` | Weekly retro with per-person breakdowns and shipping streaks. |
| `/browse` | Headless browser — real Chromium, real clicks, ~100ms/command. |
| `/setup-browser-cookies` | Import cookies from your real browser for authenticated testing. |
| `/careful` | Warn before destructive commands (rm -rf, DROP TABLE, force-push). |
| `/freeze` | Lock edits to one directory. Hard block, not just a warning. |
| `/guard` | Activate both careful + freeze at once. |
| `/unfreeze` | Remove directory edit restrictions. |
| `/gstack-upgrade` | Update gstack to the latest version. |
