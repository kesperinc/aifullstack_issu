# [산출물 명세서] Articul8 산출물 전수 분석 및 On-Premise RHOAI 구축 전략

- **일자**: 2026-09-11
- **문서명**: `2026-09-11_articul8_onprem_rhoai_specs.md`
- **관련 커밋/작업**: Articul8 55건 산출물 분석, On-Premise HW(Dell PowerEdge) 기반 RHOAI 설치 아키텍처 및 YAML 옵션 대체 매핑

---

## 1. 변경 및 생성 파일 맵 (Specs Map)

| 구분 | 파일 경로 | 역할 및 상세 설명 |
| :--- | :--- | :--- |
| **[보고서]** | [2026-09-11_articul8_onprem_rhoai_architecture_report.md](file:///c:/dev/antigravity-workspace/aifullstack/docs/2026-09-11_articul8_onprem_rhoai_architecture_report.md) | 55개 수집 파일 한 줄 요약, 온프레미스 인프라 구성 추정 및 근거, AWS 대비 온프레미스 사전 파악 자료 7종, YAML 옵션 1:1 대체 전략을 집대성한 공식 기술보고서. |
| **[웹 리포트]** | [2026-09-11_articul8_onprem_rhoai_architecture_report.html](file:///c:/dev/antigravity-workspace/aifullstack/docs/2026-09-11_articul8_onprem_rhoai_architecture_report.html) | Glassmorphism 및 다크 테마 기반 반응형 대시보드로 실시간 검색이 가능한 55개 파일 요약표, 시각적 아키텍처 캔버스, 코드 비교 뷰, 배포 로드맵 제공. |
| **[명세서]** | [2026-09-11_articul8_onprem_rhoai_specs.md](file:///c:/dev/antigravity-workspace/aifullstack/docs/specs/2026-09-11_articul8_onprem_rhoai_specs.md) | 작업 트라이어드 및 변경 이력 추적을 위한 공식 명세서 (본 파일). |

---

## 2. 주요 핵심 결과 요약

1. **산출물 전수 조사**:
   - `C:\Users\MZC01-SUNKIM317\OneDrive\2026\ISSU\Articul8 (산출물)` 내 55개 파일(기술문서 23건, 원천플레이북 19건, 고객 기회/제안서 10건, HW 견적 3건)을 전수 분석하여 한 줄 요약 완료.
2. **On-Premise HW 기반 RHOAI 구성 추정**:
   - **Bastion (1대)**: Dell PowerEdge R570 (8C/16T, 32GB RAM, 960GB SSD x 3) → a8 CLI 실행, OpenShift Installer, Mirror Registry.
   - **OpenShift Compact 클러스터 (3대)**: Dell PowerEdge R770 (각 64C/128T, 256GB RAM, 960GB SSD x 4) → 총 192C/768GB RAM으로 AWS 실측 22대 노드/316개 파드 및 OCP/RHOAI/Articul8 코어 마이크로서비스를 Compact 3노드로 집약.
   - **GPU Worker 노드 (1대)**: Dell PowerEdge XE7740 (64C/128T, 512GB RAM, 3.84TB NVMe SSD, **NVIDIA H200 NVL 4장, 총 564GB VRAM**) → AWS p4de(A100 8장) 대비 동등 이상의 대형 LLM(Llama-3-70B FP16) 및 ModelMesh 서빙 처리.
3. **AWS 대비 RHOAI 사전 파악 자료 7대 영역 도출**:
   - 공식 온프레미스 배포 가이드, 폐쇄망 오프라인 패키징(98개 이미지), 10개 S3 버킷 요구 규격, 인-클러스터 PostgreSQL/Redis 사양, H200 드라이버 호환성, 사내 DNS/TLS 인증서, ArangoDB 온프레미스 백업 타깃.
4. **YAML 상의 AWS 전용 옵션 1:1 대체 매핑 완료**:
   - `provider.aws` → `provider.onprem`
   - `p4de.24xlarge` → RHOAI AcceleratorProfile (`h200-nvl`) + NodeSelector
   - `ALB (internet-facing)` → OpenShift Ingress Route (Edge TLS) / MetalLB VIP
   - `EBS gp3` → OpenShift Data Foundation (`ocs-storagecluster-ceph-rbd`)
   - `AWS S3 (10개)` → 인-클러스터 MinIO / ODF NooBaa
   - `RDS / ElastiCache` → CloudNativePG Operator / Redis Operator
   - `AWS IRSA` → OpenShift ServiceAccount + HashiCorp Vault / ESO
