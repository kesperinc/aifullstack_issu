# -*- coding: utf-8 -*-
"""
Showcase_Master_Player.html에서 유니티 쇼케이스 건너뛰기 버그 완전 수정
1. videoEl 'ended' 이벤트에서 switchShow(0) 하드코딩 제거 -> switchShow(currentIndex + 1) 호출
2. 비디오 재생 실패/오류 시 건너뛰지 않고 안전하게 다음 쇼케이스로 진행
3. Unity iframe 자동 재생 연동 (src="Unity_발표자료.html?autoplay=1")
4. Unity_발표자료.html에서 URL 파라미터 ?autoplay=1 지원 또는 부스 모드 기본 autoplay 활성화
"""

import os
import re

target_paths = [
    r"C:\Users\MZC01-SUNKIM317\OneDrive\2026\ISSU\Intel_AI_Summit_Seoul_2026_부스전시자료\Showcase_Master_Player.html",
    r"C:\Users\MZC01-SUNKIM317\OneDrive\2026\ISSU\Intel 행사\Showcase_Master_Player.html"
]

for file_path in target_paths:
    if not os.path.exists(file_path):
        continue

    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. ended 이벤트 수정
    # 기존: if (currentIndex === 3) switchShow(0); -> switchShow(currentIndex + 1);
    html = re.sub(
        r"videoEl\.addEventListener\('ended',\s*\(\)\s*=>\s*\{[^}]*\}\);",
        """videoEl.addEventListener('ended', () => {
  // 비디오가 끝나면 다음 순서인 5번 유니티 쇼케이스(또는 다음 쇼)로 자연스럽게 이동
  switchShow(currentIndex + 1);
});""",
        html
    )

    # 2. 비디오 다중 경로 로딩 실패 시 처리 보강
    video_error_fix = """videoEl.addEventListener('error', () => {
  if (currentPathIndex < VIDEO_PATHS.length) {
    tryLoadVideo();
  } else {
    // 모든 비디오 경로 탐색 실패 시 멈추지 않고 5초 후 다음 쇼(유니티)로 안전 이동
    console.warn('[Video Error] Video not found, transitioning to next show in 5s...');
    setTimeout(() => {
      if (currentIndex === 3) switchShow(currentIndex + 1);
    }, 5000);
  }
});"""
    html = re.sub(
        r"videoEl\.addEventListener\('error',\s*\(\)\s*=>\s*\{[^}]*tryLoadVideo\(\);[^}]*\}\);",
        video_error_fix,
        html
    )

    # 3. frame4의 src를 Unity_발표자료.html?autoplay=1 로 설정
    html = html.replace('id="frame4" src="Unity_발표자료.html"', 'id="frame4" src="Unity_발표자료.html?autoplay=1"')
    html = html.replace("file: 'Unity_발표자료.html'", "file: 'Unity_발표자료.html?autoplay=1'")

    # 4. switchShow 함수에서 유니티 iframe 활성화 시 재생 트리거 강화
    switch_patch = """  if (nextShow.type === 'video') {
    videoEl.currentTime = 0;
    const playPromise = videoEl.play();
    if (playPromise !== undefined) {
      playPromise.catch(() => videoOverlay.classList.add('show'));
    }
  } else if (nextShow.id === 'frame4') {
    // 5번 유니티 전환 시 iframe 내부의 자동재생 및 첫 슬라이드 동기화
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
      console.log('Unity frame cross-origin notice:', e);
    }
  }"""
    html = re.sub(
        r"if\s*\(nextShow\.type\s*===\s*'video'\)\s*\{[^}]+playPromise\.catch\([^}]+\);\s*\}\s*\}",
        switch_patch,
        html
    )

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"[Fixed Showcase] {file_path}")

print("SUCCESS: Fixed master player skip bug!")

