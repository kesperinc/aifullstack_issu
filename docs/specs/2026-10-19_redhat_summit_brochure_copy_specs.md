# 2026-10-19 Red Hat Summit 부스 전시 브로셔 문안 작업 명세서 (Specs)

> **작성 일자**: 2026-10-19  
> **작성자**: AI Architecture Engineering Team  
> **문서 버전**: v1.0  
> **관련 문서**: [docs/2026-10-19_redhat_summit_brochure_copy_proposals.md](file:///c:/dev/antigravity-workspace/aifullstack/docs/2026-10-19_redhat_summit_brochure_copy_proposals.md)  

---

## 1. 개요 및 목적

본 명세서는 10월 Red Hat Summit 행사 부스 전시에 사용될 홍보 리플릿/브로셔(A4 규격 중 반 페이지 분량) 제작을 위해, 마케팅 및 디자인팀에 전달할 **MegazoneCloud AI Full Stack** 소개 문안의 기획 및 3개 시안 작성 작업 내역을 투명하게 기록하고 추적하기 위한 변경 명세서입니다.

---

## 2. 변경 파일 맵 (Specs Map)

| 변경 일자 | 구분 | 대상 파일 경로 | 주요 작업 내용 및 설명 |
| :--- | :--- | :--- | :--- |
| **2026-10-19** | 신규 생성 | `docs/2026-10-19_redhat_summit_brochure_copy_proposals.md` | Red Hat Summit 부스 전시용 브로셔(AI Full Stack & Articul8 연계 반 페이지 분량) 3개 시안 및 마케팅 가이드 작성 |
| **2026-10-19** | 신규 생성 | `docs/specs/2026-10-19_redhat_summit_brochure_copy_specs.md` | 본 작업 명세서 문서 생성 (작업 내역 추적 및 형상 관리) |

---

## 3. 세부 작업 명세 및 산출물 요약

### 3.1 템플릿 호환성 확보
- 기존 `AIR Studio on OpenShift` 리플릿의 3단 시각 레이아웃(헤더 ➔ 아키텍처 다이어그램 ➔ 01/02/03 핵심 기능 카드)을 1:1로 수용할 수 있도록 텍스트 구조 설계.

### 3.2 3대 시안 수립
1. **제1안 (인프라 & 플랫폼 종합형)**: Dell/NVIDIA GPU + Red Hat OpenShift AI (SNO) + vLLM/KServe 기반 턴키 엔터프라이즈 AI 풀스택 인프라 강조.
2. **제2안 (코딩 에이전트 특화형)**: 폐쇄망(Air-Gapped) 환경에서의 소스코드 보안 및 MCP 연동 자율 코딩 에이전트(VibeForge) 라이브 데모 연계 강조.
3. **제3안 (Articul8 시너지 결합형)**: 상단 반 페이지(Articul8)와 하단 반 페이지(MegazoneCloud AI Full Stack)가 하나의 엔터프라이즈 생성형 AI 패키지로 이어지는 유기적 구성 제안.

---

## 4. 형상 관리 (Git)

- **대상 브랜치**: `feature/vibe-coding-agent`
- **커밋 메시지**: `docs: add Red Hat Summit brochure copy proposals and specs (2026-10-19)`
