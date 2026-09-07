"""
Nota.ai 솔루션 종합 분석 및 On-Premises AI Full Stack 전략적 포지셔닝 보고서 생성기 (DOCX)
- 두괄식 보고서 구조 (Executive-First Structure):
  * 서론: MZC AI Full Stack 4대 레이어 구성 및 On-Prem 구축 시 치명적 'Missing Link' 정의
  * 제 1 장: 서론 - AI Full Stack 개요 및 On-Prem 구축의 Missing Link
  * 제 2 장: [핵심 제언 1] On-Premises AI Full Stack 구축 시 6대 압도적 강점 (구 Ch 5)
  * 제 3 장: [핵심 제언 2] MZC On-Prem AI Full Stack x Nota 4대 턴키 솔루션 패키지 (구 Ch 6)
            (파트 A. 서버 인프라 중심 주력 오퍼링 2종 ➔ 파트 B. Physical/Edge AI 시장 탐색형 2종)
  * 제 4 장: 비즈니스 협력 모델, 온프레미스 라이선스 및 3단계 실행 로드맵 & 최종 포지셔닝 선언
  * [부록/참조 1]: Nota.ai 기업 개요 및 글로벌 사업 위상 (15B 스타게이트, 글로벌 거점)
  * [부록/참조 2]: NetsPresso 차세대 MoE 최적화 상세 기술 원리 및 벤치마크 데이터 시트
  * [부록/참조 3]: On-Device / Multimodal & 엣지/임베디드 실측 데이터 (VLM, VLA, ASR, 국산 NPU)
  * [부록/참조 4]: 독자 버티컬 솔루션 Nota ITS 상세 분석 (대전 200개소, 두바이 RTA, V2X)
  * [부록/참조 5]: 참고 문헌 및 공식 전달 기술 자료 출처
"""

import os
from pathlib import Path
from docx import Document
from docx.shared import Pt, RGBColor, Inches, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_PARAGRAPH_ALIGNMENT
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

FONT_MAIN = "Malgun Gothic"
FONT_TITLE = "Malgun Gothic"

COLOR_MZC_BLUE = RGBColor(0x00, 0xAB, 0xF0)
COLOR_NAVY_DARK = RGBColor(0x0F, 0x17, 0x2A)
COLOR_TEXT_MAIN = RGBColor(0x22, 0x22, 0x22)
COLOR_TEXT_MUTED = RGBColor(0x55, 0x55, 0x55)
COLOR_GOLD = RGBColor(0xD4, 0xAF, 0x37)
COLOR_NVIDIA_GREEN = RGBColor(0x76, 0xB9, 0x00)
COLOR_PURPLE = RGBColor(0x9D, 0x4E, 0xDD)
COLOR_CRIMSON = RGBColor(0xC9, 0x2A, 0x2A)
COLOR_WHITE = RGBColor(0xFF, 0xFF, 0xFF)

HEX_BG_DARK_NAVY = "0F172A"
HEX_BG_LIGHT_GRAY = "F8FAFC"
HEX_BG_HIGHLIGHT = "EFF6FF"
HEX_BORDER = "CBD5E1"


def set_cell_margins(cell, top=120, bottom=120, left=140, right=140):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)


def set_cell_shading(cell, color_hex):
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shading_elm)


def set_table_borders(table, color="CBD5E1", sz="4", val="single"):
    tblPr = table._tbl.tblPr
    borders_xml = f'''
    <w:tblBorders {nsdecls("w")}>
        <w:top w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>
        <w:left w:val="none"/>
        <w:bottom w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>
        <w:right w:val="none"/>
        <w:insideH w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>
        <w:insideV w:val="none"/>
    </w:tblBorders>
    '''
    tblPr.append(parse_xml(borders_xml))


def add_section_header(doc, sec_num, title_text, subtitle_text=None, is_appendix=False):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(22)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.keep_with_next = True
    
    prefix_color = COLOR_GOLD if is_appendix else COLOR_PURPLE
    r_num = p.add_run(f"[{sec_num}] ")
    r_num.font.name = FONT_TITLE
    r_num.font.size = Pt(13.5)
    r_num.bold = True
    r_num.font.color.rgb = prefix_color

    r_title = p.add_run(title_text)
    r_title.font.name = FONT_TITLE
    r_title.font.size = Pt(13.5)
    r_title.bold = True
    r_title.font.color.rgb = COLOR_NAVY_DARK

    if subtitle_text:
        p_sub = doc.add_paragraph()
        p_sub.paragraph_format.space_before = Pt(0)
        p_sub.paragraph_format.space_after = Pt(8)
        p_sub.paragraph_format.keep_with_next = True
        r_sub = p_sub.add_run(subtitle_text)
        r_sub.font.name = FONT_MAIN
        r_sub.font.size = Pt(9.5)
        r_sub.font.color.rgb = COLOR_TEXT_MUTED
        r_sub.italic = True


def add_sub_header(doc, title_text, level=2):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(title_text)
    r.font.name = FONT_TITLE
    r.font.size = Pt(11 if level == 2 else 10)
    r.bold = True
    r.font.color.rgb = COLOR_NAVY_DARK


def add_body_p(doc, text, bold_prefix="", space_after=4):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = 1.25
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.font.name = FONT_MAIN
        r_pre.font.size = Pt(9.5)
        r_pre.bold = True
        r_pre.font.color.rgb = COLOR_NAVY_DARK
    r_text = p.add_run(text)
    r_text.font.name = FONT_MAIN
    r_text.font.size = Pt(9.5)
    r_text.font.color.rgb = COLOR_TEXT_MAIN
    return p


def add_bullet_p(doc, bold_title, text):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.space_before = Pt(1)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.line_spacing = 1.2
    
    r_b = p.add_run(bold_title)
    r_b.font.name = FONT_MAIN
    r_b.font.size = Pt(9.5)
    r_b.bold = True
    r_b.font.color.rgb = COLOR_NAVY_DARK
    
    r_t = p.add_run(text)
    r_t.font.name = FONT_MAIN
    r_t.font.size = Pt(9.5)
    r_t.font.color.rgb = COLOR_TEXT_MAIN
    return p


def add_callout_box(doc, title, text, border_color_hex="00ABF0", bg_color_hex="F0F9FF"):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    
    cell = tbl.cell(0, 0)
    cell.width = Cm(16.5)
    set_cell_margins(cell, top=130, bottom=130, left=160, right=150)
    set_cell_shading(cell, bg_color_hex)
    
    tblPr = tbl._tbl.tblPr
    borders_xml = f'''
    <w:tblBorders {nsdecls("w")}>
        <w:top w:val="none"/>
        <w:left w:val="single" w:sz="24" w:space="0" w:color="{border_color_hex}"/>
        <w:bottom w:val="none"/>
        <w:right w:val="none"/>
    </w:tblBorders>
    '''
    tblPr.append(parse_xml(borders_xml))
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(3)
    r_title = p.add_run(title)
    r_title.font.name = FONT_TITLE
    r_title.font.size = Pt(9.5)
    r_title.bold = True
    r_title.font.color.rgb = COLOR_NAVY_DARK
    
    p2 = cell.add_paragraph()
    p2.paragraph_format.space_before = Pt(0)
    p2.paragraph_format.space_after = Pt(0)
    p2.paragraph_format.line_spacing = 1.2
    r_text = p2.add_run(text)
    r_text.font.name = FONT_MAIN
    r_text.font.size = Pt(9.0)
    r_text.font.color.rgb = COLOR_TEXT_MAIN
    
    p_after = doc.add_paragraph()
    p_after.paragraph_format.space_before = Pt(0)
    p_after.paragraph_format.space_after = Pt(4)


def create_document():
    doc = Document()
    
    for section in doc.sections:
        section.top_margin = Cm(2.4)
        section.bottom_margin = Cm(2.4)
        section.left_margin = Cm(2.2)
        section.right_margin = Cm(2.2)
        section.page_width = Cm(21.0)
        section.page_height = Cm(29.7)
    
    # -------------------------------------------------------------
    # 1. 표지 / 헤더 영역 (두괄식 보고서 표준)
    # -------------------------------------------------------------
    p_meta = doc.add_paragraph()
    p_meta.paragraph_format.space_before = Pt(0)
    p_meta.paragraph_format.space_after = Pt(4)
    r_tag = p_meta.add_run("MZC AI FULL STACK EXECUTIVE STRATEGY REPORT | CONFIDENTIAL")
    r_tag.font.name = FONT_TITLE
    r_tag.font.size = Pt(8.5)
    r_tag.bold = True
    r_tag.font.color.rgb = COLOR_MZC_BLUE
    
    p_title = doc.add_paragraph()
    p_title.paragraph_format.space_before = Pt(4)
    p_title.paragraph_format.space_after = Pt(6)
    r_title = p_title.add_run("Nota.ai 솔루션 종합 분석 및\nOn-Premises AI Full Stack 전략적 포지셔닝 보고서")
    r_title.font.name = FONT_TITLE
    r_title.font.size = Pt(19)
    r_title.bold = True
    r_title.font.color.rgb = COLOR_NAVY_DARK
    
    p_sub = doc.add_paragraph()
    p_sub.paragraph_format.space_before = Pt(0)
    p_sub.paragraph_format.space_after = Pt(12)
    r_sub = p_sub.add_run("두괄식 경영 보고서: AI Full Stack 레이어 구성, 온프레미스 구축을 위한 Missing Link,\nGPU Capex 75% 절감 강점 및 서버 주력 턴키 패키지 중심 제언")
    r_sub.font.name = FONT_MAIN
    r_sub.font.size = Pt(10.5)
    r_sub.font.color.rgb = COLOR_TEXT_MUTED
    
    # 메타 정보 테이블
    tbl_meta = doc.add_table(rows=2, cols=4)
    tbl_meta.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tbl_meta, color="E2E8F0", sz="4")
    col_widths = [Cm(3.0), Cm(5.25), Cm(3.0), Cm(5.25)]
    
    meta_data = [
        [("문서 번호", True), ("SPEC-20260907-NOTA-ONPREM-01", False), ("작성 일자", True), ("2026-09-07", False)],
        [("보고 형식", True), ("두괄식 경영전략 보고서 (Executive-First)", False), ("분석 대상", True), ("Nota.ai 공식 기술 및 사업 자료 5종", False)]
    ]
    
    for r_idx, row in enumerate(tbl_meta.rows):
        for c_idx, cell in enumerate(row.cells):
            cell.width = col_widths[c_idx]
            set_cell_margins(cell, top=70, bottom=70, left=90, right=90)
            label, is_head = meta_data[r_idx][c_idx]
            if is_head:
                set_cell_shading(cell, "F1F5F9")
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            r = p.add_run(label)
            r.font.name = FONT_MAIN
            r.font.size = Pt(8.5)
            if is_head:
                r.bold = True
                r.font.color.rgb = COLOR_NAVY_DARK
            else:
                r.font.color.rgb = COLOR_TEXT_MAIN
    
    doc.add_paragraph().paragraph_format.space_after = Pt(8)
    
    # 두괄식 Executive Summary
    add_callout_box(
        doc,
        "EXECUTIVE SUMMARY: ON-PREM AI FULL STACK의 'MISSING LINK'를 완결하는 NOTA.AI",
        "현재 메가존클라우드가 정의한 'MZC AI Full Stack'은 인프라(L1)-플랫폼(L2)-서빙/최적화(L3)-비즈니스앱(L4)의 유기적 구조를 완비하였으나, "
        "이를 실제 고객의 사내 전산실(On-Premises)에 완결형으로 구축하려 할 때 ① 막대한 GPU 서버 도입 비용(Capex 5~6억), ② 전산실 랙 전력 한계(10kW 초과), "
        "③ 100% 폐쇄망 소버린 보안, ④ 국산 NPU 조기 상용화 컴파일러 부재라는 치명적인 'Missing Link(결손 고리)'에 직면합니다. "
        "Nota.ai(NetsPresso)는 2,500억 매개변수 초대형 MoE 모델을 H100 8장에서 단 2장으로 서빙(GPU 비용 75% 절감, 지능 손실 단 -0.40%)하여 "
        "이 Missing Link를 단번에 해결하는 MZC On-Prem AI Full Stack의 핵심 엔진입니다. "
        "본 보고서는 MZC의 핵심 역량인 [서버 AI 인프라 오퍼링 2종]을 최우선 주력으로 제안하고, Embedded/Edge/Physical AI는 [전략적 시장 탐색 2종]으로 구분하여 제시합니다. "
        "(상세 기술 원리 및 원천 데이터는 부록 및 참고자료 참조)",
        border_color_hex="00ABF0",
        bg_color_hex="EFF6FF"
    )

    # -------------------------------------------------------------
    # 본문 제 1 장. MZC AI Full Stack 레이어 구성 및 On-Prem 구축의 Missing Link
    # -------------------------------------------------------------
    add_section_header(doc, "제 1 장", "MZC AI Full Stack 구성 및 On-Prem 구축의 Missing Link", 
                       "현재 정리된 4대 표준 레이어 및 온프레미스 실도입 시 직면하는 4대 결손 고리 분석")
    
    add_body_p(doc, "메가존클라우드는 하드웨어부터 최상위 애플리케이션까지 엔터프라이즈 AI의 모든 여정을 턴키로 제공하는 'MZC AI Full Stack'을 구축하여 시장을 선도하고 있습니다.")
    
    add_sub_header(doc, "1. MZC AI Full Stack 표준 4대 레이어 구조")
    add_bullet_p(doc, "Layer 01. 하드웨어 인프라 (Computing & Hardware): ", "Dell PowerEdge(R760 등), Cisco 네트워킹, NVIDIA GPU(H100/L40S) 및 국산 AI 반도체(NPU) 물리 서버 인프라.")
    add_bullet_p(doc, "Layer 02. 온프레미스 플랫폼 및 오케스트레이션 (Platform & MLOps): ", "Red Hat OpenShift AI(RHOAI), Nutanix AHV/Kubernetes 기반의 컨테이너 가상화 및 클러스터 관리 환경.")
    add_bullet_p(doc, "Layer 03. 모델 최적화 및 고속 추론 서빙 (Model Optimization & Serving): ", "vLLM, Triton, KServe 등 고속 토큰 생성 엔진 및 모델 경량화/양자화 파이프라인.")
    add_bullet_p(doc, "Layer 04. 비즈니스 AI 애플리케이션 및 버티컬 (AI Apps & Solutions): ", "사내 기밀 문서 RAG, 프라이빗 코딩 에이전트, 산업별 특화 관제 및 분석 애플리케이션.")

    add_sub_header(doc, "2. On-Premises 실구축 시 직면하는 4대 Missing Link (결손 고리)")
    add_body_p(doc, "설계된 AI Full Stack 아키텍처를 실제 고객 전산실(On-Premises)에 납품하려 할 때, 아래의 4대 결손 고리로 인해 프로젝트가 지연되거나 무산되는 병목이 발생합니다:")
    add_bullet_p(doc, "Missing Link 1 (천문학적 GPU 서버 Capex 및 리드타임): ", "250B급 대형 파운데이션 MoE 모델을 사내에 구축하려면 고가의 H100 8-GPU 서버(대당 4.5억~6억 원) 1~2대가 필수적이며, 긴 조달 리드타임으로 고객 예산 승인이 좌초됨.")
    add_bullet_p(doc, "Missing Link 2 (전산실 랙 전력 10kW 한계 초과): ", "국내 기업 전산실의 표준 랙당 전력 허용량은 10~15kW 수준인데, H100 8-GPU 랙 서버 1대는 단독 피크 소비전력만 10.2kW에 달해 전산실 전기/공조 한계를 즉각 초과함.")
    add_bullet_p(doc, "Missing Link 3 (국산 NPU 소프트웨어 컴파일러 부재): ", "엔비디아 의존도를 낮추고 소버린 NPU를 도입하려 해도 고객의 파이토치 모델을 NPU에서 돌릴 수 있는 엔터프라이즈 컴파일러가 없어 실배포 불가.")
    add_bullet_p(doc, "Missing Link 4 (완전 폐쇄망 소버린 보안 완결성): ", "금융·방산 등 폐쇄망 환경에서 외부 인터넷 통신 없이 100% 사내 완결되는 지능형 압축·서빙 엔진의 결핍.")

    # -------------------------------------------------------------
    # 본문 제 2 장. [핵심 제언 1] On-Premises AI Full Stack 구축 시 6대 압도적 강점
    # -------------------------------------------------------------
    add_section_header(doc, "제 2 장", "[핵심 제언 1] On-Prem AI Full Stack 구축 시 6대 압도적 강점", 
                       "Missing Link를 완벽히 해결하는 Nota 솔루션 탑재 시 MZC 온프레미스 스택의 차별화")
    
    add_body_p(doc, "Nota.ai의 NetsPresso 최적화 엔진을 MZC Layer 03에 결합함으로써, 앞서 제기된 4대 결손 고리를 해결하고 다음과 같은 6대 압도적 사업적 강점을 확보합니다:")

    strengths = [
        ("강점 1. 온프레미스 GPU 서버 Capex 75% 절감 및 조달 리드타임 파괴",
         "2,500억 매개변수(250B)급 MoE 모델을 기존 8-GPU(H100) 서버 대신 단 2-GPU 서버(약 1.5억 원)로 서빙 가능하게 하여 하드웨어 도입 비용을 즉시 75% 절감하고 도입 리드타임을 수개월 단축합니다. (지능 손실 단 -0.40% 보존)"),
        
        ("강점 2. 사내 전산실 랙 전력(Rack Power) 및 쿨링 공조 한계(10kW) 완벽 극복",
         "H100 8-GPU 서버 1대의 피크 소비전력(10.2kW)을 2-GPU 구성(3.2kW)으로 대폭 낮추어, 수억 원의 전산실 수냉/전기 증설 공사 없이 기존 기업 전산실 랙에 즉시 안전하게 마운트할 수 있습니다."),
        
        ("강점 3. 100% 완전 폐쇄망(Air-Gap) 소버린 AI 보안 체계 완결",
         "외부 인터넷 연결이 법적으로 금지된 금융, 방산, 제조 R&D의 사내 폐쇄망(Air-Gap)에 온프레미스 컨테이너 Appliance 형태로 탑재되어 데이터 유출 가능성을 원천 차단합니다."),
        
        ("강점 4. 국산 AI 반도체(NPU) 온프레미스 조기 상용화 및 외산 락인 탈피",
         "리벨리온, 딥엑스, 모빌린트 등 국산 NPU에 특화된 자동 연산자 분해/치환 및 타깃 컴파일을 지원하여, 외산 GPU 의존도를 낮추고 소버린 AI 인프라 구축 고객을 독점 선점합니다."),
        
        ("강점 5. 현장(Edge) ➔ 사내 전산실(Core)을 연결하는 하이브리드 온프레미스 스택",
         "스마트팩토리 현장 단말에서는 NetsPresso 경량화 모델로 30FPS 실시간 불량을 검출하고, 특이 상황 시 사내 온프레미스 중앙 서버의 대형 MoE로 라우팅하는 유기적 엣지-코어 하이브리드를 완성합니다."),
        
        ("강점 6. 기업 보유 기존 레거시/중급 GPU 인프라의 파운데이션 모델 재활용",
         "신규 H100 구매가 어려운 고객도 이미 보유 중인 RTX 6000 Ada, L40S, 구형 A100(80GB) 2~4장 환경에서 100B~250B급 파운데이션 모델을 60+ TPS로 쾌속 서빙할 수 있어 기투자 IT 자산 ROI를 극대화합니다.")
    ]
    for s_title, s_desc in strengths:
        add_sub_header(doc, s_title)
        add_body_p(doc, s_desc, space_after=5)

    # -------------------------------------------------------------
    # 본문 제 3 장. [핵심 제언 2] MZC On-Prem AI Full Stack x Nota 4대 턴키 솔루션
    # -------------------------------------------------------------
    add_section_header(doc, "제 3 장", "[핵심 제언 2] MZC On-Prem AI Full Stack x Nota 4대 턴키 패키지", 
                       "서버 인프라 중심 주력 오퍼링 2종 및 Physical/Edge AI 시장 탐색형 오퍼링 2종 이원화")
    
    add_body_p(doc, "MZC의 핵심 역량이 집중된 엔터프라이즈 서버 및 데이터센터 인프라 솔루션을 [파트 A. 최우선 주력 오퍼링]으로 전진 배치하고, "
                    "상대적으로 초기 탐색 단계인 Embedded / Edge / Physical AI 영역은 Nota의 기술력을 레버리지하는 [파트 B. 전략적 시장 탐색] 오퍼링으로 이원화하여 사업을 추진합니다.")

    # 파트 A: 서버 AI 인프라 중심 주력 오퍼링
    add_sub_header(doc, "■ [파트 A. 핵심 주력] 엔터프라이즈 서버 AI 인프라 솔루션 (MZC 핵심 역량 직접 연계)")
    add_body_p(doc, "MZC의 인프라 SI/MSP 역량과 즉각 결합되어 고수익을 창출하는 최우선 공략 패키지군입니다.", space_after=4)
    
    server_packages = [
        ("패키지 1. 소버린 파운데이션 MoE 온프레미스 패키지 (Sovereign MoE On-Prem)",
         "• 대상 고객: 사내 기밀 문서 RAG, 프라이빗 코딩 에이전트 구축을 원하는 금융, 방산, 그룹사\n"
         "• 하드웨어 구성: Dell PowerEdge R760 (2x NVIDIA H100 NVL 또는 4x L40S) + Nutanix 온프레미스\n"
         "• 소프트웨어 스택: NetsPresso MoE INT4/NVFP4 압축 엔진 + vLLM 초저지연 서빙 + RHOAI Workbench\n"
         "• 제안 셀링포인트: 8-GPU 대형 클러스터 대비 하드웨어 TCO 75% 절감, 단일 2U 랙 서버로 60+ TPS 달성"),
        
        ("패키지 2. 소버린 국산 NPU 데이터센터 패키지 (Sovereign NPU Zero Lock-in)",
         "• 대상 고객: 공공 클라우드 사업자, 국가 R&D 센터, 탈 엔비디아 소버린 AI 인프라 구축 희망 기업\n"
         "• 하드웨어 구성: 리벨리온 ATOM / 딥엑스 M1 / 모빌린트 ARIES NPU 탑재 온프레미스 서버\n"
         "• 소프트웨어 스택: NetsPresso NPU 맞춤형 자동 컴파일러 + PyTorch 연산자 자동 분해/치환 모듈\n"
         "• 제안 셀링포인트: 소프트웨어 호환성 문제 100% 해결, 외산 GPU 대비 전력 및 도입 비용 60% 절감")
    ]
    for p_title, p_desc in server_packages:
        add_sub_header(doc, p_title)
        add_body_p(doc, p_desc, space_after=6)
        
    # 파트 B: Physical AI 및 Edge AI 시장 탐색형 오퍼링
    add_sub_header(doc, "■ [파트 B. 시장 탐색 및 확장 옵션] Physical AI & Edge AI 솔루션 (중장기 파트너십 협력형)")
    add_body_p(doc, "MZC의 자체 역량이 아직 Embedded/Edge/Physical AI 분야에서는 성숙 전 단계이므로, 무리한 직접 투자보다는 Nota의 글로벌 검증 기술력(두바이 RTA 계약, 대전시 200개 교차로, SmolVLA 로보틱스)을 전면에 세워 수요를 발굴하는 전략적 시장 탐색 오퍼링입니다.", space_after=4)
    
    edge_packages = [
        ("패키지 3. 스마트팩토리 하이브리드 비전 & Physical AI 패키지 (Smart Factory & Physical AI)",
         "• 대상 고객: 제조 공정 불량 검출, 작업장 안전 관제, 조작 로봇(VLA) 도입 희망 스마트공장\n"
         "• 하드웨어 구성: 현장용 Advantech/NVIDIA Jetson Orin NX 엣지 박스 + 사내 온프레미스 R760 서버\n"
         "• 소프트웨어 스택: NetsPresso 엣지 비전 경량화(YOLOX-s INT8, -76% 지연) + SmolVLA 로봇 조작 제어\n"
         "• 전략적 접근: 30FPS 실시간 현장 판정과 로봇 작업 성공률 +4.6% 제고를 바탕으로 제조 버티컬 시장 기회 탐색"),
        
        ("패키지 4. 공공/지자체 스마트교통 & 스마트시티 턴키 패키지 (Smart City & ITS Turnkey)",
         "• 대상 고객: 스마트 교차로 현대화, 터널/고속도로 돌발 상황 관제, 항만 자율주행 지자체 및 공공기관\n"
         "• 하드웨어 구성: 도로변 엣지 AI 관제 제어기 + 지자체 통합관제센터 온프레미스 서버\n"
         "• 소프트웨어 스택: Nota ITS 스마트 교차로 + VLM 기반 AID(자동 돌발 검지) + V2X 통신 모듈\n"
         "• 전략적 접근: 대전시(200개 교차로) 및 두바이 RTA 납품 레퍼런스를 앞세워 공공 스마트 인프라 사업 타당성 검토")
    ]
    for p_title, p_desc in edge_packages:
        add_sub_header(doc, p_title)
        add_body_p(doc, p_desc, space_after=6)

    # -------------------------------------------------------------
    # 본문 제 4 장. 비즈니스 협력 모델, 라이선스 체계 및 최종 포지셔닝 선언
    # -------------------------------------------------------------
    add_section_header(doc, "제 4 장", "비즈니스 협력 모델, 실행 로드맵 및 최종 포지셔닝 선언", 
                       "하드웨어 어플라이언스 번들링 및 사내 MZC AI 데모 랩 실측을 통한 3단계 시장 공략")
    
    add_sub_header(doc, "1. 온프레미스 상용 라이선스 비즈니스 모델")
    add_bullet_p(doc, "어플라이언스 번들링 영구 라이선스: ", "서버 대당 Perpetual License + 연간 유지보수(15~20%) 방식으로 Dell/Nutanix 하드웨어 견적에 포함.")
    add_bullet_p(doc, "소켓/코어 기반 서브스크립션: ", "사내 프라이빗 클라우드용 연간/다년 단위 구독 라이선스 체계.")
    add_bullet_p(doc, "공공 ITS 턴키 SI 모델: ", "구축비(SI) + 소프트웨어 솔루션 납품비(Nota) 분배 구조.")

    add_sub_header(doc, "2. MZC x Nota 3단계 공동 실행 로드맵")
    add_bullet_p(doc, "1단계 - 사내 랩 실측 PoC (즉시 실행): ", "MZC 온프레미스 데모 랩에서 Solar-Open2-250B 모델 대상 NetsPresso INT4 압축 실측 및 2-GPU 서빙 TPS/VRAM 벤치마크 백서 발간.")
    add_bullet_p(doc, "2단계 - 공동 오퍼링 상품화 (1개월 내): ", "Dell/Nutanix 하드웨어와 결합한 'MZC Sovereign AI Appliance with Nota' 표준 카탈로그 및 제안서 템플릿 완성.")
    add_bullet_p(doc, "3단계 - 대형 고객 턴키 제안 (2~3개월 내): ", "금융권 폐쇄망 RAG 구축, 제조 엔터프라이즈 스마트공장, 공공 스마트시티 사업에 턴키 공동 입찰.")

    add_sub_header(doc, "3. 최종 전략적 포지셔닝 확정 선언")
    add_callout_box(
        doc,
        "최종 전략적 포지셔닝 확정 (FINAL POSITIONING DECLARATION)",
        "Nota.ai는 MZC AI Full Stack에서 단순한 '경량화 도구 후보군'이 아니며, "
        "① 온프레미스 대규모 AI 도입 시 GPU Capex 75%와 전산실 랙 전력 한계를 파괴하는 [인프라 TCO 혁신 엔진], "
        "② 국산 NPU 조기 상용화를 실현하는 [소버린 반도체 소프트웨어 허브], "
        "③ 스마트팩토리 및 로보틱스 현장 수요를 타진하는 [Physical AI 탐색 엔진], "
        "④ 대전시/두바이 RTA 검증 레퍼런스를 보유한 [스마트 인프라 솔루션]으로서, "
        "MZC 온프레미스 AI Full Stack 사업의 실질적 수주와 수익성을 결정짓는 최상위 '핵심 전략 파트너'로 공식 격상 확정합니다.",
        border_color_hex="9D4EDD",
        bg_color_hex="FDF4FF"
    )

    # -------------------------------------------------------------
    # [부록 / 기술 참조 자료]
    # -------------------------------------------------------------
    p_div = doc.add_paragraph()
    p_div.paragraph_format.space_before = Pt(30)
    p_div.paragraph_format.space_after = Pt(10)
    r_div = p_div.add_run("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n[부록 및 상세 기술 참조 자료 (APPENDIX)]")
    r_div.font.name = FONT_TITLE
    r_div.font.size = Pt(12)
    r_div.bold = True
    r_div.font.color.rgb = COLOR_GOLD

    # 부록 1. 회사 개요 및 글로벌 입지
    add_section_header(doc, "부록 1", "Nota.ai 최신 개요 및 글로벌 사업 위상", "15B 달러 Stargate 프로젝트 유일 AI 스타트업 및 글로벌 파트너십", is_appendix=True)
    add_body_p(doc, "주식회사 노타(Nota.ai)는 AI 모델을 타깃 하드웨어에 맞춰 최적화 및 경량화하는 글로벌 테크 기업입니다. "
                    "단순 엣지 경량화를 넘어 초대형 파운데이션 모델(LLM/MoE), 온디바이스 멀티모달(VLM/VLA), 그리고 지능형 교통체계(ITS) 버티컬 솔루션까지 포괄합니다.")
    add_bullet_p(doc, "15 Billion Stargate Project 유일 참여: ", "삼성전자, 현대자동차그룹과 함께 150억 달러 규모 글로벌 AI 스타게이트 프로젝트에 AI 스타트업으로서 유일하게 공식 참여함.")
    add_bullet_p(doc, "글로벌 거점 및 100+ 파트너십: ", "한국 본사, 미국 실리콘밸리(San Jose), 독일(베를린), UAE(두바이) 거점 운영. Arm, Qualcomm, NVIDIA, ST, NXP 등 100여 개 파트너사와 양산 최적화 진행 중.")

    # 부록 2. NetsPresso 차세대 MoE LLM 압축 기술 상세 및 벤치마크
    add_section_header(doc, "부록 2", "NetsPresso 차세대 MoE 최적화 기술 상세 및 벤치마크 데이터 시트", "3단계 MoE 파이프라인 및 Solar-Open2-250B / Kimi K3 실측", is_appendix=True)
    add_bullet_p(doc, "Step 1 - 데이터 기반 PASCAL-MoE 양자화: ", "민감 전문가 라우팅(5% ➔ 18%)을 식별하여 가중치 4비트(INT4/NVFP4) 정밀 변환 및 라우팅 오차 차단.")
    add_bullet_p(doc, "Step 2 - Router 인지형(Router-Aware) 양자화: ", "전문가 간 토큰 라우팅 오버랩을 0.85 수준으로 견고히 유지(SOTA 0.80 상회)하여 다각적 추론력 보존.")
    add_bullet_p(doc, "Step 3 - 비균일 전역 프루닝(Non-uniform Expert Pruning): ", "층별 기여도 분석 기반 저기여 전문가 모듈 차등 제거로 성능 저하 없이 GPU 50% 추가 절감.")

    # MoE 테이블
    tbl_moe = doc.add_table(rows=6, cols=6)
    tbl_moe.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tbl_moe, color="CBD5E1", sz="4")
    col_w_moe = [Cm(2.6), Cm(3.4), Cm(2.6), Cm(2.6), Cm(2.5), Cm(2.8)]
    
    moe_headers = ["모델명", "최적화 구성", "Weight (GB)", "총 VRAM", "필요 GPU", "핵심 결과 및 지능 보존"]
    moe_data = [
        ["Solar-Open2\n(250B MoE)", "BF16 (원본 베이스라인)", "500.6 GB", "520.6 GB", "H100 x8", "기준 성능 (대형 클러스터 필수)"],
        ["Solar-Open2\n(250B MoE)", "Nota INT4 Global-Pruned", "117.8 GB", "137.8 GB", "H100 x2 (-75%)", "15개 태스크 지능 손실 -0.40%\n단일 2-GPU 서버 서빙 실현"],
        ["Solar-Open2\n(250B MoE)", "Nota NVFP4 Global-Pruned", "126.1 GB", "146.1 GB", "H100 x2 (-75%)", "지능 손실 -0.22% (무손실급)\n2x H100 단일 서버 서빙"],
        ["Solar-Open\n(100B MoE)", "Nota INT4 (과기정통부 1차)", "51.9 GB", "51.9 GB", "A100 x2 (-50%)", "VRAM -72.8%, MMLU 한국어 51.84\n(기존 AWQ 6.19 대비 8배 우수)"],
        ["Kimi K3\n(2.8T 초거대 MoE)", "Nota 50% 비균일 프루닝", "1.4T Params", "VRAM -50%", "B300 x4 (-50%)", "단일 4-GPU 서버 실현\nGPQA-D +2.52, IFEval +2.22"]
    ]
    for c_idx, title in enumerate(moe_headers):
        cell = tbl_moe.rows[0].cells[c_idx]
        cell.width = col_w_moe[c_idx]
        set_cell_margins(cell, top=80, bottom=80, left=70, right=70)
        set_cell_shading(cell, "0F172A")
        p = cell.paragraphs[0]
        r = p.add_run(title)
        r.font.name = FONT_MAIN
        r.font.size = Pt(8.0)
        r.bold = True
        r.font.color.rgb = COLOR_WHITE
        p.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
        
    for r_idx, row in enumerate(moe_data):
        for c_idx, val in enumerate(row):
            cell = tbl_moe.rows[r_idx + 1].cells[c_idx]
            cell.width = col_w_moe[c_idx]
            set_cell_margins(cell, top=70, bottom=70, left=70, right=70)
            if r_idx % 2 == 1:
                set_cell_shading(cell, "F8FAFC")
            p = cell.paragraphs[0]
            r = p.add_run(val)
            r.font.name = FONT_MAIN
            r.font.size = Pt(8.0)
            if "H100 x2" in val or "B300 x4" in val or "-75%" in val:
                r.bold = True
                r.font.color.rgb = COLOR_CRIMSON
            else:
                r.font.color.rgb = COLOR_TEXT_MAIN

    doc.add_paragraph().paragraph_format.space_after = Pt(4)

    # 부록 3. On-Device / Multimodal & 엣지/임베디드 실측
    add_section_header(doc, "부록 3", "On-Device / Multimodal & 엣지/임베디드 실측 데이터", "VLM, 로보틱스 VLA, 음성인식 61배 가속 및 국산 NPU 파트너십", is_appendix=True)
    add_bullet_p(doc, "Qualcomm IQ-9075 Llava-1.5-7B (VLM): ", "7.6 ➔ 15.6 FPS (2.05배 가속), VRAM 13.9GB ➔ 4.3GB (-69% 절감).")
    add_bullet_p(doc, "NVIDIA RTX 3090 SmolVLA 0.5B (로보틱스 Action): ", "621 ➔ 357ms (1.74배 가속), 로봇 작업 성공률 +4.6% 향상.")
    add_bullet_p(doc, "NVIDIA RTX 3090 Qwen3-ASR-0.6B (음성인식): ", "429 ➔ 7ms (61.3배 가속, CER -0.3% 지능 유지).")
    add_bullet_p(doc, "국산 NPU 에코시스템 실증: ", 
                 "모빌린트 ARIES(80TOPS): VLM 객체탐지 DETR 재설계 1601ms ➔ 89.97ms(94% 단축),\n"
                 "텔레칩스 Dolphin5: 차량용 비전 4종 100% 구동,\n"
                 "딥엑스 M1 NPU: ViT-L/14 CLIP 인코더 최적화 108.9ms ➔ 95.37ms.")

    # 부록 4. 독자 버티컬 솔루션 Nota ITS
    add_section_header(doc, "부록 4", "독자 버티컬 솔루션: Nota ITS 상세 분석", "대전 200개 교차로, 케냐 수출, UAE 두바이 RTA VLM 계약", is_appendix=True)
    add_bullet_p(doc, "스마트 교차로 시스템: ", "대전광역시 200개 교차로(800ch) 실구축 운영 (99% 공인 정확도), 케냐 나이로비 25개 지점 수출 계약 체결.")
    add_bullet_p(doc, "VLM 기반 자동 돌발 검지(AID): ", "한국 국도 ITS 혁신기술공모사업 선정, UAE 두바이 교통국(RTA) VLM 기반 도로 영상 관제 계약 체결.")
    add_bullet_p(doc, "V2X 협력 자율주행: ", "제주/인천 항만 자율주행 가이던스, UAE 아부다비 사디야트 섬 보행자/자율주행 V2X PoC 완료.")

    # 부록 5. 참고 문헌 및 공식 전달 기술 자료 출처
    add_section_header(doc, "부록 5", "참고 문헌 및 공식 전달 기술 자료 출처", "Nota.ai 협의 전달 원본 문서 및 보도 기사 출처", is_appendix=True)
    references = [
        ("Nota_ITS_FCD_2026.pdf", "주식회사 노타 공식 ITS 솔루션 및 글로벌 사례 소개서 (2026, 19p)"),
        ("Nota_NetsPresso_FCD_한글_2026_H1.pdf", "NetsPresso 기반 AI 모델 최적화 서비스 공식 기술 문서 (2026 H1, 40p)"),
        ("Nota_NetsPresso_UseCases_2026H2_v1.0.pdf", "NetsPresso 고객 성공 사례집 (SKT, Arm, 삼성, 업스테이지, 모빌린트, 텔레칩스 등, 2026 H2, 14p)"),
        ("Nota_NetsPresso_기사내용.pdf", "대규모 MoE LLM(Solar-Open-100B, Solar-Open2-250B, Kimi K3) 최적화 기술 분석 기사 (2026, 6p)"),
        ("양자화_최적화_사례.pdf", "NVIDIA H100/A100, Qualcomm IQ, RTX 3090 및 국산 NPU 실측 데이터 시트 (2026, 7p)"),
        ("e4ds News (2026)", "노타, 과기정통부 국가 파운데이션 모델 100B 최적화로 GPU 50% 절감 보도"),
        ("The AI News (2026)", "노타, 2500억 파라미터 거대 모델 4비트 양자화 및 비균일 프루닝 성공 보도"),
        ("ZDNet Korea (2026)", "노타, 2.8조 매개변수 Kimi K3 최신 모델 B300 4장으로 서빙 최적화 보도")
    ]
    for ref_title, ref_desc in references:
        add_bullet_p(doc, f"{ref_title}: ", ref_desc)

    return doc


def main():
    doc = create_document()
    
    out_dir1 = Path(r"c:\dev\antigravity-workspace\aifullstack\offering\docx")
    out_dir2 = Path(r"c:\dev\antigravity-workspace\aifullstack\docs")
    out_dir1.mkdir(parents=True, exist_ok=True)
    out_dir2.mkdir(parents=True, exist_ok=True)
    
    filename = "2026-09-07_Nota_AI_Comprehensive_Fullstack_Positioning_Report.docx"
    
    target1 = out_dir1 / filename
    target2 = out_dir2 / filename
    
    doc.save(str(target1))
    print(f"Saved: {target1} ({target1.stat().st_size / 1024:.1f} KB)")
    
    doc.save(str(target2))
    print(f"Saved: {target2} ({target2.stat().st_size / 1024:.1f} KB)")


if __name__ == "__main__":
    main()
