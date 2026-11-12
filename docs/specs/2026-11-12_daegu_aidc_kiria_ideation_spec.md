# [상세명세서] 대구 수성알파시티 AIDC 국책사업 검증, KIRIA 회의 아젠다 및 5MW GPUaaS 회수 사업 아이디에이션 명세

- **작성 일자**: 2026-11-12
- **연관 계획서**: [2026-11-12_daegu_aidc_kiria_ideation_plan.md](file:///c:/dev/antigravity-workspace/aifullstack/docs/plans/2026-11-12_daegu_aidc_kiria_ideation_plan.md)

---

## 1. 변경 일자별 파일 수정 맵 (Specs Map - 2026-11-12)

| 구분 | 파일 경로 | 작업 내용 요약 |
| :---: | :--- | :--- |
| **신규 생성** | `docs/akamai_ncp/daegu_suseong_aidc/2026-11-12_kiria_1st_meeting_presentation_deck.md` (`.html` / `.docx`) | • 차주 한국로봇산업진흥원(KIRIA) 원장 1차 협력 미팅용 상위 5대 핵심 협력 사업 중심 10장 구성 발표 장표<br/>• 16:9 와이드 인터랙티브 슬라이드 덱 HTML(방향키 전환·스크롤/인쇄 모드 지원) 및 슬라이드별 Word(DOCX) 동기화 산출물 |
| **신규 생성** | `docs/akamai_ncp/daegu_suseong_aidc/2026-11-12_kiria_1st_meeting_executive_summary.md` (`.html` / `.docx`) | • KIRIA 및 대구시 기계로봇과 대외 배포용 1차 협력 미팅 핵심 요약본(Handout)<br/>• Twin-Hub 협력 구조, 상위 5대 우선 협력 아이템 요약표, '27 임대형 브릿지 로드맵 및 1차 회의 협의 안건 수록 |
| **신규 생성** | `docs/akamai_ncp/daegu_suseong_aidc/2026-11-12_daegu_aidc_budget_structure_and_revenue_puzzle.md` (`.html` / `.docx`) | • 대구 AIDC 10MW(`3,500억`) / 대구시 연계 5MW(`1,750억`) 하이브리드 3:2 모델 기준 표준 예산 구조(부지·코어건축·MEP·컴퓨트·연간 OpEx) 재무 테이블 정립<br/>• 5MW 연간 회수 목표(`연 380억` / 5년 `1,900억`) 및 10MW 전체 회수 구조를 정밀 매핑한 5대 매출퍼즐(Revenue Puzzle) 독립 분석서 |
| **신규 생성** | `docs/akamai_ncp/daegu_suseong_aidc/2026-11-12_daegu_aidc_reverse_costing_pf_risk_and_jb_dongtan_analysis.md` (`.html` / `.docx`) | • 10MW LOI 비용 분해(물리 2,000억 vs 하이브리드 3,500억 vs 풀스택 6,000억) 및 5MW 연간 회수액 역산출<br/>• 기 진행사업 진입 한계 반영 '선투자-후회수' 금융 리스크 및 구미 앤트로픽 임차 무산설 보도 비교 분석<br/>• 지식산업센터 분양 모델 기반 6단계별 투자금·리스크·기대이익률(IRR/마진율) 및 최적 진입 시점 도출<br/>• 사내 추진 'JB동탄 DC 운영권 딜(IT 6.6MW / 수전 10MW급, '29.6월 RFS)' 정체 규명 및 대구 AIDC 비교 전략 |
| **신규 생성** | `docs/akamai_ncp/daegu_suseong_aidc/2026-11-12_daegu_aidc_kiria_meeting_and_5mw_business_ideation.md` | • 기정원(TIPA) 5극3특 자료 포함 여부 확인 결과 정리<br/>• 대구시 기계로봇과 9대 국책사업 및 '5,000억/7,000억' 예산 실체 팩트체크<br/>• 한국로봇산업진흥원(KIRIA) 차주 1차 회의용 Twin-Hub 전략 및 발표 목차(안)<br/>• MZC 5MW 투자금 회수용 GPUaaS 연계 **6대 트랙 · 26개 사업 아이템** 총망라 도출 *(대내외 공유 보안을 위해 특정 개인 실명 전체 비식별화 완료)* |
| **신규 생성** | `docs/akamai_ncp/daegu_suseong_aidc/2026-11-12_daegu_aidc_kiria_meeting_and_5mw_business_ideation.html` / `.docx` | • 마크다운 원본과 1:1 동기화된 다크모드 프리미엄 HTML 및 Word(DOCX) 변환 산출물 |
| **업데이트** | `docs/akamai_ncp/daegu_suseong_aidc/daegu_suseong_robot_training_center_proposal.md` (`.html` / `.docx`) | • 문서 버전 V2.0 → V2.1(`2026-11-12`) 갱신<br/>• 제7장 「대구시 9대 로봇 국책사업 연계 및 KIRIA Twin-Hub 전략」 추가 반영 |
| **업데이트** | `docs/akamai_ncp/README.md` (`.html` / `.docx`) | • `daegu_suseong_aidc/` 섹션 내 2026-11-12 주요 작업내역 4대 요약 및 전체 8종 산출물 요약표(용도·링크 통합) 신설<br/>• KIRIA 미팅 집중 부각 상위 5대 추천 사업 아이템별 **'추정 사업규모(MZC 연계 5년 누적 / 연간)'** 컬럼 산정·반영 및 `README.html` / `README.docx` 일괄 변환 |
| **업데이트** | `docs/akamai_ncp/scripts/convert_all_md.py` & `convert_html_to_docx.py` | • `conversion_targets` 딕셔너리에 신규 마크다운 파일 등록 (인터랙티브 슬라이드 `presentation_deck.html` 보존 예외 처리)<br/>• `convert_html_to_docx.py`에 `htmldocx` 미설치 오프라인 환경용 `BeautifulSoup + python-docx` 네이티브 렌더러(Mermaid 요약표·슬라이드 페이지 구분·맑은 고딕·Table Grid 지원) 폴백 탑재 |
| **정리** | `docs/akamai_ncp/daegu_suseong_aidc/ocr_extracted_text.txt` | • 취소된 이전 작업에서 생성된 0바이트 빈 임시 파일 삭제 |

---

## 2. 핵심 검증 결과 요약

1. **기정원(TIPA) 5극3특 자료 포함 여부**:
   - 신규 스캔 합본(`대구aidc_20261112.pdf`, 27p)에는 산업부·과기부 5극3특/4극3특 자료 위주로 수록되어 있으며 기정원 원문은 미포함(패키지 표 내 중기부 사업명만 등재).
   - 기존 제안서 V2.0 본문에는 `2025년 지역주력산업 개편계획` 요약치가 기 반영되어 있으므로, 신규 아이디에이션에서는 산업부·과기부 대형 R&D와 중기부·기정원 제조 AX 바우처를 양방향 통합 매핑함.
2. **예산 규모 팩트체크**:
   - 1번 특화단지(민간 설비투자 5.4조 원 + 지자체 후속 육성사업 다년도 건의 기획액 5,000~6,000억 원대)와 4번 4극3특(2,531억 확정) + 5번 지역거점 AX(4,207억 확정, 합계 약 6,738억 원)의 성격을 명확히 분리하여 착공 전 브릿지(Phase 1)와 준공 후 본 오프테이크(Phase 2~3)로 회수 시점을 정교화함.

