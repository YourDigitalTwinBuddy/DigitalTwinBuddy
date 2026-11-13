# Karmic AI Platform: Cloud-Native SaaS Setup & Action Plan
**Zero Laptop Dependency • 100% Free Cloud Infrastructure • Productivity & Health Themes**  
*Document Version: 1.0.0 | Release: Operational Execution Plan*

---

## 1. Executive Summary & Strategy

We are building the **Karmic AI Platform** as a genuine **Software as a Service (SaaS)** with **zero dependency on running your laptop 24/7**.

```mermaid
flowchart TD
    subgraph User_Touchpoints ["User Touchpoints (Any Browser or Mobile Phone)"]
        WebUI["Next.js 15 PWA Dashboard (Hosted on Vercel)"]
        MobileApp["Mobile Responsive / PWA (iOS & Android)"]
    end

    subgraph Free_Cloud_Backend ["Free Cloud Backend & Database (24/7 Serverless)"]
        API["FastAPI / LangGraph Multi-Agent Engine (Render.com / Koyeb)"]
        DB["Supabase Managed PostgreSQL 16 + pgvector + Auth"]
    end

    subgraph Free_Cloud_AI ["Free Cloud AI Foundation (Zero $ Token Cost)"]
        Groq["Groq Cloud: Llama 3.3 70B (300+ tokens/sec for fast email triage)"]
        Gemini["Google AI Studio: Gemini 2.0 / 1.5 Flash (1M context for large digests)"]
    end

    WebUI <--> API
    MobileApp <--> API
    API <--> DB
    API <--> Groq
    API <--> Gemini
```

---

## 2. The 5 Free Accounts for You to Create

To keep this project isolated, clean, and production-ready, please create new accounts using a dedicated email (e.g. `karmic.ai.platform@gmail.com` or your primary email) at these 5 services:

| Service | Signup URL | Purpose & Free Quota | What You Will Get |
| :--- | :--- | :--- | :--- |
| **1. GitHub** | [github.com/join](https://github.com/join) | Code repository, version control, automated cloud deployments. | GitHub Username & Personal Access Token (PAT). |
| **2. Supabase** | [supabase.com](https://supabase.com) | Managed PostgreSQL 16 + `pgvector` + User Authentication. Free 500MB DB & 50,000 MAU. | Project URL, Anon Public Key, Service Role Secret, Database Connection String. |
| **3. Groq Cloud** | [console.groq.com](https://console.groq.com) | Ultra-fast Llama 3.3 70B & 8B inference (300+ tokens/sec) for sub-second email triage. | Groq API Key (starts with `gsk_...`). |
| **4. Google AI Studio** | [aistudio.google.com](https://aistudio.google.com) | Gemini 2.0 / 1.5 Flash (1,500 requests/day, 1M context window) for social & document digests. | Gemini API Key (starts with `AIza...`). |
| **5. Vercel** | [vercel.com/signup](https://vercel.com/signup) | Global edge hosting for our Next.js 15 Web/Mobile PWA dashboard. | Log in using your new GitHub account. |

---

## 3. Clear Flow of Actions: Your Actions vs. My Actions

```mermaid
sequenceDiagram
    autonumber
    actor User as You (Product Owner)
    participant AI as Antigravity (AI Lead)
    participant Cloud as Cloud Platforms (Supabase, Vercel, Groq)
    
    User->>AI: 1. Reviews Setup Plan & Confirms Themes
    User->>Cloud: 2. Signs up for 5 free accounts & grabs API keys
    User->>AI: 3. Supplies credentials via secure .env.cloud
    AI->>Cloud: 4. Deploys Database Schema & Vector Tables (Supabase)
    AI->>Cloud: 5. Deploys Backend Agent API & Next.js UI (Render & Vercel)
    AI->>User: 6. Delivers live Web & Mobile PWA URL
    User->>Cloud: 7. Connects test Google account & tests Email Clean-up & Health
    User->>User: 8. Invites 5-10 Pilot Users to test!
```

| Phase | Your Actions (Product Owner) | My Actions (Antigravity AI Engineer) |
| :--- | :--- | :--- |
| **Phase 1: Accounts & Setup (Days 1–2)** | • Create the 5 free accounts (GitHub, Supabase, Groq, Google AI Studio, Vercel).<br>• Copy the keys into `.env.cloud`. | • Deliver this action guide and configuration template.<br>• Build an automated credential validation script.<br>• Initialize multi-tenant project repository. |
| **Phase 2: Database & Core Engine (Days 3–6)** | • Execute provided SQL migration script in Supabase SQL editor with 1 click.<br>• Authorize test Google OAuth app. | • Implement multi-tenant database tables with pgvector.<br>• Build LangGraph multi-agent supervisor state machine.<br>• Wire up dual model router (Groq + Gemini). |
| **Phase 3: Theme 1 - Productivity (Days 7–13)** | • Test Email Clean-up on sample inbox.<br>• Review storage clean-up suggestions.<br>• Verify 3-minute executive social digest. | • **Feature 1A**: Autonomous Email Clean-Up & Smart Triage.<br>• **Feature 1B**: Mobile Storage Bloat Scanner (iOS/Android photo/file optimizer).<br>• **Feature 1C**: Social Media & Info Stream Digest Synthesizer. |
| **Phase 4: Theme 2 - Health Twin (Days 14–20)**| • Enter sample biometric metrics (sleep, steps, recovery).<br>• Review circadian-adjusted calendar focus blocks. | • **Feature 2A**: Biometric Telemetry & Daily Health Score.<br>• **Feature 2B**: Circadian-Aware Calendar Adaptor.<br>• **Feature 2C**: Personalized Longevity Protocol Assistant. |
| **Phase 5: Cloud Launch & Pilot (Days 21–28)** | • Send Supabase Auth invite link to 5–10 pilot users.<br>• Collect feedback on time saved and delight. | • Deploy live production build to Vercel and Render.<br>• Build the interactive Agent Studio and HITL 1-click Approval Queue UI.<br>• Monitor cloud logs and response latency. |

---

## 4. Granular Technical Blueprints for Themes 1 & 2

### Theme 1: Productivity & Efficiency Suite
1. **Feature 1A: Email Clean-Up & Smart Triage**:
   - Classifies inbound mail: Promotional, Cold Outreach, Transactional, High-Priority.
   - Generates 1-click unsubscribe links and bulk archive recommendations.
   - For executive emails: Generates draft replies matching the user's authentic voice, staged in the Human-in-the-Loop approval queue.
2. **Feature 1B: Mobile Storage Management (iOS & Android Cloud Assistant)**:
   - Connects to Google Drive, iCloud, or mobile storage telemetry.
   - Detects duplicate photos, massive unused video files (>500MB), stale downloads, and WhatsApp/Telegram media bloat.
   - Generates a "Storage Reclaim Recipe" allowing users to free 10GB–50GB with 1 click.
3. **Feature 1C: Social Media & Communication Stream Digest**:
   - Ingests RSS feeds, Substack newsletters, Twitter/X threads, and LinkedIn updates.
   - Synthesizes an executive 3-minute read: "What happened today, who said what, and key action points."

### Theme 2: Health & Fitness Digital Twin
1. **Feature 2A: Biometric Telemetry & Daily Health Score**:
   - Ingests sleep architecture (Deep, REM), resting heart rate, HRV, and daily steps.
   - Calculates a normalized daily "Cognitive & Physical Readiness Score".
2. **Feature 2B: Circadian-Aware Schedule Adaptor**:
   - Dynamically protects the calendar on low-recovery days (e.g. inserts focus buffers, reschedules non-urgent late calls, suggests low-impact workouts).
3. **Feature 2C: Personalized Longevity Protocol Coach**:
   - Proactive hydration milestones, mobility breaks during long desk sessions, and nutritional timing recommendations.

---

## 5. Web & Mobile UI (PWA) Architecture

The frontend is a modern **Next.js 15 Progressive Web App (PWA)** that installs directly on iPhones and Android devices with a native app feel:
- **Digital Twin Command Center**: Morning briefing, health recovery score, email cleanup status, and storage reclaim stats on a single dashboard.
- **Agent Studio & Scenario Builder**: An interactive screen where users can create custom agents (e.g. "Newsletter Summarizer", "VIP Inbox Guard", "Workout Scheduler") and specify execution schedules.
- **Human-in-the-Loop (HITL) Approval Queue**: Safety-first 1-click "Approve & Execute" or "Edit" buttons before any email is sent or file is archived.

---

## 6. Template `.env.cloud` File

Create a file named `.env.cloud` in the project root with the following fields:

```env
# =================================================================
# KARMIC AI PLATFORM - CLOUD CONFIGURATION
# =================================================================

# 1. Supabase (Managed Postgres + pgvector + Auth)
SUPABASE_URL=https://your-project-id.supabase.co
SUPABASE_ANON_KEY=eyJhbGciOi...
SUPABASE_SERVICE_ROLE_KEY=eyJhbGciOi...
DATABASE_URL=postgresql://postgres:[YOUR-PASSWORD]@db.your-project-id.supabase.co:5432/postgres

# 2. Groq Cloud (Free Llama 3.3 70B Inference)
GROQ_API_KEY=gsk_...

# 3. Google AI Studio (Free Gemini 2.0 / 1.5 Flash Inference)
GEMINI_API_KEY=AIza...

# 4. App & Security Settings
JWT_SECRET=generate-a-random-32-char-secret
ENVIRONMENT=production
FRONTEND_URL=https://karmic-ai.vercel.app
```

