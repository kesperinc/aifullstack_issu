# [총괄 요약 리포트] 대구 수성알파시티 AIDC & 피지컬 AI 프로젝트 전체 산출물 가이드 및 링크 모음

- **문서 구분**: 프로젝트 전체 산출물 요약 리포트 (Master Document Index & Summary Report)
- **대상 디렉터리**: `docs/akamai_ncp/daegu_suseong_aidc/` (총 11종 핵심 문서 세트 · 33개 파일)
- **최종 업데이트**: 2026년 11월 14일

---

## 1. 미팅 및 목적별 빠른 선택 가이드 (Quick Start)

회의 참석 대상과 보안 수준에 따라 아래 **권장 문서 세트**를 즉시 선택하여 활용하십시오.
- **🟢 대외용 문서**: 사내 수익률(IRR/영업이익), JB동탄 DC, AWS 내부 매입 전환, 부지 시세차익·지식산업센터 분양 수익 및 특정 인명이 **100% 배제**된 안전한 대외 협력 문서입니다.
- **🔴 사내 대외비 문서**: 메가존클라우드 내부 투자심의, PF 금융 구조화, 부지 복합개발 분양 수익 보전 및 AWS 매입 오프로딩 손익 시뮬레이션을 담은 내부 전략 문서입니다.

| 활용 상황 / 대상 | 최우선 추천 문서 (클릭 시 열기) | 보조 지참 / 배포 추천 문서 | 보안 등급 |
| :--- | :--- | :--- | :---: |
| **월요일 대구시 기계로봇과 실무 미팅**<br/>*(기존사업 전환·데이터팩토리 아이디어 제안)* | **[① 월요일 제안용 16:9 PPT 슬라이드 (HTML)](./2026-11-14_daegu_robot_division_monday_proposal_ppt.html)** | **[② 월요일 제안서 서술형 DOCX 뷰어 (HTML)](./2026-11-14_daegu_robot_division_monday_proposal_narrative.html)** ([Word](./2026-11-14_daegu_robot_division_monday_proposal_narrative.docx)) | 🟢 대외용 |
| **한국로봇산업진흥원(KIRIA) 임원진 1차 미팅**<br/>*(상위 5대 공동사업 및 추정 사업규모 협의)* | **[④ KIRIA 1차 미팅 10장 발표장표 (HTML)](./2026-11-12_kiria_1st_meeting_presentation_deck.html)** | **[⑤ KIRIA 1차 미팅 핵심 요약본 (HTML)](./2026-11-12_kiria_1st_meeting_executive_summary.html)** ([Word](./2026-11-12_kiria_1st_meeting_executive_summary.docx)) | 🟢 대외용 |
| **대구시·산하기관 공식 본 제안서 제출**<br/>*(센터 구축·운영 종합 제안 및 기술 아키텍처)* | **[⑨ 수성 피지컬 AI 트레이닝 센터 제안서 V2.1 (HTML)](./daegu_suseong_robot_training_center_proposal.html)** | **[⑩ 피지컬 AI 트레이닝 센터 기술 상세판 (HTML)](./daegu_physical_ai_robot_training_center_proposal.html)** | 🟢 대외용 |
| **MZC 경영진 · 투자심의 · 사업개발 내부 검토**<br/>*(원가부지 분양보전·AWS 전환·PF 수익률)* | **[③ MZC 사내 전략: 부지·AWS 전환·5+5MW 검토서 (HTML)](./2026-11-14_mzc_internal_strategy_land_aws_offload_and_hybrid_10mw.html)** | **[⑥ 표준 예산·매출퍼즐](./2026-11-12_daegu_aidc_budget_structure_and_revenue_puzzle.html)** & **[⑦ PF 리스크·동탄 비교](./2026-11-12_daegu_aidc_reverse_costing_pf_risk_and_jb_dongtan_analysis.html)** | 🔴 사내대외비 |

---

## 2. 전체 산출물(11종) 한눈에 보기 요약표

| 번호 | 분류 / 보안 | 문서명 및 포맷별 링크 (`HTML` / `DOCX` / `MD`) | 작성일 | 핵심 요약 (주요 수록 내용) |
| :---: | :---: | :--- | :---: | :--- |
| **01** | **발표 PPT**<br/>🟢 대외용 | **[대구시 기계로봇과 · KIRIA 협력 제안 16:9 PPT](./2026-11-14_daegu_robot_division_monday_proposal_ppt.html)**<br/>([Word](./2026-11-14_daegu_robot_division_monday_proposal_ppt.docx) \| [MD](./2026-11-14_daegu_robot_division_monday_proposal_ppt.md)) | `2026-11-14` | **월요일 미팅 현장 투사용 12장 풀스크린 슬라이드 쇼**. 정부 사업 중복성 회피용 ‘KIRIA 전문가 매칭+AIDC 전환’ 모델, RFM·훈련데이터(DaaS), `Isaac×Unity` 결합, 로봇·City DT `45PB` 데이터 팩토리 시각화 |
| **02** | **서술형 제안**<br/>🟢 대외용 | **[대구시 기계로봇과 · KIRIA 협력 제안서 (서술형 DOCX형)](./2026-11-14_daegu_robot_division_monday_proposal_narrative.html)**<br/>([Word](./2026-11-14_daegu_robot_division_monday_proposal_narrative.docx) \| [MD](./2026-11-14_daegu_robot_division_monday_proposal_narrative.md)) | `2026-11-14` | **월요일 미팅 배포·정독용 A4 7쪽 Word 문서 형태 뷰어**. 01번 PPT의 모든 아젠다를 공문서·제안서 문체의 완결된 서술형 문장(전 6장)과 정량 산출표로 상세 풀어쓴 문서 |
| **03** | **사내 전략**<br/>🔴 대외비 | **[MZC 사내 전략: 부지·분양, AWS 전환 & 5+5MW 검토서](./2026-11-14_mzc_internal_strategy_land_aws_offload_and_hybrid_10mw.html)**<br/>([Word](./2026-11-14_mzc_internal_strategy_land_aws_offload_and_hybrid_10mw.docx) \| [MD](./2026-11-14_mzc_internal_strategy_land_aws_offload_and_hybrid_10mw.md)) | `2026-11-14` | 수성지구 `4~6천평` 원가 매입(시세 3배) + 지산센터 분양(`+330억`)·오피스 임대 보전, MZC 매출 80% AWS 매입분 중 `10%~25%` 전환 시 손익(`연 +365억 OP`), `5+5MW` 스윙 전략 검증 |
| **04** | **발표 PPT**<br/>🟢 대외용 | **[KIRIA 1차 협력 미팅 발표 장표 (10-Slide Deck)](./2026-11-12_kiria_1st_meeting_presentation_deck.html)**<br/>([Word](./2026-11-12_kiria_1st_meeting_presentation_deck.docx) \| [MD](./2026-11-12_kiria_1st_meeting_presentation_deck.md)) | `2026-11-12` | 한국로봇산업진흥원 임원진 미팅용 10장 슬라이드. 달성(물리 Body) × 수성(AI Brain) Twin-Hub 구도 및 **신규 예정 상위 5대 추천 사업 아이템(추정 사업규모 포함)** 집중 부각 |
| **05** | **회의 요약**<br/>🟢 대외용 | **[KIRIA 1차 협력 미팅 핵심 요약본 (Executive Handout)](./2026-11-12_kiria_1st_meeting_executive_summary.html)**<br/>([Word](./2026-11-12_kiria_1st_meeting_executive_summary.docx) \| [MD](./2026-11-12_kiria_1st_meeting_executive_summary.md)) | `2026-11-12` | 04번 발표장표와 짝을 이루는 회의 테이블 배포용 요약 유인물. Top 5 공동 기획 과제(`5년 1,490~1,930억`), `'27.1H` 클라우드 브릿지 조기 가동 및 실무 TF 안건 수록 |
| **06** | **재무 기준**<br/>🔴 대외비 | **[대구 AIDC 표준 예산 구조 재무 테이블 및 매출퍼즐](./2026-11-12_daegu_aidc_budget_structure_and_revenue_puzzle.html)**<br/>([Word](./2026-11-12_daegu_aidc_budget_structure_and_revenue_puzzle.docx) \| [MD](./2026-11-12_daegu_aidc_budget_structure_and_revenue_puzzle.md)) | `2026-11-12` | 하이브리드(코로케이션 3 : 자체 GPU 2) 기준 **10MW(`3,500억`) / 5MW(`1,750억`) CapEx·OpEx 상세 테이블** 및 대구 5MW 연간 목표 매출(`연 380억` / 5년 `1,900억`) 5대 매출퍼즐 매핑 |
| **07** | **PF · 리스크**<br/>🔴 대외비 | **[비용 역산출, PF 단계별 수익률 및 JB동탄 DC 비교 분석](./2026-11-12_daegu_aidc_reverse_costing_pf_risk_and_jb_dongtan_analysis.html)**<br/>([Word](./2026-11-12_daegu_aidc_reverse_costing_pf_risk_and_jb_dongtan_analysis.docx) \| [MD](./2026-11-12_daegu_aidc_reverse_costing_pf_risk_and_jb_dongtan_analysis.md)) | `2026-11-12` | 부동산 분양사업 유사 관점의 6단계 개발 리스크·목표 IRR 분석, LOI 금융 가치, 구미 앤트로픽 무산 사례 교훈 및 **JB동탄 DC 운영권 심사 논리와의 비교·벤치마킹** |
| **08** | **사업 풀(Pool)**<br/>🟡 기획참조 | **[9대 국책사업 검증 및 5MW 회수 26대 사업 아이디에이션](./2026-11-12_daegu_aidc_kiria_meeting_and_5mw_business_ideation.html)**<br/>([Word](./2026-11-12_daegu_aidc_kiria_meeting_and_5mw_business_ideation.docx) \| [MD](./2026-11-12_daegu_aidc_kiria_meeting_and_5mw_business_ideation.md)) | `2026-11-12` | 대구시 전달 자료(`27면 PDF`) 내 9대 로봇 국책사업 예산 실체 팩트체크(기 확정 vs 신규 예정 구분), 대구TP 88개사 수요 분석 및 **6대 트랙 × 26개 세부 사업 아이템 총람** |
| **09** | **본 제안서**<br/>🟢 대외용 | **[대구 수성 피지컬 AI 로봇 트레이닝 센터 제안서 (V2.1)](./daegu_suseong_robot_training_center_proposal.html)**<br/>([Word](./daegu_suseong_robot_training_center_proposal.docx) \| [MD](./daegu_suseong_robot_training_center_proposal.md)) | `2026-11-12` | 대구광역시 및 산하기관 제출용 **공식 종합 사업제안서 최신판**. 센터 구축 개요, 서비스 구성, 운영 모델 및 제7장 ‘9대 국책사업 연계 Twin-Hub 전략’ 통합 반영 |
| **10** | **기술 상세**<br/>🟢 대외용 | **[대구 피지컬 AI 로봇 트레이닝 센터 구축 제안서 (상세판)](./daegu_physical_ai_robot_training_center_proposal.html)**<br/>([Word](./daegu_physical_ai_robot_training_center_proposal.docx) \| [MD](./daegu_physical_ai_robot_training_center_proposal.md)) | `2026-11-09` | 피지컬 AI 아키텍처 기술 레퍼런스 문서. NVIDIA Omniverse, Isaac Lab, Cosmos 월드모델 기반 합성 데이터 생성 및 VLA 학습 파이프라인 세부 기술 명세 수록 |
| **11** | **선행 조사**<br/>🟢 기초자료 | **[대구 AIDC & 피지컬 AI 선행 조사 보고서](./daegu_aidc_physical_ai_preliminary_study.html)**<br/>([Word](./daegu_aidc_physical_ai_preliminary_study.docx) \| [MD](./daegu_aidc_physical_ai_preliminary_study.md)) | `2026-11-09` | 프로젝트 초기 기초 조사 보고서. 수성알파시티 입지 여건, 전력·통신 인프라 현황, 국내외 로봇 트레이닝 센터 벤치마킹 및 초기 정책 부합성 분석 |

---

## 3. 카테고리별 각 파일 상세 요약

### A. [2026-11-14 신규] 월요일 대구시 기계로봇과 제안 패키지 (대외용 2종)

#### ① `2026-11-14_daegu_robot_division_monday_proposal_ppt` (16:9 발표용 PPT 슬라이드)
- **파일 링크**: [HTML 슬라이드 쇼](./2026-11-14_daegu_robot_division_monday_proposal_ppt.html) | [DOCX](./2026-11-14_daegu_robot_division_monday_proposal_ppt.docx) | [MD](./2026-11-14_daegu_robot_division_monday_proposal_ppt.md)
- **형태 및 기능**: `1600×900` 고정 16:9 비율 자동 스케일링 풀스크린 프레젠테이션 앱 (발표자 노트 `N`, 레이저 포인터 `L`, 회의실 밝은 테마 전환 `T`, 목차 `M`, 전체화면 `F` 지원).
- **핵심 요약**:
  1. **중복성 심사 회피 논리**: 신규 시설 중복 건립이 아니라 기존 국책사업(국가로봇테스트필드·안전인증·R&D)을 **‘KIRIA 1:1 전문가 매칭 + 수성 AIDC 공유자원 활용’**으로 전환해 고도화하는 명분 제시.
  2. **플랫폼 서비스**: 수집 후 정제·표준화(`RLDS/LeRobot`) 기반 **로봇 훈련 데이터 서비스(DaaS)** 및 **한국형 로봇 파운데이션 모델(K-RFM)** 보급.
  3. **듀얼 Sim-to-Real**: 정밀 물리·강화학습(**`NVIDIA Isaac Sim`**)과 CAD 경량화·초실사 비전·군중 HRI·VR 원격조작 및 지역 개발자 흡수(**`Unity`**) 결합.
  4. **통합 데이터 팩토리 정량 설계**: 로봇 대당 쓰루풋(`150~550 Mbps`, `0.5~1.9 TB/일`) 및 대구 City DT 4대 수집 채널(`~65 TB/일`) 산출 기반 **유효용량 `45 PB` 3-Tier 스토리지 + `100~400G` 전용 광망** 아키텍처 제시.

#### ② `2026-11-14_daegu_robot_division_monday_proposal_narrative` (서술형 DOCX 문서 형태)
- **파일 링크**: [HTML Word 문서형 뷰어](./2026-11-14_daegu_robot_division_monday_proposal_narrative.html) | [DOCX](./2026-11-14_daegu_robot_division_monday_proposal_narrative.docx) | [MD](./2026-11-14_daegu_robot_division_monday_proposal_narrative.md)
- **형태 및 기능**: MS Word A4 7페이지 문서와 동일한 레이아웃을 웹 브라우저에서 구현한 서술형 보고서 뷰어 (상단 리본 바, 장별 이동, 글자 크기 조절, A4 인쇄 최적화 탑재).
- **핵심 요약**: ①번 PPT의 개조식 핵심 키워드를 대구시 주무관 및 진흥원 실무자가 회의 후 그대로 공문·기획안 초안으로 인용할 수 있도록 **배경 논리 → 전환 프로세스 → 서비스 구조 → 듀얼 엔진 아키텍처 → 쓰루풋·스토리지 산정 근거 → 단계별 로드맵(전 6장)** 순의 완결된 서술형 문장으로 상세 기술한 문서.

---

### B. [2026-11-14 신규] MZC 사내 전용 투자·수익성·앵커 전략서 (사내 대외비)

#### ③ `2026-11-14_mzc_internal_strategy_land_aws_offload_and_hybrid_10mw`
- **파일 링크**: [HTML 뷰어](./2026-11-14_mzc_internal_strategy_land_aws_offload_and_hybrid_10mw.html) | [DOCX](./2026-11-14_mzc_internal_strategy_land_aws_offload_and_hybrid_10mw.docx) | [MD](./2026-11-14_mzc_internal_strategy_land_aws_offload_and_hybrid_10mw.md)
- **핵심 요약**:
  1. **부지 가치 및 복합개발 수익 보전**: 대구시가 조성원가(`약 180~270억`) 수준에 매각 검토 중인 수성지구 `4,000~6,000평` 부지(시세 약 3배 상승, 평가차익 담보력 확보) 중 동대구역 인접 입지를 살려 **지식산업센터 분양(`순분양익 약 +330억 원`으로 AIDC 초기 CapEx 상쇄)** 및 **R&D 오피스 임대(`연 +40~48억 원` NOI)**를 병행하는 복합개발 모델 검증.
  2. **AWS 매입 컴퓨트 전환 손익 점검**: MZC 전체 매출 중 약 80%를 차지하는 AWS 사업(매출 `약 1.2조 원`, 순수 컴퓨트 원가 `약 5,800억 원` 추정)에서 1/4(`25% = 1,450억 원`)은 약 `9~10MW` 규모에 해당함을 규명. 즉 **AWS 컴퓨트 매입의 단 `10%`만 별도 대구 AIDC 법인으로 오프로딩해도 자체 수요 `5MW`가 즉시 100% 완판**되며, 그룹 연결 영업이익이 **`연간 약 +365억 원` 극대화**됨과 동시에 AWS EDP 할인 협상력 강화 및 해외 네오클라우드·대형 테넌트 유치(‘선 채움 후 고수익 교체’) 레버리지로 작동함을 입증.
  3. **`5MW + 5MW` 스윙 구조 & `45PB` 스토리지 사업성**: 대구 공공·로봇 수요 부족 시 MZC 자체 물량을 `6~7MW`로 탄력 확대하는 무공실 안전판과, `45PB` 데이터 팩토리 추가 투자(`약 200억 원`)를 통한 연간 `65~95억 원` 고마진 DaaS 부가수익 구조 제시.

---

### C. [2026-11-12 구축] KIRIA 미팅 패키지 · 예산/PF 분석 · 26대 사업 풀 (5종)

#### ④ `2026-11-12_kiria_1st_meeting_presentation_deck` (KIRIA 1차 미팅 10장 발표장표)
- **파일 링크**: [HTML 슬라이드](./2026-11-12_kiria_1st_meeting_presentation_deck.html) | [DOCX](./2026-11-12_kiria_1st_meeting_presentation_deck.docx) | [MD](./2026-11-12_kiria_1st_meeting_presentation_deck.md)
- **핵심 요약**: KIRIA 원장단·본부장급 미팅을 겨냥해 기 확정 사업을 제외한 **신규 예정 상위 5대 추천 아이템**(① 테스트필드 데이터 레이크 `220~280억`, ② 휴머노이드 가상 안전인증 `120~150억`, ③ 특화단지 통합 원격관제 `200~250억`, ④ 5극3특 K-RFM & R&D GPU 의무할당 `600~800억`, ⑤ 수출형 로봇 글로벌 OTA 브릿지 `350~450억` — **5년 합계 `1,490~1,930억 원`**)을 제안하는 10장 발표덱.

#### ⑤ `2026-11-12_kiria_1st_meeting_executive_summary` (KIRIA 미팅 핵심 요약 핸드아웃)
- **파일 링크**: [HTML 뷰어](./2026-11-12_kiria_1st_meeting_executive_summary.html) | [DOCX](./2026-11-12_kiria_1st_meeting_executive_summary.docx) | [MD](./2026-11-12_kiria_1st_meeting_executive_summary.md)
- **핵심 요약**: ④번 발표장표의 핵심 표(상위 5대 아이템 및 추정 사업규모, 중소 로봇기업 4대 애로 해소 효과, `'27년 상반기` 임대형 클라우드 브릿지 조기 착수안)만 압축한 대외 배포용 요약서.

#### ⑥ `2026-11-12_daegu_aidc_budget_structure_and_revenue_puzzle` (표준 예산 및 매출퍼즐 기준서)
- **파일 링크**: [HTML 뷰어](./2026-11-12_daegu_aidc_budget_structure_and_revenue_puzzle.html) | [DOCX](./2026-11-12_daegu_aidc_budget_structure_and_revenue_puzzle.docx) | [MD](./2026-11-12_daegu_aidc_budget_structure_and_revenue_puzzle.md)
- **핵심 요약**: 부지·토목건축·MEP 수전/액침냉각·컴퓨트(GPU/네트워크)·연간 OpEx 항목별로 **10MW(`3,500억 원`) 및 5MW(`1,750억 원`) 표준 예산 테이블**을 정립하고, 대구 5MW 타깃 연간 `380억 원`(5년 `1,900억 원`) 회수를 위한 5개 트랙별 전력(MW)·매출 퍼즐을 수치로 매핑한 재무 기준서.

#### ⑦ `2026-11-12_daegu_aidc_reverse_costing_pf_risk_and_jb_dongtan_analysis` (PF 리스크·수익률 & 동탄 비교)
- **파일 링크**: [HTML 뷰어](./2026-11-12_daegu_aidc_reverse_costing_pf_risk_and_jb_dongtan_analysis.html) | [DOCX](./2026-11-12_daegu_aidc_reverse_costing_pf_risk_and_jb_dongtan_analysis.docx) | [MD](./2026-11-12_daegu_aidc_reverse_costing_pf_risk_and_jb_dongtan_analysis.md)
- **핵심 요약**: 일반 아파트·지식산업센터 개발사업과 유사한 AIDC 개발 6단계(토지→인허가/수전→착공PF→MEP→선임대→운영)별 리스크 프리미엄 및 기대 IRR(`22%+ → 7~9%`)을 산정하여 최적 진입 시점을 도출하고, 구미 앤트로픽 취소 교훈 및 **JB동탄 DC 금융권 심사 대응 논리**를 비교 분석한 내부 심화 보고서.

#### ⑧ `2026-11-12_daegu_aidc_kiria_meeting_and_5mw_business_ideation` (9대 국책사업 검증 & 26대 사업 총람)
- **파일 링크**: [HTML 뷰어](./2026-11-12_daegu_aidc_kiria_meeting_and_5mw_business_ideation.html) | [DOCX](./2026-11-12_daegu_aidc_kiria_meeting_and_5mw_business_ideation.docx) | [MD](./2026-11-12_daegu_aidc_kiria_meeting_and_5mw_business_ideation.md)
- **핵심 요약**: 대구시 기계로봇과 공유 PDF(27면) 내 9대 로봇 국책사업 각각의 예산 구조와 컨소시엄 확정 여부를 정밀 검증하고, 수성 AIDC 5MW를 채울 수 있는 **6대 분야 총 26개 신규 사업 아이디어 풀(백과사전)**을 집대성한 기획 원천 문서.

---

### D. 기본 본 제안서 및 기초 기술·선행조사 문서 (3종)

#### ⑨ `daegu_suseong_robot_training_center_proposal` (통합 본 제안서 V2.1)
- **파일 링크**: [HTML 뷰어](./daegu_suseong_robot_training_center_proposal.html) | [DOCX](./daegu_suseong_robot_training_center_proposal.docx) | [MD](./daegu_suseong_robot_training_center_proposal.md)
- **핵심 요약**: 대구시 및 유관기관 제출용 공식 통합 제안서 최신판으로, 수성알파시티 입지 강점, 센터 구축·운영 아키텍처 및 제7장(9대 국책사업 연계 Twin-Hub 전략)까지 포괄 수록.

#### ⑩ `daegu_physical_ai_robot_training_center_proposal` (피지컬 AI 기술 상세 제안서)
- **파일 링크**: [HTML 뷰어](./daegu_physical_ai_robot_training_center_proposal.html) | [DOCX](./daegu_physical_ai_robot_training_center_proposal.docx) | [MD](./daegu_physical_ai_robot_training_center_proposal.md)
- **핵심 요약**: NVIDIA Omniverse / Isaac Lab / Cosmos 기반 피지컬 AI 모델 학습 파이프라인, 하드웨어 클러스터 사양 및 MLOps 기술 구성을 심층 서술한 기술 레퍼런스 문서.

#### ⑪ `daegu_aidc_physical_ai_preliminary_study` (초기 선행 조사 보고서)
- **파일 링크**: [HTML 뷰어](./daegu_aidc_physical_ai_preliminary_study.html) | [DOCX](./daegu_aidc_physical_ai_preliminary_study.docx) | [MD](./daegu_aidc_physical_ai_preliminary_study.md)
- **핵심 요약**: 대구 수성알파시티 AIDC 추진 배경, 국내외 피지컬 AI 로봇 트레이닝 센터 구축 동향 및 초기 정책·시장 타당성을 정리한 기초 리서치 자료.

---

## 4. 연관 작업계획서(Plans) · 변경명세서(Specs) · 상위 README 링크

- **상위 워크스페이스 통합 README**: [docs/akamai_ncp/README.html](../README.html) ([MD](../README.md) | [DOCX](../README.docx))
- **2026-11-14 작업계획서 (Plan)**: [2026-11-14_daegu_robot_division_ppt_and_internal_strategy_plan.html](../../plans/2026-11-14_daegu_robot_division_ppt_and_internal_strategy_plan.html) ([MD](../../plans/2026-11-14_daegu_robot_division_ppt_and_internal_strategy_plan.md) | [DOCX](../../plans/2026-11-14_daegu_robot_division_ppt_and_internal_strategy_plan.docx))
- **2026-11-14 상세변경명세서 (Spec)**: [2026-11-14_daegu_robot_division_ppt_and_internal_strategy_spec.html](../../specs/2026-11-14_daegu_robot_division_ppt_and_internal_strategy_spec.html) ([MD](../../specs/2026-11-14_daegu_robot_division_ppt_and_internal_strategy_spec.md) | [DOCX](../../specs/2026-11-14_daegu_robot_division_ppt_and_internal_strategy_spec.docx))
