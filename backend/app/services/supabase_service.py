# -*- coding: utf-8 -*-
"""
backend/app/services/supabase_service.py
Supabase Cloud Data Layer: Multi-Tenant Data Store, Query & Cache
"""

import httpx
from typing import List, Dict, Any, Optional
from backend.app.config import settings

KNOWN_COLUMNS = {
    "users": {'id', 'email', 'full_name', 'avatar_url', 'tier', 'created_at'},
    "custom_agents": {'id', 'user_id', 'agent_name', 'agent_role', 'icon', 'prompt_instructions', 'trigger_frequency', 'is_active', 'created_at'},
    "pending_actions": {'id', 'user_id', 'agent_name', 'action_type', 'title', 'description', 'impact_preview', 'payload', 'status', 'created_at', 'resolved_at'},
    "storage_items": {'id', 'user_id', 'file_name', 'file_type', 'file_size_mb', 'storage_location', 'thumbnail_url', 'last_accessed_days', 'is_reclaimable', 'status', 'flagged_at'},
    "health_logs": {'id', 'user_id', 'log_date', 'sleep_hours', 'deep_sleep_hours', 'rem_sleep_hours', 'resting_hr', 'hrv_ms', 'steps', 'recovery_score', 'circadian_status', 'recommendations', 'created_at'},
    "digital_twin_profiles": {'id', 'user_id', 'twin_name', 'tone_style', 'vocabulary_rules', 'focus_schedule', 'health_guidelines', 'created_at', 'updated_at'},
    "email_inbox": {'id', 'user_id', 'sender_name', 'sender_email', 'subject', 'snippet', 'category', 'urgency_score', 'is_unsubscribe_candidate', 'unsubscribe_url', 'draft_reply', 'status', 'received_at'},
    "social_digests": {'id', 'user_id', 'digest_date', 'title', 'summary_markdown', 'key_takeaways', 'sources', 'read_time_mins', 'created_at'}
}

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
        # In-memory store fallback for instant testing / offline
        self._memory_cache = {
            "users": [],
            "digital_twin_profiles": [],
            "email_inbox": [],
            "storage_items": [],
            "social_digests": [],
            "health_logs": [],
            "pending_actions": [],
            "custom_agents": []
        }

    async def get_table_data(self, table: str, limit: int = 50) -> List[Dict[str, Any]]:
        """
        Retrieves records from a Supabase table.
        """
        if self.url and self.key:
            try:
                order_param = "&order=created_at.desc" if table in ["users", "social_digests", "custom_agents", "pending_actions"] else ""
                async with httpx.AsyncClient(timeout=10.0) as client:
                    resp = await client.get(
                        f"{self.url}/rest/v1/{table}?select=*{order_param}&limit={limit}",
                        headers=self.headers
                    )
                    if resp.status_code == 200:
                        return resp.json()
            except Exception as e:
                print(f"[!] Supabase read exception on {table}: {e}")
                
        return self._memory_cache.get(table, [])

    async def get_record_by_field(self, table: str, field: str, value: Any) -> Optional[Dict[str, Any]]:
        """
        Retrieves a single record where field == value.
        """
        if self.url and self.key:
            try:
                async with httpx.AsyncClient(timeout=10.0) as client:
                    resp = await client.get(
                        f"{self.url}/rest/v1/{table}?{field}=eq.{value}&select=*&limit=1",
                        headers=self.headers
                    )
                    if resp.status_code == 200:
                        records = resp.json()
                        if records and len(records) > 0:
                            return records[0]
            except Exception as e:
                print(f"[!] Supabase get_record_by_field on {table}: {e}")

        # Fallback to in-memory cache
        for item in self._memory_cache.get(table, []):
            if str(item.get(field)) == str(value):
                return item
        return None

    async def get_records_by_field(self, table: str, field: str, value: Any, limit: int = 50, order_desc: bool = True) -> List[Dict[str, Any]]:
        """
        Retrieves multiple records where field == value.
        """
        if self.url and self.key:
            try:
                order_param = "&order=created_at.desc" if order_desc and table in ["social_digests", "custom_agents", "pending_actions", "health_logs"] else ""
                async with httpx.AsyncClient(timeout=10.0) as client:
                    resp = await client.get(
                        f"{self.url}/rest/v1/{table}?{field}=eq.{value}&select=*{order_param}&limit={limit}",
                        headers=self.headers
                    )
                    if resp.status_code == 200:
                        return resp.json()
            except Exception as e:
                print(f"[!] Supabase get_records_by_field on {table}: {e}")

        # Fallback to in-memory cache
        return [item for item in self._memory_cache.get(table, []) if str(item.get(field)) == str(value)]

    async def insert_record(self, table: str, record: Dict[str, Any]) -> Dict[str, Any]:
        """
        Inserts a single record into Supabase, automatically sanitizing columns.
        """
        clean_record = {k: v for k, v in record.items() if table not in KNOWN_COLUMNS or k in KNOWN_COLUMNS[table]}
        if table == "pending_actions" and "payload" not in clean_record:
            clean_record["payload"] = {}

        if self.url and self.key:
            try:
                async with httpx.AsyncClient(timeout=10.0) as client:
                    resp = await client.post(
                        f"{self.url}/rest/v1/{table}",
                        headers=self.headers,
                        json=clean_record
                    )
                    if resp.status_code in [200, 201]:
                        res = resp.json()
                        return res[0] if isinstance(res, list) and res else clean_record
                    else:
                        print(f"[!] Supabase insert failed ({resp.status_code}): {resp.text}")
            except Exception as e:
                print(f"[!] Supabase insert exception on {table}: {e}")
                
        if table in self._memory_cache:
            self._memory_cache[table].insert(0, clean_record)
        return clean_record

    async def update_record(self, table: str, match_col: str, match_val: Any, update_data: Dict[str, Any]) -> bool:
        """
        Updates a record by column match, automatically sanitizing columns.
        """
        clean_data = {k: v for k, v in update_data.items() if table not in KNOWN_COLUMNS or k in KNOWN_COLUMNS[table]}

        if self.url and self.key:
            try:
                async with httpx.AsyncClient(timeout=10.0) as client:
                    resp = await client.patch(
                        f"{self.url}/rest/v1/{table}?{match_col}=eq.{match_val}",
                        headers=self.headers,
                        json=clean_data
                    )
                    if resp.status_code in [200, 204]:
                        return True
                    else:
                        print(f"[!] Supabase update failed ({resp.status_code}): {resp.text}")
            except Exception as e:
                print(f"[!] Supabase update exception: {e}")
                
        # In-memory update
        if table in self._memory_cache:
            for item in self._memory_cache[table]:
                if str(item.get(match_col)) == str(match_val):
                    item.update(clean_data)
                    return True
        return False

    async def delete_record(self, table: str, match_col: str, match_val: Any) -> bool:
        """
        Deletes a record by column match.
        """
        if self.url and self.key:
            try:
                async with httpx.AsyncClient(timeout=10.0) as client:
                    resp = await client.delete(
                        f"{self.url}/rest/v1/{table}?{match_col}=eq.{match_val}",
                        headers=self.headers
                    )
                    return resp.status_code in [200, 204]
            except Exception as e:
                print(f"[!] Supabase delete exception: {e}")

        if table in self._memory_cache:
            self._memory_cache[table] = [i for i in self._memory_cache[table] if str(i.get(match_col)) != str(match_val)]
            return True
        return False

supabase_service = SupabaseService()


