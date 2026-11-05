# -*- coding: utf-8 -*-
"""
Unity 발표자료 HTML에서 발표 내용과 무관한 내부 개발/메타 문구 전수 제거 및 정제 스크립트
1. 상단 헤더: "핵심 맥락 중심 7-Slide 고밀도 요약본 (원본 PPT 13p 통합)"
   -> "엔터프라이즈 3D 데이터 최적화부터 인텔 온디바이스 Physical AI까지"
2. 슬라이드 카테고리 태그 및 배지: "(PPT 1~3P 통합)", "(PPT 4P)", "(PPT 5~6P 통합)", "(PPT 7~8P 통합)", "(PPT 9P)", "(PPT 10P)", "(PPT 11~13P 통합)" 제거
3. 파트 태그: "(PPT 5P)", "(PPT 6P)", "(PPT 7P)", "(PPT 8P)" 제거
4. 목차 모달 타이틀: "(7 Compact Slides — 원본 PPT 13p 통합)" -> "(Full Slide Agenda)"
5. 네비게이션 탭의 불필요한 슬라이드 번호 안내 정제:
   - "전체 (7)" -> "전체"
   - "3D 파이프라인 & 에셋 최적화 (1–3)" -> "3D 파이프라인 & 최적화"
   - "Physical AI & 로보틱스 (4–6)" -> "Physical AI & 로보틱스"
   - "메가존클라우드 도입 로드맵 (7)" -> "도입 로드맵 & 파트너십"
   - "▦ 목차 (7)" -> "▦ 목차"
"""

import re

target_paths = [
    r"C:\Users\MZC01-SUNKIM317\OneDrive\2026\ISSU\Intel 행사\Unity_발표자료.html",
    r"C:\Users\MZC01-SUNKIM317\OneDrive\2026\ISSU\Intel 행사\Unity_발표자료_Showcase.html"
]

for file_path in target_paths:
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. 상단 서브타이틀 교체
    html = re.sub(
        r'<div class="top-subtitle">.*?핵심 맥락 중심.*?</div>',
        '<div class="top-subtitle"><span><strong>엔터프라이즈 3D 데이터 최적화</strong>부터 <strong>인텔 온디바이스 Physical AI</strong>까지</span></div>',
        html,
        flags=re.DOTALL
    )

    # 2. PPT 페이지 번호 및 통합 표시 제거
    # e.g., (PPT 1~3P 통합), (PPT 4P), (PPT 5~6P 통합), (PPT 7~8P 통합), (PPT 9P), (PPT 10P), (PPT 11~13P 통합)
    html = re.sub(r'\s*\((?:원본\s*)?PPT\s*[0-9~]+[pP]?\s*(?:통합)?\)', '', html)
    html = re.sub(r'\s*\(PPT\s*Slide\s*[0-9\s\+]+\s*(?:통합)?\)', '', html)
    html = re.sub(r'\s*\(PPT\s*[0-9]+[pP]\)', '', html)

    # 3. 목차 모달 타이틀 정제
    html = html.replace('전체 슬라이드 목차 (7 Compact Slides — 원본 PPT 13p 통합)', '전체 슬라이드 목차 (Full Slide Agenda)')
    html = html.replace('전체 슬라이드 목차 (7 Compact Slides)', '전체 슬라이드 목차 (Full Slide Agenda)')

    # 4. 상단 네비게이션 탭 정제
    html = html.replace('<button class="sectab on" data-sec="all">전체 (7)</button>', '<button class="sectab on" data-sec="all">전체 아젠다</button>')
    html = html.replace('<button class="sectab" data-sec="asset">3D 파이프라인 &amp; 에셋 최적화 (1–3)</button>', '<button class="sectab" data-sec="asset">3D 파이프라인 &amp; 에셋 최적화</button>')
    html = html.replace('<button class="sectab" data-sec="ai">Physical AI &amp; 로보틱스 (4–6)</button>', '<button class="sectab" data-sec="ai">Physical AI &amp; 로보틱스</button>')
    html = html.replace('<button class="sectab" data-sec="partner">메가존클라우드 도입 로드맵 (7)</button>', '<button class="sectab" data-sec="partner">파트너십 &amp; 도입 로드맵</button>')
    html = html.replace('<span>▦ 목차 (7)</span>', '<span>▦ 목차</span>')

    # 5. 각 슬라이드의 data-category 정제 (혹시 남아있을 번호 찌꺼기 제거)
    html = html.replace('data-category="OVERVIEW · END-TO-END PIPELINE & PRODUCT SUITE"', 'data-category="OVERVIEW · 3D PIPELINE & PRODUCT SUITE"')

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)

print("SUCCESS: Cleaned up all internal/meta PPT references from both HTML files.")

