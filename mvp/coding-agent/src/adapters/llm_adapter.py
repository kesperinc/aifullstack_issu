"""
LLM Provider Adapter Module
OpenRouter API (Cloud Stage) & Red Hat OpenShift AI vLLM (On-Prem Stage) 1-Click Switching
"""

import os
import httpx
from typing import Dict, Any, Optional

class LLMAdapter:
    def __init__(self, provider: str = "openrouter"):
        self.provider = provider
        self.openrouter_key = os.getenv("OPENROUTER_API_KEY", "")
        self.rhoai_url = os.getenv("RHOAI_VLLM_ENDPOINT_URL", "http://qwen-coder.rhoai.svc:8000/v1")

    def switch_provider(self, new_provider: str):
        if new_provider in ["openrouter", "rhoai_vllm", "desktop"]:
            self.provider = new_provider

    async def generate_response(self, prompt: str, system_prompt: Optional[str] = None) -> Dict[str, Any]:
        """
        LLM 응답 생성 어댑터
        """
        # 개발 단계 / Desktop 모드 및 OpenRouter 키 유무에 따른 Fallback 지원
        if self.provider in ["openrouter", "desktop"]:
            if not self.openrouter_key or self.openrouter_key == "your_openrouter_api_key_here":
                # OpenRouter Key가 미설정된 경우 시연용 초저지연 Vibe 렌더링 결과 반환
                return {
                    "provider": "Desktop Local Engine (Simulated)",
                    "thinking": [
                        "1. Vibe 자연어 의도 분석 ➔ 대상 파일: auth_service.py 식별",
                        "2. 동기 SQLAlchemy 조회를 AsyncSession 비동기 구조로 변환 규칙 적용",
                        "3. 샌드박스 pytest 자동 검증 트리거 (tests/test_auth.py)",
                        "4. AsyncSession await 미적용 오류 스택트레이스 파싱 ➔ 셀프코렉션 보정 완료"
                    ],
                    "code_filename": "auth_service.py",
                    "code_diff": """async def authenticate_user(db: AsyncSession, credentials: UserLogin):
+   async with db.begin():
+       result = await db.execute(select(User).where(User.email == credentials.email))
+       user = result.scalars().first()
+       if not user or not await verify_password_async(credentials.password, user.password_hash):
+           raise HTTPException(status_code=400, detail="Invalid credentials")
    return user""",
                    "terminal_log": "[Sandbox] Running 'pytest tests/test_auth.py'...\n[FAILED] TypeError: object AuthSession can't be used in 'await'\n[Self-Correction] Injecting async session context manager.\n[Sandbox] Re-running 'pytest tests/test_auth.py'...\n[SUCCESS] 4 passed in 0.35s. Vibe Self-correction done!"
                }
            
            # 실제 OpenRouter API 호출
            async with httpx.AsyncClient(timeout=30.0) as client:
                headers = {"Authorization": f"Bearer {self.openrouter_key}"}
                payload = {
                    "model": "qwen/qwen-2.5-coder-32b-instruct",
                    "messages": [
                        {"role": "system", "content": system_prompt or "You are an Enterprise Coding Agent specializing in Vibe Coding."},
                        {"role": "user", "content": prompt}
                    ]
                }
                res = await client.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)
                data = res.json()
                content = data["choices"][0]["message"]["content"]
                return {"provider": "OpenRouter Cloud API", "content": content}

        elif self.provider == "rhoai_vllm":
            # 사내 Red Hat OpenShift AI vLLM 엔드포인트 호출
            async with httpx.AsyncClient(timeout=30.0) as client:
                payload = {
                    "model": "Qwen/Qwen2.5-Coder-32B-Instruct",
                    "messages": [{"role": "user", "content": prompt}]
                }
                res = await client.post(f"{self.rhoai_url}/chat/completions", json=payload)
                data = res.json()
                return {"provider": "Red Hat OpenShift AI SNO vLLM", "content": data["choices"][0]["message"]["content"]}

        return {"error": "Invalid provider"}
