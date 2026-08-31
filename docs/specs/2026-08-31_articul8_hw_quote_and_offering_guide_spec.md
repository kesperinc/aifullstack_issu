# 2026-08-31 Articul8 및 쿠팡 HW 실측 견적 반영 명세서 (Specs)

## 1. 개요 (Overview)
본 명세서는 Articul8 산출물 폴더 내 실측 서버 견적서(`MZ_SY_260828_008-AI Full Stack 서버 견적 건.xlsx`) 및 쿠팡 제안 견적서(`견적서_260731_1_메가존클라우드(쿠팡)_PowerEdge XE9780.xlsx`)의 데이터를 AI Fullstack Offering Guide 및 주요 오퍼링 문서에 반영하기 위한 명세입니다.

---

## 2. 변경 일자별 파일 수정 맵 (Specs Map)

| 변경 일자 | 수정 대상 파일 | 주요 변경 내용 |
|---|---|---|
| 2026-08-31 | `offering/mzc_ai_fullstack_strategy_service_report.html` | Option 01(Small), Option 02(Medium), Option 03(Large) 사양 및 실측 견적 금액 업데이트 |
| 2026-08-31 | `offering/generate_strategy_service_report_docx.py` | DOCX 생성 파이썬 코드 내 Option 01~03 하드웨어 사양 및 견적 금액 업데이트 |
| 2026-08-31 | `offering/articul8_ai_package_proposal.html` | Articul8 솔루션 패키지 제안서 내 H/W 금액 실측 견적 반영 |
| 2026-08-31 | `docs/specs/2026-08-31_articul8_hw_quote_and_offering_guide_spec.md` | 본 명세서 신규 생성 |

---

## 3. 세부 하드웨어 견적 반영 데이터 (Hardware Specifications & Prices)

### 3.1 Option 01 (Small 티어 / 팀·스타트업)
* **대상 규모**: 50인 이하 조직 / 개발팀 / 코딩 에이전트 전용 PoC
* **하드웨어 구성 및 GPU 단가**:
  * **RTX 6000 Ada (48GB)**: 단품 카드당 약 **1,250만 원**
  * **RTX PRO 6000 Blackwell (96GB)**: 단품 카드당 약 **2,600만 원**
* **서버 패키지 예상가 (Dell PowerEdge R760/R770 + 2x GPU)**:
  * **사양 A (RTX 6000 Ada x2)**: 서버 본체 (~2,000만 원) + 2x Ada (2,500만 원) -> **약 4,500만 원** (VRAM 96GB)
  * **사양 B (RTX PRO 6000 Blackwell x2)**: 서버 본체 (~2,200만 원) + 2x Blackwell (5,200만 원) -> **약 7,400만 원** (VRAM 192GB)
* **예상 H/W 가격**: **약 4,500만 ~ 7,400만 원**

### 3.2 Option 02 (Medium 티어 / Articul8 + 코딩 에이전트 실측 반영)
* **대상 규모**: 50~200인 중견기업 / 사업부 / Articul8 + 코딩 에이전트
* **H/W 제안 가격 범위**: **약 5억 1,500만 ~ 8억 1,800만 원 (51,500만 ~ 81,800만 원)**
* **하드웨어 구성 및 3가지 최적화 방안 (Appendix 반영)**:
  1. **Full HA 풀 패키지 (기준가 8억 1,793만 원)**: Bastion 1대(R570) + OpenShift Compact 3대(R770) + GPU Worker 1대(XE7740 4x H200 NVL)
  2. **방안 1: SNO 1-Server 통합 (5억 1,385만 원 / 3.04억 원 절감)**: Single Node OpenShift로 GPU 서버 1대에 Control/Bastion/Articul8 통합
  3. **방안 2: 사내 VM 활용 (5억 1,385만 원 / 3.04억 원 절감)**: 사내 기존 vSphere/Nutanix VM으로 Control 3대 + Bastion 구성 및 GPU 서버 1대 연동
  4. **방안 3: Control 노드 다운사이징 (6억 1,885만 원 / 1.99억 원 절감)**: Bastion VM 대체 및 Control 노드를 R570 에센셜 3대로 경량화

### 3.3 Option 03 (Large 티어 / 전사·엔터프라이즈 AI Factory 쿠팡 실측 반영)
* **대상 규모**: 200~500인 이상 전사 규모 / 제조·MRO·금융 복합 워크로드
* **쿠팡 실측 하드웨어 구성 (`PowerEdge XE9780`)**:
  * Dell PowerEdge XE9780 10U (HGX B300 NVL8 SXM5 8-GPU 공랭식, 4TB RAM, 8x 3.84TB NVMe, BlueField-3 400GbE DPU x2)
  * **1대 제안가**: **2,285,901,000 원 (22억 8,590만 원, VAT 별도)**
  * **2대 제안가**: **4,571,802,000 원 (45억 7,180만 원, VAT 별도)** / VAT 포함 50.28억 원
* **기종별 H/W 단가 산정**:
  * 8x H100 80GB (XE9680): 1대당 **약 7.5억 ~ 9.5억 원**
  * 8x H200 141GB (XE9680): 1대당 **약 9.5억 ~ 12.5억 원**
  * 8x B200/B300 NVL8 (XE9780): 1대당 **약 15억 ~ 23억 원** (실측 22.86억 원)
* **예상 H/W 패키지 구축가**: **약 15억 ~ 30억+ 원** (클러스터 랙 및 PowerScale NVMe 스토리지 연동)
