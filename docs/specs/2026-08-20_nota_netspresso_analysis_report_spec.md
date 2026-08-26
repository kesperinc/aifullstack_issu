# [명세서] Nota.ai NetsPresso 기술 심층 분석 및 MZC AI Full Stack 연계 전략 보고서

- **문서 번호**: SPEC-20260820-NOTANETSPRESSO-01
- **작성 일자**: 2026-08-20
- **작성자**: MZC AI Full Stack 아키텍처 및 ISV 솔루션 엔지니어링 팀
- **대상 파일**:
  - `offering/2026-08-20_nota_ai_netspresso_analysis_report.html` (독립 인터랙티브 웹 보고서)
  - `offering/generate_nota_netspresso_report_docx.py` (DOCX 생성기)
  - `offering/docx/2026-08-20_Nota_AI_NetsPresso_Fullstack_Analysis_Report.docx` (공식 Word 문서)
  - `docs/2026-08-20_Nota_AI_NetsPresso_Fullstack_Analysis_Report.docx` (루트 docs 동기화 문서)

---

## 1. 개요 및 분석 배경
- **요청 사항**: Nota.ai의 NetsPresso 플랫폼에 대한 핵심 기술(하드웨어 인지 최적화, 양자화, 타깃 칩셋 매칭 및 컴파일)을 분석하고, MZC AI Full Stack 편입 시 사전 검토 사항, Red Hat OpenShift AI(RHOAI)와의 기능 비교 및 상호 보완 공존 방안, 그리고 3대 단독/복합 제안 시나리오를 정밀 정리하여 독립된 HTML/DOCX 보고서로 수립.
- **가드레일 준수**: 기존 마스터 보고서(`mzc_ai_fullstack_strategy_service_report.html`)에는 아직 포함하지 않고 독립된 별도 산출물로 생성.

---

## 2. 보고서 핵심 구조 및 상세 내용

### 제 1 장. Nota.ai NetsPresso 플랫폼 핵심 기술 요약
- **하드웨어 인지 경량화 (Hardware-Aware Pruning)**: 150+ 최적화 패턴 라이브러리, 구조적 가지치기(Structured Pruning), 필터 분해 및 레이어 융합(Layer Fusion).
- **지능형 양자화 & LLM (Advanced Quantization)**: 레이어별 민감도 기반 혼합 정밀도(Mixed Precision, FP16/INT8/INT4/FP8), LLM 특화 AutoRound 기술(정확도 손실 <1%), HAQA(자율 양자화 에이전트).
- **Device Farm & 자동 컴파일**: 물리 타깃 칩셋 원격 실측(Latency, Memory, Power), ONNX/TensorRT/OpenVINO/TFLite/SNPE 원클릭 자동 컴파일 및 노코드/파이썬 SDK 파이프라인.

### 제 2 장. MZC AI Full Stack 편입 시 핵심 검토 및 사전 점검 과제 (Gap Analysis)
1. **대형 파운데이션 모델(LLM/MoE/VLM) 지원 성숙도**: 32B~70B 대형 언어 모델 및 멀티모달 모델에 대한 압축/서빙 안정성 및 TPS 실측 검증.
2. **온프레미스 완전 폐쇄망(Air-Gap) 설치 지원 여부**: 클라우드 SaaS를 넘어 사내 쿠버네티스(OpenShift/Nutanix) 컨테이너 Appliance 패키지 및 오프라인 라이선스 인증 방식 확보.
3. **엔터프라이즈 MLOps 및 서빙 엔진 연동성 (Interoperability)**: vLLM, Triton Inference Server, KServe, DataRobot, LangChain/Articul8과의 표준 REST/gRPC API 연계성.
4. **상용 라이선스 체계 및 SI 비즈니스 마진 구조**: Per-device / Per-model / Annual License 구조 파악 및 MZC H/W 번들링 오퍼링 마진율 확보.

### 제 3 장. Red Hat OpenShift AI (RHOAI)와의 기능 비교 및 상호 보완 공존 방안
- **포지셔닝 비교**: RHOAI는 인프라/오케스트레이션/서빙 플랫폼(Layer 02/03), NetsPresso는 전문 모델 압축 및 타깃 칩셋 컴파일 도구(Layer 03 특화 엔진).
- **통합 시너지 파이프라인 아키텍처**:
  - `[RHOAI Workbench (PyTorch/Ray 분산 학습)] ➔ [NetsPresso Plugin (AutoRound INT4 압축/컴파일)] ➔ [RHOAI KServe/vLLM (vGPU/MIG 스케줄링 서빙)] ➔ [초저지연 비즈니스 앱 연동]`
  - 모델 크기 1/2~1/4 압축을 통해 단일 GPU 서빙 처리량(TPS) 3배 향상 및 인프라 비용 대폭 절감.

### 제 4 장. MZC AI Full Stack 내 단독/복합 솔루션 제안 시나리오 (3대 Use Case)
- **시나리오 1: 스마트팩토리 엣지 AI 패키지**: Dell 엣지 서버 + NetsPresso 비전 모델 경량화(크기 1/5, 속도 3~5배) ➔ 제조 불량 검출 및 CCTV 실시간 관제.
- **시나리오 2: 소버린 sLLM 경량 서빙 패키지**: Dell PowerEdge R760 (2x RTX 6000 Ada / L40S) + NetsPresso AutoRound INT4 + vLLM ➔ 8-GPU 대형 서버 대신 단일 가속기로 60+ TPS 서빙 달성 (인프라 TCO 60% 절감).
- **시나리오 3: 소버린 NPU 멀티 벤더 전환 패키지**: 국산 AI 반도체(리벨리온, 퓨리오사AI, Intel Gaudi) + NetsPresso Device Farm 자동 컴파일 ➔ 엔비디아 탈피 및 Zero Lock-in 실현.

### 제 5 장. 종합 결론 및 향후 기술 검증(PoC) 제언
- **포지셔닝**: 동일 인프라 환경에서 모델 경량화 및 추론 서빙 처리량(TPS)을 최대 3배 이상 극대화할 수 있는 잠재력이 있어, **향후 MZC AI Full Stack의 Layer 03 (Model Compression / Optimization) 구성요소 중 하나로 편입을 검토할 수 있는 솔루션**.
- **신중한 검토 관점**: 즉각적 도입/필수 탑재보다는 거대 LLM 실증 성능, 온프레미스 폐쇄망(Air-Gap) 배포 안정성, 상용 라이선스 비즈니스 모델에 대한 **사전 기술 검증(PoC)이 반드시 선행되어야 하는 '향후 필요 시 검토 대상(Candidate)'**으로 관리.
- **3대 실행 과제**:
  1. 사내 데모 랩 기반 사전 기술 검증(PoC) 우선 추진 (Qwen2.5-Coder / Solar 대상 정밀 실측)
  2. 온프레미스 완전 폐쇄망(Air-Gap) 컨테이너 Appliance 패키징 및 오프라인 인증 검토
  3. 특정 고객 요구 시 제안하는 '선택형 확장 옵션(Optional Add-on)' 파트너십 협의

---

## 3. 검증 결과
- HTML 및 DOCX 파일 동시 생성 및 완전 일치 완료.
- 파일 크기: DOCX 약 41.7 KB / HTML 약 15.3 KB.
