# 📋 [명세서] Syncthing docs 원본 문서 동기화 제외 및 P2P 동기화 상태 최적화 명세서

- **문서 번호**: SPEC-20260826-SYNCTHING-IGNORE-01
- **작성 일자**: 2026년 08월 26일
- **작성자**: MZC ISSU AI Full Stack Architecture & Solution Sales Team
- **대상 워크스페이스**: `c:\dev\antigravity-workspace\aifullstack` / `c:\dev\antigravity-workspace`
- **상태**: ✅ **반영 및 검증 완료**

---

## 1. 개요 및 목적

본 명세서는 메가존클라우드 AI Full Stack 워크스페이스 및 다중 PC(사무실/노트북/홈 워크스테이션) 간 P2P 데이터 동기화 도구인 **Syncthing** 환경에서, `docs` 폴더 내의 외부 수신 원본 자료(대용량 PDF, 원본 파트너사 데이터셋 등)가 불필요하게 대역폭을 소모하거나 동기화 지연을 유발하지 않도록 **동기화 제외(Ignore Rule)** 패턴을 설정하고, 현재 활성 동기화 상태 및 충돌 무결성을 전수 점검하여 조치한 내역을 정의합니다.

---

## 2. 제외 대상 원본 문서 및 패턴 정의

### 2.1 대상 원본 문서 식별
- `docs/퀀텀ai/*.pdf` (컨택센터 AI 시장 및 기술 동향, QuantumAI 제안서, 사업 자료 등 외부 수신 대용량 원본 PDF)
- `docs/Puzzle Data/*.pdf` (파트너십 미팅 및 원본 데이터셋 PDF)
- `docs/` 하위의 원본 수신 디렉터리 (`raw/`, `original/`, `originals/`, `source/`, `sources/`)

### 2.2 Syncthing `.stignore` 규칙 적용
- **삭제 허용 플래그 (`(?d)`) 부여**: 로컬에서 불필요한 파일을 정리할 때 원격 기기에서 충돌 없이 안전하게 삭제될 수 있도록 `(?d)` 플래그 적용

```plaintext
// docs 폴더 내 원본 문서 (PDF, 대용량 원본 파일 및 원본 데이터 폴더) 제외
(?d)**/docs/**/*.pdf
(?d)**/docs/Puzzle Data/
(?d)**/docs/퀀텀ai/
(?d)**/docs/raw/
(?d)**/docs/original/
(?d)**/docs/originals/
(?d)**/docs/source/
(?d)**/docs/sources/
```

---

## 3. 적용 파일 및 설정 위치

| 파일 경로 | 적용 내용 | 상태 |
| :--- | :--- | :--- |
| `c:\dev\antigravity-workspace\aifullstack\.stignore` | `aifullstack` 리포지토리 레벨 원본 문서 제외 규칙 추가 | ✅ 적용 완료 |
| `c:\dev\antigravity-workspace\.stignore` | 워크스페이스 루트(`agy-workspace`) 레벨 원본 문서 제외 규칙 추가 | ✅ 적용 완료 |

---

## 4. 동기화 상태 진단 및 조치 결과

1. **디바이스 연결 상태 점검**:
   - `home-sunkim` (100.65.102.5:22000): ✅ **연결 정상 (Connected: True)**
   - `DESKTOP-LGNoteBook` (100.91.179.35:22000): ✅ **연결 정상 (Connected: True)**
   - `mzc-sunkim317-l`: ⏸️ 오프라인 대기 상태
2. **동기화 오류/충돌 점검**:
   - `aifullstack` 내부: 충돌 파일 0건 (클린 상태)
   - 워크스페이스 내 과거 잔여 충돌 파일 2건 탐색 및 안전 삭제 조치:
     - `moo-sim-app\docs\HANDOVER_20260729_PM.sync-conflict-*.md` (삭제 완료)
     - `moo-sim-app\docs\WORK_LOG_20260729_PM.sync-conflict-*.md` (삭제 완료)
3. **Syncthing Core 재스캔**:
   - REST API(`rest/db/scan?folder=agy-workspace`) 호출을 통한 즉시 재스캔 및 인덱스 갱신 완료
