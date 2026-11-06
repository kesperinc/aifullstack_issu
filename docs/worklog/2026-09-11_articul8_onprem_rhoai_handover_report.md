# [인수인계 보고서] Articul8 산출물 전수 분석 및 On-Premise HW 기반 RHOAI 설치·구성 핸드오버 (Handover)

- **작성일자**: 2026-09-11
- **인계자**: AI Full Stack 아키텍처 TF (Antigravity & ISSU)
- **인수자**: MEGAZONECLOUD ISSU 및 관련 엔지니어링/영업 담당자
- **문서버전**: v1.0.0
- **관련 브랜치**: `feature/vibe-coding-agent`

---

## 1. 작업 배경 및 목적 (Background & Objectives)

1. **배경**:
   - `C:\Users\MZC01-SUNKIM317\OneDrive\2026\ISSU\Articul8 (산출물)` 폴더에 수집된 55건의 Articul8 기술 자료, 운영 플레이북, 고객사 제안서, 하드웨어 견적서 분석 필요.
   - 현재 AWS EKS 기반으로 실측된 Articul8 26.06 플랫폼을 **온프레미스 Dell 서버 기반 Red Hat OpenShift AI (RHOAI)** 환경으로 이전·설치하기 위한 기술적 타당성, 인프라 구성안, 사전 파악 자료, YAML 옵션 대체 방안 수립 요청.
2. **목적**:
   - 수집된 모든 산출물(55건)의 내역 파악 및 한 줄 요약 체계화.
   - 보유 하드웨어 견적(PowerEdge R570 Bastion 1대, R770 Compact 3노드, XE7740 4GPU 1노드)의 Articul8 수용 가능성 및 정밀 사이징 검토.
   - AWS 종속적 서비스/옵션(EKS, ALB, S3, RDS, ElastiCache, EBS gp3, IRSA 등)의 OpenShift/RHOAI 1:1 대체 매핑 가이드 확립.
   - 경영진 및 기술 실무자가 즉시 활용 가능한 종합 기술보고서(Markdown) 및 인터랙티브 대시보드(HTML) 산출물 완비.

---

## 2. 주요 작업 내용 및 핵심 결론 (Key Achievements & Conclusions)

### 2.1 Articul8 전체 수집 산출물 전수 조사 (총 55건)
- **HW 견적서 (3건)**: 온프레미스 AI Full Stack 서버 견적(R570+R770 3대+XE7740 H200 4GPU, 약 8.18억 원) 및 초대형 모델용 XE9780 (B300 16장, 약 45.7억 원) 사양 정밀 분석.
- **메가존클라우드 기술자료 (23건)**: 설치·운영 Playbook, 시스템 레퍼런스 북, `a8.yaml` 기술명세서, A8 전략 회의록(Gemini 요약), SOW/WBS 파일럿 계획서, 원익IPS 폐쇄망 분석 등 분석 완료.
- **Articul8 원천 기술자료 (19건)**: a8 CLI 종합 교육 교재, 플랫폼 펀더멘털, 8대 산업별 세일즈 플레이북(제조, 금융, 항공/방위 등) 분석.
- **고객사 기회 및 제안서 (10건)**: HD현대, 경동나비엔, 원익홀딩스, 현대글로비스 및 NH투자증권 AI 플랫폼 제안서 분석.

### 2.2 Bastion 1대 + K8s 서버 3대 + 4GPU 서버 1대 설치 적합성 검토 결과
- **결론**: **설치 및 상용 운영 100% 가능(Feasible)**하며, 자원 측면에서 **약 40~50%의 충분한 안전 버퍼(Headroom)**를 확보할 수 있음.
- **세부 사이징 검토**:
  1. **K8s 노드 (R770 3대 Compact HA)**:
     - 가용 자원: **192 Core, 768GB RAM**
     - Articul8 316개 Pod 및 OCP/RHOAI/인클러스터 데이터 계층 필요량: **90~133 Core, 256~372 GB RAM**
     - **CPU 여유율 45~53%, RAM 여유율 51~66% 확보**, 노드당 파드 밀도 100~110개로 쿠버네티스 권장 한도(250개) 내 여유롭게 수용.
  2. **GPU 가속기 (XE7740 1대, NVIDIA H200 NVL 4장)**:
     - 가용 VRAM: **141GB x 4 = 총 564GB VRAM (HBM3e, 4.8TB/s 대역폭)**
     - AWS 실측 `p4de.24xlarge` (A100 80GB x 8 = 640GB) 대비 H200의 HBM3e 초고속 대역폭과 FP8 트랜스포머 엔진 덕분에 Llama-3-70B FP16/FP8 및 임베딩/멀티모달 모델 동시 서빙 시 **A100 8장을 능가하는 추론 처리량** 달성 가능.
  3. **Bastion 서버 (R570 1대)**:
     - 8C/16T, 32GB RAM, 960GB SSD x 3을 기반으로 a8 CLI 26.06 실행, OpenShift 배포 관리자, 폐쇄망 미러 레지스트리(Quay) 단독 구동에 최적.
- **주의 및 필수 점검 사항**:
  - **스토리지 복제**: ODF(Ceph) 3-Way 복제 시 R770의 960GB SSD(총 11.5TB Raw)가 실가용 3.8TB로 제한될 수 있으므로, R770 SSD를 3.84TB로 증설하거나 사내 외장 SAN/NAS(iSCSI/NFS) 연동 권고.
  - **etcd 디스크 I/O**: 3-Node Compact 클러스터 특성상 etcd 레이턴시(`< 10ms`) 보장을 위해 etcd 전용 디스크(NVMe 또는 BOSS-N1) 분리 권고.

### 2.3 AWS 대비 RHOAI 사전 파악 필요 자료 7종 확립
1. Articul8 온프레미스 배포 공식 가이드 및 `a8` CLI 온프레미스 provider 지원 여부.
2. 98개 컨테이너 이미지 및 모델 가중치 오프라인 Tarball 패키지 (과거 ECR 403 오류 차단용).
3. 10개 S3 버킷에 대한 오브젝트 스토리지(MinIO/ODF NooBaa) API 호환성 규격.
4. 인-클러스터 PostgreSQL(CloudNativePG) 및 Redis Sentinel 요구 스펙.
5. Red Hat CoreOS 상의 NVIDIA H200 드라이버 및 RHOAI KServe/vLLM 연동 스펙.
6. 사내 사설 FQDN 및 사설 Root CA 인증서 배포 체계.
7. ArangoDB Enterprise 핫백업 온프레미스 S3 엔드포인트 연동 여부.

### 2.4 YAML 상의 AWS 전용 옵션 1:1 대체 매핑
- `provider.aws` ➔ `provider.onprem` (사내 테넌트 ID 매핑)
- `eks.model_inference_large_group_instance_type: p4de.24xlarge` ➔ RHOAI AcceleratorProfile (`nvidia-h200`) + NodeSelector 직접 바인딩
- `loadBalancer.scheme: internet-facing` (ALB) ➔ OpenShift Ingress Route (Edge TLS) / MetalLB L4 VIP
- `StorageClass: ebs-sc` (EBS gp3) ➔ OpenShift Data Foundation (`ocs-storagecluster-ceph-rbd`)
- `AWS S3 (10개 버킷)` ➔ 인-클러스터 MinIO S3 호환 엔드포인트
- `AWS RDS / ElastiCache` ➔ CloudNativePG Operator / Redis Operator

---

## 3. 산출물 파일 인벤토리 (Artifacts Inventory)

| No. | 구분 | 파일 경로 | 주요 내용 및 특징 |
| :---: | :---: | :--- | :--- |
| 1 | **기술보고서** | [`docs/2026-09-11_articul8_onprem_rhoai_architecture_report.md`](file:///c:/dev/antigravity-workspace/aifullstack/docs/2026-09-11_articul8_onprem_rhoai_architecture_report.md) | 55개 파일 요약, HW 자원 정밀 사이징 계산, 사전 파악 자료 7종, YAML 1:1 대체 가이드 수록 (Markdown). |
| 2 | **웹 리포트** | [`docs/2026-09-11_articul8_onprem_rhoai_architecture_report.html`](file:///c:/dev/antigravity-workspace/aifullstack/docs/2026-09-11_articul8_onprem_rhoai_architecture_report.html) | Glassmorphism 다크 테마 대시보드. 실시간 검색 테이블, 아키텍처 캔버스, 코드 비교 뷰, 배포 로드맵 제공 (HTML). |
| 3 | **작업명세서** | [`docs/specs/2026-09-11_articul8_onprem_rhoai_specs.md`](file:///c:/dev/antigravity-workspace/aifullstack/docs/specs/2026-09-11_articul8_onprem_rhoai_specs.md) | 작업 트라이어드(Plan-Code-Doc) 및 변경 이력 추적을 위한 공식 명세서. |
| 4 | **인수인계서** | [`docs/2026-09-11_articul8_onprem_rhoai_handover_report.md`](file:///c:/dev/antigravity-workspace/aifullstack/docs/2026-09-11_articul8_onprem_rhoai_handover_report.md) | 인수인계 및 실행 권고사항을 정리한 종합 핸드오버 문서 (본 파일). |

---

## 4. 인수자 후속 권고 및 액션 아이템 (Next Steps)

1. **Articul8 본사 기술 문의 (Checklist 전달)**:
   - 본 보고서 3장의 **'사전 파악 필요 자료 7종'**을 체크리스트 형태로 정리하여 Articul8 파트너 엔지니어링 팀에 공식 질의 및 회신 요청.
   - 오프라인 컨테이너 이미지 98개 Tarball 번들 및 다운로드 링크 사전 확보 요청.
2. **사내 하드웨어 발주 및 디스크 최적화 확인**:
   - R770 Compact 노드의 스토리지 복제(Replication)를 감안하여 960GB SATA SSD 대신 **3.84TB SSD 증설 가능 여부** 사전 검토.
3. **RHOAI PoC / 드라이런(Dry-run) 진행**:
   - 가상화 또는 개발 샌드박스 환경에서 본 보고서의 `a8-onprem.yaml` 설정을 기반으로 배포 프로세스 사전 검증.
