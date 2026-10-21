# [상세명세서] 2026 Intel AI Summit 전시신청서 및 부스 전시 HTML 프레젠테이션 명세서

> **작성 일자**: 2026-10-21  
> **프로젝트**: 2026 Intel AI Summit - Gold Sponsor 참가 및 부스 전시  
> **관련 문서**: [2026-10-21_intel_ai_summit_exhibition_plan.md](file:///c:/dev/antigravity-workspace/aifullstack/docs/2026-10-21_intel_ai_summit_exhibition_plan.md)  
> **문서 상태**: 개발 완료 및 배포 검증  

---

## 1. 개요 및 목적

본 명세서는 **'2026 Intel AI Summit'** Gold Sponsor 참가와 관련하여, 운영사무국 제출용 신청서 3종(전시신청서, 전시운영안, 후원사 패스 신청서)의 공식 기재 문안을 수립하고, 부스 현장 디스플레이에서 자동 반복 루프(Auto-loop Kiosk) 형태로 참관객에게 소개될 독립형 HTML 프레젠테이션 2종의 개발 사양 및 파일 변경 내역을 기록합니다.

---

## 2. 파일 생성 및 수정 맵 (Specs Map)

| 구분 | 파일 경로 | 주요 기능 및 사양 | 비고 |
| :---: | :--- | :--- | :---: |
| **기획/문서** | [`docs/2026-10-21_intel_ai_summit_exhibition_plan.md`](file:///c:/dev/antigravity-workspace/aifullstack/docs/2026-10-21_intel_ai_summit_exhibition_plan.md) | • 운영사무국((주)ITBT) 제출용 신청서 3종 기재 문안<br>• 전시 부스 및 발표 세션 운영 전략<br>• 부스 이벤트(설문, 1:1 PoC 상담) 및 기념품 기획안 | 신규 생성 |
| **슬라이드 PPTX** | [`docs/2026-10-21_intel_ai_summit_exhibition_application.pptx`](file:///c:/dev/antigravity-workspace/aifullstack/docs/2026-10-21_intel_ai_summit_exhibition_application.pptx) | • **Google Slides 100% 호환 16:9 전시신청서 슬라이드**<br>• 원본 PDF 양식 4개 페이지 완벽 재현 (표지, 신청서, 운영안, 패스)<br>• 후원사 패스 3, 4번 변경 예정(TBD) 반영 | 신규 생성 |
| **슬라이드 뷰어** | [`docs/2026-10-21_intel_ai_summit_application_slides.html`](file:///c:/dev/antigravity-workspace/aifullstack/docs/2026-10-21_intel_ai_summit_application_slides.html) | • 구글 슬라이드 UI 형태의 반응형 인터랙티브 웹 뷰어<br>• 좌측 필름스트립 및 슬라이드 키보드(←, →) 탐색 지원 | 신규 생성 |
| **발표 덱 1** | [`docs/2026-10-21_intel_summit_articul8_presentation.html`](file:///c:/dev/antigravity-workspace/aifullstack/docs/2026-10-21_intel_summit_articul8_presentation.html) | • Articul8 발표 및 라이브 데모 시연용 슬라이드<br>• Intel Xeon/Gaudi 최적화, ModelMesh, Warp 지식그래프<br>• 9초 주기 자동 롤링, 키오스크 일시정지, 인터랙션 지원 | 신규 생성 |
| **발표 덱 2** | [`docs/2026-10-21_intel_summit_rhoai_fullstack_presentation.html`](file:///c:/dev/antigravity-workspace/aifullstack/docs/2026-10-21_intel_summit_rhoai_fullstack_presentation.html) | • Red Hat OpenShift AI(RHOAI) 기반 풀스택 소개<br>• 단일노드(SNO) 비용 절감, 에어갭 VibeForge 코딩 에이전트<br>• AWS ROSA 하이브리드 확장 및 부스 이벤트 안내 | 신규 생성 |
| **명세서** | [`docs/specs/2026-10-21_intel_ai_summit_exhibition_specs.md`](file:///c:/dev/antigravity-workspace/aifullstack/docs/specs/2026-10-21_intel_ai_summit_exhibition_specs.md) | • 작업 트라이어드(Plan-Code-Doc) 1:1:1 연계 명세<br>• 슬라이드별 기술 규격 및 키오스크 인터랙션 정의 | 신규 생성 |

---

## 3. 세부 기능 구현 명세

### 3.1 신청서 기재 문안 요약
1. **전시신청서 (Page 2)**:
   - 공식 회사명: 메가존클라우드(주) / MegazoneCloud Corporation
   - 부스 타입: Gold Type A 선택
   - 솔루션명: Articul8 Enterprise GenAI Platform & MegazoneCloud AI Full Stack on Red Hat OpenShift
   - 솔루션 소개: Intel Xeon/Gaudi 및 Red Hat OpenShift AI(RHOAI) 기반 엔터프라이즈 100% 에어갭 폐쇄망 생성형 AI 플랫폼.
2. **전시운영안 (Page 3)**:
   - 타이틀: "Intel & Red Hat OpenShift 기반의 메가존클라우드 AI Full Stack & Articul8 엔터프라이즈 GenAI 플랫폼"
   - 데모 개요: Articul8 ModelMesh 실시간 라우팅 및 지식그래프 RAG 시연, OpenShift AI 단일노드(SNO) 및 에어갭 코딩 에이전트(VibeForge) 인프라 제시.
   - 이벤트 및 기념품: 설문 참여자 대상 3in1 맥세이프 고속 무선충전기 500개 증정, 1:1 기술상담 신청자 무료 사이징 컨설팅.
3. **후원사 패스 신청서 (Page 4)**:
   - Gold 5ea 배정 현황:
     - 1번: 조은정 Leader (발표 세션 연사)
     - 2번: 김성호 (전시 부스 총괄 & 파트너십 상담)
     - **3번: [변경 예정 / TBD]** (기술 아키텍트 / Articul8 데모 엔지니어 - 조율 중)
     - **4번: [변경 예정 / TBD]** (프리세일즈 / 비즈니스 개발 - 조율 중)
     - 5번: 어형선 또는 박종서 (마케팅 / 부스 운영 및 설문 리셉션)
   - 3, 4번 인력은 우선 TBD 또는 임시 인입 후 사무국 네임택 실물 인쇄 전 최종 확정 반영 정책 적용.

### 3.2 HTML 프레젠테이션 기술 스펙 (Kiosk & Signage Engine)
- **표준 HD 해상도 최적화 (Full HD 1080p)**: 
  - 부스 모니터, 대형 TV(55~85인치), 키오스크 표준에 맞추어 **1920x1080 (16:9)** 고정 캔버스 및 타이포그래피(타이틀 48~58px, 본문 15~21px)를 전면 적용.
  - **Auto-Scaler (반응형 16:9 배율 조정)**: `Math.min(window.innerWidth / 1920, window.innerHeight / 1080)` 동적 스케일러를 탑재하여, 720p HD부터 1080p FHD, 4K 디스플레이까지 어떤 환경에서도 글자 겹침이나 줄바꿈 깨짐 없이 픽셀 퍼펙트하게 중앙 정렬 렌더링.
- **외부 의존성 제로**: CDN 장애나 오프라인/폐쇄망 부스 환경에서도 완벽히 렌더링되도록 바닐라 HTML5, CSS3, ES6 JavaScript로 구현.
- **Auto-Kiosk 루프 엔진**: 9,000ms(9초) 주기로 다음 슬라이드 자동 전환 및 상단 리니어 프로그레스 바 표시.
- **참관객 인터랙션 감지**: 마우스 호버 및 터치 시 자동 일시 정지(Pause), 키보드 방향키(←, →), 스페이스바, PgUp/PgDn, 터치 스와이프 지원.
- **덱 간 즉시 전환**: 상단 헤더의 `⇄ Switch to Deck` 버튼을 통해 Articul8 덱과 RHOAI 풀스택 덱 간 1-Click 상호 이동 가능.
- **원터치 전체화면 (F11 / 버튼)**: `⛶ Fullscreen` 버튼 및 `F` 단축키로 브라우저 전체화면 전환.

---

## 4. 검증 결과

1. **파일 무결성 검증**: UTF-8 Bom-less 인코딩으로 계획서, HTML 2종, 명세서가 정상 생성됨.
2. **로컬 경로 연계 확인**: 두 HTML 파일 간 상호 링크 및 오프라인 단독 실행 가능 여부 확인 완료.
