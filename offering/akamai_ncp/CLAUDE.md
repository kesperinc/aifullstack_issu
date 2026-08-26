# CLAUDE.md - AKAMAI & NVIDIA 클라우드 플랫폼 공동 사업 기획 프로젝트

이 문서는 `akamai_ncp` 워크스페이스 내에서 기획안 작성 및 타당성 점검 작업을 효율적으로 가이드하기 위한 안내서이자 상태 보존용 문서입니다.

---

## 1. 프로젝트 개요
- **목적**: AKAMAI의 글로벌 분산 엣지 클라우드 및 NVIDIA의 GPU AI 인프라 기술을 융합하여, 저비용·초저지연의 하이브리드 AI 클라우드 플랫폼 공동 사업 계획안을 설계하고 기술적/비즈니스적 타당성(Feasibility)을 점검합니다.
- **주요 산출물**:
  - `README.md`: 프로젝트 추진 개요 및 핵심 아키텍처/비즈니스 요약.
  - `docs/proposal/`: 공동 사업 계획 제안서 (비즈니스 모델, 파트너십 구조).
  - `docs/feasibility/`: 기술, 경제성, 시장성, 법적 규제 분석 타당성 검토 보고서.
  - `docs/simulations/`: 대역폭 비용 시뮬레이션 및 TCO 비교 분석 자료.

---

## 2. 작업 절차 및 에이전트 워크플로우

본 워크스페이스에서는 CortexOS의 단계별 검토 프로세스를 따릅니다.

1. **아이디어 구체화 및 기획안 초안 수립** (`/office-hours` 스킬 활용)
2. **비즈니스 임팩트 및 제품 가치 제안 평가** (`/plan-ceo-review` 스킬 활용)
3. **기술 및 사업적 타당성 심층 분석** (`/plan-feasibility-audit` 스킬 활용)
4. **결과물 검토 및 변경 불가능 동결 처리** (`/guard` 스킬 활용)

---

## 3. 로컬 환경 및 도구 사용 지침

만약 비용 모델링 시뮬레이션, 데이터 시각화 또는 그래프 작성을 위해 스크립트 실행이 필요할 경우, 다음 지침을 엄격히 준수합니다.

### 3.1. 파이썬 가상환경 (Python Virtual Environment)
- 프로젝트 내에 가상환경을 구성할 때는 **`uv`** 패키지 매니저를 사용하여 **`.venv`** 폴더에 생성합니다.
- 기존에 `.venv` 폴더가 존재한다면 새로 생성하지 않고 기존 가상환경을 그대로 사용합니다.

### 3.2. 데이터 시각화 및 한글 폰트 설정 규칙
- **Seaborn 스타일 설정 금지**: 데이터 시각화 그래프를 그릴 때 `sns.set_theme()` 등 Seaborn의 스타일 설정을 절대로 사용하지 않습니다.
- **한글 폰트 적용**: matplotlib 기반의 시각화 그래프를 그릴 때는 **`koreanize-matplotlib`** 패키지를 import하여 한글 폰트가 깨지지 않고 정상적으로 표시되도록 설정합니다.
  ```python
  import matplotlib.pyplot as plt
  import koreanize_matplotlib  # 한글 폰트 설정을 위해 필수 import
  ```

### 3.3. 문서 이중 저장 규칙 (MD & HTML)
- **HTML 동시 변환 필수**: 마크다운(`.md`) 분석 문서나 기획 제안서가 작성/수정될 때마다, 반드시 동일한 경로에 프리미엄 CSS 테마를 씌운 HTML(`.html`) 파일로 변환하여 동시 저장 및 커밋해야 합니다. (이중 저장 정책)

---

## 4. 핵심 명령어 레퍼런스

- **시뮬레이션 및 재무 대시보드 빌드**
  ```powershell
  .venv\Scripts\activate  # 가상환경 활성화 (Windows PowerShell)
  python scripts/bep_simulation.py  # 1. 재무 시뮬레이션 실행 및 bep_chart.png 생성
  python scripts/build_html_report.py  # 2. Base64 임베디드 프리미엄 HTML 재무 대시보드 빌드
  ```
- **마크다운 문서 일괄 HTML 변환**
  ```powershell
  python scripts/convert_all_md.py  # README, 기획서, 시장분석 보고서 등 일괄 HTML화
  ```
- **스킬 실행 명령어**
  - 에이전트는 기획 진행 단계에 따라 `.agents/skills/`에 정의된 각 스킬의 행동 지침을 수행합니다. (예: `/plan-feasibility-audit`을 입력받아 검증 단계 착수)
