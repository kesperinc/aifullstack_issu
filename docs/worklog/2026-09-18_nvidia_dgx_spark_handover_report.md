# [인수인계 보고서] NVIDIA DGX Spark 및 공식 OEM 7개사 전수 비교·기술지원 체계 핸드오버 (Handover)

- **작성일자**: 2026-09-18
- **인계자**: AI Full Stack 기술영업 및 아키텍처 TF (ISSU)
- **인수자**: MEGAZONECLOUD ISSU 및 관련 영업/기술 엔지니어링 담당자
- **문서버전**: v2.0.0
- **관련 브랜치**: `feature/vibe-coding-agent`

---

## 1. 작업 배경 및 목적 (Background & Objectives)

1. **배경**:
   - 고객사로부터 **NVIDIA DGX Spark(GB10 Grace Blackwell Superchip 기반)** 도입 및 글로벌 OEM 파트너사별 하드웨어 구성, 워런티 정책, 기술지원 체계, 장애 대응 SLA에 대한 비교 검토 요청 수신.
   - 제조사별 정책 차이에 따른 실제 엔터프라이즈 유지보수 실태 및 가이드라인 제시 필요.
2. **목적**:
   - NVIDIA Founders Edition 및 공식 OEM 파트너 7개사(Dell, HP, Lenovo, ASUS, GIGABYTE, MSI, Acer) 제품 전수 조사 및 차별점 분석.
   - 단순 하드웨어 스펙 비교를 넘어 현장 방문(On-site) 지원, 부품 교체 SLA, 워런티 연장(최대 5년), NVIDIA AI Enterprise(NVAIE) 라이선스 연계 여부를 명확히 구조화.
   - 고객사 회신 및 제안 발표에 즉시 활용할 수 있도록 **HTML 대시보드 보고서**, **서식화된 DOCX(Word) 문서**, **Markdown 원본** 산출물 패키지 구축.

---

## 2. 주요 작업 내용 및 핵심 결론 (Key Achievements & Conclusions)

### 2.1 DGX Spark 동일 플랫폼 아키텍처 검증
- 검토 대상 8개사(NVIDIA 및 7대 OEM) 제품은 모두 **NVIDIA GB10 Grace Blackwell Superchip (20코어 Grace CPU + Blackwell GPU, 128GB LPDDR5x 통합 메모리, 1 PFLOPS FP4 AI 연산 성능)** 레퍼런스 메인보드를 탑재.
- 로컬 대규모 언어 모델(LLM) 추론(최대 200B) 및 경량 파인튜닝(약 70B)의 코어 연산 성능과 기본 DGX OS 구동 환경은 대등함을 명확화.

### 2.2 기술지원 체계 및 장애 대응 SLA 기반 3대 티어 분류
1. **Tier 1 (엔터프라이즈 직영 On-site: Dell, HP, Lenovo)**:
   - **Dell**: 전국 직영 서비스망 기반 **ProSupport Plus 4시간 현장 출동 SLA**, 서울/수도권 대형 부품 물류센터 연계, **최대 5년 보증**.
   - **HP**: Z-Workstation 노하우 저소음 쿨링, 전국 Care Pack 지원망, 익일(NBD) 현장 교체.
   - **Lenovo**: Premier Support 전담 기술 어카운트 매니저 배정, 익일(NBD) 현장 부품 교체.
   - *평가: 24시간 무중단 전산실 및 연구소 코어 서버 1순위 추천.*
2. **Tier 2 (순정 AI 소프트웨어 직통: NVIDIA Founders Edition)**:
   - 최신 DGX OS 및 NGC 컨테이너 0-Day 최우선 반영, NVIDIA Enterprise Portal 직영 티켓팅 지원.
   - 국내 공인 DGX 총판(MDS테크 등) 전문 엔지니어링 1차 지원 및 버퍼 재고 교체.
3. **Tier 3 (가성비 / 연구원 개인 보급: ASUS, GIGABYTE, MSI, Acer)**:
   - **ASUS**: 초소형 경량화(1.48kg), ConnectX-7 기본 탑재.
   - **GIGABYTE**: 독자 AI TOP Utility 탑재로 초보자용 GUI 파인튜닝 지원.
   - **MSI**: 151×151mm 초소형, 구리 히트파이프 냉각, 높은 가성비.
   - **Acer**: Veriton 비즈니스 섀시, 가장 경제적인 도입 단가.
   - *지원: 공인 서비스센터 입고/택배 수리 원칙(3~5영업일), 책상 위 1인 1대 대량 보급 최적.*

---

## 3. 완료 산출물 맵 (Specs Map)

| 산출물 파일 경로 | 파일 형식 | 주요 내용 및 활용 용도 |
| :--- | :--- | :--- |
| [`docs/2026-09-18_nvidia_dgx_spark_oem_comparison_report.html`](file:///c:/dev/antigravity-workspace/aifullstack/docs/2026-09-18_nvidia_dgx_spark_oem_comparison_report.html) | HTML | 모던 웹 UI/UX (Glassmorphism, 다크 테마, 8개사 비교 테이블, 에스컬레이션 플로우, 인쇄 최적화) |
| [`docs/2026-09-18_nvidia_dgx_spark_oem_comparison_report.docx`](file:///c:/dev/antigravity-workspace/aifullstack/docs/2026-09-18_nvidia_dgx_spark_oem_comparison_report.docx) | DOCX | 고객사 공식 첨부용 A4 서식 워드 보고서 (헤더, 콜아웃 요약, 테두리/여백 정렬 완료) |
| [`docs/2026-09-18_nvidia_dgx_spark_oem_comparison_report.md`](file:///c:/dev/antigravity-workspace/aifullstack/docs/2026-09-18_nvidia_dgx_spark_oem_comparison_report.md) | Markdown | 사내 지식 베이스 및 깃 저장소 관리용 마크다운 원본 |
| [`docs/specs/2026-09-18_nvidia_dgx_spark_oem_specs.md`](file:///c:/dev/antigravity-workspace/aifullstack/docs/specs/2026-09-18_nvidia_dgx_spark_oem_specs.md) | Specs | 산출물 맵(Specs Map) 및 변경 이력 명세서 |
| [`scratch/generate_docx.py`](file:///c:/dev/antigravity-workspace/aifullstack/scratch/generate_docx.py) | Python | `python-docx` 라이브러리를 활용한 A4 워드 보고서 자동 생성 스크립트 |

---

## 4. 후속 조치 및 고객 대응 권고사항 (Action Items)

1. **고객사 이메일 회신**:
   - 본 보고서의 핵심 요약 및 시나리오별 권고안(Dell 4시간 SLA vs NVIDIA FE 순정 SW vs GIGABYTE GUI vs MSI/ASUS 가성비)을 본문에 삽입하고, 첨부파일로 `2026-09-18_nvidia_dgx_spark_oem_comparison_report.docx` 전달.
2. **상세 견적 및 NVAIE 번들링**:
   - 고객사가 특정 제조사(예: Dell 또는 NVIDIA FE)로 압축할 경우, 3년/5년 워런티 패키지 및 NVIDIA AI Enterprise(NVAIE) 서브스크립션 포함 여부에 따른 세부 비교 견적서 발행.
