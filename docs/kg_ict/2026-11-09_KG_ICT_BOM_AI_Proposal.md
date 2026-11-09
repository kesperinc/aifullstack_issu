# [사업제안서] 차세대 온프레미스/하이브리드 Coding Agent 기반 KGM 자동차 모델별 BOM 인텔리전스 챗봇 구축

**제안 대상**: KG ICT (KGM 모빌리티 IT 담당)  
**제안사**: 메가존클라우드 (MegazoneCloud)  
**작성일자**: 2026년 11월  
**수행기간**: 총 4개월 (16주)  

---

## 1. 제안 배경 및 필요성

### 1.1 KGM BOM(Bill of Materials) 업무의 현주소 및 과제
- **복잡한 차종·사양 체계**: 토레스(EVX/하이브리드/가솔린), 렉스턴(뉴 아레나/스포츠 칸), 액티언, 코란도, 티볼리 등 KGM 라인업 확대에 따라 차종·트림·엔진·구동방식별 수십만 개 부품 BOM 데이터의 복잡도 급증.
- **연구개발(R&D) 및 현업의 정보 탐색 병목**:
  - 연구원, 설계자, 상품기획, 원가기획 부서에서 과거 차종 사양 비교, 부품 공용화 여부 확인, 특정 옵션 조합별 부품 번호 확인 시 레거시 시스템(PLM/ERP)의 복잡한 화면과 파편화된 테이블 구조로 인해 탐색에 과도한 시간(건당 20~30분 이상) 소모.
  - IT 부서(KG ICT)로의 비정형 데이터 추출 및 Ad-hoc 쿼리 요청이 집중되어 업무 부하 가중.
- **데이터 준비 및 정제 단계의 필수성**:
  - 과거 타사 프로젝트의 경우 사전에 데이터셋이 이미 정제되어 있던 특수 케이스였습니다. 실무 프로덕션 적용을 위해서는 **KGM 현업과 IT(KG ICT) 간의 상호 데이터 스키마 정의, 부품 코드 표준화, 레거시 정합성 검증 등 체계적인 데이터 준비(Data Readiness) 단계가 필수적으로 선행**되어야 합니다.
- **On-Premise 및 Public Cloud 유연성 요구**:
  - 차량 설계 사양 및 BOM 정보의 보안 수준에 따라 고객사(KGM/KG ICT)가 사내 전산실 내 완전 격리형 **On-Premise**를 선택하거나, 유연한 확장을 위한 **Public Cloud**를 채택할 수 있습니다. 따라서 특정 인프라나 상용 벤더에 종속되지 않고 양쪽 환경을 모두 수용할 수 있는 하이브리드 아키텍처가 필수적입니다.

### 1.2 과거 현대자동차 남양연구소 BOM 챗봇 PoC 경험과 시사점
본 제안사는 현대자동차 남양연구소와 함께 수행한 **'자동차 모델별 BOM 확인 및 검색 챗봇 PoC'** 레퍼런스를 보유하고 있습니다.

| 구분 | 과거 현대자동차 남양연구소 PoC (2024) | 본 제안: KGM 차세대 BOM 인텔리전스 (2026) |
| :--- | :--- | :--- |
| **핵심 아키텍처** | **전통적 Text-to-SQL + Milvus RAG** | **Sandbox Code-Interpreter 에이전트 + Self-Correction** |
| **추론 방식** | 번역 → 고정 Intent(5종) 분류 → 템플릿/SQLCoder SQL 생성 | 자율 계획(ReAct) → Python/DuckDB/Kùzu 코드 생성·실행·검증 |
| **기본 인프라 기반** | IBM watsonx, OCP 클라우드 등 고비용 특정 외산 솔루션 | **RHOSAI (Red Hat OpenShift AI) 기반**<br>(On-Premise 및 Public Cloud 유연 배포 지원) |
| **엔진 스택** | Presto / Trino 분산 쿼리 엔진 | **DuckDB (임베디드 OLAP) + Kùzu (임베디드 Graph DB)** |
| **적용 모델** | Llama-3.1-8B, SQLCoder-7B (단순 프롬프트 결합) | **Nota.ai 최적화 경량 Qwen2.5-Coder (NetsPresso® 압축)** |
| **서빙 솔루션** | watsonx.ai 독점 서빙 스택 | **SGLang / vLLM / llama-server 초경량 고속 추론 엔진** |
| **인터페이스** | 단순 텍스트 Chatbot API 호출 | **음성 검색 (Whisper STT) + 계층적 드릴다운 트리 UI** |
| **정확도 수준** | 단순 질의 89%, 고난이도 복합 질의 59% (평균 72%) | **복합 조인·비교 연산 포함 90% 이상의 엔터프라이즈 정합성 확보** |
| **데이터 준비성** | 사전 정제 데이터셋 활용 | **상호 데이터 스키마 정의 및 도메인 용어 정제 단계 내재화** |

---

## 2. 엔드투엔드 시스템 아키텍처 및 상세 프로세스 설계

본 장에서는 사용자의 음성/텍스트 질의가 유입되어 최종 답변과 계층 트리 UI로 반환되기까지의 **6단계 엔드투엔드 처리 흐름**과, 이를 뒷받침하는 **5대 기능 블록 및 인프라 인스턴스 연동 구조**, 그리고 **원천 BOM DB 동기화 및 지속적 RAG 현행화 파이프라인**을 상세히 정의합니다.

### 2.1 6단계 엔드투엔드 질의-응답 처리 프로세스 흐름도

```mermaid
flowchart TD
    subgraph Step1 ["Step 1. 사용자 쿼리 유입"]
        UQ1[마이크 음성 질의\n'Voice-to-BOM'] --> STT[온프렘 Whisper STT]
        UQ2[사내 웹 포털 텍스트 질의] --> GW
        STT --> GW[API Gateway / Chatbot Backend]
    end

    subgraph Step2 ["Step 2. 의미해석 LLM (Semantic Parser)"]
        GW --> FastCache{시맨틱 캐시 확인\n(FAQ / 빈출 질의?)}
        FastCache -->|Hit: 즉시 반환| OutDirect([캐시 기반 즉시 응답])
        FastCache -->|Miss: 신규 질의| LLM1[의미해석 LLM\n- 의도(Intent) 분석\n- 엔티티/차종/부품코드 추출\n- 질의 경로(Diff/트리/조회) 판별]
    end

    subgraph Step3 ["Step 3. 쿼리/코드 변환 LLM (Coding Specialist)"]
        LLM1 --> LLM2[쿼리/코드 변환 LLM\n(Nota.ai 경량화 Qwen2.5-Coder)\n- DuckDB용 SQL 생성\n- Kùzu용 Cypher 쿼리 생성\n- 사양 Diff 연산 Python 코드 생성]
    end

    subgraph Step4 ["Step 4. 격리 샌드박스 검색 & 계층적 BOM 탐색"]
        LLM2 --> Box[격리 샌드박스 실행 엔진\n(Docker / Podman)]
        Box <-->|OLAP 수치 집계 & Diff| D1[(DuckDB)]
        Box <-->|BOM 다계층 트리 순회| D2[(Kùzu Graph DB)]
        Box <-->|최신 차종/매뉴얼 참조| D3[(Active RAG Vector Store)]
        Box -->|런타임 오류 발생 시| SelfLoop[Self-Correction 루프\n에러 스택 기반 코드 자체 재작성]
        SelfLoop --> LLM2
    end

    subgraph Step5 ["Step 5. 답변 작성 및 포맷팅 (Synthesizer)"]
        Box -->|정상 실행 데이터프레임| Synth[답변 합성 모듈\n- 부품 비교표 렌더링\n- 사양 차이점 자연어 요약\n- Excel/CSV 파일 생성]
    end

    subgraph Step6 ["Step 6. 멀티모달 최종 사용자 응답"]
        Synth --> UI_Out[인터랙티브 응답 표출\n• 대화창 요약 텍스트\n• BOM 계층 트리 뷰 동적 하이라이트\n• TTS 음성 안내 & 원클릭 다운로드]
        UI_Out --> FB[(피드백 DB & FAQ 캐시 자동 적재)]
    end
```

---

### 2.2 5대 기능 블록 및 인프라 인스턴스 연동 아키텍처

본 시스템은 **RHOSAI (Red Hat OpenShift AI)** 쿠버네티스 환경 위에서 마이크로서비스 및 GPU 워커 노드로 유기적으로 연동 구축됩니다.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        【 Layer 1 : Presentation & Client Layer 】                     │
│  • KGM 연구원/현업 사내 웹 포털 (React 대화형 챗 UI & Excel 다운로더)                   │
│  • 온프렘 음성 모듈 (Whisper STT 음성 인식 & Piper/FastSpeech TTS 음성 출력)            │
│  • BOM 계층적 드릴다운 트리 뷰어 (D3.js / SVG 기반 부품 어셈블리 네비게이터)            │
└───────────────────────────────────────────┬────────────────────────────────────────────┘
                                            │ (REST API / WebSocket / gRPC)
┌───────────────────────────────────────────▼────────────────────────────────────────────┐
│              【 Layer 2 : Gateway & Orchestration Layer (RHOSAI CPU Pods) 】           │
│  • API Gateway & Session Manager (FastAPI, 사내 SSO/권한 연계)                        │
│  • Orchestration Controller (LangGraph 기반 ReAct 다단계 플래너)                        │
│  • High-Frequency FAQ Semantic Cache (자주 묻는 질문 즉시 반환 인메모리 캐시)           │
└───────────────────────────────────────────┬────────────────────────────────────────────┘
                                            │ (High-Speed NVLink / IPC)
┌───────────────────────────────────────────▼────────────────────────────────────────────┐
│           【 Layer 3 : Cognitive & Serving Layer (RHOSAI GPU Worker Nodes) 】          │
│  • 인프라: NVIDIA RTX PRO 6000 Ada (48GB x 2EA, 총 96GB VRAM)                          │
│  • 추론 서빙 엔진: SGLang (RadixAttention 고속 캐싱) / vLLM (PagedAttention)           │
│  • 탑재 모델:                                                                          │
│    ① Semantic Parser LLM (의미해석 및 KGM 부품 용어 매핑)                             │
│    ② Coding Specialist LLM (Nota.ai NetsPresso® 최적화 Qwen2.5-Coder 32B)             │
└───────────────────────────────────────────┬────────────────────────────────────────────┘
                                            │ (IPC / Shared Memory)
┌───────────────────────────────────────────▼────────────────────────────────────────────┐
│      【 Layer 4 : Execution & Dual Embedded Data Layer (Sandbox Runtime) 】            │
│  • Isolated Docker / Podman Sandbox (보안 격리된 코드 실행 환경)                       │
│  • DuckDB (In-Process OLAP): 부품 수치 집계, 트림 간 사양 차이(Diff) 고속 연산        │
│  • Kùzu (In-Process Graph DB): 완성차-모듈-단품 간 다계층 트리 순회, 대체품 경로 탐색 │
│  • Apache Arrow Zero-Copy: DuckDB와 Kùzu 간 메모리 복사 없는 초고속 파이프라인 결합   │
└───────────────────────────────────────────┬────────────────────────────────────────────┘
                                            │ (Data Sync & Replication)
┌───────────────────────────────────────────▼────────────────────────────────────────────┐
│          【 Layer 5 : Data Integration & Continuous RAG Layer (원천 연동) 】           │
│  • 원천 시스템: KGM 레거시 PLM (Windchill), ERP (SAP), BOM 원천 RDB (Oracle/MSSQL)     │
│  • 데이터 동기화 엔진: Read Replica 복제 및 CDC / 배치 파이프라인 (Airflow)            │
│  • Active Knowledge Vector Store: 최신 출시 차종 정보, 신규 부품 변경점, 피드백 DB     │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

### 2.3 원천 BOM DB 연동 및 지속적 RAG 현행화(Continuous RAG) 설계

부품 데이터는 매주/매월 설계 변경(ECO/EO) 및 신규 연식 변경에 따라 지속적으로 업데이트되므로, 시스템이 최신 상태를 스스로 유지하도록 설계합니다.

```mermaid
flowchart LR
    subgraph SourceSystems ["KGM 원천 시스템"]
        PLM[(레거시 PLM\n설계 부품)]
        ERP[(ERP 시스템\n원가/재고)]
        BOM_DB[(BOM 원천 DB\nOracle/MSSQL)]
    end

    subgraph SyncPipeline ["데이터 연동 & 동기화 파이프라인"]
        CDC[변경 감지 CDC / \nAirflow 주기적 배치]
        PreProc[스키마 정규화 &\n부품 용어사전 매핑]
    end

    subgraph LocalDataLayer ["사내 로컬 분석 레이어 (RHOSAI)"]
        Replica[(읽기 전용 복제본\nDuckDB / Parquet)]
        GraphData[(Kùzu Graph DB\n계층 관계 인덱스)]
        ActiveRAG[(Active RAG\n최신 차종 / FAQ)]
    end

    PLM & ERP & BOM_DB --> CDC
    CDC --> PreProc
    PreProc -->|수치/테이블 적재| Replica
    PreProc -->|부품 계층 트리 갱신| GraphData
    PreProc -->|신규 차종·옵션 임베딩| ActiveRAG
```

1. **원천 BOM DB 무부하 연동 (Read-Only Replica & CDC)**:
   - 본 챗봇 시스템은 KGM 운영계(PLM/ERP) DB에 부하를 주지 않기 위해 **읽기 전용 복제본(Read Replica)** 또는 Parquet 파일 스냅샷을 주기적으로(예: 매일 자정 또는 실시간 CDC) 동기화합니다.
2. **자주 질문하는 내용(FAQ)의 시맨틱 캐싱**:
   - 현업 연구원들이 반복적으로 묻는 주요 질문(예: *"토레스 하이브리드 엔진오일 규격 및 필터 품번"*, *"렉스턴 4WD 트랜스퍼 케이스 적용 부품"*)은 질문-답변 페어로 시맨틱 캐시(Semantic Cache)에 저장되어, **LLM 재추론 없이 0.1초 내 즉시 응답**하여 GPU 리소스를 대폭 절약합니다.
3. **최신 출시 차종 및 설계 변경점의 Active Knowledge RAG 현행화**:
   - 신규 차종(예: 액티언 최신 연식, 신규 전기차 등)이나 신규 옵션 패키지가 등록되면, 배치 파이프라인이 메타데이터와 사양 설명서를 자동으로 벡터화하여 **Active RAG Vector Store**에 즉각 반영합니다.
4. **피드백 DB 기반 지속적 모델 튜닝**:
   - 현대차 PoC에서 검증된 피드백 DB 체계를 계승하여, 현업의 '좋아요/정정' 피드백을 축적하고 이를 Dynamic Few-shot 프롬프트와 향후 경량 모델 파인튜닝 데이터셋으로 재활용합니다.

---

## 3. 모델 및 서빙 혁신: Nota.ai 경량화 Qwen 모델 & 초경량 고속 서빙 엔진

### 3.1 Nota.ai 경량화 Qwen 코딩 모델 (NetsPresso® 최적화)
- **도입 배경**:
  - 자동차 BOM 및 사양 질의는 정확한 코드 생성과 지연 없는 빠른 응답 속도가 핵심입니다.
  - 본 제안에서는 AI 경량화 전문 솔루션인 **Nota.ai의 NetsPresso® 플랫폼**을 통해 구조적 프루닝(Pruning), FP8/INT4 정밀 양자화(Quantization), 지식 증류(Knowledge Distillation)를 거친 **경량 Qwen2.5-Coder 모델**을 탑재합니다.
- **성능 이점**:
  - 모델 크기와 GPU 메모리 사용량을 기존 대비 40~50% 이상 절감하면서도 코딩/추론 정합성을 95% 이상 보존.
  - NVIDIA RTX PRO 6000 Ada (48GB x 2EA) 환경에서 동시 접속자 처리량(Concurrency)을 2배 이상 확대.

### 3.2 Ollama를 넘어서는 초경량 고속 서빙 솔루션 비교 및 선정
Ollama는 간편한 로컬 실행에 적합하지만, 엔터프라이즈 환경에서의 동시 요청 처리 및 캐싱 기능에 한계가 있습니다. 이에 따라 다음의 고성능 초경량 서빙 엔진을 환경에 맞게 제공합니다:

| 솔루션 | 기술적 특징 및 장점 | KGM 사업 적용 가치 및 추천 시나리오 |
| :--- | :--- | :--- |
| **SGLang** *(최우선 추천)* | • **RadixAttention** 기술을 통한 KV 캐시 재사용 극대화<br>• 복잡한 에이전트 다단계 프롬프트 및 Tool-calling 시 지연시간 70% 단축<br>• 초당 토큰 처리량(TPS)이 vLLM 대비 1.5~2배 이상 빠름 | **복잡한 다단계 Coding Agent 실행에 최적**<br>(샌드박스 자가수정 루프 시 압도적 응답 속도 제공) |
| **vLLM** *(엔터프라이즈 표준)* | • PagedAttention 기반 메모리 파편화 제로<br>• RHOSAI / KServe와 공식 네이티브 연동<br>• 엔터프라이즈 표준 서빙 및 오토스케일링 지원 | **RHOSAI 표준 아키텍처 기반 운영 안정성 보장** |
| **llama-server (llama.cpp)** *(초경량/제로 디펜던시)* | • 순수 C/C++ 기반으로 Python 종속성 없는 초경량 바이너리<br>• 극소 메모리 풋프린트, GGUF/K-quants 정밀 양자화 지원<br>• CPU/GPU 하이브리드 오프로딩 완벽 지원 | **자원 제약 환경 또는 초경량 에지/로컬 인스턴스에 최적** |

---

## 4. 데이터 엔진 혁신: DuckDB + Kùzu (임베디드 Graph DB) 하이브리드 아키텍처

자동차 BOM 데이터는 단순한 표 형태의 집계뿐만 아니라, **부품 간의 복잡한 계층 관계(Hierarchical Tree: 모듈 ➔ 서브어셈블리 ➔ 단품)**와 **부품 공용화/대체 관계(Dependency Graph)**를 지니고 있습니다.  
따라서 본 제안에서는 **DuckDB(수치 집계 및 Diff 연산)**에 **Kùzu(임베디드 그래프 DB)**를 결합한 **듀얼 임베디드 아키텍처**를 제안합니다.

```
┌─────────────────────────────────────────────────────────────┐
│    Dual Embedded In-Memory Data Layer (Zero-Copy)           │
├──────────────────────────────┬──────────────────────────────┤
│  • DuckDB (임베디드 OLAP)     │  • Kùzu (임베디드 Graph DB)   │
│    - 컬럼 수치 집계 / 필터링 │    - BOM 계층 트리 재귀 순회 │
│    - 사양 간 차이점(Diff) 계산│    - 부품 종속성 / 대체품 경로│
├──────────────────────────────┴──────────────────────────────┤
│    ▲ Apache Arrow 메모리 제로카피(Zero-Copy) 파이프라인 결합 │
└─────────────────────────────────────────────────────────────┘
```

1. **DuckDB의 압도적 집계 속도**: 수백만 건 부품 테이블을 컬럼 기반 벡터화 연산으로 수 밀리초 내 집계·필터링하며, Python/Pandas와 Zero-copy 메모리 연동.
2. **Kùzu의 초고속 그래프 순회**: C++ 기반 인프로세스 그래프 DB로, OpenCypher 쿼리를 통해 모듈-어셈블리-단품 간 다계층 트리를 밀리초 내 순회 탐색.

---

## 5. 인터페이스 혁신: 음성 검색(Voice-to-BOM) & 계층적 드릴다운 트리 UI

1. **음성 검색 (Voice-to-BOM / Whisper 온프렘 STT)**:
   - 연구소 실험실이나 정비 현장에서 장갑을 끼고 작업 중에도 마이크 음성 질의를 통해 손쉽게 부품 정보를 호출.
   - 사내망에 배치된 경량 Whisper 모델을 통해 음성을 텍스트로 고속 변환하고 에이전트로 전달.
2. **계층적 드릴다운 트리 인터페이스 (Hierarchical Drill-down Navigator)**:
   - 완성차 ➔ 시스템(샤시/바디/전장) ➔ 메인 모듈 ➔ 서브어셈블리 ➔ 단품 파트로 이어지는 자동차 BOM 구조를 시각적 트리 다이어그램으로 제공.
   - 챗봇 답변에서 특정 모듈을 클릭하면 해당 하위 부품 트리가 동적으로 펼쳐지며, 사용자가 자연어 대화와 마우스 클릭을 혼합하여 탐색 가능.

---

## 6. 추진 일정 및 WBS (총 4개월 / 16주)

| 단계 (Phase) | 기간 | 주요 활동 및 산출물 | 마일스톤 |
| :--- | :---: | :--- | :---: |
| **1단계: 분석 및 데이터 준비** | 1개월차 (W1~W4) | 상호 데이터 스키마 정의 및 정제, RHOSAI 셋업, RTX 6000 Ada x 2 서버 구축 | 데이터 준비 및 인프라 확정 |
| **2단계: 하이브리드 데이터 파이프라인** | 2개월차 (W5~W8) | 차종·사양 메타데이터 구축, DuckDB + Kùzu 그래프 파이프라인 연계 및 CDC 연동 | BOM 메타 및 복제 파이프라인 적재 |
| **3단계: Coding Agent & 멀티모달 개발** | 3개월차 (W9~W12) | SGLang/vLLM 서빙 셋업, ReAct 에이전트, 음성 STT 및 계층 트리 UI 개발 | 샌드박스 및 멀티모달 구동 |
| **4단계: 검증 및 파일럿 이관** | 4개월차 (W13~W16) | 현업 시나리오 100선 E2E 검증(정합성 90%+), 현업 CBT, 운영자 교육 및 오픈 | 정식 서비스 오픈 |

---

## 7. 구축 옵션 비교 및 전문 인력 투입 계획 (총 4개월 / 20.0 M/M)

| 구분 | Option A (온프렘 전용 GPU 서버 도입 포함) | Option B (기보유 인프라 / 클라우드 활용) | 비고 |
| :--- | :---: | :---: | :--- |
| **하드웨어 인프라** | **NVIDIA RTX PRO 6000 (48GB x 2EA) 2U 랙 서버 1식 신규 구축** | **기보유 GPU 서버 또는 퍼블릭 클라우드 활용** | Option A 선택 시 제조사 3년 24x7 온사이트 무상 유지보수 보증 포함 |
| **전문 인력 투입 (SW 구축)** | **총 20.0 M/M (4개월 / 16주 전담 투입)** | **총 20.0 M/M (4개월 / 16주 전담 투입)** | AI 아키텍트, 코딩 에이전트, LLM 서빙, BOM/그래프 데이터, UI/QA 전문 인력 |
| **플랫폼 및 SW 라이선스** | **오픈소스 / RHOSAI 표준 스택 기반** | **오픈소스 / RHOSAI 표준 스택 기반** | 특정 외산 독점 솔루션 종속 탈피 및 연간 라이선스 부담 제로화 |
| **주요 제공 산출물** | **하드웨어 + 풀스택 에이전트 + 웹/음성/트리 UI 일체** | **풀스택 에이전트 + 웹/음성/트리 UI + 운영 매뉴얼 일체** | 고객사 인프라 환경에 맞춘 턴키 구축 및 기술 이전 |

### 7.1 전문 인력 투입 공수 세부 내역 (총 4개월 / 20.0 M/M)

| 역할 (Role) | 등급 | 투입 기간 | 투입 공수 (M/M) | 주요 담당 업무 및 핵심 산출물 |
| :--- | :---: | :---: | :---: | :--- |
| **PM / AI 아키텍트** | 특급 | 4개월 | **3.0 M/M** | 프로젝트 총괄 관리, 엔드투엔드 아키텍처 설계, 현대차 BOM PoC 노하우 이식 및 품질 보증 |
| **Lead Coding Agent 엔지니어** | 고급 | 4개월 | **4.0 M/M** | LangGraph ReAct 플래너, Docker 격리 샌드박스 인터프리터, Self-Correction 자가수정 루프 구현 |
| **온프렘/클라우드 LLM 엔지니어** | 고급 | 4개월 | **4.0 M/M** | RHOSAI 기반 SGLang/vLLM 추론 서빙 최적화, Nota.ai 경량 Qwen 모델 적용 및 프롬프트 튜닝 |
| **BOM 데이터 / 그래프 엔지니어** | 중급 | 4개월 | **5.0 M/M** | KGM 원천 BOM 스키마 정규화, DuckDB(OLAP) + Kùzu(Graph DB) 파이프라인 및 Continuous RAG 구축 |
| **UI/UX 개발 & 음성/QA 엔지니어** | 중급 | 4개월 | **4.0 M/M** | 계층적 드릴다운 트리 UI, Voice-to-BOM(Whisper STT) 연동, 현업 시나리오 100선 E2E 성능 검증 |
| **합계** | - | **4개월 (16주)** | **20.0 M/M** | **전담 엔지니어링 팀 투입을 통한 프로덕션급 BOM 인텔리전스 완성** |

---

## 8. 전체 핵심 용어집 (Glossary)

| 용어 (Term) | 영문 / 분류 | 상세 정의 및 본 사업에서의 역할 |
| :--- | :--- | :--- |
| **BOM / EBOM / MBOM** | Bill of Materials | 자동차 한 대를 구성하는 전체 부품의 계층 관계 데이터베이스 (설계/생산 기준). |
| **RHOSAI** | Red Hat OpenShift AI | 쿠버네티스 기반 엔터프라이즈 오픈 AI 플랫폼. On-Premise와 Public Cloud 간 일관성을 보장하는 핵심 스택. |
| **Nota.ai (NetsPresso®)** | AI 모델 압축/경량화 플랫폼 | 구조적 프루닝, 정밀 양자화, 지식 증류를 통해 거대 모델을 손실 없이 경량화하는 솔루션. |
| **SGLang** | SGLang (초고속 추론 서빙 엔진) | RadixAttention 기술을 통해 KV 캐시를 재사용하여 복잡한 다단계 에이전트 추론 지연을 70% 단축하는 서빙 엔진. |
| **DuckDB** | 임베디드 OLAP 데이터베이스 | 프로세스 내장형 컬럼 DB. 파이썬과 제로카피 연동되어 수백만 건 BOM을 수 밀리초 내 집계·Diff 연산. |
| **Kùzu** | 임베디드 Graph 데이터베이스 | C++ 기반 초경량 인프로세스 그래프 DB. BOM 계층 트리 순회 및 부품 종속성 경로 탐색에 최적화. |
| **Continuous RAG** | 지속적 RAG 현행화 | 원천 BOM DB 동기화 및 신규 차종, 부품 변경점, 빈출 FAQ를 주기적으로 자동 인덱싱하는 파이프라인. |
| **Semantic Cache** | 시맨틱 캐시 | 자주 묻는 질문(FAQ)의 의미적 유사도를 판별하여 LLM 재추론 없이 0.1초 내 즉각 응답을 반환하는 고속 캐시. |
| **Code-Interpreter Agent** | Code-Interpreter Agent | LLM이 Python/DuckDB/Kùzu 코드를 직접 작성하고 격리 샌드박스에서 실행하여 답변을 도출하는 에이전트. |
| **Self-Correction Loop** | 자가 수정 루프 | 코드 실행 에러나 빈 결과 발생 시 에이전트가 자체 디버깅·재실행하여 정합성 90%+ 보장. |
| **Voice-to-BOM** | 온프렘 음성 검색 인터페이스 | 연구원/현장 실무자가 마이크 음성 질의 시 온프렘 Whisper STT를 통해 즉시 부품 검색을 수행하는 기능. |
| **Drill-down Tree UI** | 계층적 드릴다운 트리 UI | 완성차부터 단품 부품까지 이어지는 BOM 계층 트리를 시각적으로 펼쳐가며 대화와 클릭을 결합 탐색하는 인터페이스. |
| **Data Readiness** | 상호 데이터 준비성 | AI 착수 전 원천 BOM 스키마 정의, 부품 코드 표준화, 테이블 정제를 수행하는 필수 선행 작업 단계. |

---

## 9. 제언 및 사전 협의 요청 사항

1. **인프라 구축 형태 결정 (On-Premise vs Public Cloud)**:
   - 사내 전산실 내 전용 GPU 서버 신규 도입(**Option A**) 또는 기보유 인프라/클라우드 활용 SW 구축(**Option B**) 방향성 확정
2. **원천 BOM DB 접근 및 복제 파이프라인 협의**:
   - 운영계 영향도를 배제하기 위한 읽기 전용 복제본(Read Replica) 및 배치 연동 방안 협의
3. **상호 데이터 준비(Data Readiness) 협의체 구성**:
   - 1차 파일럿 대상 대표 차종(토레스, 렉스턴, 액티언 등)의 원천 스키마 정의 및 도메인 정제를 수행할 공동 실무진 지정
