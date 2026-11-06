# NVIDIA DGX Spark 공식 OEM 제조사별 전수 비교·기술지원 체계 검토 보고서

* **발행 일자**: 2026년 9월 18일
* **문서 버전**: v2.0 (OEM 전수 검토 완결본)
* **대상 제품군**: NVIDIA DGX Spark 플랫폼 (GB10 Grace Blackwell Superchip 기반)
* **검토 대상 제조사**: NVIDIA Founders Edition 및 공식 OEM 7개사 (Dell, HP, Lenovo, ASUS, GIGABYTE, MSI, Acer)
* **검토 주관**: MEGAZONECLOUD Integrated Solution Sales Unit (ISSU)

---

## 💡 Executive Summary (핵심 요약)

1. **DGX Spark 동일 플랫폼 아키텍처**:
   - NVIDIA DGX Spark(Founders Edition) 및 7대 공식 OEM 파트너(Dell, HP, Lenovo, ASUS, GIGABYTE, MSI, Acer) 제품은 모두 동일한 **NVIDIA GB10 Grace Blackwell Superchip (20코어 Grace CPU + Blackwell GPU, 128GB LPDDR5x 통합 메모리, 1 PFLOPS FP4 AI 연산)** 레퍼런스 메인보드를 기반으로 합니다.
   - 따라서 로컬 대규모 언어 모델(LLM) 추론(최대 200B 파라미터) 및 경량 파인튜닝(약 70B 파라미터)의 기본 연산 성능과 DGX OS 환경은 제조사 간 대등합니다.

2. **도입 평가의 핵심 (기술지원 & 장애 대응 SLA)**:
   - 하드웨어 자체 성능이 동일하므로, 실제 구매 결정은 **① 국내 현장(On-site) 부품 지참 방문 엔지니어 조직 여부**, **② 장애 대응 SLA (24x7 4시간 현장 도착 vs NBD 익일 방문 vs 3~5일 센터 입고 수리)**, **③ 최대 5년 워런티 연장 보장성**, **④ NVIDIA AI Enterprise(NVAIE) 소프트웨어 기술지원 연계**에서 명확히 차별화됩니다.

3. **제조사별 3대 티어 분류**:
   - **엔터프라이즈 티어 (Dell, HP, Lenovo)**: 24x7 직영 지원, 4시간/익일 On-site 방문, 최대 5년 보증 (기업 핵심 연구 서버 1순위)
   - **NVIDIA 순정 티어 (Founders Edition)**: DGX OS 최신 기능 0-Day 최우선 반영, 공인 총판 전문 기술지원 연계
   - **가성비/보급 티어 (ASUS, GIGABYTE, MSI, Acer)**: 경제적 도입 단가, 책상 위 1인 1대 대량 배포 최적, 센터 입고/선출고 교체 중심

---

## 1. 제안 가능한 공식 제조사 라인업 (8개사)

| 제조사 구분 | 모델명 / 브랜드 | 폼팩터 | 주요 포지셔닝 및 핵심 특징 |
| :--- | :--- | :--- | :--- |
| **NVIDIA** | **DGX Spark (Founders Edition)** | 콤팩트 데스크톱 (~1.2kg) | NVIDIA 순정 레퍼런스 모델. 최신 DGX OS 및 NGC 스택 최우선 반영 |
| **Dell Technologies** | **Dell Pro Max GB10** | 콤팩트 데스크톱 (Micro) | 엔터프라이즈 내구성 설계, 전국 24x7 4시간 온사이트 ProSupport Plus 지원 |
| **HP (HPE)** | **ZGX Nano AI Station (G1n)** | 콤팩트 데스크톱 | Z-Workstation 노하우 기반 저소음 쿨링 설계, HP Care Pack 서비스 |
| **Lenovo** | **ThinkStation PGX** | 콤팩트 데스크톱 | 엔터프라이즈 워크스테이션 신뢰성, Lenovo Premier Support (NBD 방문) |
| **ASUS** | **Ascent GX10** | 초소형 데스크톱 (1.48kg) | 초소형 경량화, ConnectX-7 기본 강조, 디자인 어워드 수상, 가성비 우수 |
| **GIGABYTE** | **AI TOP ATOM** | 콤팩트 데스크톱 | 기가바이트 독자 AI TOP 유틸리티 탑재, 초보자용 로컬 파인튜닝 GUI 제공 |
| **MSI** | **EdgeXpert** | 초소형 데스크톱 (151x151mm) | 고밀도 구리 히트파이프, 뛰어난 가격대비성능, 연구원 대량 보급 최적 |
| **Acer** | **Veriton GN100 AI Mini** | 콤팩트 데스크톱 | 실용적인 Veriton 비즈니스 외장, 합리적인 도입 단가, 교육/실습 최적 |

---

## 2. 제조사별 주요 차별화 포인트 비교

| 제조사 | 하드웨어 및 쿨링 구성 | 확장성 및 네트워킹 | 관리 기능 (Management) | 안정성 및 운영 측면 |
| :--- | :--- | :--- | :--- | :--- |
| **NVIDIA (FE)** | 콤팩트 레퍼런스(~1.2kg), 외장 어댑터, 순정 히트싱크 | 10GbE + ConnectX-7, 2대 연결 시 405B 구동 | Base Command Agent, DGX OS 기본, NVML 모니터링 | 레퍼런스 표준 안정성, 0-Day 최신 펌웨어 즉시 반영 |
| **Dell** | 고내구성 Micro 섀시, Dell 독자 쿨링 챔버 | 10GbE, Wi-Fi 7, 켄싱턴 락, 마운팅 키트 | SupportAssist 원격진단, OpenManage 엔터프라이즈 | 24x7 번인 검증, 전국 부품망 기반 최고 가동률 |
| **HP (HPE)** | Z-Workstation급 방열, 오피스 저소음 최적화 | 10GbE, Wi-Fi 7, 멀티 DP 출력, 고속 스토리지 | HP Anyware 원격제어, Wolf Security 보안 | 소음에 민감한 개인 연구원 룸 및 오픈 오피스 적합 |
| **Lenovo** | ThinkStation 표준 섀시, 듀얼 챔버 방열 설계 | 10GbE, Wi-Fi 7, USB-C, 2대 클러스터링 | Commercial Vantage, ThinkShield 시스템 보안 | 기업 표준 PC/워크스테이션 자산 관리 정책과 100% 통합 |
| **ASUS** | 150x150x51mm 초소형 (1.48kg), 핀배열 공랭 | 10GbE + ConnectX-7 기본, 초고속 대역폭 | ASUS Control Center(ACC), 웹/모바일 진단 | 책상 위 공간 점유 극소화, 하드웨어 마감 우수 |
| **GIGABYTE** | 메탈 콤팩트 섀시, 고풍량 저소음 팬, 구리 베이스 | 10GbE, Wi-Fi 7, ConnectX-7 지원 | **GIGABYTE AI TOP Utility (GUI 파인튜닝)** | 초보 개발자도 GUI 환경에서 즉시 튜닝 가능 |
| **MSI** | 151x151x52mm 미니 섀시, 구리 히트파이프 | 10GbE, Wi-Fi 7, ConnectX-7 지원 (듀얼) | MSI Center Pro for AI, 하드웨어 진단 | 뛰어난 가성비, 1인 1대 대량 보급 최적 |
| **Acer** | 실용적 Veriton 비즈니스 외장, 표준 저소음 공랭 | 10GbE, Wi-Fi 7, ConnectX-7 지원 | Acer ControlCenter, 시스템 백업/복구 지원 | 도입 비용이 가장 저렴, 산학 과제 및 실습 최적 |

---

## 3. 제조사별 워런티 정책 비교

| 제조사 | 기본 워런티 기간 | 워런티 연장 가능 여부 | 보증 적용 범위 및 NVAIE 소프트웨어 연계 | 엔터프라이즈 적합도 |
| :--- | :--- | :--- | :--- | :--- |
| **Dell** | **기본 3년 ProSupport** | **최대 5년 보장** (도입 시 번들) | HW 전 부품 100% 무상 교체 및 온사이트 공임 포함, NVAIE 번들 | **최상 (5년 보장)** |
| **HP (HPE)** | **기본 3년 Care Pack** | **최대 5년 연장 가능** | HW 전 부품 방문 교체 지원, NVAIE 별도 연계 | **최상 (5년 보장)** |
| **Lenovo** | **기본 3년 Premier** | **최대 5년 연장 가능** | HW 전 부품 무상 방문 수리, 전담 기술 관리자, NVAIE 연계 | **최상 (5년 보장)** |
| **NVIDIA (FE)** | 1년 또는 3년 지정 | 연 단위 갱신 (최대 5년) | HW 무상 수리/교체 + **NVIDIA AI Enterprise 직영 연계** | **상 (SW 직통)** |
| **ASUS** | 기본 1년 ~ 3년 | 최대 3~5년 (B2B 계약) | HW 본체 무상 수리 (센터 입고 기준, 온사이트 별도) | **중 (계약 옵션)** |
| **GIGABYTE** | 기본 1년 ~ 3년 | 최대 3년 (총판 협의) | HW 부품 수리/교체 (센터 입고 기준), AI TOP 지원 | **중 (가성비 중심)** |
| **MSI** | 기본 1년 ~ 3년 | 최대 3년 (협의 시 5년) | HW 부품 수리/교체 (센터 입고 기준), DGX OS 부팅 보장 | **중 (가성비 중심)** |
| **Acer** | 기본 1년 ~ 3년 | 최대 3년 (B2B 패키지) | HW 본체 수리 (서비스센터 입고/택배), 교육용 특약 | **중 (가성비 중심)** |

---

## 4. 기술지원 체계 및 장애 대응 SLA 프로세스

```
[Tier 1: 엔터프라이즈 직영 On-site (Dell, HP, Lenovo)]
고객 접수 (24x7 콜센터) ➔ 전문 엔지니어 1차 원격 진단 ➔ 국내 물류 부품 출고 & 공인 엔지니어 동시 출동 (4시간 이내 / NBD) ➔ 현장 부품 교체 완결

[Tier 2: NVIDIA 직영 포털 & 총판 연계 (Founders Edition)]
고객 접수 ➔ 1차 공인 파트너 점검 ➔ NVIDIA Enterprise Support Portal 티켓 오픈 ➔ NVIDIA 본사 엔지니어 원격 진단 ➔ 국내 총판 버퍼 재고 맞교환 파견

[Tier 3: 유통 총판 / 공인 서비스센터 (ASUS, GIGABYTE, MSI, Acer)]
고객 접수 ➔ 1차 공급사 점검 ➔ 공인 서비스센터 입고 또는 택배 접수 ➔ 센터 수리 또는 선출고 RMA 교체 (3~5영업일 소요) ➔ 고객사 재배송
```

| 제조사 | 원격 기술지원 | 현장 방문 (On-site) | 부품 조달 방식 | 장애 대응 SLA |
| :--- | :--- | :--- | :--- | :--- |
| **Dell** | **24x7x365 한국어 직통** | **전국 Dell 공인 엔지니어 현장 방문 기본** | 서울/수도권 대형 통합 부품 물류센터 직접 지참 | **ProSupport Plus: 4시간 이내 현장 도착**, 일반 NBD |
| **HP (HPE)** | 24x7 또는 주간 전문 엔지니어 | **전국 HP 공인망을 통한 현장 방문 지원** | 국내 HP 공식 파츠 물류망 조달 | 익일(NBD) 현장 방문 수리 원칙, 4시간 옵션 |
| **Lenovo** | **24x7 Premier 직통** | **전국 Lenovo 공인 엔지니어 현장 방문 기본** | 국내 Lenovo 파츠 센터 직배송 | 익일(NBD) 현장 방문 수리, 전담 기술 큐 |
| **NVIDIA (FE)** | 24x7 글로벌 포털 티켓팅 | 국내 공인 총판(MDS테크 등) 엔지니어 방문 | 국내 총판 버퍼 재고 (소진 시 해외 RMA) | 원격 2~4시간 이내 응답, 부품 보유 시 익일 |
| **ASUS** | ASUS B2B 헬프데스크 주간 | 기본 입고 수리 (특약 시 온사이트 가능) | 국내 센터 재고 또는 대만 본사 RMA | 입고 후 3~5영업일 이내 (결품 시 지연) |
| **GIGABYTE** | 기가바이트 고객센터 주간 | 기본 서비스센터 입고 수리 | 국내 총판사(피씨디렉트 등) 보유 부품 | 입고 후 3~5영업일 이내 처리 |
| **MSI** | MSI 코리아 고객센터 주간 | 기본 서비스센터 입고/택배 수리 | MSI 코리아 서비스센터 보유 부품 | 입고 후 3~5영업일 이내 처리 |
| **Acer** | 에이서 코리아 고객지원센터 주간 | 기본 서비스센터 입고/택배 수리 | 국내 공인 서비스망 보유 재고 | 입고 후 3~5영업일 이내 처리 |

---

## 5. 국내 기술지원 조직 보유 현황 및 평가

1. **Dell 코리아 (평가: ★ 5.0 - 최상)**:
   - 국내 직영 엔터프라이즈 본부, 전국 시/도 파트너망, 수도권 대형 부품 물류 허브 운영.
   - 단일 벤더 계약으로 하드웨어 4시간 현장 출동 및 ProSupport 체계를 완비하여 **엔터프라이즈 운영 리스크가 가장 낮음**.
2. **HPE / HP 코리아 (평가: ★ 4.8 - 최상)**:
   - HP 코리아 본사 워크스테이션 전문 엔지니어링, 전국 거점 서비스 센터망 운영. 오피스 환경에서 신뢰성이 검증됨.
3. **Lenovo 코리아 (평가: ★ 4.7 - 최상)**:
   - 한국레노버 엔터프라이즈 서비스 본부 및 전국 Premier 지원망. 전담 기술 계정 관리자 지원.
4. **NVIDIA Founders Edition (평가: ★ 4.4 - 우수)**:
   - 최신 AI SW(NGC, Triton, TensorRT) 직통 지원 탁월, 순수 HW 교체는 국내 공인 총판(MDS테크 등)에 의존.
5. **ASUS / GIGABYTE / MSI / Acer (평가: ★ 3.5~3.8 - 양호)**:
   - 하드웨어 가성비가 가장 뛰어나며, 제품 결함 시 센터 입고 및 1:1 교체 위주로 지원. 개인 개발자 배포에 적합.

---

## 6. 고객 맞춤형 추천 권고안 (Decision Guide)

* **[추천 1] 엔터프라이즈 무중단 1순위 (24x7 4시간 현장 출동 SLA & 최대 5년 보증)**
  👉 **`Dell Pro Max GB10` (또는 HP ZGX / Lenovo PGX)**  
  *(전산실/핵심 개발용, Dell ProSupport Plus 4시간 현장 도착, 최대 5년 보증)*

* **[추천 2] 순정 AI 소프트웨어 스택 최우선 반영 및 레퍼런스 검증**
  👉 **`NVIDIA DGX Spark (Founders Edition)`**  
  *(DGX OS 및 NGC 스택 0-Day 반영, NVIDIA 직영 포털 티켓팅 연계)*

* **[추천 3] 초보자 친화적 원클릭 로컬 파인튜닝 & 직관적 워크플로우**
  👉 **`GIGABYTE AI TOP ATOM`**  
  *(AI TOP 전용 GUI 유틸리티로 직관적 모델 튜닝 및 추론 제어)*

* **[추천 4] 연구원 1인 1대 대량 배포 & 예산 절감 극대화**
  👉 **`MSI EdgeXpert`, `ASUS Ascent GX10`, `Acer Veriton GN100`**  
  *(초소형 폼팩터, 동일 GB10 연산 성능, 경제적인 도입 단가로 대량 배포 최적)*

---
* 관련 파일 링크:
  - HTML 보고서: [docs/2026-09-18_nvidia_dgx_spark_oem_comparison_report.html](file:///c:/dev/antigravity-workspace/aifullstack/docs/2026-09-18_nvidia_dgx_spark_oem_comparison_report.html)
  - Word(DOCX) 보고서: [docs/2026-09-18_nvidia_dgx_spark_oem_comparison_report.docx](file:///c:/dev/antigravity-workspace/aifullstack/docs/2026-09-18_nvidia_dgx_spark_oem_comparison_report.docx)
