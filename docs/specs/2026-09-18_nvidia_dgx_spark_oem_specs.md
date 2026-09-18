# 2026-09-18 NVIDIA DGX Spark 공식 OEM 제조사 전수 비교 산출물 명세서 (Specs v2.0)

* **작성 일자**: 2026년 9월 18일
* **문서 버전**: v2.0 (완결본)
* **수정 사유**: Supermicro GB300 항목 완전 삭제 및 NVIDIA 공식 DGX Spark(GB10) 파트너사 전수 조사 반영 (총 8개 제조사: NVIDIA Founders Edition + 7대 공식 OEM)

---

## 1. 산출물 파일 맵 (Specs Map)

| 파일 경로 | 파일 형식 | 주요 내용 및 목적 |
| :--- | :--- | :--- |
| [`docs/2026-09-18_nvidia_dgx_spark_oem_comparison_report.html`](file:///c:/dev/antigravity-workspace/aifullstack/docs/2026-09-18_nvidia_dgx_spark_oem_comparison_report.html) | HTML | 모던 웹 UI/UX (Glassmorphism, 반응형 다크 테마, 8개사 비교 테이블, 에스컬레이션 플로우, 인쇄 최적화) |
| [`docs/2026-09-18_nvidia_dgx_spark_oem_comparison_report.docx`](file:///c:/dev/antigravity-workspace/aifullstack/docs/2026-09-18_nvidia_dgx_spark_oem_comparison_report.docx) | DOCX (Word) | 고객사 전달 및 결재용 A4 서식화 보고서 (테이블 보더, 셀 패딩, 헤더 하이라이트 완비) |
| [`docs/2026-09-18_nvidia_dgx_spark_oem_comparison_report.md`](file:///c:/dev/antigravity-workspace/aifullstack/docs/2026-09-18_nvidia_dgx_spark_oem_comparison_report.md) | Markdown | 깃 저장소 및 사내 위키/지식베이스 연동용 텍스트 보고서 |
| [`scratch/generate_docx.py`](file:///c:/dev/antigravity-workspace/aifullstack/scratch/generate_docx.py) | Python Script | `python-docx` 라이브러리를 활용한 A4 워드 보고서 자동 생성 스크립트 |

---

## 2. 전수 조사 대상 제조사 및 모델 명세 (총 8개사)

1. **NVIDIA**: DGX Spark (Founders Edition) — 순정 레퍼런스 모델
2. **Dell Technologies**: Dell Pro Max GB10 — 24x7 4시간 On-site ProSupport Plus
3. **HP (HPE)**: ZGX Nano AI Station (G1n) — Z-Workstation 저소음 쿨링 & Care Pack
4. **Lenovo**: ThinkStation PGX — Lenovo Premier Support (NBD 방문)
5. **ASUS**: Ascent GX10 — 초소형 경량화(1.48kg), ConnectX-7 기본 강조
6. **GIGABYTE**: AI TOP ATOM — 기가바이트 독자 AI TOP 유틸리티(GUI 파인튜닝)
7. **MSI**: EdgeXpert — 151x151mm 미니 섀시, 고밀도 구리 방열, 가성비 우수
8. **Acer**: Veriton GN100 AI Mini — 실용적 비즈니스 섀시, 산학/교육용 경제적 단가

---

## 3. 핵심 평가 및 티어 분류 결과

* **Tier 1 (엔터프라이즈 직영 On-site)**: Dell, HP, Lenovo (24x7 직영 지원, 4시간/NBD 출동, 최대 5년 보증)
* **Tier 2 (순정 AI 소프트웨어 직통)**: NVIDIA Founders Edition (최신 DGX OS 0-Day 반영, 공인 총판 1차 지원)
* **Tier 3 (가성비 / 연구원 보급형)**: ASUS, GIGABYTE, MSI, Acer (동일 GB10 성능, 경제적 단가, 서비스센터 입고/택배 수리 중심)
