# [명세서] Liqid Composable GPU & Memory Pooling 기술 분석 및 MZC AI Full Stack / Private Cloud 총판 타당성 보고서

- **문서 번호**: SPEC-20260820-LIQID-01
- **작성 일자**: 2026-08-20
- **작성자**: MZC AI Full Stack 아키텍처 및 ISSU 프리세일즈 팀
- **대상 파일**:
  - `offering/2026-08-20_liqid_composable_gpu_memory_pooling_analysis.html` (독립 인터랙티브 웹 보고서)
  - `offering/generate_liqid_report_docx.py` (DOCX 생성기)
  - `offering/docx/2026-08-20_Liqid_Composable_GPU_Memory_Pooling_Analysis_Report.docx` (공식 Word 문서)
  - `docs/2026-08-20_Liqid_Composable_GPU_Memory_Pooling_Analysis_Report.docx` (루트 docs 동기화 문서)

---

## 1. 개요 및 ISSU 기본 배경 명시
1. **조직 정의**: ISSU(Integrated Solution Sales Unit)는 메가존클라우드의 **솔루션 세일즈(Solution Sales), 기술 영업 및 프리세일즈(Presales) 중심 조직**임.
2. **하드웨어 판매 구조**: H/W를 직접 제조/보유하지 않으며, **'세일즈 오퍼링(Offering)' 및 아키텍처 패키지 형태로 보유**함 (현재 AIDC 사업에 대하여 검토 중이나, 구체화된 내용은 없음). 실제 판매/납품은 **델(Dell)과 엔비디아(NVIDIA) 파트너를 통하여 이루어짐**.
3. **인프라 제약 조건**: 현재 ISSU 내부에는 하드웨어를 직접 설치하여 테스트할 수 있는 **자체 실증 Infra가 부재**한 상태임.

---

## 2. 보고서 핵심 분석 내용

### 제 1 장. ISSU 조직 배경 및 분석 기본 전제
- Solution Sales / Presales 중심 조직 성격, 파트너 H/W 판매 구조, 자체 실증 인프라 부재 조건 명시.

### 제 2 장. Liqid 핵심 기술 요약 (GPU & DRAM Disaggregation)
- **PCIe Gen5 패브릭 풀링**: 섀시당 10x GPU(최대 30x GPU), 섀시당 40TB DRAM(최대 200TB). Dell/HPE/Supermicro 등 기존 1U~4U 서버에 PCIe HIC 장착으로 100% 자산 보호.
- **Liqid Matrix SW**: 물리 케이블 재연결 없는 소프트웨어 정의 동적 자원 할당, Kubernetes/Slurm 플러그인, 과다 프로비저닝 75% 절감.
- **대용량 DRAM 풀 & KV Cache 가속**: 최대 200TB DRAM 공유로 90% KV Cache Hit Rate 달성 ➔ 재연산 제거로 7배 추론 가속.

### 제 3 장. NVIDIA NVL-72 vs Liqid PCIe-72 심층 비교 분석
- **코어당 비용**: NVL-72($2.21/Core) vs Liqid PCIe-72($0.31/Core ➔ 약 7배 우수).
- **전력 소모**: NVL-72(150kW 수랭식 필수) vs Liqid PCIe-72(60kW 공랭식 가능 ➔ 5배 전력 절감).
- **데이터센터**: 특수 신축 데이터센터 전용 vs 기존 기업 일반 전산실 즉시 구축 가능.

### 제 4 장. 엔터프라이즈 고가용성(HA) 및 PCIe/NTB 구조적 제약 · 성능 비교 (vs NVL / IB)
- **고가용성(HA) 및 SPOF 리스크**: Expansion Chassis 장애 시 다수 GPU/호스트 동시 중단 위험, PCIe 버스 단절 시 무중단 페일오버 한계(OS 커널 패닉/AER).
- **PCIe/NTB 구조적 확장성 제약**: 트리 구조 버스 열거 의존으로 인한 핫플러그 재할당 불안정성, 단일 섀시/Pod 랙 스케일 한계(멀티 랙은 네트워크 브릿징 필수).
- **상호연결 패브릭 성능 비교 (NVLink vs IB vs Liqid PCIe)**:
  - NVLink 5 (1.8 TB/s, ~100ns): Liqid 대비 대역폭 28배 ➔ 거대 모델 분산 사전학습/텐서 병렬화(TP) 필수.
  - InfiniBand (50~100 GB/s per Port, ~600ns~1µs): 멀티 노드 분산 클러스터링 표준.
  - Liqid PCIe Gen5 (~64 GB/s, ~200~400ns): ❌ 분산 학습 부적합, ✅ 독립 추론 서빙 및 DRAM KV Cache 가속 최적.

### 제 5 장. 엔터프라이즈 프라이빗 AI 하드웨어 토탈 패키지 제안 모델 (Turnkey Total Package)
- **제안 배경**: 개별 부품/단품 카드가 아닌 '서버+GPU+풀링섀시+스토리지+RHOAI' 결합 턴키 토탈 어플라이언스 랙으로 상품화.
- **토탈 패키지 BoM 및 수행 주체 매핑**:
  - 호스트 서버: Dell PowerEdge R760/R660 (Dual Xeon, 4~8 노드) ➔ 델 총판 파트너사 조달
  - 컴포저블 풀링: Liqid UltraStack PCIe Gen5 섀시 (1~2대, 최대 200TB DRAM) ➔ MZC ISSU 총판 + 파트너 랙 마운팅
  - GPU 가속기: NVIDIA RTX 6000 Ada (48GB) 또는 L40S PCIe 16~32대 ➔ 엔비디아 파트너사 공급
  - 사내 스토리지: Dell PowerScale / All-Flash NVMe (100TB~) ➔ 델 파트너사
  - 통합 S/W 플랫폼: Liqid Matrix SW + Red Hat OpenShift AI (RHOAI) + MZC 솔루션 ➔ MZC ISSU 통합 구축/SI
- **고객 가치**: 단일 42U 공랭식 랙 단위 턴키 공급, 전원 인가 즉시 운영, MZC 원스톱 단일 창구 SLA 제공.

### 제 6 장. 엔터프라이즈 비용 분석 및 신규 조직 셋업 BEP 시뮬레이션
- **CapEx vs S/W License vs OpEx 분석**: 호스트 서버 수 75% 감소, RHOAI 라이선스 50~75% 절감, 전력비 60% 절감.
- **3대 시나리오별 3개년 TCO 비교**:
  - [시나리오 A] NVIDIA NVL-72 턴키: 50억 원 이상 (수랭 설비 공사비 별도)
  - [시나리오 B] 전통적 8-GPU 고정형 서버 4대: 약 16~19억 원
  - [시나리오 C] MZC Composable AI 패키지: 약 10~12억 원 (전통적 방식 대비 약 35~40% TCO 절감)
- **신규 5인 전담 조직 셋업 비용 및 BEP 시뮬레이션**:
  - 전담 인력(5인) + 랩 운영비: 연간 고정비 약 7억 ~ 9억 원
  - 건당 순마진 약 4,000만 원 vs 국내 연간 수주 예상 1~2건 (연간 이익 6,000만 ~ 1억 원)
  - **예상 BEP 도달 기간: 최소 2.5년 ~ 3년 소요 (1년 내 회수 불가능)**
- **200여 가지 ISV 파트너 재평가 기준 적용 판정**:
  - 기술적 문제가 없더라도 **BEP가 1년 단위 이상 소요(2.5~3년)되는 신규 솔루션은 비즈니스 편입에 대해 부정적(No-Go)으로 판정**하며, 현재 Liqid는 **'단순 기술적 검토' 단계로 동결**.

### 제 7 장. MZC AI Full Stack 합류 및 Private Cloud 총판 사업 타당성 판단
- **솔루션 프레임워크 파편화 방지**: 기술적 가능성만으로 무분별 편입 시 표준 스택 파편화 및 엔지니어링 리스크 초래 ➔ 공인 파트너 지위를 보유한 **Dell / NVIDIA 표준 라인업 영업에 집중**.
- **총판 편입 허들(분기 100억 원) 미달 및 1년 BEP 불가에 따른 판정**: MZC 총판 사업 편입 기준(최소 분기 100억 원) 미달 및 2.5~3년의 긴 BEP로 인해 **'H/W 직접 총판 편입 불가(보류)'** 판정.
- **제한적 서드파티 연계 모델**: 특수 고객 요청 시에만 물리 섀시는 H/W 파트너가 납품하고 MZC는 S/W SI 및 기존 Dell/NVIDIA 서버 연계 매출로만 선별 대응.
- **내부 인프라 부재 대응**: 사내 물리 장비 도입 배제, Liqid 본사 Remote Cloud Lab 원격 검증 활용.

### 제 8 장. 종합 결론 및 전략적 의사결정 가이드라인
1. **현재 상태 규정: '단순 기술적 검토' 단계로 유지**: 기술적 가능성은 확인하였으나, BEP 1년 초과(2.5~3년) 및 전담 조직 셋업 부담으로 인해 **MZC 공식 솔루션 편입은 부정적(보류)으로 결론**
2. **Dell / NVIDIA 공인 총판 비즈니스 최우선 집중 (Core Business First)**: 솔루션 프레임워크 파편화를 방지하고, 메가존클라우드의 핵심 강점인 **Dell PowerEdge + NVIDIA 표준 엔터프라이즈 인프라 비즈니스에 전사 역량 집중**
3. **H/W 직접 핸들링 배제 원칙 준수**: 분기 100억 원 미달 및 재고·AS 리스크에 따라 Liqid 하드웨어 직접 총판/유통은 추진하지 않음

---

## 3. 검증 결과
- HTML 및 DOCX 파일 빌드 완료 (DOCX 크기 약 43.9 KB, HTML 크기 약 34.5 KB).
