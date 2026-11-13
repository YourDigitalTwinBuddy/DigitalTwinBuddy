# -*- coding: utf-8 -*-
"""
create_presentation_deck.py
Generates a 14-slide widescreen presentation deck for Karmic AI Platform.
"""

import pptx
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

# Color Palette Constants
BG_COLOR = RGBColor(11, 15, 25)        # Deep Obsidian #0B0F19
CARD_BG = RGBColor(22, 30, 46)         # Dark Navy Slate #161E2E
CARD_BORDER = RGBColor(42, 54, 79)     # Border #2A364F
ACCENT_BLUE = RGBColor(59, 130, 246)   # Cobalt #3B82F6
ACCENT_GREEN = RGBColor(16, 185, 129)  # Mint #10B981
ACCENT_PURPLE = RGBColor(139, 92, 246) # Violet #8B5CF6
ACCENT_AMBER = RGBColor(245, 158, 11)  # Amber #F59E0B
TEXT_WHITE = RGBColor(248, 250, 252)   # White #F8FAFC
TEXT_MUTED = RGBColor(148, 163, 184)   # Slate Muted #94A3B8
TEXT_BODY = RGBColor(203, 213, 225)    # Slate Light #CBD5E1

def create_deck(filename="Karmic_AI_Platform_Presentation_Deck.pptx"):
    prs = pptx.Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6] # Blank
    
    def set_bg(slide):
        bg = slide.background
        fill = bg.fill
        fill.solid()
        fill.fore_color.rgb = BG_COLOR
        
    def add_slide_header(slide, tag, title, subtitle=""):
        # Tag / Category pill
        if tag:
            tb_tag = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.5), Inches(0.35))
            tf_tag = tb_tag.text_frame
            tf_tag.word_wrap = True
            p_tag = tf_tag.paragraphs[0]
            p_tag.space_after = Pt(0)
            r_tag = p_tag.add_run()
            r_tag.text = tag.upper()
            r_tag.font.name = 'Arial'
            r_tag.font.size = Pt(9.5)
            r_tag.font.bold = True
            r_tag.font.color.rgb = ACCENT_BLUE

        # Main Title
        tb_title = slide.shapes.add_textbox(Inches(0.8), Inches(0.7 if tag else 0.45), Inches(11.7), Inches(0.65))
        tf_title = tb_title.text_frame
        tf_title.word_wrap = True
        p_title = tf_title.paragraphs[0]
        p_title.space_after = Pt(0)
        r_title = p_title.add_run()
        r_title.text = title
        r_title.font.name = 'Arial'
        r_title.font.size = Pt(22)
        r_title.font.bold = True
        r_title.font.color.rgb = TEXT_WHITE
        
        # Subtitle
        if subtitle:
            tb_sub = slide.shapes.add_textbox(Inches(0.8), Inches(1.3), Inches(11.7), Inches(0.45))
            tf_sub = tb_sub.text_frame
            tf_sub.word_wrap = True
            p_sub = tf_sub.paragraphs[0]
            p_sub.space_after = Pt(0)
            r_sub = p_sub.add_run()
            r_sub.text = subtitle
            r_sub.font.name = 'Arial'
            r_sub.font.size = Pt(11)
            r_sub.font.color.rgb = TEXT_MUTED

    def add_card(slide, left, top, width, height, title="", title_color=ACCENT_BLUE, border_color=CARD_BORDER):
        # Card Background Shape
        shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left), Inches(top), Inches(width), Inches(height))
        shape.fill.solid()
        shape.fill.fore_color.rgb = CARD_BG
        shape.line.color.rgb = border_color
        shape.line.width = Pt(1.2)
        
        # If title, add header
        if title:
            tb = slide.shapes.add_textbox(Inches(left + 0.2), Inches(top + 0.15), Inches(width - 0.4), Inches(0.4))
            tf = tb.text_frame
            tf.word_wrap = True
            p = tf.paragraphs[0]
            p.space_after = Pt(0)
            r = p.add_run()
            r.text = title
            r.font.name = 'Arial'
            r.font.size = Pt(12)
            r.font.bold = True
            r.font.color.rgb = title_color
        return shape

    # =========================================================================
    # SLIDE 1: TITLE SLIDE
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    set_bg(s1)
    
    # Hero Title Box
    tb_hero = s1.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(11.3), Inches(3.2))
    tf_hero = tb_hero.text_frame
    tf_hero.word_wrap = True
    
    p0 = tf_hero.paragraphs[0]
    p0.space_after = Pt(10)
    r0 = p0.add_run()
    r0.text = "KARMIC AI PLATFORM"
    r0.font.name = 'Arial'
    r0.font.size = Pt(38)
    r0.font.bold = True
    r0.font.color.rgb = TEXT_WHITE
    
    p1 = tf_hero.add_paragraph()
    p1.space_after = Pt(16)
    r1 = p1.add_run()
    r1.text = "Sovereign Personal Digital Twin & Autonomous Agentic OS"
    r1.font.name = 'Arial'
    r1.font.size = Pt(20)
    r1.font.bold = True
    r1.font.color.rgb = ACCENT_BLUE
    
    p2 = tf_hero.add_paragraph()
    p2.space_after = Pt(24)
    r2 = p2.add_run()
    r2.text = "Dual D2C & B2B Architecture • Zero-Cost Open-Source Implementation Stack • 5-10 User Pilot Blueprint"
    r2.font.name = 'Arial'
    r2.font.size = Pt(13)
    r2.font.color.rgb = TEXT_MUTED

    # Bottom Meta Bar
    add_card(s1, 1.0, 5.4, 11.33, 1.1, title="", border_color=ACCENT_BLUE)
    tb_meta = s1.shapes.add_textbox(Inches(1.2), Inches(5.5), Inches(10.9), Inches(0.9))
    tf_meta = tb_meta.text_frame
    p_meta = tf_meta.paragraphs[0]
    p_meta.space_after = Pt(4)
    r_meta_h = p_meta.add_run()
    r_meta_h.text = "PHASE 1 EXECUTION FOCUS: PRODUCTIVITY & EFFICIENCY AGENTIC SUITE\n"
    r_meta_h.font.name = 'Arial'
    r_meta_h.font.size = Pt(10)
    r_meta_h.font.bold = True
    r_meta_h.font.color.rgb = ACCENT_GREEN
    
    r_meta_b = p_meta.add_run()
    r_meta_b.text = "Featuring Hybrid Graph RAG, Local Quantized SLMs (Ollama), LangGraph State Machines & Anthropic Model Context Protocol (MCP)"
    r_meta_b.font.name = 'Arial'
    r_meta_b.font.size = Pt(10)
    r_meta_b.font.color.rgb = TEXT_BODY

    # =========================================================================
    # SLIDE 2: THE PROBLEM STATEMENT
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    set_bg(s2)
    add_slide_header(s2, "The Macro Problem", "The Broken Execution Model of the Modern Knowledge Worker", "Knowledge workers spend 50%+ of daily working hours as manual human dispatchers")
    
    card_w = 3.6
    card_h = 4.8
    top_pos = 1.9
    
    # Card 1: Cognitive Churn
    add_card(s2, 0.8, top_pos, card_w, card_h, "1. Digital Administrative Churn", ACCENT_AMBER)
    tb = s2.shapes.add_textbox(Inches(1.0), Inches(top_pos + 0.65), Inches(card_w - 0.4), Inches(card_h - 0.8))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.space_after = Pt(8)
    r = p.add_run()
    r.text = "• 3-4 Hours Lost Daily: Constant context-switching across email, Slack, calendar reconciliation, and task follow-ups.\n\n• Decision Fatigue: Manual triage of hundreds of low-cognitive inbound pings leaves zero energy for deep strategic focus.\n\n• High-Stakes Friction: Missed deadlines, double-booked meetings, and delayed high-priority correspondences."
    r.font.name = 'Arial'
    r.font.size = Pt(10)
    r.font.color.rgb = TEXT_BODY
    
    # Card 2: Fragmentation of AI
    add_card(s2, 4.8, top_pos, card_w, card_h, "2. Current AI Architecture Flaws", ACCENT_BLUE)
    tb = s2.shapes.add_textbox(Inches(5.0), Inches(top_pos + 0.65), Inches(card_w - 0.4), Inches(card_h - 0.8))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.space_after = Pt(8)
    r = p.add_run()
    r.text = "• Ephemeral Context: Existing chatbots reset every conversation; zero long-term memory of user habits, ties, or tone.\n\n• Lack of True Agency: Current assistants can generate text but cannot safely execute real-world tool actions autonomously.\n\n• Cloud Privacy Exposure: Sending intimate personal correspondence to multi-tenant commercial LLMs risks massive data leakage."
    r.font.name = 'Arial'
    r.font.size = Pt(10)
    r.font.color.rgb = TEXT_BODY
    
    # Card 3: The Physical Void
    add_card(s2, 8.8, top_pos, card_w, card_h, "3. Physical & Domestic Deficit", ACCENT_PURPLE)
    tb = s2.shapes.add_textbox(Inches(9.0), Inches(top_pos + 0.65), Inches(card_w - 0.4), Inches(card_h - 0.8))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.space_after = Pt(8)
    r = p.add_run()
    r.text = "• 2-3 Hours Daily Household Drain: Meal prep, cleaning chores, and maintenance management remain completely disconnected from digital calendars.\n\n• Siloed Hardware: Smart appliances and robotic vacuums lack semantic user awareness; they do not know when calls occur or when homes are empty."
    r.font.name = 'Arial'
    r.font.size = Pt(10)
    r.font.color.rgb = TEXT_BODY

    # =========================================================================
    # SLIDE 3: THE KARMIC SOLUTION & DUAL HORIZON
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    set_bg(s3)
    add_slide_header(s3, "Product Vision", "Karmic AI: Sovereign Personal Digital Twin & Agentic OS", "Bridging Cognitive Agency, Autonomous Cyberspace Execution, and Physical Embodiment")
    
    col_w = 5.6
    col_h = 4.8
    top_pos = 1.9
    
    # Left Card: D2C Personal Twin
    add_card(s3, 0.8, top_pos, col_w, col_h, "D2C: Sovereign Personal Operating System", ACCENT_BLUE)
    tb = s3.shapes.add_textbox(Inches(1.0), Inches(top_pos + 0.65), Inches(col_w - 0.4), Inches(col_h - 0.8))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.space_after = Pt(8)
    r = p.add_run()
    r.text = "• Sovereign Persona Representation: Understands user style, relationships, and priorities; drafts communications in authenticated voice.\n\n• Autonomous Routine Orchestration: Morning briefings, calendar negotiation, task follow-ups, and subscription management.\n\n• Edge-Native & Zero-Leak Privacy: Epistemic memory vaults run locally or on sovereign private clouds with user-held encryption keys.\n\n• Target Users: Founders, C-suite executives, high-earning remote professionals (HENRYs), creators, and tech solopreneurs."
    r.font.name = 'Arial'
    r.font.size = Pt(10.5)
    r.font.color.rgb = TEXT_BODY
    
    # Right Card: B2B SaaS & PaaS
    add_card(s3, 6.9, top_pos, col_w, col_h, "B2B: Enterprise SaaS & Developer PaaS", ACCENT_GREEN)
    tb = s3.shapes.add_textbox(Inches(7.1), Inches(top_pos + 0.65), Inches(col_w - 0.4), Inches(col_h - 0.8))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.space_after = Pt(8)
    r = p.add_run()
    r.text = "• B2B SaaS Workforce Multiplier: Deploys dedicated agentic Chief-of-Staff twins to every team lead and executive, multiplying team throughput by 3x-5x.\n\n• Cross-Silo Organizational Graph: Unifies fragmented knowledge across Jira, Confluence, Slack, GitHub, and corporate mailboxes.\n\n• B2B PaaS Developer Platform: Exposes extensible Agentic SDK and MCP skill registry for internal IT and enterprise workflow developers.\n\n• Corporate Wellness & Benefit Channel: Subsidized employer benefit driving rapid, low-CAC enterprise-wide adoption."
    r.font.name = 'Arial'
    r.font.size = Pt(10.5)
    r.font.color.rgb = TEXT_BODY

    # =========================================================================
    # SLIDE 4: VALUE PROPOSITION MATRIX
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    set_bg(s4)
    add_slide_header(s4, "Value Proposition", "Strategic Value Drivers: Returning 4 to 6 Hours Daily", "Transforming human operators from manual dispatchers into strategic directors")
    
    v_w = 2.8
    v_h = 4.8
    top_pos = 1.9
    
    # 4 Cards across
    metrics = [
        ("4-6 Hours Saved", "Daily Time Liberation", ACCENT_GREEN, "Eliminates cognitive drag from inbox zero, calendar ping-pong, and repetitive follow-ups. Unlocks deep creative and strategic focus blocks."),
        ("Zero Cognitive Churn", "Proactive Agency", ACCENT_BLUE, "Autonomous multi-agent swarms anticipate scheduling conflicts, prioritize urgent correspondence, and stage actions before being asked."),
        ("100% Zero-Leak Privacy", "Cryptographic Sovereignty", ACCENT_PURPLE, "Memory vaults and inference run on local hardware or private VPCs. Deep personal identity telemetry never leaks to third parties."),
        ("3x-5x Team Velocity", "B2B SaaS Multiplier", ACCENT_AMBER, "Replaces fractional administrative staff and automates cross-silo context sharing across distributed engineering and leadership teams.")
    ]
    
    for i, (m_val, m_title, col, m_desc) in enumerate(metrics):
        x_pos = 0.8 + i * 2.95
        add_card(s4, x_pos, top_pos, v_w, v_h, m_title, col)
        
        # Big Metric
        tb_m = s4.shapes.add_textbox(Inches(x_pos + 0.15), Inches(top_pos + 0.7), Inches(v_w - 0.3), Inches(0.8))
        tf_m = tb_m.text_frame
        p_m = tf_m.paragraphs[0]
        r_m = p_m.add_run()
        r_m.text = m_val
        r_m.font.name = 'Arial'
        r_m.font.size = Pt(16)
        r_m.font.bold = True
        r_m.font.color.rgb = col
        
        # Description
        tb_d = s4.shapes.add_textbox(Inches(x_pos + 0.15), Inches(top_pos + 1.6), Inches(v_w - 0.3), Inches(2.9))
        tf_d = tb_d.text_frame
        tf_d.word_wrap = True
        p_d = tf_d.paragraphs[0]
        r_d = p_d.add_run()
        r_d.text = m_desc
        r_d.font.name = 'Arial'
        r_d.font.size = Pt(9.5)
        r_d.font.color.rgb = TEXT_BODY

    # =========================================================================
    # SLIDE 5: THE 9-BOX BUSINESS MODEL CANVAS
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    set_bg(s5)
    add_slide_header(s5, "Business Model", "The 9-Box Business Model Canvas", "Structured for High LTV, Frugal R&D Burn, and Multi-Tiered Monetization")
    
    # 3x3 Grid
    grid_w = 3.75
    grid_h = 1.45
    boxes = [
        # Row 1
        ("8. Key Partners", "• Open-source AI ecosystems (Ollama, Hugging Face, LangGraph)\n• Hardware OEMs (Matter/Thread, ROS2)\n• Enterprise SaaS (Google, Microsoft, Slack)", ACCENT_BLUE, 0.8, 1.9),
        ("7. Key Activities", "• Multi-agent orchestration & StateGraph R&D\n• Epistemic Graph RAG memory optimization\n• MCP connector certification & security", ACCENT_BLUE, 4.8, 1.9),
        ("2. Value Propositions", "• Sovereign Personal Twin returning 4-6 hrs/day\n• Zero-leak privacy via local-first architecture\n• Enterprise workforce productivity multiplier", ACCENT_GREEN, 8.8, 1.9),
        
        # Row 2
        ("6. Key Resources", "• Epistemic Graph RAG memory schemas\n• Open-source agent orchestration state graphs\n• Fine-tuned specialized SLM weights", ACCENT_PURPLE, 0.8, 3.5),
        ("4. Customer Relationships", "• High-intimacy lifelong digital twin partner\n• High switching cost via compounding memory\n• White-glove enterprise deployment", ACCENT_PURPLE, 4.8, 3.5),
        ("1. Customer Segments", "• D2C: Executives, founders, HENRYs, creators\n• B2B SaaS: High-growth tech teams, consultancies\n• PaaS: AI developers & robotics integrators", ACCENT_GREEN, 8.8, 3.5),
        
        # Row 3
        ("9. Cost Structure", "• $0 Prototype API cost (100% free open stack)\n• Dedicated GPU spot instances (RunPod/Lambda)\n• Core engineering talent & security audits", ACCENT_AMBER, 0.8, 5.1),
        ("3. Channels", "• Product-Led Growth (Free self-hosted core)\n• B2B2C Corporate Wellness benefit programs\n• Open MCP Skill Directory distribution", ACCENT_AMBER, 4.8, 5.1),
        ("5. Revenue Streams", "• D2C Pro ($29-$49/mo) & Executive ($99/mo)\n• B2B SaaS ($35-$60/user/mo)\n• PaaS API billing & 30% Skill Store take-rate", ACCENT_GREEN, 8.8, 5.1),
    ]
    
    for title, text, col, x, y in boxes:
        add_card(s5, x, y, grid_w, grid_h, title, col)
        tb = s5.shapes.add_textbox(Inches(x + 0.1), Inches(y + 0.38), Inches(grid_w - 0.2), Inches(grid_h - 0.42))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        r = p.add_run()
        r.text = text
        r.font.name = 'Arial'
        r.font.size = Pt(8)
        r.font.color.rgb = TEXT_BODY

    # =========================================================================
    # SLIDE 6: PHASE 1 FOCUS - PRODUCTIVITY & EFFICIENCY
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    set_bg(s6)
    add_slide_header(s6, "Phase 1 Priority", "Productivity & Efficiency Suite: 5-10 User Pilot Core", "Six foundational capabilities delivering immediate time liberation")
    
    f_w = 3.65
    f_h = 2.2
    
    features = [
        ("Adaptive Morning Briefing", "Synthesizes unread emails, upcoming meetings, task priorities, and recommended deep focus blocks into an actionable 7:00 AM briefing.", ACCENT_BLUE, 0.8, 1.9),
        ("Autonomous Email Triage & Drafting", "Classifies urgency, extracts action items, queries historical relationship context, and drafts replies in the exact voice of the user.", ACCENT_GREEN, 4.8, 1.9),
        ("Proactive Calendar Negotiation", "Autonomously resolves scheduling conflicts, coordinates slots with external parties, and enforces focus rules without human intervention.", ACCENT_PURPLE, 8.8, 1.9),
        ("Intelligent Task Decomposition", "Breaks complex projects ('Prepare Board Deck') into structured sub-tasks with estimated time allocations, dependency links, and automated tracking.", ACCENT_AMBER, 0.8, 4.4),
        ("Private Document Graph RAG", "Allows natural language queries across emails, notes, PDFs, and codebases, returning grounded answers with exact source citations.", ACCENT_BLUE, 4.8, 4.4),
        ("Multi-Agent Swarm Orchestration", "Supervisor Agent delegates sub-tasks across specialized Triage, Calendar, Research, and Tool Execution worker agents via LangGraph.", ACCENT_GREEN, 8.8, 4.4),
    ]
    
    for title, desc, col, x, y in features:
        add_card(s6, x, y, f_w, f_h, title, col)
        tb = s6.shapes.add_textbox(Inches(x + 0.15), Inches(y + 0.5), Inches(f_w - 0.3), Inches(f_h - 0.6))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        r = p.add_run()
        r.text = desc
        r.font.name = 'Arial'
        r.font.size = Pt(9.5)
        r.font.color.rgb = TEXT_BODY

    # =========================================================================
    # SLIDE 7: FUTURE EXPANSIONS - HEALTH, B2B & EMBODIED ROBOTICS
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    set_bg(s7)
    add_slide_header(s7, "Future Horizons", "Evolutionary Expansion: Health, Finance, B2B & Robotics", "A seamless progression from digital cognitive assistant to embodied domestic OS")
    
    col_w = 2.8
    col_h = 4.8
    top_pos = 1.9
    
    expansions = [
        ("Phase 2: Health & Longevity", ACCENT_GREEN, "• Continuous Wearable Sync: Ingestion of Apple Health, Oura, Whoop biomarkers (HRV, Sleep, Recovery).\n\n• Circadian Scheduling: Dynamically alters calendar density based on sleep recovery scores.\n\n• Longevity Protocols: Proactive hydration, nutrition, and mobility prompts aligned with daily exertion."),
        ("Phase 3: Financial Ops", ACCENT_AMBER, "• Subscription Optimization: Scans statements, identifies zombie software, and automates cancellation.\n\n• Consumer Dispute Agents: Negotiates flight delays, incorrect utility bills, and medical charges.\n\n• Relationship Rhythms: Automated gift suggestions and thoughtful milestone greetings."),
        ("Phase 4: B2B Enterprise & PaaS", ACCENT_BLUE, "• Enterprise Swarms: Specialized agents embedded in Slack/Teams for sales, engineering, and support.\n\n• Enterprise Graph RAG: Unifies Jira, Confluence, Salesforce, and Google Drive.\n\n• PaaS Developer SDK: Public MCP marketplace for third-party domain skill monetization."),
        ("Phase 5: Embodied Robotics", ACCENT_PURPLE, "• Domestic IoT Bridge: Matter and Thread integration for automated home climate and lighting.\n\n• Robotic Cleaning Choreography: Scheduled vacuum/mop dispatch during out-of-home windows.\n\n• ROS2 & VLA Middleware: Translating high-level cognitive intent to bimanual humanoid actuators.")
    ]
    
    for i, (title, col, desc) in enumerate(expansions):
        x_pos = 0.8 + i * 2.95
        add_card(s7, x_pos, top_pos, col_w, col_h, title, col)
        tb = s7.shapes.add_textbox(Inches(x_pos + 0.15), Inches(top_pos + 0.65), Inches(col_w - 0.3), Inches(col_h - 0.8))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        r = p.add_run()
        r.text = desc
        r.font.name = 'Arial'
        r.font.size = Pt(9.5)
        r.font.color.rgb = TEXT_BODY

    # =========================================================================
    # SLIDE 8: INDUSTRY BEST PRACTICES & SUCCESS STORIES
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    set_bg(s8)
    add_slide_header(s8, "Industry Best Practices", "Incorporating Breakthroughs from Frontier AI Leaders", "Standing on the shoulders of the most successful agentic and memory architectures")
    
    col_w = 5.6
    col_h = 2.2
    
    stories = [
        ("Anthropic: Model Context Protocol (MCP)", "Standardized open protocol connecting agents directly to tools, databases, and local files. Karmic AI adopts MCP as its universal execution substrate.", ACCENT_BLUE, 0.8, 1.9),
        ("MemGPT / Letta: Hierarchical OS Memory", "Treats LLM context windows as volatile RAM with tiered memory (working, recall, archival). Karmic AI introduces a 4-tier Epistemic Memory architecture.", ACCENT_GREEN, 6.9, 1.9),
        ("LangGraph: Deterministic State Machines", "Replaces brittle loop prompts with deterministic state graphs, human-in-the-loop checkpoints, and explicit supervisor routing for high safety.", ACCENT_PURPLE, 0.8, 4.4),
        ("Microsoft: GraphRAG Framework", "Combines knowledge graph triplet extraction with hierarchical Leiden clustering to answer global, multi-hop relationship queries that vector search misses.", ACCENT_AMBER, 6.9, 4.4),
    ]
    
    for title, desc, col, x, y in stories:
        add_card(s8, x, y, col_w, col_h, title, col)
        tb = s8.shapes.add_textbox(Inches(x + 0.2), Inches(y + 0.6), Inches(col_w - 0.4), Inches(col_h - 0.8))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        r = p.add_run()
        r.text = desc
        r.font.name = 'Arial'
        r.font.size = Pt(10)
        r.font.color.rgb = TEXT_BODY

    # =========================================================================
    # SLIDE 9: SYSTEM ARCHITECTURE
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    set_bg(s9)
    add_slide_header(s9, "Engineering Blueprint", "End-to-End System Architecture & Execution Flow", "Event-driven, modular multi-agent topology designed for low latency and zero data leakage")
    
    layers = [
        ("Layer 1: Interaction Layer", "Next.js 15 PWA • Tauri/Electron Desktop Tray • WebSocket Streaming Client", ACCENT_BLUE, 1.9),
        ("Layer 2: Zero-Trust Security Gateway", "Decentralized ID (DID) • Local OS Keychains (OAuth2) • Human-in-the-Loop Checkpoints", ACCENT_PURPLE, 2.85),
        ("Layer 3: Cognitive Multi-Agent Swarm", "LangGraph Supervisor • Email Triage Agent • Calendar Agent • Deep Research Agent", ACCENT_GREEN, 3.8),
        ("Layer 4: Epistemic Memory & Hybrid RAG", "PostgreSQL pgvector (Dense/BM25) • Apache AGE / Neo4j Graph • Nightly Sleep Consolidation", ACCENT_AMBER, 4.75),
        ("Layer 5: Tool Execution & Inference Fabric", "Anthropic MCP Tool Servers (Mail, Calendar, Files) • Ollama / vLLM Local Inference", ACCENT_BLUE, 5.7)
    ]
    
    for title, tech, col, y in layers:
        add_card(s9, 0.8, y, 11.73, 0.78, title, col)
        tb = s9.shapes.add_textbox(Inches(4.2), Inches(y + 0.15), Inches(8.0), Inches(0.45))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        r = p.add_run()
        r.text = tech
        r.font.name = 'Arial'
        r.font.size = Pt(9.5)
        r.font.bold = True
        r.font.color.rgb = TEXT_WHITE

    # =========================================================================
    # SLIDE 10: ADVANCED RAG & MEMORY SUBSYSTEM
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    set_bg(s10)
    add_slide_header(s10, "Memory & RAG", "Hybrid Graph RAG & Tiered Epistemic Memory Fabric", "Transcending basic vector search through structural knowledge graphs and reflective learning")
    
    col_w = 3.65
    col_h = 4.8
    top_pos = 1.9
    
    add_card(s10, 0.8, top_pos, col_w, col_h, "1. Hybrid Search Subsystem", ACCENT_BLUE)
    tb = s10.shapes.add_textbox(Inches(1.0), Inches(top_pos + 0.65), Inches(col_w - 0.4), Inches(col_h - 0.8))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = "• Dense Embeddings: BAAI/bge-m3 model (8192 token context, multilingual).\n\n• Sparse Lexical Search: Concurrent BM25 indexing in PostgreSQL for exact keywords and code identifiers.\n\n• Reciprocal Rank Fusion: Merges vector proximity with keyword match scores.\n\n• Cross-Encoder Reranking: BAAI/bge-reranker-large scores unified candidates locally."
    r.font.name = 'Arial'
    r.font.size = Pt(9.5)
    r.font.color.rgb = TEXT_BODY
    
    add_card(s10, 4.8, top_pos, col_w, col_h, "2. Epistemic Knowledge Graph", ACCENT_GREEN)
    tb = s10.shapes.add_textbox(Inches(5.0), Inches(top_pos + 0.65), Inches(col_w - 0.4), Inches(col_h - 0.8))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = "• Entity & Relation Extraction: Asynchronous pipeline extracts Persons, Organizations, Projects, and Deadlines.\n\n• Graph Storage: Stored directly in PostgreSQL using Apache AGE extension (or Neo4j Community).\n\n• Multi-Hop Reasoning: Answers complex queries ('Who did I meet regarding Project Titan last November?')."
    r.font.name = 'Arial'
    r.font.size = Pt(9.5)
    r.font.color.rgb = TEXT_BODY
    
    add_card(s10, 8.8, top_pos, col_w, col_h, "3. Reflective Sleep Consolidation", ACCENT_PURPLE)
    tb = s10.shapes.add_textbox(Inches(9.0), Inches(top_pos + 0.65), Inches(col_w - 0.4), Inches(col_h - 0.8))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = "• Nightly Background Cron: Triggers during inactive hours (03:00 AM local time).\n\n• Episodic Summarization: Condenses daily interactions into durable behavioral rules.\n\n• Style Calibration: Analyzes user manual edits to fine-tune persona drafting templates.\n\n• Memory Pruning: Cleans obsolete cache vectors while preserving core graph facts."
    r.font.name = 'Arial'
    r.font.size = Pt(9.5)
    r.font.color.rgb = TEXT_BODY

    # =========================================================================
    # SLIDE 11: 100% FREE & OPEN-SOURCE TECH STACK
    # =========================================================================
    s11 = prs.slides.add_slide(blank_layout)
    set_bg(s11)
    add_slide_header(s11, "Implementation Stack", "100% Free & Open-Source Technology Stack", "Zero subscription fees, zero proprietary API dependencies for the 5-10 user prototype")
    
    grid_w = 3.65
    grid_h = 2.2
    
    stack_boxes = [
        ("Inference Engine & LLMs", "• Ollama / llama.cpp / vLLM (Local runtime)\n• Llama 3.3 70B (4-bit Q4_K_M) - Primary reasoning\n• Mistral NeMo 12B / Phi-4 - Sub-second routing\n• 100% Free, zero token billing", ACCENT_BLUE, 0.8, 1.9),
        ("Embeddings & Reranking", "• BAAI/bge-m3 (8192 token context, multilingual)\n• BAAI/bge-reranker-large (Cross-encoder)\n• Local execution via Sentence-Transformers\n• State-of-the-art retrieval accuracy", ACCENT_GREEN, 4.8, 1.9),
        ("Vector & Graph Database", "• PostgreSQL 16 (Relational + Metadata)\n• pgvector extension (High-speed vector indexing)\n• Apache AGE extension (Graph Cypher queries)\n• Single unified self-hosted data store", ACCENT_PURPLE, 8.8, 1.9),
        ("Agent Orchestration", "• LangGraph (Python state machine)\n• State persistence & memory checkpoints\n• Human-in-the-loop review nodes\n• Modular supervisor-worker topology", ACCENT_AMBER, 0.8, 4.4),
        ("Tool Protocol & Backend", "• Anthropic Model Context Protocol (MCP)\n• Open-source Mail, Calendar, Filesystem MCPs\n• FastAPI + Pydantic v2 + Uvicorn\n• Redis for session cache and rate limits", ACCENT_BLUE, 4.8, 4.4),
        ("Frontend & Containerization", "• Next.js 15 (React 19) + Tailwind CSS + shadcn\n• Tauri v2 / Electron desktop tray client\n• Docker & Docker Compose deployment\n• Single command setup: docker-compose up -d", ACCENT_GREEN, 8.8, 4.4)
    ]
    
    for title, desc, col, x, y in stack_boxes:
        add_card(s11, x, y, grid_w, grid_h, title, col)
        tb = s11.shapes.add_textbox(Inches(x + 0.15), Inches(y + 0.5), Inches(grid_w - 0.3), Inches(grid_h - 0.6))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        r = p.add_run()
        r.text = desc
        r.font.name = 'Arial'
        r.font.size = Pt(8.5)
        r.font.color.rgb = TEXT_BODY

    # =========================================================================
    # SLIDE 12: 5-10 USER PILOT VALIDATION PLAN
    # =========================================================================
    s12 = prs.slides.add_slide(blank_layout)
    set_bg(s12)
    add_slide_header(s12, "Pilot Execution", "5-to-10 User Prototype Validation Plan", "A 4-week structured sprint to validate time savings, accuracy, and user delight")
    
    col_w = 2.8
    col_h = 4.8
    top_pos = 1.9
    
    sprints = [
        ("Week 1: Core Foundation", ACCENT_BLUE, "• Deploy local Docker stack (Ollama, Postgres, Redis, FastAPI).\n\n• Download & benchmark Llama 3.3 & BGE-M3.\n\n• Build local MCP connectors for Google Calendar & Gmail.\n\n• Gate: Working CLI agent reading schedules and emails."),
        ("Week 2: Multi-Agent & RAG", ACCENT_GREEN, "• Implement LangGraph Supervisor, Triage, and Calendar agents.\n\n• Setup Hybrid Vector + Graph RAG in PostgreSQL.\n\n• Persona style-cloning template calibration.\n\n• Gate: Autonomous triage of 20 emails with high tone fidelity."),
        ("Week 3: Dashboard UI", ACCENT_PURPLE, "• Build Next.js / shadcn dashboard with Morning Briefing card.\n\n• Human-in-the-loop review queue for 1-click approvals.\n\n• WebSocket token streaming.\n\n• Gate: Complete desktop UI with interactive approvals."),
        ("Week 4: Live Cohort Pilot", ACCENT_AMBER, "• Onboard 5-10 pilot knowledge workers.\n\n• Run live daily workflows for 7 business days.\n\n• Collect telemetry on hours saved and accuracy.\n\n• Gate: Pilot Evaluation Report & prioritized Phase 2 roadmap.")
    ]
    
    for i, (title, col, desc) in enumerate(sprints):
        x_pos = 0.8 + i * 2.95
        add_card(s12, x_pos, top_pos, col_w, col_h, title, col)
        tb = s12.shapes.add_textbox(Inches(x_pos + 0.15), Inches(top_pos + 0.65), Inches(col_w - 0.3), Inches(col_h - 0.8))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        r = p.add_run()
        r.text = desc
        r.font.name = 'Arial'
        r.font.size = Pt(9.5)
        r.font.color.rgb = TEXT_BODY

    # =========================================================================
    # SLIDE 13: SCALABILITY & 24-MONTH ROADMAP
    # =========================================================================
    s13 = prs.slides.add_slide(blank_layout)
    set_bg(s13)
    add_slide_header(s13, "Roadmap & Scaling", "24-Month Phased Scale: From Prototype to Global Platform", "Disciplined progression from local pilot to multi-million ARR D2C and B2B SaaS/PaaS")
    
    card_w = 11.73
    card_h = 1.05
    
    phases = [
        ("Phase 1: Cognitive Prototype & Pilot (M0-M3)", "10 Pilot Users • 100% free open-source stack • Productivity suite • Hybrid Graph RAG • $0 external API burn", ACCENT_BLUE, 1.9),
        ("Phase 2: D2C Commercial SaaS Launch (M4-M9)", "2,500 Paying Subscribers • $100K+ MRR • Pro Tier ($29-$49/mo) • Managed sovereign cloud • Desktop app", ACCENT_GREEN, 3.1),
        ("Phase 3: B2B Enterprise & PaaS Expansion (M10-M18)", "25,000 Active Users • $1.2M ARR • Enterprise agent swarms • PaaS Developer SDK • Health twin • SOC2 Type II", ACCENT_PURPLE, 4.3),
        ("Phase 4: Embodied Robotics & IoT Actuation (M19-M24)", "100,000+ Users • $5M+ ARR • Matter/Thread smart domestic bridge • ROS2 cleaning robotics • 3 OEM partners", ACCENT_AMBER, 5.5)
    ]
    
    for title, desc, col, y in phases:
        add_card(s13, 0.8, y, card_w, card_h, title, col)
        tb = s13.shapes.add_textbox(Inches(1.0), Inches(y + 0.45), Inches(card_w - 0.4), Inches(0.5))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        r = p.add_run()
        r.text = desc
        r.font.name = 'Arial'
        r.font.size = Pt(10)
        r.font.color.rgb = TEXT_BODY

    # =========================================================================
    # SLIDE 14: STRATEGIC MOAT & NEXT STEPS
    # =========================================================================
    s14 = prs.slides.add_slide(blank_layout)
    set_bg(s14)
    add_slide_header(s14, "Strategic Moat & Execution", "Why Karmic AI Wins: Compounding Moat & Immediate Next Steps", "A defensible data and architectural moat returning time to humanity")
    
    col_w = 5.6
    col_h = 4.8
    top_pos = 1.9
    
    # Left Card: The Moat
    add_card(s14, 0.8, top_pos, col_w, col_h, "The Karmic Strategic Moat", ACCENT_GREEN)
    tb = s14.shapes.add_textbox(Inches(1.0), Inches(top_pos + 0.65), Inches(col_w - 0.4), Inches(col_h - 0.8))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = "• Compounding Episodic Memory: The longer a user interacts with Karmic, the richer their epistemic graph becomes. Context-switching costs are insurmountable.\n\n• Local-First Privacy Guarantee: Unassailable trust moat against big tech cloud surveillance.\n\n• Physical-Digital Bidirectional Grounding: Digital calendar context drives domestic hardware; physical home states inform digital twin planning.\n\n• Frugal Capital Efficiency: Built on open-source foundation; gross margins exceed 78% due to localized/optimized SLM inference."
    r.font.name = 'Arial'
    r.font.size = Pt(10.5)
    r.font.color.rgb = TEXT_BODY
    
    # Right Card: Next Steps
    add_card(s14, 6.9, top_pos, col_w, col_h, "Immediate Action Items & Next Steps", ACCENT_BLUE)
    tb = s14.shapes.add_textbox(Inches(7.1), Inches(top_pos + 0.65), Inches(col_w - 0.4), Inches(col_h - 0.8))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = "1. Review & Align on Architecture Blueprint: Validate document with core stakeholders.\n\n2. Initialize Local Dev Environment: Setup `docker-compose.yml` for Ollama, PostgreSQL (pgvector/AGE), Redis, and FastAPI.\n\n3. Select 5-10 Pilot Users: Formalize agreements with early-adopter founders and remote executives.\n\n4. Execute Week 1 Sprint: Benchmark local Llama 3.3 & assemble core MCP calendar and mail connectors.\n\n5. Review Prototype Milestone in 4 Weeks: Assess empirical hours saved before expanding to Health & Longevity."
    r.font.name = 'Arial'
    r.font.size = Pt(10.5)
    r.font.color.rgb = TEXT_BODY

    prs.save(filename)
    print(f"Presentation deck successfully generated: {filename}")

if __name__ == "__main__":
    create_deck()

