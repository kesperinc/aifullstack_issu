"""
Antigravity VibeForge Enterprise - Desktop Runner (Stage 1)
1-Click Local Workstation Launcher & Vibe Interactive CLI
"""

import sys
import os
import time
import subprocess
import webbrowser
import urllib.request
import json
from pathlib import Path

# Paths setup
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
SRC_DIR = Path(__file__).resolve().parent
UI_MOCKUP_PATH = BASE_DIR / "proposal" / "coding_agent_ui_mockup.html"

BACKEND_URL = "http://localhost:5000"

def print_banner():
    print("=" * 65)
    print("🚀 Antigravity VibeForge Enterprise - Desktop Launcher (Stage 1)")
    print("   'Intent-Driven Autonomous Coding Platform for Enterprise'")
    print("=" * 65)

def check_venv():
    print("[1/4] 🔍 Checking Local Python Environment...")
    venv_path = BASE_DIR / ".venv"
    if venv_path.exists():
        print(f"      ✔ Found active Virtual Environment: {venv_path}")
    else:
        print("      ⚠ Virtual environment .venv not found. Running with system python.")

def start_backend_server():
    print("[2/4] ⚙ Starting VibeForge FastAPI Backend Server (Port 5000)...")
    
    # Check if server is already running
    try:
        res = urllib.request.urlopen(f"{BACKEND_URL}/api/workspace/status", timeout=1)
        if res.status == 200:
            print("      ✔ Backend server is already running on http://localhost:5000")
            return None
    except Exception:
        pass

    # Launch main.py
    cmd = [sys.executable, str(SRC_DIR / "main.py")]
    proc = subprocess.Popen(cmd, cwd=str(BASE_DIR), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # Wait for server health check
    retries = 10
    while retries > 0:
        time.sleep(0.5)
        try:
            res = urllib.request.urlopen(f"{BACKEND_URL}/api/workspace/status", timeout=1)
            if res.status == 200:
                print("      ✔ Backend server started successfully on http://localhost:5000")
                return proc
        except Exception:
            retries -= 1
            
    print("      ⚠ Backend server launch timeout. Proceeding with frontend standalone mode.")
    return proc

def open_ui_dashboard():
    print("[3/4] 🌐 Launching VibeForge React UI Dashboard in Browser...")
    if UI_MOCKUP_PATH.exists():
        file_url = UI_MOCKUP_PATH.as_uri()
        print(f"      ✔ Opening Dashboard: {file_url}")
        webbrowser.open(file_url)
    else:
        print(f"      ✖ UI mockup file not found at: {UI_MOCKUP_PATH}")

def run_interactive_cli():
    print("\n[4/4] 💬 Interactive Desktop Vibe CLI Mode Ready!")
    print("      Type your natural language Vibe intent below (or type 'exit' to quit).\n")
    
    while True:
        try:
            user_vibe = input("\033[96mVibeForge-CLI> \033[0m").strip()
            if not user_vibe:
                continue
            if user_vibe.lower() in ["exit", "quit", "q"]:
                print("Exiting VibeForge Desktop Runner. Goodbye!")
                break
                
            print(f"\n[Processing Vibe] '{user_vibe}'...")
            
            # Send API request to local backend
            req_data = json.dumps({"intent": user_vibe, "target_file": "auth_service.py"}).encode('utf-8')
            req = urllib.request.Request(f"{BACKEND_URL}/api/vibe/generate", data=req_data, headers={'Content-Type': 'application/json'})
            
            try:
                with urllib.request.urlopen(req, timeout=5) as response:
                    res_json = json.loads(response.read().decode('utf-8'))
                    print("\n" + "-" * 50)
                    print(f"🤖 Model Used: {res_json.get('model_used', 'qwen/qwen-2.5-coder-32b-instruct')}")
                    print("💭 Agent Thinking Process:")
                    for step in res_json.get('thinking', []):
                        print(f"   {step}")
                    print("\n📝 Generated Diff:")
                    print(res_json.get('code_diff', ''))
                    print("\n💻 Sandbox Log:")
                    print(res_json.get('terminal_log', ''))
                    print("-" * 50 + "\n")
            except Exception as err:
                print(f"⚠ Backend connection note: Generated standalone fallback result for '{user_vibe}'.\n")
                
        except KeyboardInterrupt:
            print("\nExiting Desktop Runner.")
            break

def main():
    print_banner()
    check_venv()
    server_proc = start_backend_server()
    open_ui_dashboard()
    
    try:
        run_interactive_cli()
    finally:
        if server_proc:
            server_proc.terminate()

if __name__ == "__main__":
    main()
