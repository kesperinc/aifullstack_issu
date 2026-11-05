# [작업계획서] 2026-11-05 Unity Asset Transformer & Physical AI 발표자료 및 쇼케이스 제작

- **작성일자**: 2026-11-05
- **행사명**: Intel AI Summit Seoul 2026 (코엑스 1F Gold 부스)
- **주제**: Unity Asset Transformer 중심의 3D 데이터 최적화와 Physical AI 파이프라인 연계 (10분 발표/게시용)
- **주관/협력**: 메가존클라우드 (Unity 국내 공식 총판) & Intel

---

## 1. 추진 배경 및 목표
1. **행사 맥락**: 인텔 행사 부스 전시 및 10분 키오스크/세션 발표에 적합한 실무적이고 설득력 있는 하이테크 쇼케이스 자료 구축.
2. **핵심 강조점**:
   - **Asset Transformer**: 엔지니어링 CAD/BIM 등 70여 종의 복잡한 3D 원본 데이터를 수작업 없이 실시간 인터랙티브 모델로 자동 경량화·변환·배치 처리하는 핵심 엔진.
   - **Physical AI 연계**: 변환된 디지털 트윈 에셋을 기반으로 [합성 데이터 생성 ➔ AI 학습 ➔ 온디바이스 Sentis 추론 ➔ ROS2 실물 연동]으로 이어지는 완결형 물리 AI 파이프라인 제시.
   - **Intel 시너지**: 인텔 제온(Xeon) 기반 대규모 CAD 배치 변환 & 인텔 코어 울트라/아크/엣지 디바이스 기반 초저지연 온디바이스 Sentis 추론 (하드웨어 중립성 극대화).
3. **산출물 형태**: 단독 실행 및 키오스크 순환이 가능한 고품질 인터랙티브 HTML5 웹 프레젠테이션 + 상세 기획 및 발표 대본 명세서.

---

## 2. 슬라이드 구조 설계 (총 10분 분량 / 8개 슬라이드)

| 슬라이드 번호 | 주제 (Title) | 발표 배정 시간 | 핵심 콘텐츠 |
|---|---|---|---|
| **Slide 01** | **Title & Vision**: Unity Industry on Intel | 01분 00초 | Asset Transformer 기반 엔지니어링 3D 최적화와 Physical AI 생태계 비전 |
| **Slide 02** | **Industry Bottlenecks**: 자동화 확장의 3대 장벽 | 01분 15초 | 분산된 워크플로, 높은 실패 비용(Sim2Real 갭), 특정 HW 종속 한계와 비즈니스 비용 ($2.3M 다운타임) |
| **Slide 03** | **Core 1: Asset Transformer**: 3D 데이터 파이프라인의 대전환 | 01분 45초 | 70+ CAD/BIM 포맷 자동 최적화, 재사용 Recipe 표준화, SDK 및 대규모 무인 배치(Batch) 처리 |
| **Slide 04** | **Data Management: Asset Manager & 3DDS** | 01분 00초 | 클라우드/온프레미스 에셋 통합 관리, 런타임 동적 스트리밍(3D Data Streaming), 버전 관리 |
| **Slide 05** | **Core 2: Physical AI End-to-End 파이프라인** | 02분 00초 | 4단계 구조 (① 합성 데이터 & URP/PhysX ➔ ② PyTorch/ML-Agents 학습 ➔ ③ Sentis 온디바이스 추론 ➔ ④ ROS2/XR 로봇 실물 연결) |
| **Slide 06** | **AI-Driven Development**: Agentic 코딩 & Unity AI MCP | 01분 00초 | Claude Code / Antigravity / Codex와 직결되는 Unity AI MCP, 자연어 씬·UI·3D 저작 |
| **Slide 07** | **Intel Synergy**: 하드웨어 중립적 물리 AI 가속 | 01분 00초 | Intel Xeon(대규모 배치 변환/학습) + Intel Core Ultra/Arc(Sentis 엣지 온디바이스 저지연 추론) |
| **Slide 08** | **Conclusion & Roadmap**: 메가존클라우드 공식 지원 | 01분 00초 | 시운전 30~70% 단축, 과제정의-PoC-라이선스-전문컨설팅 4단계 도입 로드맵 |

---

## 3. HTML 쇼케이스 기술 구현 사양
- **해상도**: 1920x1080 Full HD 최적화 및 유동적 반응형 지원
- **디자인 테마**: Intel Blue (`#0071C5`), Cyber Cyan (`#00C7FD`), Deep Navy (`#03060f`), Unity White & Glassmorphism UI
- **인터랙션 기능**:
  - 자동 슬라이드 재생 모드 (총 10분 루프 또는 발표 데모용 슬라이드별 진행바)
  - 수동 컨트롤 (좌/우 방향키, 스페이스바 일시정지, 숫자키 1~8 다이렉트 점프, 'F' 전체화면, 'A' 자동/수동 토글)
  - 다이어그램 및 시각화 (CSS/SVG 기반 Asset Transformer 파이프라인 및 Physical AI 아키텍처 다이어그램)
  - 슬라이드별 발표자 노트 / 대본 토글 패널 ('N' 키로 발표용 대본 보기 지원)
- **외부 종속성 최소화**: 오프라인 및 로컬 단독 실행 완벽 보장

---

## 4. 실행 계획 및 최신 업데이트 내역 (2026-11-05 15:46 반영 완료)
1. `2026-11-05_Unity_Asset_Transformer_Physical_AI_발표기획서.md` 작성 완료
2. `Unity_AssetTransformer_PhysicalAI_Showcase.html` 작성 (인텔 행사 폴더에 배치)
3. **원본 PPT(`Unity_발표자료.pptx`, 13p) 기반 7-Slide 고밀도 맥락 중심 재구성 완료 (`Unity_발표자료.html` & `Unity_발표자료_Showcase.html`)**:
   - 페이지 수(13p)나 시간에 억지로 맞추지 않고 카드 하단 빈 공간을 완전히 제거하여 **7페이지 고밀도 레이아웃**으로 통합 재구성:
     - **Slide 01 (PPT 1~3p 통합)**: `Unity Industry: 3D 에셋 파이프라인(Ingest➔Convert➔Access➔Render➔Deploy➔Output) & Product Solution 체계(Author·Run·Measure)`
     - **Slide 02 (PPT 4p)**: `Asset Transformer: 복잡한 3D·CAD 데이터 자동 최적화` (좌측 3단 수평 스택 카드 + 우측 `image24.gif` 353만 폴리곤 경량화 데모)
     - **Slide 03 (PPT 5~6p 통합)**: `Asset Manager & Simulations: 3DDS 스트리밍과 동적 에셋 로딩` (좌측 2단 아키텍처 카드 + 우측 `image25.gif`, `image27.gif`, `image26.gif` 3분할 벤토 그리드)
     - **Slide 04 (PPT 7~8p 통합)**: `Physical AI 학습: Unity XR Solutions & ML-Agents` (좌측 XR 원격 조작 `image28.png` + 우측 PyTorch 다중 에이전트 강화학습 `image29.png`)
     - **Slide 05 (PPT 9p)**: `Unity Sentis: ONNX 기반 온디바이스 AI 실시간 추론` (좌측 3단 수평 카드 스택 + 우측 Unity 6 창고 로봇 시뮬레이션 `image30.png` 복원)
     - **Slide 06 (PPT 10p)**: `Simulation Pro: 센서 모델부터 ROS2 로보틱스 연동까지` (좌측 2×2 핵심 기능 그리드 + 우측 3D LiDAR/ROS2 시뮬레이션 `image31.gif`)
     - **Slide 07 (PPT 11~13p 통합)**: `메가존클라우드(공식 총판) 3대 지원 체계 & 4단계 도입 로드맵 + 부스 상담 안내` (기본 수동 전환 모드로 설정)


