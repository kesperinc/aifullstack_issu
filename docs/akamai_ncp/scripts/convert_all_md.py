import os
import re

# markdown 라이브러리가 없을 경우 pip로 설치할 수 있도록 안내하기 위해 try-except 적용
try:
    import markdown
except ImportError:
    print("오류: 파이썬 'markdown' 라이브러리가 설치되어 있지 않습니다.")
    print("가상환경 내에서 'pip install markdown'을 먼저 실행해 주십시오.")
    exit(1)

# 프리미엄 CSS 테마가 입혀진 HTML 템플릿
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <!-- 구글 폰트 적용 (Outfit & Noto Sans KR) -->
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700&family=Outfit:wght@300;400;600;800&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-color: #0b0c10;
            --card-bg: rgba(22, 25, 32, 0.7);
            --card-border: rgba(255, 255, 255, 0.08);
            --primary: #3b82f6;
            --primary-grad: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
            --accent: #ef4444;
            --success: #10b981;
            --text-main: #f3f4f6;
            --text-muted: #9ca3af;
        }}

        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            background-color: var(--bg-color);
            background-image: 
                radial-gradient(at 0% 0%, rgba(29, 78, 216, 0.12) 0, transparent 50%),
                radial-gradient(at 100% 100%, rgba(16, 185, 129, 0.08) 0, transparent 50%);
            background-attachment: fixed;
            font-family: 'Noto Sans KR', 'Outfit', sans-serif;
            color: var(--text-main);
            line-height: 1.7;
            padding: 40px 20px;
        }}

        .container {{
            max-width: 1000px;
            margin: 0 auto;
        }}

        /* 네비게이션 가이드 */
        .nav-back {{
            margin-bottom: 20px;
        }}
        
        .nav-back a {{
            color: var(--primary);
            text-decoration: none;
            font-size: 0.9rem;
            font-weight: 500;
            transition: color 0.2s ease;
        }}
        
        .nav-back a:hover {{
            color: #60a5fa;
            text-decoration: underline;
        }}

        /* 메인 리포트 카드 */
        .report-card {{
            background: var(--card-bg);
            border: 1px solid var(--card-border);
            border-radius: 16px;
            padding: 45px;
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            box-shadow: 0 10px 40px -15px rgba(0, 0, 0, 0.6);
        }}

        /* 타이틀 스타일 */
        header {{
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
            padding-bottom: 24px;
            margin-bottom: 30px;
        }}

        header h1 {{
            font-size: 2.2rem;
            font-weight: 800;
            background: linear-gradient(to right, #ffffff, #93c5fd);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 12px;
            line-height: 1.3;
        }}

        .meta-tag {{
            display: inline-block;
            background: rgba(59, 130, 246, 0.12);
            border: 1px solid rgba(59, 130, 246, 0.3);
            color: #93c5fd;
            padding: 4px 12px;
            border-radius: 12px;
            font-size: 0.8rem;
            font-weight: 500;
        }}

        /* 마크다운 요소별 렌더링 스타일링 */
        h2 {{
            font-size: 1.5rem;
            color: #93c5fd;
            margin-top: 35px;
            margin-bottom: 18px;
            border-left: 4px solid var(--primary);
            padding-left: 14px;
        }}

        h3 {{
            font-size: 1.2rem;
            color: #a7f3d0;
            margin-top: 25px;
            margin-bottom: 12px;
            padding-left: 4px;
        }}

        p {{
            margin-bottom: 18px;
            color: #e5e7eb;
            font-size: 0.98rem;
        }}

        /* 목록 스타일링 (순서 없는 리스트) */
        ul {{
            margin-bottom: 20px;
            padding-left: 10px;
        }}

        li {{
            margin-bottom: 10px;
            position: relative;
            padding-left: 22px;
            color: #d1d5db;
        }}

        li::before {{
            content: "✓";
            position: absolute;
            left: 0;
            color: var(--success);
            font-weight: bold;
        }}

        /* 마크다운 표(Table) 스타일링 */
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 25px 0;
            font-size: 0.92rem;
            border-radius: 8px;
            overflow: hidden;
        }}

        th {{
            background: rgba(30, 41, 59, 0.6);
            padding: 12px 14px;
            font-weight: 600;
            color: #93c5fd;
            border-bottom: 2px solid var(--card-border);
        }}

        td {{
            padding: 10px 14px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.05);
            color: #e5e7eb;
        }}

        tr:hover td {{
            background: rgba(255, 255, 255, 0.02);
        }}

        /* 인용구(Blockquote) 스타일링 */
        blockquote {{
            border-left: 4px solid var(--primary);
            background: rgba(59, 130, 246, 0.05);
            padding: 16px 20px;
            margin: 20px 0;
            border-radius: 0 8px 8px 0;
        }}
        
        blockquote p {{
            margin-bottom: 0;
            color: #93c5fd;
            font-weight: 500;
        }}

        /* 수평선 스타일 */
        hr {{
            border: 0;
            height: 1px;
            background: rgba(255, 255, 255, 0.08);
            margin: 30px 0;
        }}

        /* Mermaid 코드블럭 또는 일반 이미지 렌더링 스타일 */
        img {{
            max-width: 100%;
            height: auto;
            border-radius: 10px;
            border: 1px solid rgba(255, 255, 255, 0.06);
            margin: 20px 0;
        }}

        /* 꼬리말 */
        footer {{
            text-align: center;
            margin-top: 50px;
            color: var(--text-muted);
            font-size: 0.8rem;
            border-top: 1px solid rgba(255, 255, 255, 0.05);
            padding-top: 25px;
        }}
    </style>
</head>
<body>

<div class="container">
    <div class="nav-back">
        <a href="../../README.html">← 메인 README 메인 화면으로 돌아가기</a>
    </div>

    <div class="report-card">
        <header>
            <span class="meta-tag">공동 사업 기획 기획 검토서</span>
            <h1>{header_title}</h1>
        </header>

        <main>
            {body_content}
        </main>
    </div>

    <footer>
        <p>© 2026 AKAMAI & NVIDIA & MZC HYBRID PROJECT COOPERATIVE GROUP.</p>
    </footer>
</div>

</body>
</html>
"""

def convert_md_to_html(md_path, html_path):
    print(f"변환 중: {md_path} -> {html_path}")
    
    with open(md_path, 'r', encoding='utf-8') as f:
        md_text = f.read()

    # 1. 1행의 대제목(# 제목)을 읽어 타이틀로 파싱
    header_title = "AKAMAI & NVIDIA & MZC 기획안"
    title_match = re.search(r'^#\s+(.+)$', md_text, re.MULTILINE)
    if title_match:
        header_title = title_match.group(1).strip()
        # 원본 마크다운 문서 파싱 시 헤더 타이틀이 2중 출력되지 않도록 # 제목 행을 제거
        md_text = md_text.replace(title_match.group(0), "", 1)

    # 2. 마크다운 라이브러리를 이용하여 HTML 바디 파싱
    # 표(Tables)와 펜스 코드블록(Fenced Code) 등 확장 기능(Extensions) 활성화
    extensions = ['tables', 'fenced_code', 'nl2br']
    body_content = markdown.markdown(md_text, extensions=extensions)

    # 3. HTML 템플릿에 데이터 주입
    final_html = HTML_TEMPLATE.format(
        title=header_title,
        header_title=header_title,
        body_content=body_content
    )

    # 4. 결과 파일 쓰기
    dir_name = os.path.dirname(html_path)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(final_html)
    
    print(f"완료: {html_path} 생성")

def main():
    # 변환 대상 마크다운 파일과 출력될 HTML 파일 맵
    # financial_simulation_report.md는 커스텀 대시보드 보존을 위해 단순 자동 변환에서 예외(Skip) 처리
    conversion_targets = {
        'README.md': 'README.html',
        'handover.md': 'handover.html',
        'docs/research/akamai_nvidia_partnership.md': 'docs/research/akamai_nvidia_partnership.html',
        'docs/research/nvidia_ncp_market_analysis.md': 'docs/research/nvidia_ncp_market_analysis.html',
        'docs/proposal/mzc_akamai_partnership.md': 'docs/proposal/mzc_akamai_partnership.html'
    }

    for md, html in conversion_targets.items():
        if os.path.exists(md):
            convert_md_to_html(md, html)
        else:
            print(f"경고: {md} 파일을 찾을 수 없어 변환을 생략합니다.")

    print("\n[성공] 지정된 모든 마크다운 파일들의 HTML 변환이 성공적으로 끝났습니다.")
    
    # HTML to DOCX 자동 연동
    try:
        import sys
        current_dir = os.path.dirname(os.path.abspath(__file__))
        if current_dir not in sys.path:
            sys.path.append(current_dir)
        from convert_html_to_docx import main as convert_to_docx
        print("\n[DOCX 동기화] HTML 문서를 Word(DOCX) 형식으로 일괄 동기화합니다...")
        convert_to_docx()
    except Exception as e:
        print(f"[DOCX 동기화 경고] DOCX 변환 진행 중 오류 발생: {e}")

if __name__ == '__main__':
    main()

