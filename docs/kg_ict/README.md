# KGM 자동차 모델별 BOM 인텔리전스 챗봇 구축 사업제안

> **제안 대상:** KG ICT (KGM 모빌리티 IT 담당)  
> **제안사:** 메가존클라우드(주) (MegazoneCloud)  
> **작성일자:** 2026년 11월  
> **수행기간:** 총 4개월 (16주)  

---

## 📌 프로젝트 개요 (Executive Summary)

본 프로젝트는 과거 **현대자동차 남양연구소**와 성공적으로 완수한 *'자동차 모델별 BOM 확인 및 검색 챗봇 PoC'*의 도메인 지식과 노하우를 계승하고, 2026년 최신 AI 기술 패러다임(**Text-to-SQL 탈피**, **자가수정 Code-Interpreter 에이전트**, **RHOSAI 기반 On-Prem/Public 하이브리드 지원**, **Nota.ai 경량화 Qwen & SGLang 초고속 서빙**, **DuckDB + Kùzu 듀얼 임베디드 데이터 레이어**)을 적용하여 KGM 모빌리티와 KG ICT에 최적화된 차세대 사내 Private BOM 인텔리전스 시스템을 제안합니다.

---

## 🚀 과거 현대차 PoC 대비 핵심 차별화 포인트

| 비교 항목 | 과거 현대차 남양연구소 PoC (2024) | KGM 차세대 BOM 인텔리전스 (2026 제안) |
| :--- | :--- | :--- |
| **핵심 아키텍처** | **전통적 Text-to-SQL + Milvus RAG** | **Sandbox Code-Interpreter 에이전트 + Self-Correction** |
| **추론 방식** | 번역 → 5개 Intent 고정 분류 → SQL 단발 생성 | 자율 계획(ReAct) → Python/DuckDB/Kùzu 코드 생성·실행·검증 |
| **기본 인프라** | IBM watsonx, OCP 클라우드 등 특정 외산 솔루션 단독 종속 | **RHOSAI (Red Hat OpenShift AI) 기반**<br>(On-Premise 및 Public Cloud 유연 배포) |
| **엔진 스택** | Presto / Trino 분산 쿼리 엔진 | **DuckDB (임베디드 OLAP) + Kùzu (임베디드 Graph DB)** |
| **적용 모델** | Llama-3.1-8B, SQLCoder-7B 결합 | **Nota.ai 최적화 경량 Qwen2.5-Coder (NetsPresso® 압축)** |
| **서빙 솔루션** | watsonx.ai 독점 서빙 스택 | **SGLang / vLLM / llama-server 초경량 고속 추론 엔진** |
| **인터페이스** | 단순 텍스트 Chatbot API 호출 | **음성 검색 (Whisper STT) + 계층적 드릴다운 트리 UI** |
| **데이터 준비성** | 사전 정제 데이터셋 활용 (특수 환경) | **상호 데이터 스키마 정의 및 도메인 용어 정제 단계 내재화** |
| **답변 정확도** | 복합 질의 59% (평균 72%) | **복합 사양 비교 및 다중 집계 90% 이상 정합성 확보** |

---

## ⚡ 모델 및 서빙 혁신: Nota.ai 경량화 & SGLang / vLLM

1. **Nota.ai NetsPresso® 기반 경량 Qwen2.5-Coder**:
   - 구조적 프루닝(Pruning), INT4/FP8 정밀 양자화, 지식 증류를 통해 GPU VRAM 사용량을 40~50% 대폭 절감.
   - RTX PRO 6000 듀얼 환경에서 동시 접속 처리량 2배 이상 확대 및 95%+ 코딩 정합성 유지.
2. **Ollama를 넘어서는 초경량 고속 서빙 솔루션**:
   - **SGLang (최우선 추천)**: RadixAttention 기반 KV 캐시 재사용으로 다단계 코딩 에이전트 지연시간 70% 단축 및 초당 토큰 처리량(TPS) 1.5~2배 향상.
   - **vLLM**: RHOSAI / KServe 공식 네이티브 연동을 통한 엔터프라이즈 운영 안정성 보장.
   - **llama-server (llama.cpp)**: C/C++ 기반 제로 디펜던시 초경량 바이너리로 극소 메모리 풋프린트 제공.

---

## 🧩 데이터 엔진 혁신: DuckDB + Kùzu (임베디드 Graph DB) 듀얼 아키텍처

- **DuckDB (임베디드 OLAP)**: 컬럼 기반 벡터화 연산으로 수백만 건 BOM 데이터를 수 밀리초 내 집계 및 사양 간 차이점(Diff) 계산.
- **Kùzu (임베디드 Graph DB)**: C++ 기반 초경량 인프로세스 그래프 DB. OpenCypher 쿼리로 모듈-어셈블리-단품 간 다계층 트리 순회 및 부품 공용화/대체 경로 초고속 탐색.
- **Apache Arrow 메모리 제로카피 공유**: Kùzu의 그래프 순회 결과와 DuckDB의 수치 테이블을 단일 프로세스에서 제로카피로 결합하여 초고속 질의 완결.

---

## 🎙 멀티모달 인터페이스: Voice-to-BOM & 계층적 드릴다운 트리 UI

1. **음성 검색 (Voice-to-BOM / Whisper 온프렘 STT)**:
   - 연구실이나 공장 현장에서 핸즈프리로 음성 질의 시 실시간 부품 검색 및 멀티모달 응답 제공.
2. **계층적 드릴다운 트리 인터페이스 (Drill-down Navigator)**:
   - 완성차 ➔ 시스템 ➔ 모듈 ➔ 서브어셈블리 ➔ 단품 파트로 이어지는 자동차 BOM 구조를 시각적 트리 다이어그램으로 제공.
   - 대화형 챗봇에서 모듈 클릭 시 하위 부품 트리가 동적으로 펼쳐지며 대화와 클릭을 결합한 직관적 탐색 지원.

---

## ⏱ 추진 일정 및 WBS (총 4개월 / 16주)

- **1개월차 (W1 ~ W4)**: 상호 데이터 스키마 정의 및 정제, RHOSAI 셋업, RTX 6000 Ada x 2 서버 구축
- **2개월차 (W5 ~ W8)**: 차종·사양 메타데이터 구축, KGM 도메인 용어사전 정제, DuckDB + Kùzu 그래프 파이프라인 연계
- **3개월차 (W9 ~ W12)**: Coding Agent 코어 개발, Docker 격리 샌드박스, Self-Correction 엔진 및 음성 STT / 계층 트리 UI 개발
- **4개월차 (W13 ~ W16)**: 현업 시나리오 100선 E2E 성능 평가(정합성 90%+), 비공개 파일럿(CBT), 운영자 매뉴얼 교육 및 정식 오픈

---

## 👥 구축 옵션 및 전문 인력 투입 계획 (총 4개월 / 20.0 M/M)

| 구분 | Option A (온프렘 전용 GPU 서버 도입 포함) | Option B (기보유 인프라 / 클라우드 활용) | 비고 |
| :--- | :---: | :---: | :--- |
| **하드웨어 인프라** | **NVIDIA RTX PRO 6000 (48GB x 2EA) 2U 랙 서버 1식 구축** | **기보유 GPU 서버 또는 퍼블릭 클라우드 활용** | Option A 선택 시 3년 온사이트 무상 유지보수 보증 포함 |
| **전문 인력 투입 (SW 구축)** | **총 20.0 M/M (4개월 / 16주 전담 투입)** | **총 20.0 M/M (4개월 / 16주 전담 투입)** | 5대 핵심 직무 전문 엔지니어링 팀 투입 |
| **플랫폼 및 SW 라이선스** | **오픈소스 / RHOSAI 표준 스택 기반** | **오픈소스 / RHOSAI 표준 스택 기반** | 특정 외산 독점 솔루션 종속 탈피 및 라이선스 부담 제로화 |

### 전문 인력 투입 공수 내역 (총 4개월 / 20.0 M/M)
- **PM / AI 아키텍트 (특급, 3.0 M/M)**: 프로젝트 총괄, 아키텍처 설계, 현대차 PoC 노하우 이식
- **Lead Coding Agent 엔지니어 (고급, 4.0 M/M)**: ReAct 에이전트, 샌드박스 인터프리터, Self-Correction 로직 구현
- **온프렘/클라우드 LLM 엔지니어 (고급, 4.0 M/M)**: RHOSAI/SGLang 서빙 최적화, Nota.ai 경량 모델 양자화 및 프롬프트 튜닝
- **BOM 데이터 / 그래프 엔지니어 (중급, 5.0 M/M)**: KGM BOM 스키마 분석, DuckDB/Kùzu 파이프라인 및 Continuous RAG 연계
- **UI/UX 개발 & 음성/QA 엔지니어 (중급, 4.0 M/M)**: 계층 트리 UI, Whisper 음성 연동, 100선 E2E 성능 검증

---

## 📖 전체 핵심 용어집 (Glossary)

| 용어 (Term) | 영문 / 분류 | 핵심 정의 및 본 사업에서의 역할 |
| :--- | :--- | :--- |
| **BOM / EBOM / MBOM** | Bill of Materials | 자동차 한 대를 구성하는 전체 부품의 계층 관계 데이터베이스 (설계/생산 기준). |
| **RHOSAI** | Red Hat OpenShift AI | 쿠버네티스 기반 엔터프라이즈 오픈 AI 플랫폼. On-Premise와 Public Cloud 간 일관성을 보장하는 핵심 스택. |
| **Nota.ai (NetsPresso)** | 모델 압축/경량화 플랫폼 | 구조적 프루닝, INT4/FP8 양자화를 통해 Qwen 모델 크기를 50% 절감하고 속도 극대화. |
| **SGLang** | 초고속 추론 서빙 엔진 | RadixAttention 기반 캐시 재사용으로 다단계 코딩 에이전트 지연을 70% 단축하는 서빙 엔진. |
| **llama-server** | 초경량 추론 바이너리 | C/C++ 기반 제로 디펜던시 초경량 서빙 바이너리로 극소 메모리 풋프린트 제공. |
| **DuckDB** | 임베디드 OLAP DB | 프로세스 내장형 컬럼 DB. 파이썬과 제로카피 연동되어 수백만 건 BOM을 수 밀리초 내 집계·Diff 연산. |
| **Kùzu** | 임베디드 Graph DB | C++ 기반 초경량 인프로세스 그래프 DB. BOM 계층 트리 순회 및 부품 종속성 경로 탐색에 최적화. |
| **Code-Interpreter Agent** | 에이전트 아키텍처 | LLM이 Python/DuckDB/Kùzu 코드를 직접 작성하고 격리 샌드박스에서 실행하여 답변을 도출하는 에이전트. |
| **Self-Correction Loop** | 자가 수정 루프 | 코드 실행 에러나 빈 결과 발생 시 에이전트가 자체 디버깅·재실행하여 정합성 90%+ 보장. |
| **Voice-to-BOM** | 음성 검색 인터페이스 | 연구원/현장 실무자가 마이크 음성 질의 시 온프렘 Whisper STT를 통해 즉시 부품 검색 수행. |
| **Drill-down Tree UI** | 계층적 드릴다운 트리 UI | 완성차부터 단품 부품까지 이어지는 BOM 계층 트리를 시각적으로 펼쳐가며 대화·클릭 결합 탐색. |
| **Data Readiness** | 상호 데이터 준비성 | AI 착수 전 원천 BOM 스키마 정의, 부품 코드 표준화, 테이블 정제를 수행하는 필수 선행 작업 단계. |

---

## 📁 파일 구성 안내

- 📄 **[KG_ICT_BOM_AI_Proposal.docx](./KG_ICT_BOM_AI_Proposal.docx)**: 상세 사업제안서 보고서 (Word 문서)
- 📊 **[KG_ICT_BOM_AI_Proposal.pptx](./KG_ICT_BOM_AI_Proposal.pptx)**: 발표 및 경영진 보고용 슬라이드 덱 (PowerPoint 16:9)
- 🌐 **[KG_ICT_BOM_AI_Proposal.html](./KG_ICT_BOM_AI_Proposal.html)**: 브라우저에서 바로 열람 가능한 반응형 인터랙티브 웹 리포트
- 📝 **[KG_ICT_BOM_AI_Proposal.md](./KG_ICT_BOM_AI_Proposal.md)**: 사업제안서 마크다운 원본 전문

---

## 📞 문의 및 제안사 정보

- **제안사**: 메가존클라우드(주) (MegazoneCloud)
- **문의**: 메가존클라우드 모빌리티/AI 아키텍처 사업본부
