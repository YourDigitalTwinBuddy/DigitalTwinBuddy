# -*- coding: utf-8 -*-
"""
create_azure_tradeoffs_docx.py
Generates the comprehensive document:
"Karmic AI Platform: Enterprise Azure Architecture, Token Economics & 90-Day Acceleration Blueprint"
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

def build_azure_docx(filename="Karmic_AI_Azure_Enterprise_Architecture_and_Tradeoffs.docx"):
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
    r_sub = p_sub.add_run("Enterprise Azure Cloud Stack, Token Economics, Comparative Trade-Offs & 90-Day Squeezed Project Blueprint\nStrategic Evaluation for Accelerated Commercialization")
    r_sub.font.name = 'Calibri'
    r_sub.font.size = Pt(12)
    r_sub.font.color.rgb = RGBColor(0, 120, 212) # Azure Blue
    
    add_callout(
        doc,
        "EXECUTIVE DECISION MANDATE",
        "This strategic evaluation document benchmarks the commercial, enterprise-grade cloud implementation of the Karmic AI Platform "
        "leveraging Microsoft Azure and frontier GenAI models (Azure OpenAI GPT-4o, GPT-4o-mini, o3-mini) against the 100% Free/Open-Source stack. "
        "It provides granular line-item cost modeling, token economic mechanics, a full architectural trade-off analysis (Pros vs. Cons), "
        "and an aggressive 90-day (12-week) squeezed roadmap to compress time-to-market from 2 years into 3 months.",
        bg_hex="F0F6FF",
        border_color="0078D4"
    )
    
    # -------------------------------------------------------------
    # SECTION 1
    # -------------------------------------------------------------
    add_header(doc, "1. Executive Decision Framework: Speed vs. Sovereignty", level=1)
    
    add_p(doc, 
        "When launching an ambitious Agentic AI Platform like Karmic AI—spanning D2C personal productivity, B2B enterprise SaaS, "
        "and an extensible PaaS ecosystem—the founding leadership faces a foundational architectural crossroads:")
    
    add_bullet(doc, "Maximal privacy, zero vendor lock-in, zero marginal token costs, but requires managing GPU drivers, model quantization, database clustering, and self-hosted high-availability infrastructure. Time-to-market is traditionally slower due to heavy systems engineering.", "Path A: The Free & Open-Source Sovereign Stack (Ollama + PostgreSQL pgvector + Local RAG)")
    add_bullet(doc, "Immediate access to frontier intelligence (GPT-4o, o3-mini, Claude 3.5 Sonnet), enterprise SLA guarantees, turnkey hybrid search, native SOC2/HIPAA compliance, and pre-built scalable infrastructure. Time-to-market is compressed by 75%, but incurs per-token API billing and managed cloud service costs.", "Path B: The Enterprise Azure & Frontier GenAI Stack (Azure OpenAI + Azure AI Search + Cosmos DB)")
    add_bullet(doc, "Launch rapidly on Azure's managed GenAI services to achieve product-market fit and onboard 10 to 1,000 users in 90 days. Then selectively migrate high-frequency, cost-sensitive workloads (such as triage and embedding generation) to localized edge SLMs as scale dictates.", "The Recommended Strategic Vector: The 'Fast-Start Azure -> Hybrid Edge' Paradigm")

    # -------------------------------------------------------------
    # SECTION 2
    # -------------------------------------------------------------
    add_header(doc, "2. Enterprise Azure & Frontier GenAI Architecture", level=1)
    
    add_p(doc, 
        "The Azure enterprise architecture replaces self-hosted primitives with battle-tested, managed cloud components designed for 99.99% availability, "
        "enterprise multi-tenancy, and compliance:")
    
    az_table = doc.add_table(rows=10, cols=4)
    az_headers = ["Platform Subsystem", "Azure Enterprise Component", "Primary Capability", "Monthly Cost Profile"]
    az_data = [
        ["Cognitive Model Routing", "Azure OpenAI Service (GPT-4o & GPT-4o-mini)", "Frontier reasoning, persona drafting, and sub-second intent classification. 99.9% uptime SLA.", "Pay-per-token consumption (Input: $0.15-$2.50/M; Output: $0.60-$10.00/M)"],
        ["Advanced Hybrid RAG", "Azure AI Search (Semantic Ranker + Vector)", "Integrated vector indexing, BM25 full-text, and Microsoft Bing semantic cross-encoder reranking.", "Basic Tier (~$75/mo) to Standard S1 (~$250/mo)"],
        ["Knowledge Graph & Memory", "Azure Database for PostgreSQL Flexible Server", "Fully managed PostgreSQL 16 with pgvector extension and automated daily geo-redundant backups.", "Standard_B2s (2 vCPU, 4GB RAM) ~$65/mo to D4s_v5 (~$280/mo)"],
        ["App & Multi-Agent Backend", "Azure Container Apps (ACA)", "Serverless container execution running LangGraph/FastAPI. Scales to zero when idle; auto-scales under load.", "Consumption tier: ~$35 - $120/mo based on vCPU-seconds"],
        ["Cache & Ephemeral Bus", "Azure Cache for Redis", "In-memory cache for session states, token rate-limiting, and WebSocket connection persistence.", "Basic C0/C1 tier (~$16 - $55/mo)"],
        ["Frontend UI Hosting", "Azure Static Web Apps (Next.js)", "Global edge CDN hosting for the Next.js 15 dashboard, custom domains, and SSL certificates.", "Free tier for pilot; Standard tier ~$9/mo at launch"],
        ["Identity & B2B Auth", "Microsoft Entra ID (Azure AD) + External ID", "Enterprise Single Sign-On (SSO), SAML/OIDC, Multi-Factor Authentication, and B2B user directory.", "Free tier up to 50k MAU; P1 ~$6/user/mo for enterprise features"],
        ["Security & Secrets", "Azure Key Vault", "FIPS 140-2 validated cryptographic vault storing third-party OAuth tokens, client secrets, and master keys.", "~$0.03 per 10,000 operations (~$5/mo)"],
        ["API Gateway & PaaS Hub", "Azure API Management (APIM)", "Exposes developer APIs for B2B PaaS, handles developer API keys, throttling, and usage metering.", "Consumption tier (~$3.50 per million calls) to Developer tier (~$50/mo)"]
    ]
    format_table(az_table, [1.4, 1.8, 2.3, 1.5], az_headers, az_data)
    doc.add_paragraph().paragraph_format.space_after = Pt(4)

    # -------------------------------------------------------------
    # SECTION 3
    # -------------------------------------------------------------
    add_header(doc, "3. Comprehensive Comparative Trade-Off Analysis", level=1)
    
    add_p(doc, 
        "A rigorous side-by-side evaluation across key operational, financial, and strategic vectors:")
    
    trade_table = doc.add_table(rows=8, cols=3)
    trade_headers = ["Evaluation Dimension", "Free / Open-Source Stack (Ollama + Self-Hosted)", "Azure Enterprise & Frontier GenAI Stack"]
    trade_data = [
        ["Time-to-Market (TTM)", 
         "Slow (6 - 12 Months): Requires building custom infrastructure, managing GPU drivers, fine-tuning quantized models, writing custom rerankers, and handling manual failovers.",
         "Ultra-Fast (4 - 8 Weeks): Pre-built turnkey APIs for LLMs, vector search, auth, and containers. Prototype can be in users' hands in under 30 days."],
         
        ["Initial Capital Outlay (CapEx)", 
         "Very Low ($0 - $3,500): Runs on existing developer machines or a single dedicated workstation/mini-server. Zero subscription fees.",
         "Zero CapEx, Pure OpEx: Zero hardware purchase; pay purely for consumed resources on Azure."],
         
        ["Ongoing Operating Expense (OpEx)", 
         "Fixed & Frugal: Hardware electricity or fixed VPS/bare-metal server cost (~$150 - $450/month regardless of token count).",
         "Variable & Consumption-Based: Grows with token volume and active users. For small cohorts (<100 users), very cheap ($150-$500/mo); scales predictably with revenue."],
         
        ["Engineering Team Overhead", 
         "High Specialist Requirement: Demands deep MLOps, CUDA, systems programming, and database tuning expertise. Minimum 2-3 dedicated DevOps/ML engineers.",
         "Low Specialist Requirement: Standard full-stack TypeScript/Python developers can integrate managed APIs in days. Focus is 100% on product features."],
         
        ["Data Privacy & Sovereignty", 
         "Absolute Sovereignty: Data never leaves local premises or private servers. Cryptographically zero-leak. Immune to third-party policy changes.",
         "Enterprise Contractual Privacy: Azure OpenAI guarantees customer data is NOT used to train foundation models and is encrypted at rest/transit. Enterprise-compliant."],
         
        ["Model Reasoning & Accuracy", 
         "Good to High: Local Llama 3.3 70B and Qwen 2.5 32B are capable, but may struggle with subtle instruction nuances or complex multi-hop tool routing.",
         "Frontier & Unmatched: Direct access to GPT-4o, o1, and o3-mini provides world-leading reasoning, complex tool synthesis, and superior persona styling."],
         
        ["Enterprise Compliance Readiness", 
         "Manual Audit Nightmare: Achieving SOC2 Type II, ISO 27001, and HIPAA on self-hosted servers requires months of custom security engineering.",
         "Turnkey Compliance: Azure comes out-of-the-box with SOC2 Type II, HIPAA, ISO 27001, FedRAMP, and GDPR compliance certifications."]
    ]
    format_table(trade_table, [1.5, 2.7, 2.8], trade_headers, trade_data)
    doc.add_paragraph().paragraph_format.space_after = Pt(4)

    add_header(doc, "3.1 Pros & Cons Summary Matrix", level=2)
    
    add_callout(
        doc,
        "FREE & OPEN-SOURCE STACK (SELF-HOSTED)",
        "PROS:\n"
        "• $0 License/API cost: Unlimited token generation without metered billing anxiety.\n"
        "• Complete data sovereignty: Ideal for ultra-paranoid executives, defense, or highly sensitive privacy niches.\n"
        "• Zero vendor lock-in: Code runs anywhere (Apple Silicon, NVIDIA RTX, Linux, local on-prem).\n\n"
        "CONS:\n"
        "• High operational friction: Managing CUDA drivers, quantized context limits, VRAM bottlenecks, and model crashes.\n"
        "• Hardware limits: Running a 70B model requires at least 48GB VRAM (2x RTX 3090/4090 or Mac Studio M2/M3).\n"
        "• Slower development velocity: Engineering hours spent maintaining infrastructure instead of building user features.",
        bg_hex="F8FAFC",
        border_color="64748B"
    )
    
    add_callout(
        doc,
        "AZURE ENTERPRISE CLOUD STACK (MANAGED)",
        "PROS:\n"
        "• Unprecedented development speed: Turnkey APIs enable shipping a production MVP in 4 to 6 weeks.\n"
        "• Best-in-class frontier intelligence: GPT-4o and o3-mini handle complex multi-step agent reasoning effortlessly.\n"
        "• Enterprise B2B readiness: Single Sign-On (Entra ID), SOC2 compliance, and 99.9% SLAs unblock enterprise sales immediately.\n"
        "• Elastic scalability: Handles 1 user or 100,000 users without refactoring infrastructure.\n\n"
        "CONS:\n"
        "• Variable per-token costs: Poorly optimized agent loops can drive unexpected token expenses.\n"
        "• Vendor dependency: Tied to Microsoft Azure ecosystem and OpenAI model lifecycle deprecations.\n"
        "• Perceived privacy barrier: Certain privacy-sensitive users require local-first proof.",
        bg_hex="F0FDF4",
        border_color="16A34A"
    )

    # -------------------------------------------------------------
    # SECTION 4
    # -------------------------------------------------------------
    add_header(doc, "4. Deep-Dive Token Economics & Financial Modeling", level=1)
    
    add_p(doc, 
        "To make an informed commercial decision, we must demystify how tokens are consumed in an agentic platform and quantify "
        "the exact cost per user per month. Agentic workflows consume substantially more tokens than simple chatbots because agents "
        "continually evaluate context, call tools, reflect on results, and maintain persistent memory.")

    add_header(doc, "4.1 Frontier Model Pricing Benchmarks (Current Enterprise Rates)", level=2)
    tok_table = doc.add_table(rows=6, cols=5)
    tok_headers = ["Model Name", "Input Cost / 1M Tokens", "Cached Input / 1M Tokens", "Output Cost / 1M Tokens", "Primary Role in Karmic AI"]
    tok_data = [
        ["Azure OpenAI GPT-4o-mini", "$0.15", "$0.075", "$0.60", "High-frequency triage, intent classification, entity extraction, email routing (80% of calls)."],
        ["Azure OpenAI GPT-4o", "$2.50", "$1.25", "$10.00", "Complex persona drafting, strategic calendar negotiation, task decomposition, agent reflection."],
        ["Azure OpenAI o3-mini / o1-mini", "$1.10", "$0.55", "$4.40", "Deep research, complex schedule constraint solving, multi-agent conflict resolution."],
        ["Anthropic Claude 3.5 Sonnet", "$3.00", "$0.30", "$15.00", "Alternative frontier benchmark: elite nuanced persona emulation and coding."],
        ["Self-Hosted Llama 3.3 70B", "$0.00", "$0.00", "$0.00", "Zero token billing; cost amortized into fixed GPU server hardware or rental."]
    ]
    format_table(tok_table, [1.6, 1.3, 1.3, 1.3, 1.7], tok_headers, tok_data)
    doc.add_paragraph().paragraph_format.space_after = Pt(4)

    add_header(doc, "4.2 Granular User Workload Token Profile (Daily Active Knowledge Worker)", level=2)
    add_p(doc, 
        "The following table details the empirical daily token budget for an active Karmic AI user across standard productivity features:")
    
    work_table = doc.add_table(rows=7, cols=5)
    work_headers = ["Workflow Feature", "Daily Frequency", "Avg Input Tokens / Call", "Avg Output Tokens / Call", "Total Daily Tokens"]
    work_data = [
        ["Morning Context Briefing", "1 / day", "15,000 (emails + calendar)", "1,500 (structured summary)", "16,500"],
        ["Email Inbound Triage & Filter", "30 emails / day", "1,500 / email (45,000)", "100 / email (3,000)", "48,000"],
        ["Persona-Drafted Email Replies", "8 drafts / day", "3,500 (thread + tone graph)", "500 / draft (4,000)", "32,000"],
        ["Autonomous Calendar Coordination", "4 requests / day", "3,000 (slots + rules)", "400 / slot (1,600)", "13,600"],
        ["Private Document Graph RAG Search", "5 queries / day", "4,000 (chunks + entities)", "600 / answer (3,000)", "23,000"],
        ["Nightly Reflective Sleep Consolidation", "1 / night", "18,000 (day's interactions)", "1,200 (graph updates)", "19,200"]
    ]
    format_table(work_table, [1.8, 1.1, 1.6, 1.4, 1.1], work_headers, work_data)
    doc.add_paragraph().paragraph_format.space_after = Pt(4)

    add_p(doc, "Aggregate Daily Token Consumption per Active User:", bold=True)
    add_bullet(doc, "~135,000 input tokens per user per day (~4,050,000 input tokens / month).", "Total Input Volume")
    add_bullet(doc, "~14,000 output tokens per user per day (~420,000 output tokens / month).", "Total Output Volume")
    add_bullet(doc, "Because system prompts, user persona rules, and calendar guidelines remain static across calls, Azure OpenAI Prompt Caching cuts input token billing by ~50% on repeated calls.", "Prompt Caching Optimization")

    add_header(doc, "4.3 Monthly AI Inference Cost per User: Three Routing Strategies", level=2)
    
    add_p(doc, 
        "The actual cost per user depends dramatically on the model routing architecture:")
    
    cost_strat_table = doc.add_table(rows=4, cols=4)
    cost_strat_headers = ["Routing Strategy", "Model Allocation", "Net Monthly AI Cost / User", "Viability & Margin on $39/mo Pro Tier"]
    cost_strat_data = [
        ["Naive Single-Model: Pure GPT-4o", 
         "100% of all calls sent to GPT-4o", 
         "~$8.50 - $11.20 / user / month", 
         "Viable (71% Gross Margin). Unnecessarily expensive for simple email classification."],
         
        ["Smart Tiered Routing (Recommended)", 
         "80% handled by GPT-4o-mini (triage, extraction, scheduling)\n20% handled by GPT-4o (persona drafting, reflection)", 
         "~$1.15 - $1.85 / user / month", 
         "Outstanding (95% Gross Margin). Sub-second speed on 80% of tasks, frontier brilliance on high-stakes outputs."],
         
        ["Pure GPT-4o-mini Utility", 
         "100% of calls sent to GPT-4o-mini", 
         "~$0.45 - $0.65 / user / month", 
         "Ultra-low cost (98% Gross Margin). Acceptable for triage, but persona emulation lacks nuanced human warmth."]
    ]
    format_table(cost_strat_table, [1.8, 2.0, 1.6, 1.8], cost_strat_headers, cost_strat_data)
    doc.add_paragraph().paragraph_format.space_after = Pt(4)

    add_callout(
        doc,
        "THE FINANCIAL TAKEAWAY ON TOKEN ECONOMICS",
        "At ~$1.50 per user per month in variable AI inference costs using Smart Tiered Routing, a D2C customer paying $29 to $49/month "
        "yields a staggering 94% to 96% software gross margin! Even in a heavy-usage corporate environment ($60/user/month), "
        "inference costs are virtually negligible relative to the enormous time liberated ($500+ value of executive hours returned). "
        "Fears of 'ruinous token bills' are unfounded when an intelligent multi-agent router is properly implemented.",
        bg_hex="F0FDF4",
        border_color="16A34A"
    )

    # -------------------------------------------------------------
    # SECTION 5
    # -------------------------------------------------------------
    add_header(doc, "5. Total Cost of Ownership (TCO) & Azure Monthly Bill Projections", level=1)
    
    add_p(doc, 
        "Below is the complete projected monthly infrastructure and API bill across three growth cohorts: "
        "Pilot Phase (10 users), Launch Phase (1,000 users), and Growth Phase (10,000 users):")
    
    tco_table = doc.add_table(rows=10, cols=4)
    tco_headers = ["Azure Service Component", "Pilot Cohort (10 Users)", "Launch Cohort (1,000 Users)", "Scale Cohort (10,000 Users)"]
    tco_data = [
        ["Azure OpenAI Model Inference (Tiered)", "$18 / month", "$1,450 / month", "$13,800 / month"],
        ["Azure AI Search (Hybrid + Semantic)", "$75 / month (Basic)", "$250 / month (Standard S1)", "$980 / month (Standard S2/S3)"],
        ["Azure Database for PostgreSQL (Flexible)", "$65 / month (Burstable B2s)", "$175 / month (General Purpose D2s)", "$580 / month (D8s High-Avail)"],
        ["Azure Container Apps (Serverless Backend)", "$30 / month", "$180 / month", "$950 / month"],
        ["Azure Cache for Redis", "$16 / month (Basic C0)", "$55 / month (Standard C1)", "$220 / month (Premium P1)"],
        ["Azure Blob Storage & Backup", "$5 / month", "$25 / month", "$180 / month"],
        ["Azure Static Web Apps (Next.js)", "$0 (Free tier)", "$9 / month (Standard)", "$9 / month (Standard)"],
        ["Azure Key Vault, DNS & Bandwidth", "$5 / month", "$30 / month", "$160 / month"],
        ["TOTAL ESTIMATED MONTHLY BILL", "$214 / month", "$2,174 / month", "$16,879 / month"]
    ]
    format_table(tco_table, [2.3, 1.5, 1.7, 1.7], tco_headers, tco_data)
    doc.add_paragraph().paragraph_format.space_after = Pt(4)

    add_p(doc, "Unit Economic Health & Breakeven Analysis:", bold=True)
    add_bullet(doc, "Total Monthly Azure Spend = $214. Cost per user = $21.40/month. Completely affordable for rapid R&D without purchasing high-end workstation hardware.", "Pilot Phase (10 Users)")
    add_bullet(doc, "Total Monthly Azure Spend = $2,174. Monthly SaaS Revenue (1,000 users @ $39/mo avg) = $39,000. Infrastructure Cost as % of Revenue = 5.5%! (94.5% Gross Margin).", "Launch Phase (1,000 Users)")
    add_bullet(doc, "Total Monthly Azure Spend = $16,879. Monthly SaaS Revenue (10,000 users @ $39/mo avg) = $390,000. Infrastructure Cost as % of Revenue = 4.3%! (95.7% Gross Margin).", "Scale Phase (10,000 Users)")

    # -------------------------------------------------------------
    # SECTION 6
    # -------------------------------------------------------------
    add_header(doc, "6. Squeezing the Roadmap: From 2 Years to 90 Days (12 Weeks)", level=1)
    
    add_p(doc, 
        "Why did early AI projects take 18 to 24 months, and how can Karmic AI ship a fully functional, revenue-generating commercial platform in just 90 days? "
        "The shift is driven by three modern architectural tailwinds:")
    
    add_bullet(doc, "Instead of provisioning physical servers, configuring Kubernetes clusters from scratch, and writing CUDA kernels, Azure Container Apps and Azure AI Search deploy in minutes via Bicep/Terraform scripts.", "1. Serverless Managed Cloud Primitives")
    add_bullet(doc, "The Model Context Protocol (MCP) and modern agent state graph frameworks (LangGraph / Semantic Kernel) provide pre-built abstractions for tool calling, memory checkpoints, and supervisor routing. Developers write business logic, not plumbing.", "2. Standardized Agent Frameworks")
    add_bullet(doc, "Turnkey vector search, hybrid lexical matching, and Bing-grade semantic rerankers exist out-of-the-box in Azure AI Search. What previously took a dedicated search engineering team 6 months now requires a single API configuration.", "3. Turnkey Hybrid Search & Embeddings")

    add_header(doc, "6.1 The 12-Week (90-Day) Accelerated Master Project Plan", level=2)
    
    plan_table = doc.add_table(rows=13, cols=3)
    plan_headers = ["Sprint Week", "Target Focus & Engineering Deliverables", "Validation Milestone & Exit Gate"]
    plan_data = [
        ["Month 1: Weeks 1 - 2", 
         "• Azure Infrastructure Scaffolding: Provision Azure OpenAI, Azure AI Search, PostgreSQL with pgvector, and Azure Container Apps.\n• Tool Integration: Build MCP Mail (OAuth2) and MCP Google Calendar connectors.\n• Base LangGraph Architecture: Supervisor Agent + Triage Agent.", 
         "Working CLI & API agent able to summarize unread emails and inspect calendar schedules."],
         
        ["Month 1: Weeks 3 - 4", 
         "• Hybrid Graph RAG in Azure AI Search: Ingest personal documents, emails, and notes with semantic reranking.\n• Persona Emulation Engine: Implement tone extraction and few-shot prompt templates.\n• Next.js Webview & Desktop Tray Scaffolding.", 
         "MILESTONE 1 (Day 30): 10 Internal / Founder Pilot Users onboarded. Daily automated 7:00 AM briefing active."],
         
        ["Month 2: Weeks 5 - 6", 
         "• Human-in-the-Loop Review Dashboard: Interactive Next.js UI showing proposed email drafts and calendar slots.\n• Real-Time Token Streaming: FastAPI WebSockets streaming agent reasoning steps to the UI.\n• Task Decomposition Engine: Breaking natural language projects into actionable sub-tasks.", 
         "Pilot users actively approving drafted emails with 1 click; 2.5+ hours/day saved empirically."],
         
        ["Month 2: Weeks 7 - 8", 
         "• Health & Vitality Module (Preview): Ingestion of Apple Health / Oura sleep and HRV data via webhook.\n• Circadian Scheduling Logic: Auto-adjusting calendar buffers based on sleep recovery scores.\n• Multi-Tenant B2B Database Isolation & Microsoft Entra ID SSO integration.", 
         "MILESTONE 2 (Day 60): Pilot expanded to 50 active users (D2C beta + 2 corporate pilot teams). NPS > 65."],
         
        ["Month 3: Weeks 9 - 10", 
         "• Stripe Billing & Subscription Tiering: Automated self-serve checkout for $29/mo Pro and $99/mo Executive tiers.\n• Azure API Management (APIM): Exposing secure B2B developer endpoints for custom MCP skill registration.\n• Security Hardening: Penetration testing, automated audit logging, and SOC2 readiness scan.", 
         "Production payment infrastructure live; self-serve customer onboarding functional."],
         
        ["Month 3: Weeks 11 - 12", 
         "• Domestic IoT / Matter Prototype: Integration with Home Assistant / Matter bridge for scheduled office prep.\n• Commercial Public Beta Launch: Product Hunt launch, targeted founder outreach, executive referral campaign.\n• Production Operations Dashboard: Azure Application Insights monitoring latency, token burn, and errors.", 
         "MILESTONE 3 (Day 90): Commercial Launch! 250+ paying subscribers, $10K+ MRR, sub-second triage latency."]
    ]
    format_table(plan_table, [1.5, 3.5, 2.2], plan_headers, plan_data)
    doc.add_paragraph().paragraph_format.space_after = Pt(4)

    # -------------------------------------------------------------
    # SECTION 7
    # -------------------------------------------------------------
    add_header(doc, "7. Team Upskilling & Adoption Strategy", level=1)
    
    add_p(doc, 
        "To ensure the development team executes with maximum velocity while learning best practices on the journey, "
        "the following learning curriculum is established:")
    add_bullet(doc, "Mastering the official open-source specification. Separating tool servers (mail, files, shell) from reasoning brains makes the codebase 100% portable between Azure OpenAI and local Ollama.", "Core Skill 1: Model Context Protocol (MCP) Mastery")
    add_bullet(doc, "Understanding stateful agent graphs, checkpointing, interrupt handling (human approval gates), and multi-agent supervisor hierarchies using Python LangGraph or Microsoft Semantic Kernel.", "Core Skill 2: LangGraph & Deterministic Agent Workflows")
    add_bullet(doc, "Learning how to leverage Azure OpenAI's automatic prompt caching (matching identical prefixes in system instructions and history) to eliminate 50% of input token billing.", "Core Skill 3: Token Optimization & Prompt Caching")
    add_bullet(doc, "Configuring vector fields, BM25 text analyzers, and Bing Semantic Rankers in Azure AI Search to achieve state-of-the-art context retrieval without managing raw vector indexes.", "Core Skill 4: Hybrid RAG & Semantic Reranking in Azure")

    # -------------------------------------------------------------
    # SECTION 8
    # -------------------------------------------------------------
    add_header(doc, "8. Final Strategic Recommendation & Decision Matrix", level=1)
    
    add_callout(
        doc,
        "THE SYNTHESIZED EXECUTIVE RECOMMENDATION",
        "1. DO NOT spend 6-9 months wrestling with local CUDA drivers, hardware purchases, and quantization bugs before proving user demand.\n"
        "2. ADOPT the Enterprise Azure Stack for the 90-Day Launch Sprint: Leverage Azure OpenAI (GPT-4o + 4o-mini), Azure AI Search, and Container Apps to ship the commercial MVP in 12 weeks for under $250/month in pilot infrastructure.\n"
        "3. MAINTAIN MCP & LANGGRAPH STANDARDIZATION: Because the agent logic is written using open standards (MCP and LangGraph), every single tool, prompt, and memory schema can be seamlessly swapped to local Ollama/Llama 3.3 in the future without rewriting core application code!\n"
        "4. INTRODUCE THE HYBRID EDGE AT SCALE: Once paying customer volume reaches 1,000+ users, package the local SLM edge client for privacy-purist users while keeping Azure as the heavy cloud reasoning engine.",
        bg_hex="EFF6FF",
        border_color="0078D4"
    )

    doc.save(filename)
    print(f"Azure Architecture & Trade-Off Document successfully generated: {filename}")

if __name__ == "__main__":
    build_azure_docx()

