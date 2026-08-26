import os
import base64

def generate_html_report():
    chart_path = 'docs/feasibility/bep_chart.png'
    html_output_path = 'docs/feasibility/financial_simulation_report.html'
    
    # 1. BEP 차트 이미지를 Base64 문자열로 인코딩
    if os.path.exists(chart_path):
        with open(chart_path, 'rb') as f:
            encoded_bytes = base64.b64encode(f.read())
            base64_chart = encoded_bytes.decode('utf-8')
    else:
        print(f"오류: {chart_path} 파일을 찾을 수 없습니다. 먼저 bep_simulation.py를 실행하십시오.")
        return

    # 2. 시뮬레이션 원시 데이터 정의 (표 렌더링용)
    # 가동률, 매출, MZC수수료, 현금OpEx, 감가상각, 영업이익, EBITDA
    simulation_data = [
        (10, 53283, 10657, 102000, 220000, -279373, -59373),
        (20, 106566, 21313, 102000, 220000, -236747, -16747),
        (30, 159850, 31970, 102000, 220000, -194120, 25880),
        (40, 213133, 42627, 102000, 220000, -151494, 68506),
        (50, 266416, 53283, 102000, 220000, -108867, 111133),
        (60, 319699, 63940, 102000, 220000, -66241, 153759),
        (70, 372983, 74597, 102000, 220000, -23614, 196386),
        (80, 426266, 85253, 102000, 220000, 19013, 239013),
        (90, 479549, 95910, 102000, 220000, 61639, 281639),
        (100, 532832, 106566, 102000, 220000, 104266, 324266)
    ]

    # HTML 테이블 행 작성
    table_rows = ""
    for row in simulation_data:
        rate, rev, mzc, opex, dep, op, ebitda = row
        # 음수 금액 빨간색, 양수 금액 초록색 스타일 클래스 부여
        op_class = "text-danger" if op < 0 else "text-success"
        ebitda_class = "text-danger" if ebitda < 0 else "text-success"
        
        table_rows += f"""
        <tr>
            <td class="font-bold">{rate}%</td>
            <td>{rev:,.0f}</td>
            <td>{mzc:,.0f}</td>
            <td>{opex:,.0f}</td>
            <td>{dep:,.0f}</td>
            <td class="{op_class} font-semibold">{op:+,.0f}</td>
            <td class="{ebitda_class} font-semibold">{ebitda:+,.0f}</td>
        </tr>
        """

    # 3. 프리미엄 CSS 테마가 가미된 HTML 대시보드 템플릿 정의
    html_content = f"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AKAMAI-MZC 공동 GPUaaS 타당성 재무 분석 대시보드</title>
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
                radial-gradient(at 0% 0%, rgba(29, 78, 216, 0.15) 0, transparent 50%),
                radial-gradient(at 100% 100%, rgba(16, 185, 129, 0.1) 0, transparent 50%);
            background-attachment: fixed;
            font-family: 'Noto Sans KR', 'Outfit', sans-serif;
            color: var(--text-main);
            line-height: 1.6;
            padding: 40px 20px;
        }}

        .container {{
            max-width: 1400px;
            margin: 0 auto;
        }}

        /* 헤더 스타일링 (그라데이션 텍스트 & 모던 타이포그래피) */
        header {{
            text-align: center;
            margin-bottom: 40px;
        }}

        .badge {{
            display: inline-block;
            background: rgba(59, 130, 246, 0.15);
            border: 1px solid var(--primary);
            color: #60a5fa;
            padding: 6px 16px;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 500;
            margin-bottom: 12px;
            letter-spacing: 0.05em;
        }}

        h1 {{
            font-family: 'Outfit', 'Noto Sans KR', sans-serif;
            font-size: 2.5rem;
            font-weight: 800;
            background: linear-gradient(to right, #ffffff, #93c5fd, #a7f3d0);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 10px;
        }}

        .subtitle {{
            color: var(--text-muted);
            font-size: 1.1rem;
            font-weight: 300;
        }}

        /* 대시보드 카드 그리드 */
        .grid {{
            display: grid;
            grid-template-columns: repeat(12, 1fr);
            gap: 24px;
            margin-bottom: 30px;
        }}

        .card {{
            background: var(--card-bg);
            border: 1px solid var(--card-border);
            border-radius: 16px;
            padding: 30px;
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.5);
            transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease;
        }}

        .card:hover {{
            transform: translateY(-4px);
            box-shadow: 0 15px 35px -5px rgba(59, 130, 246, 0.15);
            border-color: rgba(59, 130, 246, 0.3);
        }}

        .col-12 {{ grid-column: span 12; }}
        .col-8 {{ grid-column: span 8; }}
        .col-4 {{ grid-column: span 4; }}

        @media (max-width: 1024px) {{
            .col-8, .col-4 {{ grid-column: span 12; }}
        }}

        /* 하이라이트 지표 카드 */
        .kpi-container {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 20px;
            margin-bottom: 24px;
        }}

        .kpi-card {{
            background: linear-gradient(135deg, rgba(22, 25, 32, 0.8) 0%, rgba(30, 41, 59, 0.8) 100%);
            border: 1px solid var(--card-border);
            border-radius: 12px;
            padding: 24px;
            text-align: center;
            position: relative;
            overflow: hidden;
        }}

        .kpi-card::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 4px;
            height: 100%;
            background: var(--primary);
        }}

        .kpi-card.success::before {{ background: var(--success); }}
        .kpi-card.danger::before {{ background: var(--accent); }}

        .kpi-label {{
            font-size: 0.9rem;
            color: var(--text-muted);
            margin-bottom: 8px;
            font-weight: 500;
        }}

        .kpi-value {{
            font-size: 2rem;
            font-weight: 800;
            font-family: 'Outfit', sans-serif;
            background: linear-gradient(to right, #ffffff, #e2e8f0);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}

        .kpi-card.success .kpi-value {{
            background: linear-gradient(to right, #34d399, #a7f3d0);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}

        .kpi-subtext {{
            font-size: 0.8rem;
            color: var(--text-muted);
            margin-top: 6px;
        }}

        /* 테이블 디자인 */
        .table-responsive {{
            overflow-x: auto;
            width: 100%;
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            text-align: left;
            font-size: 0.95rem;
        }}

        th {{
            background: rgba(30, 41, 59, 0.5);
            padding: 14px 16px;
            font-weight: 600;
            color: #93c5fd;
            border-bottom: 2px solid var(--card-border);
        }}

        td {{
            padding: 12px 16px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.05);
        }}

        tr:hover td {{
            background: rgba(255, 255, 255, 0.02);
        }}

        .text-danger {{ color: #f87171; }}
        .text-success {{ color: #34d399; }}
        .font-bold {{ font-weight: 700; }}
        .font-semibold {{ font-weight: 600; }}

        /* 차트 영역 */
        .chart-box {{
            display: flex;
            justify-content: center;
            align-items: center;
            background: rgba(13, 14, 18, 0.5);
            border-radius: 12px;
            padding: 16px;
            border: 1px solid rgba(255, 255, 255, 0.05);
        }}

        .chart-box img {{
            max-width: 100%;
            height: auto;
            border-radius: 8px;
        }}

        /* 텍스트 설명 구조 */
        .report-section-title {{
            font-size: 1.3rem;
            font-weight: 700;
            color: #93c5fd;
            margin-bottom: 15px;
            border-left: 4px solid var(--primary);
            padding-left: 12px;
            font-family: 'Noto Sans KR', sans-serif;
        }}

        ul {{
            list-style-type: none;
            margin-left: 10px;
        }}

        li {{
            margin-bottom: 12px;
            position: relative;
            padding-left: 20px;
            color: #e5e7eb;
        }}

        li::before {{
            content: "✓";
            position: absolute;
            left: 0;
            color: var(--success);
            font-weight: bold;
        }}

        .proposal-details {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-top: 15px;
        }}

        .proposal-item {{
            background: rgba(255, 255, 255, 0.02);
            border: 1px solid rgba(255, 255, 255, 0.04);
            border-radius: 10px;
            padding: 20px;
        }}

        .proposal-item-title {{
            font-weight: 600;
            font-size: 1.05rem;
            margin-bottom: 8px;
            color: #a7f3d0;
        }}

        footer {{
            text-align: center;
            margin-top: 60px;
            color: var(--text-muted);
            font-size: 0.85rem;
            border-top: 1px solid var(--card-border);
            padding-top: 30px;
        }}
    </style>
</head>
<body>

<div class="container">
    <header>
        <span class="badge">AKAMAI & NVIDIA & MZC HYBRID PROJECT</span>
        <h1>공동 GPUaaS 타당성 재무 시뮬레이션 대시보드</h1>
        <p class="subtitle">MZC 자산 매입 & 위탁 운영/영업 수수료 쉐어형 비즈니스 모델 정량 분석</p>
    </header>

    <!-- 하이라이트 주요 지표(KPI) 영역 -->
    <div class="kpi-container">
        <div class="kpi-card danger">
            <div class="kpi-label">초기 투자비 (CapEx)</div>
            <div class="kpi-value">110억 원</div>
            <div class="kpi-subtext">아카마이 전액 부담 (H100 HGX 16대 & L40S 32대)</div>
        </div>
        <div class="kpi-card">
            <div class="kpi-label">영업이익 흑자 BEP 가동률</div>
            <div class="kpi-value">75.54%</div>
            <div class="kpi-subtext">감가상각비(연 22억 원) 반영 회계적 흑자 기준</div>
        </div>
        <div class="kpi-card success">
            <div class="kpi-label">현금흐름(EBITDA) BEP 가동률</div>
            <div class="kpi-value">23.93%</div>
            <div class="kpi-subtext">순수 월 고정비 충당 및 현금 누출 방지 기준</div>
        </div>
        <div class="kpi-card success">
            <div class="kpi-label">투자금 회수 기간 (ROI)</div>
            <div class="kpi-value">약 4.6년</div>
            <div class="kpi-subtext">평균 가동률 80% 달성 시 (EBITDA 23.9억/연)</div>
        </div>
    </div>

    <div class="grid">
        <!-- 가동률 시뮬레이션 표 (Grid 12 중 7 차지) -->
        <div class="card col-8">
            <h2 class="report-section-title">가동률별 연간 상세 손익 시뮬레이션 (단위: 만원)</h2>
            <div class="table-responsive">
                <table>
                    <thead>
                        <tr>
                            <th>가동률</th>
                            <th>연간 총매출</th>
                            <th>MZC 수수료 (20%)</th>
                            <th>현금성 OpEx</th>
                            <th>연간 감가상각</th>
                            <th>영업이익 (상각후)</th>
                            <th>EBITDA (현금흐름)</th>
                        </tr>
                    </thead>
                    <tbody>
                        {table_rows}
                    </tbody>
                </table>
            </div>
        </div>

        <!-- 시뮬레이션 그래프 시각화 (Grid 12 중 4 차지) -->
        <div class="card col-4">
            <h2 class="report-section-title">재무 변동 분석 그래프</h2>
            <div class="chart-box">
                <!-- Base64 인코딩 이미지를 inline으로 로드 -->
                <img src="data:image/png;base64,{base64_chart}" alt="BEP 시뮬레이션 차트" />
            </div>
            <p style="font-size: 0.8rem; color: var(--text-muted); margin-top: 12px; text-align: center;">
                * 24% 가동 시 EBITDA 흑자 전환, 76% 가동 시 감가상각 포함 회계적 흑자 전환.
            </p>
        </div>

        <!-- 사업 구조 및 전략 설명 (Grid 12 전체 차지) -->
        <div class="card col-12">
            <h2 class="report-section-title">비즈니스 파트너십 아키텍처 (MZC - AKAMAI - NVIDIA)</h2>
            <div class="proposal-details">
                <div class="proposal-item">
                    <div class="proposal-item-title">1. 자산 일시 매입 (Asset Purchase)</div>
                    <p style="font-size: 0.92rem; color: var(--text-muted);">
                        국내의 심각한 GPU 수급 제약을 우회하기 위해, MZC가 기확보했거나 수급 파이프라인을 가진 GPU 하드웨어를 아카마이가 110억 원에 일시 매입(Buyout)합니다. MZC의 유동성 부담을 제로화하는 동시에 아카마이는 대기 시간 없이 즉시 자산을 인도받습니다.
                    </p>
                </div>
                <div class="proposal-item">
                    <div class="proposal-item-title">2. 위탁 운영 및 영업 (Operations & Sales Outsource)</div>
                    <p style="font-size: 0.92rem; color: var(--text-muted);">
                        한국 코로케이션 IDC 구축 후, 아카마이는 MZC에 고정 위탁 수수료(연 3.0억)를 지급하고 가상화 및 하드웨어 물리 관리를 24/7 위임합니다. 동시에 MZC는 국내 MSP 리더십을 활용해 영업 독점권을 가지고 아카마이 노드로 고객을 유치합니다.
                    </p>
                </div>
                <div class="proposal-item">
                    <div class="proposal-item-title">3. 트래픽 비용 우위성 & 매출 쉐어</div>
                    <p style="font-size: 0.92rem; color: var(--text-muted);">
                        Akamai Connected Cloud의 초저가 Egress 비용(초과 요금 기가바이트당 $0.005, 하이퍼스케일러 대비 16배 이상 저렴)을 무기로 패키지 판촉을 전개합니다. 매출의 20%를 MZC에 매출 연동 수수료로 배분하여 영업 마진 동기를 부여합니다.
                    </p>
                </div>
            </div>
        </div>

        <!-- 최종 의사결정 제언 -->
        <div class="card col-12">
            <h2 class="report-section-title">재무적 총평 및 회장 보고용 핵심 요약</h2>
            <ul>
                <li><strong>생존 임계치 극소화</strong>: 감가상각비를 제외한 현금 흐름 BEP 가동률이 단 <strong>23.93%</strong>에 불과합니다. 국내 스타트업 및 연구소 고객 중 중소규모 3~4개사만 유치해도 월간 운영 적자 리스크가 원천 소멸됩니다.</li>
                <li><strong>안정적인 투자금 회수</strong>: MZC의 적극적인 국내 세일즈를 바탕으로 가동률 80% 안착 시 약 4.6년, 90% 안착 시 약 3.9년의 짧은 투자금 회수 기간(EBITDA 누적 기준)을 가집니다.</li>
                <li><strong>독점적 가성비 우위</strong>: 아카마이의 강력한 네트워크 강점(Egress $0.005/GB)과 엔비디아 NIM 최적화를 통해 3대 퍼블릭 클라우드 대비 총소유비용(TCO)을 최대 50% 절감 가능하므로 로컬 영업 경쟁력이 확고합니다.</li>
                <li><strong>결론</strong>: MZC의 조달 파이프라인을 아카마이가 매입해 즉각 사업을 전개하고 영업/운영을 아웃소싱하는 하이브리드 모델은 신속성과 안전성, 그리고 수익성을 모두 갖춘 우수한 사업 기획안으로 판정됩니다.</li>
            </ul>
        </div>
    </div>

    <footer>
        <p>© 2026 AKAMAI CONNECTED CLOUD & MEGAZONE CLOUD FEASIBILITY STUDY GROUP. ALL RIGHTS RESERVED.</p>
    </footer>
</div>

</body>
</html>
"""
    
    # 4. HTML 파일 작성
    with open(html_output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
        
    print(f"성공: HTML 재무 보고서가 빌드되었습니다 -> {html_output_path}")
    
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
    generate_html_report()

