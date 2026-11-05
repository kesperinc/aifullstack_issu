# -*- coding: utf-8 -*-
"""
Unity_발표자료.html에 하단 자막(Subtitle / Live Caption Bar)을 추가하는 스크립트
- Glassmorphism 인텔 테마 자막 바 배치
- 7개 슬라이드별 핵심 발표자 스피치 자막 연동
- 단축키 C (자막 On/Off) 지원
- 상단 및 자막바 자체 토글 버튼 지원
- #slideHost bottom 여백 자동 보정 (콘텐츠 오버플로우 방지)
"""

import re
import os

target_path = r"C:\Users\MZC01-SUNKIM317\OneDrive\2026\ISSU\Intel 행사\Unity_발표자료.html"
showcase_path = r"C:\Users\MZC01-SUNKIM317\OneDrive\2026\ISSU\Intel 행사\Unity_발표자료_Showcase.html"

with open(target_path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. CSS 스타일 추가 및 보정
# #slideHost의 bottom을 116px로 조정하여 자막바 공간 확보
css_to_find = "#slideHost {"
slidehost_new = """#slideHost {
    position: absolute; left: 64px; right: 64px; top: 78px; bottom: 114px;
    overflow: hidden;
  }"""
html = re.sub(r'#slideHost\s*\{[^}]+\}', slidehost_new, html)

# 자막 바 관련 신규 CSS 스타일 추가 (</style> 직전에 삽입)
caption_css = """
  /* =========================================================================
     하단 실시간 발표 자막 (Live Key Narrative Caption Bar)
     ========================================================================= */
  .caption-bar {
    position: absolute;
    left: 64px;
    right: 64px;
    bottom: 58px;
    height: 48px;
    background: rgba(4, 12, 32, 0.9);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    border: 1px solid rgba(0, 199, 253, 0.45);
    border-radius: 10px;
    display: flex;
    align-items: center;
    padding: 0 16px;
    gap: 14px;
    z-index: 55;
    box-shadow: 0 4px 25px rgba(0, 0, 0, 0.65), inset 0 0 18px rgba(0, 199, 253, 0.08);
    transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
  }
  .caption-bar.caption-hidden {
    opacity: 0.35;
    background: rgba(4, 12, 32, 0.6);
  }
  .caption-bar.caption-hidden .caption-text-wrap {
    opacity: 0;
    pointer-events: none;
  }
  .caption-lead {
    display: flex;
    align-items: center;
    gap: 9px;
    flex-shrink: 0;
    padding-right: 14px;
    border-right: 1px solid rgba(255, 255, 255, 0.15);
  }
  .caption-pulse {
    width: 9px;
    height: 9px;
    border-radius: 50%;
    background: var(--intel-cyan);
    box-shadow: 0 0 10px var(--intel-cyan);
    animation: caption-pulse-anim 1.8s infinite ease-in-out;
  }
  @keyframes caption-pulse-anim {
    0%, 100% { opacity: 1; transform: scale(1); box-shadow: 0 0 10px var(--intel-cyan); }
    50% { opacity: 0.35; transform: scale(0.85); box-shadow: 0 0 3px var(--intel-cyan); }
  }
  .caption-tag {
    font-family: var(--font-mono);
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 0.09em;
    color: var(--intel-cyan);
    text-transform: uppercase;
  }
  .caption-text-wrap {
    flex: 1;
    overflow: hidden;
    position: relative;
    transition: opacity 0.2s ease;
  }
  .caption-text {
    font-size: 14.5px;
    line-height: 1.4;
    color: #f1f5f9;
    letter-spacing: -0.015em;
    white-space: nowrap;
    text-overflow: ellipsis;
    overflow: hidden;
    transition: opacity 0.25s ease, transform 0.25s ease;
  }
  .caption-text strong {
    color: #ffffff;
    font-weight: 700;
    background: rgba(0, 199, 253, 0.16);
    padding: 1px 6px;
    border-radius: 4px;
    border: 1px solid rgba(0, 199, 253, 0.35);
    margin: 0 2px;
  }
  .caption-controls {
    flex-shrink: 0;
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .caption-btn {
    background: rgba(255, 255, 255, 0.07);
    border: 1px solid rgba(255, 255, 255, 0.2);
    color: var(--text-muted);
    border-radius: 6px;
    padding: 4px 10px;
    font-family: var(--font-mono);
    font-size: 11.5px;
    cursor: pointer;
    transition: all 0.2s ease;
    display: inline-flex;
    align-items: center;
    gap: 5px;
  }
  .caption-btn:hover {
    background: rgba(0, 199, 253, 0.22);
    color: #fff;
    border-color: var(--intel-cyan);
    box-shadow: 0 0 10px rgba(0, 199, 253, 0.3);
  }
"""

if "/* 하단 실시간 발표 자막" not in html:
    html = html.replace("</style>", caption_css + "\n</style>")

# 2. 상단 네비게이션 헤더에 자막 버튼 추가
topbar_caption_btn = """        <button class="btn-top" id="btnCaptionTop" title="자막 On/Off [C]">
          <span>💬 자막 [C]</span>
        </button>
"""
if 'id="btnCaptionTop"' not in html:
    html = html.replace('<button class="btn-top" id="btnGrid"', topbar_caption_btn + '        <button class="btn-top" id="btnGrid"')

# 3. 하단 컨트롤바 단축키 도움말에 C 키 추가
if '<span><span class="kbd-key">C</span> 자막</span>' not in html:
    html = html.replace('<span><span class="kbd-key">Space</span> 자동재생</span>',
                        '<span><span class="kbd-key">Space</span> 자동재생</span>\n          <span><span class="kbd-key">C</span> 자막</span>')

# 4. 하단 자막 바 DOM 삽입 (</main> 바로 뒤, <footer class="bottombar"> 바로 앞에 삽입)
caption_dom = """
    <!-- =========================================================================
         실시간 발표 핵심 자막 바 (Live Key Narrative Caption Bar)
         ========================================================================= -->
    <div class="caption-bar" id="captionBar">
      <div class="caption-lead">
        <span class="caption-pulse"></span>
        <span class="caption-tag">LIVE CAPTION · 핵심 맥락</span>
      </div>
      <div class="caption-text-wrap">
        <div class="caption-text" id="captionText">
          자막을 불러오는 중입니다...
        </div>
      </div>
      <div class="caption-controls">
        <button class="caption-btn" id="btnCaptionToggle" title="자막 표시 토글 (단축키: C)">
          <span>자막 켜짐 [C]</span>
        </button>
      </div>
    </div>
"""

if 'id="captionBar"' not in html:
    html = html.replace('</main>', '</main>\n' + caption_dom)

# 5. 자바스크립트에 자막 데이터 및 연동 로직 추가
js_caption_logic = """
  // 슬라이드별 핵심 발표 자막 데이터 (Key Narrative Subtitles)
  const slideCaptions = {
    1: '<strong>핵심 아키텍처:</strong> 70여 종의 산업용 CAD 원본을 <strong>Asset Transformer</strong>로 1-Click 자동 경량화하고, <strong>Simulation Pro</strong> 물리 환경에서 합성 데이터를 생성·학습하여 <strong>Intel 하드웨어</strong> 상에서 온디바이스로 실물 로봇을 제어하는 완결된 Physical AI 파이프라인을 제시합니다.',
    2: '<strong>Asset Transformer (3D 자동 최적화):</strong> 353만 폴리곤의 대형 설비 CAD도 단 1-Click으로 즉시 경량화! 수작업 리토폴로지 없이 LOD 메시를 전자동 생성하고 표준 Recipe를 적용하여, 3D 데이터 전처리 시간을 <strong>최대 85%까지 획기적으로 단축</strong>합니다.',
    3: '<strong>Asset Manager & 3DDS:</strong> 기가바이트급 3D 설비 모델을 다운로드 없이 <strong>초저지연 클라우드 스트리밍</strong>으로 렌더링하며, 물리 시뮬레이션 구동 중에도 씬(Scene) 재컴파일 없이 3D 에셋을 <strong>런타임에 동적으로 즉시 교체</strong>합니다.',
    4: '<strong>Physical AI 학습 & ML-Agents:</strong> XR 공간에서의 직관적 원격 제어와 PyTorch 분산 환경을 결합! 현장에서 얻기 힘든 극한의 엣지 케이스 <strong>물리 합성 데이터를 무한 생성</strong>하고, 자율주행 물류로봇(AMR)과 로봇 암의 파지·이동 제어를 <strong>심층 강화학습</strong>합니다.',
    5: '<strong>Unity Sentis (인텔 온디바이스 추론):</strong> 외부 클라우드 통신 없는 초저지연 온디바이스 AI! 학습된 ONNX 모델을 런타임에 직접 임베딩하여, <strong>Intel Core Ultra의 NPU 및 Arc GPU</strong> 하드웨어 가속을 통해 <strong>네트워크 지연(Zero-Latency)과 보안 리스크 없이</strong> 실시간 추론을 완결합니다.',
    6: '<strong>Simulation Pro & ROS2 (Sim2Real):</strong> 가상 검증 코드를 실물 로봇에 무수정 직결! URDF 로봇 모델과 LiDAR·Depth 센서를 물리 시뮬레이션하고, <strong>ROS2 네이티브 토픽과 1:1로 직접 통신</strong>하여 가상-실물 로봇 제어(Sim-to-Real)를 완벽히 통합합니다.',
    7: '<strong>메가존클라우드 공식 파트너십 & 로드맵:</strong> Unity 국내 공식 총판 메가존클라우드는 <strong>과제 정의(STEP 1)부터 기술 검증·PoC(STEP 2), 라이선스 도입(STEP 3), 전사 활용 확대(STEP 4)</strong>까지 전 과정을 책임집니다. <strong>코엑스 1F Gold 부스</strong>에서 CAD 변환 및 AI 상담을 바로 신청하세요.'
  };

  const captionBar = document.getElementById('captionBar');
  const captionText = document.getElementById('captionText');
  const btnCaptionToggle = document.getElementById('btnCaptionToggle');
  const btnCaptionTop = document.getElementById('btnCaptionTop');
  let isCaptionVisible = true;

  function updateCaption(index) {
    if (!captionText) return;
    const text = slideCaptions[index] || '';
    captionText.style.opacity = '0';
    captionText.style.transform = 'translateY(4px)';
    setTimeout(() => {
      captionText.innerHTML = text;
      captionText.style.opacity = '1';
      captionText.style.transform = 'translateY(0)';
    }, 150);
  }

  function toggleCaption() {
    isCaptionVisible = !isCaptionVisible;
    if (captionBar) {
      if (isCaptionVisible) {
        captionBar.classList.remove('caption-hidden');
      } else {
        captionBar.classList.add('caption-hidden');
      }
    }
    const label = isCaptionVisible ? '자막 켜짐 [C]' : '자막 꺼짐 [C]';
    if (btnCaptionToggle) btnCaptionToggle.innerHTML = `<span>${label}</span>`;
    if (btnCaptionTop) btnCaptionTop.innerHTML = `<span>💬 자막 ${isCaptionVisible ? 'ON' : 'OFF'} [C]</span>`;
  }

  if (btnCaptionToggle) btnCaptionToggle.addEventListener('click', toggleCaption);
  if (btnCaptionTop) btnCaptionTop.addEventListener('click', toggleCaption);
"""

# goToSlide 함수 안에서 updateCaption(index) 호출하도록 삽입
if "updateCaption(index);" not in html:
    html = html.replace("slideCounter.textContent = `${pad2(index)} / ${pad2(totalSlides)}`;",
                        "slideCounter.textContent = `${pad2(index)} / ${pad2(totalSlides)}`;\n    updateCaption(index);")

# 단축키 C 키 이벤트 핸들러 추가
if "e.key === 'c' || e.key === 'C'" not in html:
    html = html.replace("case 'KeyF':\n        toggleFullscreen();\n        break;",
                        "case 'KeyF':\n        toggleFullscreen();\n        break;\n      case 'KeyC':\n        toggleCaption();\n        break;")

# JS 로직 추가
if "const slideCaptions =" not in html:
    # dotsContainer 뒤에 자막 초기화 코드 삽입
    html = html.replace("const dotsContainer = document.getElementById('dotsContainer');",
                        "const dotsContainer = document.getElementById('dotsContainer');\n" + js_caption_logic)

with open(target_path, "w", encoding="utf-8") as f:
    f.write(html)

with open(showcase_path, "w", encoding="utf-8") as f:
    f.write(html)

print("SUCCESS: Added subtitles (live captions) to Unity_발표자료.html and Unity_발표자료_Showcase.html")

