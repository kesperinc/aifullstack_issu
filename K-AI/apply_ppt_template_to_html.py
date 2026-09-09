# -*- coding: utf-8 -*-
"""
Dell Distributor Proposal PPT 템플릿의 디자인 시스템(색상, 2x2 그리드, 3열 컬럼, 0B2A68 배지, 헤더바)을
HTML 30슬라이드 덱에 100% 적용하는 변환 스크립트
"""
import os

html_path = os.path.join(os.path.dirname(__file__), "2026-09-09_Korea_Sovereign_AI_Strategy_Deck.html")

with open(html_path, "r", encoding="utf-8") as f:
    orig = f.read()

start_marker = "const slides = ["
end_marker = "let currentSlideIndex = 0;"
s_idx = orig.find(start_marker)
e_idx = orig.find(end_marker)
if s_idx == -1 or e_idx == -1:
    raise ValueError("Slides array markers not found in HTML!")

slides_js = orig[s_idx:e_idx].strip()

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Korea's Sovereign AI Strategy | UCLA Anderson EMBA Session Deck</title>
  <meta name="description" content="Executive 30-Slide Presentation Deck for UCLA Anderson EMBA Delegation Visit at MegazoneCloud Gwacheon HQ.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Montserrat:wght@500;600;700;800;900&family=JetBrains+Mono:wght@400;600;700&family=Outfit:wght@600;700;800&display=swap" rel="stylesheet">
  <style>
    :root {{
      /* Dell Distributor Proposal Template Exact Palette */
      --ppt-primary-navy: #0B2A68;   /* Template Badge & Dark Navy */
      --ppt-title-navy: #002060;     /* Template Headline Navy */
      --ppt-deep-navy: #001A30;      /* Cover Deep Navy */
      --ppt-accent-blue: #1760CB;    /* Template Accent Blue */
      --ppt-sky-blue: #00C2FF;       /* Cyan Glow */
      --ucla-blue: #003B5C;          /* UCLA Official Blue */
      --ucla-gold: #FFD100;          /* UCLA Official Gold */
      
      /* Slide Backgrounds & Surfaces */
      --canvas-bg: #E6EDF5;
      --slide-bg: #FFFFFF;
      --card-bg: #FFFFFF;
      --card-border: #DDE5ED;
      --card-hover-border: #1760CB;
      --border-light: #E2E8F0;
      --text-dark: #1E293B;
      --text-muted: #64748B;
      --text-light: #94A3B8;

      /* Shadows */
      --slide-shadow: 0 24px 50px -10px rgba(11, 42, 104, 0.28), 0 0 0 1px rgba(11, 42, 104, 0.1);
      --card-shadow: 0 4px 14px rgba(11, 42, 104, 0.05);
      --card-shadow-hover: 0 10px 24px rgba(23, 96, 203, 0.18);
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: 'Inter', sans-serif;
      background-color: var(--canvas-bg);
      color: var(--text-dark);
      overflow: hidden;
      height: 100vh;
      width: 100vw;
      display: flex;
      flex-direction: column;
      user-select: none;
    }}

    /* Executive Top Bar */
    header.deck-header {{
      position: relative;
      z-index: 30;
      height: 54px;
      padding: 0 28px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      background: var(--ppt-deep-navy);
      border-bottom: 2px solid var(--ucla-gold);
      box-shadow: 0 4px 14px rgba(0, 0, 0, 0.25);
      flex-shrink: 0;
    }}

    .header-left {{
      display: flex;
      align-items: center;
      gap: 16px;
    }}

    .brand-badges {{
      display: flex;
      align-items: center;
      gap: 8px;
      font-family: 'Montserrat', sans-serif;
      font-weight: 800;
      font-size: 12px;
    }}

    .badge-ucla {{
      color: var(--ucla-gold);
      background: rgba(255, 209, 0, 0.14);
      padding: 4px 10px;
      border-radius: 4px;
      border: 1px solid rgba(255, 209, 0, 0.4);
      letter-spacing: 0.5px;
    }}

    .badge-mzc {{
      color: #FFFFFF;
      background: linear-gradient(135deg, #1760CB, #00C2FF);
      padding: 4px 10px;
      border-radius: 4px;
      font-weight: 700;
      box-shadow: 0 2px 6px rgba(23, 96, 203, 0.35);
    }}

    .session-title-head {{
      font-size: 13px;
      color: #E2E8F0;
      border-left: 1px solid rgba(255, 255, 255, 0.2);
      padding-left: 14px;
      display: flex;
      align-items: center;
      gap: 8px;
      font-weight: 500;
    }}

    .live-dot {{
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background-color: #10B981;
      box-shadow: 0 0 8px #10B981;
      animation: pulse 2s infinite;
    }}

    @keyframes pulse {{
      0% {{ opacity: 0.4; }}
      50% {{ opacity: 1; }}
      100% {{ opacity: 0.4; }}
    }}

    .header-right {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .timer-badge {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 12px;
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 209, 0, 0.35);
      padding: 4px 12px;
      border-radius: 4px;
      color: var(--ucla-gold);
      font-weight: 700;
      letter-spacing: 0.5px;
    }}

    .btn-header {{
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.2);
      color: #FFFFFF;
      font-size: 12px;
      font-weight: 600;
      padding: 5px 12px;
      border-radius: 4px;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s ease;
    }}

    .btn-header:hover {{
      background: rgba(255, 255, 255, 0.22);
      border-color: var(--ppt-sky-blue);
    }}

    /* Main Stage Wrapper: Scale to Fit 16:9 Canvas */
    main.stage-wrapper {{
      position: relative;
      flex: 1;
      display: flex;
      align-items: center;
      justify-content: center;
      overflow: hidden;
      background: var(--canvas-bg);
      padding: 16px;
    }}

    /* 16:9 Master Presentation Slide Canvas (1333 x 750 px native) */
    .slide-canvas {{
      width: 1333px;
      height: 750px;
      aspect-ratio: 16 / 9;
      background: var(--slide-bg);
      border: 1px solid rgba(11, 42, 104, 0.12);
      border-radius: 12px;
      box-shadow: var(--slide-shadow);
      display: flex;
      flex-direction: column;
      overflow: hidden;
      position: relative;
      transform-origin: center center;
      transition: transform 0.15s ease-out;
      flex-shrink: 0;
    }}

    /* ==============================================================
       SLIDE HEADER: PPT Template Master Style
       ============================================================== */
    .ppt-slide-header {{
      height: 84px;
      background: #FFFFFF;
      border-bottom: 2px solid #E8EEF5;
      padding: 14px 44px 10px 44px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-shrink: 0;
      position: relative;
    }}

    .ppt-slide-header::after {{
      content: '';
      position: absolute;
      bottom: -2px;
      left: 44px;
      width: 80px;
      height: 2px;
      background: var(--ppt-accent-blue);
    }}

    .header-title-box {{
      display: flex;
      flex-direction: column;
      gap: 3px;
    }}

    .part-pill-badge {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-family: 'Montserrat', sans-serif;
      font-size: 11px;
      font-weight: 800;
      color: #FFFFFF;
      background: var(--ppt-primary-navy);
      padding: 3px 10px;
      border-radius: 4px;
      letter-spacing: 0.6px;
      text-transform: uppercase;
      align-self: flex-start;
      margin-bottom: 2px;
    }}

    h2.slide-master-title {{
      font-family: 'Montserrat', sans-serif;
      font-size: 23px;
      font-weight: 800;
      color: var(--ppt-title-navy);
      letter-spacing: -0.4px;
      line-height: 1.2;
    }}

    p.slide-master-subtitle {{
      font-size: 12.5px;
      font-weight: 600;
      color: var(--ppt-accent-blue);
      letter-spacing: 0.2px;
    }}

    .header-logo-tag {{
      font-family: 'Montserrat', sans-serif;
      font-size: 11px;
      font-weight: 800;
      color: var(--ppt-primary-navy);
      background: #F0F4FA;
      padding: 6px 14px;
      border-radius: 20px;
      border: 1px solid #D6E2EE;
      letter-spacing: 0.5px;
    }}

    /* ==============================================================
       SLIDE BODY CANVAS
       ============================================================== */
    .ppt-slide-body {{
      flex: 1;
      padding: 22px 44px 16px 44px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      overflow: hidden;
      background: #FAFCFF;
    }}

    /* --------------------------------------------------------------
       LAYOUT VARIANT 1: 2x2 Grid Cards (4-item slides)
       -------------------------------------------------------------- */
    .grid-2x2-container {{
      flex: 1;
      display: grid;
      grid-template-columns: 1fr 1fr;
      grid-template-rows: 1fr 1fr;
      gap: 16px;
      align-content: stretch;
    }}

    /* --------------------------------------------------------------
       LAYOUT VARIANT 2: 3-Column Cards (3-item slides)
       -------------------------------------------------------------- */
    .grid-3col-container {{
      flex: 1;
      display: grid;
      grid-template-columns: 1fr 1fr 1fr;
      gap: 18px;
      align-content: stretch;
    }}

    /* --------------------------------------------------------------
       LAYOUT VARIANT 3: Split Image (Left Bullets + Right 16:9 Image)
       -------------------------------------------------------------- */
    .split-image-container {{
      flex: 1;
      display: grid;
      grid-template-columns: 1.15fr 0.85fr;
      gap: 26px;
      align-items: center;
    }}

    .split-bullets-col {{
      display: flex;
      flex-direction: column;
      gap: 12px;
      height: 100%;
      justify-content: center;
    }}

    .split-image-box {{
      position: relative;
      border-radius: 10px;
      overflow: hidden;
      border: 1px solid #C5D8F1;
      box-shadow: 0 12px 30px rgba(11, 42, 104, 0.16);
      aspect-ratio: 16 / 9;
      cursor: zoom-in;
      background: #000;
      transition: transform 0.25s ease, box-shadow 0.25s ease;
    }}

    .split-image-box:hover {{
      transform: translateY(-2px);
      box-shadow: 0 16px 36px rgba(23, 96, 203, 0.25);
    }}

    .split-image-box img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }}

    .split-image-tag {{
      position: absolute;
      bottom: 0;
      left: 0;
      right: 0;
      background: linear-gradient(0deg, rgba(0, 32, 96, 0.92) 0%, rgba(0, 32, 96, 0) 100%);
      padding: 10px 14px 6px 14px;
      font-size: 11px;
      color: #E2E8F0;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    /* --------------------------------------------------------------
       PPT Template Card Box (Modular Clean Card)
       -------------------------------------------------------------- */
    .ppt-template-card {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 8px;
      padding: 16px 20px;
      box-shadow: var(--card-shadow);
      position: relative;
      overflow: hidden;
      transition: all 0.2s ease;
      display: flex;
      flex-direction: column;
      justify-content: center;
      gap: 5px;
    }}

    .ppt-template-card::before {{
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      width: 5px;
      height: 100%;
      background: linear-gradient(180deg, var(--ppt-accent-blue), var(--ppt-sky-blue));
    }}

    .ppt-template-card:hover {{
      border-color: var(--card-hover-border);
      box-shadow: var(--card-shadow-hover);
      transform: translateY(-2px);
    }}

    .card-top-row {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .card-index-box {{
      font-family: 'Montserrat', sans-serif;
      font-size: 11px;
      font-weight: 800;
      color: #FFFFFF;
      background: var(--ppt-accent-blue);
      width: 22px;
      height: 22px;
      border-radius: 4px;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }}

    .card-title-text {{
      font-family: 'Montserrat', sans-serif;
      font-size: 15px;
      font-weight: 700;
      color: var(--ppt-title-navy);
      line-height: 1.3;
    }}

    .card-desc-text {{
      font-size: 13.5px;
      line-height: 1.5;
      color: #334155;
      padding-left: 32px;
    }}

    /* --------------------------------------------------------------
       LAYOUT VARIANT 4: Executive ROI Metric Scorecard (Slide 25)
       -------------------------------------------------------------- */
    .metric-card-box {{
      background: #FFFFFF;
      border: 1px solid var(--card-border);
      border-radius: 8px;
      padding: 16px 20px;
      box-shadow: var(--card-shadow);
      display: flex;
      flex-direction: column;
      gap: 8px;
      position: relative;
    }}

    .metric-pill-highlight {{
      font-family: 'Montserrat', sans-serif;
      font-size: 12px;
      font-weight: 800;
      padding: 4px 10px;
      border-radius: 4px;
      align-self: flex-start;
      letter-spacing: 0.5px;
      display: inline-block;
    }}

    /* --------------------------------------------------------------
       VISUAL CONCEPT BAR & FOOTER BAR
       -------------------------------------------------------------- */
    .ppt-concept-strip {{
      background: #EDF3F9;
      border-left: 4px solid var(--ppt-primary-navy);
      border-radius: 4px;
      padding: 8px 16px;
      display: flex;
      align-items: center;
      gap: 12px;
      margin-top: 12px;
      flex-shrink: 0;
    }}

    .concept-label-tag {{
      font-family: 'Montserrat', sans-serif;
      font-size: 10.5px;
      font-weight: 800;
      color: var(--ppt-primary-navy);
      letter-spacing: 0.6px;
      text-transform: uppercase;
      flex-shrink: 0;
    }}

    .concept-text-info {{
      font-size: 12px;
      color: var(--text-muted);
      font-style: italic;
    }}

    .ppt-slide-footer {{
      height: 36px;
      background: #FFFFFF;
      border-top: 1px solid #E2E8F0;
      padding: 0 44px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 11px;
      color: var(--text-muted);
      flex-shrink: 0;
    }}

    .footer-left-info {{
      font-weight: 600;
    }}

    .footer-right-index {{
      font-family: 'JetBrains Mono', monospace;
      font-weight: 700;
      color: var(--ppt-title-navy);
    }}

    /* ==============================================================
       SPECIAL THEMES: COVER (Slide 1) & CLOSING Q&A (Slide 30)
       ============================================================== */
    .slide-canvas.theme-cover {{
      background: linear-gradient(135deg, #001224 0%, #00223D 45%, #0B2A68 100%);
      color: #FFFFFF;
      border-color: rgba(255, 209, 0, 0.4);
    }}

    .cover-inner-grid {{
      flex: 1;
      display: grid;
      grid-template-columns: 1.15fr 0.85fr;
      padding: 44px 52px;
      gap: 36px;
      align-items: center;
    }}

    .cover-top-pill {{
      display: inline-block;
      font-family: 'Montserrat', sans-serif;
      font-size: 11px;
      font-weight: 800;
      letter-spacing: 1px;
      color: var(--ucla-gold);
      background: rgba(255, 209, 0, 0.12);
      border: 1px solid var(--ucla-gold);
      padding: 6px 16px;
      border-radius: 20px;
      margin-bottom: 18px;
    }}

    h1.cover-main-title {{
      font-family: 'Montserrat', sans-serif;
      font-size: 38px;
      font-weight: 900;
      line-height: 1.22;
      color: #FFFFFF;
      letter-spacing: -0.5px;
      margin-bottom: 12px;
    }}

    p.cover-sub-lead {{
      font-size: 17px;
      font-weight: 500;
      color: var(--ppt-sky-blue);
      margin-bottom: 24px;
      line-height: 1.4;
    }}

    .cover-meta-box {{
      background: rgba(11, 42, 104, 0.65);
      border: 1px solid rgba(0, 194, 255, 0.4);
      border-radius: 8px;
      padding: 16px 20px;
      display: flex;
      flex-direction: column;
      gap: 8px;
      backdrop-filter: blur(12px);
    }}

    .cover-meta-item {{
      font-size: 12.5px;
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    .cover-meta-k {{
      color: var(--ucla-gold);
      font-weight: 700;
      width: 95px;
      flex-shrink: 0;
      font-family: 'Montserrat', sans-serif;
    }}

    .cover-meta-v {{
      color: #F1F5F9;
      font-weight: 500;
    }}

    .cover-visual-frame {{
      position: relative;
      border-radius: 12px;
      overflow: hidden;
      border: 2px solid rgba(0, 194, 255, 0.5);
      box-shadow: 0 20px 45px rgba(0, 0, 0, 0.7);
      aspect-ratio: 16 / 9;
      cursor: zoom-in;
    }}

    .cover-visual-frame img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }}

    /* Slide 30: Closing Q&A Theme */
    .slide-canvas.theme-closing {{
      background: linear-gradient(135deg, #001224 0%, #00223D 45%, #0B2A68 100%);
      color: #FFFFFF;
    }}

    .closing-inner-layout {{
      flex: 1;
      padding: 40px 52px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}

    .closing-cards-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
      margin-top: 20px;
    }}

    .closing-meta-card {{
      background: rgba(11, 42, 104, 0.7);
      border: 1px solid rgba(255, 209, 0, 0.4);
      border-radius: 8px;
      padding: 20px 24px;
      display: flex;
      flex-direction: column;
      gap: 8px;
      backdrop-filter: blur(10px);
    }}

    .closing-meta-card h3 {{
      font-family: 'Montserrat', sans-serif;
      font-size: 16px;
      font-weight: 700;
      color: var(--ucla-gold);
    }}

    .closing-meta-card p {{
      font-size: 13.5px;
      color: #F1F5F9;
      line-height: 1.5;
    }}

    /* ==============================================================
       BOTTOM DECK CONTROLLER & PROGRESS
       ============================================================== */
    footer.deck-controls-footer {{
      position: relative;
      z-index: 30;
      height: 58px;
      padding: 0 28px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      background: var(--ppt-deep-navy);
      border-top: 1px solid rgba(255, 255, 255, 0.1);
      flex-shrink: 0;
    }}

    .nav-btn-group {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .btn-slide-nav {{
      background: var(--ppt-primary-navy);
      border: 1px solid rgba(255, 209, 0, 0.4);
      color: #FFFFFF;
      padding: 7px 18px;
      border-radius: 4px;
      font-size: 13px;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      font-family: 'Montserrat', sans-serif;
      transition: all 0.2s ease;
    }}

    .btn-slide-nav:hover:not(:disabled) {{
      background: var(--ppt-accent-blue);
      border-color: var(--ppt-sky-blue);
      box-shadow: 0 0 12px rgba(23, 96, 203, 0.5);
    }}

    .btn-slide-nav:disabled {{
      opacity: 0.35;
      cursor: not-allowed;
    }}

    .track-wrapper {{
      flex: 1;
      max-width: 540px;
      margin: 0 24px;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }}

    .track-bar-bg {{
      height: 5px;
      width: 100%;
      background: rgba(255, 255, 255, 0.15);
      border-radius: 3px;
      overflow: hidden;
    }}

    .track-bar-fill {{
      height: 100%;
      background: linear-gradient(90deg, var(--ucla-gold), var(--ppt-sky-blue));
      width: 3.33%;
      transition: width 0.25s ease;
    }}

    .track-labels {{
      font-size: 11px;
      color: #94A3B8;
      display: flex;
      justify-content: space-between;
      font-family: 'Montserrat', sans-serif;
      font-weight: 600;
    }}

    .key-shortcuts-hint {{
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 11px;
      color: #94A3B8;
    }}

    kbd {{
      background: rgba(255, 255, 255, 0.12);
      border: 1px solid rgba(255, 255, 255, 0.25);
      border-radius: 3px;
      padding: 2px 5px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 10px;
      color: #FFF;
    }}

    /* Speaker Notes Drawer */
    .speaker-drawer {{
      position: fixed;
      bottom: 58px;
      left: 0;
      right: 0;
      background: rgba(0, 26, 48, 0.98);
      border-top: 2px solid var(--ucla-gold);
      backdrop-filter: blur(20px);
      padding: 18px 44px;
      box-shadow: 0 -10px 30px rgba(0,0,0,0.6);
      z-index: 40;
      transform: translateY(110%);
      transition: transform 0.28s cubic-bezier(0.16, 1, 0.3, 1);
    }}

    .speaker-drawer.open {{
      transform: translateY(0);
    }}

    .drawer-top-bar {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 8px;
    }}

    .drawer-title-tag {{
      font-family: 'Montserrat', sans-serif;
      font-size: 12px;
      font-weight: 800;
      letter-spacing: 0.8px;
      text-transform: uppercase;
      color: var(--ucla-gold);
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .drawer-pacing-tag {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 12px;
      color: var(--ppt-sky-blue);
      font-weight: 600;
    }}

    .drawer-script-body {{
      font-family: Georgia, serif;
      font-size: 15px;
      line-height: 1.6;
      color: #E2E8F0;
      font-style: italic;
    }}

    /* Grid Modal */
    .grid-overlay-modal {{
      position: fixed;
      inset: 0;
      background: rgba(0, 18, 36, 0.85);
      backdrop-filter: blur(14px);
      z-index: 60;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 30px;
    }}

    .grid-overlay-modal.active {{
      display: flex;
    }}

    .grid-dialog {{
      background: #FFFFFF;
      border: 2px solid var(--ppt-primary-navy);
      border-radius: 10px;
      width: 100%;
      max-width: 1200px;
      max-height: 85vh;
      display: flex;
      flex-direction: column;
      overflow: hidden;
      box-shadow: 0 25px 50px rgba(0,0,0,0.5);
    }}

    .dialog-head {{
      padding: 16px 24px;
      background: var(--ppt-deep-navy);
      color: #FFFFFF;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .dialog-body {{
      flex: 1;
      padding: 20px;
      overflow-y: auto;
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(210px, 1fr));
      gap: 12px;
      background: #F1F5F9;
    }}

    .grid-thumb-card {{
      background: #FFFFFF;
      border: 1px solid var(--card-border);
      border-radius: 6px;
      padding: 10px 12px;
      cursor: pointer;
      transition: all 0.2s ease;
      display: flex;
      flex-direction: column;
      gap: 4px;
    }}

    .grid-thumb-card:hover {{
      background: #EDF3F9;
      border-color: var(--ppt-accent-blue);
      transform: translateY(-2px);
    }}

    .grid-thumb-card.current {{
      border: 2px solid var(--ppt-primary-navy);
      background: #E2E8F0;
    }}

    .thumb-num {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 10.5px;
      color: var(--ppt-accent-blue);
      font-weight: 700;
    }}

    .thumb-title {{
      font-size: 11.5px;
      font-weight: 600;
      color: var(--ppt-title-navy);
      line-height: 1.3;
    }}
  </style>
</head>
<body>

  <!-- Top Executive Header -->
  <header class="deck-header">
    <div class="header-left">
      <div class="brand-badges">
        <span class="badge-ucla">UCLA Anderson EMBA</span>
        <span class="badge-mzc">MegazoneCloud</span>
      </div>
      <div class="session-title-head">
        <span class="live-dot"></span>
        <span>Session 3: Korea's Sovereign AI Strategy (Speaker: Andy | ISV Business Unit)</span>
      </div>
    </div>
    <div class="header-right">
      <div class="timer-badge" id="sessionTimer">⏱ 15:00 REMAINING</div>
      <button class="btn-header" id="btnNotesToggle" title="Toggle Speaker Script (Key: S)">
        📝 <span>Notes</span>
      </button>
      <button class="btn-header" id="btnGridToggle" title="View All 30 Slides (Key: G)">
        🗂 <span>All Slides</span>
      </button>
      <button class="btn-header" id="btnFullscreen" title="Toggle Fullscreen (Key: F)">
        ⛶ <span>Fullscreen</span>
      </button>
    </div>
  </header>

  <!-- Presentation Stage Wrapper (Scale to Fit) -->
  <main class="stage-wrapper" id="stageWrapper">
    <div class="slide-canvas" id="slideCanvas">
      <!-- Dynamically Rendered by JS -->
    </div>
  </main>

  <!-- Speaker Notes Drawer -->
  <div class="speaker-drawer" id="speakerDrawer">
    <div class="drawer-top-bar">
      <div class="drawer-title-tag">🎙 Executive Speaker Script & Strategic Delivery Pacing</div>
      <div class="drawer-pacing-tag" id="drawerPacing">[0:00 - 0:30]</div>
    </div>
    <div class="drawer-script-body" id="drawerContent">
      "Good morning, faculty and executives of UCLA Anderson EMBA..."
    </div>
  </div>

  <!-- Bottom Deck Controller -->
  <footer class="deck-controls-footer">
    <div class="nav-btn-group">
      <button class="btn-slide-nav" id="btnPrev" title="Previous Slide (Arrow Left)">
        ◀ Previous
      </button>
      <button class="btn-slide-nav" id="btnNext" title="Next Slide (Arrow Right or Space)">
        Next ▶
      </button>
    </div>

    <div class="track-wrapper">
      <div class="track-bar-bg">
        <div class="track-bar-fill" id="trackBarFill"></div>
      </div>
      <div class="track-labels">
        <span id="labelSlideProgress">Slide 1 of 30</span>
        <span id="labelPartProgress">PART 1: MACRO CONTEXT & IMPERATIVE</span>
      </div>
    </div>

    <div class="key-shortcuts-hint">
      <span>Navigate: <kbd>◀</kbd> <kbd>▶</kbd> <kbd>Space</kbd></span>
      <span>Notes: <kbd>S</kbd></span>
      <span>Grid: <kbd>G</kbd></span>
      <span>Full: <kbd>F</kbd></span>
    </div>
  </footer>

  <!-- 30-Slide Grid Modal -->
  <div class="grid-overlay-modal" id="gridModal">
    <div class="grid-dialog">
      <div class="dialog-head">
        <h2 style="font-size: 16px; font-weight: 700; font-family: 'Montserrat';">30-Slide Executive Presentation Overview</h2>
        <button class="btn-header" id="btnCloseGrid">✕ Close</button>
      </div>
      <div class="dialog-body" id="dialogBody">
        <!-- Injected by JS -->
      </div>
    </div>
  </div>

  <script>
    {slides_js}

    let currentSlideIndex = 0;
    const totalSlides = slides.length;
    let notesOpen = false;

    // DOM Elements
    const canvas = document.getElementById('slideCanvas');
    const stageWrapper = document.getElementById('stageWrapper');
    const trackBarFill = document.getElementById('trackBarFill');
    const labelSlideProgress = document.getElementById('labelSlideProgress');
    const labelPartProgress = document.getElementById('labelPartProgress');
    const btnPrev = document.getElementById('btnPrev');
    const btnNext = document.getElementById('btnNext');
    const speakerDrawer = document.getElementById('speakerDrawer');
    const drawerContent = document.getElementById('drawerContent');
    const drawerPacing = document.getElementById('drawerPacing');
    const btnNotesToggle = document.getElementById('btnNotesToggle');
    const btnGridToggle = document.getElementById('btnGridToggle');
    const btnCloseGrid = document.getElementById('btnCloseGrid');
    const gridModal = document.getElementById('gridModal');
    const dialogBody = document.getElementById('dialogBody');
    const btnFullscreen = document.getElementById('btnFullscreen');

    // 16:9 Scale-to-Fit Engine
    function fitPresentation() {{
      if (!stageWrapper || !canvas) return;
      const w = stageWrapper.clientWidth - 32;
      const h = stageWrapper.clientHeight - 32;
      const nativeW = 1333;
      const nativeH = 750;
      const scale = Math.min(w / nativeW, h / nativeH, 1.35);
      canvas.style.transform = `scale(${{scale}})`;
    }}
    window.addEventListener('resize', fitPresentation);

    function renderSlide(index) {{
      const s = slides[index];
      const isCover = (s.num === 1);
      const isClosing = (s.num === 30);
      const hasImage = !!s.image;

      // 1. Cover Theme (Slide 01)
      if (isCover) {{
        canvas.className = 'slide-canvas theme-cover';
        canvas.innerHTML = `
          <div class="cover-inner-grid">
            <div>
              <div class="cover-top-pill">UCLA ANDERSON EXECUTIVE MBA DELEGATION VISIT | SEOUL 2026</div>
              <h1 class="cover-main-title">${{s.title}}</h1>
              <p class="cover-sub-lead">${{s.subtitle}}</p>
              
              <div class="cover-meta-box">
                <div class="cover-meta-item">
                  <span class="cover-meta-k">Session</span>
                  <span class="cover-meta-v">Session 3 - Korea Sovereign AI Strategy (English Briefing)</span>
                </div>
                <div class="cover-meta-item">
                  <span class="cover-meta-k">Speaker</span>
                  <span class="cover-meta-v">Andy | ISV Business Unit & AI Architecture Group, MegazoneCloud</span>
                </div>
                <div class="cover-meta-item">
                  <span class="cover-meta-k">Date & Venue</span>
                  <span class="cover-meta-v">Friday, Sep 11, 2026 | MegazoneCloud Gwacheon HQ (2F Grand Room)</span>
                </div>
              </div>
            </div>

            <div class="cover-visual-frame" onclick="window.open('${{s.image}}', '_blank')" title="Click to expand full-resolution graphic">
              <img src="${{s.image}}" alt="${{s.title}}">
            </div>
          </div>
          <div class="ppt-slide-footer" style="background: rgba(0, 18, 36, 0.7); border-color: rgba(255,255,255,0.1); color: #94A3B8;">
            <span>MegazoneCloud Gwacheon Smart Tower</span>
            <span style="color: var(--ucla-gold); font-family: 'Montserrat'; font-weight: 700;">SLIDE 01 / ${{totalSlides}}</span>
          </div>
        `;
      }}
      // 2. Closing Q&A Theme (Slide 30)
      else if (isClosing) {{
        canvas.className = 'slide-canvas theme-closing';
        canvas.innerHTML = `
          <div class="closing-inner-layout">
            <div>
              <div class="cover-top-pill">CONCLUSION & OPEN Q&A DISCUSSION</div>
              <h1 class="cover-main-title">${{s.title}}</h1>
              <p class="cover-sub-lead">${{s.subtitle}}</p>
            </div>

            <div class="closing-cards-grid">
              ${{s.bullets.map(b => `
                <div class="closing-meta-card">
                  <h3>${{b[0]}}</h3>
                  <p>${{b[1]}}</p>
                </div>
              `).join('')}}
            </div>

            <div class="ppt-concept-strip" style="background: rgba(255,255,255,0.08); border-left-color: var(--ucla-gold);">
              <span class="concept-label-tag" style="color: var(--ucla-gold);">Open Discussion</span>
              <span class="concept-text-info" style="color: #E2E8F0;">${{s.visual}}</span>
            </div>
          </div>
          <div class="ppt-slide-footer" style="background: rgba(0, 18, 36, 0.7); border-color: rgba(255,255,255,0.1); color: #94A3B8;">
            <span>UCLA Anderson Executive MBA | MegazoneCloud ISV Business Unit</span>
            <span style="color: var(--ucla-gold); font-family: 'Montserrat'; font-weight: 700;">SLIDE 30 / ${{totalSlides}}</span>
          </div>
        `;
      }}
      // 3. Body Content Slides (Slide 02 ~ 29: Dell Template System)
      else {{
        canvas.className = 'slide-canvas';

        let bodyHtml = '';

        // A. Split Layout with AI Image
        if (hasImage) {{
          const cardsHtml = s.bullets.map((b, i) => `
            <div class="ppt-template-card">
              <div class="card-top-row">
                <span class="card-index-box">${{String(i + 1).padStart(2, '0')}}</span>
                <span class="card-title-text">${{b[0]}}</span>
              </div>
              <div class="card-desc-text">${{b[1]}}</div>
            </div>
          `).join('');

          bodyHtml = `
            <div class="split-image-container">
              <div class="split-bullets-col">
                ${{cardsHtml}}
              </div>
              <div class="split-image-box" onclick="window.open('${{s.image}}', '_blank')" title="Click to expand full-resolution graphic">
                <img src="${{s.image}}" alt="${{s.title}}">
                <div class="split-image-tag">
                  <span>🔍 High-Resolution Architectural Graphic</span>
                  <span style="color: var(--ucla-gold); font-weight: 700;">16:9 AI Visual</span>
                </div>
              </div>
            </div>
          `;
        }}
        // B. Executive ROI Metric Scorecard (Slide 25 Special Layout)
        else if (s.num === 25) {{
          const badgeStyles = [
            {{ bg: '#EFF6FF', text: '#1D4ED8', border: '#BFDBFE', kpi: '75% CAPEX CUT' }},
            {{ bg: '#FEF3C7', text: '#B45309', border: '#FDE68A', kpi: '3.2kW POWER' }},
            {{ bg: '#ECFDF5', text: '#047857', border: '#A7F3D0', kpi: '3x FASTER' }},
            {{ bg: '#F5F3FF', text: '#6D28D9', border: '#DDD6FE', kpi: '100% AIR-GAPPED' }}
          ];

          const cardsHtml = s.bullets.map((b, i) => {{
            const style = badgeStyles[i] || badgeStyles[0];
            return `
              <div class="metric-card-box" style="border-color: ${{style.border}};">
                <div class="metric-pill-highlight" style="background: ${{style.bg}}; color: ${{style.text}}; border: 1px solid ${{style.border}};">
                  ${{style.kpi}}
                </div>
                <div class="card-top-row">
                  <span class="card-index-box">${{String(i + 1).padStart(2, '0')}}</span>
                  <span class="card-title-text">${{b[0]}}</span>
                </div>
                <div class="card-desc-text">${{b[1]}}</div>
              </div>
            `;
          }}).join('');

          bodyHtml = `
            <div class="grid-2x2-container">
              ${{cardsHtml}}
            </div>
          `;
        }}
        // C. 4 Bullets -> 2x2 Grid Template (Slide 2, 4, 6, 8, 10, 12, 20, 22, 23, 27, 29)
        else if (s.bullets.length === 4) {{
          const cardsHtml = s.bullets.map((b, i) => `
            <div class="ppt-template-card">
              <div class="card-top-row">
                <span class="card-index-box">${{String(i + 1).padStart(2, '0')}}</span>
                <span class="card-title-text">${{b[0]}}</span>
              </div>
              <div class="card-desc-text">${{b[1]}}</div>
            </div>
          `).join('');

          bodyHtml = `
            <div class="grid-2x2-container">
              ${{cardsHtml}}
            </div>
          `;
        }}
        // D. 3 Bullets -> 3-Column Grid Template
        else {{
          const cardsHtml = s.bullets.map((b, i) => `
            <div class="ppt-template-card">
              <div class="card-top-row">
                <span class="card-index-box">${{String(i + 1).padStart(2, '0')}}</span>
                <span class="card-title-text">${{b[0]}}</span>
              </div>
              <div class="card-desc-text">${{b[1]}}</div>
            </div>
          `).join('');

          bodyHtml = `
            <div class="grid-3col-container">
              ${{cardsHtml}}
            </div>
          `;
        }}

        canvas.innerHTML = `
          <div class="ppt-slide-header">
            <div class="header-title-box">
              <span class="part-pill-badge">${{s.part}}</span>
              <h2 class="slide-master-title">${{String(s.num).padStart(2, '0')}}.  ${{s.title}}</h2>
              <p class="slide-master-subtitle">STRATEGIC FOCUS: ${{s.subtitle}}</p>
            </div>
            <div class="header-logo-tag">MegazoneCloud x UCLA EMBA</div>
          </div>

          <div class="ppt-slide-body">
            ${{bodyHtml}}
            <div class="ppt-concept-strip">
              <span class="concept-label-tag">Visual Concept</span>
              <span class="concept-text-info">${{s.visual}}</span>
            </div>
          </div>

          <div class="ppt-slide-footer">
            <span class="footer-left-info">UCLA Anderson Executive MBA Delegation | Session 3: Korea Sovereign AI Strategy | Speaker: Andy</span>
            <span class="footer-right-index">Slide ${{String(s.num).padStart(2, '0')}} / ${{totalSlides}}</span>
          </div>
        `;
      }}

      // Update Trackbar & Texts
      const pct = ((index + 1) / totalSlides) * 100;
      trackBarFill.style.width = pct + '%';
      labelSlideProgress.textContent = `Slide ${{index + 1}} of ${{totalSlides}}`;
      labelPartProgress.textContent = s.part;

      // Update Speaker Notes Drawer
      drawerContent.textContent = `"${{s.notes}}"`;
      drawerPacing.textContent = `[PACING: ${{s.duration}}]`;

      // Nav Buttons State
      btnPrev.disabled = index === 0;
      btnNext.disabled = index === totalSlides - 1;

      // Update Active Card in Modal
      document.querySelectorAll('.grid-thumb-card').forEach((el, idx) => {{
        if (idx === index) el.classList.add('current');
        else el.classList.remove('current');
      }});

      // Fit Canvas
      fitPresentation();
    }}

    function goToSlide(index) {{
      if (index >= 0 && index < totalSlides) {{
        currentSlideIndex = index;
        renderSlide(currentSlideIndex);
      }}
    }}

    function nextSlide() {{
      if (currentSlideIndex < totalSlides - 1) {{
        goToSlide(currentSlideIndex + 1);
      }}
    }}

    function prevSlide() {{
      if (currentSlideIndex > 0) {{
        goToSlide(currentSlideIndex - 1);
      }}
    }}

    function toggleNotes() {{
      notesOpen = !notesOpen;
      if (notesOpen) {{
        speakerDrawer.classList.add('open');
      }} else {{
        speakerDrawer.classList.remove('open');
      }}
    }}

    function toggleGrid() {{
      gridModal.classList.toggle('active');
    }}

    function toggleFullscreen() {{
      if (!document.fullscreenElement) {{
        document.documentElement.requestFullscreen().catch(err => alert(err.message));
      }} else {{
        document.exitFullscreen();
      }}
    }}

    // Build 30-Slide Overview Modal
    function buildGrid() {{
      dialogBody.innerHTML = '';
      slides.forEach((s, i) => {{
        const thumb = document.createElement('div');
        thumb.className = `grid-thumb-card ${{i === currentSlideIndex ? 'current' : ''}}`;
        thumb.innerHTML = `
          <div class="thumb-num">SLIDE ${{String(s.num).padStart(2, '0')}}</div>
          <div class="thumb-title">${{s.title}}</div>
        `;
        thumb.addEventListener('click', () => {{
          goToSlide(i);
          gridModal.classList.remove('active');
        }});
        dialogBody.appendChild(thumb);
      }});
    }}

    // Keyboard Shortcuts
    document.addEventListener('keydown', (e) => {{
      if (gridModal.classList.contains('active')) {{
        if (e.key === 'Escape') gridModal.classList.remove('active');
        return;
      }}

      if (e.key === 'ArrowRight' || e.key === 'PageDown' || e.key === ' ') {{
        e.preventDefault();
        nextSlide();
      }} else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {{
        e.preventDefault();
        prevSlide();
      }} else if (e.key === 'Home') {{
        e.preventDefault();
        goToSlide(0);
      }} else if (e.key === 'End') {{
        e.preventDefault();
        goToSlide(totalSlides - 1);
      }} else if (e.key === 's' || e.key === 'S') {{
        toggleNotes();
      }} else if (e.key === 'g' || e.key === 'G') {{
        toggleGrid();
      }} else if (e.key === 'f' || e.key === 'F') {{
        toggleFullscreen();
      }} else if (e.key === 'Escape') {{
        if (notesOpen) toggleNotes();
      }}
    }});

    // Event Listeners
    btnPrev.addEventListener('click', prevSlide);
    btnNext.addEventListener('click', nextSlide);
    btnNotesToggle.addEventListener('click', toggleNotes);
    btnGridToggle.addEventListener('click', toggleGrid);
    btnCloseGrid.addEventListener('click', toggleGrid);
    btnFullscreen.addEventListener('click', toggleFullscreen);

    // 15-Minute Executive Countdown Timer
    let timeLeftSeconds = 15 * 60;
    const timerElem = document.getElementById('sessionTimer');
    const timerInterval = setInterval(() => {{
      if (timeLeftSeconds <= 0) {{
        timerElem.textContent = "⏱ 00:00 (Q&A TIME)";
        timerElem.style.color = "#F59E0B";
        clearInterval(timerInterval);
        return;
      }}
      timeLeftSeconds--;
      const m = Math.floor(timeLeftSeconds / 60);
      const s = timeLeftSeconds % 60;
      timerElem.textContent = `⏱ ${{String(m).padStart(2, '0')}}:${{String(s).padStart(2, '0')}} REMAINING`;
    }}, 1000);

    // Initial Execution
    buildGrid();
    renderSlide(currentSlideIndex);
    setTimeout(fitPresentation, 50);
  </script>
</body>
</html>
"""

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print("Successfully applied PPT template layout to HTML deck!")
