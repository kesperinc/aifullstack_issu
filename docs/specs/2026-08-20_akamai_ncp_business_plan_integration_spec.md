# [명세서] AKAMAI & NVIDIA & MZC 한국형 GPUaaS 공동 사업 계획 이관 및 통합 명세서

- **문서 번호**: SPEC-20260820-AKAMAI-NCP-01
- **작성 일자**: 2026년 08월 20일
- **작성 조직**: MZC AI Full Stack 아키텍처 및 ISSU 솔루션 세일즈 팀
- **이관 출처**: `C:\dev\antigravity-workspace\akamai_ncp`
- **대상 파일**:
  - `offering/akamai_ncp/` (AKAMAI NCP 포털 및 웹 보고서 5종)
  - `docs/akamai_ncp/` (루트 문서 및 스크립트 보존)
  - `offering/docx/` (공식 Word DOCX 4종 이관 및 일자 접두사 표준화)
  - `offering/index.html` (마스터 인덱스 허브 포털 통합)

---

## 1. 사업 추진 배경 및 삼사 파트너십 구조

1. **사업 추진 배경**:
   - 국내 GPU 하드웨어 도입 리드타임 지연 극복 및 CSP(AWS, GCP, Azure)의 과도한 Egress 비용(데이터 전송료) 장벽 해소.
   - 엣지 분산 AI 추론 수요 급증에 대응하는 한국형 고성능·저비용 GPUaaS 제공.
2. **AKAMAI - NVIDIA - MZC 3자 역할 분담**:
   - **AKAMAI**: MZC 기 확보 GPU 장비 CapEx 매입, 한국 내 코로케이션 IDC 구축 및 초저가 요금제(H100 $2.50/hr, L40S $1.10/hr, Egress $0.005/GB) 제공.
   - **NVIDIA**: NVIDIA Cloud Partner (NCP) 인증, DGX Cloud 레퍼런스 아키텍처 및 NIM/Triton 소프트웨어 스택 지원.
   - **MZC**: GPU 하드웨어 자산 공급, 한국 내 24/7 위탁 운영(Ops), 엔터프라이즈/스타트업 대상 총판 영업 및 기술 컨설팅 전담.

---

## 2. 통합 이관 산출물 맵

### 1) 인터랙티브 웹 포털 및 보고서군 (`offering/akamai_ncp/`)
* **종합 사업 포털**: `offering/akamai_ncp/README.html`
* **공동 사업 제안서 웹**: `offering/akamai_ncp/proposal/mzc_akamai_partnership.html`
* **재무 타당성 및 BEP 보고서 웹**: `offering/akamai_ncp/feasibility/financial_simulation_report.html` (가동률 60% 시 14개월 BEP 및 연간 40~60억 이익)
* **Akamai-NVIDIA 협력 분석 웹**: `offering/akamai_ncp/research/akamai_nvidia_partnership.html`
* **NCP 시장 경쟁 분석 웹**: `offering/akamai_ncp/research/nvidia_ncp_market_analysis.html`
* **인수인계 보고서**: `offering/akamai_ncp/handover.html`

### 2) 공식 Word 문서 (`offering/docx/` 및 `docs/`)
1. `2026-08-20_MZC_Akamai_GPUaaS_Partnership_Proposal.docx` (38.3 KB)
2. `2026-08-20_Akamai_NCP_Financial_BEP_Simulation_Report.docx` (38.1 KB)
3. `2026-08-20_Akamai_NVIDIA_Partnership_Research.docx` (38.0 KB)
4. `2026-08-20_NVIDIA_NCP_Market_Analysis.docx` (39.0 KB)

---

## 3. 검증 결과
- 마스터 인덱스(`offering/index.html`)에 전용 카드 및 원클릭 웹/DOCX 5개 링크 등록 완료.
- 전체 공식 Word 제안서 킷이 **총 17종**으로 확장 완료.
