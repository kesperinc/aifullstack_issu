# -*- coding: utf-8 -*-
"""
인텔 행사 Unity 발표 및 부스 전시 산출물을 git docs 디렉터리에 완벽 동기화하는 스크립트
"""

import os
import shutil

repo_root = r"c:\dev\antigravity-workspace\aifullstack"
docs_dir = os.path.join(repo_root, "docs")
specs_dir = os.path.join(docs_dir, "specs")
os.makedirs(specs_dir, exist_ok=True)

booth_dir = r"C:\Users\MZC01-SUNKIM317\OneDrive\2026\ISSU\Intel_AI_Summit_Seoul_2026_부스전시자료"

# 1. 문서 파일 복사
# 기획서
src_plan = os.path.join(repo_root, "agentsmith", "docs", "2026-11-05_Unity_Asset_Transformer_Physical_AI_발표기획서.md")
dest_plan = os.path.join(docs_dir, "2026-11-05_unity_asset_transformer_physical_ai_plan.md")
if os.path.exists(src_plan):
    shutil.copy2(src_plan, dest_plan)
    print(f"[Copied] {dest_plan}")

# 최종정리본
src_summary = os.path.join(booth_dir, "2026-11-05_Intel_행사_Unity_핵심맥락_최종정리본.md")
dest_summary = os.path.join(docs_dir, "2026-11-05_intel_ai_summit_unity_executive_summary.md")
if os.path.exists(src_summary):
    shutil.copy2(src_summary, dest_summary)
    print(f"[Copied] {dest_summary}")

# 상세명세서
src_spec = os.path.join(repo_root, "agentsmith", "coding-agent", "docs", "specs", "2026-11-05_Unity_Asset_Transformer_Physical_AI_상세명세서.md")
dest_spec = os.path.join(specs_dir, "2026-11-05_unity_asset_transformer_physical_ai_specs.md")
if os.path.exists(src_spec):
    shutil.copy2(src_spec, dest_spec)
    print(f"[Copied] {dest_spec}")

# 부스 통합 안내서
src_readme = os.path.join(booth_dir, "README.md")
dest_readme = os.path.join(docs_dir, "2026-11-05_intel_ai_summit_booth_guide.md")
if os.path.exists(src_readme):
    shutil.copy2(src_readme, dest_readme)
    print(f"[Copied] {dest_readme}")

# 2. 핵심 HTML 및 배치파일 복사
# Unity 발표자료 HTML
src_u_html = os.path.join(booth_dir, "Unity_발표자료.html")
dest_u_html = os.path.join(docs_dir, "2026-11-05_unity_industry_physical_ai_presentation.html")
if os.path.exists(src_u_html):
    shutil.copy2(src_u_html, dest_u_html)
    print(f"[Copied] {dest_u_html}")

# 부스 5단계 마스터 플레이어 HTML
src_master_html = os.path.join(booth_dir, "Showcase_Master_Player.html")
dest_master_html = os.path.join(docs_dir, "2026-11-05_intel_summit_master_player_v2.html")
if os.path.exists(src_master_html):
    shutil.copy2(src_master_html, dest_master_html)
    print(f"[Copied] {dest_master_html}")

# 3. 임시 파이썬 스크립트 정리 (scripts/tools 폴더로 이동 또는 정리)
tools_dir = os.path.join(repo_root, "scripts", "tools")
os.makedirs(tools_dir, exist_ok=True)

temp_scripts = [
    "add_subtitles.py",
    "add_unity_autoplay_trigger.py",
    "clean_meta_text.py",
    "create_single_booth_package.py",
    "fix_batch_files.py",
    "fix_showcase_skip.py",
    "force_integrate_shows.py",
    "integrate_unity_to_showcase.py",
    "overhaul_master_player.py",
    "package_intel_event.py",
    "perfect_batch_patch.py"
]

for s in temp_scripts:
    sp = os.path.join(repo_root, s)
    if os.path.exists(sp):
        shutil.move(sp, os.path.join(tools_dir, s))
        print(f"[Moved to tools] {s}")

print("SUCCESS: Synchronized all docs and cleaned root directory!")
