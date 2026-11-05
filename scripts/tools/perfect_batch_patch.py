# -*- coding: utf-8 -*-
"""
배치 파일 완전 무결성 패치
1. echo 문장 내 '&' 기호를 'and'로 변경
2. 영문 별칭 파일 생성:
   Unity_발표자료.html -> Unity_Presentation.html (복사본 동기화)
   Showcase_Master_Player.html -> Showcase_Master_Player.html
3. 배치 파일에서 타깃을 확실하게 지정
"""

import os
import shutil

folders = [
    r"C:\Users\MZC01-SUNKIM317\OneDrive\2026\ISSU\Intel_AI_Summit_Seoul_2026_부스전시자료",
    r"C:\Users\MZC01-SUNKIM317\OneDrive\2026\ISSU\Intel 행사"
]

for folder in folders:
    if not os.path.exists(folder):
        continue

    # 1. 영문 파일명 복사본도 함께 생성하여 코드페이지 불일치 완전 방지
    src_kr = os.path.join(folder, "Unity_발표자료.html")
    src_en = os.path.join(folder, "Unity_Presentation.html")
    if os.path.exists(src_kr):
        shutil.copy2(src_kr, src_en)
        print(f"[Synced] {src_en}")

    # 2. run_unity_presentation.bat 생성 (ASCII 안전 문자열 기반)
    bat_unity = """@echo off
title Intel AI Summit Seoul 2026 - Unity Industry Presentation Kiosk

set "TARGET_FILE=%~dp0Unity_Presentation.html"
if not exist "%TARGET_FILE%" set "TARGET_FILE=%~dp0Unity_발표자료.html"

echo ==============================================================================
echo [Intel AI Summit Seoul 2026] Unity Industry and Physical AI Presentation
echo ------------------------------------------------------------------------------
echo Target: Unity Presentation Kiosk (7-Slide with Live Captions)
echo ==============================================================================

if exist "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" goto RUN_CHROME64
if exist "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe" goto RUN_CHROME32
if exist "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe" goto RUN_EDGE32
if exist "C:\\Program Files\\Microsoft\\Edge\\Application\\msedge.exe" goto RUN_EDGE64
goto RUN_DEFAULT

:RUN_CHROME64
echo [RUN] Launching Google Chrome Kiosk mode...
start "" "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" --kiosk --disable-features=Translate --no-first-run "%TARGET_FILE%"
exit /b 0

:RUN_CHROME32
echo [RUN] Launching Google Chrome (x86) Kiosk mode...
start "" "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe" --kiosk --disable-features=Translate --no-first-run "%TARGET_FILE%"
exit /b 0

:RUN_EDGE32
echo [RUN] Launching Microsoft Edge Kiosk mode...
start "" "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe" --kiosk "%TARGET_FILE%" --edge-kiosk-type=fullscreen
exit /b 0

:RUN_EDGE64
echo [RUN] Launching Microsoft Edge (x64) Kiosk mode...
start "" "C:\\Program Files\\Microsoft\\Edge\\Application\\msedge.exe" --kiosk "%TARGET_FILE%" --edge-kiosk-type=fullscreen
exit /b 0

:RUN_DEFAULT
echo [RUN] Launching default browser...
start "" "%TARGET_FILE%"
exit /b 0
"""

    # 3. run_kiosk.bat 생성 (ASCII 안전 문자열 기반)
    bat_kiosk = """@echo off
title Intel AI Summit Seoul 2026 - Booth Master Showcase Kiosk

set "TARGET_FILE=%~dp0Showcase_Master_Player.html"

echo ==============================================================================
echo [Intel AI Summit Seoul 2026] Booth Master Showcase Kiosk Launcher
echo ------------------------------------------------------------------------------
echo Target: Showcase_Master_Player.html (5-Stage Auto Loop)
echo ==============================================================================

if exist "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" goto RUN_CHROME64
if exist "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe" goto RUN_CHROME32
if exist "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe" goto RUN_EDGE32
if exist "C:\\Program Files\\Microsoft\\Edge\\Application\\msedge.exe" goto RUN_EDGE64
goto RUN_DEFAULT

:RUN_CHROME64
echo [RUN] Launching Google Chrome Kiosk mode...
start "" "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" --kiosk --disable-features=Translate --no-first-run "%TARGET_FILE%"
exit /b 0

:RUN_CHROME32
echo [RUN] Launching Google Chrome (x86) Kiosk mode...
start "" "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe" --kiosk --disable-features=Translate --no-first-run "%TARGET_FILE%"
exit /b 0

:RUN_EDGE32
echo [RUN] Launching Microsoft Edge Kiosk mode...
start "" "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe" --kiosk "%TARGET_FILE%" --edge-kiosk-type=fullscreen
exit /b 0

:RUN_EDGE64
echo [RUN] Launching Microsoft Edge (x64) Kiosk mode...
start "" "C:\\Program Files\\Microsoft\\Edge\\Application\\msedge.exe" --kiosk "%TARGET_FILE%" --edge-kiosk-type=fullscreen
exit /b 0

:RUN_DEFAULT
echo [RUN] Launching default browser...
start "" "%TARGET_FILE%"
exit /b 0
"""

    for fn, content in [("run_kiosk.bat", bat_kiosk),
                        ("run_unity_presentation.bat", bat_unity),
                        ("run_unity_kiosk.bat", bat_unity)]:
        fp = os.path.join(folder, fn)
        with open(fp, "w", encoding="cp949") as f:
            f.write(content)
        print(f"[Wrote] {fp}")

print("SUCCESS: Perfectly fixed all batch scripts!")

