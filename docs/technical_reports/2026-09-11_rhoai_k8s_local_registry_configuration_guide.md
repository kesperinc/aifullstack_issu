# 🚀 RHOAI Pod 구성 가이드 및 온프레미스 로컬 레지스트리 구축 전략서

* **작성 일자**: 2026년 9월 11일
* **문서 번호**: `2026-09-11_rhoai_k8s_local_registry_configuration_guide`
* **대상 인프라**: CPU 노드 3대 (64 Core, 640GB SSD x 2) + 2xGPU 워커 서버 1대
* **주요 목적**: 
  1. Red Hat OpenShift AI (RHOAI) 환경의 고성능/안정적 Pod 구성 필수 파라미터 표준화
  2. 잔여 640GB SSD를 활용한 독립 프라이빗 레지스트리(Local Mirror Registry) 구축 및 클러스터 전파 방안 제시

---

## 1. RHOAI Pod 구성 시 필수 핵심 설정값 가이드

OpenShift AI(RHOAI) 환경은 일반 Kubernetes 대비 **강화된 보안 제약(SCC)**, **GPU/가속기 전용 스케줄링**, **대용량 모델 메모리 매핑(/dev/shm)**, **LLM 가중치 로딩 시간(StartupProbe)** 등 특화된 설정이 요구됩니다.

```
┌──────────────────────────────────────────────────────────────────────────┐
│                         RHOAI Pod 아키텍처 구성                          │
├──────────────────────────────────────────────────────────────────────────┤
│  [Compute & GPU]       nvidia.com/gpu: "1" (requests = limits 강제)      │
│  [Scheduling]          nodeSelector + tolerations (GPU Taint 무효화)     │
│  [Shared Memory]       /dev/shm emptyDir (Memory) 8~32Gi (OOM 방지)      │
│  [Security/SCC]        runAsNonRoot: true, drop: [ALL] (restricted-v2)   │
│  [Health Probes]       startupProbe failureThreshold: 60 (10분 여유)     │
│  [Storage & Model]     RWX PVC 마운트 또는 S3 Data Connection 주입        │
└──────────────────────────────────────────────────────────────────────────┘
```

### 1.1. 세부 파라미터 분석표

| 설정 영역 | 핵심 파라미터 | 권장 설정값 및 내용 | 미설정 시 발생하는 장애 |
| :--- | :--- | :--- | :--- |
| **GPU / 가속기** | `resources.limits.nvidia.com/gpu` | `requests`와 `limits`를 1:1로 동일 설정 | GPU 디바이스 인식 불가, 파드 Pending |
| **노드 스케줄링** | `tolerations`, `nodeSelector` | `key: nvidia.com/gpu, operator: Exists` | GPU 노드의 Taint로 인해 파드 배치 거부 |
| **공유 메모리** | `volumes.emptyDir.medium: Memory` | `/dev/shm` 마운트, 8Gi ~ 32Gi 할당 | PyTorch 분산 통신 중 `Bus error (OOM)` 크래시 |
| **보안 컨텍스트** | `securityContext` (SCC) | `runAsNonRoot: true`, `drop: [ALL]` | OpenShift `restricted-v2` SCC에 의해 배포 차단 |
| **헬스체크** | `startupProbe` | `failureThreshold: 60`, `periodSeconds: 10` | 모델 VRAM 로딩 중(수 분 소요) 무한 재시작 루프 |
| **스토리지 연동** | `volumes`, `envFrom` | S3 Secret 연동 또는 RWX ODF PVC 마운트 | 모델 가중치 파일 접근 실패 및 기동 중단 |

### 1.2. 표준 Pod 매니페스트 샘플 (vLLM / LLM 서빙 기준)

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: vllm-llama3-serving
  namespace: rhoai-workloads
  labels:
    app: vllm-inference
spec:
  # 1. GPU 노드 배치 및 Taint 회피
  nodeSelector:
    node.kubernetes.io/instance-type: "gpu-worker"
  tolerations:
  - key: "nvidia.com/gpu"
    operator: "Exists"
    effect: "NoSchedule"

  # 2. OpenShift 보안 가드레일 (Non-Root 실행)
  securityContext:
    runAsNonRoot: true
    allowPrivilegeEscalation: false
    capabilities:
      drop:
      - ALL
    seccompProfile:
      type: RuntimeDefault

  containers:
  - name: vllm-engine
    image: 192.168.1.10:5000/models/vllm:v0.6.2
    command: ["python3", "-m", "vllm.entrypoints.openai.api_server"]
    args:
    - "--model=/models/llama-3-8b-instruct"
    - "--tensor-parallel-size=2"
    - "--max-model-len=8192"
    - "--gpu-memory-utilization=0.9"

    # 3. GPU 및 시스템 리소스 할당
    resources:
      requests:
        cpu: "8"
        memory: "32Gi"
        nvidia.com/gpu: "2"
      limits:
        cpu: "16"
        memory: "64Gi"
        nvidia.com/gpu: "2"

    # 4. 볼륨 마운트 (/dev/shm 및 모델 스토리지)
    volumeMounts:
    - name: dshm
      mountPath: /dev/shm
    - name: model-weights
      mountPath: /models

    # 5. 모델 로딩 지연을 고려한 3단계 프로브
    startupProbe:
      httpGet:
        path: /health
        port: 8000
      initialDelaySeconds: 30
      periodSeconds: 10
      failureThreshold: 60  # 최대 600초 (10분) 모델 로딩 대기
    readinessProbe:
      httpGet:
        path: /v1/models
        port: 8000
      periodSeconds: 5
    livenessProbe:
      httpGet:
        path: /health
        port: 8000
      periodSeconds: 15

  volumes:
  # /dev/shm 공유 메모리 확장
  - name: dshm
    emptyDir:
      medium: Memory
      sizeLimit: "16Gi"
  # 모델 가중치 영구 볼륨
  - name: model-weights
    persistentVolumeClaim:
      claimName: pvc-model-weights
```

---

## 2. 온프레미스 4노드 인프라 아키텍처 및 디스크 활용 방안

### 2.1. 대상 인프라 제원
* **CPU 노드 3대**: 64 Core CPU, RAM, **640GB SSD x 2장** (K8s Control Plane + Worker 컨버지드 노드)
* **GPU 노드 1대**: 2xGPU 워커 서버 (NVIDIA 가속기 탑재)

### 2.2. CPU 노드 디스크 2장 분리 전략

각 CPU 노드의 640GB SSD 2장을 다음과 같이 분리 배치하여, 시스템 I/O 경합을 원천 방지하고 독립 스토리지를 확보합니다:

```
┌────────────────────────────────────────────────────────────────────────┐
│                      CPU 노드 1 (마스터 / 레지스트리 호스트)            │
├───────────────────────────────────┬────────────────────────────────────┤
│           SSD 1 (640GB)           │           SSD 2 (640GB)            │
│       [ OS & K8s 시스템 영역 ]     │     [ 전용 로컬 이미지 레지스트리 ]  │
│  - Linux OS Root (/), Swap 없음   │  - 마운트 포인트: /data/registry    │
│  - Kubelet (/var/lib/kubelet)     │  - Podman 기반 Harbor / Registry    │
│  - 컨테이너 캐시 (/var/lib/containers)│ - 640GB 독립 대용량 이미지 풀   │
└───────────────────────────────────┴────────────────────────────────────┘
```

---

## 3. 640GB SSD 기반 로컬 컨테이너 레지스트리 구축 2대 방안

### [방안 1] 마스터 1번 노드 기반 독립형 로컬 Registry (Podman/Harbor) ⭐ 강력 권장
K8s 클러스터 내부가 아닌, **마스터 노드 호스트의 Podman/Docker 런타임에서 systemd 서비스로 직접 구동**하는 방식입니다.

* **최대 장점**: 
  1. K8s 클러스터 설치(Bootstrap) 전 단계부터 이미지를 서빙할 수 있으므로 **폐쇄망(Air-Gapped) 환경의 온프레미스 구축 시 유일하게 자립 가능한 방식**입니다.
  2. K8s 장애 발생 시에도 컨테이너 이미지를 복구용으로 즉시 풀(Pull)할 수 있습니다.

### [방안 2] K8s 인-클러스터 Local PV 기반 Registry
K8s 정상 부팅 후, 640GB SSD를 `Local PersistentVolume`으로 K8s에 등록하고, 그 위에 Harbor/Registry 파드를 띄우는 방식입니다.
* **장점**: K8s Service, Ingress, RBAC과 완벽히 연동됩니다.
* **단점**: K8s 클러스터가 깨지면 레지스트리 파드도 다운되어 복구용 이미지 취득이 어려워집니다.

---

## 4. 단계별 구축 및 클러스터 서빙 절차 (방안 1 기준)

### STEP 1. 2번째 640GB SSD 파티셔닝 및 마운트 (마스터 1번 노드)
```bash
# 1) 디스크 디바이스 식별 (예: /dev/sdb 또는 /dev/nvme1n1)
lsblk

# 2) 고성능 XFS 파일시스템 포맷
sudo mkfs.xfs -f /dev/sdb

# 3) 레지스트리 전용 디렉터리 생성 및 마운트
sudo mkdir -p /data/registry
sudo mount /dev/sdb /data/registry

# 4) 재부팅 시 영구 마운트 설정 (/etc/fstab)
UUID=$(sudo blkid -s UUID -value /dev/sdb)
echo "UUID=${UUID}  /data/registry  xfs  defaults,noatime  0 0" | sudo tee -a /etc/fstab
```

### STEP 2. TLS 인증서 및 레지스트리 디렉터리 구조 생성
```bash
sudo mkdir -p /data/registry/{data,certs,auth}

# 자체 서명 TLS 인증서 생성 (마스터 1번 IP: 192.168.1.10 가정)
sudo openssl req -newkey rsa:4096 -nodes -sha256 \
  -keyout /data/registry/certs/domain.key \
  -x509 -days 3650 \
  -out /data/registry/certs/domain.crt \
  -subj "/CN=registry.local" \
  -addext "subjectAltName=IP:192.168.1.10,DNS:registry.local"
```

### STEP 3. Podman 기반 Private Registry 실행 및 systemd 등록
```bash
# 레지스트리 컨테이너 실행
sudo podman run -d \
  --name local-registry \
  --restart=always \
  -p 5000:5000 \
  -v /data/registry/data:/var/lib/registry:z \
  -v /data/registry/certs:/certs:z \
  -e REGISTRY_HTTP_TLS_CERTIFICATE=/certs/domain.crt \
  -e REGISTRY_HTTP_TLS_KEY=/certs/domain.key \
  registry:2

# 부팅 시 자동 기동을 위한 systemd 서비스 생성
sudo podman generate systemd --new --name local-registry > /etc/systemd/system/local-registry.service
sudo systemctl daemon-reload
sudo systemctl enable --now local-registry.service
```

### STEP 4. 클러스터 전 노드(CPU 3대 + GPU 1대) 레지스트리 신뢰 등록

#### [OpenShift / CRI-O 환경]
모든 노드의 `/etc/containers/registries.conf.d/local-registry.conf`에 추가:
```toml
[[registry]]
prefix = "192.168.1.10:5000"
location = "192.168.1.10:5000"
insecure = true
```
또는 생성된 `domain.crt` 인증서를 각 노드의 `/etc/pki/ca-trust/source/anchors/`에 복사 후 `update-ca-trust` 실행.

#### [표준 Kubernetes (containerd) 환경]
각 노드의 `/etc/containerd/config.toml` 내 `plugins."io.containerd.grpc.v1.cri".registry.configs` 수정:
```toml
[plugins."io.containerd.grpc.v1.cri".registry.configs."192.168.1.10:5000".tls]
  insecure_skip_verify = true
```
설정 후 `sudo systemctl restart containerd` 적용.

---

## 5. 640GB 용량 산정 및 대용량 AI 이미지 관리 가이드

### 5.1. 이미지 사이즈 기준 저장 가능 수량
* **기본 K8s / OS 유틸리티 이미지**: 개당 100MB ~ 500MB ➔ **1,000개 이상** 수용 가능
* **일반 백엔드 / API 컨테이너**: 개당 500MB ~ 1.5GB ➔ **400개 이상** 수용 가능
* **RHOAI 서빙 / CUDA 12.x / vLLM / PyTorch 이미지**: 개당 **15GB ~ 25GB**
* **결론**: 640GB의 80% 가용 영역(약 512GB) 기준으로 **초대형 AI/GPU 추론 컨테이너 이미지 20~25종을 상시 캐싱**할 수 있어, 온프레미스 인프라 환경에서 충분한 여유를 제공합니다.

### 5.2. 디스크 풀(Full) 방지를 위한 자동 가비지 컬렉션(GC) CronJob
Docker Registry는 이미지를 태그 삭제해도 레이어 블록이 디스크에 남아 있으므로, 주기적 GC가 필수적입니다:
```bash
# 매주 일요일 새벽 3시 가비지 컬렉션 수행 스크립트 (/etc/cron.weekly/registry-gc)
#!/bin/bash
podman exec local-registry bin/registry garbage-collect /etc/docker/registry/config.yml
```

---

## 6. 결론 및 종합 제언
1. **RHOAI Pod 구성 시**: `/dev/shm` 확장(16Gi), `startupProbe` 지연 시간(10분 확보), GPU 요청/제한치 1:1 동기화, OpenShift SCC 준수가 무중단 서빙의 핵심입니다.
2. **640GB SSD 활용 시**: 3대의 CPU 노드 중 1번 노드의 SSD 2를 독립형 `Podman Local Registry`로 격리 마운트하는 것이, 클러스터 부트스트랩 및 폐쇄망 운영 관점에서 가장 안전하고 효율적인 엔터프라이즈 아키텍처입니다.
