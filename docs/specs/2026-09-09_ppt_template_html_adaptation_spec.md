# 2026-09-09 PPT 템플릿(Dell Distributor Proposal) HTML 슬라이드 덱 반영 명세서 (Specs)

## 1. 개요 및 목적
- **목적**: 사용자가 제공한 파워포인트 제안서 템플릿(`K-AI/Dell_Distibutor_proposal.pptx`)의 색상, 타이포그래피, 헤더/푸터 구조 및 카드 그리드 레이아웃을 15분 30슬라이드 영문 발표 HTML(`K-AI/2026-09-09_Korea_Sovereign_AI_Strategy_Deck.html`)에 100% 반영하여, 웹 브라우저에서도 실제 최고급 기업 프레젠테이션 쇼와 동일한 시각적 퀄리티와 조작성을 제공합니다.
- **적용 대상 세션**: UCLA Anderson Executive MBA Delegation Visit (2026-09-11 금요일 10:00~11:30 AM KST) Session 3 "Korea's Sovereign AI Strategy" (발표: MegazoneCloud ISV Business Unit / Andy).

---

## 2. 변경된 파일 목록 (Specs File Map)

| 파일 경로 | 작업 구분 | 주요 변경 내역 |
|:---|:---:|:---|
| [`K-AI/2026-09-09_Korea_Sovereign_AI_Strategy_Deck.html`](file:///c:/dev/antigravity-workspace/aifullstack/K-AI/2026-09-09_Korea_Sovereign_AI_Strategy_Deck.html) | **MODIFY** | PPT 템플릿 팔레트(다크 네이비 `#0B2A68`, 타이틀 블루 `#002060`, 액센트 `#1760CB`), 16:9 반응형 자동 스케일링 엔진, 2x2 카드 그리드, 3열 컬럼, 2단 이미지 분할, ROI 스코어카드 배지, 다크 피날레 Q&A 레이아웃 반영 |
| [`K-AI/apply_ppt_template_to_html.py`](file:///c:/dev/antigravity-workspace/aifullstack/K-AI/apply_ppt_template_to_html.py) | **NEW** | PPT 템플릿 레이아웃과 30슬라이드 전체 데이터를 병합하여 무오류 고품질 HTML을 빌드하는 자동화 스크립트 |
| [`docs/specs/2026-09-09_ppt_template_html_adaptation_plan.md`](file:///c:/dev/antigravity-workspace/aifullstack/docs/specs/2026-09-09_ppt_template_html_adaptation_plan.md) | **NEW** | PPT 템플릿 디자인 시스템의 HTML 슬라이드 이식 상세 계획서 |
| [`docs/specs/2026-09-09_ppt_template_html_adaptation_spec.md`](file:///c:/dev/antigravity-workspace/aifullstack/docs/specs/2026-09-09_ppt_template_html_adaptation_spec.md) | **NEW** | 본 코드 변경 상세 명세서 및 검증 결과 보고서 |

---

## 3. 핵심 디자인 및 레이아웃 이식 상세

### 3.1 PPT 템플릿 디자인 시스템 & 컬러 토큰 일체화
- **섹션 약장 배지 (Part Pill Badge)**: PPT 템플릿의 Shape 11 시그니처 색상인 Deep Corporate Navy (`#0B2A68`) 및 11px Montserrat 굵은 폰트 적용.
- **슬라이드 메인 헤드라인**: 템플릿 메인 타이틀 색상인 Navy Bold (`#002060`), 23px 폰트 및 블루 액센트 서브타이틀 (`#1760CB`).
- **하단 디바이더 라인**: 헤더 하단 2px 그레이 라인 및 좌측 80px 액센트 블루 포인트 라인.
- **화이트 카드 박스**: 흰색 배경 (`#FFFFFF`), 섬세한 테두리 (`#DDE5ED`), 좌측 5px 그라디언트 액센트 바, 원형 번호 배지 (`#1760CB`), 마우스 호버 시 입체감 애니메이션.

### 3.2 슬라이드 유형별 템플릿 레이아웃
1. **Cover Slide (Slide 01)**:
   - 다크 네이비 테마 (`#001224` ~ `#0B2A68`)
   - 16:9 서울 소버린 AI 메인 키 비주얼 (`images/slide01_cover_sovereign_ai.jpg`)
   - UCLA Anderson EMBA & MegazoneCloud 골드/시안 메타데이터 카드
2. **2x2 Grid Card Layout (4개 불릿 슬라이드: Slide 2, 4, 6, 8, 10, 12, 20, 22, 23, 27, 29)**:
   - 4개 항목을 수직 1열이 아닌 PPT 템플릿의 2행 x 2열(2x2) 균형 잡힌 사각 그리드로 배치하여 가독성과 공간 균형 극대화.
3. **3-Column Grid Layout (3개 불릿 슬라이드: Slide 3, 5, 9, 11, 13, 14, 15, 16, 17, 18, 21, 26)**:
   - 가로 3개 컬럼으로 카드를 시원하게 배치하여 PPT 템플릿 특유의 수평 확장감 제공.
4. **Split Image Layout (Slide 07, 19, 24, 28)**:
   - 좌측 3개 요약 카드 + 우측 16:9 고화질 비주얼 (클릭 시 원본 고해상도 팝업 줌).
5. **Executive ROI Metric Scorecard (Slide 25)**:
   - `75% CAPEX CUT` (블루), `3.2kW POWER` (앰버), `3x FASTER` (그린), `100% AIR-GAPPED` (퍼플) 등 대형 KPI 콜아웃 배지 강조.
6. **Closing Q&A Slide (Slide 30)**:
   - 발표 피날레를 장식하는 다크 네이비 테마 및 스피커 정보, 공식 이메일, 질의응답 토론 아젠다 카드 배치.

### 3.3 16:9 반응형 자동 스케일링 엔진 (Scale-to-Fit Engine)
- 어떤 해상도의 모니터/노트북/프로젝터에서도 1333 x 750 px 기준 16:9 캔버스가 화면 중앙에 왜곡 없이 꽉 차도록 `window.resize` 시 자동 `scale(scaleFactor)` 연산 적용.
- 슬라이드 내부에 스크롤바가 전혀 생기지 않는 완벽한 프레젠테이션 쇼 화면 제공.

---

## 4. 브라우저 실증 검증 결과 (Verification Evidence)

브라우저 서브에이전트(`browser_subagent`)를 통해 실제 로컬 크로미움 브라우저에서 전수 검증을 완료했습니다:

| 검증 항목 | 검증 대상 슬라이드 / UI | 검증 결과 | 캡처 아티팩트 |
|:---|:---|:---:|:---|
| **커버 슬라이드** | Slide 01 | 16:9 다크 테마, UCLA/MZC 로고 뱃지, 커버 이미지 완벽 렌더링 | `slide_01_cover_1788915931777.png` |
| **2x2 그리드 레이아웃** | Slide 02 | 템플릿 헤더 구조 및 2x2 카드 박스 정렬 확인 | `slide_02_grid_layout_1788915937196.png` |
| **이미지 분할 레이아웃** | Slide 07 | 좌측 3개 카드 + 우측 K-NPU 해남 데이터센터 16:9 그래픽 확인 | `slide_07_split_layout_1788915944442.png` |
| **발표자 대본 서랍** | `S` 키 / Notes 버튼 | 하단 서랍 슬라이드 오픈, 페이싱 타임라인 및 대본 전문 표시 확인 | `speaker_notes_drawer_1788915949349.png` |
| **30슬라이드 전체 그리드** | `G` 키 / All Slides | 30개 슬라이드 썸네일 모달 오픈, 원클릭 이동 및 닫기 확인 | `all_slides_grid_modal_1788915964377.png` |
| **ROI 메트릭 스코어카드** | Slide 25 | 4개 핵심 지표 카드 및 컬러별 KPI 배지 강조 확인 | `slide_25_roi_scorecard_1788915993721.png` |
| **피날레 다크 Q&A** | Slide 30 | 다크 테마 배경에 스피커 메타 카드 및 Q&A 아젠다 확인 | `slide_30_closing_qa_1788916003647.png` |
| **브라우저 세션 녹화본** | 전체 검증 세션 | WebP 비디오 녹화 저장 완료 | `verify_ppt_template_html_1788915920667.webp` |
