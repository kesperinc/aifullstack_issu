# 2026-10-26 MZC AI Full Stack 전시 부스 쇼케이스 상세명세서

- **작성일자**: 2026-10-26
- **대상 행사**: Red Hat 행사 전시 부스 (상설 자동 재생)
- **최종 배포 위치**: `C:\Users\MZC01-SUNKIM317\OneDrive\2026\ISSU\Redhat 행사\final\`

---

## 1. 최종 구조: 마스터 러너 방식

원본 쇼케이스 파일들을 하나로 합치지 않고, 러너 HTML이 iframe/video로 순서대로 불러와 재생한다.

| 순서 | 파트 | 파일 | 재생 시간 |
|:---:|:---|:---|:---|
| ① | AI Full Stack | `MZC_AI_FullStack_Showcase_261026.html` | 약 110초 |
| ② | Nota AI 경량화 | `Nota_Benchmark_Showcase_261015.html` (원본) | 약 120초 |
| ③ | Alioth 코더 | `Alioth_Coder_Showcase_261019_단독실행.html` (원본) | 약 180초 |
| ④ | Articul8 행사영상 | `Articul8_FullstackAI_행사영상_KR_v2.mp4` | 423초 (영상 종료 시 전환) |

④번이 끝나면 ①번으로 돌아가 반복한다.

## 2. 방식 변경 이력

1. **1차 (폐기)**: 3개 파일을 하나의 HTML로 합친 통합본 (`2026-10-26_mzc_ai_fullstack_integrated_showcase.html`)
   - 원본 스크립트 간 변수 충돌(`CASES`, `IDLE_MS`, `dotsEl`)과 CSS 충돌(`body` 여백, 슬라이드 패딩)로 화면이 깨짐
   - 저장소에 커밋하지 않음 (로컬에만 남음)
2. **2차 (최종)**: 마스터 러너 방식으로 변경. 원본 파일을 수정하지 않아 충돌이 생기지 않음
3. ① AI Full Stack 슬라이드의 좌우 여백을 80px에서 140px로 넓힘 (사용자 피드백 반영)
4. ④ Articul8 행사영상 추가

## 3. 변경 파일 맵 (Specs Map)

| 파일 | 구분 | 설명 |
|:---|:---|:---|
| `docs/2026-10-26_showcase_master_player.html` | 신규 | 마스터 러너: 4개 파트 순차 재생, 상단 컨트롤 바, 단축키, 비디오 경로 폴백 |
| `docs/2026-10-26_mzc_ai_fullstack_showcase.html` | 신규 | ① AI Full Stack 10장 슬라이드 (작업본) |
| `docs/MZC_AI_FullStack_Showcase_261026.html` | 신규 | ① 배포용 사본 (러너가 이 파일명을 참조) |
| `docs/Nota_Benchmark_Showcase_261015.html` | 신규(복사) | ② Nota 원본 사본 |
| `docs/Alioth_Coder_Showcase_261019_단독실행.html` | 신규(복사) | ③ Alioth 원본 사본 (시연 영상 Base64 내장, 약 9MB) |
| `docs/run_kiosk.bat` | 신규 | 크롬/엣지 키오스크 모드 실행 |
| `docs/specs/2026-10-26_ai_fullstack_showcase_spec.md` | 신규 | 본 명세서 |

**저장소에서 제외한 파일**
- `Articul8_FullstackAI_행사영상_KR_v2.mp4` (33MB): 용량이 커서 제외. OneDrive `final` 폴더에서 관리
- `2026-10-26_mzc_ai_fullstack_integrated_showcase.html` (18MB): 폐기된 1차 통합본

> 저장소의 `docs/`에는 mp4가 없으므로, 거기서 러너를 열면 ④번 영상은 재생되지 않는다. 행사용은 OneDrive `final` 폴더를 사용한다.

## 4. 운영 단축키

`1~4` 파트 이동 · `Space` 일시정지 · `N/→` 다음 · `P/←` 이전 · `M` 소리 · `F` 전체화면
