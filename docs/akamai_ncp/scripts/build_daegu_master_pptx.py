# -*- coding: utf-8 -*-
"""
대구 수성알파시티 AI 데이터센터(10MW→40MW) 구축 및 피지컬 AI · 스마트시티 통합 생태계 조성 방안
14-Slide 16:9 Widescreen Native PowerPoint (.pptx) 생성 스크립트
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE


FONT_KR = "맑은 고딕"

# 컬러 팔레트 (비즈니스 프레젠테이션 가독성 최우선 Clean Executive 테마)
C_NAVY = RGBColor(15, 23, 42)        # #0F172A 타이틀/헤더 다크네이비
C_BLUE = RGBColor(24, 90, 189)       # #185ABD 메인 블루
C_BLUE_SOFT = RGBColor(238, 244, 252)# #EEF4FC 연블루 배경
C_TEAL = RGBColor(15, 118, 110)      # #0F766E 에메랄드/틸
C_TEAL_SOFT = RGBColor(240, 253, 250)# #F0FDFA 연틸 배경
C_PURPLE = RGBColor(109, 40, 217)    # #6D28D9 퍼플
C_AMBER = RGBColor(180, 83, 9)       # #B45309 앰버
C_AMBER_SOFT = RGBColor(254, 243, 199)
C_ROSE = RGBColor(190, 18, 60)       # #BE123C 로즈
C_TEXT = RGBColor(30, 41, 59)        # #1E293B 본문
C_MUTED = RGBColor(100, 116, 139)    # #64748B 보조
C_BG = RGBColor(248, 250, 252)       # #F8FAFC 슬라이드 캔버스
C_WHITE = RGBColor(255, 255, 255)
C_BORDER = RGBColor(203, 213, 225)   # #CBD5E1


def set_run_style(run, size_pt, bold=False, color=C_TEXT, font_name=FONT_KR):
    run.font.name = font_name
    run.font.size = Pt(size_pt)
    run.font.bold = bold
    run.font.color.rgb = color


def add_bg(slide, color=C_BG):
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg.fill.solid()
    bg.fill.fore_color.rgb = color
    bg.line.fill.background()
    return bg


def add_header(slide, kicker, title, page_num, total_pages=14):
    # 상단 포인트 라인
    top_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(0.08))
    top_bar.fill.solid()
    top_bar.fill.fore_color.rgb = C_BLUE
    top_bar.line.fill.background()

    # Kicker 배지
    k_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.55), Inches(0.28), Inches(5.8), Inches(0.34))
    k_box.fill.solid()
    k_box.fill.fore_color.rgb = C_BLUE_SOFT
    k_box.line.color.rgb = C_BLUE
    k_box.line.width = Pt(0.75)
    tf_k = k_box.text_frame
    tf_k.word_wrap = True
    tf_k.margin_left = Inches(0.12)
    tf_k.margin_top = Inches(0.03)
    p_k = tf_k.paragraphs[0]
    r_k = p_k.add_run()
    r_k.text = kicker
    set_run_style(r_k, 10.5, bold=True, color=C_BLUE)

    # 페이지 번호
    p_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(11.65), Inches(0.28), Inches(1.13), Inches(0.36))
    p_box.fill.solid()
    p_box.fill.fore_color.rgb = C_WHITE
    p_box.line.color.rgb = C_BORDER
    tf_p = p_box.text_frame
    p_p = tf_p.paragraphs[0]
    p_p.alignment = PP_ALIGN.CENTER
    r_p = p_p.add_run()
    r_p.text = f"{page_num:02d} / {total_pages:02d}"
    set_run_style(r_p, 11, bold=True, color=C_MUTED)

    # 슬라이드 메인 타이틀
    t_box = slide.shapes.add_textbox(Inches(0.55), Inches(0.68), Inches(12.2), Inches(0.58))
    tf_t = t_box.text_frame
    tf_t.word_wrap = True
    p_t = tf_t.paragraphs[0]
    r_t = p_t.add_run()
    r_t.text = title
    set_run_style(r_t, 22, bold=True, color=C_NAVY)

    # 구분선
    line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.55), Inches(1.30), Inches(12.23), Inches(0.02))
    line.fill.solid()
    line.fill.fore_color.rgb = C_BORDER
    line.line.fill.background()


def add_headline_bar(slide, text, accent=C_BLUE):
    box = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.55), Inches(1.42), Inches(12.23), Inches(0.52))
    box.fill.solid()
    box.fill.fore_color.rgb = C_BLUE_SOFT if accent == C_BLUE else C_TEAL_SOFT
    box.line.color.rgb = C_BORDER
    box.line.width = Pt(0.75)

    stripe = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.55), Inches(1.42), Inches(0.09), Inches(0.52))
    stripe.fill.solid()
    stripe.fill.fore_color.rgb = accent
    stripe.line.fill.background()

    tf = box.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf.margin_left = Inches(0.22)
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = text
    set_run_style(r, 12.5, bold=True, color=C_NAVY)


def add_footer(slide, section_label):
    line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.55), Inches(7.02), Inches(12.23), Inches(0.015))
    line.fill.solid()
    line.fill.fore_color.rgb = C_BORDER
    line.line.fill.background()

    fb = slide.shapes.add_textbox(Inches(0.55), Inches(7.06), Inches(8.0), Inches(0.32))
    p = fb.text_frame.paragraphs[0]
    r = p.add_run()
    r.text = section_label
    set_run_style(r, 9.5, bold=False, color=C_MUTED)

    rb = slide.shapes.add_textbox(Inches(8.6), Inches(7.06), Inches(4.18), Inches(0.32))
    pr = rb.text_frame.paragraphs[0]
    pr.alignment = PP_ALIGN.RIGHT
    rr = pr.add_run()
    rr.text = "MEGAZONECLOUD × DAEGU × KIRIA · DGIST"
    set_run_style(rr, 9.5, bold=True, color=C_MUTED)


def add_card(slide, left, top, width, height, badge_text, card_title, bullets, accent=C_BLUE, bg_color=C_WHITE):
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left), Inches(top), Inches(width), Inches(height))
    card.adjustments[0] = 0.04
    card.fill.solid()
    card.fill.fore_color.rgb = bg_color
    card.line.color.rgb = C_BORDER
    card.line.width = Pt(1.0)

    # 상단 컬러 악센트 바
    bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(left + 0.12), Inches(top), Inches(width - 0.24), Inches(0.06))
    bar.fill.solid()
    bar.fill.fore_color.rgb = accent
    bar.line.fill.background()

    tf = card.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.20)
    tf.margin_right = Inches(0.18)
    tf.margin_top = Inches(0.16)
    tf.margin_bottom = Inches(0.12)

    p0 = tf.paragraphs[0]
    p0.space_after = Pt(4)
    r_badge = p0.add_run()
    r_badge.text = f"[{badge_text}]"
    set_run_style(r_badge, 10.5, bold=True, color=accent)

    p_title = tf.add_paragraph()
    p_title.space_after = Pt(8)
    r_title = p_title.add_run()
    r_title.text = card_title
    set_run_style(r_title, 14.5, bold=True, color=C_NAVY)

    for b in bullets:
        p_b = tf.add_paragraph()
        p_b.space_after = Pt(5)
        p_b.line_spacing = 1.25
        if isinstance(b, tuple):
            lead, body = b
            r1 = p_b.add_run()
            r1.text = f"▸ {lead}: "
            set_run_style(r1, 11.5, bold=True, color=C_NAVY)
            r2 = p_b.add_run()
            r2.text = body
            set_run_style(r2, 11.5, bold=False, color=C_TEXT)
        else:
            r1 = p_b.add_run()
            r1.text = f"▸ {b}"
            set_run_style(r1, 11.5, bold=False, color=C_TEXT)


def add_styled_table(slide, left, top, width, height, col_widths, headers, rows, highlight_rows=None):
    if highlight_rows is None:
        highlight_rows = set()
    shape = slide.shapes.add_table(len(rows) + 1, len(headers), Inches(left), Inches(top), Inches(width), Inches(height))
    table = shape.table
    for idx, w in enumerate(col_widths):
        table.columns[idx].width = Inches(w)

    # 헤더
    for c_idx, h_text in enumerate(headers):
        cell = table.cell(0, c_idx)
        cell.fill.solid()
        cell.fill.fore_color.rgb = C_NAVY
        cell.vertical_anchor = MSO_ANCHOR.MIDDLE
        p = cell.text_frame.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        r = p.add_run()
        r.text = h_text
        set_run_style(r, 11.5, bold=True, color=C_WHITE)

    # 바디
    for r_idx, row_data in enumerate(rows):
        is_hi = r_idx in highlight_rows
        for c_idx, val in enumerate(row_data):
            cell = table.cell(r_idx + 1, c_idx)
            cell.fill.solid()
            if is_hi:
                cell.fill.fore_color.rgb = C_BLUE_SOFT
            elif r_idx % 2 == 1:
                cell.fill.fore_color.rgb = RGBColor(241, 245, 249)
            else:
                cell.fill.fore_color.rgb = C_WHITE
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            p = cell.text_frame.paragraphs[0]
            p.line_spacing = 1.2
            r = p.add_run()
            r.text = val
            set_run_style(
                r,
                11.0,
                bold=(c_idx == 0 or is_hi),
                color=(C_BLUE if is_hi and c_idx == 0 else C_NAVY if c_idx == 0 else C_TEXT),
            )


def set_notes(slide, note_text):
    notes_slide = slide.notes_slide
    notes_slide.notes_text_frame.text = note_text


def build_pptx():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "daegu_suseong_aidc"))
    out_path = os.path.join(base_dir, "2026-11-17_daegu_aidc_ecosystem_and_kiria_master_ppt.pptx")

    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # ==================== SLIDE 01: 표지 ====================
    s1 = prs.slides.add_slide(blank_layout)
    add_bg(s1, C_NAVY)
    top_accent = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(0.12))
    top_accent.fill.solid()
    top_accent.fill.fore_color.rgb = C_TEAL
    top_accent.line.fill.background()

    sub_k = s1.shapes.add_textbox(Inches(0.75), Inches(0.85), Inches(11.8), Inches(0.45))
    r = sub_k.text_frame.paragraphs[0].add_run()
    r.text = "DAEGU SUSEONG AI INTEGRATED CENTER & PHYSICAL AI ECOSYSTEM (v3.0)"
    set_run_style(r, 13, bold=True, color=RGBColor(52, 211, 153))

    title_box = s1.shapes.add_textbox(Inches(0.75), Inches(1.40), Inches(11.8), Inches(1.75))
    tf = title_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.line_spacing = 1.25
    r1 = p.add_run()
    r1.text = "대구 수성알파시티 AI 데이터센터(10MW → 40MW) 구축 및\n피지컬 AI · 스마트시티 통합 생태계 조성 방안"
    set_run_style(r1, 31, bold=True, color=C_WHITE)

    desc_box = s1.shapes.add_textbox(Inches(0.75), Inches(3.25), Inches(11.8), Inches(0.85))
    tf_d = desc_box.text_frame
    tf_d.word_wrap = True
    p_d = tf_d.paragraphs[0]
    p_d.line_spacing = 1.35
    r_d = p_d.add_run()
    r_d.text = (
        "연내 10MW 구축 사전 MOU 체결 추진 · 지역 기업 3대 부담을 덜어주는 원스톱 AI 통합 센터(AI DC + R&D + 교육)\n"
        "데이터 안심 격리(Isolation) 기반 로봇 플라이휠 및 스마트시티 · 의료(EMR) · 모빌리티 전 영역 확장 로드맵"
    )
    set_run_style(r_d, 14, bold=False, color=RGBColor(203, 213, 225))

    cover_cards = [
        ("합의 01 · 규모 및 협약", "10MW → 40MW 확대", ["초기 10MW 기준 사업화 확정", "올해(2026년) 내 사전 MOU 체결 추진", "MOU 직후 상세 과제 공동 기획"], C_TEAL),
        ("합의 02 · 지역 생태계", "One-Stop & 안심 격리", ["기업 인프라·인력·데이터 부담 해소", "데이터 인입 허용 · 원본 반출 차단", "기여 기업 저가 인프라·모델 지원"], C_BLUE),
        ("합의 03 · 로봇 고도화", "테스트필드 · 리빙랩 직결", ["특화단지 원격 안전 관제 플라이휠", "DGIST 리빙랩 국산 로봇 비제조 확산", "5종 로봇 후속 지능화 & 가상 사전인증"], C_PURPLE),
        ("합의 04 · 스마트시티·확장", "로봇·드론 → 전 산업", ["수성 무선자가망 이동체·드론 관제", "법정 10년 의료 EMR 백업·DR·유통", "주행시험장(KIAPI)·뿌리·바이오 확장"], C_AMBER),
    ]
    for idx, (b_txt, c_tit, buls, acc) in enumerate(cover_cards):
        add_card(s1, 0.75 + idx * 3.0, 4.35, 2.82, 2.25, b_txt, c_tit, buls, accent=acc, bg_color=C_WHITE)

    foot1 = s1.shapes.add_textbox(Inches(0.75), Inches(6.85), Inches(11.8), Inches(0.4))
    rf1 = foot1.text_frame.paragraphs[0].add_run()
    rf1.text = "공유 대상: 대구광역시 · 한국로봇산업진흥원(KIRIA) · DGIST · 사업추진단   |   제안: 메가존클라우드(주) (2026. 11. 17)"
    set_run_style(rf1, 11, bold=True, color=RGBColor(148, 163, 184))
    set_notes(s1, "본 발표 자료는 대구시와 메가존클라우드 간 논의된 수성알파시티 AI 데이터센터(초기 10MW 구축 후 40MW 단계적 확대)의 연내 사전 MOU 추진과 피지컬 AI·스마트시티 통합 생태계 조성 방안을 정리한 자료입니다.")

    # ==================== SLIDE 02: 10MW -> 40MW 확대 & 연내 사전 MOU ====================
    s2 = prs.slides.add_slide(blank_layout)
    add_bg(s2)
    add_header(s2, "01. 사업 추진 기조 및 사전 협약(MOU) 로드맵", "초기 10MW 기준 단계적 확대(→ 40MW) 및 연내 사전 MOU 체결 추진", 2)
    add_headline_bar(s2, "공공 데이터 개방 및 차년도 상세 과제 공동 기획의 강력한 행정 동력 확보를 위해 ‘올해(2026년) 내 사전 MOU 체결’ 최우선 추진")
    add_card(
        s2, 0.55, 2.10, 5.98, 3.20,
        "대구시 – 메가존클라우드 기합의 프레임워크",
        "단계별 스케일업 기준선 확립 (10MW → 40MW)",
        [
            ("1단계 기준선 확정(10MW)", "초기 인허가·수전 속도 및 타당성 확보를 위해 10MW 규모를 본 사업계획 및 인프라 산정의 기준으로 설정"),
            ("초기 데이터 집중 전략", "구축 초기에는 대구의 최대 강점인 로봇·피지컬 AI 데이터 수집 및 실증 고도화에 최우선 포커스"),
            ("최종 확장 목표(40MW)", "스마트시티, 의료(EMR), 주행시험장, 뿌리제조, 바이오 데이터 확산에 맞춰 40MW 규모로 단계적 확대"),
        ],
        accent=C_BLUE,
    )
    add_card(
        s2, 6.80, 2.10, 5.98, 3.20,
        "행정 동력 확보 핵심 열쇠",
        "왜 ‘연내(2026년 내) 사전 MOU 체결’이 필수적인가?",
        [
            ("공공 협력의 공식 근거", "공공기관 특성상 10MW 이상 AI DC 구축 타당성과 공식 MOU가 선행되어야 적극적 데이터 오픈 및 부서 협업 가능"),
            ("중앙부처 국책 기획 적기 반영", "MOU 직후 대구시·KIRIA·DGIST·메가존 실무 TF를 가동하여 특화단지·리빙랩·지능화 후속 과제 신속 기획"),
            ("입주·실증 앵커 기업 유치", "공식 협약을 바탕으로 수도권·글로벌 로봇 및 AI 모델 기업의 수성 AIDC 참여 유도"),
        ],
        accent=C_TEAL,
    )
    steps_s2 = [
        ("STEP 1 · 2026 연내", "10MW 구축 MOU 체결", ["대구시–MZC 공식 협약 완수"], C_TEAL),
        ("STEP 2 · MOU 직후~27.상", "상세 기획 & 브릿지 가동", ["로봇 데이터 우선 수집·시범사업"], C_BLUE),
        ("STEP 3 · 2029년", "수성 10MW 본 센터 준공", ["AI 통합센터 가동·전국 확장"], C_PURPLE),
        ("STEP 4 · 2030년+", "40MW 확대 & 전 산업 허브", ["의료·모빌리티·바이오 전면 확산"], C_AMBER),
    ]
    for idx, (b_t, c_t, bul, acc) in enumerate(steps_s2):
        add_card(s2, 0.55 + idx * 3.10, 5.48, 2.93, 1.38, b_t, c_t, bul, accent=acc)
    add_footer(s2, "Ⅰ. 사업 추진 기조 및 사전 MOU 로드맵")
    set_notes(s2, "초기 10MW 규모를 사업계획 기준선으로 확정하고 향후 40MW로 확대합니다. 공공기관 데이터 개방과 공동 기획 동력을 위해 올해 안에 10MW 구축 사전 MOU를 체결합니다.")

    # ==================== SLIDE 03: 정부 사업 중복성 돌파 원칙 ====================
    s3 = prs.slides.add_slide(blank_layout)
    add_bg(s3)
    add_header(s3, "02. 정부 예산 심의 대응 원칙: 유사 · 중복성 원천 해소", "물리 시설 중복 신설 NO ➔ ‘전문가 매칭 + 공유 AIDC 고도화’로 돌파", 3)
    add_headline_bar(s3, "기 구축 물리 인프라(달성·DGIST)는 100% 살리고, 기업의 직접 신청 장벽·장비 중복 구매·데이터 유실 병목만 수성 AIDC로 해결")
    add_styled_table(
        s3, 0.55, 2.12, 12.23, 4.65,
        [2.2, 4.8, 5.23],
        ["비교 항목", "기존 개별 실증 · R&D 운영 방식 (As-Is)", "제안 전환 · 고도화 생태계 모델 (To-Be)"],
        [
            ["정부 심의 포지셔닝", "개별 물리 장비·지원센터 추가 신설 위주\n→ 기존 국책사업과 유사·중복성 저촉 우려", "기 구축 물리 거점(테스트필드·리빙랩)의 성과를 배가하는\n공유 AI·데이터 백엔드 고도화 (중복성 원천 해소)"],
            ["기업 참여 프로세스", "중소기업이 독자적으로 시나리오 설계·개별 신청\n→ 높은 기술 진입장벽으로 인해 참여율 저조", "KIRIA 전문위원 · 국내 대학 교수진 · MZC 아키텍트 1:1 매칭\n→ 시나리오 설계부터 AI 학습까지 전주기 컨시어지 견인"],
            ["연산 장비 예산 효율", "과제별 소규모 로컬 워크스테이션 분산 구매\n→ 사업 종료 후 장비 방치 및 급격한 노후화", "수성 AIDC 고성능 GPU · 멀티 시뮬레이션 클라우드 공유 할당\n→ 중복 투자 방지 및 대규모 클러스터 연산 즉시 투입"],
            ["실증 데이터 자산화", "외장하드 개별 반출 후 기업 내부 사장·유실\n→ 사업 종료 후 후속 AI 연구 단절", "초고속 전용망 기반 수성 AIDC 실시간 수집 · 표준 자산화\n→ 사업 종료 후에도 지역 공공 데이터 자산으로 영구 보존"],
            ["최종 기업 수혜 성과", "단발성 물리 시험 성적서 또는 적합/부적합 판정에 국한", "공인 성적서 + 재학습이 완료된 고도화 제어 AI 모델(Weights) 반환"],
        ],
        highlight_rows={0, 3},
    )
    add_footer(s3, "Ⅰ. 사업 추진 기조 및 정부 사업 중복성 해소 논리")
    set_notes(s3, "기존 사업의 낮은 참여율과 중복성 문제를 해결하기 위해, 로봇산업진흥원이나 대학 교수진 전문가를 기업과 매칭하고 연산과 데이터는 수성 AIDC 공유 자원으로 전환합니다.")

    # ==================== SLIDE 04: 대구 AI 생태계 1 - 3대 부담 해소 & AI 통합센터 ====================
    s4 = prs.slides.add_slide(blank_layout)
    add_bg(s4)
    add_header(s4, "03. 대구 AI 생태계 구축 마스터플랜 ①: 지역 기업 체감 효과", "지역 개별 기업 ‘3대 부담’ 원천 해소 및 ‘3위 일체 AI 통합 센터’ 구축", 4)
    add_headline_bar(s4, "개별 기업이 자체 구축하기 어려운 HW · SW 인프라와 선도기업 유치, 인재 교육, 서비스 체험까지 한곳에서 해결하는 복합 거점")
    pains = [
        ("기업 수혜 01 · CapEx 제로화", "인프라 투자 부담 해소", ["수억~수십억 원대 GPU 서버·스토리지·상용 SW 자체 구매 불필요", "필요한 기간·용량만큼 공유 인프라를 즉시 활용하여 초기 투자비 제거"], C_BLUE),
        ("기업 수혜 02 · 인재난 해결", "전문 인력 확보 부담 해소", ["KIRIA·대학 교수진·MZC 엔지니어 매칭으로 고급 AI 기술 공백 보완", "역외 AI 모델·학습 선도기업 유치를 통해 지역 인재 양성·흡수"], C_TEAL),
        ("기업 수혜 03 · 안심 보관", "데이터 저장·보안 부담 해소", ["하루 수 TB씩 폭증하는 비정형 센서 데이터를 45PB 중앙 스토리지에 수용", "전담 보안 관제로 개별 기업의 데이터 관리 및 유출 부담 해소"], C_PURPLE),
    ]
    for idx, (b_t, c_t, bul, acc) in enumerate(pains):
        add_card(s4, 0.55 + idx * 4.14, 2.08, 3.95, 2.38, b_t, c_t, bul, accent=acc)

    centers = [
        ("통합 기능 ①", "코어 AI 데이터센터 (AI DC)", ["H200급 클러스터 + 45PB 스토리지 + 초고속 전용망 HW/SW 통합 제공"], C_TEAL),
        ("통합 기능 ②", "피지컬 AI R&D 센터", ["산·학·연·관 공동 K-RFM 연구개발 및 역외 AI 선도기업 입주 거점"], C_BLUE),
        ("통합 기능 ③", "AI · 로봇 교육 센터", ["지역 대학생 및 재직자 대상 시뮬레이션·데이터 실무 인재 상설 양성"], C_PURPLE),
        ("통합 기능 ④", "AI 서비스 Experience", ["개발된 로봇·스마트시티 AI 서비스를 기업·시민이 체험하는 쇼케이스"], C_AMBER),
    ]
    for idx, (b_t, c_t, bul, acc) in enumerate(centers):
        add_card(s4, 0.55 + idx * 3.10, 4.65, 2.93, 2.15, b_t, c_t, bul, accent=acc, bg_color=C_BLUE_SOFT if idx == 1 else C_WHITE)
    add_footer(s4, "Ⅱ. 대구 AI 생태계 구축 방안 및 지역 기업 수혜 구조")
    set_notes(s4, "지역 기업의 인프라 투자 부담, 전문 인력 부담, 데이터 저장 부담을 해소하고, AI DC와 피지컬 AI R&D 센터, 교육 센터, 서비스 체험 존이 결합된 통합 센터를 구축합니다.")

    # ==================== SLIDE 05: 대구 AI 생태계 2 - One-Stop & 데이터 안심 격리 ====================
    s5 = prs.slides.add_slide(blank_layout)
    add_bg(s5)
    add_header(s5, "04. 대구 AI 생태계 구축 마스터플랜 ②: 데이터 주권 및 확대 재생산", "데이터~서비스 One-Stop 플랫폼 & ‘데이터 안심 격리(Isolation)’ 선순환", 5)
    add_headline_bar(s5, "원본 데이터는 대구 밖으로 나가지 않고(Egress Block), 전국 AI 기업이 대구 플랫폼 안으로 들어와 모델을 개발해 나가는 구조", accent=C_TEAL)
    onestop = [
        ("One-Stop 01", "데이터 표준 수립", ["로봇(RLDS/USD)·도시·산업 표준 규격화"], C_BLUE),
        ("One-Stop 02", "전용망 수집 · 정제", ["비식별화 · 1ms 시간정렬 · 합성 증강"], C_TEAL),
        ("One-Stop 03", "특화 모델 학습", ["대구 안심 격리망 내 파운데이션 학습"], C_PURPLE),
        ("One-Stop 04", "AI 서비스 상용화", ["학습된 모델 가중치·서비스만 현장 배포"], C_AMBER),
    ]
    for idx, (b_t, c_t, bul, acc) in enumerate(onestop):
        add_card(s5, 0.55 + idx * 3.10, 2.08, 2.93, 1.65, b_t, c_t, bul, accent=acc)

    add_card(
        s5, 0.55, 3.92, 5.98, 2.90,
        "보안 · 주권 아키텍처 (Data Isolation)",
        "① 데이터 인입 허용 · 원본 외부 반출 원천 차단",
        [
            ("Ingest OK / Raw Egress Block", "공공·실증·기업 데이터를 폭넓게 인입하되, 대구 역내 폐쇄형 안심 격리망 외부로 원본 유출 원천 차단"),
            ("역외 기업 인바운드 유치", "수도권·글로벌 기업이 대구의 독보적 데이터를 활용하기 위해 수성 플랫폼 내부로 들어와 모델을 만들고 모델만 반출"),
        ],
        accent=C_TEAL,
    )
    add_card(
        s5, 6.80, 3.92, 5.98, 2.90,
        "데이터 양 · 질 확대 재생산 (Data-for-Compute)",
        "② 데이터 제공 기업 ‘저가 인프라 + 특화 모델’ 지원",
        [
            ("인프라 저가 공급 리워드", "양질의 현장 작업·주행·공정 데이터를 인입(제공)하는 기업에 수성 AIDC 연산·스토리지 인프라 저가 제공"),
            ("기업 맞춤형 특화 모델 개발 지원", "제공 데이터를 활용해 해당 기업의 공정·로봇 특화 AI 모델 개발을 직접 기술 지원하여 자발적 데이터 증식 유도"),
        ],
        accent=C_AMBER,
    )
    add_footer(s5, "Ⅱ. 대구 AI 생태계 구축 방안 및 지역 기업 수혜 구조")
    set_notes(s5, "데이터 표준부터 서비스까지 원스톱 플랫폼을 제공하며, 데이터 인입은 허용하되 원본 반출은 차단하는 안심 격리 구조와 데이터 제공 기업 저가 인프라·특화 모델 지원 인센티브를 결합합니다.")

    # ==================== SLIDE 06: 로봇 고도화 1 - 테스트필드 & 특화단지 플라이휠 ====================
    s6 = prs.slides.add_slide(blank_layout)
    add_bg(s6)
    add_header(s6, "05. 로봇 실증 · 특화단지 연계 고도화 ①: 실시간 순환 지능화", "국가로봇테스트필드 전환 및 특화단지 ‘원격 안전 관제 데이터 플라이휠’", 6)
    add_headline_bar(s6, "특화단지 핵심 인프라인 ‘원격 안전 관제 센터’를 수성 AIDC와 결합하여 현장 운용 자체가 학습 데이터를 무한 생산하는 플라이휠 구축")
    add_card(
        s6, 0.55, 2.10, 5.98, 4.70,
        "KIRIA 국가로봇테스트필드 전주기 고도화",
        "달성(물리 실증) ↔ 수성(AI 두뇌) 4단계 직결",
        [
            ("1단계 전문가 매칭 설계", "KIRIA 전문위원·교수진이 기업과 실증 시나리오 및 센서 계측 규격 표준화"),
            ("2단계 가상 사전실증(Pre-Test)", "물리 트랙 투입 전 수성 AIDC 디지털트윈에서 수천 회 시운전으로 충돌·파손 예방"),
            ("3단계 전용망 실시간 수집", "달성 테스트필드 주행·작업 원본 로그를 100~400G 전용 광망으로 무손실 적재"),
            ("4단계 엣지케이스 재학습 반환", "실패·돌발 구간을 합성 증강 및 재학습하여 개선된 AI 제어 모델 패키지 인도"),
        ],
        accent=C_BLUE,
    )
    add_card(
        s6, 6.80, 2.10, 5.98, 4.70,
        "휴머노이드 로봇 특화단지 핵심 인프라 연계",
        "‘원격 안전 관제 센터’ 기반 데이터 플라이휠 구조",
        [
            ("원격 안전 관제 센터 통합 구축", "특화단지 핵심 인프라 사업으로 기획 중인 원격 안전 관제 센터의 백엔드를 수성 AIDC와 직결"),
            ("실시간 예외상황 원격 개입", "현장 로봇이 비정형 장애물·위험에 직면 시 관제사가 초저지연 원격 개입(Tele-op Fallback) 수행"),
            ("데이터 플라이휠(Data Flywheel)", "원격 개입 고가치 데이터 자동 축적 ➔ 수성 AIDC K-RFM 재학습 ➔ 전 로봇 무선 배포(OTA)로 자율성 무한 진화"),
            ("단일 인프라 이중 효과", "법적 안전 관제 의무 이행과 희귀 학습 데이터 대량 확보를 동시에 달성"),
        ],
        accent=C_TEAL,
    )
    add_footer(s6, "Ⅲ. KIRIA · 특화단지 · DGIST 연계 피지컬 AI 고도화")
    set_notes(s6, "국가로봇테스트필드 전주기 고도화와 함께, 휴머노이드 특화단지의 원격 안전 관제 센터를 수성 AIDC와 연결해 관제 개입 데이터가 재학습으로 순환하는 데이터 플라이휠을 구축합니다.")

    # ==================== SLIDE 07: 로봇 고도화 2 - DGIST 리빙랩 · 5종 지능화 · 사전인증 ====================
    s7 = prs.slides.add_slide(blank_layout)
    add_bg(s7)
    add_header(s7, "06. 로봇 실증 · 특화단지 연계 고도화 ②: 비제조 확산 · 국산 지능화 · 안전인증", "DGIST 리빙랩 확대 · 5종 휴머노이드 후속 지능화 · 가상 사전인증제", 7)
    add_headline_bar(s7, "제조를 넘어 비제조 일상 서비스까지 확장하고, 국산 휴머노이드의 지능 경쟁력과 안전 신뢰성 표준을 대구가 선점")
    s7_cards = [
        (
            "DGIST 협력 · 비제조 확산",
            "DGIST 휴머노이드 리빙랩 확대",
            [
                ("국산 로봇 실전 훈련", "주거·돌봄·병원·상업 환경을 모사한 DGIST 리빙랩에 한국(국산) 휴머노이드 집중 투입·훈련"),
                ("비제조 특화 사업 기획", "가사 보조, 실버케어, 대민 서비스 등 비제조 생활밀착 분야 특화 RFM 개발 및 현장 보급 과제 공동 기획"),
            ],
            C_TEAL,
        ),
        (
            "지역 AX 전환 후속 연계",
            "개발 휴머노이드 5종 후속 지능화",
            [
                ("2026년 착수 사업 연속성", "지역 AX 전환 사업을 통해 2026년 개발 시작된 ‘휴머노이드 로봇 5종 개발 사업’과 직결"),
                ("별도 후속 지능화 사업 기획", "개발된 5종 로봇 하드웨어가 세계적 작업 지능을 확보하도록 수성 AIDC 기반 두뇌 고도화 별도 과제 기획"),
            ],
            C_BLUE,
        ),
        (
            "국내 산업 보호 · 글로벌 규제",
            "휴머노이드 가상 사전인증 제도",
            [
                ("저가 외산 무분별 유입 방지", "안전 미검증 외산 로봇 유입을 견제하고 국내 설계·생산 휴머노이드의 안전 신뢰성 확보"),
                ("10만 회 병렬 가상 검증", "실물 파손 없이 인간-로봇 충돌·낙상 안정성 및 사이버보안(EU CRA)을 가상 사전인증"),
            ],
            C_PURPLE,
        ),
    ]
    for idx, (b_t, c_t, bul, acc) in enumerate(s7_cards):
        add_card(s7, 0.55 + idx * 4.14, 2.10, 3.95, 4.70, b_t, c_t, bul, accent=acc)
    add_footer(s7, "Ⅲ. KIRIA · 특화단지 · DGIST 연계 피지컬 AI 고도화")
    set_notes(s7, "DGIST 리빙랩에 국산 휴머노이드를 투입해 비제조 서비스로 확장하고, 2026년 시작된 5종 휴머노이드 개발 사업의 후속 지능화 과제 및 가상 사전인증 제도를 함께 추진합니다.")

    # ==================== SLIDE 08: 핵심 플랫폼 서비스 (DaaS & VLA K-RFM) ====================
    s8 = prs.slides.add_slide(blank_layout)
    add_bg(s8)
    add_header(s8, "07. 핵심 플랫폼 서비스 사업화: DaaS & K-RFM", "로봇 훈련 데이터 서비스(DaaS) 및 비전·언어·행동(VLA) 통합 K-RFM", 8)
    add_headline_bar(s8, "정제된 표준 행동 데이터셋(DaaS)과 물리 법칙을 이해하는 VLA · 월드 모델(K-RFM)을 결합해 지역 공공 · 산업 로봇 수요 총괄 지원")
    add_card(
        s8, 0.55, 2.10, 5.98, 4.70,
        "Robot Training Data-as-a-Service",
        "① 로봇 훈련 데이터 서비스 (Training DaaS)",
        [
            ("1ms 초정밀 멀티모달 동기화", "비전(60fps), 3D LiDAR, 전신 관절·촉각 센서(1kHz) 데이터를 1ms 이내 타임스탬프로 자동 정렬 및 정제"),
            ("비식별화 & 글로벌 표준 패키징", "작업자 안면·민감 설비 자동 마스킹 후 RLDS, LeRobot, OpenUSD 글로벌 표준 규격 변환"),
            ("안심 격리 구독 카탈로그", "희귀 사고·불량 100배 합성 증강 데이터를 포함해 대구 안심 플랫폼 내 즉시 학습 구독 제공 (구축 기간 70% 단축)"),
        ],
        accent=C_TEAL,
    )
    add_card(
        s8, 6.80, 2.10, 5.98, 4.70,
        "Vision-Language-Action & World Model",
        "② VLA 통합 K-RFM 및 물리 월드 모델 허브",
        [
            ("비전·언어·행동(VLA) 통합", "단순 시각 인식을 넘어 자연어 지시와 3D 공간 맥락을 이해하고 물리 행동을 제어하는 차세대 통합 파운데이션 모델"),
            ("자연 현상 모사 월드 모델", "중력·마찰·충돌·변형체 등 물리 인과관계를 예측하는 글로벌 수준 월드 모델(Cosmos 등) 기반 시뮬레이션"),
            ("공공·산업 로봇 지능 허브", "제조(조립·물류) + 비제조(리빙랩 돌봄·가사) + 대구 공공 로봇 수요(방재·순찰) 파인튜닝 및 온보드 경량화 배포"),
        ],
        accent=C_BLUE,
    )
    add_footer(s8, "Ⅳ. 핵심 플랫폼 서비스 및 멀티 시뮬레이션 전략")
    set_notes(s8, "메가존의 기술 파트너십을 활용해 원시 로그를 표준 학습 데이터로 가공하는 DaaS와, 비전·언어·행동이 결합된 VLA 및 물리 월드 모델 기반 K-RFM 서비스를 제공합니다.")

    # ==================== SLIDE 09: 시뮬레이션 다각화 & 오픈소스 지원 ====================
    s9 = prs.slides.add_slide(blank_layout)
    add_bg(s9)
    add_header(s9, "08. Sim-to-Real 시뮬레이션 플랫폼 다각화 및 오픈소스 지원", "NVIDIA Isaac Sim × Unity Industry × 오픈소스 표준 3원화 지원 체계", 9)
    add_headline_bar(s9, "엔비디아·유니티 공식 총판 역량 기반 최상위 상용 환경 제공 + 중소기업 라이선스 부담 해소를 위한 ‘오픈소스 표준 플랫폼’ 병행 지원")
    add_styled_table(
        s9, 0.55, 2.12, 12.23, 4.65,
        [2.3, 2.8, 3.73, 3.4],
        ["시뮬레이션 트랙", "핵심 솔루션 및 표준", "주력 역할 및 기술적 강점", "지역 생태계 및 기업 기대 효과"],
        [
            ["정밀 물리 연산 &\n대규모 강화학습", "NVIDIA Isaac Sim\n/ Isaac Lab", "PhysX 5 기반 다관절 동역학·접촉 물리 연산 및 수천 대 가상 로봇 동시 병렬 강화학습(RL)", "휴머노이드 이족보행 균형, 양팔 정밀 파지 등 고난도 물리 제어 정책 고속 획득"],
            ["디지털트윈 · HRI &\n지역 인력 흡수", "Unity Industry ·\nEnterprise / Pixyz", "대용량 CAD 경량화(Pixyz), 초실사 비전 합성(HDRP), 군중 보행자 HRI, VR 원격조작 수집", "수성알파시티 내 게임·XR·메타버스·유니티 개발 기업 및 청년 인력 즉시 흡수"],
            ["오픈소스 표준 지원\n(라이선스 부담 0원)", "MuJoCo · Gazebo ·\nROS 2 · PyBullet", "상용 라이선스 비용이 전혀 없는 글로벌 표준 오픈소스 물리 엔진 및 미들웨어 컨테이너 기본 제공", "라이선스 비용 부담을 느끼는 중소 로봇기업·스타트업·대학 연구실 진입장벽 제거"],
            ["공통 에셋 상호운용", "OpenUSD 포맷 &\nROS 2 브릿지", "공장·도시·로봇 3D 모델을 글로벌 표준 OpenUSD로 단일화하여 이기종 엔진 간 교차 검증", "단일 물리엔진 과적합(Sim-to-Real Gap) 방지 및 3D 공간 에셋 중복 제작비 절감"],
        ],
        highlight_rows={1, 2},
    )
    add_footer(s9, "Ⅳ. 핵심 플랫폼 서비스 및 멀티 시뮬레이션 전략")
    set_notes(s9, "엔비디아 아이작 심과 유니티 인더스트리 결합으로 지역 XR 개발 인력을 흡수하고, 라이선스 비용이 부담스러운 중소기업을 위해 오픈USD 및 오픈소스 시뮬레이터도 함께 지원합니다.")

    # ==================== SLIDE 10: 수성알파시티 스마트시티 연계 ====================
    s10 = prs.slides.add_slide(blank_layout)
    add_bg(s10)
    add_header(s10, "09. 스마트시티 인프라 융합: 수성알파시티 무선 자가망 × 원격 안전 관제", "이동체 로봇 · 드론을 포괄하는 ‘수성알파시티 AI 스마트시티(City DT)’ 구현", 10)
    add_headline_bar(s10, "수성알파시티 ‘유·무선 자가정보통신망 + 원격 안전 관제 센터’ 결합 ➔ 도심 이동체 로봇과 드론 데이터가 모이는 입체 스마트시티화")
    s10_cards = [
        (
            "3D 공간 베이스맵",
            "Cesium 기반 도시 디지털트윈",
            [
                ("선도 시범 모델 고도화", "세종시 등 디지털트윈 선례를 벤치마킹·고도화하여 수성구(알파시티) 및 동대구 권역 정밀 구축"),
                ("글로벌 표준 공간화", "Cesium 3D Tiles 및 OpenUSD 포맷으로 지상 도로망부터 상공 비행 회랑까지 입체 구현"),
            ],
            C_BLUE,
        ),
        (
            "자가망 + 원격 안전 관제",
            "이동체 로봇 · 드론 입체 관제",
            [
                ("무선 자가망 초저지연 직결", "수성알파시티 무선 자가망을 통해 도심 배송·순찰 로봇과 드론(무인비행체) 실시간 연동"),
                ("지상·공중 통합 안전 통제", "원격 안전 관제 센터에서 다종 이동체 충돌 예방, 비행 안전 및 비상 개입 통합 수행"),
            ],
            C_TEAL,
        ),
        (
            "살아 움직이는 도시 스캐너",
            "도시 변화분(Delta) 실시간 수집",
            [
                ("저비용 맵 자동 갱신", "로봇과 드론이 포착한 도로 파손, 불법 적치물, 재난 징후 변화분만 수성 AIDC로 실시간 수집"),
                ("엣지 프라이버시 보호", "현장 단말에서 보행자 안면·번호판 즉시 비식별화 처리 후 전송하여 규제 완벽 준수"),
            ],
            C_AMBER,
        ),
    ]
    for idx, (b_t, c_t, bul, acc) in enumerate(s10_cards):
        add_card(s10, 0.55 + idx * 4.14, 2.10, 3.95, 4.70, b_t, c_t, bul, accent=acc)
    add_footer(s10, "Ⅴ. 수성알파시티 스마트시티 연계 및 데이터 확장성")
    set_notes(s10, "수성알파시티의 무선 자가망과 원격 안전 관제 센터를 연동해 지상 이동체 로봇과 공중 드론 데이터를 실시간 수집하는 세슘 기반 스마트시티 디지털트윈을 구현합니다.")

    # ==================== SLIDE 11: 전 산업 데이터 영역 확장성 ====================
    s11 = prs.slides.add_slide(blank_layout)
    add_bg(s11)
    add_header(s11, "10. 중장기 데이터 영역 확장성: 대구·경북 핵심 데이터 자산 총결집", "초기 ‘로봇 데이터 최우선 집중’ ➔ 의료(EMR) · 주행시험장 · 뿌리 · 바이오 확장", 11)
    add_headline_bar(s11, "1단계 로봇 피지컬 AI 데이터 수집으로 플랫폼 기반을 완성한 뒤, 대구·경북이 보유한 4대 대규모 산업·공공 데이터로 외연 확장")
    add_styled_table(
        s11, 0.55, 2.12, 12.23, 4.65,
        [2.4, 3.4, 6.43],
        ["확장 단계 및 도메인", "주요 연계 기관 · 원천 인프라", "데이터 수용 · 보안 관리 및 산업 생태계 확장 모델"],
        [
            ["[1단계 최우선 포커스]\n로봇 · 피지컬 AI", "국가로봇테스트필드, 휴머노이드 특화단지,\nDGIST 리빙랩, 스마트시티 로봇·드론", "구축 초기 최우선 역량 집중 — 제조·비제조·실외 이동체 멀티모달 데이터 집중 축적 및 K-RFM · DaaS 생태계 조기 안착"],
            ["[확장 영역 ①]\n의료 · 전자의무기록(EMR)", "대구 첨단의료복합단지, 지역 병원,\n보건소 · 국가지정 센터 의무기록", "• 법적 10년 의무보관 EMR 및 공공 진료기록의 백업 · 보안 · 재해복구(DR) 수용\n• 비식별 가명처리 및 안심 격리 기반 의료 AI 연구 · 헬스케어 데이터 유통 생태계 확장"],
            ["[확장 영역 ②]\n자동차 주행시험장", "지능형자동차부품진흥원(KIAPI) 주행시험장,\n수성알파시티 자율주행 실증지구", "주행시험장 극한 평가 데이터 및 도심 자율주행 로그 직결 ➔ 지역 차부품·전장 기업의 SDV · 자율주행 월드모델 학습 지원"],
            ["[확장 영역 ③]\n뿌리산업 · 제조 공정", "성서·달성 산단 금형·용접·소성·가공 기업,\nDMI 제조AI데이터 플랫폼(MIDAS)", "숙련 작업 공정 데이터 및 비전 검사 데이터 통합 축적 ➔ 전통 뿌리·부품 기업의 다품종 유연 자율제조 전환"],
            ["[확장 영역 ④]\n바이오 · 뇌과학", "지역거점 AX 바이오 트랙, 한국뇌연구원,\n첨복단지 신약·의료기기 연구소", "유전체·단백질 구조 해석, 재활 웨어러블·수술로봇 임상 데이터 등 고성능 디지털 바이오 AI R&D 연산 확장"],
        ],
        highlight_rows={0, 1},
    )
    add_footer(s11, "Ⅴ. 수성알파시티 스마트시티 연계 및 데이터 확장성")
    set_notes(s11, "초기에는 로봇 데이터 수집에 집중하고, 향후 법정 10년 보관 전자의무기록(EMR) 백업·DR 및 연구 유통 생태계를 비롯해 주행시험장, 뿌리산업, 바이오 데이터로 확장합니다.")

    # ==================== SLIDE 12: 인프라 정량 산정 1 - 데이터 발생량 ====================
    s12 = prs.slides.add_slide(blank_layout)
    add_bg(s12)
    add_header(s12, "11. 정량 인프라 용량 설계 ①: 멀티모달 쓰루풋 및 연간 축적량", "로봇(연 10~15 PB) 및 대구 City DT(연 7.5~11.5 PB) 데이터 규모 산정", 12)
    add_headline_bar(s12, "로봇 1대당 일일 500GB ~ 2TB 발생 ➔ 3개년 핵심 학습 데이터셋 목표(약 15PB+) 및 도시 공간 데이터를 정밀 반영한 용량 설계")
    add_styled_table(
        s12, 0.55, 2.12, 12.23, 4.65,
        [2.5, 4.3, 2.4, 3.03],
        ["수집 데이터 도메인", "주요 탑재 센서 및 수집 채널 구성", "단위 발생량 / 쓰루풋", "연간 순증 정제 데이터량"],
        [
            ["양팔 휴머노이드 로봇", "4ch 스테레오 RGB-D + 3D LiDAR + 양손 촉각 + 전신 관절(1kHz)", "대당 1.2 ~ 2.0 TB / 일\n(압축 350~550 Mbps)", "로봇 통합 (300대 기준)\n연 10 ~ 15 PB 순증"],
            ["산업용 협동 · 매니퓰레이터", "손목/오버헤드 고해상도 RGB-D + 6축 F/T 센서 · PLC 로그(1kHz)", "대당 0.5 ~ 0.8 TB / 일\n(압축 150~250 Mbps)", "(원시 60~90PB 중 핵심\n15~20% 선별 + 합성증강)"],
            ["실외 이동체 로봇 · 드론", "6ch 서라운드 카메라 + 128ch LiDAR + Radar + RTK-GNSS/IMU", "대당 1.0 ~ 1.6 TB / 일\n(압축 300~450 Mbps)", "3개년 핵심 학습 풀 ~15PB+"],
            ["대구 City DT 스마트시티", "수성 무선자가망 로봇·드론 변화분 스캔 + 스마트교차로·AI CCTV(비식별) + Cesium 3D 도시맵 갱신", "도시 집계 45 ~ 65 TB / 일\n(자가망 상시 ~20 Gbps+)", "City DT 통합\n연 7.5 ~ 11.5 PB 순증"],
        ],
        highlight_rows={0, 3},
    )
    add_footer(s12, "Ⅵ. 컴퓨트 · 스토리지(45PB) · 광대역 네트워크 정량 설계")
    set_notes(s12, "로봇 1대당 하루 500GB~2TB의 데이터가 발생하여 연간 10~15PB의 순수 로봇 학습 데이터가 축적되며, 대구 City DT 데이터 역시 연간 7.5~11.5PB 규모로 축적됩니다.")

    # ==================== SLIDE 13: 인프라 정량 산정 2 - GPU · 45PB 스토리지 · 광망 ====================
    s13 = prs.slides.add_slide(blank_layout)
    add_bg(s13)
    add_header(s13, "12. 정량 인프라 용량 설계 ②: 연산 클러스터 · 3-Tier 스토리지 · 초고속 망", "GPU 클러스터(H200급 300~500대) · 45 PB 스토리지 · 100~400G 네트워크", 13)
    add_headline_bar(s13, "15PB급 학습 데이터 단일·통합 클러스터 처리 및 멀티테넌트 가동률 버퍼(~30%)를 반영한 균형 잡힌 컴퓨트 · 스토리지 아키텍처")
    add_styled_table(
        s13, 0.55, 2.12, 12.23, 4.65,
        [2.4, 2.2, 3.4, 4.23],
        ["인프라 구성 영역", "설계 산정 규모", "핵심 기술 규격 및 티어링", "설계 근거 및 주요 수용 워크로드"],
        [
            ["고성능 GPU 클러스터\n(학습·시뮬레이션·추론)", "H200급 기준\n300 ~ 400대\n(최대 500대 규모)", "최신 NVIDIA H200(및 차세대 GPU) 고밀도 액랭(DLC) 클러스터, 동적 스케줄링·가상화 분할", "15PB 핵심 데이터셋 단일/통합 클러스터 고속 학습, 다중 랙 확장 및 다수 기업 동시 할당(유효 활용률 ~30% 버퍼 반영)"],
            ["Tier 1: Hot Storage\n(초고속 병렬 스토리지)", "유효 5 PB", "All-Flash NVMe 병렬 파일시스템\n(Lustre/GPFS, GDS, 읽기 600GB/s~1TB/s+)", "수백 대 GPU 동시 학습 시 스토리지 I/O 병목(Starvation) 원천 해소 및 실시간 인제스트 버퍼"],
            ["Tier 2: Warm Storage\n(데이터 레이크하우스)", "유효 15 PB", "고성능 S3 호환 오브젝트 스토리지\n+ 멀티모달 데이터 카탈로그(Iceberg)", "정제 완료 로봇 훈련 데이터(DaaS) 구독 서빙 및 대구 City DT Cesium/OpenUSD 공간맵 호스팅"],
            ["Tier 3: Cold / Archive\n(장기보존·법정백업)", "유효 25 PB\n(총합 45 PB)", "고밀도 아카이빙 스토리지(EC)\n+ WORM(위변조 방지) 및 자동 ILM", "테스트필드·안전인증 원본 증적 보존(3~5년) 및 법정 10년 의무보관 의료 EMR 백업·DR 수용"],
            ["광대역 네트워크 망\n(패브릭 & 외부 전용망)", "내부 400G/800G\n외부 100~400G", "연산-스토리지 400G+ 무손실 패브릭,\n달성·DGIST↔수성 100~400G 광망 + 자가망", "대용량 멀티모달 원본 실시간 무손실 수집 및 원격 안전 관제 센터 초저지연(<2ms) 실시간 제어"],
        ],
        highlight_rows={0, 1},
    )
    add_footer(s13, "Ⅵ. 컴퓨트 · 스토리지(45PB) · 광대역 네트워크 정량 설계")
    set_notes(s13, "15PB 데이터를 단일·통합 클러스터로 구동하고 다중 랙 활용률을 반영해 H200 기준 300~400대(최대 500대)의 GPU와 총 45PB 3-Tier 스토리지, 100~400G 광대역 망을 산정했습니다.")

    # ==================== SLIDE 14: 로드맵 · 역할 분담 및 협의 안건 ====================
    s14 = prs.slides.add_slide(blank_layout)
    add_bg(s14)
    add_header(s14, "13. 추진 로드맵 · 기관별 역할 분담 및 후속 실행 안건", "연내 10MW 사전 MOU 체결 기반 3단계 로드맵 및 실무 협의 사항", 14)
    phases = [
        ("사전 기반 · 2026 연내", "10MW 구축 MOU 체결", ["대구시–MZC 10MW AI DC MOU", "MOU 직후 상세 과제 공동 기획 착수"], C_TEAL),
        ("1단계 · 2027.상 ~ 2028", "브릿지 시범사업 & 수집", ["클라우드 브릿지 조기 시범 가동", "로봇 데이터 우선 수집·입주기업 모집"], C_BLUE),
        ("2단계 · 2029년", "10MW 준공 & 전국 확장", ["수성 10MW 통합센터(DC+R&D+교육)", "데이터 안심 격리 · 전국 기업 확장"], C_PURPLE),
        ("3단계 · 2030년+", "40MW 확대 & 전 산업 허브", ["최종 40MW AI DC 단계적 확대", "의료·주행·뿌리·바이오 통합 허브"], C_AMBER),
    ]
    for idx, (b_t, c_t, bul, acc) in enumerate(phases):
        add_card(s14, 0.55 + idx * 3.10, 1.48, 2.93, 2.05, b_t, c_t, bul, accent=acc, bg_color=C_TEAL_SOFT if idx == 0 else C_WHITE)

    roles = [
        ("정책 · 행정 · 데이터 총괄", "대구광역시", ["10MW→40MW MOU 체결 및 인허가·수전 행정 지원", "중앙부처 예산 협의 및 무선자가망·공공/의료 데이터 연계"], C_BLUE),
        ("전문가 브릿지 · 실증/인증 주관", "KIRIA · DGIST (혁신기관)", ["테스트필드 · 특화단지(원격관제) · 리빙랩 실증 총괄", "기업별 전문가·교수진 매칭 브릿지 및 가상 사전인증 기준"], C_TEAL),
        ("인프라 투자 · 원스톱 플랫폼 운영", "메가존클라우드 (MZC)", ["AI 통합센터 구축·운영 및 준공 전 클라우드 브릿지 제공", "데이터 격리 플랫폼·선도기업 유치·기여기업 저가 인프라 지원"], C_PURPLE),
    ]
    for idx, (b_t, c_t, bul, acc) in enumerate(roles):
        add_card(s14, 0.55 + idx * 4.14, 3.72, 3.95, 2.25, b_t, c_t, bul, accent=acc)

    agenda = s14.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.55), Inches(6.14), Inches(12.23), Inches(0.74))
    agenda.adjustments[0] = 0.08
    agenda.fill.solid()
    agenda.fill.fore_color.rgb = C_BLUE_SOFT
    agenda.line.color.rgb = C_BLUE
    tf_a = agenda.text_frame
    tf_a.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf_a.margin_left = Inches(0.20)
    pa = tf_a.paragraphs[0]
    ra = pa.add_run()
    ra.text = "📌 당면 협의 안건:  ① 연내 『대구시–MZC 10MW AI DC 구축 MOU』 체결 일정 확정  |  ② 데이터 안심 격리 및 기여기업 보상 모델 검토  |  ③ 특화단지 원격관제 · 리빙랩 · 5종 로봇 지능화 공동 기획 TF 가동"
    set_run_style(ra, 11.5, bold=True, color=C_NAVY)

    add_footer(s14, "감사합니다 | 대구광역시 × 한국로봇산업진흥원(KIRIA) × DGIST × 메가존클라우드")
    set_notes(s14, "올해 안에 10MW 구축 사전 MOU를 체결하여 동력을 확보하고, 내년 상반기 브릿지 시범사업부터 2029년 본 센터 준공, 40MW 확대로 이어지는 로드맵을 제안드립니다. 감사합니다.")

    prs.save(out_path)
    print(f"성공: PPTX 파일 생성 완료 -> {out_path} ({os.path.getsize(out_path):,} bytes)")


if __name__ == "__main__":
    build_pptx()
