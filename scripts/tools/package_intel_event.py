# -*- coding: utf-8 -*-
"""
인텔 행사(Intel AI Summit Seoul 2026) 최종 전달용 통합 배포 패키지 구성 스크립트
위치: C:\\Users\\MZC01-SUNKIM317\\OneDrive\\2026\\ISSU\\Intel_AI_Summit_Seoul_2026_최종전달패키지
"""

import os
import shutil

src_root = r"C:\Users\MZC01-SUNKIM317\OneDrive\2026\ISSU\Intel 행사"
dest_root = r"C:\Users\MZC01-SUNKIM317\OneDrive\2026\ISSU\Intel_AI_Summit_Seoul_2026_최종전달패키지"

unity_dir = os.path.join(dest_root, "01_Unity_Industry_Physical_AI_발표자료")
booth_dir = os.path.join(dest_root, "02_부스전시용_AI_Fullstack_쇼케이스")

os.makedirs(unity_dir, exist_ok=True)
os.makedirs(booth_dir, exist_ok=True)

# 1. Unity Industry 발표 관련 필수 파일 복사
unity_files = [
    "Unity_발표자료.html",
    "Unity_발표자료_Showcase.html",
    "run_unity_presentation.bat",
    "run_unity_kiosk.bat",
    "Unity_발표자료.pptx",
    "Unity_소개.pdf",
    "2026-11-05_Intel_행사_Unity_핵심맥락_최종정리본.md"
]

for f in unity_files:
    src_f = os.path.join(src_root, f)
    if os.path.exists(src_f):
        shutil.copy2(src_f, os.path.join(unity_dir, f))
        print(f"[Unity Copied] {f}")

# Unity 에셋 폴더 복사
src_assets = os.path.join(src_root, "unity_presentation_assets")
dest_assets = os.path.join(unity_dir, "unity_presentation_assets")
if os.path.exists(dest_assets):
    shutil.rmtree(dest_assets)
shutil.copytree(src_assets, dest_assets)
print(f"[Unity Assets Copied] unity_presentation_assets folder")

# 2. 부스 전시용 AI Full-Stack 쇼케이스 파일 복사
booth_files = [
    "Showcase_Master_Player.html",
    "run_kiosk.bat",
    "MZC_Intel_AI_FullStack_Showcase.html",
    "Nota_Benchmark_Showcase_261015.html",
    "Alioth_Coder_Showcase_261019_단독실행.html",
    "Articul8_FullstackAI_행사영상_KR_v2.mp4",
    "Articul8_FullstackAI_행사영상_KR_v2.srt",
    "MZC_Intel_Vibe_Coding_Interactive_Demo.html"
]

for f in booth_files:
    src_f = os.path.join(src_root, f)
    if os.path.exists(src_f):
        shutil.copy2(src_f, os.path.join(booth_dir, f))
        print(f"[Booth Copied] {f}")

# 3. 루트 실행용 원클릭 배치파일 생성
root_bat_unity = """@echo off
chcp 65001 > nul
title Unity Industry & Physical AI 발표 실행
echo ========================================================
echo  Intel AI Summit Seoul 2026 - Unity Industry 발표자료 실행
echo ========================================================
cd /d "%~dp001_Unity_Industry_Physical_AI_발표자료"
call run_unity_presentation.bat
"""

root_bat_booth = """@echo off
chcp 65001 > nul
title MZC-Intel 부스 AI 쇼케이스 실행
echo ========================================================
echo  Intel AI Summit Seoul 2026 - 부스 전시용 쇼케이스 실행
echo ========================================================
cd /d "%~dp002_부스전시용_AI_Fullstack_쇼케이스"
call run_kiosk.bat
"""

with open(os.path.join(dest_root, "1_Unity_발표자료_실행.bat"), "w", encoding="utf-8") as f:
    f.write(root_bat_unity)

with open(os.path.join(dest_root, "2_부스_AI쇼케이스_실행.bat"), "w", encoding="utf-8") as f:
    f.write(root_bat_booth)

# 4. 종합 안내서 (README.md) 생성
readme_content = """# Intel AI Summit Seoul 2026 — 통합 전달 및 배포 패키지

**행사 일시:** 2026년 11월 12일(목) 코엑스 1F 그랜드볼룸 Gold 부스 및 세션룸  
**배포 대상:** 발표자, 현장 부스 운영팀, 기술 지원 엔지니어, 고객 전달용  
**총괄 주관:** 메가존클라우드(MegazoneCloud) AI & Unity 비즈니스 조직

---

## 📁 폴더 구성 요약

이 패키지는 다른 사람에게 전달할 때 그대로 복사/압축하여 전달할 수 있도록 구성되어 있습니다.

```
Intel_AI_Summit_Seoul_2026_최종전달패키지/
├── 📄 1_Unity_발표자료_실행.bat           <-- [1-Click] Unity 10분 키노트/발표자료 전체화면 실행
├── 📄 2_부스_AI쇼케이스_실행.bat          <-- [1-Click] 부스 루프 전시(Full-Stack AI) 전체화면 실행
│
├── 📂 01_Unity_Industry_Physical_AI_발표자료/   <-- [핵심] Unity 산업용 3D 에셋 & Physical AI 솔루션
│   ├── Unity_발표자료.html               (1920x1080 인터랙티브 슬라이드, 하단 실시간 자막 탑재)
│   ├── run_unity_presentation.bat        (단독 실행 배치파일)
│   ├── 2026-11-05_Intel_행사_Unity_핵심맥락_최종정리본.md (10분 발표 대본 및 핵심 맥락 요약서)
│   ├── Unity_발표자료.pptx               (편집/인쇄 가능한 최신 원본 파워포인트)
│   ├── Unity_소개.pdf                    (보조 브로슈어)
│   └── unity_presentation_assets/        (핵심 데모 비디오 GIF 및 고해상도 그래픽 에셋)
│
└── 📂 02_부스전시용_AI_Fullstack_쇼케이스/    <-- [부스] 현장 무한 루프 쇼케이스 & 체험형 데모
    ├── Showcase_Master_Player.html       (4개 쇼케이스 자동 연속 순환 재생 플레이어)
    ├── run_kiosk.bat                     (부스 디스플레이 전용 1920x1080 키오스크 실행기)
    ├── MZC_Intel_AI_FullStack_Showcase.html (MZC-Intel 풀스택 AI 쇼케이스 슬라이드)
    ├── Nota_Benchmark_Showcase_261015.html  (Nota on Intel 엣지 경량화 벤치마크)
    ├── Alioth_Coder_Showcase_261019_단독실행.html (자율 코딩 에이전트 쇼케이스)
    ├── Articul8_FullstackAI_행사영상_KR_v2.mp4 & srt (부스 고화질 행사 영상)
    └── MZC_Intel_Vibe_Coding_Interactive_Demo.html (관람객 참여형 실시간 Vibe 코딩 데모)
```

---

## 🚀 현장 실행 및 조작 방법

### 1) Unity Industry & Physical AI 발표 (세션 및 부스 설명)
- **실행**: 루트의 `1_Unity_발표자료_실행.bat` 더블클릭
- **주요 단축키**:
  - `←` / `→` : 이전 / 다음 슬라이드 이동
  - `Space` : 10분 자동 발표 모드 시작 / 일시정지 (슬라이드별 권장 타이머 연동)
  - `C` : **하단 실시간 발표 자막(Live Caption) On / Off** 토글
  - `G` : 7개 슬라이드 전체 목차 그리드 보기
  - `F` : 1920x1080 전체화면 모드 토글
  - `Esc` : 목차 닫기 또는 전체화면 종료

### 2) 부스 루프 전시 (대형 모니터 무한 재생)
- **실행**: 루트의 `2_부스_AI쇼케이스_실행.bat` 더블클릭
- **재생 순서 (약 14분 순환 루프)**:
  1. MZC-Intel AI FULL STACK (1분 50초)
  2. Nota on Intel 벤치마크 (2분)
  3. Alioth Coder 자율 코딩 에이전트 (3분)
  4. Articul8 행사 영상 (7분 3초)
- **단축키**:
  - `1`, `2`, `3`, `4`: 해당 쇼케이스 파트로 즉시 점프 (고객 문의 응대 시)
  - `Space`: 일시정지 / 재생
  - `M`: Articul8 영상 음소거(Mute) 해제 / 설정
  - `Alt + F4`: 키오스크 종료

---

## 💡 전달 시 유의사항
- 본 폴더(`Intel_AI_Summit_Seoul_2026_최종전달패키지`)를 ZIP 파일로 압축하여 이메일, 슬랙, 또는 USB 메모리로 그대로 전달하시면, 상대방 PC에서 브라우저만 설치되어 있으면 인터넷 연결 없이도 로컬에서 100% 정상 구동됩니다.
"""

with open(os.path.join(dest_root, "README.md"), "w", encoding="utf-8") as f:
    f.write(readme_content)

print(f"\n[ALL DONE] Successfully created distribution package at: {dest_root}")

