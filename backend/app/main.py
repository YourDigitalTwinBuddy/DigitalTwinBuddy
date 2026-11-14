# -*- coding: utf-8 -*-
"""
backend/app/main.py
Karmic AI Platform: Multi-Tenant Cloud SaaS & PaaS Core
Zero-Laptop Dependency • Productivity & Health Themes • Simple UID/PWD Auth • Mobile Telemetry & File Analyzer
"""

import os
import uuid
import hashlib
from datetime import datetime
from typing import Dict, Any, List, Optional
from fastapi import FastAPI, HTTPException, Body, Header
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
    version="1.1.0"
)

# Enable CORS for Web, Mobile PWA, and external APIs
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =============================================================================
# SIMPLE UID / PWD AUTHENTICATION & MULTI-TENANT IDENTITY (SaaS / PaaS)
# =============================================================================
SALT = "karmic_sovereign_salt_2026"

def hash_password(password: str) -> str:
    return hashlib.sha256((password + SALT).encode("utf-8")).hexdigest()

# In-memory user credential & tenant store (synced with Supabase)
USERS_DB: Dict[str, Dict[str, Any]] = {
    "digitaltwinbuddy@gmail.com": {
        "id": "00000000-0000-0000-0000-000000000001",
        "email": "digitaltwinbuddy@gmail.com",
        "password_hash": hash_password("TwinBuddy2026!"),
        "full_name": "Navin (Digital Twin Buddy)",
        "tier": "executive",
        "created_at": "2026-11-13T00:00:00"
    }
}

SESSION_TOKENS: Dict[str, str] = {
    "token_navin_default": "digitaltwinbuddy@gmail.com"
}

def get_current_user_email(auth_header: Optional[str] = Header(None)) -> str:
    if auth_header and auth_header.startswith("Bearer "):
        token = auth_header.split(" ")[1]
        if token in SESSION_TOKENS:
            return SESSION_TOKENS[token]
    return "digitaltwinbuddy@gmail.com"

@app.post("/api/auth/register")
async def register(payload: Dict[str, Any] = Body(...)):
    email = payload.get("email", "").strip().lower()
    password = payload.get("password", "").strip()
    full_name = payload.get("full_name", "").strip() or email.split("@")[0].capitalize()

    if not email or "@" not in email:
        raise HTTPException(status_code=400, detail="Valid email required")
    if len(password) < 6:
        raise HTTPException(status_code=400, detail="Password must be at least 6 characters")
    if email in USERS_DB:
        raise HTTPException(status_code=400, detail="User with this email already exists")

    user_id = str(uuid.uuid4())
    user_record = {
        "id": user_id,
        "email": email,
        "password_hash": hash_password(password),
        "full_name": full_name,
        "tier": "pro",
        "created_at": datetime.utcnow().isoformat()
    }
    USERS_DB[email] = user_record
    
    # Store in Supabase
    await supabase_service.insert_record("users", {
        "id": user_id,
        "email": email,
        "full_name": full_name,
        "tier": "pro"
    })
    
    # Create default digital twin profile
    await supabase_service.insert_record("digital_twin_profiles", {
        "user_id": user_id,
        "twin_name": f"{full_name}'s Digital Twin",
        "tone_style": "Executive, Concise & Strategic",
        "vocabulary_rules": "Polite, direct, action-oriented"
    })

    token = f"token_{uuid.uuid4().hex[:16]}"
    SESSION_TOKENS[token] = email

    return {
        "status": "SUCCESS",
        "token": token,
        "user": {
            "id": user_id,
            "email": email,
            "full_name": full_name,
            "tier": "pro"
        }
    }

@app.post("/api/auth/login")
async def login(payload: Dict[str, Any] = Body(...)):
    email = payload.get("email", "").strip().lower()
    password = payload.get("password", "").strip()

    user = USERS_DB.get(email)
    if not user or user["password_hash"] != hash_password(password):
        raise HTTPException(status_code=401, detail="Invalid Email or Password")

    token = f"token_{uuid.uuid4().hex[:16]}"
    SESSION_TOKENS[token] = email

    return {
        "status": "SUCCESS",
        "token": token,
        "user": {
            "id": user["id"],
            "email": user["email"],
            "full_name": user["full_name"],
            "tier": user["tier"]
        }
    }

@app.get("/api/auth/me")
async def get_me(authorization: Optional[str] = Header(None)):
    email = get_current_user_email(authorization)
    user = USERS_DB.get(email, USERS_DB["digitaltwinbuddy@gmail.com"])
    return {
        "user": {
            "id": user["id"],
            "email": user["email"],
            "full_name": user["full_name"],
            "tier": user["tier"]
        }
    }

# =============================================================================
# SYSTEM HEALTH & PROFILE
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
        "active_llm_model": settings.GROQ_MODEL,
        "total_registered_users": len(USERS_DB)
    }

@app.get("/api/twin/profile")
async def get_profile(authorization: Optional[str] = Header(None)):
    email = get_current_user_email(authorization)
    user = USERS_DB.get(email, USERS_DB["digitaltwinbuddy@gmail.com"])
    return {
        "user_id": user["id"],
        "full_name": user["full_name"],
        "email": user["email"],
        "twin_name": f"{user['full_name']}'s Chief-of-Staff",
        "tone_style": "Executive, Strategic & Empathetic",
        "vocabulary_rules": "Direct, cordial, high-signal, zero corporate jargon",
        "status": "SYNCHRONIZED_ACTIVE"
    }

# =============================================================================
# THEME 1: PRODUCTIVITY & EFFICIENCY
# =============================================================================
@app.get("/api/productivity/inbox")
async def get_inbox():
    return await email_agent.get_demo_inbox()

@app.post("/api/productivity/email/ingest")
async def ingest_email(payload: Dict[str, Any] = Body(...), authorization: Optional[str] = Header(None)):
    """
    Ingests and triages a new incoming email in real time with Groq.
    """
    email = get_current_user_email(authorization)
    user = USERS_DB.get(email, USERS_DB["digitaltwinbuddy@gmail.com"])
    profile = await get_profile(authorization)
    
    email_data = {
        "id": str(uuid.uuid4()),
        "user_id": user["id"],
        "sender_name": payload.get("sender_name", "Incoming Sender"),
        "sender_email": payload.get("sender_email", "sender@domain.com"),
        "subject": payload.get("subject", "No Subject"),
        "snippet": payload.get("body", payload.get("snippet", ""))
    }
    
    result = await email_agent.triage_inbox_item(email_data, profile)
    await supabase_service.insert_record("email_inbox", result)
    return result

@app.get("/api/productivity/storage")
async def get_storage_overview(authorization: Optional[str] = Header(None)):
    email = get_current_user_email(authorization)
    user = USERS_DB.get(email, USERS_DB["digitaltwinbuddy@gmail.com"])
    return await storage_agent.analyze_storage_bloat(user["id"])

@app.post("/api/mobile/storage/analyze-batch")
async def analyze_mobile_storage_batch(files: List[Dict[str, Any]] = Body(...), authorization: Optional[str] = Header(None)):
    """
    Client-side file picker sends list of files (name, size, type) from phone/laptop.
    Agent scans for duplicates, heavy files (>100MB), and returns a clean-up recipe.
    """
    email = get_current_user_email(authorization)
    user = USERS_DB.get(email, USERS_DB["digitaltwinbuddy@gmail.com"])
    
    analyzed_items = []
    seen_names = set()
    total_reclaimable_mb = 0.0

    for f in files:
        fname = f.get("name", "file")
        fsize_mb = round(float(f.get("size_bytes", 0)) / (1024 * 1024), 2)
        base_name = fname.rsplit(".", 1)[0].lower()

        is_duplicate = False
        recom = "File appears unique."
        ftype = "STANDARD_FILE"

        if base_name in seen_names:
            is_duplicate = True
            ftype = "DUPLICATE_PHOTO" if any(fname.lower().endswith(ext) for ext in [".jpg", ".jpeg", ".png", ".heic"]) else "DUPLICATE_FILE"
            recom = f"Duplicate file detected. Retain primary file and purge copy."
            total_reclaimable_mb += fsize_mb
        elif fsize_mb > 150:
            ftype = "LARGE_VIDEO" if any(fname.lower().endswith(ext) for ext in [".mp4", ".mov", ".mkv", ".avi"]) else "HEAVY_ARCHIVE"
            recom = f"Large file ({fsize_mb} MB). Recommend compressing or cold-archiving."
            total_reclaimable_mb += fsize_mb
        elif "whatsapp" in fname.lower() or "telegram" in fname.lower():
            ftype = "CHAT_DUMP"
            recom = "Chat cache media dump. Safe to clean."
            total_reclaimable_mb += fsize_mb

        seen_names.add(base_name)
        analyzed_items.append({
            "id": str(uuid.uuid4()),
            "user_id": user["id"],
            "file_name": fname,
            "file_size_mb": fsize_mb,
            "file_type": ftype,
            "is_reclaimable": is_duplicate or fsize_mb > 150 or ftype == "CHAT_DUMP",
            "recommendation": recom
        })

    # Stage action in queue if reclaimable space found
    if total_reclaimable_mb > 0:
        await supabase_service.insert_record("pending_actions", {
            "id": str(uuid.uuid4()),
            "user_id": user["id"],
            "agent_name": "Mobile Storage Optimization Agent",
            "action_type": "DELETE_STORAGE",
            "title": f"Reclaim {round(total_reclaimable_mb / 1024, 2)} GB from Selected Device Files",
            "description": f"Purge {len([i for i in analyzed_items if i['is_reclaimable']])} identified duplicate & heavy items.",
            "impact_preview": f"Frees up {round(total_reclaimable_mb, 1)} MB of storage space immediately.",
            "status": "PENDING"
        })

    return {
        "status": "COMPLETED",
        "total_files_scanned": len(files),
        "total_reclaimable_gb": round(total_reclaimable_mb / 1024, 2),
        "items": analyzed_items
    }

@app.get("/api/productivity/digest")
async def get_social_digest(authorization: Optional[str] = Header(None)):
    email = get_current_user_email(authorization)
    user = USERS_DB.get(email, USERS_DB["digitaltwinbuddy@gmail.com"])
    digests = await supabase_service.get_table_data("social_digests", limit=1)
    if digests:
        return digests[0]
    return await social_agent.generate_daily_digest(user["id"])

@app.post("/api/productivity/digest/generate")
async def generate_digest(authorization: Optional[str] = Header(None)):
    email = get_current_user_email(authorization)
    user = USERS_DB.get(email, USERS_DB["digitaltwinbuddy@gmail.com"])
    return await social_agent.generate_daily_digest(user["id"])

# =============================================================================
# THEME 2: HEALTH & FITNESS DIGITAL TWIN & MOBILE TELEMETRY
# =============================================================================
@app.get("/api/health-twin/status")
async def get_health_status(authorization: Optional[str] = Header(None)):
    email = get_current_user_email(authorization)
    user = USERS_DB.get(email, USERS_DB["digitaltwinbuddy@gmail.com"])
    logs = await supabase_service.get_table_data("health_logs", limit=1)
    if logs:
        return logs[0]
    return await health_agent.evaluate_daily_biometrics(user["id"], {
        "sleep_hours": 7.6,
        "deep_sleep_hours": 1.6,
        "rem_sleep_hours": 1.7,
        "hrv_ms": 72,
        "resting_hr": 58,
        "steps": 9400
    })

@app.post("/api/mobile/telemetry/sync")
async def sync_mobile_telemetry(payload: Dict[str, Any] = Body(...), authorization: Optional[str] = Header(None)):
    """
    Webhook for iPhone (via iOS Shortcuts) and Android (via Health Connect API)
    Syncs live steps, battery, sleep, and HRV.
    """
    email = get_current_user_email(authorization)
    user = USERS_DB.get(email, USERS_DB["digitaltwinbuddy@gmail.com"])
    
    telemetry = {
        "sleep_hours": float(payload.get("sleep_hours", 7.5)),
        "deep_sleep_hours": float(payload.get("deep_sleep_hours", 1.5)),
        "rem_sleep_hours": float(payload.get("rem_sleep_hours", 1.6)),
        "hrv_ms": int(payload.get("hrv_ms", 65)),
        "resting_hr": int(payload.get("resting_hr", 60)),
        "steps": int(payload.get("steps", 8500)),
        "device_type": payload.get("device_type", "Mobile Device (iOS/Android)"),
        "battery_pct": payload.get("battery_pct", 85)
    }
    
    result = await health_agent.evaluate_daily_biometrics(user["id"], telemetry)
    return {
        "status": "TELEMETRY_SYNCHRONIZED",
        "device": telemetry["device_type"],
        "readiness_score": result["recovery_score"],
        "circadian_status": result["circadian_status"],
        "calendar_recommendation": result["calendar_recommendation"]
    }

# =============================================================================
# PAAS AGENT STUDIO
# =============================================================================
@app.get("/api/agents")
async def list_agents(authorization: Optional[str] = Header(None)):
    email = get_current_user_email(authorization)
    user = USERS_DB.get(email, USERS_DB["digitaltwinbuddy@gmail.com"])
    return await agent_studio.list_agents(user["id"])

@app.post("/api/agents")
async def create_agent(agent_data: Dict[str, Any] = Body(...), authorization: Optional[str] = Header(None)):
    email = get_current_user_email(authorization)
    user = USERS_DB.get(email, USERS_DB["digitaltwinbuddy@gmail.com"])
    return await agent_studio.create_agent(user["id"], agent_data)

@app.post("/api/agents/{agent_id}/run")
async def run_agent_scenario(agent_id: str, payload: Dict[str, Any] = Body(...), authorization: Optional[str] = Header(None)):
    email = get_current_user_email(authorization)
    user = USERS_DB.get(email, USERS_DB["digitaltwinbuddy@gmail.com"])
    return await agent_studio.run_scenario(user["id"], agent_id, payload.get("input", ""))

# =============================================================================
# HUMAN-IN-THE-LOOP (HITL) APPROVAL QUEUE
# =============================================================================
@app.get("/api/actions/pending")
async def get_pending_actions(authorization: Optional[str] = Header(None)):
    actions = await supabase_service.get_table_data("pending_actions")
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
    status = resolution.get("status", "APPROVED")
    await supabase_service.update_record("pending_actions", "id", action_id, {"status": status})
    return {"action_id": action_id, "status": status, "message": f"Action marked as {status}"}

# =============================================================================
# DIGITAL TWIN COMMAND CENTER (PWA ROOT)
# =============================================================================
@app.get("/", response_class=HTMLResponse)
async def serve_dashboard():
    template_path = os.path.join(os.path.dirname(__file__), "templates", "index.html")
    if os.path.exists(template_path):
        with open(template_path, "r", encoding="utf-8") as f:
            return f.read()
    root_index = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "index.html")
    if os.path.exists(root_index):
        with open(root_index, "r", encoding="utf-8") as f:
            return f.read()
    return "<h1>Karmic AI Platform is Running!</h1>"

print("Karmic AI Platform Multi-Tenant Core v1.1.0 Loaded.")
