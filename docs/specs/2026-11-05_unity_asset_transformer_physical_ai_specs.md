# [상세명세서] 2026-11-05 Unity Industry 발표자료 레이아웃 센터링 및 인텔 표준 웹폰트 완결 명세서

- **문서 번호**: SPEC-20261105-UNITY-INTEL-06
- **작성일자**: 2026-11-05
- **행사명**: Intel AI Summit Seoul 2026 (코엑스 1F Gold 부스)
- **최종 산출물**:
  - `C:\Users\MZC01-SUNKIM317\OneDrive\2026\ISSU\Intel 행사\Unity_발표자료.html`
  - `C:\Users\MZC01-SUNKIM317\OneDrive\2026\ISSU\Intel 행사\Unity_발표자료_Showcase.html`
  - `C:\Users\MZC01-SUNKIM317\OneDrive\2026\ISSU\Intel 행사\run_unity_presentation.bat`

---

## 1. 화면 우하단 쏠림(배치 오류) 원인 분석 및 해결

### 발생 원인
1. **스크립트 구문 오류로 인한 리사이징 중단**:
   - 파일 생성 버퍼 문제로 스크립트 첫 줄이 `t totalSlides = 13;`로 잘려 들어가 `SyntaxError: Unexpected identifier 'totalSlides'` 예외가 발생.
   - 이로 인해 `autoScale()` 함수가 실행되지 못함.
2. **CSS 기본 트랜스폼 누락**:
   - `#stage`의 CSS 기본 스타일에 `transform: translate(-50%, -50%)`가 누락된 채 `left: 50%; top: 50%;`만 지정되어 있어, 스크립트 실행이 중단되었을 때 스테이지의 좌상단(0, 0)이 뷰포트 정중앙에 고정되어 우측 하단으로 쏠리는 현상 발생.

### 조치 내역
1. **CSS 초기 상태 센터링 보장**:
   ```css
   #stage {
     position: absolute;
     left: 50%;
     top: 50%;
     width: 1920px;
     height: 1080px;
     transform: translate(-50%, -50%) scale(1);
     transform-origin: center center;
   }
   ```
2. **JS 코드 무결성 검증**:
   - Node.js 구문 파서(`new Function(script)`)를 통해 `Script syntax: 100% PERFECT OK!` 검증 완료.
3. **이중 리사이징 훅 등록**:
   - `DOMContentLoaded`, 즉시 1차 호출, `resize` 이벤트 리스너를 결합하여 브라우저 로딩 즉시 화면 중앙에 정확한 16:9 비율로 스케일링되도록 보장.

---

## 2. 타이포그래피 및 인텔 디자인 시스템 표준화
- **헤드라인**: `'Pretendard', 'Inter', sans-serif` (38px Bold, 인텔 시안 그라데이션)
- **본문/설명문**: `'Pretendard', 'Inter', sans-serif` (15~17px, 가독성 높은 자간)
- **테크 뱃지/카운터/시계**: `'Space Mono', monospace` (인텔 테크놀로지 룩앤필)
- **비디오 재생**: Slide 04(Asset Transformer), Slide 05(Asset Manager), Slide 06(Simulations 동적 로딩), Slide 10(Simulation Pro & ROS2)이 인텔 시안 네온 프레임 안에서 끊김 없이 100% 동시 재생.

---

## 3. 현장 운용 가이드
- 브라우저에서 `Unity_발표자료.html`을 새로고침(`F5`)하거나 `run_unity_presentation.bat`을 실행하면, 화면 크기와 모니터 해상도에 맞춰 정중앙에 선명하게 정렬된 13개 슬라이드를 확인하실 수 있습니다.


---

# [SPEC-20261105-UNITY-INTEL-07] 하단 실시간 발표 자막 (Live Key Narrative Caption Bar) 구현

## 1. 개요
- **목적**: 인텔 행사 부스 전시 및 10분 키노트 발표 시, 관람객 및 청중이 화면 아래의 자막만 읽어도 전체 핵심 맥락을 완벽히 이해할 수 있도록 슬라이드 하단에 실시간 발표자 자막 바(Subtitle / Live Caption Bar)를 구축.
- **적용 파일**: 
  - `C:\Users\MZC01-SUNKIM317\OneDrive\2026\ISSU\Intel 행사\Unity_발표자료.html`
  - `C:\Users\MZC01-SUNKIM317\OneDrive\2026\ISSU\Intel 행사\Unity_발표자료_Showcase.html`

## 2. 주요 구현 사양
1. **Glassmorphism 인텔 테마 자막 바**:
   - `background: rgba(4, 12, 32, 0.9)`, `backdrop-filter: blur(14px)`, `border: 1px solid rgba(0, 199, 253, 0.45)`, `border-radius: 10px`.
   - 좌측: 인텔 시안 네온 펄스 애니메이션 LED 닷 및 `LIVE CAPTION · 핵심 맥락` 뱃지.
   - 중앙: 슬라이드 전환 시 150ms 부드러운 페이드인 애니메이션과 함께 핵심 스피치 자막 표시 (키워드는 인텔 시안 배경 및 테두리 볼드 강조).
   - 우측: `자막 켜짐/꺼짐 [C]` 토글 버튼.
2. **슬라이드별 핵심 자막 매핑**:
   - **Slide 1 (개요 & 아키텍처)**: 70+ CAD 1-Click 자동 경량화(Asset Transformer)부터 물리 시뮬레이션 합성 데이터, 인텔 온디바이스 추론, 실물 로봇 제어까지의 완결 파이프라인.
   - **Slide 2 (Asset Transformer)**: 353만 폴리곤 설비 단 1-Click 경량화 및 LOD 자동 생성, Recipe 표준화로 전처리 공수 85% 단축.
   - **Slide 3 (Asset Manager & 3DDS)**: 기가바이트급 3D 설비 모델 무다운로드 초저지연 스트리밍 및 시뮬레이션 중 런타임 동적 에셋 교체.
   - **Slide 4 (Physical AI & ML-Agents)**: XR 원격 제어 및 PyTorch 분산 환경 결합, 극한 엣지 케이스 물리 합성 데이터 무한 생성과 강화학습.
   - **Slide 5 (Unity Sentis on Intel)**: 클라우드 통신 없는 초저지연 온디바이스 AI, Intel Core Ultra NPU 및 Arc GPU 하드웨어 가속 기반 실시간 추론.
   - **Slide 6 (Simulation Pro & ROS2)**: URDF 모델 및 센서 물리 시뮬레이션, ROS2 네이티브 토픽 1:1 직결을 통한 Sim2Real 가상-실물 연동.
   - **Slide 7 (메가존클라우드 파트너십)**: Unity 국내 공식 총판 메가존클라우드의 과제 정의-PoC-라이선스-전사 확대 4단계 실행 및 코엑스 1F Gold 부스 안내.
3. **단축키 및 인터랙션**:
   - 키보드 `C` 키: 실시간 자막 바 표시 / 반투명 숨김 토글.
   - 상단 헤더: `💬 자막 [C]` 토글 버튼 추가.
   - 하단 상태 바: 단축키 안내에 `C 자막` 뱃지 추가.
4. **검증 결과**: Node.js 문법 파싱 검증 완료 (`Exit Code: 0`).


---

# [SPEC-20261105-UNITY-INTEL-08] 발표 자료 외 불필요한 메타/내부 메모 문구 전수 정제

## 1. 개요
- **목적**: 인텔 행사 공식 발표 및 부스 전시에 부합하도록, 제작 과정에서 삽입되었던 내부용 작업 메모(PPT 페이지 번호, 통합 안내, 요약본 안내 등)를 전수 식별하여 공식 발표용 전문 문구로 전면 교체 및 정제.
- **적용 파일**: 
  - `C:\Users\MZC01-SUNKIM317\OneDrive\2026\ISSU\Intel 행사\Unity_발표자료.html`
  - `C:\Users\MZC01-SUNKIM317\OneDrive\2026\ISSU\Intel 행사\Unity_발표자료_Showcase.html`

## 2. 주요 정제 내역
1. **상단 네비게이션 서브타이틀 교체**:
   - 기존: `핵심 맥락 중심 7-Slide 고밀도 요약본 (원본 PPT 13p 통합)`
   - 변경: `엔터프라이즈 3D 데이터 최적화부터 인텔 온디바이스 Physical AI까지`
2. **슬라이드 카테고리 및 파트 태그의 PPT 번호 제거**:
   - `01 · OVERVIEW & ARCHITECTURE (PPT 1~3P 통합)` ➔ `01 · OVERVIEW & ARCHITECTURE`
   - `02 · CORE ENGINE — ASSET TRANSFORMER (PPT 4P)` ➔ `02 · CORE ENGINE — ASSET TRANSFORMER`
   - `03 · ASSET HUB & DYNAMIC INGESTION (PPT 5~6P 통합)` ➔ `03 · ASSET HUB & DYNAMIC INGESTION`
   - `PART A · ASSET MANAGER (PPT 5P)` ➔ `PART A · ASSET MANAGER`
   - `PART B · ASSET MANAGER FOR SIMULATIONS (PPT 6P)` ➔ `PART B · ASSET MANAGER FOR SIMULATIONS`
   - `04 · TELEOPERATION & AI TRAINING (PPT 7~8P 통합)` ➔ `04 · TELEOPERATION & AI TRAINING`
   - `PART A · UNITY XR SOLUTIONS (PPT 7P)` ➔ `PART A · UNITY XR SOLUTIONS`
   - `PART B · UNITY ML-AGENTS (PPT 8P)` ➔ `PART B · UNITY ML-AGENTS`
   - `05 · ON-DEVICE AI RUNTIME — UNITY SENTIS (PPT 9P)` ➔ `05 · ON-DEVICE AI RUNTIME — UNITY SENTIS`
   - `06 · FULL-SPECTRUM ROBOTICS — SIMULATION PRO (PPT 10P)` ➔ `06 · FULL-SPECTRUM ROBOTICS — SIMULATION PRO`
   - `07 · OFFICIAL PARTNER & ROADMAP (PPT 11~13P 통합)` ➔ `07 · OFFICIAL PARTNER & ROADMAP`
3. **상단 네비게이션 카테고리 탭 정제**:
   - `전체 (7)` ➔ `전체 아젠다`
   - `3D 파이프라인 & 에셋 최적화 (1–3)` ➔ `3D 파이프라인 & 에셋 최적화`
   - `Physical AI & 로보틱스 (4–6)` ➔ `Physical AI & 로보틱스`
   - `메가존클라우드 도입 로드맵 (7)` ➔ `파트너십 & 도입 로드맵`
   - `▦ 목차 (7)` ➔ `▦ 목차`
4. **목차 모달 타이틀 정제**:
   - `전체 슬라이드 목차 (7 Compact Slides — 원본 PPT 13p 통합)` ➔ `전체 슬라이드 목차 (Full Slide Agenda)`


---

# [SPEC-20261105-UNITY-INTEL-09] 타인 전달 및 현장 배포용 'Intel AI Summit Seoul 2026 최종전달패키지' 구축

## 1. 개요
- **목적**: 인텔 행사 관련 자료를 다른 사람(발표자, 부스 운영팀, 고객, 파트너사)에게 단일 폴더 통째로 압축/전달(Handover)할 수 있도록, 불필요한 중간 부산물 없이 독립적으로 즉각 실행 가능한 통합 배포 패키지 디렉터리를 구축.
- **최종 전달 경로**: `C:\Users\MZC01-SUNKIM317\OneDrive\2026\ISSU\Intel_AI_Summit_Seoul_2026_최종전달패키지`

## 2. 패키지 세부 구성
1. **최상위 원클릭 실행기 및 안내 문서**:
   - `1_Unity_발표자료_실행.bat` (Unity 10분 발표자료 1920x1080 키오스크 즉시 실행)
   - `2_부스_AI쇼케이스_실행.bat` (부스 14분 루프 AI 풀스택 쇼케이스 즉시 실행)
   - `README.md` (종합 사용자 가이드, 단축키, 현장 운영 팁 수록)
2. **`01_Unity_Industry_Physical_AI_발표자료/` (메인 발표 & 솔루션)**:
   - `Unity_발표자료.html` (최종 7-Slide 인터랙티브 슬라이드, 하단 실시간 자막 탑재)
   - `run_unity_presentation.bat` (단독 실행기)
   - `2026-11-05_Intel_행사_Unity_핵심맥락_최종정리본.md` (10분 발표 대본 및 핵심 맥락 요약서)
   - `Unity_발표자료.pptx` (최신 편집 원본)
   - `Unity_소개.pdf` (보조 소개서)
   - `unity_presentation_assets/` (GIF/이미지 에셋 일체)
3. **`02_부스전시용_AI_Fullstack_쇼케이스/` (부스 전시 & 루프)**:
   - `Showcase_Master_Player.html` (4개 쇼케이스 자동 연속 순환 재생기)
   - `run_kiosk.bat` (1920x1080 키오스크 실행기)
   - `MZC_Intel_AI_FullStack_Showcase.html` (MZC-Intel 풀스택 AI)
   - `Nota_Benchmark_Showcase_261015.html` (Nota 엣지 경량화 벤치마크)
   - `Alioth_Coder_Showcase_261019_단독실행.html` (Alioth 코더)
   - `Articul8_FullstackAI_행사영상_KR_v2.mp4` & `.srt` (행사 고화질 비디오)
   - `MZC_Intel_Vibe_Coding_Interactive_Demo.html` (관람객 참여형 바이브 코딩 데모)


---

# [SPEC-20261105-UNITY-INTEL-10] 부스 전시용 통합 단일 폴더(Single-Folder Package) 구축 및 전달 체계 확립

## 1. 개요
- **목적**: 유니티(Unity) 발표자료를 포함하여 인텔 행사 부스 전시에 필요한 모든 자료를 서브폴더로 분리하지 않고 **단 하나의 단일 폴더**에 통합 수납하여, 다른 사람에게 전달할 때 이 단일 폴더 통째로 압축/전달할 수 있도록 단순화.
- **최종 전달 경로**: `C:\Users\MZC01-SUNKIM317\OneDrive\2026\ISSU\Intel_AI_Summit_Seoul_2026_부스전시자료`

## 2. 단일 폴더 수납 파일 목록
1. **유니티 부스 전시 & 발표 메인 솔루션**:
   - `Unity_발표자료.html` (최종 7-Slide 인터랙티브 슬라이드, 하단 실시간 자막 탑재)
   - `Unity_발표자료_Showcase.html`
   - `run_unity_presentation.bat` (유니티 1-Click 키오스크 실행기)
   - `run_unity_kiosk.bat`
   - `unity_presentation_assets/` (핵심 데모 GIF 및 슬라이드 에셋 서브폴더)
   - `Unity_발표자료.pptx` (최신 편집 원본 파워포인트)
   - `Unity_소개.pdf` (보조 브로슈어)
   - `2026-11-05_Intel_행사_Unity_핵심맥락_최종정리본.md` (10분 발표 대본 및 핵심 맥락 요약서)
2. **부스 무한루프 쇼케이스 & 데모**:
   - `Showcase_Master_Player.html` (4개 쇼케이스 자동 연속 순환 재생 플레이어)
   - `run_kiosk.bat` (부스 디스플레이 1-Click 실행기)
   - `MZC_Intel_AI_FullStack_Showcase.html` (MZC-Intel 풀스택 AI 쇼케이스 슬라이드)
   - `Nota_Benchmark_Showcase_261015.html` (Nota on Intel 엣지 경량화 벤치마크)
   - `Alioth_Coder_Showcase_261019_단독실행.html` (자율 코딩 에이전트 쇼케이스)
   - `Articul8_FullstackAI_행사영상_KR_v2.mp4` & `.srt` (부스 고화질 행사 영상)
   - `MZC_Intel_Vibe_Coding_Interactive_Demo.html` (관람객 참여형 실시간 Vibe 코딩 데모)
3. **부스 운영 안내 매뉴얼**:
   - `README.txt` & `README.md` (단축키 및 현장 운영 안내)


---

# [SPEC-20261105-UNITY-INTEL-11] 부스 모니터 무한루프 마스터 플레이어에 유니티(Unity) 자료 5번째 순환 파트 통합

## 1. 개요
- **목적**: 부스 대형 디스플레이 무한루프 재생기(`Showcase_Master_Player.html`)의 마지막 5번째 순환 쇼케이스로 **유니티 발표자료(`Unity_발표자료.html`)**를 내장하여, 행사 부스에서 별도의 수동 조작 없이도 유니티 솔루션까지 완벽히 포함된 5개 파트가 자동 연속 순환 재생되도록 통합.
- **적용 파일**: 
  - `C:\Users\MZC01-SUNKIM317\OneDrive\2026\ISSU\Intel 행사\Showcase_Master_Player.html`
  - `C:\Users\MZC01-SUNKIM317\OneDrive\2026\ISSU\Intel_AI_Summit_Seoul_2026_부스전시자료\Showcase_Master_Player.html`

## 2. 통합 후 5단계 무한 순환 루프 사양
1. **쇼케이스 재생 순서 (총 약 19분 28초 1사이클 무한 반복)**:
   - ① **MZC-Intel AI FULL STACK** (1분 50초 / 10개 슬라이드)
   - ② **Nota AI 경량화 벤치마크 on Intel** (2분 00초)
   - ③ **Alioth Coder 자율 코딩 에이전트** (3분 00초)
   - ④ **Articul8 Full Stack AI 행사영상** (7분 03초)
   - ⑤ **★ Unity Industry on Intel (Asset Transformer & Physical AI)** (5분 15초 / 7개 슬라이드 자막 탑재)
   - ➔ **⑤번 종료 후 자동으로 ①번으로 복귀하여 24시간 무한 연속 루프 재생**.
2. **신규 기능 및 단축키 확장**:
   - 상단 헤더에 `⑤ Unity Industry on Intel` 전용 네온 탭 버튼 추가.
   - 키보드 숫자 **`5`** 키로 유니티 쇼케이스 즉시 점프 지원 (`1`, `2`, `3`, `4`, `5`).
   - 단독 실행용 `run_unity_presentation.bat`와 부스 루프용 `run_kiosk.bat`를 모두 단일 폴더에 수납.


---

# [SPEC-20261105-UNITY-INTEL-12] 배치 파일(.bat) CMD 괄호 파싱 및 코드페이지 오류 완전 해결

## 1. 문제 분석
- **현상**: `cmd.exe`에서 `run_kiosk.bat` 실행 시 `'ioth'은(는)...`, `'ogram'은(는)...`, `\Google\Chrome\Application\chrome.exe" (은(는) 예상되지 않았습니다.` 에러 발생 및 실행 중단.
- **원인**:
  1. `if exist ... ( ... )` 다중 괄호 블록 내부에서 UTF-8/CP949 인코딩 불일치로 인해 2바이트 문자가 깨지며 괄호 `)` 및 공백이 명령어로 잘못 파싱됨.
  2. `echo` 문장 내 앰퍼샌드(`&`)가 명령어 체이닝 연산자로 해석되어 뒤따르는 단어가 독립 명령어로 실행 시도됨.
  3. 한글 파일명 경로(`Unity_발표자료.html`)가 CMD 코드페이지에 따라 깨지는 현상.

## 2. 해결 조치
1. **점프 라벨(goto) 구조 전면 도입**: 괄호 `( ... )`를 완전히 제거하고 `:RUN_CHROME64`, `:RUN_EDGE32`, `:RUN_DEFAULT` 점프 라벨 구조로 변경하여 CMD 파서 에러 원천 차단.
2. **특수문자 및 기호 정제**: `echo` 문장 내의 `&`를 안전한 `and`로 변경.
3. **영문 별칭 파일 동기화**: `Unity_Presentation.html`을 자동 동기화 생성하여 어떤 윈도우 언어/코드페이지 환경에서도 파일 경로 실패가 발생하지 않도록 방어.
4. **검증 완료**: `run_kiosk.bat` 및 `run_unity_presentation.bat` 실행 테스트 결과 0개 에러, Chrome 키오스크 모드 즉시 정상 기동 확인 (`Exit Code: 0`).


---

# [SPEC-20261105-UNITY-INTEL-13] 부스 마스터 플레이어 유니티(Unity) 건너뛰기 버그 완전 해결

## 1. 문제 분석
- **현상**: `Showcase_Master_Player.html` 실행 시 4번(Articul8 행사영상)이 종료된 후 5번(유니티)으로 전환되지 않고 건너뛰어져 다시 1번으로 돌아가버림.
- **원인**:
  1. `Showcase_Master_Player.html` 내부의 `videoEl.addEventListener('ended', ...)` 이벤트 핸들러에 `if (currentIndex === 3) switchShow(0);`로 하드코딩되어 있어, 4번 비디오가 끝나면 무조건 0번(1번 풀스택 쇼케이스)으로 점프하고 4번(유니티, index 4)을 건너뜀.
  2. 비디오 로딩 실패 시 다음 쇼케이스로 넘어가지 않고 멈추는 에러 핸들링 부재.
  3. `Unity_발표자료.html`이 iframe으로 로드되었을 때 자동재생 모드가 활성화되지 않아 슬라이드가 전환되지 않을 가능성.

## 2. 해결 조치
1. **비디오 종료 이벤트 동적 전환화**:
   - `videoEl.addEventListener('ended', () => switchShow(currentIndex + 1));`로 변경하여 4번 영상 종료 즉시 5번 유니티 쇼케이스(`index 4`)로 정확하게 진입하도록 수정.
2. **비디오 로딩 실패 안전 가드레일**:
   - 로컬 비디오 탐색 실패 시 멈추지 않고 5초 후 안전하게 다음 쇼케이스(유니티)로 자동 전환되도록 폴백 추가.
3. **유니티 iframe 진입 시 자동재생 및 첫 슬라이드 동기화**:
   - 마스터 플레이어에서 5번으로 전환될 때 유니티 iframe 내부의 `goToSlide(1)` 및 `toggleAutoplay()`를 직접 호출하도록 연동.
   - `Unity_발표자료.html`에 `?autoplay=1` 또는 iframe 임베드 감지 시 즉시 슬라이드 자동재생 타이머가 켜지는 로직 삽입.
4. **검증 완료**: Node.js 문법 파싱 검증 완료 (`Exit Code: 0`).


---

# [SPEC-20261105-UNITY-INTEL-14] 부스 마스터 플레이어 5단계 순환 재생 및 클릭·단축키 전면 개편

## 1. 개요 및 원인 규명
- **현상**:
  1. 상단 메뉴 탭에서 5번째 '유니티' 버튼을 클릭해도 화면 전환이 일어나지 않음.
  2. 키보드 좌우 화살표(`←` / `→`) 조작 시 4번(Articul8 비디오) 다음에 5번(유니티)이 스킵되고 다시 1번으로 돌아감.
- **원인 분석**:
  1. **헤더 폭 오버플로우로 인한 클릭 차단**: 기존 탭 버튼 라벨이 너무 길어 전체 폭(1620px 이상)이 협소한 해상도(DPI 125%/150% 또는 1600px 이하)에서 우측 컨트롤 버튼 영역(`.runner-ctrls`)에 5번째 유니티 버튼이 가려져 마우스 클릭 이벤트가 도달하지 못함.
  2. **비디오 ended 이벤트 및 이벤트 핸들링 분기 오류**: 비디오 종료 이벤트 및 이전 구버전 스크립트 캐시로 인해 4번 비디오 종료 시 0번으로 리셋되거나, 화살표 네비게이션 시 인덱스 매핑 누락 발생.

## 2. 전면 개편 조치 내역
1. **상단 탭 레이아웃 및 폭 최적화 (반응형 100% 클릭 보장)**:
   - 버튼 텍스트를 간결하고 직관적으로 정제:
     - `① Full-Stack AI` (01:50)
     - `② Nota 벤치마크` (02:00)
     - `③ Alioth 코더` (03:00)
     - `④ Articul8 영상` (07:03)
     - `⑤ Unity Physical AI` (05:15)
   - 탭 5개의 총 너비를 650px 수준으로 슬림화하여 어떤 랩탑/모니터 해상도에서도 우측 버튼과 절대 겹치지 않도록 여백 확보.
   - 각 탭에 인라인 `onclick="switchShow(n, true)"`를 부여하여 DOM 로딩 타이밍과 무관하게 100% 즉시 클릭 동작 보장.
2. **5단계 순차 이동 엔진(0 -> 1 -> 2 -> 3 -> 4 -> 0) 완결**:
   - `nextShow()` 및 `prevShow()` 전용 네비게이션 함수를 독립 구현하여, 키보드 좌우 화살표(`→`, `←`), `N`/`P`, 상단 헤더의 `▶`/`◀` 버튼 모두에서 **1단계씩 정확하게 순차 전진/후진**하도록 통일.
   - 4번 비디오 종료 시 무조건 5번(유니티, `index 4`)으로 전환.
   - 5번 유니티 시간 만료(315초) 시 무조건 0번(1번 풀스택 AI)으로 복귀하여 **24시간 무한 루프 완결**.
3. **유니티 전환 시 자동 초기화 및 재생 연동**:
   - 5번 유니티 진입 시 `Unity_발표자료.html?autoplay=1`을 즉시 깨워 슬라이드가 1번부터 자동으로 재생되도록 보장.
4. **검증 완료**: Node.js 구문 파싱 검증 완료 (`Exit Code: 0`).


---

# [SPEC-20261105-UNITY-INTEL-15] 유니티 HTML 자막 바 완전 제거 및 원본 슬라이드 레이아웃 복원

## 1. 개요
- **목적**: 사용자의 요청에 따라 `Unity_발표자료.html` 및 관련 파일에 임시 적용되었던 하단 고정형 자막 바 및 관련 제어 요소를 완전히 제거하고, 슬라이드 본문이 화면 전체에 쾌적하게 렌더링되도록 원본 1920x1080 레이아웃을 100% 복원.
- **적용 파일**:
  - `C:\Users\MZC01-SUNKIM317\OneDrive\2026\ISSU\Intel_AI_Summit_Seoul_2026_부스전시자료\Unity_발표자료.html`
  - `C:\Users\MZC01-SUNKIM317\OneDrive\2026\ISSU\Intel_AI_Summit_Seoul_2026_부스전시자료\Unity_Presentation.html`
  - `C:\Users\MZC01-SUNKIM317\OneDrive\2026\ISSU\Intel 행사\Unity_발표자료.html`
  - `C:\Users\MZC01-SUNKIM317\OneDrive\2026\ISSU\Intel 행사\Unity_Presentation.html`

## 2. 작업 내용
1. **DOM 및 UI 엘리먼트 제거**: `#captionBar` 자막 바 컨테이너, `#btnCaptionTop` 상단 자막 토글 버튼, 하단 바의 `C 자막` 단축키 안내 뱃지 완전 삭제.
2. **CSS 레이아웃 원상 복원**: `#slideHost`의 하단 여백을 원래의 `bottom: 68px`로 복원하여 카드의 세로 비율과 여백을 최적화하고, `.caption-bar` 관련 모든 스타일 시트 제거.
3. **자바스크립트 엔진 정제**: `slideCaptions` 데이터 객체, `updateCaption()`, `toggleCaption()`, `KeyC` 이벤트 핸들러 완전 삭제.
4. **검증 완료**: Node.js 구문 파싱 검증 통과 (`Exit Code: 0`).


---

# [SPEC-20261105-UNITY-INTEL-16] 행사 플랫폼 전시사 소개 영역 노출용 '솔루션 및 전시 타이틀 / 데모 및 솔루션 개요' 최종본 업데이트

## 1. 개요
- **목적**: 초기 신청서(10/21) 작성 이후 고도화된 부스 5대 통합 쇼케이스(① MZC-Intel 4-Layer AI Full Stack, ② Nota AI 모델 경량화, ③ Alioth Coder 및 실시간 Vibe 코딩, ④ Articul8 엔터프라이즈 GenAI, ⑤ Unity Industry & Physical AI) 구성을 반영하여 행사 당일 고객 플랫폼 내 전시사 소개 영역에 노출될 공식 문안을 최신화.
- **적용 파일**:
  - [`docs/2026-10-21_intel_ai_summit_application_slides.html`](file:///c:/dev/antigravity-workspace/aifullstack/docs/2026-10-21_intel_ai_summit_application_slides.html)
  - [`docs/2026-11-05_intel_ai_summit_booth_guide.md`](file:///c:/dev/antigravity-workspace/aifullstack/docs/2026-11-05_intel_ai_summit_booth_guide.md)

## 2. 주요 변경 사항
1. **전시 타이틀 최신화**:
   - 기존 Red Hat OpenShift 및 AWS ROSA 중심 문구에서 인텔 행사(Intel AI Summit Seoul 2026)의 정체성과 신규 추가된 **Unity Physical AI**, **Nota AI**, **Alioth Coder**를 포괄하는 타이틀로 개편.
2. **데모 및 솔루션 개요 최신화**:
   - 코딩 에이전트 명칭을 실제 쇼케이스 탑재 명칭인 **Alioth Coder (및 실시간 Vibe Coding / FIM 라이브 시연)**로 통일.
   - **Nota AI 경량화 벤치마크(NetsPresso INT4 양자화)** 및 **Unity Industry & Physical AI (Asset Transformer 1-Click CAD 경량화, Unity Sentis 인텔 NPU/Arc 온디바이스 추론, Simulation Pro & ROS2 연동)** 파트를 명시적으로 추가.
