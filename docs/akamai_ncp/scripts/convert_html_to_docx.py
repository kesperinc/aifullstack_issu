import os
import re
import glob
from bs4 import BeautifulSoup, NavigableString
from docx import Document
from htmldocx import HtmlToDocx


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


def convert_html_to_docx(html_path, docx_path):
    print(f"변환 시작: {html_path} -> {docx_path}")
    document = Document()
    new_parser = HtmlToDocx()

    # HTML 파일 읽기
    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # BeautifulSoup으로 본문 파싱
    soup = BeautifulSoup(html_content, 'html.parser')

    # report-card 클래스 또는 docContent 메인 영역 내부의 컨텐츠가 메인 본문
    body_content = soup.find('div', class_='report-card')
    if not body_content:
        body_content = soup.find('main', id='docContent')
    if not body_content:
        body_content = soup.find('body')

    if body_content:
        preprocess_soup_for_docx(body_content)
        html_str = str(body_content)
    else:
        preprocess_soup_for_docx(soup)
        html_str = str(soup)

    # docx 문서에 HTML 추가
    new_parser.add_html_to_document(html_str, document)

    # 모든 표(Table)에 깔끔한 격자 테두리 스타일 적용
    for table in document.tables:
        try:
            table.style = 'Table Grid'
        except Exception:
            pass

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
