# [작업계획서] 대구시 기계로봇과 월요일 제안용 PPT 발표장표(중복성 회피·고도화·데이터팩토리) 및 MZC 내부 수익성·AWS 전환 전략 수립

- **작성 일자**: 2026-11-14
- **대상 프로젝트**: 대구 수성알파시티 AIDC (1단계 10MW = 대구 로봇·City DT 공공 5MW + MZC 자체/글로벌 테넌트 5MW)
- **산출물 분리 원칙**:
  1. **대외 제안용 (대구시 기계로봇과 월요일 미팅용)**: 수익성·JB동탄·AWS 내부 매입·토지 차익 등 민감 재무 내용을 **100% 배제**하고, KIRIA 협력 기반 **기존 사업 고도화(중복성 해소), RFM·데이터 서비스, Isaac+Unity 시뮬레이션, 로봇·City DT 데이터 팩토리(센서 쓰루풋·스토리지 산정 포함)**를 PPT 장표 형태로 간결·명쾌하게 구성.
  2. **사내 전략 검토용 (MZC 내부 전용)**: 수성지구 4,000~6,000평 원가 매입 및 지식산업센터 분양·오피스 임대 보전 전략, AWS 매출(80%) 중 컴퓨트 매입 1/4(25%) 별도 AIDC 법인 전환 수익성 및 협상 레버리지, `5MW+5MW` 스윙 용량 배분 전략을 정밀 분석.

---

## 1. 작업 배경 및 핵심 해결 과제

1. **정부·지자체 사업 중복성 심사 돌파**:
   - 기존 국책사업(국가로봇테스트필드, 안전인증센터 등)과 유사한 신규 구축 제안 시 중복성 문제로 예산 확보가 불가함.
   - **전환 논리**: 물리 시설 중복 신설이 아닌 **'기존 비효율적 직접 신청·개별 수행 사업을 [KIRIA 전문가 매칭 + 수성 AIDC 공유자원 활용] 체계로 전환·고도화'**하는 운영 혁신 모델 제시.
2. **피지컬 AI + City DT 통합 데이터 팩토리 및 기술 스택 확장**:
   - RFM(로봇 파운데이션 모델) 서비스 및 수집 후 로봇 훈련 데이터 서비스(DaaS) 구체화.
   - `NVIDIA Isaac Sim`(정밀 동역학·강화학습)과 `Unity`(초현실 비전 합성·HRI·VR 원격조작·도심/공장 에셋·지역 XR 인력 연계) 결합 방안 수립.
   - 로봇 대당 수집 데이터량·센서 쓰루풋 및 대구 City DT 데이터 수집 체계·용량을 정량 산출하여 **컴퓨트 외 계층형 스토리지(PB급)·네트워크 규모** 도출.
3. **메가존 내부 사업성 및 앵커 테넌트 확보 전략 검증**:
   - 수성알파시티 4,000~6,000평 원가 부지 매입 + 동대구역 인접 지식산업센터 분양·오피스 임대 병행 구조 검토.
   - MZC 전체 매출의 약 80%를 차지하는 AWS 컴퓨트 매입 물량 중 일부(목표 1/4 검토 및 5MW 물리 한계 대조)를 별도 법인인 대구 AIDC로 전환(Repatriation)할 때의 수익성 개선, AWS 협상력, 글로벌 테넌트 GPUaaS 유치 효과 검증.

---

## 2. 생성 및 갱신 대상 파일 목록

1. **대외 월요일 미팅용 PPT 발표자료 (`MD` / 인터랙티브 `HTML` 슬라이드 덱 / `DOCX`)**
   - `docs/akamai_ncp/daegu_suseong_aidc/2026-11-14_daegu_robot_division_monday_proposal_ppt.md`
   - `docs/akamai_ncp/daegu_suseong_aidc/2026-11-14_daegu_robot_division_monday_proposal_ppt.html` *(12-Slide 16:9 PPT Deck)*
   - `docs/akamai_ncp/daegu_suseong_aidc/2026-11-14_daegu_robot_division_monday_proposal_ppt.docx`
2. **내부 전략 및 수익성 심층 검토서 (`MD` / `HTML` / `DOCX`)**
   - `docs/akamai_ncp/daegu_suseong_aidc/2026-11-14_mzc_internal_strategy_land_aws_offload_and_hybrid_10mw.md`
   - `docs/akamai_ncp/daegu_suseong_aidc/2026-11-14_mzc_internal_strategy_land_aws_offload_and_hybrid_10mw.html`
   - `docs/akamai_ncp/daegu_suseong_aidc/2026-11-14_mzc_internal_strategy_land_aws_offload_and_hybrid_10mw.docx`
3. **인덱스 · 스크립트 · 상세명세서 동기화**
   - `docs/akamai_ncp/README.md` (`.html` / `.docx`)
   - `docs/akamai_ncp/scripts/convert_all_md.py`
   - `docs/specs/2026-11-14_daegu_robot_division_ppt_and_internal_strategy_spec.md` (`.html` / `.docx`)
