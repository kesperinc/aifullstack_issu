# 엔터프라이즈 코딩 에이전트 MVP 단계별 개발 TODO 로드맵 (with Vibe Coding)

본 문서는 **코딩 에이전트 MVP의 단기 구현 과제 (Desktop-First) 및 중장기 기능 개발 로드맵**을 관리하는 TODO 목록입니다.

---

## 🎯 MVP 단기 개발 과제 (Stage 1 Desktop ~ Stage 3 On-Premise)

### Stage 1: 로컬 데스크톱(Desktop-First) 실행 버전 구축
- [x] 프로젝트 메인 `README.md` 및 Vibe Coding 개념 정립
- [x] Git 브랜치 전략 수립 (`main`, `staging`, `feature/vibe-coding-agent`)
- [ ] 로컬 데스크톱 Runner 스크립트 작성 (`mvp/coding-agent/src/desktop_runner.py`)
- [ ] Vibe Coding 요구사항 파서 & 다중 파일 자율 생성기 작성 (`mvp/coding-agent/src/vibe/`)
- [ ] OpenRouter API Key 시크릿 감지 Pre-commit Hook 적용

### Stage 2: GCP 기반 멀티 테넌트 & MCP 라우터 확장
- [ ] GCP 인프라 구축 및 개발자 테넌트별 Docker 샌드박스 할당기
- [ ] MCP (Model Context Protocol) JSON-RPC 게이트웨이 포트(3000) 바인딩
- [ ] VS Code (Continue.dev) 및 Agentic CLI (Antigravity/Claude Code) MCP 커넥터 연동

### Stage 3: 온프레미스 (Red Hat OpenShift AI SNO) 1-Click 포팅 & 시연
- [ ] 10월 Red Hat 행사 시연용 파이썬/자바 실시간 Vibe 코딩 및 FIM 샘플 프로젝트 준비 (`mvp/coding-agent/samples/`)
- [ ] OpenShift AI (SNO) vLLM 엔드포인트 호환 어댑터 1-Click 스위칭 포팅
- [ ] 샌드박스 자율 `pytest` 실행 및 에러 셀프코렉션(Self-Correction) 라이브 부스 연출

---

## 🚀 중장기 구현 과제 (Mid/Long-term Backlog)

- [ ] **Multi-tenant Quota Management**: 개발자별 일단위/월단위 LLM 토큰 사용량 제한 및 예산 모니터링
- [ ] **Domain Fine-tuning Pipeline**: 사내 프레임워크 전용 Qwen2.5-Coder LoRA 파인튜닝
- [ ] **Enterprise Audit Dashboard**: 에이전트 커밋 및 코드 변경점 시계열 감사 대시보드
