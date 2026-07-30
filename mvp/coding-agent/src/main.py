"""
Enterprise Coding Agent OS Backend Main Server
FastAPI Web App (Port 8080) with REST API & MCP Router (Port 3000)
"""

import sys
from pathlib import Path

# Add src to sys.path
src_dir = Path(__file__).resolve().parent
if str(src_dir) not in sys.path:
    sys.path.insert(0, str(src_dir))

import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, Dict, Any

from adapters.llm_adapter import LLMAdapter
from vibe.engine import VibeEngine
from mcp.router import MCPRouter

app = FastAPI(
    title="Enterprise Coding Agent OS Backend API",
    description="Vibe Coding Orchestration Engine & MCP Gateway REST API",
    version="1.0.0"
)

# CORS 설정 (프론트엔드 HTML / 대시보드와 통신 연동)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 백엔드 핵심 서비스 인스턴스 초기화
llm_adapter = LLMAdapter(provider="desktop")
vibe_engine = VibeEngine(llm_adapter)
mcp_router = MCPRouter(port=3000)

# Request Models
class VibeRequest(BaseModel):
    intent: str
    target_file: Optional[str] = "auth_service.py"
    provider: Optional[str] = "desktop"

class ProviderSwitchRequest(BaseModel):
    provider: str

@app.get("/")
def read_root():
    return {
        "status": "online",
        "service": "Enterprise Coding Agent OS Backend Server",
        "mcp_gateway_port": 3000,
        "docs_url": "http://localhost:8080/docs"
    }

@app.get("/api/workspace/status")
def get_workspace_status():
    """
    샌드박스 상태 및 LLM/Syncthing 동기화 정보 반환
    """
    return {
        "status": "RUNNING",
        "active_sandbox": "Local Desktop Runner (.venv)",
        "llm_provider": llm_adapter.provider,
        "mcp_port": 3000,
        "syncthing_protected": True,
        "quota": {
            "used": 12.40,
            "total": 35.00
        }
    }

@app.post("/api/vibe/generate")
async def generate_vibe_code(req: VibeRequest):
    """
    Vibe 의도(Prompt)를 입력받아 자율 코드, Thinking, 샌드박스 셀프코렉션 결과 생성
    """
    if not req.intent.strip():
        raise HTTPException(status_code=400, detail="Intent prompt cannot be empty")
    
    if req.provider:
        llm_adapter.switch_provider(req.provider)
        
    result = await vibe_engine.execute_vibe(req.intent, req.target_file)
    return result

@app.post("/api/provider/switch")
def switch_llm_provider(req: ProviderSwitchRequest):
    """
    OpenRouter (Desktop) vs Red Hat OpenShift AI (RHOAI) 1-Click 스위칭
    """
    llm_adapter.switch_provider(req.provider)
    return {"status": "success", "current_provider": llm_adapter.provider}

@app.post("/api/mcp/rpc")
def mcp_json_rpc(payload: Dict[str, Any]):
    """
    MCP (Model Context Protocol) JSON-RPC 게이트웨이 엔드포인트
    """
    return mcp_router.handle_rpc_request(payload)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, reload=False)
