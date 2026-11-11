# 📋 [명세서] 2026-11-11 원익홀딩스·원익로보틱스 AX 센터 RFI 설명회 정리 및 제안서 개정(v2.0) 명세서

- **문서 번호**: SPEC-20261111-WONIK-AXC-RFI-01
- **작성 일자**: 2026-11-11
- **대상 워크스페이스**: `c:\dev\antigravity-workspace\aifullstack` (`https://github.com/kesperinc/aifullstack_issu.git`)
- **적용 규칙**: [AGENTS.md](file:///c:/dev/antigravity-workspace/aifullstack/AGENTS.md) 필수 개발 및 문서화 가드레일 준수

---

## 1. 개요 및 목적

2026년 11월 11일 진행된 원익홀딩스·원익로보틱스 AX 센터(피지컬 AI 로봇 트레이닝 센터) RFI 설명회 현장 논의 사항을 기반으로 핵심 팩트를 정리(마크다운 및 배포용 텍스트 파일)하고, 이를 반영한 개정 사업제안서(v2.0)를 수립하여 버전 관리합니다.

---

## 2. 주요 반영 내역 요약

1. **로봇 핸드(Allegro Hand) 중심 AI 트레이닝 센터 및 사업화 비전 정의**:
   - 작업자의 정교한 손(Hand)이 필수적인 수작업 모사 공정 및 5개 범용 Cell 유연 지원 구조 정의.
   - 로봇이 로봇을 제조·훈련하는 Dark Factory 구현 및 ‘트레이닝 완료 로봇’ 외부 판매 모델(대중국 경쟁력 확보) 반영.
2. **현행 NVIDIA 플랫폼(Isaac Sim / RFM)의 기술적 미비점 보완 및 전방위 제안**:
   - 시뮬레이션↔AI 트레이닝 반복, Synthetic 데이터 증강, **원익 자체 보유 기구학(Kinematics) 코드 기반 정확도·재현율 검증 루프** 결합.
   - 국제적으로 희소한 로봇 트레이닝 컨설팅 역량 확보(EY 불참 확정 제외 글로벌 컨설팅 펌 발굴) 및 다분야 전방위 기술 컨소시엄 구성안 수립.
3. **트레이닝 메모리 소요량 기반 복합 GPU 클러스터 및 현장 Micro Data Center 설계**:
   - 2년간 H200 192~400장(또는 288GB 메모리의 B300 96~200장) 대용량 메모리 학습 Tier + 물리 시뮬레이션 전용 GPU(RTX PRO 6000 Blackwell / L40S) 결합 복합 GPU 제안 및 향후 본 환경 Migration 반영.
   - 로컬+클라우드 하이브리드 환경의 산출물(Output) 기준 보안 구역 분리 및 핵심 공정 보안 데이터·실시간 로봇 제어 연동을 전담하는 소규모 **Micro Data Center(Local Data Center)** 정의.

---

## 3. 변경 파일 맵 (Specs Map)

| 구분 | 파일 경로 | 변경 유형 | 설명 |
| :--- | :--- | :---: | :--- |
| **설명회 정리 (MD)** | [`docs/2026-11-11_wonik_robotics_rfi_briefing_summary.md`](file:///c:/dev/antigravity-workspace/aifullstack/docs/2026-11-11_wonik_robotics_rfi_briefing_summary.md) | `[NEW]` | 원익홀딩스·원익로보틱스 RFI 설명회 확정 팩트 정리 (마크다운) |
| **설명회 정리 (TXT)** | [`docs/2026-11-11_wonik_robotics_rfi_briefing_summary.txt`](file:///c:/dev/antigravity-workspace/aifullstack/docs/2026-11-11_wonik_robotics_rfi_briefing_summary.txt) | `[NEW]` | 대내외 공유·전달용 순수 텍스트 본 (문서 루트) |
| **설명회 정리 (TXT)** | [`docs/akamai_ncp/wonik_ax_center/2026-11-11_wonik_robotics_rfi_briefing_summary.txt`](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/wonik_ax_center/2026-11-11_wonik_robotics_rfi_briefing_summary.txt) | `[NEW]` | 대내외 공유·전달용 순수 텍스트 본 (원익 AX 센터 폴더) |
| **개정 제안서 (v2.0)** | [`docs/akamai_ncp/wonik_ax_center/2026-11-11_wonik_robotics_ax_center_proposal_v2.md`](file:///c:/dev/antigravity-workspace/aifullstack/docs/akamai_ncp/wonik_ax_center/2026-11-11_wonik_robotics_ax_center_proposal_v2.md) | `[NEW]` | 11/11 RFI 설명회 팩트 전면 반영 개정 사업제안서 (v2.0) |
| **변경 명세서** | [`docs/specs/2026-11-11_wonik_robotics_rfi_briefing_spec.md`](file:///c:/dev/antigravity-workspace/aifullstack/docs/specs/2026-11-11_wonik_robotics_rfi_briefing_spec.md) | `[NEW]` | 2026-11-11 원익 RFI 설명회 문서화 및 제안서 개정 명세서 (본 문서) |
