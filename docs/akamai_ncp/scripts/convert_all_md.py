import os
import re

try:
    import markdown
    from bs4 import BeautifulSoup
except ImportError:
    print("오류: 파이썬 'markdown' 또는 'beautifulsoup4' 라이브러리가 설치되어 있지 않습니다.")
    exit(1)

# 클린 문서형(Word Paper UI 기본) + 다크모드 토글 및 내부 논의 보완항목 네비게이터 지원 HTML 템플릿
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="ko" data-theme="light">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <!-- 한글 가독성 최적화 웹폰트 (Pretendard & Noto Sans KR) -->
    <link rel="stylesheet" as="style" crossorigin href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css" />
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            --canvas-bg: #e8edf3;
            --card-bg: #ffffff;
            --card-border: #cfd8e3;
            --primary: #185abd;
            --primary-soft: #eef4fc;
            --heading-h1: #0f172a;
            --heading-h2: #1e3a8a;
            --heading-h3: #0f172a;
            --heading-h4: #1d4ed8;
            --text-main: #1e293b;
            --text-sub: #334155;
            --text-muted: #64748b;
            --table-border: #cbd5e1;
            --table-head-bg: #f1f5f9;
            --table-head-text: #0f172a;
            --table-hover: #f8fafc;
            --quote-bg: #f8fafc;
            --quote-text: #1e3a8a;
            --code-bg: #f1f5f9;
            --code-text: #0f172a;
            --review-red: #ee0000;
            --review-row-bg: #fff5f5;
            --toolbar-bg: #ffffff;
            --toolbar-border: #cbd5e1;
        }}

        [data-theme="dark"] {{
            --canvas-bg: #0b0c10;
            --card-bg: #151922;
            --card-border: rgba(255, 255, 255, 0.12);
            --primary: #3b82f6;
            --primary-soft: rgba(59, 130, 246, 0.15);
            --heading-h1: #f8fafc;
            --heading-h2: #93c5fd;
            --heading-h3: #a7f3d0;
            --heading-h4: #bfdbfe;
            --text-main: #e5e7eb;
            --text-sub: #d1d5db;
            --text-muted: #9ca3af;
            --table-border: rgba(255, 255, 255, 0.14);
            --table-head-bg: rgba(30, 41, 59, 0.85);
            --table-head-text: #93c5fd;
            --table-hover: rgba(255, 255, 255, 0.03);
            --quote-bg: rgba(59, 130, 246, 0.08);
            --quote-text: #93c5fd;
            --code-bg: rgba(255, 255, 255, 0.08);
            --code-text: #f3f4f6;
            --review-red: #ff6b6b;
            --review-row-bg: rgba(239, 68, 68, 0.12);
            --toolbar-bg: #111827;
            --toolbar-border: rgba(255, 255, 255, 0.12);
        }}

        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        html {{
            scroll-behavior: smooth;
        }}

        body {{
            background-color: var(--canvas-bg);
            font-family: 'Pretendard', 'Noto Sans KR', 'Malgun Gothic', '맑은 고딕', sans-serif;
            color: var(--text-main);
            line-height: 1.76;
            word-break: keep-all;
            -webkit-font-smoothing: antialiased;
            padding-bottom: 50px;
        }}

        /* 상단 고정 문서 컨트롤 바 (인쇄 및 DOCX 변환 시 자동 제외) */
        .doc-toolbar {{
            position: sticky;
            top: 0;
            z-index: 1000;
            background: var(--toolbar-bg);
            border-bottom: 1px solid var(--toolbar-border);
            box-shadow: 0 2px 10px rgba(15, 23, 42, 0.06);
        }}

        .toolbar-inner {{
            max-width: 1120px;
            margin: 0 auto;
            padding: 10px 24px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 10px;
        }}

        .toolbar-left {{
            display: flex;
            align-items: center;
            gap: 12px;
            flex-wrap: wrap;
        }}

        .nav-back-link {{
            color: var(--primary);
            text-decoration: none;
            font-size: 0.88rem;
            font-weight: 600;
            padding: 4px 10px;
            border-radius: 6px;
            background: var(--primary-soft);
            transition: opacity 0.15s ease;
        }}

        .nav-back-link:hover {{
            opacity: 0.85;
        }}

        .doc-badge {{
            font-size: 0.82rem;
            font-weight: 700;
            color: var(--text-muted);
            letter-spacing: -0.01em;
        }}

        .toolbar-actions {{
            display: flex;
            align-items: center;
            gap: 8px;
            flex-wrap: wrap;
        }}

        .t-btn {{
            cursor: pointer;
            font-family: inherit;
            font-size: 0.82rem;
            font-weight: 600;
            padding: 5px 12px;
            border-radius: 6px;
            border: 1px solid var(--table-border);
            background: var(--card-bg);
            color: var(--text-main);
            transition: all 0.15s ease;
        }}

        .t-btn:hover {{
            border-color: var(--primary);
            color: var(--primary);
        }}

        .t-btn.active-hl {{
            background: #fff1f2;
            border-color: #ee0000;
            color: #ee0000;
        }}

        /* 내부 논의용 타 부서 자료보완 항목 바로가기 바 */
        .review-nav-bar {{
            background: #fff8f8;
            border-top: 1px solid #fecaca;
            padding: 8px 24px;
        }}

        [data-theme="dark"] .review-nav-bar {{
            background: rgba(127, 29, 29, 0.25);
            border-top-color: rgba(248, 113, 113, 0.3);
        }}

        .review-nav-inner {{
            max-width: 1120px;
            margin: 0 auto;
            display: flex;
            align-items: center;
            flex-wrap: wrap;
            gap: 6px;
        }}

        .review-nav-title {{
            font-size: 0.8rem;
            font-weight: 700;
            color: var(--review-red);
            margin-right: 4px;
        }}

        .rev-chip {{
            display: inline-block;
            font-size: 0.76rem;
            font-weight: 600;
            color: #b91c1c;
            background: #ffffff;
            border: 1px solid #fca5a5;
            border-radius: 999px;
            padding: 2px 10px;
            text-decoration: none;
            transition: all 0.15s ease;
        }}

        [data-theme="dark"] .rev-chip {{
            color: #fca5a5;
            background: rgba(15, 23, 42, 0.7);
            border-color: rgba(248, 113, 113, 0.45);
        }}

        .rev-chip:hover {{
            background: #fee2e2;
            border-color: #ef4444;
        }}

        /* 메인 컨테이너 및 문서 카드 (Word 용지 스타일) */
        .container {{
            max-width: 1120px;
            margin: 28px auto 0;
            padding: 0 20px;
        }}

        .report-card {{
            background: var(--card-bg);
            border: 1px solid var(--card-border);
            border-radius: 12px;
            padding: 52px 58px;
            box-shadow: 0 10px 30px rgba(15, 23, 42, 0.07);
        }}

        @media (max-width: 768px) {{
            .report-card {{
                padding: 28px 20px;
            }}
        }}

        /* 문서 헤더 스타일 (Word 16pt/14pt/12pt 계층 반영) */
        header {{
            border-bottom: 2px solid var(--table-border);
            padding-bottom: 22px;
            margin-bottom: 28px;
        }}

        header h1 {{
            font-size: 1.75rem;
            font-weight: 800;
            color: var(--heading-h1);
            line-height: 1.35;
            letter-spacing: -0.02em;
        }}

        /* 본문 제목 위계 */
        h2 {{
            font-size: 1.38rem;
            font-weight: 800;
            color: var(--heading-h2);
            margin-top: 38px;
            margin-bottom: 16px;
            border-left: 4px solid var(--primary);
            padding-left: 12px;
            line-height: 1.4;
        }}

        main > h2:first-child {{
            margin-top: 8px;
        }}

        h3 {{
            font-size: 1.16rem;
            font-weight: 700;
            color: var(--heading-h3);
            margin-top: 26px;
            margin-bottom: 12px;
            line-height: 1.45;
        }}

        h4 {{
            font-size: 1.04rem;
            font-weight: 700;
            color: var(--heading-h4);
            margin-top: 20px;
            margin-bottom: 10px;
            line-height: 1.45;
        }}

        p {{
            margin-bottom: 14px;
            color: var(--text-main);
            font-size: 0.97rem;
        }}

        /* 메타 정보 문단 박스 정돈 */
        p.doc-meta-box {{
            background: var(--table-hover);
            border: 1px solid var(--table-border);
            border-radius: 8px;
            padding: 16px 20px;
            font-size: 0.92rem;
            line-height: 1.85;
            margin-bottom: 24px;
        }}

        code {{
            font-family: 'Consolas', 'Menlo', monospace;
            font-size: 0.88em;
            background: var(--code-bg);
            color: var(--code-text);
            padding: 2px 6px;
            border-radius: 4px;
        }}

        pre code {{
            display: block;
            padding: 14px 16px;
            overflow-x: auto;
            line-height: 1.55;
        }}

        /* 목록 스타일링 — 상위 그룹 헤더와 1·2단계 하위 목록 명확 분리 (Word 수정 포맷 반영) */
        ol {{
            margin-top: 6px;
            margin-bottom: 18px;
            padding-left: 24px;
            list-style-type: decimal;
        }}

        ul {{
            margin-top: 6px;
            margin-bottom: 18px;
            padding-left: 22px;
            list-style-type: disc;
        }}

        li {{
            margin-bottom: 8px;
            color: var(--text-sub);
            font-size: 0.96rem;
            line-height: 1.72;
            padding-left: 3px;
        }}

        /* 하위 목록을 품은 대항목(그룹 항목) 간 호흡 여백 확보 */
        li.has-sublist {{
            margin-top: 14px;
            margin-bottom: 14px;
            color: var(--text-main);
        }}

        li.has-sublist > ul,
        li.has-sublist > ol {{
            margin-top: 7px;
            margin-bottom: 8px;
            padding-left: 24px;
        }}

        /* 2단계 이상 중첩 목록 (예: R3 실적의 계약 주체 / 준공 여부) */
        ul ul, ol ul {{
            list-style-type: disc;
        }}

        ul ul ul, ol ul ul, ul ol ul {{
            list-style-type: circle;
            margin-top: 4px;
            margin-bottom: 6px;
            padding-left: 24px;
        }}

        /* 대괄호 카테고리 헤더 (예: [Physical AI / 제조 특화 AI 아키텍처 실적]) — 불릿 제거 */
        li.category-header {{
            list-style: none;
            margin-left: -18px;
            margin-top: 18px;
            margin-bottom: 10px;
            color: var(--heading-h3);
        }}

        /* 표(Table) 스타일링 — Word Table Grid 가독성 반영 */
        .table-wrap {{
            width: 100%;
            overflow-x: auto;
            margin: 18px 0 24px;
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 0.89rem;
            line-height: 1.58;
            border: 1px solid var(--table-border);
        }}

        th {{
            background: var(--table-head-bg);
            color: var(--table-head-text);
            font-weight: 700;
            padding: 10px 12px;
            border: 1px solid var(--table-border);
            border-bottom: 2px solid #94a3b8;
            text-align: left;
            vertical-align: middle;
        }}

        td {{
            padding: 9px 12px;
            border: 1px solid var(--table-border);
            color: var(--text-main);
            vertical-align: top;
        }}

        tr:hover td {{
            background: var(--table-hover);
        }}

        /* 타 부서 자료보완 / 현행화 확인 필요 표시 (Word COLOR=#EE0000 1:1 매핑) */
        .review-red {{
            color: var(--review-red) !important;
        }}

        body.highlight-review .review-red {{
            background-color: rgba(238, 0, 0, 0.09);
            box-shadow: 0 0 0 2px rgba(238, 0, 0, 0.15);
            border-radius: 3px;
            padding: 1px 3px;
        }}

        tr.review-row td {{
            background-color: var(--review-row-bg);
        }}

        @keyframes pulseFocus {{
            0% {{ background-color: #fef08a; box-shadow: 0 0 0 6px #fef08a; }}
            100% {{ background-color: transparent; box-shadow: none; }}
        }}

        .jump-focus {{
            animation: pulseFocus 2.2s ease-out;
            border-radius: 4px;
        }}

        /* 인용구(Blockquote) */
        blockquote {{
            border-left: 4px solid var(--primary);
            background: var(--quote-bg);
            padding: 14px 18px;
            margin: 18px 0;
            border-radius: 0 8px 8px 0;
        }}

        blockquote p, blockquote li {{
            color: var(--quote-text);
            margin-bottom: 4px;
        }}

        hr {{
            border: 0;
            height: 1px;
            background: var(--table-border);
            margin: 28px 0;
        }}

        .mermaid {{
            background: #f8fafc;
            border: 1px solid var(--table-border);
            border-radius: 8px;
            padding: 18px;
            margin: 14px 0 22px;
            text-align: center;
            overflow-x: auto;
        }}

        [data-theme="dark"] .mermaid {{
            background: rgba(15, 23, 42, 0.6);
        }}

        img {{
            max-width: 100%;
            height: auto;
            border-radius: 8px;
            border: 1px solid var(--table-border);
            margin: 16px 0;
        }}

        .footnote {{
            margin-top: 36px;
            padding-top: 18px;
            border-top: 1px dashed var(--table-border);
            font-size: 0.86rem;
            color: var(--text-muted);
        }}

        footer.doc-footer {{
            text-align: center;
            margin-top: 36px;
            color: var(--text-muted);
            font-size: 0.8rem;
        }}

        @media print {{
            body {{
                background: #ffffff;
                padding: 0;
            }}
            .doc-toolbar {{
                display: none !important;
            }}
            .container {{
                max-width: 100%;
                margin: 0;
                padding: 0;
            }}
            .report-card {{
                border: none;
                box-shadow: none;
                padding: 0;
            }}
        }}
    </style>
</head>
<body>

<div class="doc-toolbar">
    <div class="toolbar-inner">
        <div class="toolbar-left">
            {nav_back_html}
            <span class="doc-badge">{doc_badge}</span>
        </div>
        <div class="toolbar-actions">
            {hl_btn_html}
            <button type="button" class="t-btn" id="themeToggleBtn" onclick="toggleTheme()">다크 모드</button>
            <button type="button" class="t-btn" onclick="window.print()">인쇄 / PDF 저장</button>
        </div>
    </div>
    {review_nav_html}
</div>

<div class="container">
    <div class="report-card">
        <header>
            <h1>{header_title}</h1>
        </header>

        <main id="docContent">
            {body_content}
        </main>
    </div>

    <footer class="doc-footer">
        <p>{footer_text}</p>
    </footer>
</div>

<script>
    function toggleTheme() {{
        const html = document.documentElement;
        const btn = document.getElementById('themeToggleBtn');
        if (html.getAttribute('data-theme') === 'dark') {{
            html.setAttribute('data-theme', 'light');
            btn.textContent = '다크 모드';
        }} else {{
            html.setAttribute('data-theme', 'dark');
            btn.textContent = '라이트 모드(문서형)';
        }}
    }}

    function toggleReviewHighlight(btn) {{
        document.body.classList.toggle('highlight-review');
        btn.classList.toggle('active-hl');
    }}

    function jumpToReview(id) {{
        const el = document.getElementById(id);
        if (!el) return;
        const y = el.getBoundingClientRect().top + window.pageYOffset - 120;
        window.scrollTo({{ top: y, behavior: 'smooth' }});
        const target = el.closest('tr') || el.closest('li') || el.closest('p') || el;
        target.classList.remove('jump-focus');
        void target.offsetWidth;
        target.classList.add('jump-focus');
    }}
</script>
</body>
</html>
"""


def _resolve_doc_metadata(md_path):
    """문서 경로와 파일명에 맞는 상단 배지 및 하단 푸터 문구를 반환합니다."""
    norm = md_path.replace('\\', '/').lower()
    fname = os.path.basename(norm)

    if 'wonik_ax_center' in norm or 'wonik_robotics' in fname:
        if 'rfi_response' in fname:
            badge = "원익로보틱스 AX Center RFI 공식 회신서 · 내부 논의 및 자료보완본 (2026.11.18)"
        elif 'written_inquiry' in fname:
            badge = "원익로보틱스 AX Center RFI 공식 서면 질의서"
        else:
            badge = "원익로보틱스 AX Center 구축 MP 사업 제안 문서"
        footer = "© 2026 MEGAZONECLOUD CORP. — 원익로보틱스 AX Center 구축 MP 사업 전담 TF (대외비 · Confidential)"
    elif 'daegu_suseong_aidc' in norm or 'daegu_' in fname:
        badge = "대구 수성알파시티 AIDC & 피지컬 AI 로봇 트레이닝 센터 기획"
        footer = "© 2026 MEGAZONECLOUD CORP. — 대구 AIDC & Physical AI 추진 TF"
    else:
        badge = "MZC 하이브리드 클라우드 & AI 인프라 사업 기획"
        footer = "© 2026 MEGAZONECLOUD HYBRID CLOUD & AI INFRASTRUCTURE GROUP."

    return badge, footer


def _postprocess_html_structure(body_html):
    """
    마크다운 변환 결과 HTML을 정밀 보정하여:
    1) 문서 상단 메타데이터 문단 박스화
    2) 하위 목록을 가진 li에 has-sublist, 대괄호 카테고리 헤더에 category-header 부여
    3) 표를 .table-wrap으로 감싸고 .review-red가 있는 행에 .review-row 부여
    4) data-rev-label 항목을 수집하여 상단 바로가기 칩 목록 생성
    """
    soup = BeautifulSoup(body_html, 'html.parser')

    # 1) 상단 문서 메타 정보 문단(문서 번호: ... 제출 일자: ...) 스타일 부여
    for p in soup.find_all('p', limit=4):
        txt = p.get_text()
        if '문서 번호' in txt and ('제출 일자' in txt or '작성 일자' in txt):
            p['class'] = p.get('class', []) + ['doc-meta-box']
            break

    # 2) 중첩 목록 및 대괄호 카테고리 헤더 클래스 부여
    for li in soup.find_all('li'):
        sub_lists = li.find_all(['ul', 'ol'], recursive=False)
        if sub_lists:
            classes = list(li.get('class', []))
            classes.append('has-sublist')
            # 직계 첫 텍스트 또는 strong 텍스트가 '['로 시작하고 하위 ol을 가진 경우 카테고리 소제목 처리
            direct_txt = ''.join(
                c.get_text() if hasattr(c, 'get_text') else str(c)
                for c in li.contents
                if getattr(c, 'name', None) not in ('ul', 'ol')
            ).strip()
            if direct_txt.startswith('[') and direct_txt.endswith(']') and li.find('ol', recursive=False):
                classes.append('category-header')
            li['class'] = classes

    # 3) 표 반응형 래퍼 및 보완 필요 행(.review-row) 표시
    for tbl in soup.find_all('table'):
        for tr in tbl.find_all('tr'):
            if tr.find(class_='review-red'):
                tr['class'] = list(tr.get('class', [])) + ['review-row']
        if not (tbl.parent and 'table-wrap' in tbl.parent.get('class', [])):
            wrap = soup.new_tag('div', **{'class': 'table-wrap'})
            tbl.wrap(wrap)

    # 4) 내부 논의용 타 부서 자료보완 항목(data-rev-label) 추출
    review_items = []
    for idx, elem in enumerate(soup.find_all(attrs={'data-rev-label': True}), 1):
        rid = elem.get('id')
        if not rid:
            rid = f'rev-auto-{idx}'
            elem['id'] = rid
        review_items.append((rid, elem['data-rev-label']))

    return str(soup), review_items


def _normalize_md_list_indent(md_text):
    """
    Python markdown 파서(기본 4칸 들여쓰기 규칙)에서 2~3칸 또는 5~6칸으로 작성된
    중첩 목록이 상위 목록으로 평탄화(번호 깨짐)되는 문제를 방지하기 위해,
    코드블록 외부의 중첩 리스트 들여쓰기를 4칸/8칸 배수로 정규화합니다.
    """
    out = []
    in_fence = False
    list_re = re.compile(r'^( +)([\*\-\+]|\d+\.)(\s+.*)$')

    for line in md_text.splitlines():
        stripped = line.lstrip()
        if stripped.startswith('```'):
            in_fence = not in_fence
            out.append(line)
            continue
        if in_fence:
            out.append(line)
            continue

        m = list_re.match(line)
        if m:
            spaces = len(m.group(1))
            marker = m.group(2)
            rest = m.group(3)
            if 2 <= spaces <= 4:
                norm_spaces = 4
            elif 5 <= spaces <= 8:
                norm_spaces = 8
            elif spaces >= 9:
                norm_spaces = 12
            else:
                norm_spaces = spaces
            out.append((' ' * norm_spaces) + marker + rest)
        else:
            out.append(line)
    return '\n'.join(out)


def convert_md_to_html(md_path, html_path, standalone=False):
    print(f"변환 중: {md_path} -> {html_path}")

    with open(md_path, 'r', encoding='utf-8') as f:
        md_text = f.read()

    # 1. 1행의 대제목(# 제목)을 읽어 타이틀로 파싱
    header_title = "메가존클라우드 사업 기획 문서"
    title_match = re.search(r'^#\s+(.+)$', md_text, re.MULTILINE)
    if title_match:
        header_title = title_match.group(1).strip()
        md_text = md_text.replace(title_match.group(0), "", 1)

    # 1-1. 중첩 목록 들여쓰기 정규화 (평탄화 및 번호 깨짐 원천 방지)
    md_text = _normalize_md_list_indent(md_text)

    # 2. 마크다운 확장 기능 변환
    extensions = ['tables', 'fenced_code', 'nl2br', 'footnotes']
    body_content = markdown.markdown(md_text, extensions=extensions)

    # mermaid 코드블럭을 div.mermaid 로 변환
    body_content = re.sub(
        r'<pre><code class="language-mermaid">([\s\S]*?)</code></pre>',
        r'<div class="mermaid">\1</div>',
        body_content
    )

    # 3. DOM 구조 정밀 보정 및 자료보완 항목 추출
    body_content, review_items = _postprocess_html_structure(body_content)

    # 4. Mermaid 스크립트 주입 (문서형 라이트 테마와 어울리는 neutral 테마 적용)
    mermaid_script = """<script type="module">
    import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
    mermaid.initialize({ startOnLoad: true, theme: 'neutral' });
</script>"""
    if '<div class="mermaid">' in body_content:
        body_content += f"\n{mermaid_script}"

    # 5. 네비게이션 링크 및 보완 항목 툴바 구성
    doc_badge, footer_text = _resolve_doc_metadata(md_path)

    nav_back_html = ""
    if not standalone:
        current_script_dir = os.path.dirname(os.path.abspath(__file__))
        base_dir = os.path.abspath(os.path.join(current_script_dir, '..'))
        readme_html = os.path.join(base_dir, 'README.html')
        html_abs_dir = os.path.dirname(os.path.abspath(html_path))
        if os.path.abspath(html_path).lower() != os.path.abspath(readme_html).lower():
            rel_readme = os.path.relpath(readme_html, html_abs_dir).replace('\\', '/')
            nav_back_html = f'<a class="nav-back-link" href="{rel_readme}">← 전체 문서 목록(README)</a>'

    review_nav_html = ""
    hl_btn_html = ""
    if review_items:
        chips = "".join(
            f'<a href="#{rid}" class="rev-chip" onclick="event.preventDefault(); jumpToReview(\'{rid}\');">{label}</a>'
            for rid, label in review_items
        )
        review_nav_html = (
            '<div class="review-nav-bar">'
            '<div class="review-nav-inner">'
            f'<span class="review-nav-title">타 부서 자료보완 · 확인 필요 ({len(review_items)}건):</span>'
            f'{chips}'
            '</div>'
            '</div>'
        )
        hl_btn_html = '<button type="button" class="t-btn" onclick="toggleReviewHighlight(this)">보완항목 형광강조</button>'

    final_html = HTML_TEMPLATE.format(
        title=header_title,
        header_title=header_title,
        doc_badge=doc_badge,
        footer_text=footer_text,
        nav_back_html=nav_back_html,
        hl_btn_html=hl_btn_html,
        review_nav_html=review_nav_html,
        body_content=body_content
    )

    dir_name = os.path.dirname(html_path)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(final_html)

    print(f"완료: {html_path} 생성")


def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.abspath(os.path.join(current_dir, '..'))
    has_docs_subdir = os.path.isdir(os.path.join(base_dir, 'docs'))
    prefix = 'docs/' if has_docs_subdir else ''

    # 변환 대상 마크다운 파일과 출력될 HTML 파일 맵
    # 커스텀 슬라이드 덱 UI 파일들은 자동 덮어쓰기에서 제외(Skip) 처리
    conversion_targets = {
        'README.md': 'README.html',
        'handover.md': 'handover.html',
        f'{prefix}research/akamai_nvidia_partnership.md': f'{prefix}research/akamai_nvidia_partnership.html',
        f'{prefix}research/nvidia_ncp_market_analysis.md': f'{prefix}research/nvidia_ncp_market_analysis.html',
        f'{prefix}proposal/mzc_akamai_partnership.md': f'{prefix}proposal/mzc_akamai_partnership.html',
        f'{prefix}daegu_suseong_aidc/2026-11-14_daegu_aidc_document_summary_report.md': f'{prefix}daegu_suseong_aidc/2026-11-14_daegu_aidc_document_summary_report.html',
        f'{prefix}daegu_suseong_aidc/2026-11-14_mzc_internal_strategy_land_aws_offload_and_hybrid_10mw.md': f'{prefix}daegu_suseong_aidc/2026-11-14_mzc_internal_strategy_land_aws_offload_and_hybrid_10mw.html',
        f'{prefix}daegu_suseong_aidc/2026-11-12_kiria_1st_meeting_executive_summary.md': f'{prefix}daegu_suseong_aidc/2026-11-12_kiria_1st_meeting_executive_summary.html',
        f'{prefix}daegu_suseong_aidc/2026-11-12_daegu_aidc_budget_structure_and_revenue_puzzle.md': f'{prefix}daegu_suseong_aidc/2026-11-12_daegu_aidc_budget_structure_and_revenue_puzzle.html',
        f'{prefix}daegu_suseong_aidc/2026-11-12_daegu_aidc_reverse_costing_pf_risk_and_jb_dongtan_analysis.md': f'{prefix}daegu_suseong_aidc/2026-11-12_daegu_aidc_reverse_costing_pf_risk_and_jb_dongtan_analysis.html',
        f'{prefix}daegu_suseong_aidc/2026-11-12_daegu_aidc_kiria_meeting_and_5mw_business_ideation.md': f'{prefix}daegu_suseong_aidc/2026-11-12_daegu_aidc_kiria_meeting_and_5mw_business_ideation.html',
        f'{prefix}daegu_suseong_aidc/daegu_aidc_physical_ai_preliminary_study.md': f'{prefix}daegu_suseong_aidc/daegu_aidc_physical_ai_preliminary_study.html',
        f'{prefix}daegu_suseong_aidc/daegu_suseong_robot_training_center_proposal.md': f'{prefix}daegu_suseong_aidc/daegu_suseong_robot_training_center_proposal.html',
        f'{prefix}daegu_suseong_aidc/daegu_physical_ai_robot_training_center_proposal.md': f'{prefix}daegu_suseong_aidc/daegu_physical_ai_robot_training_center_proposal.html',
        f'{prefix}wonik_ax_center/20261118_wonik_robotics_ax_center_rfi_response.md': f'{prefix}wonik_ax_center/20261118_wonik_robotics_ax_center_rfi_response.html',
        f'{prefix}wonik_ax_center/wonik_robotics_ax_center_rfi_response.md': f'{prefix}wonik_ax_center/wonik_robotics_ax_center_rfi_response.html',
        f'{prefix}wonik_ax_center/wonik_robotics_ax_center_rfi_response_scp_draft.md': f'{prefix}wonik_ax_center/wonik_robotics_ax_center_rfi_response_scp_draft.html',
        f'{prefix}wonik_ax_center/wonik_robotics_ax_center_proposal.md': f'{prefix}wonik_ax_center/wonik_robotics_ax_center_proposal.html',
        f'{prefix}wonik_ax_center/2026-11-11_wonik_robotics_ax_center_proposal_v2.md': f'{prefix}wonik_ax_center/2026-11-11_wonik_robotics_ax_center_proposal_v2.html',
        f'{prefix}wonik_ax_center/wonik_robotics_ax_center_rfi_written_inquiry.md': f'{prefix}wonik_ax_center/wonik_robotics_ax_center_rfi_written_inquiry.html',
        f'{prefix}wonik_ax_center/archive/wonik_rfi_v12_vs_v17_comparison.md': f'{prefix}wonik_ax_center/archive/wonik_rfi_v12_vs_v17_comparison.html',
        f'{prefix}wonik_ax_center/archive/wonik_robotics_ax_center_rfp_spec_in_recommendations.md': f'{prefix}wonik_ax_center/archive/wonik_robotics_ax_center_rfp_spec_in_recommendations.html'
    }

    for md_rel, html_rel in conversion_targets.items():
        md = os.path.join(base_dir, md_rel)
        html = os.path.join(base_dir, html_rel)
        if os.path.exists(md):
            convert_md_to_html(md, html)
        else:
            print(f"경고: {md} 파일을 찾을 수 없어 변환을 생략합니다.")

    print("\n[성공] 지정된 모든 마크다운 파일들의 HTML 변환이 성공적으로 끝났습니다.")

    # HTML to DOCX 자동 연동 (수동 편집 정본 DOCX는 보호됨)
    try:
        import sys
        if current_dir not in sys.path:
            sys.path.append(current_dir)
        from convert_html_to_docx import main as convert_to_docx
        print("\n[DOCX 동기화] HTML 문서를 Word(DOCX) 형식으로 일괄 동기화합니다...")
        convert_to_docx()
    except Exception as e:
        print(f"[DOCX 동기화 경고] DOCX 변환 진행 중 오류 발생: {e}")


if __name__ == '__main__':
    main()
