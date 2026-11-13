# -*- coding: utf-8 -*-
"""
backend/app/agents/email_agent.py
Theme 1A: Autonomous Email Clean-Up, Unsubscribe Optimization & Persona Triage
"""

import uuid
from typing import List, Dict, Any
from backend.app.services.llm_service import llm_service
from backend.app.services.supabase_service import supabase_service

class EmailCleanUpAgent:
    def __init__(self):
        self.agent_name = "Email Clean-Up & Triage Agent"

    async def triage_inbox_item(self, email_data: Dict[str, Any], user_profile: Dict[str, Any]) -> Dict[str, Any]:
        """
        Uses LLM to evaluate an incoming email, assign a category, generate 1-click unsubscribe advice,
        and draft executive-level responses for VIP items.
        """
        system_prompt = f"""You are the Email Clean-Up & Executive Triage Agent for Karmic AI Platform.
The user's persona and tone style is: "{user_profile.get('tone_style', 'Executive, Concise, Professional')}".
Vocabulary rules: "{user_profile.get('vocabulary_rules', 'Direct, polite, zero corporate fluff')}".

Analyze the incoming email and return a JSON object with:
1. "category": One of ["PROMOTIONAL", "COLD_OUTREACH", "TRANSACTIONAL", "VIP_ACTION"]
2. "urgency_score": Integer 1 (lowest) to 5 (highest)
3. "is_unsubscribe_candidate": Boolean (true if marketing, newsletter, or promotional blast)
4. "clean_up_recommendation": String (e.g. "One-click unsubscribe & archive 14 past emails from this sender" or "Stage drafted reply for approval")
5. "draft_reply": String (If VIP_ACTION, provide a complete, polished draft response matching the user's authentic tone. Otherwise null)
6. "rationale": Short explanation of triage choice
"""

        user_prompt = f"""Sender: {email_data.get('sender_name')} <{email_data.get('sender_email')}>
Subject: {email_data.get('subject')}
Body: {email_data.get('snippet')}
"""

        analysis = await llm_service.generate_structured_json(system_prompt, user_prompt)
        
        # Merge with base email record
        result = {
            "id": email_data.get("id", str(uuid.uuid4())),
            "user_id": email_data.get("user_id", "00000000-0000-0000-0000-000000000001"),
            "sender_name": email_data.get("sender_name", "Unknown"),
            "sender_email": email_data.get("sender_email", ""),
            "subject": email_data.get("subject", ""),
            "snippet": email_data.get("snippet", ""),
            "category": analysis.get("category", "PROMOTIONAL"),
            "urgency_score": analysis.get("urgency_score", 1),
            "is_unsubscribe_candidate": analysis.get("is_unsubscribe_candidate", False),
            "clean_up_recommendation": analysis.get("clean_up_recommendation", "Archive"),
            "draft_reply": analysis.get("draft_reply"),
            "status": "DRAFT_STAGED" if analysis.get("draft_reply") else "CLEANED"
        }
        
        # If VIP draft created, automatically stage in Human-in-the-Loop Pending Action queue!
        if result["draft_reply"]:
            await supabase_service.insert_record("pending_actions", {
                "id": str(uuid.uuid4()),
                "user_id": result["user_id"],
                "agent_name": self.agent_name,
                "action_type": "SEND_EMAIL",
                "title": f"Approve Reply to: {result['sender_name']}",
                "description": f"Subject: Re: {result['subject']}",
                "impact_preview": result["draft_reply"],
                "payload": {"recipient": result["sender_email"], "draft": result["draft_reply"]},
                "status": "PENDING"
            })
            
        return result

    async def get_demo_inbox(self) -> List[Dict[str, Any]]:
        """
        Returns rich sample emails demonstrating all 4 triage categories and clean-up recommendations.
        """
        return [
            {
                "id": "em-001",
                "sender_name": "Satya Nadella (Partner Executive)",
                "sender_email": "satya@partner-network.com",
                "subject": "Strategic Cloud Partnership: Q4 Roadmap Alignment",
                "snippet": "Hi Navin, enjoyed our previous discussion on the Sovereign Digital Twin. Can your team share the latest architecture deck for the Q4 review before Thursday? Best, Satya.",
                "category": "VIP_ACTION",
                "urgency_score": 5,
                "is_unsubscribe_candidate": False,
                "clean_up_recommendation": "Priority VIP message. Stage voice-matched draft reply.",
                "draft_reply": "Hi Satya, thanks for reaching out. Delighted to hear from you. The updated Karmic architecture deck and technical specifications are prepared and attached for our Thursday alignment. Looking forward to reviewing together. Warm regards, Navin.",
                "status": "DRAFT_STAGED"
            },
            {
                "id": "em-002",
                "sender_name": "SaaS Digest Weekly",
                "sender_email": "newsletter@saasweeklyblast.io",
                "subject": "Top 100 AI Cloud Tool Trends You Must Know in 2026",
                "snippet": "Don't miss our latest sponsored webinar featuring cloud benchmarks, tool ratings, and SaaS pricing breakdowns...",
                "category": "PROMOTIONAL",
                "urgency_score": 1,
                "is_unsubscribe_candidate": True,
                "clean_up_recommendation": "Unopened for 60+ days. Recommend 1-click unsubscribe and archive 24 related emails.",
                "draft_reply": None,
                "status": "CLEANED"
            },
            {
                "id": "em-003",
                "sender_name": "Growth B2B Cold Outreach",
                "sender_email": "jake@coldoutreachleadgen.co",
                "subject": "Quick question regarding your lead pipeline?",
                "snippet": "Hey there! I saw you're building Karmic AI. We can get you 50 qualified B2B demos a month guaranteed with our automated scraper...",
                "category": "COLD_OUTREACH",
                "urgency_score": 1,
                "is_unsubscribe_candidate": True,
                "clean_up_recommendation": "Automated cold solicitation detected. Deflect to spam/archive.",
                "draft_reply": None,
                "status": "CLEANED"
            },
            {
                "id": "em-004",
                "sender_name": "Stripe Billing Notifications",
                "sender_email": "notifications@stripe.com",
                "subject": "Invoice Paid: Cloud Hosting Service #INV-2026-8812",
                "snippet": "Your payment of $19.00 USD for the serverless container service has succeeded. Retain this invoice for tax records.",
                "category": "TRANSACTIONAL",
                "urgency_score": 2,
                "is_unsubscribe_candidate": False,
                "clean_up_recommendation": "Expense receipt recorded into financial ledger; automatically filed into 'Receipts'.",
                "draft_reply": None,
                "status": "CLEANED"
            }
        ]

email_agent = EmailCleanUpAgent()

