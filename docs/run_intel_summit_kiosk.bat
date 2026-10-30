@echo off
chcp 65001 > nul
title [Intel AI Summit Seoul 2026] MegazoneCloud Booth Master Kiosk Launcher

echo ==============================================================================
echo [Intel AI Summit Seoul 2026] 메가존클라우드 부스 키오스크 실행기
echo ------------------------------------------------------------------------------
echo 대상 파일: 2026-10-30_intel_summit_master_player.html
echo 모드: Fullscreen Kiosk Mode (1920x1080)
echo 조작키 안내:
echo   - 1 ~ 4 : 파트 1~4 즉시 이동
echo   - Space : 일시정지 / 재생
echo   - N / -> : 다음 파트
echo   - P / <- : 이전 파트
echo   - F : 전체화면 토글
echo   - Alt+F4 / ESC : 종료
echo ==============================================================================

set TARGET_FILE=%~dp02026-10-30_intel_summit_master_player.html

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

echo [안내] 전용 브라우저 경로를 찾지 못하여 기본 브라우저로 엽니다...
start "" "%TARGET_FILE%"
