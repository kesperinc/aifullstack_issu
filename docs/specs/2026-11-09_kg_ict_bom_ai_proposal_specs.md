# [상세명세서] KG ICT × KGM 모빌리티 BOM 인텔리전스 챗봇 구축 사업제안서 고도화 및 원격 저장소 현행화 명세

- **문서 번호**: SPEC-2026-11-09-KGICT-BOM
- **작성 일자**: 2026-11-09
- **대상 고객**: KG ICT (KGM 모빌리티 IT 담당)
- **수행 기간 / 공수**: 총 4개월 (16주) / 총 20.0 M/M (금액 표기 제외 고객 설명용 버전)

---

## 1. 작업 개요 (Overview)
1. **타 PC 원격 GitHub 작업 내역 동기화**:
   - `kesperinc/aifullstack_issu` 원격 저장소의 `origin/main` 최신 커밋(`4de0753`, `feature/vibe-coding-agent` 병합 및 Akamai/NCP·원익 AX·대구 AIDC·Hybrid Cloud 4+1 문서 통합본)을 로컬 `main` 브랜치로 완벽히 현행화 완료.
   - `kesperinc/kg-ict-bom-ai-proposal` 원격 저장소(`cb573c2`)의 KG ICT 제안서 자산을 현행 워크스페이스(`docs/kg_ict/`) 및 로컬 `c:\dev\antigravity-workspace\KGict\`와 통합 동기화.
2. **KG ICT 고객 대면 제안 설명용 최종본 제작 (HTML / DOCX / PPTX / MD)**:
   - **전체 수행 기간**: 총 **4개월 (16주)** WBS 체계 적용 (1개월차 상호 데이터 준비 및 표준 컨테이너 AI 플랫폼 셋업 ➔ 2개월차 메타데이터 및 듀얼 임베디드 DB 구축 ➔ 3개월차 Coding Agent 및 음성/트리 UI 개발 ➔ 4개월차 100선 정합성 90%+ 검증 및 오픈).
   - **특정 제품명 전면 배제 및 일반 기술 용어화**:
     - 특정 벤더/오픈소스 제품명(Nota.ai, DuckDB, Kùzu, SGLang, vLLM, RHOSAI, Whisper 등)을 모두 제거하고, **모델 경량화 솔루션**, **경량화 코딩 특화 모델**, **초경량 고속 서빙 솔루션**, **분석형 임베디드 DB + 임베디드 그래프 DB (듀얼 임베디드 DB)**, **표준 컨테이너 AI 플랫폼**, **온프레미스 음성인식(STT) 모델** 등으로 명확하고 이해하기 쉽게 풀어서 서술.
   - **투입 공수(M/M) 포함 및 금액(원화) 전면 제외**:
     - 총 투입 공수 **20.0 M/M** (PM/AI 아키텍트 특급 `3.0 M/M`, Lead Coding Agent 고급 `4.0 M/M`, 온프렘/클라우드 LLM 고급 `4.0 M/M`, BOM 데이터/그래프 중급 `5.0 M/M`, UI/UX & 음성/QA 중급 `4.0 M/M`) 상세 표기.
     - 모든 단가, 소계, 하드웨어/소프트웨어 견적 금액(`원`, `억 원` 등)을 전면 제거하여 기술·일정·투입공수 중심의 고객 미팅용 제안서로 완성.

---

## 2. 변경 일자별 파일 수정 맵 (Specs Map - 2026-11-09)

| 구분 | 파일 경로 | 변경 유형 | 주요 내용 및 역할 |
| :--- | :--- | :---: | :--- |
| **HTML 제안서** | `docs/kg_ict/KG_ICT_BOM_AI_Proposal.html`<br>`docs/kg_ict/2026-11-09_KG_ICT_BOM_AI_Proposal.html` | 수정/생성 | 고객 발표 및 웹 브라우징용 인터랙티브 HTML 제안서 (4개월/16주 WBS, 20.0 M/M 공수표, 금액 제외) |
| **Word 제안서** | `docs/kg_ict/KG_ICT_BOM_AI_Proposal.docx`<br>`docs/kg_ict/2026-11-09_KG_ICT_BOM_AI_Proposal.docx` | 수정/생성 | 고객 제출 및 인쇄용 Word(`.docx`) 사업제안서 (전 9개 장 상세 구성, 표지·아키텍처·WBS·20.0 M/M·용어집 포함, 금액 제외) |
| **PPTX 요약본** | `docs/kg_ict/KG_ICT_BOM_AI_Proposal.pptx`<br>`docs/kg_ict/2026-11-09_KG_ICT_BOM_AI_Proposal.pptx` | 수정/생성 | 대면 브리핑용 프레젠테이션 슬라이드 (4개월/20.0 M/M 반영, 금액 제외) |
| **Markdown 원본** | `docs/kg_ict/KG_ICT_BOM_AI_Proposal.md`<br>`docs/kg_ict/2026-11-09_KG_ICT_BOM_AI_Proposal.md`<br>`docs/kg_ict/README.md` | 수정/생성 | 마크다운 제안서 원본 및 저장소 README 현행화 |
| **빌드 도구** | `scripts/tools/build_kg_ict_docs.py` | 신규 생성 | `python-docx` 및 `python-pptx` 기반 제안 문서 자동 생성 스크립트 |
| **상세명세서** | `docs/specs/2026-11-09_kg_ict_bom_ai_proposal_specs.md` | 신규 생성 | Plan-Code-Doc 트라이어드 상세명세서 |

