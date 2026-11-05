# -*- coding: utf-8 -*-
"""
Showcase_Master_Player.html에 마지막 5번째 쇼케이스로
'Unity Industry on Intel (Asset Transformer & Physical AI)'를 통합하는 스크립트
"""

import re
import os

target_paths = [
    r"C:\Users\MZC01-SUNKIM317\OneDrive\2026\ISSU\Intel 행사\Showcase_Master_Player.html",
    r"C:\Users\MZC01-SUNKIM317\OneDrive\2026\ISSU\Intel_AI_Summit_Seoul_2026_부스전시자료\Showcase_Master_Player.html"
]

for file_path in target_paths:
    if not os.path.exists(file_path):
        continue

    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. 탭 버튼 추가 (timer3 뒤에 timer4 추가)
    tab_html = """    <button class="runner-tab unity-tab" data-index="4">
      <span>⑤ Unity Industry on Intel</span>
      <span class="tab-timer" id="timer4">05:15</span>
    </button>
  </nav>"""
    if 'data-index="4"' not in html:
        html = re.sub(r'</button>\s*</nav>', '</button>\n' + tab_html, html, count=1)

    # 2. frame4 iframe 추가 (videoWrapper 뒤에 추가)
    frame_html = """  <iframe class="show-item" id="frame4" src="Unity_발표자료.html"></iframe>
</main>"""
    if 'id="frame4"' not in html:
        html = re.sub(r'</div>\s*</main>', '</div>\n' + frame_html, html, count=1)

    # 3. SHOWS 배열에 Unity 쇼케이스 객체 추가
    shows_addition = """,
  {
    name: 'Unity Industry on Intel (Asset Transformer & Physical AI)',
    type: 'iframe',
    file: 'Unity_발표자료.html',
    durationSec: 315,
    id: 'frame4'
  }
];"""
    if 'Unity Industry on Intel' not in html:
        html = re.sub(r'id:\s*[\'"]videoWrapper[\'"]\s*\n\s*\}\s*\n\];', "id: 'videoWrapper'\n  }" + shows_addition, html, count=1)

    # 4. 키보드 단축키 '5' 추가
    html = html.replace("['1', '2', '3', '4'].includes(e.key)", "['1', '2', '3', '4', '5'].includes(e.key)")

    # 5. 유니티 탭 전용 네온 스타일 추가 (옵션)
    unity_css = """
  .runner-tab.unity-tab.active {
    background: rgba(32, 227, 178, 0.16);
    border-color: #20E3B2;
    color: #20E3B2;
    box-shadow: 0 0 14px rgba(32, 227, 178, 0.35);
  }
"""
    if ".runner-tab.unity-tab.active" not in html:
        html = html.replace("</style>", unity_css + "\n</style>")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)

print("SUCCESS: Updated Showcase_Master_Player.html with Unity Industry 5th show!")

