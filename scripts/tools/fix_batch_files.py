# -*- coding: utf-8 -*-
"""
배치 파일(.bat)의 인코딩 및 괄호 파싱 에러를 완벽히 해결하는 스크립트
- 괄호 블록 ( ... ) 을 제거하고 표준 goto 라벨 점프 구조로 변경
- 한국어 Windows cmd.exe 표준 CP949 인코딩으로 저장
- 한글 경로 및 파일명을 안전하게 따옴표(" ") 처리
"""

import os

folders = [
    r"C:\Users\MZC01-SUNKIM317\OneDrive\2026\ISSU\Intel_AI_Summit_Seoul_2026_부스전시자료",
    r"C:\Users\MZC01-SUNKIM317\OneDrive\2026\ISSU\Intel 행사"
]

bat_kiosk_code = """@echo off
title [Intel AI Summit Seoul 2026] Booth Master Showcase Kiosk
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

bat_unity_code = """@echo off
title [Intel AI Summit Seoul 2026] Unity Industry Presentation Kiosk
set "TARGET_FILE=%~dp0Unity_발표자료.html"

echo ==============================================================================
echo [Intel AI Summit Seoul 2026] Unity Industry & Physical AI Presentation
echo ------------------------------------------------------------------------------
echo Target: Unity_발표자료.html (7-Slide Interactive Presentation with Live Captions)
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

for folder in folders:
    if not os.path.exists(folder):
        continue

    # CP949 인코딩으로 저장 (Windows cmd.exe 완벽 호환)
    p_kiosk = os.path.join(folder, "run_kiosk.bat")
    with open(p_kiosk, "w", encoding="cp949") as f:
        f.write(bat_kiosk_code)
    print(f"[Updated] {p_kiosk}")

    p_unity = os.path.join(folder, "run_unity_presentation.bat")
    with open(p_unity, "w", encoding="cp949") as f:
        f.write(bat_unity_code)
    print(f"[Updated] {p_unity}")

    # run_unity_kiosk.bat도 동일하게 통일
    p_unity_kiosk = os.path.join(folder, "run_unity_kiosk.bat")
    with open(p_unity_kiosk, "w", encoding="cp949") as f:
        f.write(bat_unity_code)
    print(f"[Updated] {p_unity_kiosk}")

print("\nSUCCESS: All batch files rewritten with fail-safe label jumps and CP949 encoding!")

