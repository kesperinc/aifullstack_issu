# [명세서] SambaNova RDU 기술 분석 및 MZC AI Full Stack 편입 가능성 종합 검토 보고서

- **문서 번호**: SPEC-20260820-SAMBANOVA-01
- **작성 일자**: 2026-08-20
- **작성자**: MZC AI Full Stack 아키텍처 및 ISSU 프리세일즈 팀
- **분석 대상 문서**: `SambaNova Overview Deck-Unitrontech-072726.pdf`
- **대상 파일**:
  - `offering/2026-08-20_sambanova_ai_fullstack_analysis.html` (인터랙티브 웹 보고서)
  - `offering/generate_sambanova_report_docx.py` (DOCX 생성기)
  - `offering/docx/2026-08-20_SambaNova_AI_Fullstack_Analysis_Report.docx` (공식 Word 문서)
  - `docs/2026-08-20_SambaNova_AI_Fullstack_Analysis_Report.docx` (루트 docs 동기화 문서)

---

## 1. 개요 및 ISSU 기본 배경 명시
1. **조직 정의**: ISSU(Integrated Solution Sales Unit)는 메가존클라우드의 **솔루션 세일즈(Solution Sales), 기술 영업 및 프리세일즈(Presales) 중심 조직**임.
2. **하드웨어 판매 구조**: H/W를 직접 제조/보유하지 않으며, **'세일즈 오퍼링(Offering)' 및 아키텍처 패키지 형태로 보유**함 (현재 AIDC 사업에 대하여 검토 중이나, 구체화된 내용은 없음). 실제 판매/납품은 **Dell과 NVIDIA 파트너 에코시스템을 통하여 실행**됨.
3. **인프라 제약 조건**: 현재 ISSU 내부에는 SambaRack이나 RDU 칩셋 등 독자 하드웨어를 직접 설치하여 테스트할 수 있는 **자체 실증 Infra가 부재**한 상태임.

---

## 2. 보고서 핵심 분석 내용

### 제 1 장. ISSU 조직 배경 및 분석 기본 전제
- Solution Sales / Presales 중심 조직 성격, 파트너 H/W 판매 구조, 자체 실증 인프라 부재 조건 명시.

### 제 2 장. SambaNova 핵심 기술 분석 (RDU & Dataflow Architecture)
- **SN50 RDU (5nm AI 프로세서)**: TSMC 5nm 5세대 RDU, SRAM+HBM2e+DDR 3-Tier 메모리 계층 통합.
- **Fast Decode 특화 (250+ Tokens/s/user)**: LLM 추론 중 순차적 토큰 생성(Decode) 단계 최적화로 GPU 대비 10배 빠른 토큰 생성 및 4~5배 Throughput 제공.
- **SambaRack & SambaStack**: 256개 RDU 집적 어플라이언스 (랙당 30kW로 일반 공랭 전산실 수용 가능), 온프레미스 및 완전 폐쇄망(Air-Gapped) 프라이빗 추론 플랫폼.

### 제 3 장. NVIDIA GPU vs SambaNova RDU 심층 기술 & 토큰노믹스 비교
- **비교 분석**: CUDA 에코시스템 vs SambaFlow 독자 컴파일러, Decode 속도(80 Tok/s vs 250 Tok/s), 데이터센터 전력(150kW vs 30kW).

### 제 4 장. 신규 비즈니스 인력/조직 셋업 비용 및 BEP 시뮬레이션
- **5인 전담 조직 셋업 비용**: 연간 고정비 약 10억 ~ 12억 원.
- **국내 시장 수주 현실**: 1차년도 예상 수주 0~1건 (매출 이익 약 0~2억 원).
- **예상 BEP 기간**: 최소 3~4년 이상 소요 (1년 내 회수 불가능).
- **200여 개 ISV 재평가 기준 적용 판정**: BEP 1년 초과 시 신규 솔루션 편입 불가 원칙에 따라 **'공식 솔루션 편입 부정적 (No-Go / 단순 기술 검토로 동결)'** 판정.

### 제 5 장. MZC AI Full Stack 합류 및 총판 사업 타당성 판단
- **솔루션 프레임워크 파편화 방지**: 독자 RDU 칩셋 도입 시 표준 스택 파편화 초래 ➔ **Dell / NVIDIA 표준 라인업 영업에 집중**.
- **총판 편입 허들(분기 100억 원) 미달**: MZC 총판 기준 미달 및 H/W 직접 핸들링(수입/재고/AS) 원천 배제.
- **특수 고객 제한적 연계**: 금융사 등 고객 요청 시 H/W는 서드파티 파트너(Unitrontech 등)가 납품하고 MZC는 S/W SI로만 선별 대응.

### 제 6 장. 종합 결론 및 전략적 의사결정 가이드라인
1. **현재 상태 규정: '단순 기술적 검토' 단계로 유지 (공식 편입 부정적)**
2. **Dell / NVIDIA 공인 총판 사업에 전사 역량 집중 (Core Business First)**
3. **H/W 직접 핸들링 배제 및 선별적 서드파티 파트너 연계 유지**

---

## 3. 검증 결과
- HTML 및 DOCX 파일 빌드 완료 (DOCX 크기 약 40.1 KB, HTML 크기 약 19.5 KB).
