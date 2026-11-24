# -*- coding: utf-8 -*-
"""Performance Flow 사전 목표 합의서 및 주간 보고 DOCX 생성 스크립트 (정량 수치 배제 및 간소화 버전)."""

from pathlib import Path
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn


FONT_NAME = "맑은 고딕"
HEADER_DARK_BG = "595959"
SUBHEADER_GRAY_BG = "E6E6E6"
BORDER_COLOR = "404040"


def set_cell_shading(cell, fill_hex: str) -> None:
    """셀 배경색을 설정한다."""
    shading = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shading)


def set_cell_margins(cell, top=110, bottom=110, left=140, right=140) -> None:
    """셀 내부 여백(dxa)을 설정한다."""
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement("w:tcMar")
    for side, val in [("top", top), ("bottom", bottom), ("left", left), ("right", right)]:
        node = OxmlElement(f"w:{side}")
        node.set(qn("w:w"), str(val))
        node.set(qn("w:type"), "dxa")
        tcMar.append(node)
    tcPr.append(tcMar)


def set_table_borders(table, color: str = BORDER_COLOR, sz: str = "6") -> None:
    """표 전체 테두리를 설정한다."""
    tblPr = table._tbl.tblPr
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'<w:top w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:bottom w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:left w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:right w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:insideH w:val="single" w:sz="4" w:space="0" w:color="{color}"/>'
        f'<w:insideV w:val="single" w:sz="4" w:space="0" w:color="{color}"/>'
        f"</w:tblBorders>"
    )
    tblPr.append(borders)


def style_run(run, size_pt: float = 9.5, bold: bool = False, color: RGBColor = RGBColor(0x1F, 0x1F, 0x1F)) -> None:
    """한글/영문 폰트 및 스타일을 일관되게 적용한다."""
    run.font.name = FONT_NAME
    run._element.rPr.rFonts.set(qn("w:eastAsia"), FONT_NAME)
    run.font.size = Pt(size_pt)
    run.bold = bold
    run.font.color.rgb = color


def add_cell_lines(cell, lines: list[tuple[str, bool]], size_pt: float = 9.5, color: RGBColor = RGBColor(0x1F, 0x1F, 0x1F)) -> None:
    """셀 내부에 여러 줄의 서식 있는 문단을 추가한다."""
    cell.text = ""
    for idx, (text, is_bold) in enumerate(lines):
        p = cell.paragraphs[0] if idx == 0 else cell.add_paragraph()
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.line_spacing = 1.3
        r = p.add_run(text)
        style_run(r, size_pt=size_pt, bold=is_bold, color=color)


def add_banner_row(table, title: str, col_widths: list[Cm]) -> None:
    """어두운 회색 상단 배너 행을 추가한다."""
    row = table.add_row()
    merged = row.cells[0].merge(row.cells[1])
    set_cell_shading(merged, HEADER_DARK_BG)
    set_cell_margins(merged, top=130, bottom=130, left=160, right=160)
    merged.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
    add_cell_lines(merged, [(title, True)], size_pt=10.0, color=RGBColor(0xFF, 0xFF, 0xFF))
    row.cells[0].width = col_widths[0]
    row.cells[1].width = col_widths[1]


def add_subbanner_row(table, title: str, col_widths: list[Cm]) -> None:
    """연한 회색 섹션 구분 행을 추가한다."""
    row = table.add_row()
    merged = row.cells[0].merge(row.cells[1])
    set_cell_shading(merged, SUBHEADER_GRAY_BG)
    set_cell_margins(merged, top=95, bottom=95, left=160, right=160)
    merged.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
    add_cell_lines(merged, [(title, True)], size_pt=9.5)


def add_kv_row(table, key_lines: list[tuple[str, bool]], val_lines: list[tuple[str, bool]], col_widths: list[Cm], key_bg: str | None = None) -> None:
    """항목(좌측) - 내용(우측) 2열 행을 추가한다."""
    row = table.add_row()
    c0, c1 = row.cells[0], row.cells[1]
    c0.width = col_widths[0]
    c1.width = col_widths[1]
    c0.vertical_alignment = WD_ALIGN_VERTICAL.TOP
    c1.vertical_alignment = WD_ALIGN_VERTICAL.TOP
    set_cell_margins(c0, top=110, bottom=110, left=130, right=130)
    set_cell_margins(c1, top=110, bottom=110, left=150, right=150)
    if key_bg:
        set_cell_shading(c0, key_bg)
    add_cell_lines(c0, key_lines, size_pt=9.5)
    add_cell_lines(c1, val_lines, size_pt=9.5)


def build_document(output_path: Path) -> None:
    """Performance Flow 공식 양식 기반 DOCX 문서를 생성한다."""
    doc = Document()

    # 페이지 여백 설정 (A4)
    for section in doc.sections:
        section.page_width = Cm(21.0)
        section.page_height = Cm(29.7)
        section.top_margin = Cm(2.0)
        section.bottom_margin = Cm(2.0)
        section.left_margin = Cm(1.8)
        section.right_margin = Cm(1.8)

    normal = doc.styles["Normal"]
    normal.font.name = FONT_NAME
    normal._element.rPr.rFonts.set(qn("w:eastAsia"), FONT_NAME)
    normal.font.size = Pt(9.5)

    # 1. 사전 목표 합의서 제목
    title_p = doc.add_paragraph()
    title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    title_p.paragraph_format.space_after = Pt(8)
    tr = title_p.add_run("사전 목표 합의서 (Initial Agreement)")
    style_run(tr, size_pt=13.5, bold=True)

    note_p = doc.add_paragraph()
    note_p.paragraph_format.space_after = Pt(6)
    nr = note_p.add_run("※ 프로그램 착수 시 구성원, FLM, Unit Leader가 상호 확인하고 수립하는 단계입니다.")
    style_run(nr, size_pt=9.0, color=RGBColor(0x33, 0x33, 0x33))

    col_widths = [Cm(4.0), Cm(13.4)]

    t1 = doc.add_table(rows=0, cols=2)
    t1.alignment = WD_TABLE_ALIGNMENT.CENTER
    t1.autofit = False
    set_table_borders(t1)

    # 원본 PDF와 동일한 배너 및 헤더 구조
    add_banner_row(t1, "사전 목표 수립 (기간: 2026. 11. 24 ~ 2027. 02. 21)", col_widths)
    add_kv_row(t1, [("항목", True)], [("내용", True)], col_widths, key_bg=SUBHEADER_GRAY_BG)
    set_cell_shading(t1.rows[-1].cells[1], SUBHEADER_GRAY_BG)

    add_kv_row(
        t1,
        [("현재 역량 Gap", True), ("(개선점)", True)],
        [
            ("• 조직 및 직무 전환에 따른 역할 재정립(Re-boarding) 및 기대수준 정렬", True),
            ("  - 상반기 평가 기준 시점의 소속 조직(하드웨어 총판사업)과 현재 소속 조직(ISV BU) 간 사업 구조 및 수행 직무가 상이함에 따라, ISV BU의 직무 기대수준(솔루션·하이브리드 AI 기반 기술 제안, 프리세일즈 및 사업개발 기술 지원)에 맞춘 역할 정의와 업무 프로세스 안착이 필요함.", False),
            ("• 병렬 기술 지원 과제의 우선순위 조율 및 진행 가시성 제고", True),
            ("  - 다수의 대내외 RFI/RFP 대응 및 영업·BD 기술 지원 업무를 병행하는 과정에서, 리더십과의 사전 우선순위 합의 및 주간 단위 진행 경과 공유 체계를 정립할 필요가 있음.", False),
        ],
        col_widths,
    )

    add_kv_row(
        t1,
        [("정량적 목표 및", True), ("수치화된 개선", True), ("지표", True)],
        [
            ("※ 조직 전환에 따른 신규 직무 안착 단계임을 고려하여, 경직된 수치 대신 핵심 업무 영역별 수행 기준 및 산출물 확인 방식으로 운영함.", False),
            ("", False),
            ("1. 주요 전략 사업 RFI·RFP 제안 대응 및 Tech 아키텍처 수행", True),
            ("  - 목표 내용: 진행 중이거나 신규 추진되는 주요 과제(현대자동차 GPU RFI/RFP, 원익로보틱스, KG ICT BOM 프로젝트, 대구 AIDC 등)에 대한 제안 총괄 지원, 기술 아키텍처 설계 및 산출물 정합성 검토 수행", False),
            ("  - 달성 기준 및 확인 자료: 대내외 추진 일정에 맞춘 단계별 제안·기술 검토 문서 작성 여부 및 공유폴더(Google Drive/워크스페이스) 내 산출물 이력", False),
            ("", False),
            ("2. ISV BU 프리세일즈, 영업지원 및 BD 기술 협업", True),
            ("  - 목표 내용: AI Full Stack 관련 오퍼링·아키텍처 정리 및 영업·BD 부서와 연계한 고객 기술 미팅, 프리세일즈 기술 검토, 파트너·벤더 기술 협의 지원", False),
            ("  - 달성 기준 및 확인 자료: 주간 단위로 수행한 프리세일즈·영업/BD 기술 지원 자료, 아키텍처 문서 또는 관련 미팅·협업 기록", False),
        ],
        col_widths,
    )

    add_kv_row(
        t1,
        [("정성적/질적", True), ("전진 목표", True), ("업무 태도 및", True), ("품질 개선", True)],
        [
            ("• 선제적 우선순위 협의 및 이슈 공유: 병렬 과제 수행 중 일정이나 범위 조율이 필요한 사항을 Unit Leader와 사전에 공유·협의하여 원활한 협업 체계를 유지함.", False),
            ("• 고객·사업 관점의 산출물 완성도 제고: 단순 기술 사양 정리를 넘어 사업 구도 및 유관 부서(영업·전략·파트너) 의견을 종합 반영한 제안·기술 산출물 품질을 확보함.", False),
            ("", False),
            ("• [월별 실행 방향]", True),
            ("  - 1개월 차: ISV BU 내 당면 RFI/제안 과제 집중 대응 및 주간 업무 공유·점검 체계 안착", False),
            ("  - 2개월 차: 후속 RFP·제안 대응 및 AI Full Stack 기반 프리세일즈·영업/BD 기술 지원 수행", False),
            ("  - 3개월 차: 진행 과제별 주요 산출물·기술 자산 정리 및 ISV BU 내 기술 지원 역할 안정화", False),
        ],
        col_widths,
    )

    add_kv_row(
        t1,
        [("FLM 지원 계획", True)],
        [
            ("• 주 1회 정기 면담을 통한 ISV BU 내 담당 과제의 우선순위 조정 및 업무 범위 가이드 제공", False),
            ("• 주요 RFI/RFP 및 대외 제안 진행 시 유관 부서 협업 조율 및 의사결정 이슈 해소 지원", False),
            ("• 주요 산출물에 대한 방향성 피드백 및 신규 조직 직무 안착 코칭 제공", False),
        ],
        col_widths,
    )

    add_subbanner_row(t1, "피드백 면담", col_widths)
    add_kv_row(
        t1,
        [("면담 날짜", True)],
        [("실제 면담일: 2026. 11. __   /   합의일: 2026. 11. __", False)],
        col_widths,
    )
    add_kv_row(
        t1,
        [("피드백 내용", True)],
        [("", False), ("", False), ("", False)],
        col_widths,
    )
    add_kv_row(
        t1,
        [("구성원", True), ("체크사항", True)],
        [("● 회사가 부여한 목표 및 지원 계획을 확인하고 성과 개선에 성실히 임할 것을 확인하였습니다.", False)],
        col_widths,
    )
    add_kv_row(
        t1,
        [("작성자", True), ("체크사항", True), ("(Unit Leader)", True)],
        [("● 구성원의 목표 달성을 위해 구성원의 지원 계획에 성실히 임할 것을 확인하였습니다.", False)],
        col_widths,
    )

    # 페이지 나누기: 주간 보고 양식 (매주 간편하게 재사용 가능하도록 구성)
    doc.add_page_break()

    w_title = doc.add_paragraph()
    w_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    w_title.paragraph_format.space_after = Pt(8)
    wr = w_title.add_run("주 단위 보고 및 평가 (Weekly Report)")
    style_run(wr, size_pt=13.5, bold=True)

    w_note = doc.add_paragraph()
    w_note.paragraph_format.space_after = Pt(6)
    wnr = w_note.add_run("※ 주 단위 관리 대상자용 - 매주 면담 전 구성원이 셀프 작성하고, 리더가 피드백을 기록합니다.")
    style_run(wnr, size_pt=9.0, color=RGBColor(0x33, 0x33, 0x33))

    t2 = doc.add_table(rows=0, cols=2)
    t2.alignment = WD_TABLE_ALIGNMENT.CENTER
    t2.autofit = False
    set_table_borders(t2)

    add_banner_row(t2, "1주차 주간 보고 (기간: 2026. 11. 24 ~ 2026. 11. 27)", col_widths)
    add_subbanner_row(t2, "[구성원 Self-작성] 실행 결과 및 자가 평가", col_widths)

    add_kv_row(
        t2,
        [("이번 주 과제", True), ("및 목표치", True)],
        [
            ("• Performance Flow 사전 목표 수립 및 Unit Leader 면담·합의 진행", False),
            ("• 현대자동차 GPU RFI 대응 관련 제안 표준 템플릿 정리 및 제출 자료 기술 정합성 검토·지원", False),
            ("• 진행 중인 주요 제안·프리세일즈 과제(원익로보틱스, KG ICT BOM, 대구 AIDC, AI Full Stack 등) 현황 점검", False),
        ],
        col_widths,
    )

    add_kv_row(
        t2,
        [("달성 산출물", True), ("(증빙 필수)", True)],
        [
            ("- 사전 목표 합의서 작성 및 제출본", False),
            ("- 현대자동차 GPU RFI 관련 검토 문서 및 업무 공유폴더 링크: [Google Drive Docs URL]", False),
        ],
        col_widths,
    )

    add_kv_row(
        t2,
        [("질적 개선점", True)],
        [
            ("- 유관 파트 간 산출물 포맷과 정합성을 사전 점검하여 제안 문서의 일관성을 확보함.", False),
            ("- 차주 후속 RFI/제안 일정 관련 유관 부서 협업 및 우선순위 지속 조율 예정.", False),
        ],
        col_widths,
    )

    add_subbanner_row(t2, "[Unit Leader (FLM) 작성] 객관적 평가 및 지원 내역", col_widths)

    add_kv_row(
        t2,
        [("주 단위 종합", True), ("결과", True)],
        [
            ("● 기대수준을 크게 상회함 - 기존의 기대를 뛰어넘어 조직 전체에 매우 혁신적이고 파급력이 큰 영향(Impact)을 미침", False),
            ("● 기대수준을 상회함 - 할당된 목표를 뛰어넘는 우수한 성과를 내고 높은 영향력을 발휘함", False),
            ("● 기대수준을 충족함 - 자신에게 부여된 역할과 목표에 맞는 기대 수준을 충실히 달성함", False),
            ("● 기대수준을 일부 미달함 - 기대에 미치지 못하는 부분이 일부 있어 추가적인 성장과 개선이 필요함", False),
            ("● 기대수준을 크게 미달함 - 전반적으로 기대 수준에 크게 미치지 못하여 긴급한 성능 개선 조치가 필요함", False),
        ],
        col_widths,
    )

    add_kv_row(t2, [("달성 여부 및", True), ("피드백", True)], [("", False), ("", False)], col_widths)
    add_kv_row(t2, [("지도 및 조치", True), ("내역", True)], [("", False), ("", False)], col_widths)

    add_subbanner_row(t2, "피드백 면담", col_widths)
    add_kv_row(t2, [("면담 날짜", True)], [("2026. 11. __", False)], col_widths)
    add_kv_row(t2, [("피드백 내용", True)], [("", False), ("", False)], col_widths)
    add_kv_row(
        t2,
        [("구성원", True), ("체크사항", True)],
        [("● 이번 주 실행 결과에 대한 피드백을 숙지하였으며, 이를 바탕으로 향후 목표 달성에 성실히 임할 것을 확인합니다.", False)],
        col_widths,
    )
    add_kv_row(
        t2,
        [("작성자", True), ("체크사항", True), ("(Unit Leader)", True)],
        [("● 구성원의 목표 달성을 돕기 위해 필요한 코칭과 지원 계획에 성실히 임할 것을 확인합니다.", False)],
        col_widths,
    )

    doc.save(str(output_path))


if __name__ == "__main__":
    out = Path(r"c:\dev\antigravity-workspace\pflow\Performance_Flow_김성호_사전목표합의서_및_1주차보고.docx")
    build_document(out)
    print(f"재생성 완료: {out}")
