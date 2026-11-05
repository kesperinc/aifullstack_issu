# -*- coding: utf-8 -*-
"""
Unity_발표자료.html에 부스 모드 및 ?autoplay=1 감지 자동 재생 로직 추가
"""

import os
import re

folders = [
    r"C:\Users\MZC01-SUNKIM317\OneDrive\2026\ISSU\Intel_AI_Summit_Seoul_2026_부스전시자료",
    r"C:\Users\MZC01-SUNKIM317\OneDrive\2026\ISSU\Intel 행사"
]

auto_trigger_code = """
  // URL 파라미터(?autoplay=1) 또는 부스 iframe 임베드 시 자동재생 활성화
  const urlParams = new URLSearchParams(window.location.search);
  const isEmbed = window.self !== window.top;
  if (urlParams.get('autoplay') === '1' || urlParams.get('kiosk') === '1' || isEmbed) {
    if (!isAutoplay) {
      toggleAutoplay();
    }
  }
"""

for folder in folders:
    if not os.path.exists(folder):
        continue

    for fn in ["Unity_발표자료.html", "Unity_Presentation.html", "Unity_발표자료_Showcase.html"]:
        fp = os.path.join(folder, fn)
        if not os.path.exists(fp):
            continue

        with open(fp, "r", encoding="utf-8") as f:
            html = f.read()

        if "urlParams.get('autoplay')" not in html:
            html = html.replace("startTimerLoop();", "startTimerLoop();\n" + auto_trigger_code)
            with open(fp, "w", encoding="utf-8") as f:
                f.write(html)
            print(f"[Autoplay Added] {fp}")

print("SUCCESS: Added URL/embed autoplay trigger to all Unity presentation files!")

