# -*- coding: utf-8 -*-
"""
create_master_docx.py
Generates the comprehensive Karmic AI Platform Master Architecture Document (.docx)
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

def build_docx(filename="Karmic_AI_Platform_Master_Architecture_Document.docx"):
    doc = docx.Document()
    
    # Page setup - Margins 0.8 inch
    sections = doc.sections
    for section in sections:
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
    r_sub = p_sub.add_run("Sovereign Personal Digital Twin & Autonomous Agentic OS\nComprehensive System Design, Architecture, 100% Free Open-Source Implementation Stack & Business Model Blueprint")
    r_sub.font.name = 'Calibri'
    r_sub.font.size = Pt(12)
    r_sub.font.color.rgb = RGBColor(37, 99, 235) # Blue 600
    
    add_callout(
        doc,
        "EXECUTIVE BRIEFING & STRATEGIC CONTEXT",
        "This document establishes the end-to-end technical architecture, multi-agent engineering patterns, "
        "hybrid Graph RAG framework, zero-cost open-source technology stack, and 9-box business model for the Karmic AI Platform. "
        "Engineered to launch initially as a focused 'Productivity & Efficiency' Agentic Digital Twin for a 5-10 user pilot, "
        "the platform is architected from Day 1 to scale into a multi-tenant D2C personal operating system and a B2B SaaS/PaaS enterprise agent platform, "
        "ultimately bridging digital cognitive agency with embodied physical domestic automation.",
        bg_hex="EFF6FF",
        border_color="2563EB"
    )
    
    # -------------------------------------------------------------
    # SECTION 1
    # -------------------------------------------------------------
    add_header(doc, "1. Executive Summary, Product Vision & Strategic Paradigm", level=1)
    
    add_p(doc, 
        "Modern human productivity is crippled by an artificial barrier between cognitive intent and physical/digital execution. "
        "Despite exponential breakthroughs in generative artificial intelligence, knowledge workers and everyday consumers remain "
        "friction-laden manual dispatchers—spending between 40% and 60% of their daily working hours triaging communications, "
        "reconciling conflicting calendars, summarizing scattered documents, and executing repetitive administrative churn.")
    
    add_p(doc,
        "Karmic AI Platform introduces a unified sovereign architecture engineered to bridge Cognitive Agency, Autonomous Digital Execution, "
        "and Physical World Automation. Operating at the convergence of Direct-to-Consumer (D2C) personal intelligence and Enterprise B2B SaaS/PaaS, "
        "Karmic AI serves as a permanent, context-aware extension of the user: a Sovereign Personal Digital Twin.")
    
    add_bullet(doc, "Acts as an authenticated proxy capable of synthesizing multi-channel communications, managing diary appointments, and executing routine digital handshakes in the user's authentic tone and style.", "Autonomous Sovereign Persona Representation")
    add_bullet(doc, "A multi-tier memory fabric integrating dense vector embeddings, lexical BM25 search, and structural knowledge graphs that dynamically captures user preferences, social ties, habits, and operating heuristics.", "Persistent Epistemic Graph RAG Fabric")
    add_bullet(doc, "Autonomous agentic swarms governed by deterministic state machines (LangGraph) and the open Model Context Protocol (MCP) to safely execute complex multi-step workflows across external services.", "Sandboxed Agentic Tool Execution")
    add_bullet(doc, "A strict edge-native and private-vault posture ensuring that deep personal identity telemetry, credentials, and memory graphs remain cryptographically owned and controlled by the individual.", "Zero-Leak Privacy Architecture")
    add_bullet(doc, "Translating cognitive routines and schedule awareness into spatial home automation via Matter/Thread protocols and ROS2 robotics middleware.", "Embodied Physical Horizon")

    # -------------------------------------------------------------
    # SECTION 2
    # -------------------------------------------------------------
    add_header(doc, "2. Value Proposition & Strategic Differentiators", level=1)
    
    add_p(doc, 
        "Karmic AI addresses distinct value propositions across D2C personal users, B2B enterprise knowledge workers, and PaaS ecosystem developers:")
    
    add_header(doc, "2.1 D2C Value Proposition: Personal Time Liberation & Cognitive Sovereignty", level=2)
    add_bullet(doc, "Returns 3 to 4 hours of digital administrative churn and 1 to 2 hours of home logistics coordination every day.", "4 to 6 Productive Hours Returned Daily")
    add_bullet(doc, "Eliminates the mental overhead of inbox zero, calendar ping-pong, follow-up tracking, and subscription auditing.", "Zero Cognitive Churn")
    add_bullet(doc, "Unlike commercial cloud LLMs that monetize user interactions or share data across multi-tenant prompts, Karmic AI executes on local/private infrastructure with zero data leakage.", "Complete Cryptographic Sovereignty")
    add_bullet(doc, "The twin continuously evolves with the user, learning subtle preferences, communication nuances, and ethical boundaries through reflective consolidation.", "Long-Horizon Adaptive Memory")
    
    add_header(doc, "2.2 B2B SaaS Value Proposition: Enterprise Workforce Augmentation", level=2)
    add_bullet(doc, "Equips every knowledge worker, manager, and executive with a dedicated agentic Chief of Staff, multiplying high-leverage strategic output by 3x-5x.", "Executive & Knowledge Worker Productivity Multiplier")
    add_bullet(doc, "Agents autonomously synthesize action items, prepare cross-functional project updates, and ensure alignment across Slack, Jira, GitHub, and email.", "Cross-Silo Context Synthesis")
    add_bullet(doc, "Eliminates scheduling friction for multi-stakeholder external and internal meetings through autonomous agent-to-agent negotiation protocols.", "Automated Meeting & Calendar Orchestration")
    
    add_header(doc, "2.3 B2B PaaS Value Proposition: Extensible Agentic Infrastructure", level=2)
    add_bullet(doc, "Enterprises and independent developers can build, test, and deploy specialized agent skills using standard Model Context Protocol (MCP) servers.", "Extensible Developer SDK & MCP Skill Registry")
    add_bullet(doc, "Deployable completely on-premises or within enterprise virtual private clouds (VPC) using 100% open-source local LLMs and vector/graph databases.", "Private Sovereign Deployment")
    add_bullet(doc, "Exposes unified APIs for multi-agent state management, persistent memory recall, and deterministic verification gates.", "Agentic Infrastructure as a Service")

    # Value Proposition Comparison Table
    add_p(doc, "Strategic Differentiation Matrix vs. Existing Market Paradigms:", bold=True)
    val_table = doc.add_table(rows=5, cols=4)
    val_headers = ["Strategic Dimension", "Traditional LLMs (ChatGPT/Claude)", "Point Productivity Tools (Motion/Superhuman)", "Karmic AI Platform"]
    val_data = [
        ["Agency & Execution", "Reactive prompt-response; cannot take persistent autonomous action.", "Narrow heuristic automation; hardcoded rules without semantic reasoning.", "Proactive multi-agent autonomous execution via MCP tools and stateful graphs."],
        ["Memory & Context", "Ephemeral context window; resets every conversation.", "Fragmented app-specific databases; no cross-domain user understanding.", "Persistent Graph RAG + Episodic Vector Fabric reflecting lifetime user habits."],
        ["Privacy & Sovereignty", "Centralized cloud; customer data used for fine-tuning or retained in telemetry.", "SaaS multi-tenant databases prone to vendor lock-in.", "100% sovereign, local-first / private-cloud deployment; zero data leakage."],
        ["Physical-Digital Bridge", "Zero somatic awareness or physical hardware connection.", "Completely confined to cyberspace screens and calendars.", "Unified bridge from digital routines to Matter/Thread IoT and ROS2 robotics."]
    ]
    format_table(val_table, [1.5, 1.7, 1.8, 1.8], val_headers, val_data)
    doc.add_paragraph().paragraph_format.space_after = Pt(4)

    # -------------------------------------------------------------
    # SECTION 3
    # -------------------------------------------------------------
    add_header(doc, "3. The 9-Box Business Model Canvas", level=1)
    
    add_p(doc, 
        "The Karmic AI business model is structured across the standard 9-box framework, harmonizing immediate D2C user acquisition with scalable B2B SaaS and PaaS monetization:")
    
    bm_table = doc.add_table(rows=10, cols=3)
    bm_headers = ["Canvas Dimension", "Strategic Implementation", "Key Metrics & Milestones"]
    bm_data = [
        ["1. Customer Segments", 
         "D2C: C-suite executives, founders, high-earning remote professionals (HENRYs), solopreneurs, creators.\nB2B: High-growth tech companies, professional service firms (consulting, legal, finance), distributed enterprise teams.\nPaaS: AI software engineers, enterprise workflow developers, robotics integrators.",
         "D2C TAM: $50B+ (120M global knowledge workers).\nB2B TAM: $40B+ enterprise productivity & agent software."],
        
        ["2. Value Propositions", 
         "• Sovereign Personal Digital Twin returning 4-6 hours daily.\n• Zero cognitive churn via proactive email, calendar, and task orchestration.\n• Zero-leak privacy through local-first and self-hosted open-source architecture.\n• Enterprise agent swarms multiplying team velocity without linear headcount growth.",
         "• NPS > 65.\n• Daily active user engagement > 4.5 sessions/day.\n• > 85% autonomous task completion rate without manual overrides."],
        
        ["3. Channels", 
         "• Product-Led Growth (PLG): Free self-hosted community edition for developers and tech enthusiasts.\n• Direct D2C Digital Marketing: Targeted thought leadership, viral video demos of agentic workflows.\n• B2B2C Corporate Wellness / Productivity Benefits: Sponsored executive twin packages subsidized by employers.\n• MCP Marketplace: Distribution of agent skills via the open MCP directory.",
         "• CAC < $45 for D2C Pro.\n• B2B Sales cycle < 30 days via self-serve pilot-to-enterprise upgrades.\n• Organic developer referral rate > 35%."],
         
        ["4. Customer Relationships", 
         "• High-Intimacy Autonomous Partnership: The twin becomes an indispensable life partner that knows user preferences intimately.\n• High Retention Moat: Contextual memory graphs accumulate compounding value over time; switching costs are prohibitive.\n• Enterprise White-Glove Support: Dedicated deployment engineers for self-hosted enterprise clusters.",
         "• Gross Revenue Retention (GRR) > 92%.\n• Net Revenue Retention (NRR) > 130% on B2B.\n• Annualized churn < 5% on annual Pro tiers."],
         
        ["5. Revenue Streams", 
         "• D2C Freemium: Free local self-hosted version for 1 user.\n• D2C Pro SaaS: $29 - $49 / month (managed cloud sync, high-capacity reasoning, advanced MCP integrations).\n• D2C Executive & Family: $99 / month (multi-agent swarms, domestic IoT, shared family graphs).\n• B2B Enterprise SaaS: $35 - $60 / user / month (SOC2, team graphs, admin control plane).\n• PaaS API & Skill Marketplace: Consumption-based API billing + 30% take-rate on certified physical/digital skills.",
         "• Seed target: $1.2M ARR within 12 months.\n• Series A target: $5M+ ARR at 24 months.\n• Blended Gross Margin > 78% (low API costs due to local/open-source inference)."],
         
        ["6. Key Resources", 
         "• Proprietary Epistemic Graph RAG Memory Architecture & Reflection Schemas.\n• Open-source agent orchestration state graphs (LangGraph custom nodes).\n• Fine-tuned specialized Small Language Models (SLMs) for intent classification and tool routing.\n• Robust catalog of certified MCP tool adapters.",
         "• 4 Core patent applications (Epistemic Memory Consolidation, Agent-to-Agent Negotiation, Cognitive-Physical VLA Bridge)."],
         
        ["7. Key Activities", 
         "• Continuous R&D on stateful multi-agent architectures and hybrid local/cloud inference.\n• Core development of the zero-cost open-source stack and Docker deployment scripts.\n• Security hardening of sandboxed execution environments and credential enclaves.\n• Cultivating developer community around the MCP skill ecosystem.",
         "• Bi-weekly release cadence.\n• Zero reported critical security/privacy vulnerabilities."],
         
        ["8. Key Partners", 
         "• Open-source AI ecosystems (Ollama, Hugging Face, vLLM, LangChain/LangGraph).\n• Hardware OEMs: Smart domestic hardware manufacturers (Matter/Thread certified devices), consumer robotics labs.\n• Enterprise software platforms (Google Workspace, Microsoft 365, Notion, Slack, Jira).\n• Academic & research labs in Embodied AI and Graph Neural Networks.",
         "• 3 Confirmed hardware OEM integration pilots in Phase 2.\n• Full compliance with Google and Microsoft API verification standards."],
         
        ["9. Cost Structure", 
         "• Phase 1 Prototype Cost: $0 external API cost (utilizing local open-source models on commodity hardware).\n• Cloud Infrastructure: Dedicated GPU clusters (H100/A100 spot instances via RunPod/Lambda Labs) for hosted users.\n• Engineering Talent: ML systems engineers, full-stack agent developers, robotics middleware specialists.\n• Security Audits & Compliance: SOC2 Type II, HIPAA, and penetration testing.",
         "• Initial prototyping burn: < $5,000 / month.\n• Target unit economics: < $4.20 monthly inference cost per active Pro user against $39/mo subscription (89% contribution margin)."]
    ]
    format_table(bm_table, [1.5, 3.8, 1.5], bm_headers, bm_data)
    doc.add_paragraph().paragraph_format.space_after = Pt(4)

    # -------------------------------------------------------------
    # SECTION 4
    # -------------------------------------------------------------
    add_header(doc, "4. Problem Statements & Granular Feature Use Cases", level=1)
    
    add_p(doc, 
        "Karmic AI solves concrete operational bottlenecks across multiple life domains, beginning with a focused Phase 1 "
        "Productivity & Efficiency suite, followed by planned expansions into Health, Finance, Enterprise B2B, and Physical Robotics.")
    
    add_header(doc, "4.1 Phase 1 Focus: Productivity & Efficiency Agentic Suite (5-10 User Pilot)", level=2)
    add_p(doc, 
        "The initial deployment focuses exclusively on eliminating digital administrative friction for knowledge workers. "
        "The following core features represent the foundation of the 5-10 user prototype:")
    
    add_bullet(doc, "Every morning at 07:00, the twin ingests unread emails, upcoming calendar events, Slack/Discord pings, and task backlogs. It synthesizes a high-context briefing detailing: (a) top 3 critical objectives for the day, (b) calendar conflicts requiring resolution, (c) high-priority sender emails requiring responses, and (d) proactive recommendations for deep-work focus blocks.", "Adaptive Morning Context Briefing")
    add_bullet(doc, "The twin classifies incoming correspondence into urgent, informational, transactional, and spam. For substantive emails, it drafts responses in the exact voice, tone, vocabulary, and sign-off style of the user, referencing prior historical context from the Graph RAG store. The user simply reviews and clicks 'Approve' (or allows autonomous dispatch for trusted senders).", "Autonomous Persona-Emulated Email Triage & Drafting")
    add_bullet(doc, "When meeting invitations or scheduling requests arrive via email or chat, the twin negotiates optimal time slots without human intervention. It checks the user's focus preferences (e.g., 'no morning meetings before 11:00 AM', 'cluster external calls on Tuesday/Thursday'), proposes slots, and confirms invites.", "Proactive Calendar Optimization & Meeting Negotiation")
    add_bullet(doc, "Incoming complex projects (e.g., 'Prepare Q3 Board Deck') are automatically decomposed into structured, sequential action items with estimated time allocations, dependency links, and automated deadline reminders.", "Intelligent Task Decomposition & Follow-Up Tracker")
    add_bullet(doc, "The user can query anything across their lifetime documents, notes, past emails, and project files using natural language. The system retrieves precise factual answers with exact source citations via hybrid Graph RAG, even synthesizing connections across disparate documents.", "Personal Knowledge Base & Semantic Search")
    add_bullet(doc, "Autonomous multi-agent swarms operate under a central Supervisor Agent: a Triage Agent parses inputs, a Calendar Agent manages slots, a Research Agent browses the web or internal docs, and a Tool Execution Agent interacts with third-party APIs via MCP.", "Multi-Agent Orchestration Fabric")

    add_header(doc, "4.2 Phase 2 Extension: Personal Health, Vitality & Longevity Twin", level=2)
    add_p(doc, 
        "Physical vitality directly dictates cognitive performance. Phase 2 extends the digital twin into an autonomous health advocate:")
    add_bullet(doc, "Ingests continuous time-series metrics from wearables (Apple HealthKit, Oura, Whoop, Garmin) including HRV, resting heart rate, sleep stage cycles, and VO2 max.", "Continuous Biomarker Ingestion & Telemetry")
    add_bullet(doc, "The digital twin correlates cognitive workload and calendar density with physiological strain. On days following poor REM/deep sleep or depressed HRV, the twin automatically reschedules non-urgent meetings, inserts focus pauses, and alerts the user.", "Circadian Rhythm & Recovery-Aware Scheduling")
    add_bullet(doc, "Proactively prompts optimal hydration, post-meal mobility walks, and nutritional strategies tailored to planned physical and mental exertion levels.", "Personalized Longevity Protocol Enforcement")
    add_bullet(doc, "Synthesizes annual blood panels, doctor summaries, and medication regimens into a unified personal health knowledge graph, tracking longitudinal biomarkers against optimal longevity ranges.", "Longitudinal Medical History Graph")

    add_header(doc, "4.3 Phase 3 Extension: Financial & Autonomous Consumer Operations", level=2)
    add_bullet(doc, "Scans recurring bank/credit card statements to identify zombie subscriptions, duplicate software tools, and unannounced price hikes, autonomously dispatching cancellation or renegotiation requests.", "Autonomous Subscription & Expense Optimization")
    add_bullet(doc, "Dispatches task agents to dispute incorrect utility charges, medical bills, or travel cancellation fees with airline and hotel customer service channels, utilizing conversational negotiation strategies.", "Autonomous Consumer Dispute Mediation")
    add_bullet(doc, "Maintains personal and professional relationship rhythms, autonomously flagging upcoming birthdays, anniversaries, and key professional milestones, preparing thoughtful custom greetings and gift recommendations.", "Proactive Relationship & Gifting Management")

    add_header(doc, "4.4 Phase 4 Extension: B2B Enterprise Workforce Augmentation & PaaS Suite", level=2)
    add_bullet(doc, "Deploying teams of specialized agents (Sales Pipeline Agent, Customer Support Resolver, Code Review Assistant) that collaborate with human employees in shared Slack/Teams channels.", "Enterprise Multi-Agent Swarms")
    add_bullet(doc, "Bridging fragmented enterprise knowledge silos (Confluence, Jira, Salesforce, Google Drive) into a unified enterprise Graph RAG, allowing instant answers to complex organizational queries.", "Cross-Silo Enterprise Knowledge Graph")
    add_bullet(doc, "A comprehensive developer portal allowing third-party engineers to write custom agent tools, publish certified MCP connectors, and monetize domain-specific agentic skills.", "PaaS Developer SDK & Skill Marketplace")

    add_header(doc, "4.5 Phase 5 Extension: Embodied Physical Execution & Robotics Bridge", level=2)
    add_bullet(doc, "Translates calendar and schedule states into domestic IoT actions (e.g., activating robot vacuums when leaving for work, pre-cooling home office 30 minutes before arrival, adjusting lighting for deep focus).", "Matter & Thread Smart Domestic Orchestration")
    add_bullet(doc, "Connects high-level cognitive intentions ('Clean workspace before morning meeting') into spatial trajectories executed by domestic robotic appliances and emerging bimanual humanoid systems via Robot Operating System 2 (ROS2) and Vision-Language-Action (VLA) models.", "ROS2 & VLA Physical Actuation")

    # -------------------------------------------------------------
    # SECTION 5
    # -------------------------------------------------------------
    add_header(doc, "5. Industry Best Practices & Leader Success Stories", level=1)
    
    add_p(doc, 
        "Karmic AI incorporates proven engineering and product patterns established by current frontier AI research and industry leaders:")
    
    ind_table = doc.add_table(rows=6, cols=3)
    ind_headers = ["Industry Leader & Concept", "Core Technical Breakthrough", "Karmic AI Adaptation & Implementation"]
    ind_data = [
        ["Anthropic: Model Context Protocol (MCP)", 
         "Standardized open protocol connecting AI assistants directly to external data sources, local files, tools, and execution environments without proprietary API wrappers.", 
         "Adopted as the foundational tool-calling substrate. All external tools (Gmail, Google Calendar, File System, Notion, Slack) are wrapped as modular open-source MCP servers."],
         
        ["MemGPT / Letta: Hierarchical OS Memory", 
         "Treats LLM context windows like CPU RAM, introducing tiered memory management: working context, recall memory (FIFO vector store), and archival memory (persistent external store).", 
         "Implements a 4-tier memory hierarchy: working context buffer, short-term episodic vector store, persistent epistemic knowledge graph, and a nightly reflective consolidation cycle."],
         
        ["Rewind AI / Limitless: Continuous Ambient Context", 
         "Pioneered continuous background context capture (screen, audio, calendar) compressed locally with privacy-preserving semantic indexing.", 
         "Karmic AI captures calendar, email metadata, and task notes via local background daemons, embedding them into local vector stores with zero data leaving the user's machine."],
         
        ["LangGraph / CrewAI: Stateful Multi-Agent Graphs", 
         "Replaces brittle auto-regressive agent loops with deterministic state machines, human-in-the-loop checkpoints, and explicit supervisor-worker hierarchies.", 
         "Core orchestration engine built on LangGraph StateGraphs. High-stakes actions (sending external emails, modifying calendar events) require explicit user approval nodes."],
         
        ["Microsoft Research: GraphRAG", 
         "Combines knowledge graph extraction (entities, relationships, claims) with hierarchical Leiden community clustering to answer broad, global queries that standard vector search fails on.", 
         "Karmic AI deploys a hybrid Graph RAG pipeline utilizing PostgreSQL + Apache AGE / Neo4j alongside dense vector embeddings (BGE-M3) and cross-encoder rerankers."]
    ]
    format_table(ind_table, [1.8, 2.5, 2.5], ind_headers, ind_data)
    doc.add_paragraph().paragraph_format.space_after = Pt(4)

    # -------------------------------------------------------------
    # SECTION 6
    # -------------------------------------------------------------
    add_header(doc, "6. Comprehensive System Architecture & Engineering Blueprint", level=1)
    
    add_p(doc, 
        "The Karmic AI Platform is architected as a modular, event-driven, multi-tier system built on zero-trust security and low-latency execution:")
    
    add_callout(
        doc,
        "CORE ARCHITECTURAL TOPOLOGY",
        "Layer 1: User Interaction Layer (Desktop App, Web Dashboard, Mobile PWA, Ambient Audio)\n"
        "Layer 2: Zero-Trust Security & Identity Gateway (Decentralized ID, Local Master Keys, RBAC)\n"
        "Layer 3: Multi-Agent Cognitive Orchestrator (LangGraph Supervisor, Specialized Sub-Agents, HITL Review)\n"
        "Layer 4: Epistemic Memory & Hybrid RAG Engine (Postgres pgvector + Apache AGE Graph + Nightly Sleep Consolidation)\n"
        "Layer 5: Tool Execution Fabric (Model Context Protocol / Sandboxed Local Tools)\n"
        "Layer 6: Open-Source Inference Engine (Ollama / vLLM / llama.cpp local quantized SLMs/LLMs)\n"
        "Layer 7: Embodied Actuation Bridge (Matter/Thread Domestic IoT & ROS2 Robotics Middleware)",
        bg_hex="F8FAFC",
        border_color="0D9488"
    )
    
    add_header(doc, "6.1 Multi-Agent Orchestration Topology (LangGraph State Machine)", level=2)
    add_p(doc, 
        "Rather than relying on unconstrained autonomous loops that are prone to hallucination, Karmic AI uses a structured "
        "Supervisor-Worker StateGraph:")
    add_bullet(doc, "Ingests user prompts, emails, and calendar triggers. Categorizes incoming intents, checks user permissions, and routes tasks to specialized worker sub-agents.", "Supervisor Agent (Cognitive Router)")
    add_bullet(doc, "Analyzes incoming email messages, classifies urgency, extracts action items, queries the memory graph for tone and historical relationship context, and produces draft responses.", "Email & Communication Triage Agent")
    add_bullet(doc, "Parses proposed meeting requests, resolves calendar availability against user focus rules, computes optimal schedule density, and stages calendar invites.", "Calendar & Scheduling Agent")
    add_bullet(doc, "Executes multi-step information gathering across local files, documents, and external web APIs, synthesizing structured summaries with citation links.", "Deep Research & Knowledge Agent")
    add_bullet(doc, "Connects to MCP servers to execute verified actions (e.g., dispatch email, create calendar event, update task database, write file).", "Sandboxed Tool Executor Agent")
    add_bullet(doc, "Any action carrying external consequence (e.g., sending an email outside the organization, deleting an event) transitions the state machine into an awaiting-approval pause state, pushing a discrete notification to the user's dashboard.", "Human-in-the-Loop (HITL) Checkpoint")

    add_header(doc, "6.2 Advanced RAG Architecture: Hybrid Graph RAG & Tiered Epistemic Memory", level=2)
    add_p(doc, 
        "Standard vector RAG suffers from semantic blindspots: it cannot perform global multi-hop reasoning or understand evolving relationships. "
        "Karmic AI implements a state-of-the-art Hybrid Graph RAG framework:")
    add_bullet(doc, "Documents, emails, and notes are chunked (512 tokens with 64-token overlap). Dense embeddings are generated using the open-source BAAI/bge-m3 model (8192 context length, high-accuracy multilingual). Concurrent sparse BM25 lexical indices are maintained for precise keyword and entity matching.", "Dense & Sparse Vector Search")
    add_bullet(doc, "An asynchronous background pipeline extracts Entities (people, companies, projects, dates), Relations (works_with, reports_to, scheduled_for, priority_level), and Claims into a structural Knowledge Graph stored in PostgreSQL (Apache AGE extension) or Neo4j Community Edition.", "Knowledge Graph Triplet Extraction")
    add_bullet(doc, "Queries execute a dual retrieval: (1) Top-K semantic nearest neighbors from vector space, and (2) Top-N sub-graph traversal paths from the knowledge graph. The results are unified and reranked using BAAI/bge-reranker-large, discarding low-confidence noise.", "Reciprocal Rank Fusion & Cross-Encoder Reranking")
    add_bullet(doc, "During inactive periods (e.g., 03:00 AM local time), a background task summarizes the day's episodic interactions, abstracts new behavioral heuristics ('User prefers asynchronous Slack messages over Zoom calls before noon'), updates the knowledge graph, and prunes stale vector entries.", "Nightly Reflective Sleep Consolidation")

    add_header(doc, "6.3 Model Context Protocol (MCP) Integration", level=2)
    add_p(doc, 
        "Karmic AI natively adopts Anthropic's open-source Model Context Protocol (MCP) as the universal tool substrate. "
        "By separating cognitive model reasoning from physical tool servers, Karmic AI ensures modularity, security, and portability:")
    add_bullet(doc, "Connects to local user mailboxes via secure OAuth2 or local IMAP/SMTP, providing tools: list_unread_emails, get_thread_context, create_draft_reply, send_email.", "MCP Mail Server")
    add_bullet(doc, "Interfaces directly with Google Calendar / CalDAV, providing tools: get_day_schedule, find_free_slots, create_event, update_event, decline_conflict.", "MCP Calendar Server")
    add_bullet(doc, "Enables the agent to read, parse, and summarize local user markdown notes, PDFs, spreadsheets, and source code securely.", "MCP Filesystem & Knowledge Server")
    add_bullet(doc, "Allows the agent to search for public information via DuckDuckGo / SearXNG without tracking or subscription costs.", "MCP Web Search Server")

    # -------------------------------------------------------------
    # SECTION 7
    # -------------------------------------------------------------
    add_header(doc, "7. 100% Free & Open-Source Technology Stack", level=1)
    
    add_p(doc, 
        "To enable a rapid, low-friction prototype for 5-10 users with ZERO premium cloud subscription dependencies, "
        "the entire Karmic AI Platform is built exclusively on high-performance open-source technologies:")
    
    stack_table = doc.add_table(rows=11, cols=4)
    stack_headers = ["Layer / Subsystem", "Open-Source Technology", "License", "Role in Prototype & Scale"]
    stack_data = [
        ["Local LLM Inference Engine", "Ollama / llama.cpp / vLLM", "MIT / Apache 2.0", "Runs quantized foundation models locally on CPU or consumer GPU (RTX 3060/4080 or Apple Silicon M-series). Zero API billing."],
        ["Primary Foundation LLM", "Llama 3.3 70B (4-bit Q4_K_M) or Qwen 2.5 14B/32B", "Llama 3.3 Community / Apache 2.0", "Core cognitive reasoning, email drafting, task decomposition, and multi-agent coordination. Runs at 25-45 tokens/sec locally."],
        ["Lightweight Fast SLM", "Mistral NeMo 12B / Phi-4 14B / DeepSeek-R1-Distill-8B", "Apache 2.0 / MIT", "Sub-second intent classification, tool routing, email categorization, and entity extraction. Runs on minimal RAM."],
        ["Text Embedding Model", "BAAI/bge-m3 (Hugging Face)", "Apache 2.0", "Multilingual dense + sparse embeddings with 8192 token context. Runs locally via Sentence-Transformers / FastEmbed."],
        ["Cross-Encoder Reranker", "BAAI/bge-reranker-large", "Apache 2.0", "High-precision reranker scoring semantic relevance before context injection. 100% local CPU/GPU inference."],
        ["Vector Database", "PostgreSQL + pgvector", "PostgreSQL Open License", "Combines relational user records, session state, and high-dimensional vector embeddings in a single battle-tested database."],
        ["Knowledge Graph DB", "PostgreSQL + Apache AGE (or Neo4j Community)", "Apache 2.0 / GPLv3", "Stores graph nodes (Entities, Persons, Projects) and edges (Works_With, Attending, Priority). Supports Cypher queries."],
        ["Agent Orchestration Engine", "LangGraph (Python)", "MIT", "Stateful multi-agent state machines with persistence, branching, and human-in-the-loop pause/resume checkpoints."],
        ["Backend API Framework", "FastAPI + Pydantic v2 + Uvicorn", "MIT", "Asynchronous, high-throughput REST and WebSocket gateway serving agent interactions and MCP tool calls."],
        ["Task Queue & Cache", "Redis (Community) + Python Asyncio / Celery", "BSD 3-Clause", "In-memory caching of active conversation states, token rate limiting, and background RAG embedding queues."]
    ]
    format_table(stack_table, [1.4, 1.8, 1.2, 2.4], stack_headers, stack_data)
    doc.add_paragraph().paragraph_format.space_after = Pt(4)

    add_header(doc, "7.1 Frontend & User Interaction Stack (100% Free Open Source)", level=2)
    add_bullet(doc, "Next.js 15 (React 19, App Router) with Tailwind CSS, Lucide Icons, and shadcn/ui component library (MIT License). Modern, ultra-responsive dark-mode dashboard.", "Web Dashboard & PWA")
    add_bullet(doc, "Tauri v2 (Rust + Webview, MIT License) or Electron. Consumes under 60MB RAM on desktop, running lightweight tray daemons for instant keyboard shortcut invocation.", "Desktop Client Wrapper")
    add_bullet(doc, "FastAPI WebSocket endpoints providing real-time token-by-token streaming of agent thoughts, plan execution steps, and live approval cards.", "Real-Time Streaming Protocol")
    add_bullet(doc, "Entire platform packaged in a multi-container Docker Compose file (`docker-compose up -d`), orchestrating Ollama, Postgres/pgvector, Redis, FastAPI Backend, and Next.js Frontend with a single command.", "Containerization & Deployment")

    # -------------------------------------------------------------
    # SECTION 8
    # -------------------------------------------------------------
    add_header(doc, "8. 5-10 User Prototype Implementation Plan & Pilot Validation", level=1)
    
    add_p(doc, 
        "To validate product-market fit, execution latency, and autonomous reliability before scaling, "
        "a structured 4-week pilot deployment is established for 5 to 10 selected power users (founders, executives, tech leads):")
    
    sprint_table = doc.add_table(rows=5, cols=3)
    sprint_headers = ["Sprint Phase", "Core Engineering Objectives", "Deliverables & Verification Gate"]
    sprint_data = [
        ["Week 1: Core Foundation & Free Stack Assembly", 
         "• Deploy local Docker Compose stack (Ollama, PostgreSQL with pgvector, Redis, FastAPI).\n• Download and benchmark Llama 3.3 (or Qwen 2.5) and BGE-M3 embeddings.\n• Build local MCP connectors for Google Calendar and IMAP/Gmail.", 
         "Working CLI agent able to query calendar slots and list unread emails with zero paid API calls."],
         
        ["Week 2: Multi-Agent Workflows & Memory Fabric", 
         "• Implement LangGraph Supervisor, Triage, and Calendar agents.\n• Build Hybrid Vector + Graph RAG pipeline in PostgreSQL.\n• Implement persona style-cloning prompt templates based on historical sent emails.", 
         "End-to-end agentic workflow: Ingests 20 test emails, classifies urgency, and generates high-accuracy drafts matching user tone."],
         
        ["Week 3: Dashboard UI & Human-in-the-Loop Review Queue", 
         "• Build Next.js / shadcn dashboard with Daily Morning Briefing card, Pending Action Approval Queue, and Chat Assistant.\n• Implement WebSocket token streaming.\n• Package desktop webview / PWA wrapper.", 
         "Interactive UI where users can review drafted emails, approve calendar invites with 1-click, and inspect agent reasoning."],
         
        ["Week 4: 5-10 User Pilot Rollout & Validation", 
         "• Onboard 5-10 pilot users onto local or self-hosted instances.\n• Run live daily workflows (morning briefing, email triage, meeting booking).\n• Measure quantitative time savings, triage accuracy, and qualitative user delight.", 
         "Pilot Evaluation Report detailing daily hours saved, autonomous completion rates, and prioritized Phase 2 feature requests."]
    ]
    format_table(sprint_table, [1.5, 3.2, 2.1], sprint_headers, sprint_data)
    doc.add_paragraph().paragraph_format.space_after = Pt(4)

    add_header(doc, "8.1 Prototype Success Metrics & Evaluation Rubric", level=2)
    add_bullet(doc, "Target: >= 2.5 hours of administrative work saved per pilot user per day.", "Daily Time Liberation Metric")
    add_bullet(doc, "Target: >= 90% of drafted emails accepted as-is or with minor (< 10 word) edits.", "Persona Emulation Accuracy")
    add_bullet(doc, "Target: 0 unapproved external emails sent; 100% adherence to human-in-the-loop boundaries.", "Safety & Approval Compliance")
    add_bullet(doc, "Target: Sub-second initial response; complete draft generation under 8 seconds on local hardware.", "Inference & Tool Latency")
    add_bullet(doc, "Target: Net Promoter Score (NPS) >= 70 among pilot cohort.", "User Delight & Retention Intent")

    # -------------------------------------------------------------
    # SECTION 9
    # -------------------------------------------------------------
    add_header(doc, "9. Scalability Evolution: From Pilot to D2C & B2B SaaS/PaaS", level=1)
    
    add_p(doc, 
        "Following successful validation of the 5-10 user prototype, the architecture scales seamlessly into a production-grade multi-tenant platform:")
    
    add_header(doc, "9.1 Transition to Cloud-Native Multi-Tenant Architecture", level=2)
    add_bullet(doc, "Users with high-end personal workstations or Apple Silicon retain the 100% free local edge execution model. Users seeking hands-off zero-setup access are onboarded to managed sovereign cloud containers hosted on cost-effective dedicated GPU instances (e.g. RunPod, Lambda Labs, Hetzner).", "Hybrid Edge-Cloud Topology")
    add_bullet(doc, "Each user's knowledge graph and vector embeddings are stored in isolated cryptographic schemas with per-user tenant encryption keys. Even platform administrators cannot inspect memory graphs.", "Multi-Tenant Epistemic Vaults")
    add_bullet(doc, "B2B customers receive dedicated admin consoles with team-wide role-based access control (RBAC), audit logging, compliance dashboards, and shared organizational knowledge graphs.", "B2B Enterprise Control Plane")

    add_header(doc, "9.2 PaaS Developer Ecosystem & Skill Marketplace", level=2)
    add_bullet(doc, "Exposing standard REST, GraphQL, and WebSocket APIs allowing enterprise software teams to bind internal microservices directly into the Karmic agentic fabric.", "Karmic Agentic SDK")
    add_bullet(doc, "Third-party developers create and sell specialized skills (e.g., Legal Contract Auditor, Biotech Literature Synthesizer, Real Estate Lead Qualifier) through a certified skill store.", "PaaS Skill Marketplace (30% Platform Take-Rate)")

    # -------------------------------------------------------------
    # SECTION 10
    # -------------------------------------------------------------
    add_header(doc, "10. Phased Roadmap, Risk Matrix & Capital Efficiency", level=1)
    
    add_p(doc, "Comprehensive 24-Month Roadmap Across 4 Scaled Horizons:", bold=True)
    road_table = doc.add_table(rows=5, cols=4)
    road_headers = ["Phase & Horizon", "Timeframe", "Core Architectural Deliverables", "Target Scale & Traction"]
    road_data = [
        ["Phase 1: Cognitive Prototype & Pilot", "Months 0 - 3", "• 100% free open-source stack deployment.\n• Productivity & Efficiency Multi-Agent suite.\n• Hybrid Graph RAG in PostgreSQL.\n• 5-10 user intensive pilot validation.", "10 Active Pilot Users;\n2.5+ hours saved/day;\nZero external API costs."],
        ["Phase 2: D2C Commercial SaaS Launch", "Months 4 - 9", "• Electron/Tauri desktop app & mobile PWA.\n• Managed sovereign cloud hosting cluster.\n• Launch of $29-$49/mo Pro Tier.\n• Gmail, Outlook, Notion, Slack integrations.", "2,500 Paying Subscribers;\n$100K+ Monthly Recurring Revenue;\n92% monthly retention."],
        ["Phase 3: B2B Enterprise & PaaS Expansion", "Months 10 - 18", "• Enterprise multi-agent team swarms.\n• PaaS Developer SDK & MCP Skill Store.\n• Personal Health & Vitality twin integration.\n• SOC2 Type II compliance.", "25,000 Active Users;\n$1.2M ARR;\n30+ Certified MCP Partner skills."],
        ["Phase 4: Embodied Robotics & IoT Actuation", "Months 19 - 24", "• Matter & Thread smart domestic bridge.\n• ROS2 middleware for consumer cleaning robots.\n• VLA model integration for spatial tasks.\n• B2B2C Corporate Wellness partnerships.", "100,000+ Ecosystem Users;\n$5M+ ARR;\n3 Major hardware OEM partnerships."]
    ]
    format_table(road_table, [1.5, 1.1, 2.6, 1.6], road_headers, road_data)
    doc.add_paragraph().paragraph_format.space_after = Pt(4)

    add_header(doc, "10.1 Strategic Risk Analysis & Mitigation Matrix", level=2)
    risk_table = doc.add_table(rows=5, cols=3)
    risk_headers = ["Risk Domain", "Potential Impact", "Engineering & Operational Mitigation Strategy"]
    risk_data = [
        ["Agent Hallucinations & False Actions", 
         "High: Erroneous emails sent or improper calendar bookings damaging professional relationships.", 
         "Strict Human-in-the-Loop (HITL) checkpoints on all external mutations. State machines require user confirmation before executing any tool call with side effects."],
         
        ["Local Hardware Compute Constraints", 
         "Medium: Slow response latency on users' older laptops running local 70B models.", 
         "Dynamic model tiering: Lightweight 8B/12B models handle triage and routing with sub-second latency; optional seamless fallback to private self-hosted remote GPU cluster."],
         
        ["Privacy & Security Compromise", 
         "Critical: Unauthorized access to personal emails, calendar schedules, or identity graphs.", 
         "Local-first cryptographic enclaves. All credentials and API tokens stored in OS-native secure keychains (Apple Keychain / Windows Credential Vault). Zero cloud telemetry."],
         
        ["Third-Party API & Protocol Breakage", 
         "Medium: Upstream changes to Google, Microsoft, or Apple APIs breaking tool execution.", 
         "Adoption of Model Context Protocol (MCP) standardizes integration boundaries. Fail-safe degradation allows manual fallback when external services are unavailable."]
    ]
    format_table(risk_table, [1.5, 1.8, 3.5], risk_headers, risk_data)
    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # Document Save
    doc.save(filename)
    print(f"Master Architecture Document successfully generated: {filename}")

if __name__ == "__main__":
    build_docx()

