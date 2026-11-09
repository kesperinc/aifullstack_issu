# -*- coding: utf-8 -*-
"""
KG ICT x KGM 모빌리티 BOM 인텔리전스 챗봇 구축 사업제안서 (.docx 및 .pptx 생성 스크립트)
- 수행 기간: 총 4개월 (16주)
- 투입 공수: 총 20.0 M/M (역할별/등급별 세부 M/M 포함)
- 금액 표기: 제외 (고객 대면 제안 설명용 비가격 버전)
"""
import os
import sys
import types
try:
    import PIL
except ImportError:
    pil_mod = types.ModuleType("PIL")
    pil_mod.Image = types.ModuleType("PIL.Image")
    pil_mod.ImageFont = types.ModuleType("PIL.ImageFont")
    sys.modules["PIL"] = pil_mod
    sys.modules["PIL.Image"] = pil_mod.Image
    sys.modules["PIL.ImageFont"] = pil_mod.ImageFont

import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import qn, nsdecls

import pptx
from pptx.util import Inches as PptxInches, Pt as PptxPt
from pptx.dml.color import RGBColor as PptxRGBColor
from pptx.enum.shapes import MSO_SHAPE


def set_cell_background(cell, fill_hex: str) -> None:
    """테이블 셀 배경색을 지정합니다."""
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)


def set_cell_margins(cell, top=110, bottom=110, left=140, right=140) -> None:
    """테이블 셀 내부 여백을 설정합니다."""
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)


def add_styled_table(doc, headers, rows, highlight_last_row=False):
    """문서에 정돈된 엔터프라이즈 스타일 표를 추가합니다."""
    table = doc.add_table(rows=len(rows) + 1, cols=len(headers))
    table.style = 'Table Grid'
    table.alignment = WD_TABLE_ALIGNMENT.CENTER

    # 헤더 행 스타일링
    hdr_cells = table.rows[0].cells
    for i, header_text in enumerate(headers):
        hdr_cells[i].text = header_text
        set_cell_background(hdr_cells[i], "0F2D5F")
        set_cell_margins(hdr_cells[i], top=130, bottom=130, left=150, right=150)
        for p in hdr_cells[i].paragraphs:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for run in p.runs:
                run.font.bold = True
                run.font.color.rgb = RGBColor(255, 255, 255)
                run.font.size = Pt(10)
                run.font.name = '맑은 고딕'
                run._element.rPr.rFonts.set(qn('w:eastAsia'), '맑은 고딕')

    # 데이터 행 스타일링
    for r_idx, row_data in enumerate(rows):
        row_cells = table.rows[r_idx + 1].cells
        is_last = highlight_last_row and (r_idx == len(rows) - 1)
        bg_color = "DBEAFE" if is_last else ("F8FAFC" if r_idx % 2 == 1 else "FFFFFF")
        for c_idx, val in enumerate(row_data):
            row_cells[c_idx].text = str(val)
            set_cell_background(row_cells[c_idx], bg_color)
            set_cell_margins(row_cells[c_idx], top=105, bottom=105, left=140, right=140)
            for p in row_cells[c_idx].paragraphs:
                for run in p.runs:
                    run.font.size = Pt(9.5)
                    run.font.name = '맑은 고딕'
                    run._element.rPr.rFonts.set(qn('w:eastAsia'), '맑은 고딕')
                    if c_idx == 0 or is_last:
                        run.font.bold = True
                        run.font.color.rgb = RGBColor(15, 45, 95)
                    else:
                        run.font.color.rgb = RGBColor(30, 41, 59)
    doc.add_paragraph()


def add_section_heading(doc, text: str) -> None:
    """대단원 제목(Heading 1)을 추가합니다."""
    h = doc.add_heading(text, level=1)
    h.paragraph_format.space_before = Pt(18)
    h.paragraph_format.space_after = Pt(8)
    for run in h.runs:
        run.font.name = '맑은 고딕'
        run._element.rPr.rFonts.set(qn('w:eastAsia'), '맑은 고딕')
        run.font.color.rgb = RGBColor(15, 45, 95)
        run.font.size = Pt(15)
        run.font.bold = True


def add_sub_heading(doc, text: str) -> None:
    """중단원 제목(Heading 2)을 추가합니다."""
    h = doc.add_heading(text, level=2)
    h.paragraph_format.space_before = Pt(12)
    h.paragraph_format.space_after = Pt(4)
    for run in h.runs:
        run.font.name = '맑은 고딕'
        run._element.rPr.rFonts.set(qn('w:eastAsia'), '맑은 고딕')
        run.font.color.rgb = RGBColor(30, 64, 175)
        run.font.size = Pt(12)
        run.font.bold = True


def add_bullet(doc, bold_prefix: str, desc: str) -> None:
    """굵은 머리말이 포함된 불릿 문단을 추가합니다."""
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.space_after = Pt(4)
    r1 = p.add_run(bold_prefix)
    r1.bold = True
    r1.font.color.rgb = RGBColor(15, 45, 95)
    r1.font.name = '맑은 고딕'
    r1._element.rPr.rFonts.set(qn('w:eastAsia'), '맑은 고딕')
    r2 = p.add_run(desc)
    r2.font.name = '맑은 고딕'
    r2._element.rPr.rFonts.set(qn('w:eastAsia'), '맑은 고딕')


def create_word_proposal(output_path: str) -> None:
    """KG ICT 제안 설명용 Word(.docx) 문서를 생성합니다."""
    doc = docx.Document()

    # 여백 설정
    for section in doc.sections:
        section.top_margin = Inches(0.85)
        section.bottom_margin = Inches(0.85)
        section.left_margin = Inches(0.85)
        section.right_margin = Inches(0.85)

    # 기본 폰트 지정
    style = doc.styles['Normal']
    font = style.font
    font.name = '맑은 고딕'
    font.size = Pt(10.5)
    font.color.rgb = RGBColor(30, 41, 59)
    style.element.rPr.rFonts.set(qn('w:eastAsia'), '맑은 고딕')

    # ==========================================================
    # 표지 (Cover Page)
    # ==========================================================
    for _ in range(2):
        doc.add_paragraph()

    p_badge = doc.add_paragraph()
    p_badge.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_badge = p_badge.add_run("KG ICT × KGM 모빌리티 차세대 엔터프라이즈 AI 구축 제안")
    r_badge.font.size = Pt(12)
    r_badge.font.bold = True
    r_badge.font.color.rgb = RGBColor(37, 99, 235)

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_title = p_title.add_run("차세대 온프레미스/하이브리드 Coding Agent 기반\nKGM 자동차 모델별 BOM 인텔리전스 챗봇 구축 사업제안서")
    r_title.font.size = Pt(21)
    r_title.font.bold = True
    r_title.font.color.rgb = RGBColor(15, 45, 95)

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_sub = p_sub.add_run(
        "RHOSAI 표준 플랫폼 · Nota.ai 경량 Qwen2.5-Coder · DuckDB + Kùzu(Graph DB) 듀얼 엔진 ·\n"
        "Voice-to-BOM 음성 검색 및 계층적 드릴다운(Drill-down) 트리 UI 통합 아키텍처"
    )
    r_sub.font.size = Pt(11)
    r_sub.font.color.rgb = RGBColor(100, 116, 139)

    for _ in range(3):
        doc.add_paragraph()

    # 표지 핵심 요약 지표 표
    add_styled_table(
        doc,
        ["핵심 지표 항목", "목표 수준", "핵심 기술 및 비즈니스 기대효과"],
        [
            ["BOM 탐색 소요 시간", "95% 단축", "건당 30분 레거시 수작업 비교 → 자연어/음성 질의 10초 이내 표 출력"],
            ["복합 질의 응답 정합성", "90% 이상", "과거 Text-to-SQL(59%) 한계 극복, 샌드박스 자가수정(Self-Correction) 탑재"],
            ["총 수행 기간 / 공수", "4개월 (16주) / 20.0 M/M", "전담 AI 아키텍트·코딩 에이전트·LLM·데이터·UI 엔지니어 밀착 투입"],
            ["데이터 보안 및 유연성", "100% On-Prem / Hybrid", "RHOSAI 기반 사내망 완벽 격리 배포 및 퍼블릭 클라우드 유연 확장"]
        ]
    )

    for _ in range(2):
        doc.add_paragraph()

    meta_p = doc.add_paragraph()
    meta_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_meta = meta_p.add_run(
        "제안 대상 : KG ICT (KGM 모빌리티 IT 총괄)\n"
        "제안사 : 메가존클라우드(주) (MegazoneCloud)\n"
        "수행 기간 : 총 4개월 (16주)  |  투입 공수 : 총 20.0 M/M\n"
        "제출 일자 : 2026년 11월"
    )
    r_meta.font.size = Pt(11)
    r_meta.font.bold = True
    r_meta.font.color.rgb = RGBColor(51, 65, 85)

    doc.add_page_break()

    # ==========================================================
    # 1. 제안 배경 및 현대차 PoC 교훈
    # ==========================================================
    add_section_heading(doc, "1. 제안 배경 및 현대자동차 남양연구소 PoC 교훈")
    doc.add_paragraph(
        "토레스(EVX/하이브리드/가솔린), 렉스턴(뉴 아레나/스포츠 칸), 액티언, 코란도, 티볼리 등 KGM의 라인업 다변화와 "
        "친환경 전동화 전환에 따라 차종·연식·트림·옵션별 수십만 개 부품 BOM(Bill of Materials) 데이터의 복잡도가 급격히 증가하고 있습니다. "
        "현재 연구소(R&D), 상품기획, 원가기획 부서에서는 과거 차종 사양 비교, 부품 공용화 검토, 옵션 조합별 파트넘버 확인 시 "
        "복잡한 레거시 PLM/ERP 화면과 파편화된 테이블 구조로 인해 과도한 탐색 시간이 소모되고 있으며, "
        "KG ICT로의 수시 Ad-hoc 데이터 추출 요청이 집중되어 IT 운영 부하가 가중되고 있습니다."
    )

    add_sub_heading(doc, "1.1 현대자동차 남양연구소 PoC 경험 계승과 3대 핵심 보완점")
    doc.add_paragraph(
        "메가존클라우드는 현대자동차 남양연구소와 함께 수행한 'BOM 확인 및 검색 챗봇 PoC' 레퍼런스를 보유하고 있습니다. "
        "당시 실무에서 검증된 자동차 BOM 도메인 노하우를 계승하되, 과거 아키텍처의 한계점을 2026년 최신 AI 기술로 완벽히 극복하여 제안합니다."
    )
    add_bullet(
        doc,
        "① 상호 데이터 준비(Data Readiness) 선행 필수화 : ",
        "과거 PoC는 이미 정제된 데이터셋이 주어진 특수 환경이었습니다. 실무 프로덕션 성공을 위해 1개월차에 KGM 현업 및 KG ICT와 함께 원천 BOM 스키마 정의, 부품 코드 표준화, 결측치 정제를 수행하는 '상호 데이터 준비' 과정을 정규 공정으로 내재화했습니다."
    )
    add_bullet(
        doc,
        "② Text-to-SQL의 한계를 넘어선 Sandbox Coding Agent : ",
        "단발성 SQL 생성 방식(정합성 59% 수준)에서 탈피하여, 코딩 특화 모델이 Python/DuckDB/Kùzu 분석 코드를 작성하고 격리 샌드박스에서 실행·자가수정(Self-Correction)을 거치는 에이전트 아키텍처로 90% 이상의 정합성을 달성합니다."
    )
    add_bullet(
        doc,
        "③ 특정 외산 솔루션 종속 탈피 및 RHOSAI 표준화 : ",
        "과거 IBM watsonx 등 특정 외산 상용 솔루션 종속에서 벗어나, RHOSAI(Red Hat OpenShift AI)를 기본 플랫폼으로 채택하여 사내 온프레미스(On-Premise)와 퍼블릭 클라우드(Public Cloud) 양쪽 모두에 유연하게 배포할 수 있습니다."
    )

    add_styled_table(
        doc,
        ["비교 항목", "과거 현대자동차 남양연구소 PoC (2024)", "KGM 차세대 BOM 인텔리전스 (2026 본 제안)"],
        [
            ["핵심 아키텍처", "전통적 Text-to-SQL + Milvus RAG 구조", "Sandbox Code-Interpreter 에이전트 + Self-Correction 루프"],
            ["추론 방식", "한글→영문 번역 → 5개 고정 Intent 분류 → SQL 생성", "자율 계획(ReAct) → Python/DuckDB/Kùzu 코드 생성·실행·검증"],
            ["기본 인프라 기반", "IBM watsonx, OCP 클라우드 등 특정 벤더 단독 종속", "RHOSAI (Red Hat OpenShift AI) 기반 On-Prem / Cloud 하이브리드"],
            ["데이터 엔진", "Presto / Trino 분산 쿼리 엔진", "초고속 임베디드 OLAP (DuckDB) + Graph DB (Kùzu) 듀얼 엔진"],
            ["적용 모델", "Llama-3.1-8B, SQLCoder-7B (단순 프롬프트 결합)", "Nota.ai 최적화 경량 Qwen2.5-Coder (초저지연 코딩 특화 모델)"],
            ["추론 서빙 엔진", "단순 API / 기본 컨테이너 서빙", "초경량 고속 서빙 엔진 (SGLang / vLLM / llama-server)"],
            ["사용자 인터페이스", "단순 텍스트 챗봇 API (단답형 결과 출력)", "음성 검색(Voice-to-BOM) + 계층적 드릴다운(Drill-down) 트리 UI"],
            ["데이터 준비성", "사전 정제 데이터셋 활용 (특수 환경)", "상호 데이터 스키마 정의 및 도메인 용어 정제 단계 내재화 (90%+ 정합성)"]
        ]
    )

    # ==========================================================
    # 2. 엔드투엔드 시스템 아키텍처 및 6단계 처리 프로세스
    # ==========================================================
    add_section_heading(doc, "2. 엔드투엔드 시스템 아키텍처 및 6단계 처리 프로세스")
    doc.add_paragraph(
        "사용자의 음성 및 자연어 질의가 유입되어 의미 해석, 코드 변환, 샌드박스 탐색, 자가 수정, 멀티모달 UI 응답으로 이어지는 "
        "6단계 엔드투엔드 프로세스와 5대 기능 레이어 구성을 설계하였습니다."
    )

    add_sub_heading(doc, "2.1 6단계 엔드투엔드 질의-응답 처리 흐름")
    add_styled_table(
        doc,
        ["단계", "프로세스 명칭", "수행 주체 (모듈)", "상세 처리 내역 및 데이터 흐름"],
        [
            ["Step 1", "사용자 쿼리 유입", "Web Portal / Whisper STT", "사내 웹 포털 텍스트 입력 또는 마이크 음성 질의(Voice-to-BOM)를 온프렘 Whisper STT가 텍스트로 즉시 변환"],
            ["Step 2", "의미해석 및 캐시 확인", "Semantic Parser LLM & Cache", "빈출 질문(FAQ) 시맨틱 캐시 히트 시 0.1초 내 즉시 반환. 신규 질문은 의도(Intent) 분석 및 차종/부품코드 엔티티 추출"],
            ["Step 3", "쿼리/코드 변환", "Nota.ai 경량 Qwen2.5-Coder", "스키마 메타데이터를 참조하여 DuckDB SQL, Kùzu OpenCypher 그래프 쿼리, 사양 Diff 연산용 Python 코드 동적 작성"],
            ["Step 4", "격리 샌드박스 탐색", "Docker Sandbox (DuckDB+Kùzu)", "격리 컨테이너에서 DuckDB 수치 집계 및 Kùzu BOM 다계층 트리 순회 수행. 에러/빈 결과 발생 시 Self-Correction 루프로 자체 디버깅"],
            ["Step 5", "답변 작성 (합성)", "Response Synthesizer", "도출된 데이터프레임 결과를 기반으로 부품 비교표 마크다운 렌더링, 핵심 사양 차이점 자연어 요약 및 Excel 다운로드 파일 생성"],
            ["Step 6", "멀티모달 최종 응답", "Chat UI / Tree UI / TTS", "대화창 표출과 동시에 우측 BOM 계층 트리 뷰에서 해당 모듈 자동 하이라이트·확장, 음성 안내(TTS) 출력 및 피드백 DB 적재"]
        ]
    )

    add_sub_heading(doc, "2.2 5대 기능 블록 및 RHOSAI 인프라 레이어 구성")
    add_styled_table(
        doc,
        ["계층 (Layer)", "구성 모듈 및 인스턴스", "핵심 역할 및 기술 사양"],
        [
            ["Layer 1 : Client & UI", "React 웹 포털, D3.js 계층 트리 뷰어, 음성 입출력기", "대화형 챗 UI, 완료 결과와 양방향 연동되는 BOM 계층 드릴다운 트리 네비게이터, 핸즈프리 마이크 인터페이스"],
            ["Layer 2 : Gateway & Orchestration", "FastAPI Gateway, LangGraph ReAct Controller, FAQ Cache", "사내 SSO 인증 연동, 에이전트 다단계 추론 상태 관리, 빈출 질문 시맨틱 캐시(0.1초 즉시 응답) 처리"],
            ["Layer 3 : Cognitive & Serving", "RHOSAI GPU Node, SGLang / vLLM, Nota.ai Qwen Coder", "RadixAttention/PagedAttention 기반 초고속 추론 서빙, 온프렘 Whisper STT 및 경량 코딩 특화 모델 구동"],
            ["Layer 4 : Dual Embedded Data", "Isolated Docker Sandbox, DuckDB + Kùzu + Apache Arrow", "네트워크 차단 격리 샌드박스 내에서 DuckDB(OLAP 집계/Diff)와 Kùzu(그래프 트리 순회)를 Zero-Copy 메모리로 통합 구동"],
            ["Layer 5 : Integration & Continuous RAG", "Read Replica, Airflow CDC, Vector DB, Feedback DB", "KGM 원천 PLM/ERP 무부하 읽기 복제본 연동, 신규 출시 차종/설계변경(ECO) 자동 인덱싱 및 사용자 피드백 축적"]
        ]
    )

    add_sub_heading(doc, "2.3 원천 BOM DB 무부하 연동 및 지속적 RAG 현행화 (Continuous RAG)")
    add_bullet(
        doc,
        "• 운영계 부하 원천 차단 (Read-Only Replica & CDC) : ",
        "KGM의 핵심 운영 시스템(PLM/ERP)에 직접 쿼리를 실행하지 않고, 읽기 전용 복제본(Read Replica) 및 Parquet/Graph 스냅샷을 일 단위 또는 CDC(변경 데이터 캡처) 배치로 동기화하여 운영계 영향을 0%로 유지합니다."
    )
    add_bullet(
        doc,
        "• 최신 차종·사양 Active RAG 자동 현행화 : ",
        "신규 차종이나 연식 변경, 설계 변경(ECO) 발생 시 Airflow 파이프라인이 변경된 부품 메타데이터와 약어사전을 자동으로 벡터화하여 에이전트가 항상 최신 BOM 정보를 기반으로 코드를 작성하도록 보장합니다."
    )

    # ==========================================================
    # 3. 모델 및 서빙 혁신 (Nota.ai 경량 Qwen & SGLang/vLLM)
    # ==========================================================
    add_section_heading(doc, "3. 모델 및 서빙 혁신 : Nota.ai 경량화 Qwen & 초경량 고속 서빙 엔진")
    doc.add_paragraph(
        "자동차 BOM 분석 코딩 에이전트는 정교한 Python/SQL/Cypher 문법 생성 능력과 현업이 체감하는 빠른 응답 속도(Low Latency)를 동시에 만족해야 합니다."
    )
    add_bullet(
        doc,
        "• Nota.ai NetsPresso® 기반 경량 Qwen2.5-Coder : ",
        "AI 모델 압축 전문 기술인 Nota.ai의 NetsPresso® 플랫폼을 통해 구조적 프루닝(Pruning), INT4/FP8 정밀 양자화, 도메인 지식 증류를 수행합니다. 원본 거대 모델 대비 VRAM 점유율을 40~50% 절감하면서도 코딩 정확도를 95% 이상 보존하여 동시 접속 처리량을 2배 이상 높입니다."
    )
    add_bullet(
        doc,
        "• Ollama의 한계를 넘어서는 엔터프라이즈 서빙 엔진 : ",
        "단일 사용자 중심인 Ollama 대신, 다중 사용자 동시 요청과 에이전트 반복 루프에 최적화된 SGLang, vLLM, llama-server를 환경에 맞게 구성합니다."
    )

    add_styled_table(
        doc,
        ["서빙 엔진", "핵심 기술 특징", "기존 Ollama 대비 강점 및 적용 시나리오"],
        [
            ["SGLang (최우선 추천)", "RadixAttention 기반 프롬프트/KV 캐시 재사용 극대화", "다단계 Coding Agent 및 자가수정(Self-Correction) 반복 시 추론 지연시간 70% 단축, 초당 토큰 처리량(TPS) 1.5~2배 향상"],
            ["vLLM (엔터프라이즈 표준)", "PagedAttention 알고리즘 및 Continuous Batching", "GPU 메모리 파편화 제로화, RHOSAI(OpenShift AI) KServe 표준 런타임 내장 지원으로 엔터프라이즈 안정성 확보"],
            ["llama-server (llama.cpp)", "순수 C/C++ 기반 제로 디펜던시 초경량 바이너리", "극소 메모리 풋프린트 및 CPU+GPU 하이브리드 오프로딩 지원으로 개발/검증 및 경량 엣지 환경에 즉시 구동"]
        ]
    )

    # ==========================================================
    # 4. 데이터 엔진 혁신 : DuckDB + Kùzu 듀얼 아키텍처
    # ==========================================================
    add_section_heading(doc, "4. 데이터 엔진 혁신 : DuckDB + Kùzu (임베디드 Graph DB) 듀얼 아키텍처")
    doc.add_paragraph(
        "자동차 BOM 데이터는 수십만 건의 부품 단가·수량·사양을 집계하는 '테이블 연산(OLAP)' 성격과, "
        "완성차 ➔ 시스템 ➔ 모듈 ➔ 어셈블리 ➔ 단품으로 이어지는 '다계층 트리 및 대체품 네트워크(Graph)' 성격을 동시에 가지고 있습니다. "
        "본 제안은 별도의 무거운 외부 DB 서버 없이 샌드박스 프로세스 내부에서 동작하는 듀얼 임베디드 엔진을 구축합니다."
    )
    add_bullet(
        doc,
        "• DuckDB (In-Process OLAP 엔진) : ",
        "수백만 건의 BOM 테이블을 컬럼 기반 벡터화 연산으로 수 밀리초 내 집계·필터링하며, Python Pandas/Polars와 Zero-Copy로 연동되어 트림 간 사양 비교(Diff) 연산을 초고속으로 처리합니다."
    )
    add_bullet(
        doc,
        "• Kùzu (In-Process Graph DB) : ",
        "DuckDB와 동일한 임베디드 철학을 가진 초고속 C++ 그래프 DB로, OpenCypher 쿼리를 통해 복잡한 다계층 BOM 트리 순회(Traversal), 특정 단품이 사용된 상위 차종 역추적(Where-Used), 단종 부품의 호환 대체 경로 탐색을 밀리초 단위로 수행합니다."
    )
    add_bullet(
        doc,
        "• Apache Arrow Zero-Copy 통합 시너지 : ",
        "Kùzu에서 탐색한 부품 관계 그래프 결과를 메모리 복사 없이 Apache Arrow 포맷으로 즉시 DuckDB/Polars로 전달하여 복합 분석을 단일 파이썬 샌드박스에서 완결합니다."
    )

    # ==========================================================
    # 5. 인터페이스 혁신 : 음성 검색 & 계층적 드릴다운 트리 UI
    # ==========================================================
    add_section_heading(doc, "5. 인터페이스 혁신 : 음성 검색(Voice-to-BOM) & 계층적 드릴다운 트리 UI")
    add_bullet(
        doc,
        "• 🎤 음성 검색 (Voice-to-BOM, 온프렘 Whisper STT) : ",
        "연구실이나 조립·정비 현장에서 도면이나 부품을 다루며 키보드 타이핑이 어려운 상황에서도 마이크 음성만으로 즉시 질의할 수 있습니다. 외부 클라우드 API를 사용하지 않고 사내 GPU 서버 내 Whisper 모델로 한국어 및 부품 영문 약어를 정확히 인식합니다."
    )
    add_bullet(
        doc,
        "• 🌳 계층적 드릴다운(Drill-down) 트리 UI : ",
        "단순 채팅창을 넘어, 화면 우측에 [차종 ➔ 시스템 ➔ 모듈 ➔ 서브어셈블리 ➔ 단품] 계층 구조를 시각적 트리로 제공합니다. 챗봇 답변에서 특정 부품을 클릭하면 트리 뷰가 해당 노드로 자동 펼쳐지며, 트리 노드를 클릭해 하위 부품을 탐색하거나 상위 공용 차종을 역추적할 수 있습니다."
    )
    add_bullet(
        doc,
        "• 💼 부서별 핵심 파생 효과 : ",
        "(R&D 연구소) 사양 비교 및 부품 탐색 시간 95% 단축 / (원가기획·구매) 차종 간 부품 공용화율 분석 및 단종 대체품 즉시 식별 / (KG ICT) 반복 Ad-hoc 데이터 추출 요청 80% 이상 자동화 및 사내 표준 Private AI 플랫폼 자산화."
    )

    doc.add_page_break()

    # ==========================================================
    # 6. 추진 일정 및 WBS (총 4개월 / 16주)
    # ==========================================================
    add_section_heading(doc, "6. 추진 일정 및 WBS (총 4개월 / 16주)")
    doc.add_paragraph(
        "상호 데이터 준비(Data Readiness)부터 RHOSAI 인프라 셋업, DuckDB+Kùzu 듀얼 엔진 구축, Coding Agent 및 멀티모달 트리 UI 개발, "
        "현업 시나리오 100선 검증 및 안정화까지 총 4개월(16주) 일정으로 체계적으로 수행합니다."
    )

    add_styled_table(
        doc,
        ["단계 (Phase)", "수행 기간", "핵심 수행 과업 및 상세 내용", "주요 산출물 / 마일스톤"],
        [
            [
                "1단계: 데이터 준비 및 인프라 구축",
                "1개월차\n(W1 ~ W4)",
                "• KGM-KG ICT 상호 BOM 데이터 스키마 정의 및 정제 기준 수립\n• 주력 차종 원천 테이블 매핑 및 결측치/비표준 코드 정제\n• RHOSAI (On-Prem 또는 Cloud) 클러스터 및 GPU 서빙 환경 셋업",
                "• BOM 표준 스키마 정의서\n• 인프라 아키텍처 설계서\n• 개발/검증 클러스터 오픈"
            ],
            [
                "2단계: 메타데이터 및 듀얼 데이터 엔진",
                "2개월차\n(W5 ~ W8)",
                "• KGM 차종·트림·옵션 코드 표준화 및 현업 약어/용어사전 구축\n• DuckDB(OLAP) + Kùzu(Graph DB) 듀얼 인메모리 파이프라인 구축\n• 운영계 무부하 Read Replica 및 Airflow CDC 자동 동기화 구현",
                "• KGM BOM 도메인 용어사전\n• DuckDB+Kùzu 데이터 엔진\n• CDC 동기화 파이프라인"
            ],
            [
                "3단계: Coding Agent & 멀티모달 UI",
                "3개월차\n(W9 ~ W12)",
                "• Nota.ai 경량 Qwen2.5-Coder 탑재 및 SGLang/vLLM 고속 서빙\n• LangGraph ReAct 플래너, Docker 격리 샌드박스, Self-Correction 구현\n• Voice-to-BOM 음성 검색(STT) 및 계층적 드릴다운 트리 웹 UI 개발",
                "• 샌드박스 Coding Agent\n• FAQ 시맨틱 캐시 모듈\n• 음성/계층 트리 웹 포털"
            ],
            [
                "4단계: 정합성 검증 및 파일럿 오픈",
                "4개월차\n(W13 ~ W16)",
                "• 현업 대표 복합 질의 시나리오 100선 E2E 테스트 (정합성 90%+ 달성)\n• 연구소/원가기획 현업 비공개 파일럿(CBT) 및 피드백 루프 튜닝\n• KG ICT 운영자 기술 이전 교육 및 정식 서비스 오픈(Go-Live)",
                "• 100선 정합성 검증 보고서\n• 운영자/사용자 매뉴얼\n• 정식 서비스 Go-Live"
            ]
        ]
    )

    # ==========================================================
    # 7. 구축 옵션 비교 및 전문 인력 투입 계획 (총 4개월 / 20.0 M/M)
    # ==========================================================
    add_section_heading(doc, "7. 구축 옵션 비교 및 전문 인력 투입 계획 (총 4개월 / 20.0 M/M)")
    doc.add_paragraph(
        "KG ICT의 사내 인프라 보유 현황 및 클라우드 운영 정책에 맞춰 선택하실 수 있도록 2가지 구축 옵션(Option A / Option B)과 "
        "4개월간의 전담 전문 인력 투입 계획(총 20.0 M/M)을 제시합니다. (본 문서는 기술 및 공수 중심 제안 설명용으로 금액 표기를 제외한 버전입니다.)"
    )

    add_sub_heading(doc, "7.1 인프라 구축 옵션 비교 (Option A vs Option B)")
    add_styled_table(
        doc,
        ["구분", "Option A : 온프렘 전용 GPU 서버 도입 포함 패키지", "Option B : 기보유 인프라 / 클라우드 활용 (SW 구축)", "비고"],
        [
            ["인프라 구성 방식", "사내 전산실 내 전용 듀얼 GPU 랙 서버 1식 신규 도입·구축", "고객사 기보유 GPU 서버 또는 퍼블릭 클라우드(AWS/GCP/Azure) 활용", "RHOSAI 기반 동일 아키텍처"],
            ["권장 하드웨어 사양", "NVIDIA RTX 6000 Ada (RTX PRO 6000) 48GB x 2EA (총 96GB VRAM) 2U 서버", "기보유 GPU 자원 또는 클라우드 GPU 인스턴스 할당", "SGLang + 경량 Qwen 구동 최적"],
            ["하드웨어 보증/유지보수", "제조사 정품 3년 24x7 온사이트(NBD) 무상 기술지원 포함", "기존 인프라 또는 클라우드SLA 정책 준용", "안정적 엔터프라이즈 운영"],
            ["SW 구축 투입 공수", "총 20.0 M/M (4개월간 전담 엔지니어링 팀 투입)", "총 20.0 M/M (4개월간 전담 엔지니어링 팀 투입)", "동일 SW 범위 및 품질 보장"],
            ["SW 라이선스 정책", "오픈소스 스택 및 RHOSAI 기반으로 외산 독점 라이선스 종속 없음", "오픈소스 스택 및 RHOSAI 기반으로 외산 독점 라이선스 종속 없음", "장기 TCO 절감 및 내재화"]
        ]
    )

    add_sub_heading(doc, "7.2 전문 인력 투입 공수 세부 내역 (총 4개월 / 20.0 M/M)")
    add_styled_table(
        doc,
        ["역할 (Role)", "기술 등급", "투입 기간", "투입 공수 (M/M)", "주요 담당 업무 및 핵심 산출물"],
        [
            ["PM / AI 아키텍트", "특급", "4개월", "3.0 M/M", "프로젝트 총괄 관리, RHOSAI 하이브리드 아키텍처 설계, 상호 데이터 스키마 표준화 리드"],
            ["Lead Coding Agent 엔지니어", "고급", "4개월", "4.0 M/M", "LangGraph 기반 ReAct 플래너, Docker 격리 샌드박스, Self-Correction 자가수정 루프 개발"],
            ["온프렘/클라우드 LLM 엔지니어", "고급", "4개월", "4.0 M/M", "Nota.ai 경량 Qwen2.5-Coder 최적화, SGLang/vLLM 고속 서빙 클러스터 구성, 프롬프트 튜닝"],
            ["BOM 데이터 / 그래프 엔지니어", "중급", "4개월", "5.0 M/M", "원천 BOM 정제, DuckDB(OLAP) + Kùzu(Graph DB) 듀얼 엔진 구축, Read Replica/CDC 파이프라인"],
            ["UI/UX 개발 & 음성/QA 엔지니어", "중급", "4개월", "4.0 M/M", "Voice-to-BOM 음성 검색(Whisper STT), 계층적 드릴다운 트리 웹 UI, 현업 시나리오 100선 E2E 검증"],
            ["합계 (Total)", "5개 전문 파트", "총 4개월 (16주)", "총 20.0 M/M", "데이터 정제부터 샌드박스 에이전트·멀티모달 트리 UI까지 엔드투엔드 전담 구축"]
        ],
        highlight_last_row=True
    )

    # ==========================================================
    # 8. 성공적인 사업 착수를 위한 사전 협의 요청 사항
    # ==========================================================
    add_section_heading(doc, "8. 성공적인 사업 착수를 위한 사전 협의 요청 사항")
    add_bullet(
        doc,
        "1. 배포 환경 결정 (On-Premise vs Public Cloud) : ",
        "KG ICT 전산실 내 GPU 인프라 가용 여부 및 클라우드 활용 정책을 확인하여 Option A(사내 전용 GPU 서버 신규 도입) 또는 Option B(기보유 인프라/클라우드 활용 SW 구축) 방향을 확정하고자 합니다."
    )
    add_bullet(
        doc,
        "2. 상호 데이터 준비 (Data Readiness) 워크숍 : ",
        "1차 파일럿 대상 주력 차종(토레스, 렉스턴, 액티언 등 3~4개 차종)의 원천 BOM 테이블 스키마, 부품 계층 구조 정의서, 현업 약어/용어사전 샘플 데이터를 조기 상호 검토하여 정제 리드타임을 단축하고자 합니다."
    )
    add_bullet(
        doc,
        "3. 현업 대표 질문 셋 (Golden Test Set) 수집 : ",
        "R&D 연구소 및 원가기획 부서에서 가장 빈번하게 요청하는 대표 BOM 조회 및 사양 비교 질문 30~50건을 사전에 공유해 주시면, 초기 에이전트 정확도 벤치마크 기준으로 즉시 반영하겠습니다."
    )

    # ==========================================================
    # 9. 부록 : 핵심 기술 및 자동차 BOM 도메인 용어집
    # ==========================================================
    add_section_heading(doc, "9. 부록 : 전체 핵심 기술 및 자동차 BOM 도메인 용어집 (Glossary)")
    add_styled_table(
        doc,
        ["용어 (Term)", "풀네임 / 영문 표기", "핵심 정의 및 본 사업에서의 역할"],
        [
            ["BOM (EBOM / MBOM)", "Bill of Materials", "차량 제작에 필요한 모든 부품·모듈·어셈블리의 품번, 수량, 계층 구조 및 조립 관계를 정의한 핵심 데이터베이스 (설계 EBOM / 생산 MBOM)"],
            ["RHOSAI", "Red Hat OpenShift AI", "쿠버네티스 기반 엔터프라이즈 표준 AI 플랫폼으로 On-Premise와 Public Cloud 간 완벽한 이식성과 확장성 보장"],
            ["Code-Interpreter Agent", "Sandbox Coding Agent", "자연어 질의를 해결하기 위해 LLM이 Python/DuckDB/Cypher 분석 코드를 직접 작성하고 격리 샌드박스에서 실행·검증하는 차세대 에이전트"],
            ["Self-Correction Loop", "자가 수정 루프", "코드 실행 중 에러나 빈 결과 발생 시 에이전트가 에러 로그를 스스로 해석하여 코드를 재작성·재실행함으로써 정합성을 90%+로 끌어올리는 기술"],
            ["Nota.ai (NetsPresso®)", "AI Model Compression", "프루닝·양자화(INT4/FP8)·지식증류를 통해 거대 코딩 모델의 VRAM 사용량을 절반으로 줄이면서 추론 속도와 동시 처리량을 극대화하는 기술"],
            ["SGLang / vLLM", "High-Speed Serving Engine", "RadixAttention(SGLang) 및 PagedAttention(vLLM) 기반으로 다단계 에이전트 반복 추론 지연을 70% 단축하는 초경량 고속 서빙 엔진"],
            ["DuckDB + Kùzu", "Dual Embedded Data Engine", "인프로세스 OLAP 엔진(DuckDB)과 인프로세스 Graph DB(Kùzu)를 Apache Arrow Zero-Copy로 결합해 수치 집계와 BOM 트리 순회를 동시 고속 처리"],
            ["Continuous RAG", "지속적 RAG 현행화", "운영계 무부하 복제본(Read Replica/CDC) 연동 및 신규 차종·설계변경(ECO) 메타데이터를 자동 인덱싱하는 파이프라인"],
            ["Voice-to-BOM", "On-Prem Voice Search", "사내 GPU 서버 내 Whisper STT 모델을 활용해 연구소/현장에서 마이크 음성으로 즉각 부품을 조회하는 핸즈프리 인터페이스"],
            ["Drill-down Tree UI", "Hierarchical Tree UI", "완성차부터 단품까지 BOM 다계층 구조를 시각적 트리로 펼쳐보며 대화창과 양방향으로 연동 탐색하는 사용자 인터페이스"]
        ]
    )

    doc.save(output_path)
    print(f"[완료] Word 제안서 생성 완료: {output_path}")


def create_pptx_proposal(output_path: str) -> None:
    """KG ICT 제안 설명용 PowerPoint(.pptx) 문서를 생성합니다 (금액 제외, 4개월, 20.0 M/M 반영)."""
    prs = pptx.Presentation()
    prs.slide_width = PptxInches(13.333)
    prs.slide_height = PptxInches(7.5)
    blank_layout = prs.slide_layouts[6]

    C_NAVY = PptxRGBColor(15, 35, 75)
    C_BLUE = PptxRGBColor(30, 80, 165)
    C_SKY = PptxRGBColor(230, 242, 255)
    C_LIGHT_BG = PptxRGBColor(248, 250, 252)
    C_DARK = PptxRGBColor(30, 41, 59)
    C_GRAY = PptxRGBColor(100, 116, 139)
    C_WHITE = PptxRGBColor(255, 255, 255)
    C_CARD_BORDER = PptxRGBColor(226, 232, 240)

    def add_header(slide, title, category="KG ICT × KGM 모빌리티 AI 혁신 제안"):
        tb_cat = slide.shapes.add_textbox(PptxInches(0.8), PptxInches(0.42), PptxInches(11.7), PptxInches(0.35))
        p_cat = tb_cat.text_frame.paragraphs[0]
        p_cat.text = category.upper()
        p_cat.font.size = PptxPt(11)
        p_cat.font.bold = True
        p_cat.font.color.rgb = C_BLUE

        tb_title = slide.shapes.add_textbox(PptxInches(0.8), PptxInches(0.74), PptxInches(11.7), PptxInches(0.75))
        p_title = tb_title.text_frame.paragraphs[0]
        p_title.text = title
        p_title.font.size = PptxPt(21)
        p_title.font.bold = True
        p_title.font.color.rgb = C_NAVY

    # Slide 1: Cover
    s1 = prs.slides.add_slide(blank_layout)
    bg1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = C_NAVY
    bg1.line.color.rgb = C_NAVY

    tb1 = s1.shapes.add_textbox(PptxInches(1.2), PptxInches(1.8), PptxInches(11.0), PptxInches(3.8))
    tf1 = tb1.text_frame
    tf1.word_wrap = True

    p = tf1.paragraphs[0]
    p.text = "KGM 모빌리티 차종별 사양·부품 정보의 초격차 검색 인텔리전스"
    p.font.size = PptxPt(15)
    p.font.bold = True
    p.font.color.rgb = PptxRGBColor(96, 165, 250)

    p2 = tf1.add_paragraph()
    p2.text = "차세대 온프레미스/하이브리드 Coding Agent 기반\nBOM 인텔리전스 챗봇 구축 제안"
    p2.font.size = PptxPt(32)
    p2.font.bold = True
    p2.font.color.rgb = C_WHITE
    p2.space_before = PptxPt(12)

    p3 = tf1.add_paragraph()
    p3.text = "RHOSAI 표준 플랫폼 & DuckDB+Kùzu 듀얼 엔진 & 지속적 RAG 현행화(Continuous RAG) 설계"
    p3.font.size = PptxPt(14)
    p3.font.color.rgb = PptxRGBColor(203, 213, 225)
    p3.space_before = PptxPt(14)

    tb1_meta = s1.shapes.add_textbox(PptxInches(1.2), PptxInches(5.8), PptxInches(11.0), PptxInches(1.0))
    p_meta = tb1_meta.text_frame.paragraphs[0]
    p_meta.text = "제안 대상: KG ICT  |  제안사: 메가존클라우드(주)  |  수행기간: 총 4개월 (16주)  |  투입공수: 총 20.0 M/M"
    p_meta.font.size = PptxPt(13)
    p_meta.font.color.rgb = PptxRGBColor(148, 163, 184)

    # Slide 2: Executive Summary
    s2 = prs.slides.add_slide(blank_layout)
    add_header(s2, "Executive Summary : 사업 제안 핵심 요약")

    cards = [
        ("01. 배경 및 과제", "데이터 준비성 선행과 KGM BOM 복잡도", "과거 PoC와 달리 현업과 IT 간의 상호 데이터 준비(Data Readiness) 선행 필수\n연구소·원가기획 부서의 부품 탐색 병목 해소 및 Ad-hoc 쿼리 요청 80% 자동화"),
        ("02. 차세대 기술 혁신", "RHOSAI & DuckDB+Kùzu & 경량 모델", "특정 벤더 종속 탈피 RHOSAI 기반 On-Prem/Public 하이브리드 지원\nNota.ai 경량 Qwen 모델과 DuckDB+Kùzu 듀얼 엔진으로 90%+ 정합성 확보"),
        ("03. 파생 가치 및 편의성", "음성 검색 & 계층 트리 UI & 전사 AI 허브", "핸즈프리 음성 질의(Voice-to-BOM) 및 부품 계층 드릴다운 뷰 제공\n부품 공용화율 제고로 신규 금형비 절감 및 KG ICT AI 표준 플랫폼 자산화"),
        ("04. 수행 기간 및 투입 인력", "총 4개월 (16주) · 20.0 M/M 투입", "총 기간: 4개월 (16주) / 전문 인력 20.0 M/M 밀착 투입\nOption A: 온프렘 전용 GPU 서버(RTX PRO 6000 x 2) 신규 도입 패키지\nOption B: 기보유 GPU 인프라 또는 클라우드 활용 SW 구축\n오픈소스 스택 기반으로 상용 라이선스 종속 탈피")
    ]

    for idx, (step, title, desc) in enumerate(cards):
        x = PptxInches(0.8 + idx * 2.95)
        y = PptxInches(1.8)
        w = PptxInches(2.8)
        h = PptxInches(4.9)

        box = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, w, h)
        box.fill.solid()
        box.fill.fore_color.rgb = C_SKY if idx == 1 else C_LIGHT_BG
        box.line.color.rgb = C_BLUE if idx == 1 else C_CARD_BORDER

        tb = s2.shapes.add_textbox(x + PptxInches(0.15), y + PptxInches(0.15), w - PptxInches(0.3), h - PptxInches(0.3))
        tf = tb.text_frame
        tf.word_wrap = True

        p0 = tf.paragraphs[0]
        p0.text = step
        p0.font.size = PptxPt(12)
        p0.font.bold = True
        p0.font.color.rgb = C_BLUE

        p1 = tf.add_paragraph()
        p1.text = title
        p1.font.size = PptxPt(14)
        p1.font.bold = True
        p1.font.color.rgb = C_NAVY
        p1.space_before = PptxPt(8)

        p2 = tf.add_paragraph()
        p2.text = desc
        p2.font.size = PptxPt(10.5)
        p2.font.color.rgb = C_DARK
        p2.space_before = PptxPt(14)

    # Slide 3: 6단계 엔드투엔드 프로세스
    s3 = prs.slides.add_slide(blank_layout)
    add_header(s3, "엔드투엔드 시스템 아키텍처 및 6단계 처리 프로세스")

    steps = [
        ("Step 1. 쿼리 유입", "사내 웹 포털 텍스트 또는\n마이크 음성(Voice-to-BOM)\n온프렘 Whisper STT 변환"),
        ("Step 2. 의미해석 LLM", "FAQ 시맨틱 캐시 확인(0.1초 응답)\n신규 질의 의도(Intent) 분석\n엔티티/부품코드 추출 및 라우팅"),
        ("Step 3. 쿼리/코드 변환", "Nota.ai 경량 Qwen Coder\nDuckDB용 SQL 생성\nKùzu용 Cypher 쿼리 생성\n사양 Diff 연산 Python 코드"),
        ("Step 4. 샌드박스 탐색", "Docker 격리 샌드박스 실행\nDuckDB 수치 집계 & Diff\nKùzu BOM 계층 트리 순회\nSelf-Correction 자가수정 루프"),
        ("Step 5. 답변 합성", "데이터프레임 결과 집계\n부품 사양 비교표 렌더링\n자연어 요약 설명 생성\nExcel/CSV 다운로드 링크"),
        ("Step 6. 멀티모달 응답", "대화창 결과 표출\nBOM 계층 트리 뷰 동적 확장\n음성 안내(TTS) 출력\n피드백 DB 자동 적재")
    ]

    for idx, (st_name, st_desc) in enumerate(steps):
        col = idx % 3
        row = idx // 3
        x = PptxInches(0.8 + col * 3.95)
        y = PptxInches(1.8 + row * 2.5)
        w = PptxInches(3.7)
        h = PptxInches(2.2)

        box = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, w, h)
        box.fill.solid()
        box.fill.fore_color.rgb = C_SKY if idx in [1, 2, 3] else C_WHITE
        box.line.color.rgb = C_BLUE if idx in [1, 2, 3] else C_CARD_BORDER

        tb = s3.shapes.add_textbox(x + PptxInches(0.15), y + PptxInches(0.15), w - PptxInches(0.3), h - PptxInches(0.3))
        tf = tb.text_frame
        tf.word_wrap = True

        p0 = tf.paragraphs[0]
        p0.text = st_name
        p0.font.size = PptxPt(13)
        p0.font.bold = True
        p0.font.color.rgb = C_BLUE if idx in [1, 2, 3] else C_NAVY

        p1 = tf.add_paragraph()
        p1.text = st_desc
        p1.font.size = PptxPt(10.5)
        p1.font.color.rgb = C_DARK
        p1.space_before = PptxPt(8)

    # Slide 4: 구축 옵션 및 20.0 M/M 투입 인력 계획
    s4 = prs.slides.add_slide(blank_layout)
    add_header(s4, "구축 옵션 비교 및 전문 인력 투입 계획 (총 4개월 / 20.0 M/M)")

    s4_table = s4.shapes.add_table(7, 5, PptxInches(0.8), PptxInches(1.75), PptxInches(11.73), PptxInches(5.0))
    s4_tbl = s4_table.table
    s4_tbl.columns[0].width = PptxInches(2.7)
    s4_tbl.columns[1].width = PptxInches(1.1)
    s4_tbl.columns[2].width = PptxInches(1.4)
    s4_tbl.columns[3].width = PptxInches(1.5)
    s4_tbl.columns[4].width = PptxInches(5.03)

    h_mm = ["역할 (Role)", "등급", "투입 기간", "투입 공수", "주요 담당 업무 및 핵심 산출물"]
    for ci, h in enumerate(h_mm):
        c = s4_tbl.cell(0, ci)
        c.text = h
        c.fill.solid()
        c.fill.fore_color.rgb = C_NAVY
        for p in c.text_frame.paragraphs:
            p.font.size = PptxPt(11)
            p.font.bold = True
            p.font.color.rgb = C_WHITE

    mm_rows = [
        ("PM / AI 아키텍트", "특급", "4개월", "3.0 M/M", "프로젝트 총괄, RHOSAI 아키텍처 설계, 상호 데이터 스키마 표준화 리드"),
        ("Lead Coding Agent 엔지니어", "고급", "4개월", "4.0 M/M", "ReAct 플래너, Docker 격리 샌드박스, Self-Correction 자가수정 루프 개발"),
        ("온프렘/클라우드 LLM 엔지니어", "고급", "4개월", "4.0 M/M", "Nota.ai 경량 Qwen 최적화, SGLang/vLLM 고속 서빙 구성, 프롬프트 튜닝"),
        ("BOM 데이터 / 그래프 엔지니어", "중급", "4개월", "5.0 M/M", "BOM 데이터 정제, DuckDB + Kùzu(Graph DB) 듀얼 엔진 및 CDC 파이프라인"),
        ("UI/UX 개발 & 음성/QA 엔지니어", "중급", "4개월", "4.0 M/M", "Voice-to-BOM 음성 검색(STT), 계층적 드릴다운 트리 UI, 100선 E2E 검증"),
        ("합계 (Option A / B 공통 SW 공수)", "-", "4개월 (16주)", "총 20.0 M/M", "Option A(전용 GPU 서버 신규 도입) / Option B(기보유 인프라·클라우드 활용)")
    ]
    for ri, rdata in enumerate(mm_rows, start=1):
        bg_col = PptxRGBColor(219, 234, 254) if ri == 6 else (C_SKY if ri % 2 == 1 else C_WHITE)
        for ci, val in enumerate(rdata):
            c = s4_tbl.cell(ri, ci)
            c.text = val
            c.fill.solid()
            c.fill.fore_color.rgb = bg_col
            for p in c.text_frame.paragraphs:
                p.font.size = PptxPt(10.5)
                p.font.color.rgb = C_NAVY if (ri == 6 or ci in [0, 3]) else C_DARK
                if ri == 6 or ci in [0, 3]:
                    p.font.bold = True

    prs.save(output_path)
    print(f"[완료] PowerPoint 제안서 생성 완료: {output_path}")


if __name__ == "__main__":
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "docs", "kg_ict"))
    docx_out = os.path.join(base_dir, "KG_ICT_BOM_AI_Proposal.docx")
    pptx_out = os.path.join(base_dir, "KG_ICT_BOM_AI_Proposal.pptx")
    create_word_proposal(docx_out)
    create_pptx_proposal(pptx_out)
