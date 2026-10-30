@echo off
chcp 65001 > nul
title [Intel AI Summit Seoul 2026] MZC-Intel AI FULL STACK Master Showcase

echo ==============================================================================
echo [Intel AI Summit Seoul 2026] MZC-Intel AI FULL STACK 4-파트 마스터 쇼케이스
echo ------------------------------------------------------------------------------
echo 대상 파일: 2026-10-30_intel_ai_summit_showcase_runner.html
echo 구성:
echo   1. MZC-Intel AI FULL STACK (10 Slides)
echo   2. Nota on Intel (NetsPresso 경량화)
echo   3. Alioth Coder (자율 코딩 에이전트)
echo   4. Articul8 행사영상 (Intel-Backed GenAI Platform)
echo 
echo 조작 단축키:
echo   - 1 ~ 4 : 파트 1~4 즉시 이동
echo   - Space : 일시정지 / 재생
echo   - N / -> : 다음 파트
echo   - P / <- : 이전 파트
echo   - M : 비디오 음소거 토글
echo   - F : 전체화면 토글
echo ==============================================================================

set TARGET_FILE=%~dp02026-10-30_intel_ai_summit_showcase_runner.html

if exist "C:\Program Files\Google\Chrome\Application\chrome.exe" (
    echo [실행] Google Chrome 키오스크 모드로 실행합니다...
    start "" "C:\Program Files\Google\Chrome\Application\chrome.exe" --kiosk --disable-features=Translate --no-first-run "%TARGET_FILE%"
    exit /b 0
)

if exist "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" (
    echo [실행] Google Chrome (x86) 키오스크 모드로 실행합니다...
    start "" "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" --kiosk --disable-features=Translate --no-first-run "%TARGET_FILE%"
    exit /b 0
)

if exist "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" (
    echo [실행] Microsoft Edge 키오스크 모드로 실행합니다...
    start "" "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --kiosk "%TARGET_FILE%" --edge-kiosk-type=fullscreen
    exit /b 0
)

start "" "%TARGET_FILE%"

