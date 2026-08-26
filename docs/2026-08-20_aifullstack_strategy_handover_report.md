# [인수인계 보고서] MEGAZONECLOUD AI Full Stack 전략 및 오퍼링 인수인계 핸드오버 문서

- **문서 번호**: WORKLOG-20260820-AIFULLSTACK-HANDOVER-01
- **작성 일자**: 2026년 08월 20일
- **작성 조직**: 메가존클라우드(주) ISSU 아키텍처 & 솔루션 프리세일즈 팀
- **문서 목적**: 본 리포지토리(`aifullstack`)가 향후 **AI Full Stack 전략 수립, 빅테크 비교, 3rd-Party ISV 타당성 검토 및 세일즈 오퍼링 총괄 허브**로 운영됨에 따른 전체 산출물 현황, 비즈니스 가드레일, 및 운영 지침의 체계적 인수인계

---

## 1. 리포지토리 목적 및 역할 정의

본 워크스페이스는 메가존클라우드 ISSU(Integrated Solution Sales Unit)의 **엔터프라이즈 AI Full Stack 전략 수립 및 세일즈 오퍼링 총괄 허브**로 정의됩니다.

* **조직 본질**: 메가존클라우드의 **솔루션 세일즈(Solution Sales), 기술 영업 및 프리세일즈(Presales) 중심 조직**입니다.
* **오퍼링 형태**: 하드웨어를 직접 제조/보유하지 않으며, **'세일즈 오퍼링(Offering)' 및 아키텍처 컨설팅 패키지 형태**로 포트폴리오를 보유합니다 (현재 AIDC 사업에 대하여 검토 중이나, 구체화된 내용은 없음).
* **공급 체계**: 실제 물리적 하드웨어의 조달, 납품, 유지보수 및 구축은 **Dell과 NVIDIA 파트너 에코시스템**을 통해 실행됩니다.
* **인프라 제약**: 사내에 독자 H/W를 직접 설치하여 테스트할 수 있는 **자체 실증 Infra가 부재**하므로, 클라우드 Testbed 및 파트너 원격 랩을 통해 기술 검증을 수행합니다.

---

## 2. 5대 핵심 비즈니스 원칙 및 의사결정 가드레일

새로운 하드웨어/소프트웨어 솔루션을 검토하거나 세일즈 오퍼링을 구성할 때 아래 5가지 가드레일을 100% 준수해야 합니다:

1. **Dell / NVIDIA 공인 총판 지위 극대화 (Core Focus)**:
   * 메가존클라우드가 이미 확보한 **Dell PowerEdge 서버 및 NVIDIA GPU 표준 엔터프라이즈 인프라 비즈니스에 전사 영업 및 엔지니어링 역량을 최우선 집중**합니다.
2. **솔루션 프레임워크 파편화 방지**:
   * 기술적 실현 가능성만으로 무분별하게 신규 H/W 섀시나 독자 칩셋을 표준 포트폴리오에 편입하지 않으며, 표준 4-Layer 아키텍처의 단순성과 안정성을 지킵니다.
3. **총판 사업 편입 허들 (분기 100억 원 이상) 및 H/W 직접 핸들링 배제**:
   * MZC 총판 사업 편입 기준(분기 100억 원, 연간 400억 원 이상)에 미달하는 니치 솔루션은 총판으로 편입하지 않으며, 실물 H/W 수입·재고·AS를 MZC가 직접 떠안는 **'H/W 직접 핸들링'은 원천 배제**합니다.
4. **신규 비즈니스 인력/조직 셋업 비용 & 1년 단위 BEP(손익분기점) 기준**:
   * 신규 솔루션 검토 시 **5인 전담 조직(세일즈 2 + 엔지니어 2 + PM 1) 셋업 연간 고정비(약 7억~12억 원) 시뮬레이션을 의무적으로 포함**합니다.
   * 200여 개 ISV 파트너십 재평가 기준에 따라, 기술적 하자가 없더라도 **손익분기점(BEP)이 1년 단위 이상 소요되면 공식 편입에 대해 '부정적(No-Go / 단순 기술 검토로 동결)'**으로 판정합니다.
5. **객관적 톤앤매너 및 '검토 보고서' 명칭 원칙**:
   * "강력 추천", "독보적" 등의 과장된 수식어를 배제하고 "높은 가능성이 있다", "비즈니스 검토 필요" 등 신중하고 객관적인 톤을 유지합니다.
   * 공식 전략 수립으로 오인되지 않도록 ISV 타당성 문서는 **"AI Full Stack 편입 가능성 종합 검토 보고서"** 명칭을 사용합니다.

---

## 3. 전체 산출물 현황 (Architecture & File Map)

현재 리포지토리에 구축 완료된 핵심 산출물 체계는 다음과 같습니다:

```
c:\dev\antigravity-workspace\aifullstack\
├── offering\                                 # 🌐 인터랙티브 웹 포털 및 보고서 (15종)
│   ├── index.html                            # 🌟 마스터 인덱스 허브 포털 (날짜별 최신순 정렬)
│   ├── mzc_ai_fullstack_strategy_service_report.html # 🏢 경영진 마스터 전략 보고서
│   ├── nvidia_ai_factory_vs_mzc_fullstack_comparison.html # ⚔️ 빅테크 비교 가이드
│   ├── 2026-08-20_sambanova_ai_fullstack_analysis.html    # ⚡ SambaNova RDU 종합 검토서
│   ├── 2026-08-20_liqid_composable_gpu_memory_pooling_analysis.html # 💾 Liqid CDI 분석서
│   ├── 2026-08-20_nota_ai_netspresso_analysis_report.html # 🧠 Nota NetsPresso 분석서
│   ├── akamai_ncp/                           # 🌐 AKAMAI GPUaaS 공동 사업 포털 및 보고서군 (5종 웹)
│   │   ├── README.html                       # 🚀 GPUaaS 공동 사업 종합 포털
│   │   ├── proposal/mzc_akamai_partnership.html # 📋 공동 사업 제안서 웹
│   │   └── feasibility/financial_simulation_report.html # 📊 재무/BEP 보고서 웹
│   ├── ai_fullstack_solution_packages_portal.html # 📦 4대 비즈니스 솔루션 패키지 포털
│   ├── generate_*_report_docx.py             # ⚙️ 공식 Word 문서 자동 생성 파이썬 스크립트군
│   └── docx\                                 # 📄 공식 Word (DOCX) 산출물 (17종)
│       ├── 2026-08-20_MZC_AI_Fullstack_Strategy_Service_Report.docx
│       ├── 2026-08-20_NVIDIA_Dell_MZC_AI_Factory_Comparison_and_Implementation_Guide.docx
│       ├── 2026-08-20_MZC_Akamai_GPUaaS_Partnership_Proposal.docx
│       ├── 2026-08-20_Akamai_NCP_Financial_BEP_Simulation_Report.docx
│       ├── 2026-08-20_Akamai_NVIDIA_Partnership_Research.docx
│       ├── 2026-08-20_NVIDIA_NCP_Market_Analysis.docx
│       ├── 2026-08-20_SambaNova_AI_Fullstack_Analysis_Report.docx
│       ├── 2026-08-20_Liqid_Composable_GPU_Memory_Pooling_Analysis_Report.docx
│       ├── 2026-08-20_Nota_AI_NetsPresso_Fullstack_Analysis_Report.docx
│       └── [솔루션 패키지 및 세부 제안서 8종 DOCX]
├── docs\
│   ├── TODO.md                               # 📋 전략 및 오퍼링 현행화 로드맵
│   ├── specs\                                # 📑 프로젝트 작업 명세서 (Plan-Code-Doc 트라이어드)
│   │   ├── 2026-08-20_mzc_ai_fullstack_strategy_service_report_spec.md
│   │   ├── 2026-08-20_akamai_ncp_business_plan_integration_spec.md
│   │   ├── 2026-08-20_sambanova_ai_fullstack_analysis_spec.md
│   │   ├── 2026-08-20_liqid_composable_gpu_memory_pooling_analysis_spec.md
│   │   └── 2026-08-20_nota_netspresso_analysis_report_spec.md
│   └── worklog\                              # 📝 인수인계 및 작업 일지
│       └── 2026-08-20_aifullstack_strategy_handover_report.md
└── TODO.md                                   # 📋 루트 로드맵 파일
```

---

## 4. 3대 3rd-Party ISV/HW 검토 결과 요약

| 솔루션명 | 핵심 기술 요약 | 5인 조직 연간 고정비 | 예상 BEP 기간 | 최종 비즈니스 판정 |
| :--- | :--- | :--- | :--- | :--- |
| **SambaNova Systems**<br>(SN50 RDU / SambaRack) | • TSMC 5nm 3-Tier 메모리<br>• 250+ Tok/s Fast Decode 특화 | 약 10억 ~ 12억 원 | **3년 ~ 4년 소요**<br>(1년 내 불가) | 🛑 **공식 편입 부정적 (No-Go)**<br>• 단순 기술 검토로 동결<br>• Dell/NVIDIA 총판 집중 |
| **Liqid Inc.**<br>(Composable PCIe CDI) | • PCIe Gen5 GPU/DRAM 풀링<br>• 200TB 동적 할당 및 TCO 35% 절감 | 약 7억 ~ 9억 원 | **2.5년 ~ 3년 소요**<br>(1년 내 불가) | 🛑 **공식 편입 부정적 (No-Go)**<br>• 분기 100억 허들 미달<br>• H/W 직접 핸들링 배제 |
| **Nota.ai**<br>(NetsPresso) | • HW 인지 경량화 & 양자화<br>• RHOAI 상호보완 TPS 3배 극대화 | 기존 MLOps 인력 활용 가능<br>(추가 고정비 미미) | **즉시 협업 가능**<br>(S/W 파트너십) | ⚠️ **선별적 PoC 검증 추진**<br>• 대형 LLM 및 폐쇄망 실증 후<br>S/W 오퍼링 연계 검토 |

---

## 5. 차기 작업자를 위한 운영 지침

1. **파이썬 가상환경 및 DOCX 빌드**:
   * 본 프로젝트의 파이썬 환경은 `.venv`를 사용합니다 (`.venv\Scripts\python`).
   * 신규 DOCX 생성 시 `python-docx` 라이브러리를 활용하며, `offering/generate_*_docx.py` 패턴을 준수합니다.
2. **문서 명명 규칙 준수**:
   * 새로 작성되는 모든 전략서, 보고서, 명세서, 작업일지는 **의무적으로 `YYYY-MM-DD_` 접두사를 파일명에 포함**합니다.
3. **Plan-Code-Doc 트라이어드 규칙**:
   * 작업 시 `[작업계획서/TODO]` - `[HTML 웹 보고서 / DOCX / 코드]` - `[docs/specs/ 명세서]`를 1:1:1 세트로 항상 최신 상태로 유지합니다.
4. **마스터 인덱스 포털 유지보수**:
   * 신규 문서 발행 시 `offering/index.html` 최상단 타임라인에 최신 일자 카드로 즉시 등록하여 엔터프라이즈 사용자가 원클릭으로 탐색할 수 있도록 유지합니다.
