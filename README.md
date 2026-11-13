# Karmic AI Platform (DigitalTwinBuddy)
**Sovereign Personal Digital Twin & Autonomous Agentic OS**  
*Built for High-Leverage Productivity, Storage Optimization & Circadian Longevity*

---

## 🌟 Overview

**Karmic AI Platform** is a sovereign personal digital twin designed to bridge **Cognitive Agency**, **Autonomous Cyberspace Execution**, and **Physical Embodied Automation**.

Built on a **100% Free Cloud-Native Software as a Service (SaaS)** architecture, Karmic AI operates 24/7 without requiring your personal laptop to run continuously as a server.

---

## 🚀 Two Foundational Product Themes

### Theme 1: Productivity & Efficiency
1. **Email Clean-Up & Smart Triage**:
   - Ingests inboxes, classifies noise (Promotional, Cold Outreach, Transactional, VIP).
   - Generates 1-click bulk unsubscribe and archive recommendations.
   - For high-priority VIP messages: Synthesizes draft replies in your authentic voice, staged in the Human-in-the-Loop review queue.
2. **Mobile Storage Management (iOS & Android Cloud Assistant)**:
   - Identifies burst duplicate photos, massive unused video archives (>500MB), stale downloads, and chat media bloat (WhatsApp/Telegram).
   - Generates a visual 1-click **Storage Reclaim Recipe** to free up 10GB–50GB of cloud & phone space.
3. **Social Media & Newsletter Executive Digest**:
   - Ingests Substack newsletters, Twitter/X threads, and RSS feeds.
   - Synthesizes a high-signal, 3-minute executive read at 07:00 AM daily.

### Theme 2: Health & Fitness Digital Twin
1. **Biometric Telemetry & Daily Health Score**:
   - Tracks sleep architecture (Deep, REM), resting heart rate, HRV, and daily steps.
   - Calculates a normalized **Cognitive & Physical Readiness Score (0–100)**.
2. **Circadian-Aware Calendar Adaptor**:
   - Protects your work calendar on low-recovery days (inserts focus pauses, reschedules non-urgent evening calls, shifts workouts to low-impact recovery walks).
3. **Personalized Longevity Protocol Coach**:
   - Proactive hydration milestones, mobility breaks during long seated sessions, and nutritional timing aligned with workout demands.

---

## 🛠️ Multi-Tenant Cloud Architecture

| Subsystem | Cloud Provider | Specs & Quota |
| :--- | :--- | :--- |
| **Code & CI/CD** | **GitHub** | Version control & Vercel deployment webhooks |
| **Managed DB & Auth** | **Supabase** | PostgreSQL 16 with `pgvector` & built-in Auth |
| **High-Speed Inference** | **Groq Cloud** | Llama 3.3 70B & Qwen 2.5 (300+ tokens/sec) |
| **Large-Context Inference** | **Google AI Studio** | Gemini 3.8 Flash (1,500 req/day free) |
| **Frontend UI (PWA)** | **Vercel** | Global Edge CDN hosting for Next.js / PWA |
| **Agent Server** | **FastAPI / Python** | Asynchronous multi-agent supervisor |

---

## ⚡ Quickstart Guide (Running Locally)

```bash
# 1. Clone repository
git clone https://github.com/YourDigitalTwinBuddy/DigitalTwinBuddy.git
cd DigitalTwinBuddy

# 2. Setup Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate

# 3. Install Dependencies
pip install fastapi uvicorn httpx pydantic python-dotenv

# 4. Copy Environment Template
cp .env.example .env.cloud
# Populate .env.cloud with your keys

# 5. Launch Digital Twin Engine
python -m uvicorn backend.app.main:app --port 8000 --reload

# 6. Open Browser
# Web & Mobile UI: http://localhost:8000
# Interactive API Docs: http://localhost:8000/docs
```

---

## 🔐 Security & Human-in-the-Loop (HITL) Guardrails

All external actions (sending drafted emails, deleting duplicate files, moving calendar meetings) require explicit 1-click **"Approve & Execute"** in the **Action Queue** before any side effects are applied.

