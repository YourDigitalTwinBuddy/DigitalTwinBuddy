# -*- coding: utf-8 -*-
"""
create_cloud_setup_docx.py
Generates the comprehensive document:
"Karmic AI Platform: Cloud-Native SaaS Setup, Account Credentials & Operational Action Plan"
"""

import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from helpers import (
    set_cell_background, set_cell_margins, add_header,
    add_p, add_bullet, add_callout, format_table
)

def build_cloud_setup_docx(filename="Karmic_AI_Cloud_Setup_and_Action_Plan.docx"):
    doc = docx.Document()
    
    # Page setup - Margins 0.8 inch
    for section in doc.sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)
        
    # Document Title Block
    p_title = doc.add_paragraph()
    p_title.paragraph_format.space_before = Pt(0)
    p_title.paragraph_format.space_after = Pt(2)
    r_title = p_title.add_run("KARMIC AI PLATFORM")
    r_title.font.name = 'Calibri'
    r_title.font.size = Pt(24)
    r_title.font.bold = True
    r_title.font.color.rgb = RGBColor(15, 23, 42) # Slate 900
    
    p_sub = doc.add_paragraph()
    p_sub.paragraph_format.space_before = Pt(0)
    p_sub.paragraph_format.space_after = Pt(14)
    r_sub = p_sub.add_run("Cloud-Native SaaS Implementation Blueprint & Step-by-Step Action Plan\nZero-Laptop Dependency • Free Cloud Services • Productivity & Health Themes • User/Agent Workflow")
    r_sub.font.name = 'Calibri'
    r_sub.font.size = Pt(12)
    r_sub.font.color.rgb = RGBColor(16, 149, 193) # Vibrant Cyan/Blue
    
    add_callout(
        doc,
        "OPERATIONAL EXECUTION DIRECTIVE",
        "This document provides the exact operational roadmap to build and deploy Karmic AI Platform as a true "
        "Cloud-Native Software as a Service (SaaS) with ZERO dependency on keeping your personal laptop running. "
        "It establishes the specific free cloud accounts you need to create, provides a transparent flow of responsibilities "
        "(Your Actions vs. My Actions), and specifies the complete product blueprint for our initial two foundational themes: "
        "(1) Productivity & Efficiency (Email Clean-up, Mobile Storage Management, Social Media Digest) and "
        "(2) Health & Fitness Digital Twin with an interactive Web/Mobile Agent Studio.",
        bg_hex="F0FDF4",
        border_color="16A34A"
    )
    
    # -------------------------------------------------------------
    # SECTION 1
    # -------------------------------------------------------------
    add_header(doc, "1. Architecture Blueprint: 100% Free Cloud SaaS (Zero Laptop Dependency)", level=1)
    
    add_p(doc, 
        "To achieve a true Software as a Service (SaaS) architecture without tying your laptop to a 24/7 power cord or managing local daemons, "
        "every layer of the Karmic AI Platform runs on resilient, permanent free-tier cloud infrastructure:")
    
    cloud_table = doc.add_table(rows=6, cols=4)
    cloud_headers = ["Platform Layer", "Free Cloud Service", "Free Tier Quota & Specs", "Role in Karmic AI SaaS"]
    cloud_data = [
        ["Code & CI/CD", "GitHub (New Dedicated Account)", "Unlimited public/private repos, 2,000 CI/CD mins/month", "Version control, automated testing, and continuous deployment webhooks."],
        ["Managed Database & Auth", "Supabase (Cloud PostgreSQL)", "500MB Postgres 16 + pgvector, 50,000 MAU, built-in Auth", "Multi-tenant user profiles, digital twin personas, vector embeddings, and session tokens."],
        ["Frontier AI Inference", "Groq Cloud + Google AI Studio", "Groq: Llama 3.3 70B (300 t/s); Google: Gemini 2.0 Flash (1,500 req/day)", "Dual cloud inference: Groq handles sub-second email triage; Gemini handles 1M-token large document digests."],
        ["Backend Multi-Agent API", "Render.com / Koyeb (Free Cloud Tier)", "512MB RAM serverless web service, automatic HTTPS, git deploy", "Runs Python FastAPI, LangGraph multi-agent state machines, and background cron schedules."],
        ["Frontend Web & Mobile PWA", "Vercel (Hobby Free Tier)", "Unlimited deployments, global edge CDN, custom domain support", "Hosts the Next.js 15 responsive Web & Mobile PWA dashboard for user interactions."]
    ]
    format_table(cloud_table, [1.5, 1.8, 1.8, 2.1], cloud_headers, cloud_data)
    doc.add_paragraph().paragraph_format.space_after = Pt(4)

    # -------------------------------------------------------------
    # SECTION 2
    # -------------------------------------------------------------
    add_header(doc, "2. Account Setup Checklist: Accounts for You to Create", level=1)
    
    add_p(doc, 
        "To keep Karmic AI Platform clean, secure, and isolated from your personal accounts, please create fresh accounts "
        "(using a dedicated project email such as 'karmic.ai.platform@gmail.com' or your primary email) at the following 5 platforms:")
    
    acc_table = doc.add_table(rows=6, cols=4)
    acc_headers = ["Service & Signup URL", "Account Type", "Information Needed for Development", "Action Required by You"]
    acc_data = [
        ["1. GitHub\nhttps://github.com/join", 
         "Free Developer Account", 
         "GitHub Username & Personal Access Token (PAT) with repo permissions.", 
         "Create account 'karmic-ai-platform' (or similar). Create a new private repository named 'karmic-ai-platform'."],
         
        ["2. Supabase\nhttps://supabase.com", 
         "Free Starter Tier", 
         "Project URL, anon public key, service_role secret, and DB connection string.", 
         "Sign up (via your new GitHub account), create a new project named 'karmic-db', and select your closest AWS region."],
         
        ["3. Groq Cloud\nhttps://console.groq.com", 
         "Free Developer Tier", 
         "Groq API Key (starts with 'gsk_...').", 
         "Sign up with Google/GitHub, navigate to 'API Keys', click 'Create API Key', and copy the key."],
         
        ["4. Google AI Studio\nhttps://aistudio.google.com", 
         "Free API Tier", 
         "Gemini API Key (starts with 'AIza...').", 
         "Sign in with Google, click 'Get API Key', create a key in a new project, and copy the key."],
         
        ["5. Vercel\nhttps://vercel.com/signup", 
         "Hobby Free Tier", 
         "Linked to your new GitHub account for 1-click deployments.", 
         "Sign up using 'Continue with GitHub' so Vercel can automatically deploy the frontend from our repo."]
    ]
    format_table(acc_table, [1.8, 1.3, 2.1, 2.0], acc_headers, acc_data)
    doc.add_paragraph().paragraph_format.space_after = Pt(4)

    add_callout(
        doc,
        "SECURITY & CREDENTIAL HANDLING PROTOCOL",
        "• NEVER share raw passwords in plain chat.\n"
        "• Once created, you will store your API keys and connection strings safely in a local '.env.cloud' configuration file on your machine.\n"
        "• I will provide an automated script that securely tests each key against its respective cloud service to verify connectivity before we deploy.",
        bg_hex="FEF3C7",
        border_color="D97706"
    )

    # -------------------------------------------------------------
    # SECTION 3
    # -------------------------------------------------------------
    add_header(doc, "3. Flow of Actions: Your Responsibilities vs. My Responsibilities", level=1)
    
    add_p(doc, 
        "To ensure seamless alignment and rapid velocity, here is the transparent division of labor across the project lifecycle:")
    
    flow_table = doc.add_table(rows=6, cols=3)
    flow_headers = ["Project Phase", "Your Actions (User / Product Owner)", "My Actions (Antigravity AI Engineer)"]
    flow_data = [
        ["Phase 1: Environment & Accounts (Days 1 - 2)", 
         "1. Create the 5 free cloud accounts (GitHub, Supabase, Groq, Google AI Studio, Vercel).\n2. Populate the template `.env.cloud` file with the generated API keys and DB strings.\n3. Review and approve the UI/UX workflow wireframes.",
         "1. Deliver this setup guide and the `.env.example` template.\n2. Write a diagnostic script to validate connectivity across all 5 accounts.\n3. Scaffold the complete multi-tenant repository structure (FastAPI + Next.js)."],
         
        ["Phase 2: Database & Core Agentic Engine (Days 3 - 7)", 
         "1. Run the Supabase SQL migration script (provided by me) in the Supabase SQL Editor with 1 click.\n2. Connect your test Gmail or Google Calendar account via OAuth2 settings page.", 
         "1. Write the database schema with pgvector indexes, agent state tables, and user twin profiles.\n2. Implement the LangGraph agent state machines and multi-model router (Groq + Gemini).\n3. Build the core MCP tool connectors."],
         
        ["Phase 3: Theme 1 Implementation - Productivity (Days 8 - 14)", 
         "1. Test Email Clean-up with real/test inbox.\n2. Inspect storage clean-up suggestions on test folders.\n3. Review generated daily Social Media / Newsletter briefing.", 
         "1. Build Feature 1A: Email Clean-Up Agent (auto-categorize, bulk unsubscribe, draft replies).\n2. Build Feature 1B: Mobile Storage Bloat Analyzer (photos, duplicate files, cloud drive bloat).\n3. Build Feature 1C: Social Media & Email Summary Digest Synthesizer."],
         
        ["Phase 4: Theme 2 Implementation - Health & Fitness (Days 15 - 21)", 
         "1. Input sample biometric / routine data (or sync wearable test webhook).\n2. Review health-informed schedule suggestions (e.g. recovery-based focus pauses).", 
         "1. Build Feature 2A: Health Twin Telemetry Ingestion (Sleep, HRV, steps, hydration).\n2. Build Feature 2B: Circadian Schedule Adaptor (dynamic calendar protection).\n3. Build Feature 2C: Personalized Longevity Protocol Assistant."],
         
        ["Phase 5: Cloud Deployment & Pilot Onboarding (Days 22 - 28)", 
         "1. Invite 5 - 10 pilot users via the Supabase Auth invite link.\n2. Collect pilot feedback on time saved and UI usability.", 
         "1. Deploy frontend to Vercel and backend to Render/Koyeb.\n2. Build the multi-tenant Agent Studio & HITL 1-click Approval Queue UI.\n3. Monitor cloud health, latency, and telemetry logs."]
    ]
    format_table(flow_table, [1.5, 2.8, 2.9], flow_headers, flow_data)
    doc.add_paragraph().paragraph_format.space_after = Pt(4)

    # -------------------------------------------------------------
    # SECTION 4
    # -------------------------------------------------------------
    add_header(doc, "4. Granular Technical Blueprints: The 2 Core Themes", level=1)
    
    add_p(doc, 
        "The prototype focuses on high-impact, immediate-gratification features across Productivity and Health:")
    
    add_header(doc, "4.1 Theme 1: Productivity & Efficiency Suite", level=2)
    
    add_bullet(doc, 
        "Connects to user inboxes via secure OAuth2. Autonomously analyzes incoming mail across 4 distinct vectors: "
        "(1) Promotional newsletters (generates automated 1-click unsubscribe links and bulk archive recommendations), "
        "(2) Cold sales pitches (auto-deflected into an 'Agent Cold Filter' folder), "
        "(3) Transactional receipts/bills (extracted and routed to financial graphs), and "
        "(4) High-priority personal/executive emails (generates draft replies in the user's authentic voice staged in the HITL review queue).",
        "Feature 1A: Autonomous Email Clean-Up & Smart Triage")
    
    add_bullet(doc, 
        "An intelligent cloud assistant that integrates with Google Drive, iCloud, or local mobile photo vaults. "
        "Scans for: (1) Duplicate or near-identical burst photos, (2) Giant video files (>500MB) that have not been viewed in 12+ months, "
        "(3) High-volume WhatsApp/Telegram media dumps (stale memes, forwarded clips), and (4) Stale downloads. "
        "The agent presents a visual 'Storage Clean-up Recipe' allowing the user to reclaim 10GB–50GB of cloud/phone storage with 1-click batch approval.",
        "Feature 1B: Mobile Storage Management (iOS & Android Cloud Assistant)")
    
    add_bullet(doc, 
        "Eliminates doomscrolling and newsletter fatigue. Ingests user RSS feeds, Substack newsletters, bookmarked Twitter/X threads, "
        "and LinkedIn notifications. The agent runs a semantic filtering pipeline (powered by Gemini Flash's large context window) "
        "and delivers an executive 3-minute read: 'What matters today in your industry, what key people said, and action items for your network.'",
        "Feature 1C: Social Media & Communication Stream Digest")

    add_header(doc, "4.2 Theme 2: Health & Fitness Digital Twin", level=2)
    
    add_bullet(doc, 
        "Creates a sovereign personal health ledger in Supabase. Ingests sleep architecture (deep, REM, light), resting heart rate (RHR), "
        "Heart Rate Variability (HRV), daily steps, and workout strain logs. Tracks longitudinal baselines rather than just daily snapshots.",
        "Feature 2A: Biometric Telemetry & Daily Health Score")
    
    add_bullet(doc, 
        "Connects physiological recovery directly to the user's digital calendar. On days following depressed HRV or poor sleep (<80% recovery score), "
        "the Health Twin automatically suggests: (1) Inserting a 45-minute afternoon cognitive focus buffer, "
        "(2) Rescheduling non-urgent evening social commitments or shifting strenuous HIIT workouts to low-impact zone-2 recovery walks, "
        "and (3) Warning against late caffeine intake.",
        "Feature 2B: Circadian-Aware Calendar & Routine Adaptor")
    
    add_bullet(doc, 
        "Proactively recommends optimal hydration milestones, personalized stretching/mobility breaks based on seated desk hours, "
        "and nutritional timing aligned with upcoming workout demands.",
        "Feature 2C: Personalized Longevity & Bio-Routine Coach")

    # -------------------------------------------------------------
    # SECTION 5
    # -------------------------------------------------------------
    add_header(doc, "5. User Interface (Web & Mobile PWA) & Agent Studio Design", level=1)
    
    add_p(doc, 
        "The user experience is designed as an ultra-responsive Next.js 15 Progressive Web App (PWA) with full mobile device support:")
    
    add_bullet(doc, "Single-screen morning status showing: (a) Daily Health Recovery Score, (b) Email Clean-up Savings (e.g. '18 emails triaged, 3 drafts waiting'), (c) Storage bloat detected (e.g. '4.2 GB reclaimable'), and (d) 3-minute executive social digest.", "1. The Digital Twin Command Center")
    add_bullet(doc, "An interactive visual interface where users can create new specialized agents (e.g. 'Nutrition Agent', 'Twitter Trend Scout', 'Investor Email Guard') by selecting goals, custom persona rules, and execution frequency.", "2. Custom Agent & Scenario Studio")
    add_bullet(doc, "Safety-first control plane. The user sees cards for every high-stakes action proposed by the twin (e.g., 'Delete 14 duplicate photos?', 'Send drafted reply to Sarah?', 'Reschedule 5:00 PM call?'). 1-click 'Approve', 'Edit', or 'Reject'.", "3. Human-in-the-Loop (HITL) Action Queue")

    # -------------------------------------------------------------
    # SECTION 6
    # -------------------------------------------------------------
    add_header(doc, "6. Immediate Next Steps & Kickoff Checklist", level=1)
    
    add_callout(
        doc,
        "KICKOFF CHECKLIST (READY FOR REVIEW)",
        "Step 1: You review this document and confirm the 2 themes.\n"
        "Step 2: You create the 5 free accounts (GitHub, Supabase, Groq, Google AI Studio, Vercel).\n"
        "Step 3: I scaffold the complete repository code, multi-tenant Supabase schema, and agent router.\n"
        "Step 4: We connect your API keys and deploy the live cloud prototype!\n\n"
        "Total estimated setup time to live cloud prototype: Under 7 days.",
        bg_hex="EFF6FF",
        border_color="0284C7"
    )

    doc.save(filename)
    print(f"Cloud Setup & Action Plan Document successfully generated: {filename}")

if __name__ == "__main__":
    build_cloud_setup_docx()

