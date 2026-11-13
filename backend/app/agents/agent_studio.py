# -*- coding: utf-8 -*-
"""
backend/app/agents/agent_studio.py
PaaS Custom Agent & Scenario Builder: Extensible Multi-Agent Creation Engine
"""

import uuid
from typing import List, Dict, Any
from backend.app.services.llm_service import llm_service
from backend.app.services.supabase_service import supabase_service

class AgentStudio:
    def __init__(self):
        self._default_agents = [
            {
                "id": "agent-001",
                "agent_name": "Executive Inbox Guardian",
                "agent_role": "Email Clean-up & VIP Reply Drafting",
                "icon": "Mail",
                "trigger_frequency": "REALTIME",
                "is_active": True,
                "prompt_instructions": "Monitor inbound mail, flag cold sales, auto-archive spam, and draft replies in Navin's authentic voice."
            },
            {
                "id": "agent-002",
                "agent_name": "Mobile Storage Cleaner",
                "agent_role": "iOS & Android Cloud Storage Optimizer",
                "icon": "HardDrive",
                "trigger_frequency": "WEEKLY",
                "is_active": True,
                "prompt_instructions": "Analyze camera roll duplicate photos and WhatsApp media dumps. Reclaim gigabytes of cloud storage."
            },
            {
                "id": "agent-003",
                "agent_name": "3-Min Executive Digest Scout",
                "agent_role": "Social Media & Newsletter Synthesizer",
                "icon": "Newspaper",
                "trigger_frequency": "DAILY_MORNING",
                "is_active": True,
                "prompt_instructions": "Synthesize 30+ tech newsletters and X/Twitter bookmarks into a concise 3-minute executive read at 07:00 AM."
            },
            {
                "id": "agent-004",
                "agent_name": "Circadian Longevity Twin",
                "agent_role": "Biometrics, Sleep Recovery & Calendar Protection",
                "icon": "Activity",
                "trigger_frequency": "DAILY_MORNING",
                "is_active": True,
                "prompt_instructions": "Ingest sleep architecture and HRV. Protect work calendar when recovery is depressed and prescribe longevity protocols."
            }
        ]

    async def list_agents(self, user_id: str) -> List[Dict[str, Any]]:
        db_agents = await supabase_service.get_table_data("custom_agents")
        if db_agents:
            return db_agents
        return self._default_agents

    async def create_agent(self, user_id: str, agent_data: Dict[str, Any]) -> Dict[str, Any]:
        record = {
            "id": str(uuid.uuid4()),
            "user_id": user_id,
            "agent_name": agent_data.get("agent_name", "Custom Task Agent"),
            "agent_role": agent_data.get("agent_role", "Task Assistant"),
            "icon": agent_data.get("icon", "Cpu"),
            "trigger_frequency": agent_data.get("trigger_frequency", "DAILY_MORNING"),
            "is_active": True,
            "prompt_instructions": agent_data.get("prompt_instructions", "Assist user with specialized workflows.")
        }
        await supabase_service.insert_record("custom_agents", record)
        return record

    async def run_scenario(self, user_id: str, agent_id: str, scenario_input: str) -> Dict[str, Any]:
        """
        Executes an agent against a custom user scenario or ad-hoc request.
        """
        system_prompt = "You are a specialized autonomous agent deployed on the Karmic AI Platform. Execute the user's scenario with precision, deterministic logic, and clear output."
        response = await llm_service.generate_completion(
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Scenario Input: {scenario_input}"}
            ]
        )
        return {"agent_id": agent_id, "status": "COMPLETED", "result": response}

agent_studio = AgentStudio()

