# AKAMAI & NVIDIA & MZC 한국형 GPUaaS 공동 사업 타당성 검토 프로젝트

본 프로젝트는 한국 시장 내 GPU 서버 수급의 한계를 극복하고, 저비용·고효율의 인공지능 추론 및 학습 환경을 제공하기 위한 **AKAMAI - NVIDIA - MZC(메가존클라우드) 공동 GPUaaS(GPU-as-a-Service) 사업 기획안**과 이에 대한 다차원적 타당성 검증(Feasibility Study) 보고서를 수립하는 워크스페이스입니다.

---

## 1. 사업 추진 배경 및 필요성

1. **국내 GPU 서버 확보 한계**: 글로벌 GPU 공급망 병목 및 규제 요인으로 인해 한국 내 기업들의 GPU 하드웨어 도입 리드타임이 수개월에서 1년 이상 지연되고 있습니다.
2. **비용 및 Egress 장벽**: 기존 대형 하이퍼스케일러(AWS, GCP, Azure)의 GPU 클라우드는 높은 사용료와 특히 거대한 데이터 전송 요금(Egress Fees)으로 인해 기업들의 AI 운영 TCO(총소유비용)를 급격히 상승시키고 있습니다.
3. **엣지 분산 AI 수요 증가**: 스마트 팩토리, 자율주행, 실시간 미디어 스트리밍 등 저지연 추론이 요구되는 분야가 급증함에 따라 중앙 집중식 AI 공장에서 분산 엣지 구조로의 패러다임 전환이 필요합니다.

---

## 2. 삼사(AKAMAI - NVIDIA - MZC) 파트너십 협력 구조

본 기획안은 **"아카마이의 자본력/글로벌 인프라 + 엔비디아의 AI 플랫폼 + MZC의 로컬 하드웨어 및 운영 역량"**을 결합한 하이브리드 위탁 운영 모델을 제안합니다.

```mermaid
graph TD
    MZC[MZC 메가존클라우드] -- "1. GPU 하드웨어 자산 공급" --> Akamai[AKAMAI Connected Cloud]
    Akamai -- "2. CapEx 매입 & IDC 구축 투자" --> Edge[한국 내 분산 GPUaaS 노드 구축]
    NVIDIA[NVIDIA AI 플랫폼 기술] -- "3. NIM, Triton, NCP 플랫폼 제공" --> Edge
    Edge -- "4. 위탁 운영 및 영업 관리 위임" --> MZC
    MZC -- "5. 국내 영업 및 MSP 관리" --> Customer[국내 AI 연구소 / 기업 고객]
    Customer -- "6. GPUaaS 사용 및 비용 지불" --> Edge
    Edge -- "7. 수익 배분 (Revenue Share)" --> MZC
```

### 파트너별 세부 역할:
*   **AKAMAI (투자 및 글로벌 인프라)**
    *   MZC가 기 확보한 GPU 하드웨어 장비를 일시 매입하여 초기 자본 투자(CapEx) 부담 완화.
    *   한국 내 코로케이션 IDC를 임차하여 Akamai Connected Cloud 전용 GPUaaS 엣지 노드로 편입.
    *   **요금 초강수 제안**: H100 시간당 **$2.50** (약 3,300원), L40S 시간당 **$1.10** (약 1,450원) 및 **초저가 Egress 요금($0.005/GB)** 적용 (국내 Naver/NHN의 시간당 7,000~8,000원대 GPU 요금 및 90~130원대 Egress 요금 대비 최소 50%~95%의 비용 절감 메리트 제공).
*   **NVIDIA (AI 솔루션 및 공급망)**
    *   NVIDIA Cloud Partner(NCP) 인증 및 DGX Cloud 레퍼런스 아키텍처 제공.
    *   NVIDIA NIM 및 Triton Inference Server 탑재를 통한 풀스택 AI 추론 파이프라인 소프트웨어 최적화 보장.
*   **MZC (장비 공급, 위탁 운영 및 영업)**
    *   글로벌 공급난 속에서 기 확보된 GPU 하드웨어 솔루션의 아카마이 매각 파이프라인 확보.
    *   한국 내 GPUaaS 인프라의 24/7 전문 위탁 운영(Ops) 및 기술 지원.
    *   국내 엔터프라이즈, AI 스타트업, 공공기관 대상 총판 영업 및 기술 컨설팅 수행.

---

## 3. 디렉토리 구조 및 산출물 안내

프로젝트 분석 문서와 타당성 시뮬레이션 자료는 아래 경로에 체계적으로 자산화됩니다.

```
akamai_ncp/
├── .agents/                    # 에이전트 가이드라인 및 워크플로우 정의
│   ├── AGENTS.md               # AI 에이전트 전역 준수 규칙 (비즈니스 타당성 감사 기준)
│   └── skills/                 # 기획 검토를 위한 전문 스킬 모음
├── daegu_suseong_aidc/         # 대구 수성알파시티 AIDC & 피지컬 AI 로봇 트레이닝 센터 전담 폴더 (선행조사·제안서)
├── wonik_ax_center/            # 원익로보틱스 AX 트레이닝 센터 전담 폴더 (RFI 서면질의·공식회신·본제안서·아카이브)
├── proposal/                   # ISV BU Hybrid Cloud 팀 마스터 전략서(v3.5) 및 MZC-아카마이 공동 사업 제안서
├── research/                   # 아카마이-엔비디아 협력 분석 및 NVIDIA NCP 시장 분석 보고서
├── feasibility/                # 기술, 경제성(BEP 시뮬레이션 결과 포함), 보안 분석 보고서
├── scripts/
│   ├── bep_simulation.py       # 가동률 및 비용 모델링용 파이썬 시뮬레이션 스크립트
│   └── convert_all_md.py       # 마크다운 -> 프리미엄 HTML & DOCX 일괄 변환 스크립트
└── CLAUDE.md                   # 로컬 개발 및 실행 환경 가이드라인
```

### 📄 ISV BU Hybrid Cloud 팀 마스터 전략 및 R&R 통합 제안서 (v3.5):
* **[ISV BU Hybrid Cloud 팀 마스터 방향성, 매출 극대화(영업 퍼널/MPN 판매채널화) 및 7인 멤버별 R&R 통합 제안서 (v3.5)](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/proposal/HYBRID_CLOUD_TEAM_STRATEGY_MASTER_INTEGRATED.html)** ([Markdown 원본](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/proposal/HYBRID_CLOUD_TEAM_STRATEGY_MASTER_INTEGRATED.md) / [Word 다운로드](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/proposal/HYBRID_CLOUD_TEAM_STRATEGY_MASTER_INTEGRATED.docx))

### 📄 대구 수성알파시티 AIDC & 피지컬 AI 로봇 트레이닝 센터 산출물 (`daegu_suseong_aidc/`):

#### 📌 [2026-11-17 · 11-14 · 11-12 업데이트] 주요 작업내역 요약
0. **[🆕 2026-11-17] 대구시 · KIRIA · DGIST 공유용 『대구 수성알파시티 AI 데이터센터(10MW→40MW) 구축 및 피지컬 AI · 스마트시티 통합 생태계 조성 방안 (v3.0)』 최신 반영**: 11.16 회의 합의사항(연내 `10MW` 사전 MOU 체결 및 향후 `40MW` 확대, 지역 기업 3대 부담 해소, 원스톱 플랫폼, 데이터 인입 허용·반출 차단 `Data Isolation` 및 기여기업 저가 인프라·특화모델 리워드, `AI DC+R&D+교육` 통합센터, 특화단지 원격 안전 관제 데이터 플라이휠, DGIST 리빙랩 비제조 지능화, 5종 휴머노이드 후속 지능화, `Isaac×Unity×오픈소스`, 수성 무선자가망 이동체·드론 스마트시티 및 의료 EMR 10년 의무보관 백업/DR·주행시험장·뿌리·바이오 확장, `H200급 300~500대`·`45PB` 산정)을 A4 문서형 HTML 뷰어·MD·DOCX로 통합 구축.
1. **[2026-11-14] 월요일 대구시 기계로봇과 제안용 ‘16:9 PPT 발표장표 HTML’ 및 ‘서술형 DOCX 형태 HTML’ 2종 제작 (대외용 — 내부 수익/동탄 배제)**: 정부 사업 **중복성 심사 돌파 논리('기존 실증·인증·R&D 사업을 KIRIA 전문가 매칭 + 수성 AIDC 공유 클라우드로 전환·고도화')**, **RFM & 로봇 훈련 데이터 서비스(DaaS)**, **`NVIDIA Isaac Sim + Unity` 상호보완 시뮬레이션**, 그리고 **로봇(대당 쓰루풋·데이터량) + 대구 City DT 통합 데이터 팩토리(`45PB` 3-Tier 스토리지 산정 포함)**를 ① 현장 투사용 **16:9 풀스크린 PPT 슬라이드 쇼 HTML**과 ② 인쇄·검토·배포용 **A4 서술형 DOCX 문서 뷰어 HTML** 2가지 포맷으로 동시 구축.
2. **[2026-11-14] MZC 사내 전략·수익성 심층 검토서 수립 (내부 전용)**: ① 수성지구 `4,000~6,000평` 조성원가 매입(시세 3배 상승) 및 동대구역 인접 **지식산업센터 분양(`+330억` 보전)·오피스 임대(`연 +45억` NOI)** 복합개발 타당성, ② MZC 매출 80%를 차지하는 **AWS 컴퓨트 매입 중 일부(단 10%만 전환해도 5MW 완판, `연 +365억` 연결 영업이익 개선 / 1/4 전환 시 10MW 소화)**를 별도 AIDC 법인으로 전환하는 레버리지 및 글로벌 테넌트 유치(`5MW+5MW` 스윙 배분) 정밀 검증.
3. **[2026-11-12] 대구시 로봇 9대 국책사업 팩트체크 & 26대 사업 아이디에이션**: 대구시 기계로봇과 전달 자료(`대구aidc_20261112.pdf`, 27면) 및 기정원(TIPA) 5극3특 검증, 달성(물리) × 수성(AI 두뇌) **'Twin-Hub' 전략** 및 상위 5대 추천 사업(추정 사업규모 포함) 도출.
4. **[2026-11-12] 10MW/5MW 표준 예산 구조 · 매출퍼즐 · PF 단계별 수익률 정립**: 하이브리드 3:2 모델 기준 예산 테이블(`10MW 3,500억` / `5MW 1,750억`), `연 380억 원`(5년 `1,900억 원`) 5대 매출퍼즐 및 JB동탄 DC 비교 전략 문서화.

#### 🗂️ `daegu_suseong_aidc/` 전체 문서 리스트 요약표

| 구분 | 문서명 (HTML 뷰어 / 원본 / Word) | 기준일 | 핵심 내용 및 활용 용도 |
| :---: | :--- | :---: | :--- |
| **🆕 11.22 공무원 정본**<br/>*(공식 보고서)* | **[대구 수성 AI 데이터센터(10MW→40MW) 구축 및 생태계 조성 공식 사업구상서 (v4.0 Formal)](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/daegu_suseong_aidc/2026-11-22_daegu_aidc_formal_proposal_for_officials.html)**<br/>([MD](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/daegu_suseong_aidc/2026-11-22_daegu_aidc_formal_proposal_for_officials.md) / [DOCX](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/daegu_suseong_aidc/2026-11-22_daegu_aidc_formal_proposal_for_officials.docx)) | `2026-11-22` | **[공무원 공식 제출용 정본]** 4부 체계(비전·`3,000평`·앵커 1:1·`Data Isolation` / `10MW` 30~50% 데이터양 `A` Part 1·2 매핑 / 멘토링·모델러·대학·마켓·고용 150명+ / 연내 MOU·인센티브) + 미주·부록 A~D·용어설명·참고문헌 |
| **🆕 11.22 발표 PPT**<br/>*(요약 12장)* | **[대구 수성 AI 데이터센터(10MW→40MW) 공식 브리핑 요약 PPT (12-Slide Summary)](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/daegu_suseong_aidc/2026-11-22_daegu_aidc_formal_proposal_ppt.html)**<br/>([MD](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/daegu_suseong_aidc/2026-11-22_daegu_aidc_formal_proposal_ppt.md) / [DOCX](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/daegu_suseong_aidc/2026-11-22_daegu_aidc_formal_proposal_ppt.docx)) | `2026-11-22` | **[공무원·유관기관 현장 발표 요약용]** 1부~4부 피드백 핵심을 12장 16:9 풀스크린 슬라이드로 압축 요약 (발표노트·레이저·라이트테마·PDF 인쇄 지원) |
| **11.17 발표용 PPT** | **[대구 수성 AIDC(10MW→40MW) 및 AI 생태계 조성 16:9 발표용 PPT (14-Slide Deck)](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/daegu_suseong_aidc/2026-11-17_daegu_aidc_ecosystem_and_kiria_master_ppt.html)**<br/>([PPTX 파워포인트](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/daegu_suseong_aidc/2026-11-17_daegu_aidc_ecosystem_and_kiria_master_ppt.pptx) / [MD](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/daegu_suseong_aidc/2026-11-17_daegu_aidc_ecosystem_and_kiria_master_ppt.md) / [DOCX](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/daegu_suseong_aidc/2026-11-17_daegu_aidc_ecosystem_and_kiria_master_ppt.docx)) | `2026-11-17` | **[대외 미팅 라이브 발표 & 메일 첨부용]** 11.16 회의 합의사항 전면 반영 14장 풀스크린 웹 PPT 슬라이드 쇼 + 실제 편집 가능한 네이티브 `.pptx` 파일 (발표자 노트 내장) |
| **🆕 최신 마스터 보고서** | **[대구 수성알파시티 AI 데이터센터(10MW→40MW) 구축 및 피지컬 AI · 스마트시티 통합 생태계 조성 방안 (v3.0)](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/daegu_suseong_aidc/2026-11-17_daegu_aidc_ecosystem_and_kiria_master_report.html)**<br/>([MD](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/daegu_suseong_aidc/2026-11-17_daegu_aidc_ecosystem_and_kiria_master_report.md) / [DOCX](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/daegu_suseong_aidc/2026-11-17_daegu_aidc_ecosystem_and_kiria_master_report.docx)) | `2026-11-17` | **[대외 공유 최신본 — 대구시·KIRIA·부사장님 전달용]** 연내 10MW MOU(→40MW), 지역기업 3대 부담 해소, 원스톱 플랫폼, 데이터 격리(Isolation)·기여보상, 특화단지 원격관제 플라이휠·DGIST 리빙랩·무선자가망 스마트시티·의료 EMR 백업/DR 종합 보고서 |
| **📑 총괄 요약 리포트** | **[대구 수성 AIDC & 피지컬 AI 전체 산출물(11종) 총괄 요약 리포트 · 링크 허브](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/daegu_suseong_aidc/2026-11-14_daegu_aidc_document_summary_report.html)**<br/>([MD](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/daegu_suseong_aidc/2026-11-14_daegu_aidc_document_summary_report.md) / [DOCX](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/daegu_suseong_aidc/2026-11-14_daegu_aidc_document_summary_report.docx)) | `2026-11-14` | **[마스터 인덱스 리포트]** 미팅 대상별 추천 문서 선택 가이드, 대외용/사내대외비 보안 등급 구분 및 11종 전체 파일별 핵심 요약·바로가기 총정리 |
| **★ 월요일 PPT** | **[대구시 기계로봇과 · KIRIA 협력 제안 16:9 발표용 PPT (12-Slide Deck)](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/daegu_suseong_aidc/2026-11-14_daegu_robot_division_monday_proposal_ppt.html)**<br/>([MD](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/daegu_suseong_aidc/2026-11-14_daegu_robot_division_monday_proposal_ppt.md) / [DOCX](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/daegu_suseong_aidc/2026-11-14_daegu_robot_division_monday_proposal_ppt.docx)) | `2026-11-14` | **[대외 미팅 라이브 발표용 — 수익/동탄 배제]** 16:9 풀스크린 인터랙티브 PPT 슬라이드(발표자 노트·레이저 포인터·라이트 테마 탑재) |
| **★ 월요일 서술형** | **[대구시 기계로봇과 · KIRIA 협력 제안서 — 서술형 DOCX 형태 문서](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/daegu_suseong_aidc/2026-11-14_daegu_robot_division_monday_proposal_narrative.html)**<br/>([MD](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/daegu_suseong_aidc/2026-11-14_daegu_robot_division_monday_proposal_narrative.md) / [DOCX](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/daegu_suseong_aidc/2026-11-14_daegu_robot_division_monday_proposal_narrative.docx)) | `2026-11-14` | **[대외 배포·검토용 — 수익/동탄 배제]** A4 7쪽 분량 MS Word 문서형 HTML 뷰어(중복성 해소·RFM/DaaS·Isaac×Unity·`45PB` 데이터 팩토리 완결 문장체 서술본) |
| **★ 사내 전략서** | **[MZC 사내 전략 검토서: 부지·분양 보전, AWS 매입 전환 & 5+5MW 사업성](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/daegu_suseong_aidc/2026-11-14_mzc_internal_strategy_land_aws_offload_and_hybrid_10mw.html)**<br/>([MD](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/daegu_suseong_aidc/2026-11-14_mzc_internal_strategy_land_aws_offload_and_hybrid_10mw.md) / [DOCX](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/daegu_suseong_aidc/2026-11-14_mzc_internal_strategy_land_aws_offload_and_hybrid_10mw.docx)) | `2026-11-14` | **[사내 경영진 대외비]** 4~6천평 원가 부지 + 지산센터 분양·오피스 임대 보전, AWS 컴퓨트 매입 전환(10%~25%) 연결 손익(`연 +365억 OP`), 5+5MW 스윙 및 `45PB` 스토리지 CapEx/수익 검증 |
| **발표 장표** | **[KIRIA 1차 협력 미팅 발표 장표 (10-Slide Deck)](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/daegu_suseong_aidc/2026-11-12_kiria_1st_meeting_presentation_deck.html)**<br/>([MD](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/daegu_suseong_aidc/2026-11-12_kiria_1st_meeting_presentation_deck.md) / [DOCX](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/daegu_suseong_aidc/2026-11-12_kiria_1st_meeting_presentation_deck.docx)) | `2026-11-12` | **[대외 미팅 발표용]** KIRIA·대구시 1차 회의용 16:9 인터랙티브 슬라이드(Twin-Hub 구도, Top 5 추천 아이템·추정 사업규모, `'27.1H` 임대형 브릿지, 협의 안건) |
| **회의 요약본** | **[KIRIA 1차 협력 미팅 핵심 요약본 (Executive Handout)](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/daegu_suseong_aidc/2026-11-12_kiria_1st_meeting_executive_summary.html)**<br/>([MD](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/daegu_suseong_aidc/2026-11-12_kiria_1st_meeting_executive_summary.md) / [DOCX](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/daegu_suseong_aidc/2026-11-12_kiria_1st_meeting_executive_summary.docx)) | `2026-11-12` | **[대외 배포 유인물]** 사내 민감 PF 이슈를 배제하고 협력 명분·Top 5 아이템(추정 사업규모 포함)·기업 애로 해소·실무 TF 안건만 압축한 요약서 |
| **예산·매출퍼즐** | **[대구 AIDC 표준 예산 구조 재무 테이블 및 매출퍼즐 분석서](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/daegu_suseong_aidc/2026-11-12_daegu_aidc_budget_structure_and_revenue_puzzle.html)**<br/>([MD](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/daegu_suseong_aidc/2026-11-12_daegu_aidc_budget_structure_and_revenue_puzzle.md) / [DOCX](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/daegu_suseong_aidc/2026-11-12_daegu_aidc_budget_structure_and_revenue_puzzle.docx)) | `2026-11-12` | **[내부 재무 기준서]** 10MW(`3,500억`)/5MW(`1,750억`) 부지·건축·MEP·컴퓨트·연간 OpEx 상세 테이블 및 5MW(`연 380억`/5년 `1,900억`) 5대 매출퍼즐 매핑 |
| **역산출·PF분석** | **[대구 AIDC 비용 역산출, PF 단계별 수익률 및 'JB동탄 DC' 비교 보고서](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/daegu_suseong_aidc/2026-11-12_daegu_aidc_reverse_costing_pf_risk_and_jb_dongtan_analysis.html)**<br/>([MD](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/daegu_suseong_aidc/2026-11-12_daegu_aidc_reverse_costing_pf_risk_and_jb_dongtan_analysis.md) / [DOCX](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/daegu_suseong_aidc/2026-11-12_daegu_aidc_reverse_costing_pf_risk_and_jb_dongtan_analysis.docx)) | `2026-11-12` | **[내부 전략·심사용]** 지식산업센터 분양 모델 대비 6단계 개발 리스크·기대수익률(IRR), 최적 진입 시점, 구미 앤트로픽 무산 교훈 및 JB동탄 DC 비교 |
| **아이디에이션** | **[대구 AIDC 9대 국책사업 검증 및 5MW 회수 26대 사업 아이디에이션 총괄본](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/daegu_suseong_aidc/2026-11-12_daegu_aidc_kiria_meeting_and_5mw_business_ideation.html)**<br/>([MD](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/daegu_suseong_aidc/2026-11-12_daegu_aidc_kiria_meeting_and_5mw_business_ideation.md) / [DOCX](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/daegu_suseong_aidc/2026-11-12_daegu_aidc_kiria_meeting_and_5mw_business_ideation.docx)) | `2026-11-12` | **[전체 백과사전]** 9대 국책사업 예산 실체 팩트체크, 대구TP 88개사 수요 분석, 6대 트랙 × 26개 세부 사업 아이템 풀(Pool) 총망라 |
| **통합 제안서** | **[대구 수성알파시티 피지컬 AI 로봇 트레이닝 센터 구축·운영 제안서 (V2.1)](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/daegu_suseong_aidc/daegu_suseong_robot_training_center_proposal.html)**<br/>([MD](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/daegu_suseong_aidc/daegu_suseong_robot_training_center_proposal.md) / [DOCX](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/daegu_suseong_aidc/daegu_suseong_robot_training_center_proposal.docx)) | `2026-11-12` | **[본 제안서 최신판]** 대구시·산하기관 대상 공식 제안서 (V2.1에 제7장 '9대 국책사업 연계 및 KIRIA Twin-Hub 전략' 증보 반영) |
| **기술 상세판** | **[대구 피지컬 AI 로봇 트레이닝 센터 구축 제안서 (상세판)](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/daegu_suseong_aidc/daegu_physical_ai_robot_training_center_proposal.html)**<br/>([MD](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/daegu_suseong_aidc/daegu_physical_ai_robot_training_center_proposal.md) / [DOCX](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/daegu_suseong_aidc/daegu_physical_ai_robot_training_center_proposal.docx)) | `2026-11-09` | **[아키텍처 레퍼런스]** NVIDIA Omniverse / Isaac Lab / Cosmos 기반 피지컬 AI 트레이닝 파이프라인 기술 상세 설계본 |
| **선행 조사** | **[대구 AIDC & 피지컬 AI 선행 조사 보고서](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/daegu_suseong_aidc/daegu_aidc_physical_ai_preliminary_study.html)**<br/>([MD](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/daegu_suseong_aidc/daegu_aidc_physical_ai_preliminary_study.md) / [DOCX](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/daegu_suseong_aidc/daegu_aidc_physical_ai_preliminary_study.docx)) | `2026-11-09` | **[기초 리서치]** 수성알파시티 입지 여건, 국내외 로봇 트레이닝 센터 동향 및 초기 타당성 조사 보고서 |

#### 🚀 KIRIA 1차 미팅 집중 부각 '상위 5대 추천 사업 아이템' 및 추정 사업규모

> **산정 기준**: 이미 컨소시엄이 확정된 기 진행 과제는 제외하고 **`'26년 말 ~ '27년+` 신규 기획·공모 예정 사업**을 대상으로 산출함. 추정 사업규모는 **모사업 국책 예산 규모**와 이 중 수성 AIDC(코로케이션·GPUaaS·플랫폼 구축/운영)로 유입 가능한 **MZC 타깃 추정 사업규모(5년 누적 및 연간 환산)**를 구분하여 표기함.

| 순위 | 추천 공동 사업 아이템명 | 연계 예정 국책사업 (모사업 예산 규모) | **추정 사업규모 (MZC 연계 5년 누적 / 연간)** | 핵심 내용 및 수익·회수 구조 |
| :---: | :--- | :--- | :---: | :--- |
| **Top 1** | **국가로봇테스트필드 '실증 데이터 레이크 & 사전 가상실증(Sim-to-Real)' 백엔드** | • 테스트필드 데이터 저장·활용 인프라 공모(`255.7억`)<br/>• 테스트필드(`1,997.5억`) 실·가상 실증 고도화 | **`220억 ~ 280억 원`**<br/>*(구축 SI `80~100억` + 운영 `연 30~35억`)* | 달성-수성 전용광망 직결 스토리지·레이크하우스 구축 및 물리 입소 전 Isaac Sim 사전 시운전 패스 표준화 (`0.8MW` 수용) |
| **Top 2** | **휴머노이드 'AI 신뢰성 · 극한 충돌 · 사이버보안(EU CRA)' 가상 인증 클라우드** | • 신규 휴머노이드 로봇 안전인증센터 구축(`'26~'30, 187억`) 및 공인 인증 수수료·바우처 | **`120억 ~ 150억 원`**<br/>*(구축 `35~45억` + 운영 `연 20~25억`)* | 실물 파손 없는 10만 회 병렬 충돌·적대적 해킹 방어 시뮬레이션 기반 KIRIA 글로벌 공인 인증 발급 (`0.5MW` 수용) |
| **Top 3** | **휴머노이드 특화단지 '가변식 가상 테스트베드 & 국가 통합 원격관제 센터'** | • 대구·경북 휴머노이드 특화단지 지자체 후속 건의(`5년 약 3,000~5,000억` 기획 중 기반사업) | **`200억 ~ 250억 원`**<br/>*(구축 `50~70억` + 운영 `연 30~35억`)* | 현장 로봇 비정상 상황 원격 개입(Tele-op Fallback) 중앙 관제 및 부품기업 `CAD→OpenUSD` 디지털 카탈로그 (`0.5MW` 수용) |
| **Top 4** | **5극3특 'K-로봇 파운데이션 모델(RFM) 허브 & 국책 R&D GPU 바우처 할당제'** | • 5극3특 성장엔진 대형 R&D + M.AX R&D (`다년도 3,000~5,000억` 풀) + 초광역특구 샌드박스 | **`600억 ~ 800억 원`**<br/>*(바우처·전용노드 `연 120~160억`)* | 신규 R&D 연구비 15~20% 공동활용 GPU 의무 편성(`1.0MW`) + 비식별 유예 원본영상 학습 규제특례 인바운드 유치(`0.4MW`) |
| **Top 5** | **수출형 K-로봇 '글로벌 원격관제 · 무선 AI 업데이트(OTA)' 수출 브릿지** | • KIRIA 수출지원 + 5극3특 수출바우처 + 기정원(TIPA) 제조 AX 바우처(`연 300~500억` 풀) | **`350억 ~ 450억 원`**<br/>*(구독·바우처 `연 70~90억`)* | 인증 완료 수출 로봇에 수성 AIDC 코어 + Akamai 글로벌 엣지(4,000+ PoP, Egress 0원) 원스톱 관제 번들링 (`0.6MW` 수용) |
| **합계** | **상위 5대 핵심 사업군 총계** *(+산하 6개 기관 서버실 통합 `5년 250억` 별도)* | **신규 예정 국책 인프라 · 대형 R&D · 기업 바우처 패키지 결합** | **`1,490억 ~ 1,930억 원`**<br/>*(SI 구축 + 운영 `연 270~345억`)* | 산하기관 통합 코로케이션(`1.2MW`, `연 50억`) 합산 시 **대구 5MW 목표(`연 380억` / 5년 `1,900억`) 100% 달성** |

### 📄 원익로보틱스 AX 트레이닝 센터 산출물 (`wonik_ax_center/`):
* **[2026-11-18 원익로보틱스 AX Center RFI 공식 회신서 (내부 논의 · 타 부서 자료보완 정본)](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/wonik_ax_center/20261118_wonik_robotics_ax_center_rfi_response.html)** ([Markdown 원본](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/wonik_ax_center/20261118_wonik_robotics_ax_center_rfi_response.md) / [Word 정본](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/wonik_ax_center/20261118_wonik_robotics_ax_center_rfi_response.docx))
* **[원익로보틱스 AX Center RFI 공식 회신서 (최신 동기화본)](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/wonik_ax_center/wonik_robotics_ax_center_rfi_response.html)** ([Markdown 원본](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/wonik_ax_center/wonik_robotics_ax_center_rfi_response.md) / [Word 다운로드](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/wonik_ax_center/wonik_robotics_ax_center_rfi_response.docx))
* **[2026-11-11 설명회 팩트 반영 개정 사업제안서 (v2.0)](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/wonik_ax_center/2026-11-11_wonik_robotics_ax_center_proposal_v2.html)** ([Markdown 원본](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/wonik_ax_center/2026-11-11_wonik_robotics_ax_center_proposal_v2.md) / [Word 다운로드](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/wonik_ax_center/2026-11-11_wonik_robotics_ax_center_proposal_v2.docx))
* **[원익로보틱스 AX Center (피지컬 AI 로봇 트레이닝 센터) 구축 사업제안서](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/wonik_ax_center/wonik_robotics_ax_center_proposal.html)** ([Markdown 원본](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/wonik_ax_center/wonik_robotics_ax_center_proposal.md) / [Word 다운로드](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/wonik_ax_center/wonik_robotics_ax_center_proposal.docx))
* **[원익로보틱스 AX Center RFI 공식 서면 질의서](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/wonik_ax_center/wonik_robotics_ax_center_rfi_written_inquiry.html)** ([Markdown 원본](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/wonik_ax_center/wonik_robotics_ax_center_rfi_written_inquiry.md) / [Word 다운로드](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/wonik_ax_center/wonik_robotics_ax_center_rfi_written_inquiry.docx))
* **[원익로보틱스 이전 비교/권고 분석 보고서 (Archive)](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/wonik_ax_center/archive/)**

### 📄 AKAMAI - NVIDIA - MZC 공동 사업 산출물 바로가기:
* **[아카마이-엔비디아 파트너십 분석](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/research/akamai_nvidia_partnership.html)**
* **[NVIDIA NCP 시장 분석](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/research/nvidia_ncp_market_analysis.html)**
* **[MZC-아카마이 공동 사업 제안서](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/proposal/mzc_akamai_partnership.html)**
* **[재무적 타당성 시뮬레이션 보고서](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/feasibility/financial_simulation_report.html)**

---

## 4. 타당성 점검 마일스톤

본 워크스페이스는 다음과 같은 4단계 타당성 평가 프로세스를 거쳐 기획을 구체화합니다:
1. **기술 적합성**: LKE 및 가상화 노드 상에서의 NVIDIA AI 엔터프라이즈 성능 벤치마크 및 엣지 지연 시간 검증.
2. **비즈니스 및 경제성**: 파이썬 시뮬레이션을 활용한 투자 규모별 BEP(손익분기 가동률) 및 ROI 도출.
3. **시장성**: 하이퍼스케일러(AWS, GCP, Azure) 대비 가격 경쟁력 포지셔닝 분석.
4. **규제 및 보안**: 망분리, 개인정보보호법 및 데이터 주권 요건 검토.
