# MZC ISSU AI Full Stack 온프레미스 오퍼링 최적화 및 전략 보고서 개정 핸드오버 문서

**문서 번호**: HANDOVER-2026-08-26-001  
**작성 일자**: 2026년 8월 26일  
**작성 부서**: MEGAZONECLOUD Integrated Solution Sales Unit (ISSU) / AI Full Stack CoE  
**인수인계 대상**: 차기 프로젝트 담당자, 솔루션 아키텍트, 영업 및 마케팅 본부  
**관련 저장소**: `aifullstack` (Corpus: `kesperinc/aifullstack_issu`)  

---

## 1. 개요 및 목적 (Executive Summary)

본 문서는 2026년 8월 26일 자로 완료된 **MEGAZONECLOUD AI Full Stack 전략 서비스 보고서 개정, 온프레미스(On-Premise) 및 소버린(Sovereign) 중심 솔루션 포트폴리오 최적화, Articul8 AI 10대 산업 Use Case 카탈로그 신설, 그리고 로컬 오프라인 다운로드 100% 상대 경로 지원** 작업에 대한 최종 핸드오버(인수인계) 문서입니다.

단일 벤더 종속을 탈피한 **모듈형 소버린 플랫폼(Vendor-Agnostic Modular)** 표준을 확립하고, 고객이 온프레미스 환경에서 즉시 도입 가능한 4대 비즈니스 솔루션 패키지와 TCO 가이드를 완비하였습니다.

---

## 2. 주요 작업 및 개정 완료 내역

### 2.1 4-Layer 엔터프라이즈 AI Full Stack 생태계 정비
* **Layer 04 (Solution Layer)**:
  * 최상위 산업 도메인 인텔리전스에 집중하여 **`Articul8 AI (A8)`**, **`Cohere`** 2대 엔터프라이즈 소버린 플랫폼으로 단일화.
* **Layer 03 (Model + Tool Layer)**:
  * 중복성 및 경쟁력 검토를 통해 DataRobot(RHOAI MLOps와 중복) 및 Anaconda Enterprise(GitLab/RHOAI와 중복)를 제외하고, **정예 10대 솔루션 라인업 확정**:
  1. `vLLM` (PagedAttention 오픈소스 표준 고속 추론 엔진)
  2. `LiteLLM` (100+ LLM 단일 규격 라우팅 게이트웨이)
  3. `sLLM` (Qwen2.5-Coder, Llama 3.3 사내 경량 언어 모델)
  4. `vLM` (Qwen2-VL, Llama-Vision 멀티모달 비전 언어 모델 - 신규 추가)
  5. `MCP` (Model Context Protocol 기반 사내 코딩 에이전트)
  6. `GitLab` (사내 소스코드 관리 및 DevSecOps/CI-CD 표준 - 명칭 일원화)
  7. `MinIO` (고성능 S3 호환 AI 오브젝트 스토리지)
  8. `Redis Enterprise` (초저지연 인메모리 시맨틱 캐시 & 벡터)
  9. `Confluent` (엔터프라이즈 실시간 Kafka 스트리밍)
  10. `Dynatrace` (Dynatrace Managed 완전 폐쇄망 AIOps & Davis AI RCA)
* **Layer 02 (OS + Virtualization Layer)**:
  * `Red Hat OpenShift / RHOAI SNO`, `Nutanix NCI + Nutanix NKP (K8s Platform)` 표준화.
* **Layer 01 (H/W Layer)**:
  * `Dell PowerEdge 서버`, `NVIDIA GPU (B200/300, H100/200, L40S, RTX 6000 Ada/Blackwell)`, `리벨리온, 퓨리오사AI`, `Dell PowerScale 스토리지 (DGX SuperPOD 인증) / 400GbE RoCEv2, InfiniBand` 확정 (**Pure Storage 삭제**).

### 2.2 표준 사이징 및 TCO 가이드라인 정립 (Section 05)
* **H/W 장비비와 S/W 솔루션 TCO 분리**:
  * **Small (~50인)**: H/W 약 4,500만~6,000만 원 (Dell R760 2-GPU/NPU) / S/W 약 5,000만~6,000만 원 (1억 미만 턴키)
  * **Medium (100~300인)**: H/W 약 1.5억~2.2억 원 (Dell R760xa 4-GPU) / S/W 약 1.8억~2.5억 원
  * **Large (500인+)**: H/W 약 6억~10억+ 원 (Dell XE9680 8-GPU + PowerScale) / S/W 약 3.5억~5.5억+ 원
* **비용 안내 가이드라인 명시**: "TCO 및 라이선스는 S/W 기준이며, H/W 장비 가격은 조달 사양별 별도 견적 제공"

### 2.3 4대 핵심 비즈니스 솔루션 패키지 및 Articul8 3대 Use Case (Section 07)
* **Package 01**: **엔터프라이즈 사내 코딩 에이전트 & DevOps 패키지** (GitLab + MCP Server + Qwen2.5-Coder + vLLM)
* **Package 02**: **Articul8 AI 산업 도메인 특화 지식 패키지** (제조·항공MRO vs 금융 도메인 분기, 건설 패키지 배제)
* **Package 03**: **온프레미스 문서 & 데이터 인텔리전스 파이프라인 (Data RAG)** (MinIO + Cohere + Redis Enterprise)
* **Package 04**: **온프레미스 소버린 AI 팩토리 & PoC 랜딩 패키지** (Dell PowerEdge + PowerScale + Nutanix AHV/OpenShift + NVIDIA NIM)
* **Articul8 3대 Use Case**:
  * Use Case 01 [제조·스마트팩토리]: 설비 이상 감지 및 자율 예지보전 AI (비계획 다운타임 40% 감축)
  * Use Case 04 [항공우주·방산]: MRO 프로세스 인텔리전스 & 정밀 정비 AI (매뉴얼 해석 정확도 92%)
  * Use Case 10 [금융·투자]: 금융 서비스 리서치 & 여신/공시 심사 AI (실사 수 주 ➔ 수 분 단축)

### 2.4 부록(Appendix) 핵심 솔루션 평가 매트릭스 전면 개편
* 중복 헤더 태그 완전 제거 및 정돈.
* **Layer 04 핵심 솔루션 특징 및 적용 분야 테이블 신설** (Articul8, Cohere).
* **Layer 03 4개 하위 분야 평가 매트릭스 최신화** (추론·라우팅 / 모델·개발생산성 / 데이터스토리지·스트리밍 / AIOps).

### 2.5 Articul8 AI 10대 산업 Use Case 전용 웹 카탈로그 구축
* 신규 카탈로그 구축: [`offering/articul8_ai_usecase_catalog.html`](file:///c:/dev/antigravity-workspace/aifullstack/offering/articul8_ai_usecase_catalog.html)
* **12종 원본 프레젠테이션 다운로드 연동**:
  1. `Articul8_AI_기술자료집_v1.0(한화시스템).pptx` (7.1 MB)
  2. `Articul8_AI_기술자료집_v1.1(한화시스템).pptx` (최신판, 8.5 MB)
  3. `UseCase1_PredictiveMaintenance_1.pptx` (제조 예지보전)
  4. `UseCase2_DigitalTwin_reformatted.pptx` (디지털 트윈)
  5. `UseCase3_WarrantyClaims_reformatted.pptx` (보증 클레임)
  6. `UseCase4_MRO_Aerospace_reformatted.pptx` (항공우주 MRO)
  7. `UseCase5_NetworkDataAnalysis_reformatted.pptx` (통신 네트워크 분석)
  8. `UseCase6_CyberSecurity_reformatted.pptx` (사이버 보안)
  9. `UseCase7_ConstructionAssetMgmt_reformatted.pptx` (건설 자산 관리)
  10. `UseCase8_ProactiveGridAwareness_reformatted.pptx` (스마트 그리드)
  11. `UseCase9_MarketingCompliance_reformatted.pptx` (마케팅 규제 준수)
  12. `UseCase10_FinancialServices_reformatted.pptx` (금융 서비스 리서치)
* 마스터 포털 [`offering/index.html`](file:///c:/dev/antigravity-workspace/aifullstack/offering/index.html) 최상단 오늘 일자(`2026-08-26`) 릴리스 카드 등록 완료.

### 2.6 로컬 오프라인 다운로드용 상대 경로(Relative Path) 100% 무결성 검증
* `offering/` 폴더 내 **전체 24개 HTML 파일의 모든 내부 링크 및 다운로드 버튼을 100% 상대 경로로 설정 및 전수 검사 완료** (`0 Missing, 0 Absolute file:///`).
* 사용자가 폴더를 로컬 PC로 다운로드하여 더블 클릭 시, 외부 웹 서버 없이도 완벽한 탐색 및 파일 다운로드가 동작합니다.

---

## 3. 핵심 산출물 맵 (Deliverables Map)

| 구분 | 파일 경로 | 주요 내용 및 특징 |
| :--- | :--- | :--- |
| **마스터 오퍼링 허브** | [`offering/index.html`](file:///c:/dev/antigravity-workspace/aifullstack/offering/index.html) | 최신 릴리스 타임라인(2026-08-26) 및 전략보고서/Articul8 카탈로그 카드 허브 |
| **전략 보고서 (Web)** | [`offering/mzc_ai_fullstack_strategy_service_report.html`](file:///c:/dev/antigravity-workspace/aifullstack/offering/mzc_ai_fullstack_strategy_service_report.html) | 4-Layer, 글로벌 비교, 사이징 TCO, 4대 패키지, 부록 평가 매트릭스 수록 웹 |
| **전략 보고서 (Word)** | [`offering/docx/2026-08-20_MZC_AI_Fullstack_Strategy_Service_Report.docx`](file:///c:/dev/antigravity-workspace/aifullstack/offering/docx/2026-08-20_MZC_AI_Fullstack_Strategy_Service_Report.docx)<br>[`docs/2026-08-20_MZC_AI_Fullstack_Strategy_Service_Report.docx`](file:///c:/dev/antigravity-workspace/aifullstack/docs/2026-08-20_MZC_AI_Fullstack_Strategy_Service_Report.docx) | 최신 온프레미스 오퍼링 반영 공식 경영진 제출용 Word 산출물 (56.7 KB) |
| **Articul8 카탈로그** | [`offering/articul8_ai_usecase_catalog.html`](file:///c:/dev/antigravity-workspace/aifullstack/offering/articul8_ai_usecase_catalog.html) | 한화시스템 기술자료집 2종 및 10대 산업 Use Case PPTX 즉시 다운로드 카탈로그 |
| **DOCX 자동 빌더** | [`offering/generate_strategy_service_report_docx.py`](file:///c:/dev/antigravity-workspace/aifullstack/offering/generate_strategy_service_report_docx.py) | Python-docx 기반 전략 보고서 Word 자동 생성 및 배포 스크립트 |
| **개정 상세 명세서** | [`docs/specs/2026-08-26_ai_fullstack_onprem_offering_refinement_spec.md`](file:///c:/dev/antigravity-workspace/aifullstack/docs/specs/2026-08-26_ai_fullstack_onprem_offering_refinement_spec.md) | 변경 전/후 비교표 및 세부 엔지니어링 명세 기록 |
| **작업 관리 현황판** | [`docs/TODO.md`](file:///c:/dev/antigravity-workspace/aifullstack/docs/TODO.md) / [`TODO.md`](file:///c:/dev/antigravity-workspace/aifullstack/TODO.md) | 전체 프로젝트 로드맵 및 최신 작업 완료 상태 트래킹 |

---

## 4. 운영 및 유지보수 가이드 (Maintenance Guide)

1. **Word(DOCX) 보고서 재생성 방법**:
   ```powershell
   # 가상환경 활성화 상태에서 실행
   .venv\Scripts\python offering/generate_strategy_service_report_docx.py
   ```
   * 실행 시 `offering/docx/` 및 `docs/` 경로에 2개의 대칭 Word 파일이 자동 동기화 생성됩니다.
2. **자료 추가 시 상대 경로 유지 수칙**:
   * 신규 HTML 작성 시 `file:///c:/...` 형태의 절대 경로를 사용하지 않고 `index.html`, `docx/...`, `articul8 usecases/...` 형태의 상대 경로를 유지해야 합니다.
3. **규칙 및 명명 수칙 준수**:
   * 본 프로젝트는 `AGENTS.md`의 16개 필수 가드레일을 준수하며, 신규 생성 문서는 항상 `YYYY-MM-DD_` 접두사를 의무 적용합니다.

---

**인수인계 완료 확인자**: MEGAZONECLOUD ISSU 전략기획팀 / AI Full Stack CoE
