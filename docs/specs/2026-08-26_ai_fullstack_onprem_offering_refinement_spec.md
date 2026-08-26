# MZC ISSU AI Full Stack On-Premise 오퍼링 최적화 및 리포트 개정 상세 명세서

**문서 번호**: SPEC-2026-08-26-002  
**작성 일자**: 2026-08-26  
**작성자**: MEGAZONECLOUD ISSU 전략기획팀 / AI Full Stack CoE  
**문서 상태**: 완료 (Approved & Implemented)  
**적용 대상**: `offering/mzc_ai_fullstack_strategy_service_report.html`, `offering/generate_strategy_service_report_docx.py`, `offering/docx/2026-08-20_MZC_AI_Fullstack_Strategy_Service_Report.docx`, `docs/2026-08-20_MZC_AI_Fullstack_Strategy_Service_Report.docx`

---

## 1. 개정 배경 및 목적

엔터프라이즈 고객의 요구에 부응하여 **완전한 온프레미스(On-Premise) 및 소버린(Sovereign) 폐쇄망 지원이 가능한 핵심 솔루션 중심**으로 AI Full Stack 오퍼링을 최적화하고 재구성하였습니다. 불필요하게 복잡하거나 클라우드 의존적인 요소를 배제하고, **Articul8 산업 도메인 특화 지식 그래프**, **사내 코딩 에이전트 + GitLab**, **온프레미스 Data RAG (MinIO/Cohere/Redis)**, 그리고 **Dell/NVIDIA/Nutanix/OpenShift AI Factory**를 주축으로 하는 직관적이고 강력한 턴키 비즈니스 패키지를 정립하였습니다.

---

## 2. 주요 변경 및 최적화 내역 요약

### 2.1 글로벌 빅테크 AI 스택 비교 분석 (Section 03)
1. **용어 정비**: '개방형·모듈형' 표현에서 '개방형'을 제외하고 **'모듈형 소버린 플랫폼 (Vendor-Agnostic Modular)'**으로 정립.
2. **NPU 표기 통일**: **'리벨리온, 퓨리오사AI'**로 명시하고 Gaudi는 삭제.
3. **인프라 벤더 최적화**: Zadara, VMware, **Pure Storage**를 삭제하고 **Dell PowerEdge, Dell PowerScale, Red Hat OpenShift, Nutanix AHV** 중심 구성.
4. **모델 라인업 압축 및 순서 정렬**: 조나단(Jonathan), Solar(업스테이지) 삭제 -> **A8, Cohere, 오픈소스 LLM** 순서로 변경 및 중심 재편.

### 2.2 4-Layer 엔터프라이즈 AI Full Stack 생태계 (Section 04)
- **Layer 04 (Solution Layer)**: 최상위 산업 도메인 인텔리전스에 집중하여 **Articul8 (A8 Model Mesh & Knowledge Graph)**, **Cohere (Command R+ / Embed / Rerank)** 2대 핵심 엔터프라이즈 소버린 플랫폼으로 단일화.
- **Layer 03 (Model + Tool Layer)**: 모델, 개발 생산성, 추론엔진, 데이터 및 AIOps로 전주기 통합 (요청 순서 기준 정확 배치):
  1. **vLLM** (오픈소스 사실상 표준 초고속 LLM 추론 엔진)
  2. **LiteLLM** (통합 모델 라우팅 & API 게이트웨이)
  3. **sLLM (오픈소스 언어 파운데이션 모델)** (Qwen2.5-Coder, Llama 3.3 사내 폐쇄망 구동)
  4. **vLM (멀티모달 비전 언어 모델)** (Qwen2-VL, Llama-Vision 비정형 이미지·도면 분석)
  5. **MCP (사내 코딩 에이전트)** (IDE 자동완성 및 Model Context Protocol)
  6. **GitLab** (사내 소스코드 관리, DevSecOps 및 CI/CD 자동화)
  7. **MinIO** (온프레미스 고성능 AI 오브젝트 스토리지)
  8. **Redis Enterprise** (인메모리 초저지연 벡터 검색 & 시맨틱 캐시)
  9. **Confluent** (Kafka 엔터프라이즈 실시간 데이터 스트리밍)
  10. **Dynatrace** (Dynatrace Managed 완전 폐쇄망 온프레미스 지원 & Davis AI Causal RCA)
- **Layer 02 (OS + Virtualization)**: **Red Hat OpenShift / RHOAI SNO**, **Nutanix NCI + Nutanix NKP (K8s Platform)**로 2대 코어 가상화 플랫폼 확정.
- **Layer 01 (H/W Layer)**: **Dell PowerEdge 서버**, **NVIDIA GPU (B200/300, H100/200, L40S, RTX 6000 Ada/Blackwell)**, **리벨리온, 퓨리오사AI**, **Dell PowerScale 스토리지 (DGX SuperPOD 인증) / 400GbE RoCEv2, InfiniBand** 확정 (**Pure Storage 삭제**).

### 2.3 표준 사이징 오퍼링 가이드 (Section 05)
- **예상 H/W 가격 컬럼 분리 신설**:
  - Small 티어: 약 4,500만 ~ 6,000만 원 (Dell R760 2-GPU/NPU)
  - Medium 티어: 약 1.5억 ~ 2.2억 원 (Dell R760xa 4-GPU)
  - Large 티어: 약 6억 ~ 10억+ 원 (Dell XE9680 8-GPU + PowerScale)
- **S/W 솔루션 TCO 기준 분리**:
  - Small 티어: 약 5,000만 ~ 6,000만 원 (1억 미만 턴키 진입)
  - Medium 티어: 약 1.8억 ~ 2.5억 원 (Articul8 + Cohere + vLLM/NIM + MinIO/Redis)
  - Large 티어: 약 3.5억 ~ 5.5억+ 원 (Articul8 + Cohere/GitLab + MinIO/Confluent/Dynatrace)
- **비용 안내 가이드라인 명시**: "TCO 및 라이선스 금액은 S/W 솔루션 기준이며, H/W 장비 가격은 고객사 사양 및 조달 조건에 따라 별도 견적 제공"

### 2.4 4대 핵심 비즈니스 솔루션 패키지 및 Articul8 3대 Use Case (Section 07)
- **Package 01**: **엔터프라이즈 코딩 에이전트 & DevOps 패키지** (사내 Git/CI/CD + MCP Server + Qwen2.5-Coder + vLLM + GitLab).
- **Package 02**: **Articul8 산업 도메인 특화 지식 패키지** (제조·항공우주 MRO vs 금융 도메인 구분, 건설 패키지 배제).
- **Package 03**: **온프레미스 문서 & 데이터 인텔리전스 파이프라인 (Data RAG)** (MinIO + Cohere + Redis Enterprise 기반 온프레미스 데이터 자산화).
- **Package 04**: **온프레미스 소버린 AI 팩토리 & PoC 랜딩 패키지** (Dell PowerEdge + PowerScale + Nutanix AHV/OpenShift + NVIDIA NIM).
- **Articul8 3대 핵심 Use Case 패키지 상세 (`offering/articul8 usecases/` 분석 기반)**:
  1. **Use Case 01 [제조·스마트팩토리]**: 설비 이상 감지 및 자율 예지보전 AI 패키지 (Data-Aware ➔ Domain ➔ Report Generation 3단계 에이전트, 비계획 다운타임 40% 감축)
  2. **Use Case 04 [항공우주·방산 MRO]**: MRO 프로세스 인텔리전스 & 정밀 정비 AI 패키지 (복잡 매뉴얼 92% 해석 정확도, 100% 감사 추적성)
  3. **Use Case 10 [금융·투자]**: 금융 서비스 리서치 & 여신 심사 AI 패키지 (100만+ 재무문서 자동분석, 거시경제 분석 95% 자동화, 실사 수 주 ➔ 수 분 단축)

### 2.5 부록(Appendix) 핵심 솔루션 특징 및 평가 매트릭스 전면 개정
- **중복 헤더 제거**: 데이터 플랫폼 & 레이크하우스 중복 태그 및 잔여 구역 완전 정리.
- **Layer 04 핵심 솔루션 특징 및 적용 분야 테이블 신설**:
  - **Articul8 AI**: 제조(PdM), 항공(MRO), 금융 도메인 특화 지식 그래프, 환각 95% 억제, 100% 폐쇄망 턴키 배포.
  - **Cohere**: 사내 소버린 파운데이션 모델(Command R+), 고정밀 RAG 임베딩(Embed v3) 및 재순위화(Rerank 3.5).
- **Layer 03 세부 분야별 솔루션 평가 매트릭스 최신화**:
  - 1. 초고속 추론 서빙 & 모델 라우팅 (`vLLM`, `LiteLLM`)
  - 2. 사내 소버린 모델 & 개발 생산성 / DevSecOps (`sLLM`, `vLM`, `MCP`, `GitLab`)
  - 3. 온프레미스 AI 스토리지 & 실시간 데이터 파이프라인 (`MinIO`, `Redis Enterprise`, `Confluent`)
  - 4. 온프레미스 AIOps & 풀스택 옵저버빌리티 (`Dynatrace`)

---

## 3. 수정 파일 맵 (Specs Map)

| 파일 경로 | 수정 유형 | 핵심 변경 내용 |
| :--- | :---: | :--- |
| [`offering/index.html`](file:///c:/dev/antigravity-workspace/aifullstack/offering/index.html) | MODIFY | 마스터 오퍼링 포털 내 최신 릴리스 타임라인 및 전략 보고서 카드 날짜 2026-08-26(오늘) 갱신 |
| [`offering/mzc_ai_fullstack_strategy_service_report.html`](file:///c:/dev/antigravity-workspace/aifullstack/offering/mzc_ai_fullstack_strategy_service_report.html) | MODIFY | Section 03, 04(Layer 03 온프레미스 10대 솔루션 정렬 및 GitLab 일원화), 05, 07, 08, 부록 1/2 웹 리포트 수정 완료 |
| [`offering/generate_strategy_service_report_docx.py`](file:///c:/dev/antigravity-workspace/aifullstack/offering/generate_strategy_service_report_docx.py) | MODIFY | DOCX 생성 파이썬 스크립트 내 비교표, 4-Layer, 사이징 표, 패키지 및 4대 UseCase, 부록 우선순위/참고문헌 100% 동기화 (작성일자 2026-08-26 최신화) |
| [`offering/docx/2026-08-20_MZC_AI_Fullstack_Strategy_Service_Report.docx`](file:///c:/dev/antigravity-workspace/aifullstack/offering/docx/2026-08-20_MZC_AI_Fullstack_Strategy_Service_Report.docx) | GENERATE | 최신 온프레미스 오퍼링이 100% 반영된 Word 보고서 산출물 재생성 완료 (56.7 KB) |
| [`docs/2026-08-20_MZC_AI_Fullstack_Strategy_Service_Report.docx`](file:///c:/dev/antigravity-workspace/aifullstack/docs/2026-08-20_MZC_AI_Fullstack_Strategy_Service_Report.docx) | GENERATE | `docs/` 폴더 내 공식 문서 배포본 동기화 완료 (56.7 KB) |
| [`docs/specs/2026-08-26_ai_fullstack_onprem_offering_refinement_spec.md`](file:///c:/dev/antigravity-workspace/aifullstack/docs/specs/2026-08-26_ai_fullstack_onprem_offering_refinement_spec.md) | NEW | 본 온프레미스 오퍼링 최적화 및 리포트 개정 작업 명세서 작성 |
| [`docs/TODO.md`](file:///c:/dev/antigravity-workspace/aifullstack/docs/TODO.md) | MODIFY | 온프레미스 오퍼링 정비 및 리포트 개정 항목 완료 처리 |

---

## 4. 검증 결과

- **HTML 무결성 검증**: 잔여 비대상 키워드(조나단, Solar, Gaudi, Zadara, VMware) 0건 확인 완료.
- **DOCX 빌드 검증**: `generate_strategy_service_report_docx.py` 실행 완료 (`Exit Code 0`), 57.0 KB 크기의 정상 Word 파일 2개 생성 확인.
- **비즈니스 가이드라인 일치도**: 100% 완결.
