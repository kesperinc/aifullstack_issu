import os
import matplotlib.pyplot as plt
import koreanize_matplotlib  # 한글 폰트 깨짐 방지를 위해 필수 사용

# 1. 고정 재무 상수 정의
CAPEX_H100 = 16 * 450_000_000        # H100 (8-Way HGX) 16대 매입: 72억 원
CAPEX_L40S = 32 * 100_000_000        # L40S (4-Way) 32대 매입: 32억 원
CAPEX_SETUP = 600_000_000            # 초기 IDC 구축 및 네트워크망 설정: 6억 원
TOTAL_CAPEX = CAPEX_H100 + CAPEX_L40S + CAPEX_SETUP # 총 CapEx: 110억 원

# 감가상각 설정 (하드웨어 5년 정액법, 잔존가치 0원 가정)
DEPRECIATION_PER_YEAR = TOTAL_CAPEX / 5.0 # 연간 22억 원 감가상각

# 연간 현금성 고정 운영비 (OpEx)
OPEX_IDC_POWER = 35_000_000 * 12     # IDC 임차 및 전력비: 연 4.2억 원
OPEX_NETWORK = 15_000_000 * 12       # 100Gbps 전용회선 요금: 연 1.8억 원
OPEX_MZC_OPS = 25_000_000 * 12       # MZC 위탁 운영 인력비: 연 3.0억 원
OPEX_MARKETING_MISC = 10_000_000 * 12 # 마케팅 및 기타 고정비: 연 1.2억 원
TOTAL_CASH_OPEX = OPEX_IDC_POWER + OPEX_NETWORK + OPEX_MZC_OPS + OPEX_MARKETING_MISC # 연간 총 현금성 OpEx: 10.2억 원

# 변동비 설정 (매출 연동 변동비)
MZC_REV_SHARE_RATE = 0.20            # MZC 영업 대행 수수료율: 매출의 20%

# 2. 가격 정책 및 최대 매출 한계 정의 (100% 가동 시)
# 환율 가정: 1 USD = 1,320 KRW
# H100 GPU 시간당 $2.50 책정 (8-Way 노드당 시간당 $20.00 -> 26,400원)
REVENUE_MAX_H100 = 16 * 8 * 2.50 * 1320 * 24 * 365 # H100 연간 최대 매출: 약 37.0억 원
# L40S GPU 시간당 $1.10 책정 (4-Way 노드당 시간당 $4.40 -> 5,808원)
REVENUE_MAX_L40S = 32 * 4 * 1.10 * 1320 * 24 * 365 # L40S 연간 최대 매출: 약 16.3억 원
TOTAL_MAX_REVENUE = REVENUE_MAX_H100 + REVENUE_MAX_L40S # 총 연간 최대 매출 한계: 약 53.3억 원

def run_simulation():
    utilization_rates = [x / 100.0 for x in range(10, 101, 10)]
    revenue_data = []
    opex_dep_data = []
    mzc_share_data = []
    operating_profit_data = [] # 영업이익 (감가상각 후)
    ebitda_data = []           # EBITDA (감가상각 전 현금흐름)

    print("=== 가동률별 연간 손익 시뮬레이션 결과 (단위: 만원) ===")
    print(f"{'가동률 (%)':<10} | {'연간 매출':<12} | {'MZC 수수료':<12} | {'현금 OpEx':<12} | {'감가상각':<12} | {'영업이익':<12} | {'EBITDA':<12}")
    print("-" * 100)

    bep_utilization = None

    for rate in utilization_rates:
        # 가동률에 따른 매출
        rev = TOTAL_MAX_REVENUE * rate
        # 가동률 연동 MZC 수수료 (매출의 20%)
        mzc_share = rev * MZC_REV_SHARE_RATE
        # 총 고정비 + 감가상각비
        total_fixed = TOTAL_CASH_OPEX + DEPRECIATION_PER_YEAR
        
        # 영업이익 = 매출 - MZC수수료 - (고정비 + 감가상각)
        op_profit = rev - mzc_share - total_fixed
        # EBITDA = 영업이익 + 감가상각
        ebitda = op_profit + DEPRECIATION_PER_YEAR

        revenue_data.append(rev / 10_000)
        mzc_share_data.append(mzc_share / 10_000)
        operating_profit_data.append(op_profit / 10_000)
        ebitda_data.append(ebitda / 10_000)

        # BEP(영업이익 0 돌파) 지점 탐색
        if op_profit >= 0 and bep_utilization is None:
            # 선형 보간을 통한 대략적인 BEP 가동률 계산
            prev_rate = rate - 0.1
            prev_rev = TOTAL_MAX_REVENUE * prev_rate
            prev_share = prev_rev * MZC_REV_SHARE_RATE
            prev_op = prev_rev - prev_share - total_fixed
            
            # 보간법 식: rate_bep = prev_rate + (0 - prev_op)/(op_profit - prev_op) * 0.1
            bep_utilization = prev_rate + (0.0 - prev_op) / (op_profit - prev_op) * 0.1

        print(f"{rate*100:9.0f}% | {rev/10000:10,.0f} | {mzc_share/10000:10,.0f} | {TOTAL_CASH_OPEX/10000:10,.0f} | {DEPRECIATION_PER_YEAR/10000:10,.0f} | {op_profit/10000:10,.0f} | {ebitda/10000:10,.0f}")

    if bep_utilization:
        print("-" * 100)
        print(f"★ 정량적 손익분기점(BEP) 가동률: {bep_utilization * 100:.2f}% (영업이익이 흑자로 전환하는 지점)")
        print(f"★ 현금흐름 기준 BEP(EBITDA > 0) 가동률: {(TOTAL_CASH_OPEX / (TOTAL_MAX_REVENUE * (1 - MZC_REV_SHARE_RATE))) * 100:.2f}%")
        print("-" * 100)

    # 3. 데이터 시각화 및 차트 저장 (Seaborn 테마 배제, Vanilla Matplotlib + koreanize-matplotlib 사용)
    plt.figure(figsize=(10, 6))
    x_labels = [f"{int(r*100)}%" for r in utilization_rates]
    
    plt.plot(x_labels, revenue_data, marker='o', label='연간 총매출', color='#1f77b4', linewidth=2)
    plt.plot(x_labels, operating_profit_data, marker='s', label='영업이익 (감가상각 후)', color='#d62728', linewidth=2)
    plt.plot(x_labels, ebitda_data, marker='^', label='EBITDA (현금흐름)', color='#2ca02c', linewidth=2)
    
    # BEP 제로 라인 표시
    plt.axhline(0, color='gray', linestyle='--', linewidth=1)
    
    if bep_utilization:
        bep_idx = int(bep_utilization * 10) - 1
        plt.annotate(f'BEP 가동률: {bep_utilization*100:.1f}%', 
                     xy=(bep_idx + 0.5, 0), 
                     xytext=(bep_idx - 1, 50000),
                     arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=6))

    plt.title('AKAMAI-MZC 공동 GPUaaS 가동률별 재무 시뮬레이션', fontsize=14, fontweight='bold', pad=15)
    plt.xlabel('GPU 인프라 연간 평균 가동률 (%)', fontsize=11, labelpad=10)
    plt.ylabel('금액 (단위: 만원)', fontsize=11, labelpad=10)
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend(loc='upper left', frameon=True, shadow=True)
    plt.tight_layout()

    # 결과 차트를 타당성 보고서 디렉토리에 저장
    output_dir = 'docs/feasibility'
    os.makedirs(output_dir, exist_ok=True)
    chart_path = os.path.join(output_dir, 'bep_chart.png')
    plt.savefig(chart_path, dpi=300)
    plt.close()
    print(f"시뮬레이션 차트가 성공적으로 저장되었습니다: {chart_path}")

if __name__ == '__main__':
    run_simulation()
