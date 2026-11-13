# -*- coding: utf-8 -*-
"""
backend/app/agents/health_agent.py
Theme 2: Health & Fitness Digital Twin: Biometrics, Circadian Rhythm & Longevity Protocols
"""

import uuid
from datetime import datetime
from typing import Dict, Any, List
from backend.app.services.llm_service import llm_service
from backend.app.services.supabase_service import supabase_service

class HealthFitnessAgent:
    def __init__(self):
        self.agent_name = "Health & Longevity Digital Twin"

    async def evaluate_daily_biometrics(self, user_id: str, telemetry: Dict[str, Any]) -> Dict[str, Any]:
        """
        Processes sleep architecture, HRV, steps, and resting heart rate.
        Calculates a Readiness Score and recommends circadian calendar adjustments.
        """
        sleep_hours = telemetry.get("sleep_hours", 7.2)
        deep_sleep = telemetry.get("deep_sleep_hours", 1.4)
        rem_sleep = telemetry.get("rem_sleep_hours", 1.6)
        hrv = telemetry.get("hrv_ms", 62)
        rhr = telemetry.get("resting_hr", 59)
        steps = telemetry.get("steps", 9200)

        # Baseline readiness algorithm
        base_score = int(min(100, (sleep_hours / 8.0) * 40 + (hrv / 70.0) * 35 + (deep_sleep / 1.8) * 25))
        circadian_status = "OPTIMAL" if base_score >= 80 else ("MODERATE_FATIGUE" if base_score >= 65 else "DEPRESSED_RECOVERY")

        system_prompt = """You are the Health & Longevity Digital Twin for Karmic AI Platform.
Analyze the user's daily physiological telemetry and generate personalized bio-routine protocols.
Connect their biological readiness to their work calendar.

Return a JSON with:
1. "recovery_score": Integer (calculated score or calibrated)
2. "circadian_status": String ("OPTIMAL", "MODERATE_FATIGUE", "DEPRESSED_RECOVERY")
3. "calendar_recommendation": Concrete schedule adjustment (e.g. "Insert 45-min afternoon recovery buffer at 14:00" or "Optimal for high-cognitive board deck drafting")
4. "workout_recommendation": Tailored physical strain guidance (e.g. "Low-impact 30-min Zone-2 walk; avoid heavy CNS deadlifts today")
5. "longevity_tips": List of 2-3 specific behavioral interventions (hydration, sunlight timing, caffeine cutoff)
"""

        user_prompt = f"""Telemetry Metrics:
- Total Sleep: {sleep_hours} hrs (Deep: {deep_sleep} hrs, REM: {rem_sleep} hrs)
- Heart Rate Variability (HRV): {hrv} ms
- Resting Heart Rate: {rhr} bpm
- Daily Steps: {steps}
- Baseline Score: {base_score}/100
"""

        analysis = await llm_service.generate_structured_json(system_prompt, user_prompt)
        
        health_record = {
            "id": str(uuid.uuid4()),
            "user_id": user_id,
            "log_date": datetime.now().strftime("%Y-%m-%d"),
            "sleep_hours": sleep_hours,
            "deep_sleep_hours": deep_sleep,
            "rem_sleep_hours": rem_sleep,
            "resting_hr": rhr,
            "hrv_ms": hrv,
            "steps": steps,
            "recovery_score": analysis.get("recovery_score", base_score),
            "circadian_status": analysis.get("circadian_status", circadian_status),
            "calendar_recommendation": analysis.get("calendar_recommendation", "Protect afternoon focus blocks."),
            "workout_recommendation": analysis.get("workout_recommendation", "Zone 2 aerobic recovery protocol."),
            "longevity_tips": analysis.get("longevity_tips", ["Hydrate with 500ml water upon waking", "Caffeine cutoff at 14:00"]),
            "created_at": datetime.utcnow().isoformat()
        }

        # If recovery is depressed, automatically stage a calendar protection block in pending_actions!
        if health_record["recovery_score"] < 75:
            await supabase_service.insert_record("pending_actions", {
                "id": str(uuid.uuid4()),
                "user_id": user_id,
                "agent_name": self.agent_name,
                "action_type": "RESCHEDULE_CALENDAR",
                "title": "Protect Calendar: Insert 45-Min Recovery Pause",
                "description": f"Health Readiness is {health_record['recovery_score']}/100. Reschedule 15:00 non-critical sync and insert cognitive rest buffer.",
                "impact_preview": "Prevents afternoon cognitive burnout and preserves executive stamina.",
                "payload": {"slot": "15:00 - 15:45", "action": "INSERT_FOCUS_BUFFER"},
                "status": "PENDING"
            })

        await supabase_service.insert_record("health_logs", health_record)
        return health_record

health_agent = HealthFitnessAgent()
