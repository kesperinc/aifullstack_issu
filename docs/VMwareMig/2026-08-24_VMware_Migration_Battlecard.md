# VMware Migration Battlecard
## 메가존클라우드 (MZC) — 영업 1-Page 요약

**버전**: V1.0 | **작성일**: 2026-08-24 | **대상**: ISV/Hybrid Cloud BU 영업팀

---

## 한 줄 가치 제안

> **"Broadcom 이후 VMware 비용이 3~7배 폭등하셨나요?**  
> Nutanix AHV로 기존 VM을 그대로 이전하고, Red Hat OpenShift로 AI·컨테이너 플랫폼을 확보하세요.  
> 5년 TCO 30~50% 절감 + 데이터 주권 유지 + AI 현대화 — 메가존클라우드가 검증된 마이그레이션으로 함께합니다."

---

## Broadcom VMware 변경 사항 (3줄 요약)

1. 영구 라이선스(Perpetual) 폐지 → 3년 구독(Subscription) 강제 전환
2. CPU 소켓 단위 과금 → 코어 단위(최소 16코어) 과금으로 2~5배 비용 폭증
3. 160여 개 단품 → VCF/VVF 2개 번들 강제 통합 (불필요 기능 강매)

---

## 대체 솔루션 핵심 매핑

| VMware | Nutanix 대체 | Red Hat 대체 |
|--------|------------|-------------|
| ESXi (하이퍼바이저) | AHV (NCI 내장, 무료) | KVM (OpenShift Virt.) |
| vSAN (스토리지) | DSF (NCI 내장, 무료) | ODF |
| NSX (네트워크/보안) | Flow Network Security | OVN-K8s + ACS |
| vCenter (관리) | Prism Central | ACM + OpenShift Console |
| Tanzu (K8s) | NKP | Red Hat OCP |
| VMC on AWS | NC2 on AWS / Azure | ROSA |
| VMware Private AI | NAI / GPT-in-a-Box | OpenShift AI (RHOAI) |
| HCX (마이그레이션) | Nutanix Move (무료) | Red Hat MTV |

---

## 3가지 대체 시나리오

| 시나리오 | 대상 고객 | 핵심 제안 |
|---------|---------|---------|
| A: 인프라 교체 | VM만 운영 중인 기업 | VMware → Nutanix NCI/AHV (VM 그대로, 비용 절감) |
| B: 앱 현대화 | K8s/AI 도입 계획 있음 | VMware → Red Hat OpenShift Virtualization + OCP |
| C: 풀스택 (권장) | 대기업/그룹사, AI 구축 | Nutanix NCI (인프라) + Red Hat OCP (플랫폼) |

---

## 타깃 고객 시그널 (2개 이상이면 즉시 미팅 제안)

- 🔴 VMware 계약 갱신 D-6개월 이내 도래
- 🔴 Broadcom 전환 비용 인상 통보 수령
- 🔴 vSAN/NSX 미사용인데 VCF 강매 대상
- 🟠 AI/GPU 인프라 신규 구축 RFI/RFP 발행
- 🟠 SAP S/4HANA 마이그레이션 계획 착수
- 🟠 K8s 클러스터 난립(5개+), 운영 인력 부족
- 🟡 클라우드 비용 초과, Cloud Repatriation 검토
- 🟡 DevSecOps/앱 현대화/AI 서비스 기획 착수

---

## 업종별 핵심 메시지

| 업종 | 핵심 Pain | 핵심 Offering | 레퍼런스 |
|------|---------|-------------|---------|
| 제조 | SAP+VMware 비용 급등, On-prem 의무 | SAP PCE CDC + Nutanix NCI + AI GPU | HD한국조선해양 (30% 절감) |
| 금융 | 망분리+DR+랜섬웨어 | 계정계(AHV) + 분석계(NC2) + Data Lens | BNK금융그룹 (90% 업무) |
| 공공 | 폐쇄망+예산+AI | 구독형 NCI + Sovereign AI 풀스택 | 공공 PoC 확산 중 |
| 대기업 | 그룹사 통합+AI | 그룹 HCI + NC2 Cloud Burst + NAI | 에버랜드 NC2 최초 도입 |
| 의료 | 장기보관+AI 진단 | NUS 장기보관 + OpenShift AI | - |

---

## TCO 절감 핵심 수치

| 항목 | 수치 |
|------|------|
| S/W 라이선스 절감 (100 Core) | 약 60~70% (VMware $53K/년 → Nutanix $15~20K/년) |
| 3년 TCO 절감 (100 VM) | 약 32% ($399K → $270K) |
| NC2 vs VMC on AWS | 약 30~40% 저렴 |
| 업계 평균 TCO 절감율 | 28~55% |

---

## 마이그레이션 핵심 도구 — Nutanix Move

- 에이전트리스(Agentless): 별도 소프트웨어 설치 불필요
- 백그라운드 사전 복제: 서비스 운영 중 데이터 사전 이전
- 컷오버 다운타임: 통상 10분 이내
- Rollback 지원: 원복 가능
- 무료 제공: Nutanix 구독에 포함

---

## MZC 마이그레이션 패키지 (11단계 팩토리)

| 단계 | 내용 | 비고 |
|------|------|------|
| 1. Rapid Assessment | 인벤토리/종속성/TCO 분석 | 권장 진입점 (무상/펀딩 지원) |
| 2. Migration Pilot | 10~20 VM Go/No-Go 검증 | 2~4주 |
| 3. Migration Factory | Wave별 본 이관 | 12~24주 |
| 4~5. NC2/DR | AWS VPC + DR 구성 | - |
| 6~7. AI Ready | GPU 인프라 + AI 플랫폼 | NAI/RHOAI |
| 8. Managed Ops | MZC MSP 운영 | 24x7 |
| 9. Funding | AWS/Nutanix/RedHat 펀딩 | 비용 절감 핵심 레버 |

---

## 반론 대응 5줄 요약

| 반론 | 대응 |
|------|------|
| "생태계가 VMware보다 약하다" | Nutanix 2,500+ 파트너, Dell/HPE/Lenovo 공식 인증, 국내 대형 레퍼런스 다수 |
| "마이그레이션 중 서비스 중단이 무섭다" | Move 에이전트리스 방식으로 컷오버 10분 이내, 파일럿 후 웨이브 단위 리스크 분산 |
| "OpenShift가 너무 비싸다" | TCO 전체(운영 인력, 보안, 자동화)로 비교; MZC MSP로 운영 부담 위임 |
| "현재 계약 중도해지가 어렵다" | Co-existence로 병행 구축 후 갱신 만료 시 완전 전환, 단계적 접근 가능 |
| "외장 스토리지를 버려야 하냐" | NCI는 Dell/NetApp/Pure Storage 외장 스토리지와 유연한 결합 지원 |

---

## 이해관계자별 1줄 메시지

- **CIO/CTO**: "VM·컨테이너·AI 워크로드를 단일 하이브리드 전략 아래 묶습니다"
- **CFO**: "5년 TCO 30~50% 절감, 예측 가능한 구독 구조로 예산 안정성 확보"
- **인프라팀장**: "Nutanix Move로 다운타임 최소화, 기존 운영 방식 그대로 전환"
- **보안팀장**: "망분리/폐쇄망 완벽 준수, Data Lens 기반 데이터 거버넌스 강화"
- **개발팀장**: "VM에서 컨테이너·AI까지, 단일 플랫폼 셀프서비스 배포 환경"

---

## 다음 액션

1. **진입 미팅 제안**: "VMware 라이선스 현황 점검 및 대안 검토 미팅" (30~60분)
2. **Rapid Assessment 착수**: 무상 또는 펀딩 지원 적용 제안
3. **파이프라인 등록**: CRM에 Tier 분류 및 갱신 만료일 기록

---

*메가존클라우드 ISV/Hybrid Cloud BU | 2026-08-24 | V1.0*
