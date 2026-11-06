# 2026-08-31 Articul8 & 쿠팡 HW 실측 견적 반영 및 AI Fullstack Offering 최신화 인수인계 보고서 (Handover Report)

## 1. 개요 및 인수인계 배경 (Overview & Background)

본 보고서는 Articul8(A8) 산출물 폴더 내 실측 서버 견적서(`MZ_SY_260828_008-AI Full Stack 서버 견적 건.xlsx`) 및 쿠팡 제안 견적서(`견적서_260731_1_메가존클라우드(쿠팡)_PowerEdge XE9780.xlsx`)의 실측 데이터와 시장 가격 조사를 바탕으로 **MZC AI Fullstack Offering Guide** 및 주요 오퍼링 보고서를 최신화하고 다른 시스템/팀에서 즉시 활용할 수 있도록 작성된 핸드오버 문서입니다.

* **작업 수행 일자**: 2026-08-31
* **주요 목적**:
  1. Articul8 실측 견적가 및 쿠팡 PowerEdge XE9780 제안가를 오퍼링 가이드에 완벽 반영
  2. NVIDIA RTX 6000 Ada 및 RTX PRO 6000 Blackwell GPU의 단품 카드 단가 반영
  3. Option 02 (Medium 티어) Bastion 및 OpenShift Control 노드 다이어트를 통한 3가지 H/W 비용 절감 방안 부록(Appendix) 신규 구성
  4. HTML 오퍼링 보고서 및 파이썬 DOCX 자동 생성 파이프라인 수치 동기화 및 문서 재발급

---

## 2. 오퍼링 티어별 최종 하드웨어 사양 및 가격 정의 (Tier Specs & Pricing)

### 2.1 Option 01 (Small 티어 / 팀·스타트업 2x GPU 구성)
* **권장 대상**: 50인 이하 조직 / 개발팀 / 코딩 에이전트 전용 PoC
* **GPU 카드 시장 단가**:
  * **NVIDIA RTX 6000 Ada (48GB GDDR6)**: 단품 카드당 약 **1,250만 원**
  * **NVIDIA RTX PRO 6000 Blackwell (96GB GDDR7)**: 단품 카드당 약 **2,600만 원**
* **서버 패키지 예상가 (Dell PowerEdge R760/R770 본체 + 2x GPU)**:
  * **사양 A (2x RTX 6000 Ada 96GB VRAM)**: 서버 본체 (~2,000만 원) + GPU 2개 (2,500만 원) = **약 4,500만 원**
  * **사양 B (2x RTX PRO 6000 Blackwell 192GB VRAM)**: 서버 본체 (~2,200만 원) + GPU 2개 (5,200만 원) = **약 7,400만 원**
* **최종 표기 가격**: **약 4,500만 ~ 7,400만 원 (VAT 별도)**

### 2.2 Option 02 (Medium 티어 / Articul8 + 코딩 에이전트)
* **권장 대상**: 50~200인 중견기업 / 사업부 / Articul8 + 코딩 에이전트
* **하드웨어 구성 선택 범위**:
  * **최소 사양 (SNO 단일 물리 서버 / 사내 기존 VM 연동)**: Dell PowerEdge XE7740 (4x H200 NVL) 1대 -> **5억 1,385만 원**
  * **풀 사양 (Full HA 5-Server 풀 패키지)**: Bastion 1대 + Compact 3대 + GPU Worker 1대 -> **8억 1,793만 원 (VAT 별도) / 8억 9,972만 원 (VAT 포함)**
* **최종 표기 가격**: **약 5억 1,500만 ~ 8억 1,800만 원 (51,500만 ~ 81,800만 원, VAT 별도)**

### 2.3 Option 03 (Large 티어 / 대기업·전사 AI Factory 쿠팡 실측가)
* **권장 대상**: 200~500인 이상 전사 규모 / 제조·MRO·금융 복합 워크로드
* **쿠팡 실측 데이터 (`Dell PowerEdge XE9780`)**:
  * Dell PowerEdge XE9780 10U (HGX B300 NVL8 SXM5 8-GPU 공랭식, 4TB RAM, BlueField-3 400GbE DPU x2)
  * **쿠팡 1대 제안가**: **2,285,901,000 원 (22억 8,590만 원, VAT 별도)**
  * **쿠팡 2대 제안 총액**: **4,571,802,000 원 (45억 7,180만 원, VAT 별도)** / VAT 포함 **50.28억 원**
* **기종별 1대당 단가 범주**:
  * 8x H100 80GB (XE9680): 1대당 **약 7.5억 ~ 9.5억 원**
  * 8x H200 141GB (XE9680): 1대당 **약 9.5억 ~ 12.5억 원**
  * 8x Blackwell B200/B300 NVL8 (XE9780): 1대당 **약 15억 ~ 23억 원** (실측 제안가 22.86억 원)
* **최종 표기 가격**: **약 15억 ~ 30억+ 원 / 랙 (VAT 별도)**

---

## 3. Option 02 하드웨어 구성 다이어트 3가지 방안 (부록 반영)

| 구분 옵션 | 물리 서버 구성 사양 | H/W 견적가 (VAT 별도) | 비용 절감액 | 특징 및 권장 적용 워크로드 |
|---|---|---|---|---|
| **기준: Full HA 구성 (풀 패키지)** | Dell XE7740 (4x H200) 1대<br>Dell R770 Compact 3대<br>Dell R570 Bastion 1대 (총 5대) | **8억 1,793만 원<br>(81,793만 원)** | 기준가 (0원) | • 24x7 미션 크리티컬 무중단 서비스<br>• Control Plane 물리 완전 이중화 |
| **방안 1: SNO 통합 (1-Server) ★추천** | **Dell XE7740 1대 단일 물리서버**<br>Single Node OpenShift (SNO)<br>RHOAI + Articul8 + Bastion 통합 | **5억 1,385만 원<br>(51,385만 원)** | **▼ 3억 408만 원 절감<br>(37%↓ 절감)** | • **Small-Start / PoC / 초가성비 구축**<br>• 4U 소형화, 랙 공간 및 전력 최소화 |
| **방안 2: 사내 VM 활용 (Virtual Control)** | Dell XE7740 (4x H200) 1대<br>**고객사 기존 VM (vSphere/Nutanix)**<br>Control VM 3대 + Bastion VM 1대 | **5억 1,385만 원<br>(51,385만 원)** | **▼ 3억 408만 원 절감<br>(37%↓ 절감)** | • **기존 가상화 인프라 보유 고객사**<br>• H/W 신규구매 최소화 + SW HA |
| **방안 3: Control 노드 다운사이징** | Dell XE7740 (4x H200) 1대<br>**Dell R570 에센셜 3대 (Control)**<br>Bastion 사내 VM 대체 (총 4대) | **6억 1,885만 원<br>(61,885만 원)** | **▼ 1억 9,908만 원 절감<br>(24%↓ 절감)** | • Control 물리 노드 분리 유지<br>• 제온 서버 축소로 비용 다이어트 |

---

## 4. 변경된 파일 맵 및 시스템 자산 현황 (Specs Map)

| 번호 | 변경 파일 경로 | 주요 수정 및 반영 내역 |
|---|---|---|
| 1 | `offering/mzc_ai_fullstack_strategy_service_report.html` | Section 05 표기 수정 (Option 01: 4.5천~7.4천만 원, Option 02: 5.15억~8.18억 원, Option 03: 15억~30억+ 원) 및 **Appendix 부록 섹션 추가** |
| 2 | `offering/generate_strategy_service_report_docx.py` | 파이썬 DOCX 생성 코드 내 `sizing_data` 튜플 및 Appendix 자동 생성 함수 반영 |
| 3 | `offering/docx/2026-08-20_MZC_AI_Fullstack_Strategy_Service_Report.docx` | DOCX 파이프라인 자동 생성 보고서 최종본 (58.0 KB) |
| 4 | `docs/2026-08-20_MZC_AI_Fullstack_Strategy_Service_Report.docx` | 문서 동기화용 DOCX 최신본 (58.0 KB) |
| 5 | `offering/articul8_ai_package_proposal.html` | Articul8 제안서 테이블 내 HW CAPEX 51,500만 ~ 81,800만 원 최신화 |
| 6 | `docs/specs/2026-08-31_articul8_hw_quote_and_offering_guide_spec.md` | 본 작업에 대한 1:1:1 작업 트라이어드 Specs 명세서 |
| 7 | `docs/2026-08-31_articul8_hw_quote_and_offering_refinement_handover.md` | 본 핸드오버 인수인계 보고서 |

---

## 5. 다른 시스템 및 팀 연동/활용 가이드 (System Integration Guide)

1. **영업/제안 팀 활용**:
   - `offering/mzc_ai_fullstack_strategy_service_report.html` 파일 및 `offering/docx/2026-08-20_MZC_AI_Fullstack_Strategy_Service_Report.docx` 파일을 수주 제안 시 표준 오퍼링 가이드로 제시.
   - Articul8 제안 시 고객 예산에 따라 **부록(Appendix)** 표를 활용하여 **SNO 5.15억 원 방안**부터 **Full HA 8.18억 원 방안**까지 맞춤 제안.

2. **자동화 DOCX 스크립트 실행 방법**:
   ```bash
   python c:\dev\antigravity-workspace\aifullstack\offering\generate_strategy_service_report_docx.py
   ```
   - 스크립트를 실행하면 `offering/docx/` 및 `docs/` 디렉터리에 보고서 DOCX 파일이 자동 재생성됩니다.

3. **Git 저장소 동기화**:
   - 본 작업 내역은 Git `main` 브랜치에 승인 완료된 커밋으로 기록되며 원격 저장소에 푸시됩니다.
