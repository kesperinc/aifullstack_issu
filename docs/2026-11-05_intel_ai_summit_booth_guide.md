================================================================
 MZC-Intel AI 부스 전시 통합 패키지 (단일 폴더 배포용)
 행사명: Intel AI Summit Seoul 2026
 일시/장소: 2026-11-12(목) 코엑스 1F 그랜드볼룸 Gold 부스
 주관: 메가존클라우드(MegazoneCloud) AI & Unity 비즈니스 조직
================================================================

[ 핵심 1-Click 실행 안내 ]
  1. 부스 쇼케이스 무한 루프 실행 : run_kiosk.bat 더블클릭
     -> 부스 대형 모니터용 통합 5단계 순환 루프 플레이어 즉시 실행
     -> 재생 순서 (총 약 19분 30초 무한 반복 루프):
        ① MZC-Intel AI FULL STACK (1분 50초)
        ② Nota AI 경량화 벤치마크 (2분 00초)
        ③ Alioth Coder 자율 코딩 에이전트 (3분 00초)
        ④ Articul8 행사영상 (7분 03초)
        ⑤ Unity Industry on Intel (5분 15초 - Asset Transformer & Physical AI 슬라이드 자동 루프)
        -> ⑤번이 끝나면 자동으로 ①번으로 돌아가 무한 반복 재생됩니다!
     -> 주요 단축키:
        - 1 / 2 / 3 / 4 / 5 : 해당 쇼케이스 파트로 즉시 점프 (고객 문의 시 즉시 전환)
        - Space             : 일시정지 / 재생
        - M                 : 영상 음소거 해제/설정
        - F                 : 1920x1080 전체화면 토글
        - Alt+F4            : 키오스크 종료

  2. 유니티 단독 발표 / 세션 진행 : run_unity_presentation.bat 더블클릭
     -> 유니티 7-Slide 10분 키노트 전용 키오스크 즉시 실행
     -> 주요 단축키:
        - Space : 자동 재생 / 일시정지
                - G     : 전체 7개 슬라이드 목차 보기
        - F     : 전체화면 토글
        - Alt+F4: 종료

  3. 관람객 실시간 Vibe 코딩 체험 : MZC_Intel_Vibe_Coding_Interactive_Demo.html 열기
     -> AI 엔지니어 및 관람객 대상 실시간 파이썬/자바 Vibe 코딩 라이브 시연

================================================================
[ 단일 폴더 내 파일 목록 및 역할 ]
================================================================
  [부스 무한루프 쇼케이스 메인]
  - Showcase_Master_Player.html              : 5개 쇼케이스(유니티 포함) 자동 순환 마스터 플레이어
  - run_kiosk.bat                            : 부스 쇼케이스 1-Click 실행기 (추천!)
  - MZC_Intel_AI_FullStack_Showcase.html     : ① MZC-Intel 풀스택 AI 쇼케이스
  - Nota_Benchmark_Showcase_261015.html      : ② Nota on Intel 엣지 경량화 벤치마크
  - Alioth_Coder_Showcase_261019_단독실행.html : ③ Alioth 코더 에이전트 쇼케이스
  - Articul8_FullstackAI_행사영상_KR_v2.mp4   : ④ Articul8 행사 고화질 영상
  - Articul8_FullstackAI_행사영상_KR_v2.srt   : ④ 행사 영상 한글 자막
  - Unity_발표자료.html                       : ⑤ 유니티 부스 전시/발표 메인 HTML 
  - run_unity_presentation.bat               : 유니티 발표자료 단독 1-Click 실행기
  - unity_presentation_assets/               : 유니티 핵심 데모 영상(GIF) 및 그래픽 에셋
  - 2026-11-05_Intel_행사_Unity_핵심맥락_최종정리본.md : 10분 발표 대본 및 핵심 맥락 요약서
  - Unity_발표자료.pptx                       : 유니티 최신 원본 파워포인트 (인쇄/편집용)
  - Unity_소개.pdf                            : 보조 소개 자료

  [관람객 체험 데모]
  - MZC_Intel_Vibe_Coding_Interactive_Demo.html : Vibe 코딩 & FIM 라이브 시연기

================================================================
[ 타인 전달 방법 ]
================================================================
이 폴더('Intel_AI_Summit_Seoul_2026_부스전시자료')를 통째로 ZIP으로 압축하여
이메일, 슬랙, USB 등으로 전달하시면 받는 분 PC에서 브라우저만으로 즉시 작동합니다.


================================================================
 [ 행사 플랫폼 등록용 : 솔루션 및 전시 타이틀 / 데모 및 솔루션 개요 최종본 ]
================================================================
[솔루션 및 전시타이틀]
Intel 기반 메가존클라우드 AI Full Stack: Articul8 엔터프라이즈 GenAI부터 Unity Physical AI까지
(부제: 개방형 4-Layer 인프라·초경량 모델 최적화·자율 코딩 에이전트·온디바이스 Physical AI를 아우르는 엔터프라이즈 AI 턴키 솔루션)
[데모 및 솔루션 개요]
1. [발표 & 코어 플랫폼] Articul8 엔터프라이즈 GenAI & MZC-Intel 4-Layer AI Full Stack
- 제조/금융/중공업 구축 사례 기반 사내 도면·기술문서 지식그래프(Knowledge Graph) 고정밀 RAG 시연 (환각 제로화)
- Intel Xeon 6 & Gaudi 3 최적화 ModelMesh™ 지능형 멀티 모델 실시간 라우팅 및 100% 에어갭 폐쇄망 인프라 (3개년 TCO 52% 절감)
2. [모델 최적화 & 자율 코딩] Nota AI 초경량화 & Alioth Coder (Vibe Coding / FIM)
- NetsPresso 기반 LLM(Solar/Llama-3) INT4 양자화 압축 및 Intel 서버·AI PC(Core Ultra NPU) 초고속 추론 벤치마크 (레이턴시 최대 4.1배 개선)
- 사내 소스코드 유출 없는 폐쇄망 자율 코딩 에이전트(Alioth Coder) 전시 
3. [산업용 디지털 트윈 & 로보틱스] Unity Industry & Physical AI on Intel
- 70+ 산업용 CAD/BIM 원본 데이터를 1-Click 경량화하는 Asset Transformer 및 클라우드 3D 스트리밍(3DDS)
- Unity Sentis 기반 Intel Core Ultra NPU/Arc GPU 초저지연 온디바이스 AI 추론 및 Simulation Pro·ROS2 직결 Sim2Real
4. [부스 디스플레이 상영] 5대 핵심 쇼케이스 통합 키오스크(Auto-loop HTML5) 상시 게시 및 관람객 핸즈온 체험
