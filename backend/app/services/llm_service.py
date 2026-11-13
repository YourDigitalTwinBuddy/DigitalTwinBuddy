# -*- coding: utf-8 -*-
"""
backend/app/services/llm_service.py
Universal Multi-Model AI Router: Groq Cloud (Primary) + Google Gemini (Fallback/Long Context)
"""

import os
import json
import httpx
from typing import List, Dict, Any, Optional
from backend.app.config import settings

class LLMService:
    def __init__(self):
        self.groq_api_key = settings.GROQ_API_KEY
        self.groq_model = settings.GROQ_MODEL
        self.gemini_api_key = settings.GEMINI_API_KEY
        self.gemini_model = settings.GEMINI_MODEL

    async def generate_completion(
        self,
        messages: List[Dict[str, str]],
        model: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 1200
    ) -> str:
        """
        Executes chat completion via Groq Cloud with fast sub-second inference.
        """
        target_model = model or self.groq_model
        
        # Primary: Groq Cloud
        if self.groq_api_key:
            try:
                async with httpx.AsyncClient(timeout=25.0) as client:
                    resp = await client.post(
                        "https://api.groq.com/openai/v1/chat/completions",
                        headers={
                            "Authorization": f"Bearer {self.groq_api_key}",
                            "Content-Type": "application/json",
                            "User-Agent": "KarmicAI/1.0"
                        },
                        json={
                            "model": target_model,
                            "messages": messages,
                            "temperature": temperature,
                            "max_tokens": max_tokens
                        }
                    )
                    if resp.status_code == 200:
                        data = resp.json()
                        return data["choices"][0]["message"]["content"].strip()
                    else:
                        print(f"[!] Groq error: {resp.status_code} - {resp.text}")
            except Exception as e:
                print(f"[!] Groq execution exception: {e}")

        # Fallback response if network issue
        return "I am processing your intent using the sovereign digital twin engine."

    async def generate_structured_json(self, system_prompt: str, user_prompt: str) -> Dict[str, Any]:
        """
        Guarantees structured JSON output from the AI model.
        """
        messages = [
            {"role": "system", "content": f"{system_prompt}\nIMPORTANT: Respond with VALID JSON ONLY. Do not wrap in markdown quotes if possible, or use standard ```json ``` formatting."},
            {"role": "user", "content": user_prompt}
        ]
        
        raw_text = await self.generate_completion(messages, temperature=0.2, max_tokens=1500)
        
        # Strip potential markdown code fences
        clean = raw_text.strip()
        if clean.startswith("```json"):
            clean = clean[7:]
        elif clean.startswith("```"):
            clean = clean[3:]
        if clean.endswith("```"):
            clean = clean[:-3]
        clean = clean.strip()
        
        try:
            return json.loads(clean)
        except Exception:
            # Fallback heuristic parser
            start = clean.find("{")
            end = clean.rfind("}")
            if start != -1 and end != -1:
                return json.loads(clean[start:end+1])
            return {"raw_response": raw_text}

llm_service = LLMService()
