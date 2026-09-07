# [명세서] Nota.ai 솔루션 종합 분석 및 On-Premises AI Full Stack 전략적 포지셔닝 보고서

- **문서 번호**: SPEC-20260907-NOTA-ONPREM-01
- **작성 일자**: 2026-09-07
- **보고 형식**: 두괄식 경영전략 보고서 (Executive-First Structure)
- **작성자**: MZC AI Full Stack 전략추진 및 ISV 솔루션 아키텍처 팀
- **대상 파일**:
  - `offering/2026-09-07_nota_ai_comprehensive_solution_analysis_and_fullstack_positioning_report.html` (두괄식 웹 대시보드)
  - `offering/generate_nota_comprehensive_report_docx.py` (두괄식 DOCX 공식 생성기)
  - `offering/docx/2026-09-07_Nota_AI_Comprehensive_Fullstack_Positioning_Report.docx` (공식 Word 문서)
  - `docs/2026-09-07_Nota_AI_Comprehensive_Fullstack_Positioning_Report.docx` (루트 docs 동기화 문서)
  - `docs/specs/2026-09-07_nota_ai_comprehensive_solution_analysis_spec.md` (본 상세 명세서)

---

## 1. 보고서 구조 및 두괄식 재구성 원칙

본 보고서는 C-레벨 및 경영진 대상 보고를 위해 **두괄식(Executive-First) 구조**로 전면 개편되었습니다:
1. **서론(제 1 장)**: MZC AI Full Stack의 4대 기본 계층을 명시하고, 온프레미스 실구축 시 직면하는 **4대 치명적 Missing Link(결손 고리)**를 명확히 정의.
2. **핵심 제언 1(제 2 장)**: Missing Link를 단번에 해결하는 온프레미스 AI Full Stack 구축 시 6대 압도적 강점 전진 배치 (Capex 75% 절감, 랙 소비전력 3.2kW 급감 등).
3. **핵심 제언 2(제 3 장)**: MZC On-Prem AI Full Stack x Nota 4대 턴키 패키지를 **[서버 AI 인프라 주력 2종]**과 **[Physical/Edge AI 시장 탐색 2종]**으로 명확히 이원화하여 전진 배치.
4. **결론(제 4 장)**: 비즈니스 라이선스 모델, 사내 랩 실측 3단계 실행 로드맵 및 최종 핵심 전략 파트너 격상 확정 선언.
5. **부록 및 참고자료 (Appendix)**: 상세 기술적 원리(PASCAL-MoE, 비균일 프루닝), 원천 벤치마크 데이터 시트(Solar 250B, Kimi 2.8T, VLM/VLA, ITS) 및 참고 문헌은 부록 1~5로 후진 배치하여 보고서 가독성을 극대화.

---

## 2. MZC AI Full Stack 레이어 및 On-Prem 구축의 4대 Missing Link

### 2.1 AI Full Stack 표준 4대 레이어
- **Layer 01. 하드웨어 인프라**: Dell PowerEdge R760, Cisco, NVIDIA GPU 및 국산 NPU 서버
- **Layer 02. 플랫폼 & 오케스트레이션**: Red Hat OpenShift AI (RHOAI), Nutanix AHV/Kubernetes
- **Layer 03. 모델 최적화 & 서빙**: vLLM, Triton, KServe 및 **NetsPresso 최적화 엔진 (Missing Link 해결 핵심)**
- **Layer 04. 비즈니스 AI 애플리케이션**: 사내 폐쇄망 RAG, 프라이빗 코딩 에이전트, 산업별 특화 관제

### 2.2 On-Premises 실도입 시 4대 Missing Link (결손 고리)
1. **Missing Link 1 (천문학적 GPU 서버 Capex & 조달 납기)**: 250B 파운데이션 MoE 모델 서빙 시 대당 5~6억 원 고가 H100 8-GPU 서버 1~2대 필수 ➔ Nota INT4 도입으로 단일 2-GPU 서버(약 1.5억 원) 서빙 달성 (**Capex 75% 절감**).
2. **Missing Link 2 (전산실 랙 전력 10kW 한계 초과)**: 8-GPU 서버 피크 소비전력 10.2kW로 랙 한계(10kW) 초과 ➔ Nota 2-GPU 구성 시 **3.2kW로 급감**, 전산실 증설 공사 불필요.
3. **Missing Link 3 (국산 NPU 소프트웨어 컴파일러 부재)**: 외산 락인 탈피를 위한 국산 NPU 도입 시 컴파일러 부재 ➔ NetsPresso NPU 자동 컴파일러 및 연산자 치환 **100% 호환 보장**.
4. **Missing Link 4 (완전 폐쇄망 소버린 보안 완결성)**: 금융/방산 폐쇄망에 Appliance 형태로 탑재되어 외부 유출 위험 0% 실현.

---

## 3. MZC On-Prem AI Full Stack x Nota 4대 턴키 솔루션 패키지 (이원화 체계)

### [파트 A. 핵심 주력] 엔터프라이즈 서버 AI 인프라 솔루션 (MZC 핵심 역량 연계)
| 패키지명 | 타깃 고객군 | 하드웨어 인프라 구성 | 소프트웨어 스택 | 핵심 셀링 포인트 |
| :--- | :--- | :--- | :--- | :--- |
| **1. 소버린 MoE 온프레미스 패키지** | 금융, 공공, 그룹사 폐쇄망 RAG/에이전트 | Dell PowerEdge R760 (2x H100 NVL) + Nutanix | NetsPresso INT4/NVFP4 + vLLM 초저지연 서빙 | 8-GPU 대비 Capex 75% 절감, 랙전력 3.2kW, 단일 2U 서버 60+ TPS |
| **2. 소버린 NPU 데이터센터 패키지** | 공공 클라우드, 국가 R&D, 소버린 AI 인프라 | 리벨리온 ATOM / 딥엑스 M1 / 모빌린트 NPU 서버 | NetsPresso NPU 자동 컴파일러 + 연산자 치환 | 국산 NPU 소프트웨어 호환성 100% 보장, TCO 60% 절감, 외산 락인 탈피 |

### [파트 B. 시장 탐색 및 확장 옵션] Physical AI & Edge AI 솔루션 (파트너십 레버리지 탐색형)
*전략적 배경: MZC의 엔터프라이즈 역량이 아직 Embedded/Edge/Physical AI 분야에서는 성숙 전 단계이므로, 무리한 직접 투자보다는 Nota의 글로벌 검증 기술력(두바이 RTA, 대전시, 로보틱스 VLA)을 전면에 세워 수요를 발굴하는 전략적 시장 탐색(Market Exploration) 오퍼링으로 관리.*

| 패키지명 | 타깃 고객군 | 하드웨어 인프라 구성 | 소프트웨어 스택 | 전략적 시장 탐색 포인트 |
| :--- | :--- | :--- | :--- | :--- |
| **3. 스마트팩토리 & Physical AI 패키지** | 제조 공정 불량 검출, 작업장 안전, 로봇(VLA) 도입 희망 스마트공장 | Advantech / NVIDIA Jetson 엣지 박스 + R760 | NetsPresso 엣지 비전(INT8) + SmolVLA 로봇 제어 | 30FPS 현장 결함 판정 및 로봇 조작 성공률 +4.6% 향상을 바탕으로 제조 시장 기회 탐색 |
| **4. 스마트시티 ITS 턴키 패키지** | 지자체, 교통관제센터, 항만 자율주행 인프라 | 도로변 엣지 AI 관제 제어기 + 지자체 관제 서버 | Nota ITS 스마트교차로 + VLM 돌발검지 + V2X | 대전(200개)/두바이 RTA 검증 레퍼런스를 앞세워 공공 스마트 인프라 사업 타당성 타진 |

---

## 4. 부록 및 참고 문헌 구성 (Appendix)

- **부록 1**: Nota.ai 기업 개요 및 글로벌 사업 위상 (15B 스타게이트 유일 참여, 미국/독일/UAE 거점)
- **부록 2**: NetsPresso 차세대 MoE 최적화 상세 원리 및 벤치마크 데이터 시트 (Solar 250B, Solar 100B, Kimi 2.8T)
- **부록 3**: On-Device / Multimodal & 엣지/임베디드 실측 데이터 (Qualcomm IQ-9075, RTX 3090 SmolVLA, ASR 61배 가속)
- **부록 4**: 독자 버티컬 솔루션 Nota ITS 상세 분석 (대전 200개소, UAE 두바이 RTA VLM 계약, V2X)
- **부록 5**: 참고 문헌 및 공식 전달 기술 자료 출처 목록 (PDF 5종 및 국내외 언론 보도 3종)

---

## 5. 생성 및 변경 파일 맵 (Specs Map)

| 구분 | 파일 경로 | 형태 | 설명 |
| :--- | :--- | :--- | :--- |
| **보고서 (HTML)** | `offering/2026-09-07_nota_ai_comprehensive_solution_analysis_and_fullstack_positioning_report.html` | 전면 개편 | 두괄식 구조, Missing Link 그리드, Chart.js, 부록 분리 웹 대시보드 |
| **생성기 (Python)** | `offering/generate_nota_comprehensive_report_docx.py` | 전면 개편 | 두괄식 경영보고서 및 부록 5종 자동 생성기 |
| **보고서 (DOCX)** | `offering/docx/2026-09-07_Nota_AI_Comprehensive_Fullstack_Positioning_Report.docx` | 전면 개편 | 공식 Word 문서 (44.0 KB) |
| **동기화 (DOCX)** | `docs/2026-09-07_Nota_AI_Comprehensive_Fullstack_Positioning_Report.docx` | 전면 개편 | docs 루트 동기화 Word 문서 (44.0 KB) |
| **명세서 (Markdown)**| `docs/specs/2026-09-07_nota_ai_comprehensive_solution_analysis_spec.md` | 현행화 | 본 상세 명세서 (AGENTS.md 규칙 5, 15, 16 준수) |
