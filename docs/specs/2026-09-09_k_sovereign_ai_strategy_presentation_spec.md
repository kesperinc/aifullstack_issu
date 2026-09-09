# 📋 [명세서] UCLA Anderson Executive MBA 내방 세션용 Sovereign AI 전략 발표자료 수립 상세 명세서

- **문서 번호**: SPEC-20260909-UCLA-SOVEREIGN-AI-01
- **작성 일자**: 2026-09-09
- **발표 일자**: 2026-09-11 (금) 10:00 ~ 11:30 AM KST
- **작성자**: MZC ISSU AI Full Stack Architecture & Solution Sales Team
- **발표자**: Andy (ISV Business Unit & AI Architecture Group, MegazoneCloud)
- **대상 청중**: UCLA Anderson Executive MBA (EMBA 44명 + 교수/스태프 6명, 총 50명)
- **세션 주제**: "Korea Sovereign AI Strategy" (영어 발표, 약 15분 발표 + Q&A)
- **산출물 폴더**: `c:\dev\antigravity-workspace\aifullstack\K-AI\`
- **적용 규칙**: [AGENTS.md](file:///c:/dev/antigravity-workspace/aifullstack/AGENTS.md) 16대 필수 개발 및 운영 규칙 준수

---

## 1. 추진 배경 및 청중 분석

### 1.1 내방 행사 개요
- **행사명**: UCLA Anderson Executive MBA Seoul Immersion - MegazoneCloud Visit Program
- **일시**: 2026년 9월 11일(금) 10:00 ~ 11:30 KST (90분 본 세션 + 20분 사옥 투어)
- **장소**: 메가존클라우드 과천 본사 2층 그랜드 컨퍼런스룸
- **세션 구성**:
  1. Company Overview (Doug 대표)
  2. Enterprise AI & Digital Transformation (AIR / AI Architect Unit)
  3. **Korea Sovereign AI Strategy (ISV Business Unit / Andy 발표자)**

### 1.2 청중 특성 및 전략적 연계 포인트
- **청중**: 글로벌 대기업/투자사 시니어 리더 및 경영진 (EMBA 44명)
- **핵심 관심사**:
  - 한국의 엔터프라이즈 AI 및 클라우드 도입 속도와 특수성
  - 메가존클라우드의 성장 스토리(국내 1호 AWS 프리미어 파트너 ➔ 1.8조 원 기업가치 유니콘 등극)
  - 글로벌 빅테크(AWS, Google, MS, Dell, NVIDIA)와의 파트너십 오케스트레이션
  - 한국 기술 기업의 글로벌 확장(미국, 일본, 동남아) 전략 및 도전 과제
- **방한 기간 타 방문 기업과의 연결**:
  - 삼성전자(메모리/HBM), 아모레퍼시픽(뷰티 AI), **DEEPX(국산 온디바이스 NPU)** 등 방문 예정
  - 특히 DEEPX의 NPU 칩셋 기술과 MZC의 엔터프라이즈 풀스택 연동을 발표 중 강조하여 청중 몰입도 극대화.

---

## 2. 4대 관점(Infra, Model, Solution, Service) 프레임워크 설계

정부 과기정통부(MSIT) 소버린 AI 2.0 정책 및 산업계 실태 분석을 기반으로 4대 축을 정립하였습니다:

### 2.1 Pillar 1: Infrastructure (인프라 & 국산 실리콘 주권)
- **국가 AI 컴퓨팅 센터 (AI 고속도로)**: 전남 해남 솔라시도 민관합작(SPC) 착공 (2026년 8월), 2028년 1.5만 장 ➔ 2030년 5만 장 GPU 클러스터 공급 로드맵.
- **K-클라우드 프로젝트 & NPU 팜**: 리벨리온(ATOM), 퓨리오사AI(RENEGADE), 딥엑스(All-in-4), 모빌린트 등 국산 추론 칩 생태계.
- **하이브리드 & 온프레미스 인프라**: Dell PowerEdge + NVIDIA 메인스트림과 Akamai GPUaaS의 TCO 절감 결합.
- **전산실 10kW 랙 전력 한계 돌파**: 8-GPU(10.2kW) 대신 고효율 2-GPU 2U 서버(3.2kW)로 기존 전산실 즉시 도입 실현.

### 2.2 Pillar 2: Model (파운데이션 모델 & 도메인 특화)
- **국산 파운데이션 모델 생태계**: 네이버 HyperCLOVA X, LG AI연구원 EXAONE 3.0, 업스케이지 Solar.
- **모놀리식에서 도메인 sLLM & MoE로의 전환**: 250B 총 파라미터 중 20B~30B만 활성화하는 MoE 구조로 속도/비용 최적화.
- **문화적/언어적/규제적 정렬 (Sovereign Moat)**: 기업 존댓말/비즈니스 에티켓, 상법/노동법 정밀 인용, 금융보안원/개인정보보호법 100% 준수.
- **경량화 컴파일러 기술**: INT4/NVFP4 양자화 및 비균일 프루닝으로 메모리 70% 절감 및 65+ TPS 달성.

### 2.3 Pillar 3: Solution (소프트웨어 오케스트레이션 & 보안)
- **엔터프라이즈 Missing Link 해결**: AI PoC의 85%가 양산 실패하는 파편화 문제를 4-Layer 일체형 풀스택으로 해소.
- **MZC 4-Layer 아키텍처**: L1 하드웨어 ➔ L2 Nutanix/RHOAI 가상화 ➔ L3 Nota NetsPresso/vLLM 모델 서빙 ➔ L4 엔터프라이즈 애플리케이션.
- **에어갭(Air-Gapped) 폐쇄망 보안 & 그래프 RAG**: 단 1바이트의 외부 유출도 없는 물리적 격리, Mem0 영구 메모리 + Graphify AST RAG 구조.
- **글로벌 & 국내 ISV 생태계 총괄**: Articul8, Cohere 등 글로벌 ISV와 Nota, 퍼즐데이터, 퀀텀AI 등 국내 강소 ISV 통합.

### 2.4 Pillar 4: Service (기업 참여 & 실제 도입 사례)
- **대한민국 대표 기업군 실도입**: 반도체(웨이퍼 결함 검사), 금융(사내 온프레미스 여신 심사), 뷰티(맞춤형 처방), 중공업(예지보전).
- **소버린 AI 턴키 어플라이언스**: 2U 랙 서버 전원 연결 후 2시간 내 사내 구축 완료.
- **정량적 비즈니스 ROI**: H100 8-GPU 대비 Capex 75% 절감($120K vs $480K), 3.2kW 전력 충족, 지연시간 3배 단축.
- **대국민 AI 혁신**: AI 공무원, 대국민 복지 바우처, 지방 공공의료 AI 진단 보조.

---

## 3. 슬라이드 데크 30장 구성 및 15분 페이싱 계획

| 파트 | 슬라이드 범위 | 할당 시간 | 핵심 전달 목표 |
|---|---|---|---|
| **Part 1. 매크로 배경 및 국가적 과제** | Slides 01 ~ 06 | 0:00 ~ 3:00 (3분) | 소버린 AI 2.0 정의, 한국의 G3 위상, 전산실 3대 장벽, 4대 기둥 소개 |
| **Part 2. 기둥 1 - 인프라 & 실리콘 주권** | Slides 07 ~ 12 | 3:00 ~ 6:00 (3분) | 해남 AI 센터(5만 장), K-NPU 팹리스(딥엑스 환영), 3.2kW 전력 해결 |
| **Part 3. 기둥 2 - 파운데이션 모델 생태계** | Slides 13 ~ 17 | 6:00 ~ 8:30 (2.5분) | 하이퍼클로바X/엑사원, MoE 구조, 한국어 에티켓/법률 정밀도, INT4 최적화 |
| **Part 4. 기둥 3 - 솔루션 & 풀스택 오케스트레이션** | Slides 18 ~ 22 | 8:30 ~ 11:00 (2.5분) | Missing Link 극복, 4-Layer 스택, 에어갭 그래프 RAG, ISV 파트너십 |
| **Part 5. 기둥 4 - 서비스 & 엔터프라이즈 채택** | Slides 23 ~ 26 | 11:00 ~ 13:00 (2분) | 삼성/아모레 도입 사례, 2시간 턴키 어플라이언스, 75% Capex 절감 실측 |
| **Part 6. 메가존클라우드 전략 & 글로벌 비전** | Slides 27 ~ 30 | 13:00 ~ 15:00 (2분) | 클라우드 유니콘 성장사, 미국/일본/동남아 확장, EMBA 리더 제언, Q&A 오픈 |

---

## 4. 산출물 파일 맵 (Specs Map)

| 구분 | 파일 경로 | 형식 | 역할 및 상세 내용 |
| :--- | :--- | :---: | :--- |
| **공식 파워포인트** | [`K-AI/2026-09-09_Korea_Sovereign_AI_Strategy_Deck.pptx`](file:///c:/dev/antigravity-workspace/aifullstack/K-AI/2026-09-09_Korea_Sovereign_AI_Strategy_Deck.pptx) | PPTX | 16:9 와이드스크린(13.33x7.5"), 30슬라이드 공식 덱, 5대 16:9 고화질 이미지 및 발표자 대본(Notes) 완비 (4.55 MB) |
| **PPTX 생성기** | [`K-AI/build_k_sovereign_ai_pptx.py`](file:///c:/dev/antigravity-workspace/aifullstack/K-AI/build_k_sovereign_ai_pptx.py) | Python | Dell 총판 제안서 템플릿의 디자인 시스템을 반영한 자동 PPTX 빌더 |
| **마크다운** | [`K-AI/2026-09-09_Korea_Sovereign_AI_Strategy_Deck.md`](file:///c:/dev/antigravity-workspace/aifullstack/K-AI/2026-09-09_Korea_Sovereign_AI_Strategy_Deck.md) | MD | 30장 슬라이드 전문, 불릿 포인트, 비주얼 가이드, 스피커 대본(Notes) |
| **문서 생성기** | [`K-AI/generate_k_sovereign_ai_deck_docx.py`](file:///c:/dev/antigravity-workspace/aifullstack/K-AI/generate_k_sovereign_ai_deck_docx.py) | Python | 고급 스타일링(UCLA Navy/Gold, MZC Blue) 적용 DOCX 생성 스크립트 |
| **공식 워드** | [`K-AI/2026-09-09_Korea_Sovereign_AI_Strategy_Deck.docx`](file:///c:/dev/antigravity-workspace/aifullstack/K-AI/2026-09-09_Korea_Sovereign_AI_Strategy_Deck.docx) | DOCX | 5대 고해상도 이미지가 포함된 4.5MB 인쇄 및 배포용 프레젠테이션 브리프 |
| **인터랙티브 웹** | [`K-AI/2026-09-09_Korea_Sovereign_AI_Strategy_Deck.html`](file:///c:/dev/antigravity-workspace/aifullstack/K-AI/2026-09-09_Korea_Sovereign_AI_Strategy_Deck.html) | HTML | 키보드 탐색, 전체화면(F), 대본 토글(S), 전체보기(G), 15분 타이머 및 2열 이미지 그리드 탑재 |
| **상세 명세서** | [`docs/specs/2026-09-09_k_sovereign_ai_strategy_presentation_spec.md`](file:///c:/dev/antigravity-workspace/aifullstack/docs/specs/2026-09-09_k_sovereign_ai_strategy_presentation_spec.md) | MD | 본 표준 작업 명세서 |

---

## 5. 최종 검증 결과
- 모든 슬라이드 및 발표 대본은 100% 영문(English only)으로 작성 완료.
- 15분 발표 시간에 맞춘 타임코드 슬롯(`0:00~0:30`부터 `14:30~15:00`까지) 완비.
- DOCX 및 HTML 빌드 정상 완료 및 브라우저/오피스 호환성 검증 완료.
