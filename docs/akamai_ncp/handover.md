# 프로젝트 핸드오버 문서 (인수인계서)

- **작성일**: 2026년 8월 11일
- **프로젝트명**: AKAMAI & NVIDIA & MZC 한국형 GPUaaS 공동 사업 기획 및 타당성(Feasibility) 검토

본 문서는 프로젝트의 현 상태와 금일 달성한 주요 성과, 그리고 향후 이어서 진행해야 하는 과제를 다음 담당 에이전트 및 팀원에게 인수인계하기 위해 작성되었습니다.

---

## 1. 오늘 달성한 주요 성과 요약 (Accomplished Today)

금일 작업 세션을 통해 한국 내 GPU 공급 제약을 극복하고 가격 경쟁력을 확보하기 위한 3사 공동 사업 기획의 핵심 초안과 재무 시뮬레이션을 완료하고, 가시성 높은 프리미엄 대시보드를 생성하여 깃허브 원격에 저장 완료했습니다.

### 1) 깃/깃허브 연동 및 저장소 초기 구조 수립
- 로컬 Git 저장소 초기화 및 GitHub 원격 레포지토리 [kesperinc/akamai_ncp](https://github.com/kesperinc/akamai_ncp) (Private) 연동 성공.
- 기획 규칙 파일(`.agents/AGENTS.md`), 개발 가이드(`CLAUDE.md`), 최상위 소개글(`README.md`) 등 프로젝트 핵심 기틀 파일 생성 및 최초 푸시 완료.

### 2) 기술 협력 및 시장 경쟁력 분석 완료
- **아카마이-엔비디아 협력 분석** (`docs/research/akamai_nvidia_partnership.md`):
  - Blackwell GPU 분산 엣지 AI 추론 아키텍처 분석.
  - **Akamai Guardicore Segmentation**과 **NVIDIA BlueField-4 STX DPU**의 결합으로 성능 저하 없는 제로 트러스트 보안 인프라 기술 조사.
- **시장성 및 7개사 단가 비교** (`docs/research/nvidia_ncp_market_analysis.md`):
  - NVIDIA NCP(Nvidia Cloud Partner) 프로그램 생태계 분석.
  - 글로벌/국내 7대사(NCP/Neo-Clouds, AKAMAI, AWS, GCP, AZURE, Naver Cloud, NHN Cloud)의 H100, L40S, A100 GPU 인스턴스 시간당 단가 및 기가바이트(GB)당 Egress 비용 정량 비교표 수립.
  - Akamai Connected Cloud의 초저가 Egress 요금($0.005/GB)이 하이퍼스케일러 및 국내 CSP(GB당 90~130원대) 대비 16배 이상 저렴하여 분산 추론 환경에서 막강한 TCO 이점을 가짐을 수치화하여 규명.

### 3) 한국형 하이브리드 비즈니스 모델 설계
- **MZC-아카마이 공동 사업 제안서** (`docs/proposal/mzc_akamai_partnership.md`):
  - 국내 GPU 수급 대기 시간(Lead-time)을 줄이기 위해, MZC가 확보한 하드웨어를 아카마이가 일시 매입(CapEx 110억 원 규모)하여 한국 내 Tier 3 IDC 노드로 편입.
  - 물리 장비 운영 및 로컬 기술 지원/총판 영업권을 MZC에 위탁. MZC에게는 고정 위탁 수수료 및 **발생 매출의 20%를 파트너 수수료로 배분(Revenue Share)**하여 영업 시너지를 극대화하는 하이브리드 구조 설계.
  - 운영(Ops) 엔지니어 4명 및 세일즈 아키텍트 3명 등 총 7명 규모의 구체적 투입 인력 명시.

### 4) 정량적 재무 및 BEP 시뮬레이션 모델 구축
- **시뮬레이션 개발** (`scripts/bep_simulation.py`):
  - 3개년 감가상각(CapEx 110억, 5년 정액법) 및 현금성 OpEx(연 10.2억), MZC 수수료 변수를 연동하여 손익분기 가동률을 계산하는 파이썬 코드 작성.
  - Matplotlib 및 `koreanize-matplotlib`를 사용하여 한글 폰트가 적용된 BEP 분석 그래프(`docs/feasibility/bep_chart.png`) 자동 생성.
- **재무 분석 보고서** (`docs/feasibility/financial_simulation_report.md`):
  - **회계적 영업이익 BEP 가동률: 75.54%** (연간 감가상각비 22억 원 반영 시)
  - **현금흐름(EBITDA) BEP 가동률: 23.93%** (감가상각비를 제외한 실제 현금흐름 흑자 전환선. GPU 엣지 인프라의 약 24%만 판매해도 영업 유지비 적자 리스크 완전 해소.)
  - 가동률 80% 안착 시 약 4.6년, 90% 안착 시 약 3.9년의 짧은 CapEx 투자금 회수(ROI) 기간 도출.

### 5) 프리미엄 대시보드 및 일괄 HTML 변환 빌더 개발
- **HTML 대시보드 생성** (`docs/feasibility/financial_simulation_report.html`):
  - 시뮬레이션 원시 데이터 표 및 BEP 그래프 이미지(`bep_chart.png`를 Base64 Data URI로 인라인 인코딩)를 단일 파일 내에 임베딩.
  - Dark Mode, Glassmorphism, Noto Sans KR/Outfit 웹 폰트 및 Hover 애니메이션을 결합해 프리미엄 퀄리티의 UI 대시보드 리포트로 빌드 (`scripts/build_html_report.py`).
- **일괄 변환기 개발** (`scripts/convert_all_md.py`):
  - 프로젝트 내 모든 주요 마크다운 문서들(README, 리서치 보고서, 공동 사업 제안서)을 파이썬 마크다운 엔진과 프리미엄 CSS 스타일 템플릿을 결합하여 HTML 파일들로 일괄 변환 완료.

### 6) HTML ➡ Word(DOCX) 일괄 변환 및 자동 동기화 연동
- **HTML ➡ DOCX 변환기 개발** (`scripts/convert_html_to_docx.py`):
  - `docs` 폴더 내에 저장된 HTML 보고서를 Word(`.docx`) 문서로 일괄 변환하는 전용 스크립트를 신규 개발했습니다.
  - HTML 내의 복잡한 CSS 테마 스타일이 깨지거나 변환오류가 생기는 문제를 방지하고자, BeautifulSoup4를 활용하여 HTML의 본문 알맹이(`report-card` 또는 `body` 영역)만 깨끗이 추출하여 Word 형식에 맞춤 삽입 및 빌드하도록 설계했습니다.
- **빌드 연동 및 이중 저장 자동화 강화**:
  - `convert_all_md.py` 및 `build_html_report.py` 빌드 과정의 마지막 완료 단계에 DOCX 변환 모듈을 자동으로 트리거하도록 연동했습니다.
  - 이에 따라 마크다운을 업데이트하면 **Markdown ➡ HTML ➡ DOCX**의 3단계 문서 포맷이 원클릭으로 완벽하게 최신 상태로 동기화(이중 저장 및 추가 DOCX 변환)되도록 안전장치를 수립했습니다.
  - `docs` 폴더 하위의 HTML 문서들에 대칭되는 `.docx` 문서 파일들을 모두 생성 및 동기화 완료했습니다.

### 7) CortexOS 가드레일 및 이중 저장 규칙 수립
- **[.agents/AGENTS.md](file:///c:/dev/antigravity-workspace/akamai_ncp/.agents/AGENTS.md)**에 **이중 저장 정책 (MD & HTML 동시 저장)** 가드레일을 추가하여, 에이전트가 마크다운을 갱신할 때마다 빌드 스크립트를 재실행해 HTML 산출물이 완벽히 동기화되도록 안전장치를 수립하고 `CLAUDE.md`에도 이중 저장 정책 및 실행 명령어를 동기화 완료.

### 8) 원익로보틱스 AX Center (피지컬 AI 로봇 트레이닝 센터) 제안 및 RFI 비교 분석 완료
- **원익로보틱스 맞춤형 AX Center 구축 제안서** (`docs/wonik_ax_center/wonik_robotics_ax_center_proposal.md`):
  - 메가존클라우드(MZC) & 메이머스트(Maymust) 연합 기반 H200 400장 규모의 피지컬 AI 로봇 트레이닝 센터 및 AIDC 구축/운영 전략 수립.
  - 트랙 A(데이터센터 인프라) - B(컴퓨트/플랫폼) - C(데이터 파이프라인/Isaac Sim 가상 트레이닝) 전 주기 턴키 제안.
- **RFI v1.2 vs v1.7 변경점 심층 비교 분석** (`docs/wonik_ax_center/wonik_rfi_v12_vs_v17_comparison.md`):
  - RFI 최신 개정판(v1.7)의 실질적 변경 요건 분석 및 질의(Q&A) 대응 전략 문서화.
- **팀 합의 및 산출물 정비** (`docs/wonik_ax_center/scratch/teamwork_review_consensus.md`):
  - 크로스 팀 리뷰 컨센서스 도출 및 디렉토리 구조 최적화(`docs/wonik_ax_center/` 전용 분리, 구버전은 `docs/proposal/archive/`로 이동).

### 9) 대구 수성알파시티 피지컬 AI 로봇 트레이닝 센터 제안서 수립
- **대구 수성알파시티 제안서** (`docs/proposal/daegu_suseong_robot_training_center_proposal.md` / `daegu_physical_ai_robot_training_center_proposal.md`):
  - 대구 AIDC 및 수성알파시티 거점 피지컬 AI 로봇 훈련/검증 센터 구축 제안 완성.
  - Akamai 분산 엣지 추론망과의 하이브리드 연계 모델 제시.

### 10) OpenUSD 표준 기술 정의 및 각주 스타일 엔진 고도화
- **선행 연구 보고서 OpenUSD 표준 용어 보강** (`docs/research/daegu_aidc_physical_ai_preliminary_study.md`):
  - Pixar/NVIDIA 주도의 OpenUSD(Universal Scene Description) 표준 정의 및 NVIDIA Omniverse/Isaac Sim 데이터 파이프라인(CAD Ingestion/Tessellation) 해설 각주 추가.
- **마크다운 변환 엔진 내 각주(Footnotes) 확장 기능 및 전용 CSS 스타일링 반영** (`scripts/convert_all_md.py`).

### 11) ISV BU Hybrid Cloud 팀 마스터 방향성, 영업 퍼널(%)·MPN 판매채널화 및 7인 멤버별 R&R 통합 제안서 (v3.2) 수립
- **통합 전략 제안서 구축** (`docs/proposal/HYBRID_CLOUD_TEAM_STRATEGY_MASTER_INTEGRATED.md` / `.html` / `.docx`):
  - 7인 코어 멤버(김성호, 최재규, 안재우, 이성표, 장필성, 박경률[박경륜], 최성호) + 협업 라인의 역할 분담(R&R 카드 및 RACI 매트릭스) 확정.
  - 6대 비즈니스 파트 균형 요약 및 22개 전체 영업기회(Opty)에 대한 5단계 영업 퍼널(Sales Funnel)·추정 진행률(`10% ~ 90%`) 정량 진단 반영 (대구 AIDC `55%`, KG ICT `50%`, 현대로템 `50%` 등 사업제안 단계 반영).
  - MPN(메가존 파트너 네트워크)을 양방향 전략 판매채널(Sell-Through)로 활용하고, 수시로 개최되는 `MPN C-Level 미팅`을 레버리지하여 Top-Down 공동 영업 기회(Give & Take)를 창출하는 실행 전략 수립.

---

## 2. 현재 저장소 및 자산 상태 (Current Status)

- **Git 상태**: 원익로보틱스 AX Center 및 대구 수성알파시티 피지컬 AI 로봇 트레이닝 센터 제안서, RFI 비교 분석 보고서, OpenUSD 각주 보강 및 모든 MD ➡ HTML ➡ DOCX 동기화 완료 후 GitHub 원격 커밋 및 푸시 대기 상태.
- **문서 포맷 동기화**: 모든 산출물이 Markdown(.md), 프리미엄 테마 HTML(.html), 실무용 워드(.docx) 3종 세트로 완전 동기화 보존됨.


---

## 3. 다음 단계에서 수행해야 할 과제 (Next Actions)

이후 교대하는 작업자나 에이전트는 기 수립된 가이드라인과 재무 모델을 기반으로 다음 단계를 보완하는 기획을 수행해야 합니다.

1. **국내 1차 타겟 고객 확보(Landing) 시나리오 구체화**
   - MZC의 기존 한국 내 클라우드 고객망 중 대형 모델 파인튜닝 연구소, 실시간 의료 AI 진단 솔루션 기업 등 1차로 아카마이 GPUaaS로 마이그레이션이 유력한 타겟 고객사 3~5개를 가상 선정하여, 이들의 실제 마이그레이션 시나리오 및 비용 절감률을 시뮬레이션합니다.
2. **한국 내 고전력 IDC 물리적 입지 선정 및 코로케이션 비용 실사**
   - 가산, 상암, 가양 등 서울/경인권의 Tier 3 IDC 중 랙당 15kW~20kW 고전력 공급이 가능하고 아카마이 PoP망과 다이렉트로 연동할 수 있는 물리적 데이터센터 입지 후보를 도출하고 예상 임차비용을 구체화합니다.
3. **NVIDIA NIM/Triton 구동 최적화를 위한 LKE 성능 PoC(기술 실증) 계획 수립**
   - 아카마이 Connected Cloud의 Linode Kubernetes Engine(LKE) 상에 NVIDIA AI Enterprise 스택을 최적화하기 위한 기술 검증용 PoC 환경 구성안과 벤치마크 테스트 항목을 설계합니다.
4. **국내 데이터 컴플라이언스 법규(망분리, 개인정보보호법) 타당성 검증**
   - 금융/공공 등 특정 분야에서 요구하는 국내 망분리 요건 및 개인정보 전송 제한 법률을 준수하면서 분산 GPUaaS를 제공하기 위한 보안 물리적 격리 방안을 명문화합니다.
