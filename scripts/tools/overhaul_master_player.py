# -*- coding: utf-8 -*-
"""
Showcase_Master_Player.html 완전 무결성 전면 개편
- 5개 탭 폭 최적화 (어떤 해상도에서도 겹침 없는 100% 클릭 보장)
- 인라인 onclick 바인딩으로 클릭 무조건 동작
- 0 -> 1 -> 2 -> 3 -> 4 -> 0 순차 실행 100% 보장
- 비디오 ended 이벤트 시 확실하게 4(Unity)로 전환
- 좌우 화살표 (키보드 및 상단 이전/다음 버튼) 순차 이동 완벽 보장
"""

import os

folders = [
    r"C:\Users\MZC01-SUNKIM317\OneDrive\2026\ISSU\Intel_AI_Summit_Seoul_2026_부스전시자료",
    r"C:\Users\MZC01-SUNKIM317\OneDrive\2026\ISSU\Intel 행사"
]

master_html_content = """<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
<meta name="robots" content="noindex, nofollow">
<title>Intel AI Summit Seoul 2026 - MZC-Intel Master Showcase (5-Stage Auto Loop)</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/pretendard/1.3.9/static/pretendard.min.css">
<link href="https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Inter:wght@400;600;700;800;900&display=swap" rel="stylesheet">
<style>
  :root {
    --bg: #03060f;
    --panel-bg: rgba(6, 14, 28, 0.95);
    --border: rgba(0, 199, 253, 0.28);
    --border-hl: rgba(0, 199, 253, 0.85);
    --intel-blue: #0071C5;
    --intel-cyan: #00C7FD;
    --intel-deep: #001E50;
    --unity-neon: #20E3B2;
    --text: #edf2f9;
    --muted: #8c9cb8;
    --font: 'Pretendard', 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    --mono: 'Space Mono', ui-monospace, Menlo, Consolas, monospace;
  }

  * { margin: 0; padding: 0; box-sizing: border-box; }
  html, body {
    width: 100%; height: 100%; overflow: hidden; background: #000;
    font-family: var(--font); color: var(--text); user-select: none;
  }
  body.hidecursor, body.hidecursor * { cursor: none !important; }

  /* 뷰포트 컨테이너 */
  #frameContainer {
    position: absolute; inset: 0; width: 100%; height: 100%;
    background: #000; overflow: hidden;
  }
  .show-item {
    position: absolute; inset: 0; width: 100%; height: 100%;
    border: none; outline: none; opacity: 0; visibility: hidden; pointer-events: none;
    transition: opacity 0.4s ease, visibility 0.4s;
    background: #000;
  }
  .show-item.active {
    opacity: 1; visibility: visible; pointer-events: auto; z-index: 10;
  }

  /* 비디오 래퍼 */
  #videoWrapper {
    display: flex; align-items: center; justify-content: center; background: #000;
  }
  #articul8Video {
    width: 100%; height: 100%; object-fit: contain; background: #000;
  }
  #videoOverlayPlay {
    position: absolute; inset: 0; display: none; align-items: center; justify-content: center;
    background: rgba(0, 0, 0, 0.45); cursor: pointer; z-index: 20;
  }
  #videoOverlayPlay.show { display: flex; }
  .play-circle {
    width: 80px; height: 80px; border-radius: 50%;
    background: linear-gradient(135deg, var(--intel-blue), var(--intel-cyan));
    display: flex; align-items: center; justify-content: center;
    color: #fff; font-size: 36px; box-shadow: 0 0 30px rgba(0, 199, 253, 0.5);
    transition: transform 0.2s;
  }
  .play-circle:hover { transform: scale(1.1); }

  /* 상단 마스터 네비게이션 헤더 */
  #runnerHeader {
    position: absolute; top: 0; left: 0; right: 0; height: 56px;
    background: var(--panel-bg); backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border-bottom: 1px solid var(--border);
    display: flex; align-items: center; justify-content: space-between;
    padding: 0 20px; z-index: 1000;
    box-shadow: 0 4px 24px rgba(0, 0, 0, 0.6);
    transition: transform 0.3s ease, opacity 0.3s ease;
  }
  #runnerHeader.minimized {
    transform: translateY(-50px); opacity: 0.15;
  }
  #runnerHeader:hover {
    transform: translateY(0); opacity: 1;
  }

  /* 상단 진행 프로그레스 바 */
  #headerProgress {
    position: absolute; left: 0; bottom: 0; height: 3px;
    background: linear-gradient(90deg, var(--intel-blue), var(--intel-cyan), var(--unity-neon));
    box-shadow: 0 0 10px var(--intel-cyan);
    width: 0%; transition: width 0.25s linear;
  }

  .runner-brand {
    display: flex; align-items: center; gap: 10px; cursor: pointer; flex-shrink: 0;
  }
  .intel-pill {
    padding: 3px 8px; border-radius: 4px;
    background: linear-gradient(135deg, var(--intel-blue), var(--intel-cyan));
    color: #fff; font-family: var(--mono); font-size: 11px; font-weight: 800;
    letter-spacing: 0.05em;
  }
  .runner-brand-text {
    font-size: 13.5px; font-weight: 700; color: #fff;
    display: flex; align-items: center; gap: 6px; white-space: nowrap;
  }
  .booth-tag {
    font-family: var(--mono); font-size: 11px; color: var(--intel-cyan);
    padding: 1px 6px; border: 1px solid rgba(0, 199, 253, 0.4); border-radius: 4px;
  }

  /* 5개 쇼케이스 탭 */
  .runner-nav {
    display: flex; align-items: center; gap: 8px; flex: 1; justify-content: center;
    max-width: 960px; margin: 0 12px;
  }
  .runner-tab {
    display: flex; align-items: center; gap: 6px;
    padding: 6px 12px; border-radius: 6px; border: 1px solid transparent;
    background: rgba(255, 255, 255, 0.05); color: var(--muted);
    font-size: 12px; font-weight: 600; cursor: pointer; transition: all 0.2s;
    white-space: nowrap; flex: 1; justify-content: center;
  }
  .runner-tab:hover {
    color: #fff; background: rgba(255, 255, 255, 0.1); border-color: rgba(255, 255, 255, 0.2);
  }
  .runner-tab.active {
    background: rgba(0, 199, 253, 0.16); border-color: var(--border-hl);
    color: var(--intel-cyan); box-shadow: 0 0 14px rgba(0, 199, 253, 0.25);
  }
  .runner-tab.unity-tab.active {
    background: rgba(32, 227, 178, 0.18) !important;
    border-color: var(--unity-neon) !important;
    color: var(--unity-neon) !important;
    box-shadow: 0 0 16px rgba(32, 227, 178, 0.4) !important;
  }
  .tab-timer {
    font-family: var(--mono); font-size: 10.5px; opacity: 0.85;
    padding: 1px 5px; border-radius: 3px; background: rgba(0, 0, 0, 0.35);
  }

  /* 우측 컨트롤 버튼 */
  .runner-ctrls {
    display: flex; align-items: center; gap: 6px; flex-shrink: 0;
  }
  .ctrl-btn {
    width: 32px; height: 32px; border-radius: 6px; border: 1px solid rgba(255, 255, 255, 0.15);
    background: rgba(255, 255, 255, 0.05); color: #fff; font-size: 13px;
    display: flex; align-items: center; justify-content: center; cursor: pointer; transition: all 0.2s;
  }
  .ctrl-btn:hover {
    background: var(--intel-blue); border-color: var(--intel-cyan);
    box-shadow: 0 0 10px rgba(0, 199, 253, 0.4);
  }

  /* 알림 토스트 */
  #toast {
    position: absolute; bottom: 32px; right: 32px;
    padding: 10px 18px; border-radius: 8px;
    background: rgba(4, 12, 28, 0.92); border: 1px solid var(--intel-cyan);
    color: #fff; font-size: 13.5px; font-weight: 600;
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.6);
    opacity: 0; pointer-events: none; transition: opacity 0.3s; z-index: 1000;
  }
  #toast.show { opacity: 1; }
</style>
</head>
<body>

<header id="runnerHeader">
  <div id="headerProgress"></div>

  <div class="runner-brand" onclick="togglePause()">
    <span class="intel-pill">INTEL AI SUMMIT 2026</span>
    <span class="runner-brand-text">
      MZC-Intel AI FULL STACK
      <span class="booth-tag">Gold #04</span>
    </span>
  </div>

  <!-- 5개 쇼케이스 순환 탭 (인라인 onclick으로 100% 클릭 보장) -->
  <nav class="runner-nav">
    <button class="runner-tab active" id="tab0" data-index="0" onclick="switchShow(0, true)">
      <span>① Full-Stack AI</span>
      <span class="tab-timer" id="timer0">01:50</span>
    </button>
    <button class="runner-tab" id="tab1" data-index="1" onclick="switchShow(1, true)">
      <span>② Nota 벤치마크</span>
      <span class="tab-timer" id="timer1">02:00</span>
    </button>
    <button class="runner-tab" id="tab2" data-index="2" onclick="switchShow(2, true)">
      <span>③ Alioth 코더</span>
      <span class="tab-timer" id="timer2">03:00</span>
    </button>
    <button class="runner-tab video-tab" id="tab3" data-index="3" onclick="switchShow(3, true)">
      <span>④ Articul8 영상</span>
      <span class="tab-timer" id="timer3">07:03</span>
    </button>
    <button class="runner-tab unity-tab" id="tab4" data-index="4" onclick="switchShow(4, true)">
      <span>⑤ Unity Physical AI</span>
      <span class="tab-timer" id="timer4">05:15</span>
    </button>
  </nav>

  <!-- 컨트롤 버튼 -->
  <div class="runner-ctrls">
    <button class="ctrl-btn" id="prevShowBtn" title="이전 (P / ←)" onclick="prevShow()">◀</button>
    <button class="ctrl-btn" id="pauseShowBtn" title="일시정지 / 재생 (Space)" onclick="togglePause()">❚❚</button>
    <button class="ctrl-btn" id="nextShowBtn" title="다음 (N / →)" onclick="nextShow()">▶</button>
    <button class="ctrl-btn sound-btn" id="soundBtn" title="음소거 토글 (M)" onclick="toggleSound()">🔇</button>
    <button class="ctrl-btn" id="fsBtn" title="전체화면 (F)" onclick="toggleFullscreen()">⛶</button>
  </div>
</header>

<!-- 메인 뷰포트 컨테이너 (5개 쇼케이스 프레임) -->
<main id="frameContainer">
  <iframe class="show-item active" id="frame0" src="MZC_Intel_AI_FullStack_Showcase.html"></iframe>
  <iframe class="show-item" id="frame1" src="Nota_Benchmark_Showcase_261015.html"></iframe>
  <iframe class="show-item" id="frame2" src="Alioth_Coder_Showcase_261019_단독실행.html"></iframe>

  <div class="show-item" id="videoWrapper">
    <video id="articul8Video" playsinline preload="auto" muted controls="false"></video>
    <div id="videoOverlayPlay" title="클릭하여 영상 재생"><div class="play-circle">▶</div></div>
  </div>

  <iframe class="show-item" id="frame4" src="Unity_발표자료.html?autoplay=1"></iframe>
</main>

<div id="toast">쇼케이스 전환됨</div>

<script>
/* ═════════════════════════════════════════════════════════════
   인텔 AI Summit 2026 쇼케이스 5단계 순환 목록 및 재생 시간
   순서: ① Full-Stack AI -> ② Nota -> ③ Alioth -> ④ Articul8 -> ⑤ Unity -> 무한 루프
   ═════════════════════════════════════════════════════════════ */
const SHOWS = [
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
];

let currentIndex = 0;
let isPaused = false;
let elapsedSec = 0;
let timerInterval = null;
let toastTimeout = null;

// 비디오 요소
const videoEl = document.getElementById('articul8Video');
const videoOverlay = document.getElementById('videoOverlayPlay');

// 비디오 다중 경로 폴백 리스트
const VIDEO_PATHS = [
  'Articul8_FullstackAI_행사영상_KR_v2.mp4',
  './Articul8_FullstackAI_행사영상_KR_v2.mp4',
  '../Redhat 행사/Articul8_FullstackAI_행사영상_KR_v2.mp4'
];

let currentPathIndex = 0;
function tryLoadVideo() {
  if (currentPathIndex < VIDEO_PATHS.length) {
    videoEl.src = VIDEO_PATHS[currentPathIndex];
    videoEl.load();
    currentPathIndex++;
  }
}
videoEl.addEventListener('error', () => {
  if (currentPathIndex < VIDEO_PATHS.length) {
    tryLoadVideo();
  } else {
    // 비디오 로딩 실패 시 5초 후 안전하게 5번 유니티로 이동
    setTimeout(() => {
      if (currentIndex === 3) switchShow(4);
    }, 5000);
  }
});
tryLoadVideo();

// 4번 비디오가 끝나면 무조건 5번(유니티, index 4)으로 이동!
videoEl.addEventListener('ended', () => {
  switchShow(4);
});

// 커서 자동 숨김
let cursorTimeout = null;
function handleMouseMove() {
  document.body.classList.remove('hidecursor');
  document.getElementById('runnerHeader').classList.remove('minimized');
  clearTimeout(cursorTimeout);
  cursorTimeout = setTimeout(() => {
    if (!isPaused) {
      document.body.classList.add('hidecursor');
      document.getElementById('runnerHeader').classList.add('minimized');
    }
  }, 4000);
}
window.addEventListener('mousemove', handleMouseMove);

function showToast(msg) {
  const toast = document.getElementById('toast');
  toast.textContent = msg;
  toast.classList.add('show');
  clearTimeout(toastTimeout);
  toastTimeout = setTimeout(() => toast.classList.remove('show'), 2200);
}

function updateTabs() {
  for (let i = 0; i < SHOWS.length; i++) {
    const tab = document.getElementById(`tab${i}`);
    if (tab) {
      tab.classList.toggle('active', i === currentIndex);
    }
  }
}

function updateProgress() {
  const currentShow = SHOWS[currentIndex];
  let curSec = elapsedSec;
  let totalSec = currentShow.durationSec;

  if (currentShow.type === 'video' && videoEl.duration && !isNaN(videoEl.duration)) {
    curSec = Math.floor(videoEl.currentTime);
    totalSec = Math.floor(videoEl.duration);
  }

  const pct = Math.min(100, (curSec / totalSec) * 100);
  document.getElementById('headerProgress').style.width = pct + '%';

  const remainSec = Math.max(0, totalSec - curSec);
  const m = String(Math.floor(remainSec / 60)).padStart(2, '0');
  const s = String(remainSec % 60).padStart(2, '0');
  const timerEl = document.getElementById(`timer${currentIndex}`);
  if (timerEl) timerEl.textContent = `${m}:${s}`;
}

function switchShow(newIndex, manual = false) {
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
    // 유니티 프레임 활성화 시
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
    } catch(e) {}
  }

  updateTabs();
  updateProgress();
  showToast(`${currentIndex + 1}단계: ${nextShow.name}`);
}

function nextShow() {
  switchShow(currentIndex + 1, true);
}

function prevShow() {
  switchShow(currentIndex - 1, true);
}

function tick() {
  if (isPaused) return;

  const currentShow = SHOWS[currentIndex];
  if (currentShow.type === 'iframe') {
    elapsedSec += 1;
    updateProgress();
    if (elapsedSec >= currentShow.durationSec) {
      // 시간 만료 시 다음 쇼케이스로 이동 (0 -> 1 -> 2 -> 3 -> 4 -> 0 무한 루프)
      switchShow(currentIndex + 1);
    }
  } else if (currentShow.type === 'video') {
    updateProgress();
  }
}

function togglePause() {
  isPaused = !isPaused;
  const pauseBtn = document.getElementById('pauseShowBtn');
  const currentShow = SHOWS[currentIndex];

  if (isPaused) {
    pauseBtn.textContent = '▶';
    if (currentShow.type === 'video') videoEl.pause();
    showToast('일시정지됨 (스페이스바로 재개)');
  } else {
    pauseBtn.textContent = '❚❚';
    if (currentShow.type === 'video') videoEl.play();
    showToast('재생 시작');
  }
}

function toggleSound() {
  videoEl.muted = !videoEl.muted;
  const soundBtn = document.getElementById('soundBtn');
  if (videoEl.muted) {
    soundBtn.textContent = '🔇';
    showToast('음소거 켜짐');
  } else {
    soundBtn.textContent = '🔊';
    showToast('음소거 해제됨');
  }
}

function toggleFullscreen() {
  if (!document.fullscreenElement) {
    document.documentElement.requestFullscreen().catch(() => {});
  } else {
    document.exitFullscreen().catch(() => {});
  }
}

videoOverlay.addEventListener('click', () => {
  videoOverlay.classList.remove('show');
  videoEl.play();
});

// 키보드 단축키
window.addEventListener('keydown', (e) => {
  if (e.key === ' ' || e.code === 'Space') {
    e.preventDefault();
    togglePause();
  } else if (e.key === 'ArrowRight' || e.key === 'n' || e.key === 'N') {
    nextShow();
  } else if (e.key === 'ArrowLeft' || e.key === 'p' || e.key === 'P') {
    prevShow();
  } else if (e.key === 'm' || e.key === 'M') {
    toggleSound();
  } else if (e.key === 'f' || e.key === 'F') {
    toggleFullscreen();
  } else if (['1', '2', '3', '4', '5'].includes(e.key)) {
    const idx = parseInt(e.key, 10) - 1;
    switchShow(idx, true);
  }
});

// 타이머 시작
timerInterval = setInterval(tick, 1000);
updateTabs();
updateProgress();
</script>

</body>
</html>
"""

for folder in folders:
    if not os.path.exists(folder):
        continue
    fp = os.path.join(folder, "Showcase_Master_Player.html")
    with open(fp, "w", encoding="utf-8") as f:
        f.write(master_html_content)
    print(f"[Rewritten Perfectly] {fp}")

print("SUCCESS: Showcase_Master_Player.html completely overhauled!")

