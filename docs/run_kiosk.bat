@echo off
chcp 65001 > nul
title MZC Enterprise AI Full Stack Kiosk Runner

echo ========================================================
echo   MZC Enterprise AI Full Stack Exhibition Runner
echo   순서: AI Full Stack -> Nota -> Alioth 연속 자동 순환
echo ========================================================
echo.

set "TARGET_FILE=%~dp0Showcase_Master_Player.html"

:: Chrome 전체화면 키오스크 시도
if exist "C:\Program Files\Google\Chrome\Application\chrome.exe" (
    start "" "C:\Program Files\Google\Chrome\Application\chrome.exe" --kiosk "%TARGET_FILE%"
    goto :done
)
if exist "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" (
    start "" "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" --kiosk "%TARGET_FILE%"
    goto :done
)

:: Edge 전체화면 키오스크 시도
if exist "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" (
    start "" "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --kiosk "%TARGET_FILE%"
    goto :done
)

:: 기본 브라우저 실행
start "" "%TARGET_FILE%"

:done
exit
