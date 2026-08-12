@echo off
chcp 65001 > NUL
title VibeForge AI - Local Desktop Runner Launcher

echo =================================================================
echo 🚀 Antigravity VibeForge Enterprise - 1-Click Desktop Launcher
echo =================================================================
echo.

if exist .venv\Scripts\python.exe (
    echo [OK] Launching with Virtual Environment Python (.venv)...
    .venv\Scripts\python.exe agentsmith/coding-agent/src/desktop_runner.py
) else (
    echo [WARNING] Virtual environment .venv not found. Using system python...
    python agentsmith/coding-agent/src/desktop_runner.py
)

pause
