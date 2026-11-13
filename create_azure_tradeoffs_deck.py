# -*- coding: utf-8 -*-
"""
create_azure_tradeoffs_deck.py
Generates the executive decision deck:
"Karmic_AI_Azure_vs_Free_Tradeoff_Deck.pptx" (12 widescreen 16:9 slides)
"""

import pptx
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

# Color Palette
BG_COLOR = RGBColor(11, 15, 25)        # Deep Obsidian #0B0F19
CARD_BG = RGBColor(22, 30, 46)         # Dark Navy Slate #161E2E
CARD_BORDER = RGBColor(42, 54, 79)     # Border #2A364F
AZURE_BLUE = RGBColor(0, 120, 212)     # Microsoft Azure Blue #0078D4
ACCENT_GREEN = RGBColor(16, 185, 129)  # Mint Green #10B981
ACCENT_PURPLE = RGBColor(139, 92, 246) # Violet #8B5CF6
ACCENT_AMBER = RGBColor(245, 158, 11)  # Amber #F59E0B
TEXT_WHITE = RGBColor(248, 250, 252)   # White #F8FAFC
TEXT_MUTED = RGBColor(148, 163, 184)   # Slate Muted #94A3B8
TEXT_BODY = RGBColor(203, 213, 225)    # Slate Light #CBD5E1

def create_deck(filename="Karmic_AI_Azure_vs_Free_Tradeoff_Deck.pptx"):
    prs = pptx.Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]
    
    def set_bg(slide):
        bg = slide.background
        fill = bg.fill
        fill.solid()
        fill.fore_color.rgb = BG_COLOR
        
    def add_slide_header(slide, tag, title, subtitle=""):
        if tag:
            tb_tag = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.5), Inches(0.35))
            tf_tag = tb_tag.text_frame
            tf_tag.word_wrap = True
            p_tag = tf_tag.paragraphs[0]
            r_tag = p_tag.add_run()
            r_tag.text = tag.upper()
            r_tag.font.name = 'Arial'
            r_tag.font.size = Pt(9.5)
            r_tag.font.bold = True
            r_tag.font.color.rgb = AZURE_BLUE

        tb_title = slide.shapes.add_textbox(Inches(0.8), Inches(0.7 if tag else 0.45), Inches(11.7), Inches(0.65))
        tf_title = tb_title.text_frame
        tf_title.word_wrap = True
        p_title = tf_title.paragraphs[0]
        r_title = p_title.add_run()
        r_title.text = title
        r_title.font.name = 'Arial'
        r_title.font.size = Pt(22)
        r_title.font.bold = True
        r_title.font.color.rgb = TEXT_WHITE
        
        if subtitle:
            tb_sub = slide.shapes.add_textbox(Inches(0.8), Inches(1.3), Inches(11.7), Inches(0.45))
            tf_sub = tb_sub.text_frame
            tf_sub.word_wrap = True
            p_sub = tf_sub.paragraphs[0]
            r_sub = p_sub.add_run()
            r_sub.text = subtitle
            r_sub.font.name = 'Arial'
            r_sub.font.size = Pt(11)
            r_sub.font.color.rgb = TEXT_MUTED

    def add_card(slide, left, top, width, height, title="", title_color=AZURE_BLUE, border_color=CARD_BORDER):
        shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left), Inches(top), Inches(width), Inches(height))
        shape.fill.solid()
        shape.fill.fore_color.rgb = CARD_BG
        shape.line.color.rgb = border_color
        shape.line.width = Pt(1.2)
        
        if title:
            tb = slide.shapes.add_textbox(Inches(left + 0.2), Inches(top + 0.15), Inches(width - 0.4), Inches(0.4))
            tf = tb.text_frame
            tf.word_wrap = True
            p = tf.paragraphs[0]
            r = p.add_run()
            r.text = title
            r.font.name = 'Arial'
            r.font.size = Pt(12)
            r.font.bold = True
            r.font.color.rgb = title_color
        return shape

    # SLIDE 1: Title
    s1 = prs.slides.add_slide(blank_layout)
    set_bg(s1)
    tb_hero = s1.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(11.3), Inches(3.2))
    tf_hero = tb_hero.text_frame
    tf_hero.word_wrap = True
    p0 = tf_hero.paragraphs[0]
    r0 = p0.add_run()
    r0.text = "KARMIC AI PLATFORM"
    r0.font.name = 'Arial'
    r0.font.size = Pt(36)
    r0.font.bold = True
    r0.font.color.rgb = TEXT_WHITE
    
    p1 = tf_hero.add_paragraph()
    r1 = p1.add_run()
    r1.text = "Enterprise Azure Architecture, Token Economics & 90-Day Acceleration Blueprint"
    r1.font.name = 'Arial'
    r1.font.size = Pt(20)
    r1.font.bold = True
    r1.font.color.rgb = AZURE_BLUE
    
    p2 = tf_hero.add_paragraph()
    r2 = p2.add_run()
    r2.text = "Comprehensive Trade-Off Analysis: Free Open-Source vs. Azure Managed Cloud • Unit Economics • 12-Week Sprint"
    r2.font.name = 'Arial'
    r2.font.size = Pt(13)
    r2.font.color.rgb = TEXT_MUTED

    add_card(s1, 1.0, 5.4, 11.33, 1.1, title="", border_color=AZURE_BLUE)
    tb_meta = s1.shapes.add_textbox(Inches(1.2), Inches(5.5), Inches(10.9), Inches(0.9))
    tf_meta = tb_meta.text_frame
    p_meta = tf_meta.paragraphs[0]
    r_meta_h = p_meta.add_run()
    r_meta_h.text = "STRATEGIC DECISION MANDATE\n"
    r_meta_h.font.name = 'Arial'
    r_meta_h.font.size = Pt(10)
    r_meta_h.font.bold = True
    r_meta_h.font.color.rgb = ACCENT_GREEN
    r_meta_b = p_meta.add_run()
    r_meta_b.text = "Benchmarking time-to-market, total cost of ownership, variable token economics, and compressing execution from 2 years into 3 months."
    r_meta_b.font.name = 'Arial'
    r_meta_b.font.size = Pt(10)
    r_meta_b.font.color.rgb = TEXT_BODY

    # SLIDE 2: The Crossroads
    s2 = prs.slides.add_slide(blank_layout)
    set_bg(s2)
    add_slide_header(s2, "Executive Crossroads", "The Core Dilemma: Frugal Open-Source vs. High-Velocity Cloud", "Evaluating the foundational trade-offs of speed, operational complexity, and unit economics")
    
    col_w = 5.6
    col_h = 4.8
    top_pos = 1.9
    
    add_card(s2, 0.8, top_pos, col_w, col_h, "Path A: Free Open-Source Sovereign Stack", ACCENT_AMBER)
    tb = s2.shapes.add_textbox(Inches(1.0), Inches(top_pos + 0.65), Inches(col_w - 0.4), Inches(col_h - 0.8))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = "• Core Engine: Ollama / vLLM, Llama 3.3 70B, PostgreSQL pgvector.\n\n• The Promise: $0 software licensing and zero token billing; complete local data sovereignty.\n\n• The Hidden Cost: Heavy MLOps friction, CUDA driver management, high hardware CapEx, slower iteration speed.\n\n• Realistic Timeline: 6 to 12 months of systems engineering before reaching stable multi-user reliability."
    r.font.name = 'Arial'
    r.font.size = Pt(10.5)
    r.font.color.rgb = TEXT_BODY
    
    add_card(s2, 6.9, top_pos, col_w, col_h, "Path B: Enterprise Azure & Frontier Cloud Stack", AZURE_BLUE)
    tb = s2.shapes.add_textbox(Inches(7.1), Inches(top_pos + 0.65), Inches(col_w - 0.4), Inches(col_h - 0.8))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = "• Core Engine: Azure OpenAI (GPT-4o + 4o-mini), Azure AI Search, Container Apps.\n\n• The Promise: World-class reasoning, turnkey hybrid search, instant SOC2/HIPAA compliance, zero infrastructure to manage.\n\n• The Real Cost: Variable per-token API billing and managed cloud subscriptions (~$214/mo pilot, ~$1.50/user/mo token burn).\n\n• Realistic Timeline: 4 to 8 weeks to functional prototype; commercial launch in 90 days."
    r.font.name = 'Arial'
    r.font.size = Pt(10.5)
    r.font.color.rgb = TEXT_BODY

    # SLIDE 3: Azure Enterprise Architecture
    s3 = prs.slides.add_slide(blank_layout)
    set_bg(s3)
    add_slide_header(s3, "Enterprise Blueprint", "Turnkey Azure Cloud Architecture for Karmic AI", "Pre-built managed primitives replacing hundreds of custom infrastructure hours")
    
    grid_w = 3.65
    grid_h = 2.2
    
    az_boxes = [
        ("Cognitive Engine: Azure OpenAI", "• GPT-4o: Complex persona drafting & reasoning\n• GPT-4o-mini: Sub-second triage & tool routing\n• o3-mini: Deep research & constraint solving\n• 99.9% availability SLA, zero data training", AZURE_BLUE, 0.8, 1.9),
        ("Hybrid RAG: Azure AI Search", "• Integrated vector indexing + BM25 keyword\n• Microsoft Bing Semantic Ranker built-in\n• Document Intelligence for OCR & PDFs\n• Basic ($75/mo) to Standard S1 ($250/mo)", ACCENT_GREEN, 4.8, 1.9),
        ("Memory & Data: Managed Postgres", "• Azure Database for PostgreSQL Flexible Server\n• Built-in pgvector extension & automated backups\n• High availability & geo-redundant storage\n• Multi-tenant isolated client schemas", ACCENT_PURPLE, 8.8, 1.9),
        ("Compute: Azure Container Apps", "• Serverless container execution for FastAPI\n• LangGraph multi-agent state machines\n• Automatic scale-to-zero when idle\n• Pay purely for vCPU/RAM seconds", ACCENT_AMBER, 0.8, 4.4),
        ("Security: Entra ID & Key Vault", "• Microsoft Entra ID (Azure AD) enterprise SSO\n• FIPS 140-2 validated Azure Key Vault\n• Private Endpoints & zero public exposure\n• SOC2 Type II, HIPAA, ISO 27001 certified", AZURE_BLUE, 4.8, 4.4),
        ("PaaS & Edge: APIM & CDN", "• Azure API Management (APIM) for B2B APIs\n• Azure Static Web Apps (Next.js dashboard)\n• Azure Cache for Redis (token rate limits)\n• Developer marketplace telemetry", ACCENT_GREEN, 8.8, 4.4)
    ]
    
    for title, desc, col, x, y in az_boxes:
        add_card(s3, x, y, grid_w, grid_h, title, col)
        tb = s3.shapes.add_textbox(Inches(x + 0.15), Inches(y + 0.5), Inches(grid_w - 0.3), Inches(grid_h - 0.6))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        r = p.add_run()
        r.text = desc
        r.font.name = 'Arial'
        r.font.size = Pt(8.5)
        r.font.color.rgb = TEXT_BODY

    # SLIDE 4: Comprehensive Trade-Offs
    s4 = prs.slides.add_slide(blank_layout)
    set_bg(s4)
    add_slide_header(s4, "Comparative Analysis", "Side-by-Side Trade-Off Evaluation", "Direct comparison across key operational, financial, and strategic vectors")
    
    trade_w = 2.8
    trade_h = 4.8
    top_pos = 1.9
    
    cards = [
        ("Time-to-Market", AZURE_BLUE, "FREE STACK:\n6-12 Months (Heavy infra & CUDA tuning)\n\nAZURE ENTERPRISE:\n4-8 Weeks (Turnkey pre-built services)\n\nWINNER: Azure (75% faster launch)"),
        ("Initial CapEx & OpEx", ACCENT_GREEN, "FREE STACK:\n$0 API fees, but requires $3K+ hardware per dev.\n\nAZURE ENTERPRISE:\n$0 CapEx; ~$214/mo for 10-user pilot cohort.\n\nWINNER: Tie (Depends on cash vs. hardware)"),
        ("Reasoning & Nuance", ACCENT_PURPLE, "FREE STACK:\nLlama 3.3 70B is good, but subtle nuances fail.\n\nAZURE ENTERPRISE:\nGPT-4o provides world-leading persona style.\n\nWINNER: Azure (Frontier intelligence)"),
        ("Data Sovereignty", ACCENT_AMBER, "FREE STACK:\n100% cryptographic local zero-leak vault.\n\nAZURE ENTERPRISE:\nContractual enterprise privacy (no training).\n\nWINNER: Free Stack (For paranoid niches)")
    ]
    
    for i, (title, col, desc) in enumerate(cards):
        x_pos = 0.8 + i * 2.95
        add_card(s4, x_pos, top_pos, trade_w, trade_h, title, col)
        tb = s4.shapes.add_textbox(Inches(x_pos + 0.15), Inches(top_pos + 0.65), Inches(trade_w - 0.3), Inches(trade_h - 0.8))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        r = p.add_run()
        r.text = desc
        r.font.name = 'Arial'
        r.font.size = Pt(9.5)
        r.font.color.rgb = TEXT_BODY

    # SLIDE 5: Token Economics Demystified
    s5 = prs.slides.add_slide(blank_layout)
    set_bg(s5)
    add_slide_header(s5, "Token Economics", "Demystifying Token Mechanics in Agentic Systems", "Understanding why agentic systems consume more tokens—and how to optimize them")
    
    col_w = 5.6
    col_h = 4.8
    top_pos = 1.9
    
    add_card(s5, 0.8, top_pos, col_w, col_h, "Why Agents Consume More Tokens", ACCENT_AMBER)
    tb = s5.shapes.add_textbox(Inches(1.0), Inches(top_pos + 0.65), Inches(col_w - 0.4), Inches(col_h - 0.8))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = "• Iterative Evaluation: Unlike simple single-turn chatbots, agents inspect state, call tools, evaluate responses, and loop.\n\n• System Prompts & Tool Definitions: Every call includes schema definitions for MCP tools (email, calendar, search), adding 2,000-4,000 base tokens.\n\n• RAG Context Injection: Top-K retrieved documents, emails, and graph relationships are loaded into the prompt context.\n\n• Nightly Reflection: Ingests the entire day's interaction log to extract lasting epistemic memories."
    r.font.name = 'Arial'
    r.font.size = Pt(10)
    r.font.color.rgb = TEXT_BODY
    
    add_card(s5, 6.9, top_pos, col_w, col_h, "The Secret Weapons of Cost Optimization", ACCENT_GREEN)
    tb = s5.shapes.add_textbox(Inches(7.1), Inches(top_pos + 0.65), Inches(col_w - 0.4), Inches(col_h - 0.8))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = "• Azure Prompt Caching: Static system prompts and tool schemas receive an automatic 50% discount on input tokens on identical prefixes.\n\n• Dynamic Model Tiering: 80% of repetitive calls (triage, classification, entity extraction) are routed to GPT-4o-mini ($0.15/M tokens).\n\n• Selective Frontier Routing: Reserve expensive GPT-4o ($2.50/M) exclusively for persona drafting and final complex reasoning.\n\n• Semantic Caching: Redis caches repeated identical queries before they ever hit the LLM API."
    r.font.name = 'Arial'
    r.font.size = Pt(10)
    r.font.color.rgb = TEXT_BODY

    # SLIDE 6: Daily Workload Token Profile
    s6 = prs.slides.add_slide(blank_layout)
    set_bg(s6)
    add_slide_header(s6, "Workload Modeling", "Daily User Workload Token Profile", "Empirical token consumption for an active knowledge worker across core features")
    
    card_w = 11.73
    card_h = 4.8
    top_pos = 1.9
    
    add_card(s6, 0.8, top_pos, card_w, card_h, "Daily Active User Token Breakdown", AZURE_BLUE)
    tb = s6.shapes.add_textbox(Inches(1.1), Inches(top_pos + 0.65), Inches(card_w - 0.6), Inches(card_h - 0.8))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = "1. Morning Context Briefing (1x/day): 15,000 input tokens | 1,500 output tokens\n" \
             "2. Inbound Email Triage & Filtering (30 emails/day): 45,000 input tokens | 3,000 output tokens\n" \
             "3. Persona-Drafted Email Replies (8 drafts/day): 28,000 input tokens | 4,000 output tokens\n" \
             "4. Autonomous Calendar Negotiation (4 bookings/day): 12,000 input tokens | 1,600 output tokens\n" \
             "5. Private Document Graph RAG Search (5 queries/day): 20,000 input tokens | 3,000 output tokens\n" \
             "6. Nightly Reflective Sleep Consolidation (1x/night): 18,000 input tokens | 1,200 output tokens\n\n" \
             "----------------------------------------------------------------------------------------------------\n" \
             "TOTAL DAILY VOLUME PER USER: ~138,000 Input Tokens | ~14,300 Output Tokens\n" \
             "MONTHLY VOLUME PER USER (30 Days): ~4.1 Million Input Tokens | ~430,000 Output Tokens"
    r.font.name = 'Courier New'
    r.font.size = Pt(9.5)
    r.font.color.rgb = TEXT_BODY

    # SLIDE 7: Monthly Cost Per User Routing Models
    s7 = prs.slides.add_slide(blank_layout)
    set_bg(s7)
    add_slide_header(s7, "Unit Economics", "Monthly AI Inference Cost per User", "Comparing single-model naive routing against smart tiered routing")
    
    col_w = 3.65
    col_h = 4.8
    top_pos = 1.9
    
    add_card(s7, 0.8, top_pos, col_w, col_h, "Strategy 1: Pure GPT-4o (Naive)", ACCENT_AMBER)
    tb = s7.shapes.add_textbox(Inches(1.0), Inches(top_pos + 0.65), Inches(col_w - 0.4), Inches(col_h - 0.8))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = "• Model: 100% GPT-4o\n\n• Monthly Cost: ~$8.50 - $11.20 / user\n\n• Gross Margin: 71% - 78% on $39/mo Pro tier\n\n• Assessment: Works well, but wastes frontier compute on simple spam classification and date parsing."
    r.font.name = 'Arial'
    r.font.size = Pt(10)
    r.font.color.rgb = TEXT_BODY
    
    add_card(s7, 4.8, top_pos, col_w, col_h, "Strategy 2: Smart Tiered Routing", ACCENT_GREEN)
    tb = s7.shapes.add_textbox(Inches(5.0), Inches(top_pos + 0.65), Inches(col_w - 0.4), Inches(col_h - 0.8))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = "• Model: 80% GPT-4o-mini + 20% GPT-4o\n\n• Monthly Cost: ~$1.15 - $1.85 / user\n\n• Gross Margin: 95% - 97% on $39/mo Pro tier\n\n• Assessment: RECOMMENDED. Sub-second speed on routine triage; flawless persona warmth on outward drafts."
    r.font.name = 'Arial'
    r.font.size = Pt(10)
    r.font.color.rgb = TEXT_BODY
    
    add_card(s7, 8.8, top_pos, col_w, col_h, "Strategy 3: Pure GPT-4o-mini", AZURE_BLUE)
    tb = s7.shapes.add_textbox(Inches(9.0), Inches(top_pos + 0.65), Inches(col_w - 0.4), Inches(col_h - 0.8))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = "• Model: 100% GPT-4o-mini\n\n• Monthly Cost: ~$0.45 - $0.65 / user\n\n• Gross Margin: 98%+ on $39/mo Pro tier\n\n• Assessment: Ultra-cheap utility tier, but complex persona nuance and task decomposition suffer."
    r.font.name = 'Arial'
    r.font.size = Pt(10)
    r.font.color.rgb = TEXT_BODY

    # SLIDE 8: Total Cost of Ownership
    s8 = prs.slides.add_slide(blank_layout)
    set_bg(s8)
    add_slide_header(s8, "Total Cost of Ownership", "Azure Monthly Infrastructure Bill Across Cohorts", "Predictable scaling from 10 pilot users to 10,000 commercial subscribers")
    
    col_w = 3.65
    col_h = 4.8
    top_pos = 1.9
    
    add_card(s8, 0.8, top_pos, col_w, col_h, "Pilot Cohort (10 Users)", AZURE_BLUE)
    tb = s8.shapes.add_textbox(Inches(1.0), Inches(top_pos + 0.65), Inches(col_w - 0.4), Inches(col_h - 0.8))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = "• Azure OpenAI (Tiered): $18/mo\n• Azure AI Search (Basic): $75/mo\n• Azure PostgreSQL (B2s): $65/mo\n• Azure Container Apps: $30/mo\n• Redis & Key Vault: $26/mo\n\nTOTAL: $214 / month\n($21.40 / user / month)\n\nZero CapEx barrier to launch!"
    r.font.name = 'Arial'
    r.font.size = Pt(9.5)
    r.font.color.rgb = TEXT_BODY
    
    add_card(s8, 4.8, top_pos, col_w, col_h, "Launch Cohort (1,000 Users)", ACCENT_GREEN)
    tb = s8.shapes.add_textbox(Inches(5.0), Inches(top_pos + 0.65), Inches(col_w - 0.4), Inches(col_h - 0.8))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = "• Azure OpenAI (Tiered): $1,450/mo\n• Azure AI Search (S1): $250/mo\n• Azure PostgreSQL (D2s): $175/mo\n• Azure Container Apps: $180/mo\n• Redis, APIM & Storage: $119/mo\n\nTOTAL: $2,174 / month\nMonthly Revenue: $39,000\nINFRA COST: 5.5% OF REVENUE!"
    r.font.name = 'Arial'
    r.font.size = Pt(9.5)
    r.font.color.rgb = TEXT_BODY
    
    add_card(s8, 8.8, top_pos, col_w, col_h, "Scale Cohort (10,000 Users)", ACCENT_PURPLE)
    tb = s8.shapes.add_textbox(Inches(9.0), Inches(top_pos + 0.65), Inches(col_w - 0.4), Inches(col_h - 0.8))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = "• Azure OpenAI (Tiered): $13,800/mo\n• Azure AI Search (S2/S3): $980/mo\n• Azure PostgreSQL (D8s HA): $580/mo\n• Azure Container Apps: $950/mo\n• Redis, APIM, Storage: $569/mo\n\nTOTAL: $16,879 / month\nMonthly Revenue: $390,000\nINFRA COST: 4.3% OF REVENUE!"
    r.font.name = 'Arial'
    r.font.size = Pt(9.5)
    r.font.color.rgb = TEXT_BODY

    # SLIDE 9: Why 90 Days Instead of 2 Years?
    s9 = prs.slides.add_slide(blank_layout)
    set_bg(s9)
    add_slide_header(s9, "Time Compression", "Why 90 Days Instead of 2 Years?", "How modern managed cloud primitives compress multi-year roadmaps")
    
    col_w = 3.65
    col_h = 4.8
    top_pos = 1.9
    
    add_card(s9, 0.8, top_pos, col_w, col_h, "1. Zero Infra Provisioning", AZURE_BLUE)
    tb = s9.shapes.add_textbox(Inches(1.0), Inches(top_pos + 0.65), Inches(col_w - 0.4), Inches(col_h - 0.8))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = "• In 2023: Building custom CUDA pipelines, server failovers, and Kubernetes clusters took 6-9 months.\n\n• In 2026: Azure Container Apps and Azure AI Studio deploy complete environments in 15 minutes via declarative Bicep scripts."
    r.font.name = 'Arial'
    r.font.size = Pt(10)
    r.font.color.rgb = TEXT_BODY
    
    add_card(s9, 4.8, top_pos, col_w, col_h, "2. Turnkey Hybrid RAG", ACCENT_GREEN)
    tb = s9.shapes.add_textbox(Inches(5.0), Inches(top_pos + 0.65), Inches(col_w - 0.4), Inches(col_h - 0.8))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = "• In 2023: Writing custom cross-encoders, BM25 tokenizers, and vector sync daemons required a full team.\n\n• In 2026: Azure AI Search provides integrated dense vector indexing, BM25, and Bing Semantic Rerankers out-of-the-box."
    r.font.name = 'Arial'
    r.font.size = Pt(10)
    r.font.color.rgb = TEXT_BODY
    
    add_card(s9, 8.8, top_pos, col_w, col_h, "3. Standard Agent Protocols", ACCENT_PURPLE)
    tb = s9.shapes.add_textbox(Inches(9.0), Inches(top_pos + 0.65), Inches(col_w - 0.4), Inches(col_h - 0.8))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = "• In 2023: Developers wrote fragile regex loops to parse tool outputs.\n\n• In 2026: Model Context Protocol (MCP) and LangGraph provide bulletproof state machines and tool schemas instantly."
    r.font.name = 'Arial'
    r.font.size = Pt(10)
    r.font.color.rgb = TEXT_BODY

    # SLIDE 10: 12-Week Master Plan
    s10 = prs.slides.add_slide(blank_layout)
    set_bg(s10)
    add_slide_header(s10, "Execution Plan", "The 12-Week (90-Day) Master Project Plan", "Aggressive, structured sprints leading to commercial revenue generation in 3 months")
    
    card_w = 11.73
    card_h = 1.45
    
    sprints = [
        ("Month 1 (Weeks 1 - 4): Foundation & Internal Pilot", "• Setup Azure OpenAI, AI Search, Container Apps & PostgreSQL\n• Implement MCP Mail & Google Calendar connectors via LangGraph\n• Milestone 1 (Day 30): 10 Internal / Founder Pilot Users active on daily 7:00 AM briefing", AZURE_BLUE, 1.9),
        ("Month 2 (Weeks 5 - 8): Review Queue, B2B Multi-Tenancy & Health", "• Build Human-in-the-Loop approval dashboard & WebSocket streaming\n• Integrate Apple Health/Oura sleep webhook for circadian scheduling\n• Milestone 2 (Day 60): 50 Active Users (D2C beta + 2 corporate pilot teams). NPS > 65", ACCENT_GREEN, 3.5),
        ("Month 3 (Weeks 9 - 12): Commercial Public Launch & PaaS Hub", "• Implement Stripe billing ($29 Pro / $99 Exec) & Azure APIM for B2B APIs\n• Matter/IoT smart home proof-of-concept for office prep\n• Milestone 3 (Day 90): Commercial Launch! 250+ paying users, $10K+ MRR", ACCENT_PURPLE, 5.1)
    ]
    
    for title, desc, col, y in sprints:
        add_card(s10, 0.8, y, card_w, card_h, title, col)
        tb = s10.shapes.add_textbox(Inches(1.0), Inches(y + 0.42), Inches(card_w - 0.4), Inches(card_h - 0.5))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        r = p.add_run()
        r.text = desc
        r.font.name = 'Arial'
        r.font.size = Pt(9.5)
        r.font.color.rgb = TEXT_BODY

    # SLIDE 11: Team Upskilling Roadmap
    s11 = prs.slides.add_slide(blank_layout)
    set_bg(s11)
    add_slide_header(s11, "Team Adoption", "Team Upskilling & Learning Curriculum", "Empowering the engineering squad with the most valuable modern AI engineering skills")
    
    col_w = 2.8
    col_h = 4.8
    top_pos = 1.9
    
    skills = [
        ("1. MCP Mastery", AZURE_BLUE, "• Learn the official open-source Model Context Protocol.\n\n• Separate cognitive reasoning from tool servers.\n\n• Enables 100% portability between Azure and local Ollama."),
        ("2. LangGraph StateGraphs", ACCENT_GREEN, "• Master state machines, checkpoints, and interrupts.\n\n• Build deterministic supervisor-worker topologies.\n\n• Implement strict Human-in-the-Loop review gates."),
        ("3. Prompt Caching", ACCENT_PURPLE, "• Optimize prefix structure for system prompts & schemas.\n\n• Exploit Azure OpenAI automatic 50% discount on cached tokens.\n\n• Enforce strict JSON schema responses."),
        ("4. Azure AI Search", ACCENT_AMBER, "• Configure vector fields & HNSW indexes.\n\n• Integrate BM25 full-text lexical search.\n\n• Enable Bing Semantic Rankers for maximum retrieval accuracy.")
    ]
    
    for i, (title, col, desc) in enumerate(skills):
        x_pos = 0.8 + i * 2.95
        add_card(s11, x_pos, top_pos, col_w, col_h, title, col)
        tb = s11.shapes.add_textbox(Inches(x_pos + 0.15), Inches(top_pos + 0.65), Inches(col_w - 0.3), Inches(col_h - 0.8))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        r = p.add_run()
        r.text = desc
        r.font.name = 'Arial'
        r.font.size = Pt(9.5)
        r.font.color.rgb = TEXT_BODY

    # SLIDE 12: Final Recommendation
    s12 = prs.slides.add_slide(blank_layout)
    set_bg(s12)
    add_slide_header(s12, "Decision Matrix", "Final Strategic Recommendation: The Hybrid Vector", "How Karmic AI captures both speed and sovereignty without compromise")
    
    col_w = 5.6
    col_h = 4.8
    top_pos = 1.9
    
    add_card(s12, 0.8, top_pos, col_w, col_h, "The Winning Playbook", ACCENT_GREEN)
    tb = s12.shapes.add_textbox(Inches(1.0), Inches(top_pos + 0.65), Inches(col_w - 0.4), Inches(col_h - 0.8))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = "1. Launch on Azure Cloud (Month 1-3):\nTake advantage of managed Azure OpenAI, AI Search, and Container Apps to ship in 90 days for ~$214/month in pilot infrastructure.\n\n2. Standardize on Open MCP Protocols:\nWrite all agent skills and memory schemas to open MCP standards so models can be swapped instantly.\n\n3. Introduce Local Edge SLMs at Scale:\nOnce paying user revenue is established, deploy optional on-device Ollama/Llama 3.3 for privacy-purist users."
    r.font.name = 'Arial'
    r.font.size = Pt(10)
    r.font.color.rgb = TEXT_BODY
    
    add_card(s12, 6.9, top_pos, col_w, col_h, "Immediate Next Action Items", AZURE_BLUE)
    tb = s12.shapes.add_textbox(Inches(7.1), Inches(top_pos + 0.65), Inches(col_w - 0.4), Inches(col_h - 0.8))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = "• Step 1: Align Founders & Leadership on Azure Fast-Start Strategy.\n\n• Step 2: Create Azure Subscription & Provision Azure OpenAI (GPT-4o + 4o-mini quota).\n\n• Step 3: Kick off Week 1 Sprint: Scaffolding LangGraph Supervisor and MCP Mail/Calendar tools.\n\n• Step 4: Onboard First 10 Founder Pilot Users on Day 30!\n\n• Let's begin app development with clarity and velocity."
    r.font.name = 'Arial'
    r.font.size = Pt(10)
    r.font.color.rgb = TEXT_BODY

    prs.save(filename)
    print(f"Presentation deck successfully generated: {filename}")

if __name__ == "__main__":
    create_deck()

