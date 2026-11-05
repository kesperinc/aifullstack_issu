# -*- coding: utf-8 -*-
"""
Showcase_Master_Player.html에 SHOWS 5개 완전 통합 스크립트
"""

import os
import re

target_paths = [
    r"C:\Users\MZC01-SUNKIM317\OneDrive\2026\ISSU\Intel_AI_Summit_Seoul_2026_부스전시자료\Showcase_Master_Player.html",
    r"C:\Users\MZC01-SUNKIM317\OneDrive\2026\ISSU\Intel 행사\Showcase_Master_Player.html"
]

shows_array_code = """const SHOWS = [
  {
    name: 'MZC-Intel AI FULL STACK (10 Slides)',
    type: 'iframe',
    file: 'MZC_Intel_AI_FullStack_Showcase.html',
    durationSec: 110,
    id: 'frame0'
  },
  {
    name: 'Nota AI 경량화 벤치마크 on Intel',
    type: 'iframe',
    file: 'Nota_Benchmark_Showcase_261015.html',
    durationSec: 120,
    id: 'frame1'
  },
  {
    name: 'Alioth Coder 자율 코딩 에이전트',
    type: 'iframe',
    file: 'Alioth_Coder_Showcase_261019_단독실행.html',
    durationSec: 180,
    id: 'frame2'
  },
  {
    name: 'Articul8 Full Stack AI 행사영상',
    type: 'video',
    file: 'Articul8_FullstackAI_행사영상_KR_v2.mp4',
    durationSec: 423,
    id: 'videoWrapper'
  },
  {
    name: 'Unity Industry on Intel (Asset Transformer & Physical AI)',
    type: 'iframe',
    file: 'Unity_발표자료.html?autoplay=1',
    durationSec: 315,
    id: 'frame4'
  }
];"""

nav_tabs_code = """  <nav class="runner-nav">
    <button class="runner-tab active" data-index="0">
      <span>① MZC-Intel AI FULL STACK</span>
      <span class="tab-timer" id="timer0">01:50</span>
    </button>
    <button class="runner-tab" data-index="1">
      <span>② Nota on Intel</span>
      <span class="tab-timer" id="timer1">02:00</span>
    </button>
    <button class="runner-tab" data-index="2">
      <span>③ Alioth Coder</span>
      <span class="tab-timer" id="timer2">03:00</span>
    </button>
    <button class="runner-tab video-tab" data-index="3">
      <span>④ Articul8 영상</span>
      <span class="tab-timer" id="timer3">07:03</span>
    </button>
    <button class="runner-tab unity-tab" data-index="4">
      <span>⑤ Unity Industry on Intel</span>
      <span class="tab-timer" id="timer4">05:15</span>
    </button>
  </nav>"""

frame_container_code = """<main id="frameContainer">
  <iframe class="show-item active" id="frame0" src="MZC_Intel_AI_FullStack_Showcase.html"></iframe>
  <iframe class="show-item" id="frame1" src="Nota_Benchmark_Showcase_261015.html"></iframe>
  <iframe class="show-item" id="frame2" src="Alioth_Coder_Showcase_261019_단독실행.html"></iframe>

  <div class="show-item" id="videoWrapper">
    <video id="articul8Video" playsinline preload="auto" muted controls="false"></video>
    <div id="videoOverlayPlay" title="클릭하여 영상 재생"><div class="play-circle">▶</div></div>
  </div>

  <iframe class="show-item" id="frame4" src="Unity_발표자료.html?autoplay=1"></iframe>
</main>"""

for file_path in target_paths:
    if not os.path.exists(file_path):
        continue

    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. runner-nav 교체
    html = re.sub(r'<nav class="runner-nav">.*?</nav>', nav_tabs_code, html, flags=re.DOTALL)

    # 2. frameContainer 교체
    html = re.sub(r'<main id="frameContainer">.*?</main>', frame_container_code, html, flags=re.DOTALL)

    # 3. SHOWS 배열 교체
    html = re.sub(r'const SHOWS\s*=\s*\[.*?\];', shows_array_code, html, flags=re.DOTALL)

    # 4. ended 이벤트 교체
    html = re.sub(
        r"videoEl\.addEventListener\('ended'.*?\}\);",
        "videoEl.addEventListener('ended', () => { switchShow(currentIndex + 1); });",
        html,
        flags=re.DOTALL
    )

    # 5. switchShow 안전 보강
    # newIndex 범위 체크
    switch_body = """function switchShow(newIndex, manual = false) {
  if (newIndex < 0) newIndex = SHOWS.length - 1;
  if (newIndex >= SHOWS.length) newIndex = 0;

  // 이전 항목 비활성화
  const prevShow = SHOWS[currentIndex];
  const prevEl = document.getElementById(prevShow.id);
  if (prevEl) prevEl.classList.remove('active');

  if (prevShow.type === 'video') {
    videoEl.pause();
    videoOverlay.classList.remove('show');
  }

  currentIndex = newIndex;
  elapsedSec = 0;

  // 다음 항목 활성화
  const nextShow = SHOWS[currentIndex];
  const nextEl = document.getElementById(nextShow.id);
  if (nextEl) nextEl.classList.add('active');

  if (nextShow.type === 'video') {
    videoEl.currentTime = 0;
    const playPromise = videoEl.play();
    if (playPromise !== undefined) {
      playPromise.catch(() => videoOverlay.classList.add('show'));
    }
  } else if (nextShow.id === 'frame4') {
    try {
      const uFrame = document.getElementById('frame4');
      if (uFrame && uFrame.contentWindow) {
        if (typeof uFrame.contentWindow.goToSlide === 'function') {
          uFrame.contentWindow.goToSlide(1);
        }
        if (uFrame.contentWindow.isAutoplay === false && typeof uFrame.contentWindow.toggleAutoplay === 'function') {
          uFrame.contentWindow.toggleAutoplay();
        }
      }
    } catch(e) {
      console.log('Unity frame message:', e);
    }
  }

  updateTabs();
  updateProgress();
  showToast(`${currentIndex + 1}단계: ${nextShow.name}`);
}"""
    html = re.sub(r'function switchShow\(newIndex, manual = false\)\s*\{.*?showToast\([^)]+\);\s*\}', switch_body, html, flags=re.DOTALL)

    # 6. 단축키 1..5 확실히 반영
    html = re.sub(r"\['1',\s*'2',\s*'3',\s*'4'\]\.includes\(e\.key\)", "['1', '2', '3', '4', '5'].includes(e.key)", html)

    # 7. 유니티 탭 스타일 보강
    if ".runner-tab.unity-tab" not in html:
        u_style = """
  .runner-tab.unity-tab.active {
    background: rgba(32, 227, 178, 0.16) !important;
    border-color: #20E3B2 !important;
    color: #20E3B2 !important;
    box-shadow: 0 0 14px rgba(32, 227, 178, 0.35) !important;
  }
"""
        html = html.replace("</style>", u_style + "\n</style>")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"[Updated] {file_path}")

print("SUCCESS: Perfectly integrated 5 shows into Showcase_Master_Player.html!")

