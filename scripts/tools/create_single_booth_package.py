# -*- coding: utf-8 -*-
"""
인텔 행사 부스 전시용 통합 단일 폴더 생성 스크립트
경로: C:\\Users\\MZC01-SUNKIM317\\OneDrive\\2026\\ISSU\\Intel_AI_Summit_Seoul_2026_부스전시자료
- 유니티와 부스 전시 자료를 하위 폴더 분리 없이 단 하나의 폴더에 통합
- 부스 전시 목적에 필요한 자료들만 선별 복사
- README.txt 및 README.md 종합 안내 매뉴얼 수록
"""

import os
import shutil

src_root = r"C:\Users\MZC01-SUNKIM317\OneDrive\2026\ISSU\Intel 행사"
dest_root = r"C:\Users\MZC01-SUNKIM317\OneDrive\2026\ISSU\Intel_AI_Summit_Seoul_2026_부스전시자료"

# 대상 폴더 생성 (기존 폴더가 있으면 정리 후 재생성)
if os.path.exists(dest_root):
    shutil.rmtree(dest_root)
os.makedirs(dest_root, exist_ok=True)

# 1. 단일 폴더에 복사할 부스 전시용 필수 파일 목록
booth_files = [
    # 유니티 부스 전시 & 발표 메인 솔루션
    "Unity_발표자료.html",
    "Unity_발표자료_Showcase.html",
    "run_unity_presentation.bat",
    "run_unity_kiosk.bat",
    "Unity_발표자료.pptx",
    "Unity_소개.pdf",
    "2026-11-05_Intel_행사_Unity_핵심맥락_최종정리본.md",

    # 부스 무한루프 쇼케이스 & 데모
    "Showcase_Master_Player.html",
    "run_kiosk.bat",
    "MZC_Intel_AI_FullStack_Showcase.html",
    "Nota_Benchmark_Showcase_261015.html",
    "Alioth_Coder_Showcase_261019_단독실행.html",
    "Articul8_FullstackAI_행사영상_KR_v2.mp4",
    "Articul8_FullstackAI_행사영상_KR_v2.srt",
    "MZC_Intel_Vibe_Coding_Interactive_Demo.html",
]

for filename in booth_files:
    src_f = os.path.join(src_root, filename)
    if os.path.exists(src_f):
        shutil.copy2(src_f, os.path.join(dest_root, filename))
        print(f"[Copied] {filename}")
    else:
        print(f"[Not Found] {filename}")

# 2. 유니티 에셋 폴더 복사 (HTML에서 상대경로로 참조)
src_assets = os.path.join(src_root, "unity_presentation_assets")
dest_assets = os.path.join(dest_root, "unity_presentation_assets")
shutil.copytree(src_assets, dest_assets)

# 에셋 내부의 임시 스크립트 정리
for f in os.listdir(dest_assets):
    if f.endswith(('.ps1', '.txt', '.json')):
        os.remove(os.path.join(dest_assets, f))
print("[Copied & Cleaned] unity_presentation_assets")

# 3. 단일 폴더용 부스 전시 통합 안내 매뉴얼 (README.txt & README.md)
readme_txt = """================================================================
 MZC-Intel AI 부스 전시 통합 패키지 (단일 폴더 배포용)
 행사명: Intel AI Summit Seoul 2026
 일시/장소: 2026-11-12(목) 코엑스 1F 그랜드볼룸 Gold 부스
 주관: 메가존클라우드(MegazoneCloud) AI & Unity 비즈니스 조직
================================================================

[ 핵심 1-Click 실행 안내 ]
  1. 유니티 부스 전시 / 발표 실행 : run_unity_presentation.bat 더블클릭
     -> 1920x1080 키오스크 모드로 즉시 실행 (슬라이드 하단 실시간 자막 탑재)
     -> 주요 단축키:
        - Space : 자동 재생 / 일시정지
        - C     : 하단 실시간 발표자 자막 On/Off 토글
        - G     : 전체 7개 슬라이드 목차 보기
        - F     : 전체화면 토글
        - Alt+F4: 종료

  2. 부스 쇼케이스 무한 루프 실행 : run_kiosk.bat 더블클릭
     -> 부스 대형 모니터용 14분 순환 루프 플레이어 즉시 실행
     -> 재생 순서: AI FULL STACK -> Nota AI -> Alioth Coder -> Articul8 영상
     -> 주요 단축키:
        - 1 / 2 / 3 / 4 : 해당 쇼케이스 파트로 즉시 점프
        - Space         : 일시정지 / 재생
        - M             : 영상 음소거 해제/설정
        - Alt+F4        : 종료

  3. 관람객 실시간 Vibe 코딩 체험 : MZC_Intel_Vibe_Coding_Interactive_Demo.html 열기
     -> AI 엔지니어 및 관람객 대상 실시간 파이썬/자바 Vibe 코딩 라이브 시연

================================================================
[ 단일 폴더 내 파일 목록 및 역할 ]
================================================================
  [유니티 부스 전시 솔루션]
  - Unity_발표자료.html                       : 유니티 부스 전시/발표 메인 HTML (자막 내장)
  - run_unity_presentation.bat               : 유니티 발표자료 1-Click 실행기
  - unity_presentation_assets/               : 핵심 데모 영상(GIF) 및 그래픽 에셋
  - 2026-11-05_Intel_행사_Unity_핵심맥락_최종정리본.md : 10분 발표 대본 및 핵심 맥락 요약서
  - Unity_발표자료.pptx                       : 최신 원본 파워포인트 (인쇄/편집용)
  - Unity_소개.pdf                            : 보조 소개 자료

  [부스 무한루프 쇼케이스]
  - Showcase_Master_Player.html              : 4개 쇼케이스 자동 연속 순환 재생기
  - run_kiosk.bat                            : 부스 쇼케이스 1-Click 실행기
  - MZC_Intel_AI_FullStack_Showcase.html     : MZC-Intel 풀스택 AI 쇼케이스
  - Nota_Benchmark_Showcase_261015.html      : Nota on Intel 엣지 경량화 벤치마크
  - Alioth_Coder_Showcase_261019_단독실행.html : Alioth 코더 에이전트 쇼케이스
  - Articul8_FullstackAI_행사영상_KR_v2.mp4   : Articul8 행사 고화질 영상
  - Articul8_FullstackAI_행사영상_KR_v2.srt   : 행사 영상 한글 자막

  [관람객 체험 데모]
  - MZC_Intel_Vibe_Coding_Interactive_Demo.html : Vibe 코딩 & FIM 라이브 시연기

================================================================
[ 타인 전달 방법 ]
================================================================
이 폴더('Intel_AI_Summit_Seoul_2026_부스전시자료')를 통째로 ZIP으로 압축하여
이메일, 슬랙, USB 등으로 전달하시면 받는 분 PC에서 브라우저만으로 즉시 작동합니다.
"""

with open(os.path.join(dest_root, "README.txt"), "w", encoding="utf-8") as f:
    f.write(readme_txt)

with open(os.path.join(dest_root, "README.md"), "w", encoding="utf-8") as f:
    f.write(readme_txt)

# 이전 서브폴더 분리형 패키지 디렉터리가 있다면 정리
old_dest = r"C:\Users\MZC01-SUNKIM317\OneDrive\2026\ISSU\Intel_AI_Summit_Seoul_2026_최종전달패키지"
if os.path.exists(old_dest):
    shutil.rmtree(old_dest)
    print(f"[Cleaned old folder] {old_dest}")

print(f"\n[SUCCESS] Single-folder booth package created at:\n{dest_root}")

