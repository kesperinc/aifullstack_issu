#!/usr/bin/env bash
# =================================================================
# 🚀 Antigravity VibeForge Enterprise - 1-Click Linux/macOS Launcher
# (Equivalent to run_desktop.bat script specification)
# =================================================================

export LANG=C.UTF-8
export LC_ALL=C.UTF-8

echo "================================================================="
echo "🚀 Antigravity VibeForge Enterprise - 1-Click Desktop Launcher"
echo "   'Intent-Driven Autonomous Coding Platform for Enterprise'"
echo "================================================================="
echo ""

# Find Python Executable in Virtual Environment
if [ -f ".venv/bin/python" ]; then
    echo "[OK] Launching with Virtual Environment Python (.venv)..."
    .venv/bin/python agentsmith/coding-agent/src/desktop_runner.py
elif [ -f ".venv/bin/python3" ]; then
    echo "[OK] Launching with Virtual Environment Python3 (.venv)..."
    .venv/bin/python3 agentsmith/coding-agent/src/desktop_runner.py
else
    echo "[WARNING] Virtual environment .venv not found. Using system python3..."
    python3 agentsmith/coding-agent/src/desktop_runner.py
fi

echo ""
read -p "Press [Enter] key to exit..." dummy
