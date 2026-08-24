# VMware Migration Sales Offering Guide
## Nutanix Cloud Platform + Red Hat OpenShift 기반 하이브리드 클라우드 전환 전략

**작성**: 메가존클라우드(MZC) ISV/Hybrid Cloud BU  
**작성일**: 2026년 8월 24일  
**버전**: V2.0 (종합 세일즈 가이드)  
**분류**: 엔터프라이즈 세일즈 킷 & 고객 제안용

---

## Executive Summary

2023년 말 Broadcom의 VMware 인수 이후, 기존의 영구 라이선스 폐지, 소켓 단위에서 **물리 CPU 코어당 과금(최소 16코어 보장)**으로의 전환, 그리고 160여 개 SKU를 VCF/VVF의 2대 메가 번들로 강제 통폐합함에 따라 국내외 기업들의 가상화 라이선스 갱신 비용이 기존 대비 **2~5배(최대 7배)** 급증하고 있습니다.

메가존클라우드는 **Nutanix Cloud Platform(NCI/AHV/NC2)**과 **Red Hat OpenShift(OCP/OpenShift Virt./OpenShift AI)**를 결합하여 VMware 인프라 전체를 100% 대체하는 통합 오퍼링을 제공합니다. 
무상 제공되는 **Nutanix Move** 도구를 통해 에이전트리스 방식으로 10분 이내 무중단 컷오버를 실현하며, 소프트웨어 라이선스 비용 60~70% 절감, 5개년 누적 TCO 30~50% 실질 절감, 그리고 온프레미스 데이터 주권 100% 보호를 보장합니다.

---

## 0. 고객 및 시장 환경 분석 (Customer Context & Pain Points)

과거 국내 가상화 시장에서 VMware는 금융, 제조, 공공, 대기업 전반에 걸쳐 약 85~90%의 압도적인 점유율을 차지해 왔습니다. 그러나 Broadcom의 공격적인 가격 인상과 번들 강제화로 인해 2024~2026년 계약 갱신 시점을 맞이한 국내 기업의 40~60% 이상이 '탈(脫)VMware'를 경영진 핵심 과제로 지정하고 대안 플랫폼 도입을 긴급 추진하고 있습니다.

### 0.1 Broadcom 라이선스 정책 6대 변경 사항 비교

| 변경 항목 | 기존 (인수 전) | 현재 (Broadcom 정책) | 고객사 영향 및 Pain Points |
|-----------|---------------|---------------------|---------------------------|
| **라이선스 형태** | 영구 라이선스 (Perpetual) | 구독형 (Subscription) 강제 전환 | 소유권 상실, 구독료 미납 시 운영 중단 위험 |
| **과금 단위** | CPU 소켓(Socket) 단위 | 물리 CPU 코어(Core) 단위 (최소 16코어) | 최신 고밀도 서버(32~64 코어) 라이선스 비용 급증 |
| **제품 패키징** | 160여 개 개별 SKU 선택 | VCF / VVF 메가 번들 강제화 | 미사용 기능(vSAN, NSX 등) 강제 구매 (Shelfware) |
| **계약 기간** | 1, 3, 5년 유연 선택 | 3년 약정 기본화 | 예산 운용 경직성 및 대규모 일시 약정 부담 |
| **파트너 체계** | 다층 파트너 체계 | 파트너 티어 대폭 축소 | 기술 지원 공백 및 전담 엔지니어 부족 우려 |

---

## 1. VMware 제품군 개요 및 Shelfware 맹점 분석

Broadcom은 제품군을 VCF(풀스택 번들, 코어당 연 $100~$200+)와 VVF(경량 번들, 코어당 연 $50~$100) 단 두 가지만을 판매하고 있습니다. 
국내 대다수 엔터프라이즈는 이미 고성능 외장 SAN 스토리지를 운영 중임에도 불필요한 vSAN 소프트웨어 비용을 지불해야 하며, 물리 방화벽을 쓰면서도 복잡한 NSX 비용을 강제 지불해야 하는 심각한 **'Shelfware(미사용 잉여 기능 강매)'** 현상에 시달리고 있습니다.

---

## 2. Red Hat OpenShift & Nutanix 대체 영역 1:1 매핑

| VMware 컴포넌트 | VMware 기능 | Nutanix 대체 솔루션 | Red Hat 대체 솔루션 | 대체 도입 시 핵심 고객 이점 |
|----------------|-----------|-------------------|-------------------|---------------------------|
| **ESXi Hypervisor** | Type-1 하이퍼바이저 | **AHV (Acropolis)** | **KVM (OpenShift Virt.)** | **NCI 라이선스 내 AHV 무상 포함**, 중복 과금 제로화 |
| **vCenter** | VM 통합 관리 | **Prism Central** | **OpenShift Console + ACM** | 단일 콘솔에서 수천 개 VM 및 K8s 클러스터 통합 관제 |
| **vSAN** | HCI 분산 스토리지 | **DSF (Distributed Fabric)** | **ODF (Data Foundation)** | 인라인 중복제거/압축 기술로 스토리지 유효 용량 2~3배 확장 |
| **NSX** | SDN/마이크로세그멘테이션 | **Flow Network Security** | **OVN-Kubernetes + ACS** | 간편한 마이크로세그멘테이션으로 운영 공수 70% 절감 |
| **Tanzu** | K8s 배포/관리 | **NKP (Kubernetes Plat.)** | **OpenShift Container Plat.** | CNCF 완벽 호환 및 엔터프라이즈 DevSecOps 내장 |
| **VMware Cloud on AWS** | AWS 기반 관리형 VMware | **NC2 on AWS / Azure** | **ROSA / ARO** | 양방향 자유 마이그레이션, AWS Native AI(Bedrock) 즉시 연동 |
| **VMware Private AI** | AI/ML 인프라 | **NAI (Enterprise AI)** | **OpenShift AI (RHOAI)** | NVIDIA GPU 턴키 통합 및 사내 폐쇄망 LLM 서빙 |
| **HCX** | 무중단 마이그레이션 | **Nutanix Move (무상)** | **Red Hat MTV (무상)** | 에이전트리스 백그라운드 복제 후 10분 내 컷오버 |

---

## 3. 국내외 경쟁 가상화 및 클라우드 솔루션 심층 분석

- **Microsoft Azure Stack HCI / Azure Local**: Hyper-V 기반의 Azure 하이브리드 솔루션으로 Windows 라이선스 연계(AHB) 혜택은 있으나, Azure 계정 종속성이 강해 30일 이상 인터넷 단절 시 인증 문제가 발생(폐쇄망 도입 난항)하며 AWS/GCP 등 멀티클라우드 연동이 불가능합니다.
- **오케스트로 (Okestro) 콘트라베이스 (Contrabass)**: KVM/OpenStack 기반 국산 플랫폼으로 공공 보안 적합성(CC인증) 획득 및 국내 밀착 지원이 강점이나, 글로벌 CSP(AWS/Azure)와의 워크로드 양방향 이관 한계 및 글로벌 ISV(SAP HANA 등) 에코시스템이 부족합니다.
- **SUSE Harvester / Rancher**: KubeVirt 기반의 오픈소스 경량 HCI로 비용이 저렴하나, 스토리지 성숙도가 Nutanix DSF 대비 미흡하며 국내 대형 금융/제조 계정계 검증 레퍼런스가 부재합니다.
- **Proxmox VE (PVE)**: 오픈소스 무료 하이퍼바이저이나 24x7 엔터프라이즈 SLA 및 상용 백업 솔루션 생태계 부재로 미션 크리티컬 워크로드 적용 불가.

---

## 4. Target Industry & Account 공략 전략

- **제조 (Manufacturing)**: SAP S/4HANA 전환 시 RISE with SAP 대신 **SAP PCE CDC**(Customer Data Center) 프라이빗 클라우드 구성으로 데이터 주권 보호. (HD한국조선해양 사례: 30% 비용 절감)
- **금융 (Financial Services)**: 전자금융감독규정상 망분리 준수 및 계정계(온프레미스 AHV) + 정보계(NC2 on AWS) 하이브리드 연동, Data Lens 랜섬웨어 방어. (BNK금융그룹 사례: 90% 업무시스템 운영)
- **공공 (Public Sector)**: 단년도 예산 분산 구독형 도입 및 폐쇄망(Air-Gap) 소버린 AI 턴키 구현.
- **대기업/그룹사**: 공통 프라이빗 클라우드 통합 관리 및 성수기 트래픽 대응을 위한 NC2 Cloud Bursting. (에버랜드 사례: 국내 최초 도입)

---

## 5. 비용 구조 및 TCO 분석 (100 Core / 3개년 기준)

| 비용 분석 항목 | VMware VCF 유지 시 | Nutanix NCI 전환 시 | 비용 절감 효과 |
|---------------|-------------------|-------------------|---------------|
| **S/W 라이선스 및 구독료** | $204,000 (~2.75억 원) | $75,000 (~1.01억 원) | **63.2% 절감 ($129,000 절감)** |
| **하드웨어 유지보수 비용** | $45,000 | $45,000 | 동일 (기존 서버 재활용) |
| **마이그레이션 구축 비용 (1회)** | $0 | $30,000 (펀딩 시 $0) | 글로벌 파트너 펀딩 전액 감면 |
| **운영 및 인건비 (3개년)** | $150,000 | $120,000 | **20% 절감 (Prism 자동화)** |
| **3개년 총 TCO 합계** | **$399,000 (~5.38억 원)** | **$270,000 (~3.64억 원)** | **총 $129,000 (~1.74억 원 절감)** |

---

## 6. 참고 문헌 및 출처 (References & Sources)

1. Broadcom Inc., *VMware Cloud Foundation (VCF) and VMware vSphere Foundation (VVF) Packaging & Pricing Guide*, Official Whitepaper, 2024-2026.
2. Nutanix Inc., *Nutanix Cloud Platform vs. VMware vSphere TCO & Workload Migration Analysis Whitepaper*, 2025.
3. Red Hat Inc., *Red Hat OpenShift Virtualization: Migrating Virtual Machines to Cloud-Native Infrastructure*, Technical Guide, 2025.
4. Gartner Research, *Market Guide for Cloud-Native Infrastructure & Hyperconverged Platforms*, Gartner Report, 2025.
5. S-Core Insight, *국내 엔터프라이즈 가상화 시장 변화와 클라우드 네이티브 현대화 전략*, S-Core Consulting Report, 2024-2025.
6. ZDNet Korea & 디지털데일리, *Broadcom 인수 후 국내 가상화 대안 솔루션 도입 및 PoC 현황*, 2025.
7. MEGAZONECLOUD Corp., *Nutanix 기반 Hybrid Cloud Sales Offering Guide v1.4 & ISV Sales Playbook*, 2026.08.
