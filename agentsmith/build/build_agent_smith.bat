@echo off
chcp 65001 > NUL
title Agent Smith IDE - Custom VS Code Fork & Gulp Build System

echo =================================================================
echo 🤖 Agent Smith IDE - 1-Click VS Code Fork & Gulp Builder
echo =================================================================
echo.

set BASE_DIR=%~dp0..\..
set AGENT_SMITH_DIR=%BASE_DIR%\agentsmith
set VSCODE_DIR=%AGENT_SMITH_DIR%\vscode
set PATCHES_DIR=%AGENT_SMITH_DIR%\patches
set BUILD_DIR=%AGENT_SMITH_DIR%\build
set EXTENSION_DIR=%AGENT_SMITH_DIR%\extension

:: 1. 디렉터리 생성 및 준비
if not exist "%VSCODE_DIR%" mkdir "%VSCODE_DIR%"
if not exist "%PATCHES_DIR%" mkdir "%PATCHES_DIR%"
if not exist "%EXTENSION_DIR%" mkdir "%EXTENSION_DIR%"

:: 2. 필수 빌드 종속성 검사 (Harness)
echo [1/4] Checking compile dependencies...
where node >nul 2>nul
if %errorlevel% neq 0 (
    echo [FAIL] Node.js가 감지되지 않았습니다. LTS 버전을 먼저 설치하십시오.
    exit /b 1
) else (
    for /f "tokens=*" %%i in ('node -v') do set NODE_VER=%%i
    echo      [OK] Node.js Version: %NODE_VER%
)

where yarn >nul 2>nul
if %errorlevel% neq 0 (
    echo [WARNING] Yarn 패키지 매니저가 감지되지 않았습니다. npm을 통해 글로벌 설치를 시도합니다...
    call npm install -g yarn
) else (
    for /f "tokens=*" %%i in ('yarn -v') do set YARN_VER=%%i
    echo      [OK] Yarn Version: %YARN_VER%
)

where git >nul 2>nul
if %errorlevel% neq 0 (
    echo [FAIL] Git이 감지되지 않았습니다. 빌드를 위해 Git을 먼저 설치하십시오.
    exit /b 1
)

echo.

:: 3. 오리지널 Code-OSS 레포지토리 클론 및 체크아웃
echo [2/4] Cloning/Syncing Microsoft Code-OSS Upstream...
if not exist "%VSCODE_DIR%\.git" (
    echo      [Action] Cloning microsoft/vscode (Tag: 1.86.0) into %VSCODE_DIR%...
    git clone --depth 1 --branch 1.86.0 https://github.com/microsoft/vscode.git "%VSCODE_DIR%"
) else (
    echo      [OK] Microsoft Code-OSS 리포지토리가 이미 존재합니다. 동기화를 건너뜁니다.
)
echo.

:: 4. patches/ 내 커스텀 UI/브랜딩 패치 자동 적용
echo [3/4] Checking and applying Agent Smith custom branding patches...
set PATCH_APPLIED=0
if exist "%PATCHES_DIR%\*.patch" (
    echo      [Action] Applying custom patches inside %PATCHES_DIR%...
    cd /d "%VSCODE_DIR%"
    for %%f in ("%PATCHES_DIR%\*.patch") do (
        echo        Applying %%~nxf...
        git apply "%%f" && set PATCH_APPLIED=1
    )
    if %PATCH_APPLIED% equ 1 (
        echo      [OK] 모든 커스텀 브랜딩 및 텔레메트리 제거 패치가 적용되었습니다.
    ) else (
        echo      [WARNING] 패치 적용 도중 오류가 발생했거나 변경점이 없습니다.
    )
) else (
    echo      [NOTICE] 적용할 패치 파일(*.patch)이 존재하지 않습니다. 순수 Code-OSS로 가동합니다.
    echo               (향후 에디터 브랜딩 패치 추가 시 자동 적용됩니다.)
)
echo.

:: 5. Code-OSS 빌드 의존성 인스톨 및 가동 준비
echo [4/4] Installing Code-OSS compile dependencies (Yarn)...
cd /d "%VSCODE_DIR%"
:: Gulp 빌드를 위한 의존성 설치
call yarn install --frozen-lockfile

echo.
echo =================================================================
echo 🎉 Agent Smith IDE 컴파일 환경 구성 완료!
echo   * 오리지널 코드 경로: %VSCODE_DIR%
echo   * 향후 'yarn run watch' 또는 'yarn run compile'로 실행할 수 있습니다.
echo =================================================================
echo.
pause
