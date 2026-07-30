# 🚀 Antigravity VibeForge Enterprise MVP 단계별 TODO 로드맵

본 문서는 **Antigravity VibeForge Enterprise (Vibe Coding Agent OS)**의 Stage 1~3 개발 과제 및 중장기 로드맵 현행화 목록입니다.

* **최종 현행화 일자**: 2026년 7월 30일
* **현재 완성 단계**: **Stage 1 (Desktop-First MVP) 100% 완료**

---

## 🎯 MVP 단기 개발 과제 (Stage 1 Desktop ~ Stage 3 On-Premise)

### ✅ Stage 1: 로컬 데스크톱(Desktop-First) 실행 버전 구축 (100% 완료)
- [x] 공식 제품 브랜드 정립: **`Antigravity VibeForge Enterprise`** (약칭: **`VibeForge AI`**)
- [x] 프로젝트 메인 `README.md` 및 Vibe Coding 자율 개발 패러다임 개념 정립
- [x] Git 브랜치 전략 수립 및 GitHub 원격 저장소 동기화 (`main`, `staging`, `feature/vibe-coding-agent`)
- [x] 1-Click OS별 데스크톱 실행 스크립트 구축 (`run_desktop.bat`, `run_desktop.sh`)
- [x] 로컬 데스크톱 Runner 엔진 구현 (`mvp/coding-agent/src/desktop_runner.py`)
- [x] React IDE UI/UX 대시보드 구축 (`proposal/coding_agent_ui_mockup.html`)
  - [x] View / Go / Run / Terminal 메타 메뉴 및 **Agentic CLI(`Antigravity`, `Claude Code`, `Codex`)** 연동
  - [x] VS Code 공식 엠블럼 Icon 및 `🛒 Extensions Market` 접근 모달
  - [x] 코드 창 아래 **Coding Agent SOTA 모델 선택 바** (Qwen 2.5 Coder, Claude 3.5 Sonnet, DeepSeek Coder V2, GPT-4o, Llama 3.3 70B 1-Click Vibe 연동)
  - [x] 다중 파일 준비 코드 탭 시스템 (`auth_service.py`, `test_auth.py`, `models.py`, `config.py`)
  - [x] `🔑 OpenRouter OAuth & API Key` 연동 모달
- [x] FastAPI 백엔드 Vibe 오케스트레이션 엔진 구축 (`mvp/coding-agent/src/main.py`, `Port 5000`)
  - [x] Vibe 파서, Agent Thinking Stream, Code Diff, 샌드박스 `pytest` 검증 & 셀프코렉션(Self-Correction) 연동
- [x] OpenRouter API Key 시크릿 유출 방지 검사 스크립트 작성 (`mvp/coding-agent/scripts/check_secrets.py`)
- [x] Stage 1 개발 작업일지 작성 및 저장 (`docs/worklog/2026-07-30_vibeforge_stage1_worklog.md`)

---

### 🔜 Stage 2: GCP 기반 멀티 테넌트 & MCP 라우터 확장 (차기 진행 과제)
- [x] MCP (Model Context Protocol) JSON-RPC 게이트웨이 포트(3000) 바인딩 (`mvp/coding-agent/src/mcp/router.py`)
- [x] VS Code (Continue.dev) 및 Agentic CLI 커넥터 인터페이스 연동
- [ ] GCP GKE 기반 개발자 테넌트별 동적 Docker 샌드박스 할당기 구현
- [ ] 개발자별 일단위/월단위 LLM 토큰 사용량 할당 및 쿼터(Quota) 모니터링 API

---

### 🔜 Stage 3: 온프레미스 (Red Hat OpenShift AI SNO) 1-Click 포팅 & 시연
- [x] OpenShift AI (SNO) vLLM 엔드포인트 호환 어댑터 1-Click 스위칭 포팅 (`mvp/coding-agent/src/adapters/llm_adapter.py`)
- [x] 샌드박스 자율 `pytest` 실행 및 에러 셀프코렉션(Self-Correction) 시연 로직 준비
- [ ] 10월 Red Hat 행사 부스 시연용 파이썬/자바 실시간 Vibe 코딩 및 FIM 샘플 프로젝트 작성 (`mvp/coding-agent/samples/`)
- [ ] OpenShift AI (SNO) 단일 노드(Baremetal) 1-Click 배포 헬름 차트 및 매니페스트 작성

---

## 🚀 중장기 구현 과제 (Mid/Long-term Backlog)

- [ ] **Enterprise Multi-tenant Quota System**: 프로젝트/팀별 LLM 토큰 소비 예산 제한 및 알림
- [ ] **Domain Fine-tuning Pipeline**: 사내 프레임워크 및 도메인 전용 Qwen2.5-Coder LoRA 파인튜닝 파이프라인
- [ ] **Enterprise Audit Dashboard**: 코딩 에이전트 자율 커밋 및 코드 변경점 시계열 감사 웹 대시보드

---

© 2026 AI Architecture Engineering Team. All rights reserved.
