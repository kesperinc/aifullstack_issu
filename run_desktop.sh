#!/usr/bin/env bash
# VibeForge AI - 1-Click Linux / macOS Desktop Runner Script

echo "================================================================="
echo "🚀 Antigravity VibeForge Enterprise - 1-Click Desktop Launcher"
echo "================================================================="
echo ""

if [ -f ".venv/bin/python" ]; then
    echo "[OK] Launching with Virtual Environment Python (.venv)..."
    .venv/bin/python mvp/coding-agent/src/desktop_runner.py
else
    echo "[WARNING] Virtual environment .venv not found. Using system python3..."
    python3 mvp/coding-agent/src/desktop_runner.py
fi
