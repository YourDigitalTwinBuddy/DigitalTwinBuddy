# -*- coding: utf-8 -*-
"""
backend/app/main.py
Karmic AI Platform: Multi-Tenant Cloud SaaS & PaaS Core
Zero-Laptop Dependency • Productivity & Health Themes • Multi-Agent Studio
"""

import os
from typing import Dict, Any, List
from fastapi import FastAPI, HTTPException, Body
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

from backend.app.config import settings
from backend.app.services.supabase_service import supabase_service
from backend.app.services.llm_service import llm_service
from backend.app.agents.email_agent import email_agent
from backend.app.agents.storage_agent import storage_agent
from backend.app.agents.social_digest_agent import social_agent
from backend.app.agents.health_agent import health_agent
from backend.app.agents.agent_studio import agent_studio

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="Sovereign Personal Digital Twin & Autonomous Agentic OS",
    version="1.0.0"
)

# Enable CORS for Web, Mobile PWA, and external APIs
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DEMO_USER_ID = "00000000-0000-0000-0000-000000000001"

# =============================================================================
# 1. SYSTEM HEALTH & IDENTITY
# =============================================================================
@app.get("/api/health")
async def health_check():
    return {
        "status": "HEALTHY",
        "platform": settings.PROJECT_NAME,
        "admin_email": settings.ADMIN_EMAIL,
        "supabase_connected": bool(settings.SUPABASE_URL and settings.SUPABASE_SERVICE_ROLE_KEY),
        "groq_connected": bool(settings.GROQ_API_KEY),
        "gemini_connected": bool(settings.GEMINI_API_KEY),
        "active_llm_model": settings.GROQ_MODEL
    }

@app.get("/api/twin/profile")
async def get_profile():
    return {
        "user_id": DEMO_USER_ID,
        "full_name": "Navin (Digital Twin Buddy)",
        "email": settings.ADMIN_EMAIL,
        "twin_name": "Karmic Sovereign Chief-of-Staff",
        "tone_style": "Executive, Strategic & Empathetic",
        "vocabulary_rules": "Direct, cordial, high-signal, zero corporate jargon",
        "status": "SYNCHRONIZED_ACTIVE"
    }

# =============================================================================
# 2. THEME 1: PRODUCTIVITY & EFFICIENCY
# =============================================================================
@app.get("/api/productivity/inbox")
async def get_inbox():
    return await email_agent.get_demo_inbox()

@app.post("/api/productivity/email/triage")
async def triage_email(email_data: Dict[str, Any] = Body(...)):
    profile = await get_profile()
    result = await email_agent.triage_inbox_item(email_data, profile)
    return result

@app.get("/api/productivity/storage")
async def get_storage_overview():
    return await storage_agent.analyze_storage_bloat(DEMO_USER_ID)

@app.get("/api/productivity/digest")
async def get_social_digest():
    digests = await supabase_service.get_table_data("social_digests", limit=1)
    if digests:
        return digests[0]
    return await social_agent.generate_daily_digest(DEMO_USER_ID)

@app.post("/api/productivity/digest/generate")
async def generate_digest(topics: str = "AI, Cloud Computing, Startups, Longevity"):
    return await social_agent.generate_daily_digest(DEMO_USER_ID, topics)

# =============================================================================
# 3. THEME 2: HEALTH & FITNESS DIGITAL TWIN
# =============================================================================
@app.get("/api/health-twin/status")
async def get_health_status():
    logs = await supabase_service.get_table_data("health_logs", limit=1)
    if logs:
        return logs[0]
    return await health_agent.evaluate_daily_biometrics(DEMO_USER_ID, {
        "sleep_hours": 7.6,
        "deep_sleep_hours": 1.6,
        "rem_sleep_hours": 1.7,
        "hrv_ms": 72,
        "resting_hr": 58,
        "steps": 9400
    })

@app.post("/api/health-twin/evaluate")
async def evaluate_health(telemetry: Dict[str, Any] = Body(...)):
    return await health_agent.evaluate_daily_biometrics(DEMO_USER_ID, telemetry)

# =============================================================================
# 4. PAAS AGENT STUDIO & CUSTOM SCENARIOS
# =============================================================================
@app.get("/api/agents")
async def list_agents():
    return await agent_studio.list_agents(DEMO_USER_ID)

@app.post("/api/agents")
async def create_agent(agent_data: Dict[str, Any] = Body(...)):
    return await agent_studio.create_agent(DEMO_USER_ID, agent_data)

@app.post("/api/agents/{agent_id}/run")
async def run_agent_scenario(agent_id: str, payload: Dict[str, Any] = Body(...)):
    return await agent_studio.run_scenario(DEMO_USER_ID, agent_id, payload.get("input", ""))

# =============================================================================
# 5. HUMAN-IN-THE-LOOP (HITL) APPROVAL QUEUE
# =============================================================================
@app.get("/api/actions/pending")
async def get_pending_actions():
    actions = await supabase_service.get_table_data("pending_actions")
    # Return default demo actions if none stored yet
    if not actions:
        return [
            {
                "id": "act-01",
                "agent_name": "Email Clean-Up & Triage Agent",
                "action_type": "SEND_EMAIL",
                "title": "Approve Reply to Satya Nadella",
                "description": "Subject: Re: Strategic Cloud Partnership: Q4 Roadmap Alignment",
                "impact_preview": "Hi Satya, thanks for reaching out. Delighted to hear from you. The updated Karmic architecture deck and technical specifications are prepared and attached for our Thursday alignment. Looking forward to reviewing together. Warm regards, Navin.",
                "status": "PENDING"
            },
            {
                "id": "act-02",
                "agent_name": "Mobile Storage Optimization Agent",
                "action_type": "DELETE_STORAGE",
                "title": "Reclaim 4.86 GB Storage on Phone & Cloud",
                "description": "Purge 2 duplicate burst photos, 1 stale 4K keynote recording (3.4GB), and WhatsApp forwarded batch.",
                "impact_preview": "Immediately reclaims 4.86 GB across iCloud & internal phone storage.",
                "status": "PENDING"
            },
            {
                "id": "act-03",
                "agent_name": "Circadian Longevity Twin",
                "action_type": "RESCHEDULE_CALENDAR",
                "title": "Insert 45-Min Afternoon Recovery Buffer",
                "description": "Biological readiness: 88%. Peak cognitive window concludes at 14:00. Insert rest buffer from 15:00 - 15:45.",
                "impact_preview": "Blocks meeting invites and silences non-urgent Slack notifications.",
                "status": "PENDING"
            }
        ]
    return actions

@app.post("/api/actions/{action_id}/resolve")
async def resolve_action(action_id: str, resolution: Dict[str, Any] = Body(...)):
    status = resolution.get("status", "APPROVED") # 'APPROVED' or 'REJECTED'
    await supabase_service.update_record("pending_actions", "id", action_id, {"status": status})
    return {"action_id": action_id, "status": status, "message": f"Action marked as {status}"}

# =============================================================================
# 6. DIGITAL TWIN COMMAND CENTER (RESPONSIVE WEB & MOBILE PWA UI)
# =============================================================================
@app.get("/", response_class=HTMLResponse)
async def serve_dashboard():
    with open(os.path.join(os.path.dirname(__file__), "templates", "index.html"), "r", encoding="utf-8") as f:
        return f.read()

print("Karmic AI Platform Backend Module Loaded.")

