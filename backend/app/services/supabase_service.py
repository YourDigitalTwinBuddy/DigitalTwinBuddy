# -*- coding: utf-8 -*-
"""
backend/app/services/supabase_service.py
Supabase Cloud Data Layer: Multi-Tenant Data Store & Cache
"""

import httpx
from typing import List, Dict, Any, Optional
from backend.app.config import settings

class SupabaseService:
    def __init__(self):
        self.url = settings.SUPABASE_URL.rstrip("/")
        self.key = settings.SUPABASE_SERVICE_ROLE_KEY or settings.SUPABASE_ANON_KEY
        self.headers = {
            "apikey": self.key,
            "Authorization": f"Bearer {self.key}",
            "Content-Type": "application/json",
            "Prefer": "return=representation",
            "User-Agent": "KarmicAI/1.0"
        }
        # In-memory store fallback for instant testing
        self._memory_cache = {
            "emails": [],
            "storage": [],
            "digests": [],
            "health": [],
            "actions": [],
            "custom_agents": []
        }

    async def get_table_data(self, table: str, limit: int = 50) -> List[Dict[str, Any]]:
        """
        Retrieves records from a Supabase table, with fallback to in-memory store.
        """
        if self.url and self.key:
            try:
                async with httpx.AsyncClient(timeout=10.0) as client:
                    resp = await client.get(
                        f"{self.url}/rest/v1/{table}?select=*&limit={limit}&order=created_at.desc" if "created_at" in ["users", "social_digests", "custom_agents", "pending_actions"] else f"{self.url}/rest/v1/{table}?select=*&limit={limit}",
                        headers=self.headers
                    )
                    if resp.status_code == 200:
                        records = resp.json()
                        if records:
                            return records
            except Exception as e:
                print(f"[!] Supabase read exception on {table}: {e}")
                
        return self._memory_cache.get(table, [])

    async def insert_record(self, table: str, record: Dict[str, Any]) -> Dict[str, Any]:
        """
        Inserts a single record into Supabase.
        """
        if self.url and self.key:
            try:
                async with httpx.AsyncClient(timeout=10.0) as client:
                    resp = await client.post(
                        f"{self.url}/rest/v1/{table}",
                        headers=self.headers,
                        json=record
                    )
                    if resp.status_code in [200, 201]:
                        res = resp.json()
                        return res[0] if isinstance(res, list) and res else record
            except Exception as e:
                print(f"[!] Supabase insert exception on {table}: {e}")
                
        if table in self._memory_cache:
            self._memory_cache[table].insert(0, record)
        return record

    async def update_record(self, table: str, match_col: str, match_val: Any, update_data: Dict[str, Any]) -> bool:
        """
        Updates a record by column match.
        """
        if self.url and self.key:
            try:
                async with httpx.AsyncClient(timeout=10.0) as client:
                    resp = await client.patch(
                        f"{self.url}/rest/v1/{table}?{match_col}=eq.{match_val}",
                        headers=self.headers,
                        json=update_data
                    )
                    if resp.status_code in [200, 204]:
                        return True
            except Exception as e:
                print(f"[!] Supabase update exception: {e}")
                
        # In-memory update
        if table in self._memory_cache:
            for item in self._memory_cache[table]:
                if item.get(match_col) == match_val:
                    item.update(update_data)
                    return True
        return False

supabase_service = SupabaseService()
