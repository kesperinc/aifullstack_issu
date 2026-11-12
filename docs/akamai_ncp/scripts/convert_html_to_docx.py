import os
import re
import glob
from bs4 import BeautifulSoup, NavigableString
from docx import Document
from docx.shared import Pt, RGBColor
from docx.oxml.ns import qn

try:
    from htmldocx import HtmlToDocx
except ImportError:
    HtmlToDocx = None


def _clean_mermaid_label(text):
    """Mermaid 라벨 내부의 HTML 태그(<br/>, <b> 등)를 깔끔한 HTML 조각으로 정규화합니다."""
    if not text:
        return ""
    s = text.strip().strip('"').strip("'")
    # 대소문자 무관하게 <br>, <br/>, <br />를 표준 <br/>로 통일
    s = re.sub(r'<\s*br\s*/?\s*>', '<br/>', s, flags=re.IGNORECASE)
    # <b>, </b>를 <strong>, </strong>으로 변환
    s = re.sub(r'<\s*b\s*>', '<strong>', s, flags=re.IGNORECASE)
    s = re.sub(r'<\s*/\s*b\s*>', '</strong>', s, flags=re.IGNORECASE)
    return s


def _strip_tags_to_plain(text):
    """문자열 내의 <br/>, <b> 등 모든 HTML 태그를 공백 또는 줄바꿈으로 제거합니다."""
    if not text:
        return ""
    s = re.sub(r'<\s*br\s*/?\s*>', ' ', text, flags=re.IGNORECASE)
    s = re.sub(r'<[^>]+>', '', s)
    return re.sub(r'\s+', ' ', s).strip()


def _mermaid_to_html_table(raw_mermaid):
    """
    Mermaid 코드 블록(flowchart, sequenceDiagram 등)을 파싱하여
    Word(.docx) 문서에서 깨지지 않고 가독성 높게 표시되는 HTML <table> 구조로 변환합니다.
    """
    lines = [line.strip() for line in raw_mermaid.splitlines() if line.strip()]
    if not lines:
        return ""

    first_line = lines[0]

    # 1. 시퀀스 다이어그램(sequenceDiagram) 처리
    if first_line.startswith("sequenceDiagram"):
        participants = {}
        rows_html = []

        for line in lines[1:]:
            if line == "autonumber":
                continue

            # participant / actor 정의 파싱
            m_part = re.match(r'^(?:participant|actor)\s+([A-Za-z0-9_]+)\s+as\s+(.+)$', line)
            if m_part:
                pid, plabel = m_part.group(1), _strip_tags_to_plain(m_part.group(2))
                participants[pid] = plabel
                continue

            # Note over 구문 파싱
            m_note = re.match(r'^Note\s+over\s+[^:]+:\s*(.+)$', line, flags=re.IGNORECASE)
            if m_note:
                note_text = _strip_tags_to_plain(m_note.group(1))
                rows_html.append(
                    f'<tr><td colspan="2"><strong>{note_text}</strong></td></tr>'
                )
                continue

            # 메시지 화살표(->>, -->>, ->, -->) 파싱
            m_msg = re.match(r'^([A-Za-z0-9_]+)\s*-{1,2}>>?\s*([A-Za-z0-9_]+)\s*:\s*(.+)$', line)
            if m_msg:
                src, dst, msg = m_msg.group(1), m_msg.group(2), _clean_mermaid_label(m_msg.group(3))
                src_name = participants.get(src, src)
                dst_name = participants.get(dst, dst)
                actor_str = f"{src_name}" if src == dst else f"{src_name} → {dst_name}"
                rows_html.append(
                    f'<tr><td><strong>{actor_str}</strong></td><td>{msg}</td></tr>'
                )

        if not rows_html:
            return ""

        return (
            '<p><strong>[다이어그램 요약: 단계별 상호작용 흐름]</strong></p>'
            '<table>'
            '<thead><tr><th>수행 주체 / 흐름</th><th>세부 수행 내용</th></tr></thead>'
            f'<tbody>{"".join(rows_html)}</tbody>'
            '</table>'
        )

    # 2. 플로우차트(flowchart / graph) 처리
    subgraphs = []
    current_sg = None
    standalone_nodes = []
    edge_notes = []

    for line in lines[1:]:
        # subgraph 시작
        m_sg = re.match(r'^subgraph\s+[A-Za-z0-9_]+\s*\[\s*"?(.+?)"?\s*\]$', line)
        if m_sg:
            current_sg = {"title": _strip_tags_to_plain(m_sg.group(1)), "items": []}
            subgraphs.append(current_sg)
            continue

        if line == "end":
            current_sg = None
            continue

        # 라벨이 있는 엣지 (예: A ==>|"설명"| B)
        m_edge_lbl = re.match(r'^([A-Za-z0-9_]+)\s*[=-]+>\|"(.+?)"\|\s*([A-Za-z0-9_]+)$', line)
        if m_edge_lbl:
            edge_text = _strip_tags_to_plain(m_edge_lbl.group(2))
            edge_notes.append(edge_text)
            continue

        # 일반 화살표 연결선(A --> B 등)은 무시
        if re.match(r'^[A-Za-z0-9_]+\s*<?[-=]+>?\s*[A-Za-z0-9_]+$', line):
            continue

        # 노드 정의 (예: NodeID["내용"] 또는 NodeID("내용"))
        m_node = re.match(r'^[A-Za-z0-9_]+\s*[\[\(\{]+"?(.+?)"?[\]\)\}]+$', line)
        if m_node:
            cleaned = _clean_mermaid_label(m_node.group(1))
            if current_sg is not None:
                current_sg["items"].append(cleaned)
            else:
                standalone_nodes.append(cleaned)

    rows_html = []
    for sg in subgraphs:
        body_html = "<br/>".join(sg["items"]) if sg["items"] else "-"
        rows_html.append(
            f'<tr><td><strong>{sg["title"]}</strong></td><td>{body_html}</td></tr>'
        )

    for node_html in standalone_nodes:
        rows_html.append(f'<tr><td><strong>구성 요소</strong></td><td>{node_html}</td></tr>')

    for edge_note in edge_notes:
        rows_html.append(
            f'<tr><td><strong>연계 / 이관 흐름</strong></td><td>{edge_note}</td></tr>'
        )

    if not rows_html:
        return ""

    return (
        '<p><strong>[아키텍처 다이어그램 요약]</strong></p>'
        '<table>'
        '<thead><tr><th>구분 / 영역</th><th>핵심 구성 및 수행 내용</th></tr></thead>'
        f'<tbody>{"".join(rows_html)}</tbody>'
        '</table>'
    )


def preprocess_soup_for_docx(soup):
    """
    HtmlToDocx 변환 전에 BeautifulSoup DOM을 정리하여
    <script>, <style>, Mermaid 코드 블록, 이스케이프된 <br/> 태그 등이
    워드(.docx) 본문에 날것으로 노출되지 않도록 전처리합니다.
    """
    # 1. 불필요한 스크립트, 스타일, 상단 배지(.tag), 하단 푸터(.footer), 각주 역참조 제거
    for tag in soup.find_all(['script', 'style']):
        tag.decompose()
    for badge in soup.find_all('div', class_='tag'):
        badge.decompose()
    for footer in soup.find_all('div', class_='footer'):
        footer.decompose()
    for backref in soup.find_all('a', class_='footnote-backref'):
        backref.decompose()

    # 2. Mermaid 다이어그램(<div class="mermaid">)을 깔끔한 요약 표(<table>)로 변환
    for m_div in soup.find_all('div', class_='mermaid'):
        raw_code = m_div.get_text()
        table_html = _mermaid_to_html_table(raw_code)
        if table_html:
            frag = BeautifulSoup(table_html, 'html.parser')
            m_div.replace_with(frag)
        else:
            m_div.decompose()

    # 3. 텍스트 노드에 남아 있을 수 있는 리터럴 HTML 태그 문자열(<br/>, <b> 등) 정리
    tag_pattern = re.compile(r'<\s*/?\s*(?:br|b|strong|i|em)\s*/?\s*>', flags=re.IGNORECASE)
    for text_node in list(soup.find_all(string=True)):
        val = str(text_node)
        if tag_pattern.search(val):
            # 리터럴 <br> 등을 실제 HTML 태그로 재파싱하여 교체
            normalized = re.sub(r'<\s*br\s*/?\s*>', '<br/>', val, flags=re.IGNORECASE)
            normalized = re.sub(r'<\s*b\s*>', '<strong>', normalized, flags=re.IGNORECASE)
            normalized = re.sub(r'<\s*/\s*b\s*>', '</strong>', normalized, flags=re.IGNORECASE)
            frag = BeautifulSoup(normalized, 'html.parser')
            text_node.replace_with(frag)


def _apply_korean_font(document):
    """문서 기본 한글 글꼴을 맑은 고딕으로 설정합니다."""
    style = document.styles['Normal']
    style.font.name = 'Malgun Gothic'
    style.font.size = Pt(10.5)
    style._element.rPr.rFonts.set(qn('w:eastAsia'), 'Malgun Gothic')


def _add_inline_runs(paragraph, node):
    """인라인 HTML 태그(strong, b, em, code, a, br 등)를 보존하여 문단에 추가합니다."""
    for child in node.children:
        if isinstance(child, NavigableString):
            txt = str(child)
            if txt:
                paragraph.add_run(txt)
        elif child.name == 'br':
            paragraph.add_run('\n')
        elif child.name in ('strong', 'b'):
            r = paragraph.add_run(child.get_text())
            r.bold = True
        elif child.name in ('em', 'i'):
            r = paragraph.add_run(child.get_text())
            r.italic = True
        elif child.name == 'code':
            r = paragraph.add_run(child.get_text())
            r.font.name = 'Consolas'
            r.font.color.rgb = RGBColor(0x1D, 0x4E, 0xD8)
        elif child.name == 'a':
            r = paragraph.add_run(child.get_text())
            r.font.color.rgb = RGBColor(0x1D, 0x4E, 0xD8)
        else:
            _add_inline_runs(paragraph, child)


def _render_list_native(document, list_tag, level=0):
    """순서 있는/없는 목록 및 중첩 목록을 Word 리스트 스타일로 렌더링합니다."""
    style_name = 'List Number' if list_tag.name == 'ol' else 'List Bullet'
    for li in list_tag.find_all('li', recursive=False):
        p = document.add_paragraph(style=style_name)
        if level > 0:
            p.paragraph_format.left_indent = Pt(18 * level)
        for child in li.children:
            if getattr(child, 'name', None) in ('ul', 'ol'):
                continue
            if isinstance(child, NavigableString):
                t = str(child).strip('\n')
                if t.strip():
                    p.add_run(t)
            elif child.name in ('strong', 'b'):
                r = p.add_run(child.get_text())
                r.bold = True
            elif child.name == 'code':
                r = p.add_run(child.get_text())
                r.font.name = 'Consolas'
            elif child.name == 'br':
                p.add_run('\n')
            else:
                p.add_run(child.get_text())
        for sub in li.find_all(['ul', 'ol'], recursive=False):
            _render_list_native(document, sub, level + 1)


def _render_table_native(document, table_tag):
    """HTML <table>을 Table Grid 스타일의 Word 표로 렌더링합니다."""
    rows = table_tag.find_all('tr')
    if not rows:
        return
    max_cols = max((len(r.find_all(['th', 'td'])) for r in rows), default=0)
    if max_cols == 0:
        return
    table = document.add_table(rows=len(rows), cols=max_cols)
    try:
        table.style = 'Table Grid'
    except Exception:
        pass
    for r_idx, row in enumerate(rows):
        cells = row.find_all(['th', 'td'])
        for c_idx, cell in enumerate(cells):
            if c_idx >= max_cols:
                break
            w_cell = table.cell(r_idx, c_idx)
            w_cell.text = ''
            p = w_cell.paragraphs[0]
            for br in cell.find_all('br'):
                br.replace_with('\n')
            run = p.add_run(cell.get_text().strip())
            run.font.size = Pt(9.5)
            if cell.name == 'th' or r_idx == 0:
                run.bold = True


def _render_dom_native(document, root, slide_counter=None):
    """htmldocx 미설치 환경에서도 BeautifulSoup DOM을 재귀 순회하여 고품질 Word 문서를 생성합니다."""
    if slide_counter is None:
        slide_counter = [0]

    for elem in root.children:
        if isinstance(elem, NavigableString):
            continue
        tag = elem.name
        classes = elem.get('class', []) if hasattr(elem, 'get') else []
        if 'control-bar' in classes or 'slide-footer' in classes or 'nav-back' in classes:
            continue

        if tag == 'section' and 'slide' in classes:
            if slide_counter[0] > 0:
                document.add_page_break()
            slide_counter[0] += 1
            _render_dom_native(document, elem, slide_counter)
        elif tag == 'h1':
            document.add_heading(elem.get_text().strip(), level=0)
        elif tag == 'h2':
            document.add_heading(elem.get_text().strip(), level=1)
        elif tag == 'h3':
            document.add_heading(elem.get_text().strip(), level=2)
        elif tag == 'h4':
            document.add_heading(elem.get_text().strip(), level=3)
        elif tag == 'p':
            txt = elem.get_text().strip()
            if txt:
                p = document.add_paragraph()
                _add_inline_runs(p, elem)
        elif tag in ('ul', 'ol'):
            _render_list_native(document, elem, level=0)
        elif tag == 'blockquote':
            txt = elem.get_text().strip()
            if txt:
                p = document.add_paragraph()
                p.paragraph_format.left_indent = Pt(18)
                r = p.add_run(txt)
                r.italic = True
                r.font.color.rgb = RGBColor(0x1E, 0x40, 0xAF)
        elif tag == 'pre':
            txt = elem.get_text()
            if txt.strip():
                p = document.add_paragraph()
                p.paragraph_format.left_indent = Pt(12)
                r = p.add_run(txt)
                r.font.name = 'Consolas'
                r.font.size = Pt(9)
        elif tag == 'table':
            _render_table_native(document, elem)
            document.add_paragraph()
        elif tag in ('div', 'header', 'main', 'section', 'article'):
            # kpi-box 등 단순 텍스트 박스는 한 줄 요약 문단으로 처리하고 나머지는 재귀 탐색
            if 'kpi-box' in classes:
                p = document.add_paragraph(style='List Bullet')
                p.add_run(elem.get_text(' — ', strip=True)).bold = True
            else:
                _render_dom_native(document, elem, slide_counter)


def convert_html_to_docx(html_path, docx_path):
    print(f"변환 시작: {html_path} -> {docx_path}")
    document = Document()
    _apply_korean_font(document)

    # HTML 파일 읽기
    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # BeautifulSoup으로 본문 파싱
    soup = BeautifulSoup(html_content, 'html.parser')

    # report-card, deck-viewport, docContent 메인 영역 탐색
    body_content = (
        soup.find('div', class_='report-card')
        or soup.find('div', class_='deck-viewport')
        or soup.find('main', id='docContent')
        or soup.find('body')
    )

    target_node = body_content if body_content else soup
    preprocess_soup_for_docx(target_node)

    if HtmlToDocx is not None and not soup.find('div', class_='deck-viewport'):
        new_parser = HtmlToDocx()
        new_parser.add_html_to_document(str(target_node), document)
        for table in document.tables:
            try:
                table.style = 'Table Grid'
            except Exception:
                pass
    else:
        _render_dom_native(document, target_node)

    # 문서 저장
    document.save(docx_path)
    print(f"변환 완료: {docx_path}")


def main():
    # 스크립트 파일 기준으로 상위(akamai_ncp) 폴더 절대 경로 찾기
    current_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.abspath(os.path.join(current_dir, '..'))
    # docs 하위 폴더가 따로 있으면 그 안을, 아니면 base_dir 내부 하위 폴더를 탐색
    candidate_docs = os.path.join(base_dir, 'docs')
    search_root = candidate_docs if os.path.isdir(candidate_docs) else base_dir

    # 대상 폴더 내부의 모든 html 파일 탐색
    html_files = glob.glob(os.path.join(search_root, '**', '*.html'), recursive=True)

    if not html_files:
        print("docs 폴더 내에서 HTML 파일을 찾을 수 없습니다.")
        return

    for html_file in html_files:
        docx_file = os.path.splitext(html_file)[0] + '.docx'
        try:
            convert_html_to_docx(html_file, docx_file)
        except Exception as e:
            print(f"{html_file} 변환 중 오류 발생: {e}")


if __name__ == '__main__':
    main()
