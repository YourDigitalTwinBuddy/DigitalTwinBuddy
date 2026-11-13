# -*- coding: utf-8 -*-
"""
backend/app/agents/storage_agent.py
Theme 1B: Mobile & Cloud Storage Bloat Management (iOS / Android Assistant)
"""

import uuid
from typing import List, Dict, Any
from backend.app.services.supabase_service import supabase_service

class MobileStorageAgent:
    def __init__(self):
        self.agent_name = "Mobile Storage Optimization Agent"

    async def analyze_storage_bloat(self, user_id: str) -> Dict[str, Any]:
        """
        Analyzes storage items across mobile photos, cloud drives, and chat caches.
        Returns a structured cleanup plan and statistics.
        """
        items = await self.get_sample_storage_items(user_id)
        
        total_bloat_mb = sum(item["file_size_mb"] for item in items if item.get("is_reclaimable"))
        duplicate_count = sum(1 for item in items if item["file_type"] == "DUPLICATE_PHOTO")
        large_video_count = sum(1 for item in items if item["file_type"] == "LARGE_VIDEO")
        chat_dump_count = sum(1 for item in items if item["file_type"] == "CHAT_DUMP")
        
        # Build 1-click clean-up recipe
        cleanup_recipe = {
            "total_reclaimable_gb": round(total_bloat_mb / 1024, 2),
            "reclaimable_mb": round(total_bloat_mb, 1),
            "duplicate_photos": duplicate_count,
            "large_stale_videos": large_video_count,
            "chat_media_dumps": chat_dump_count,
            "items": items
        }
        
        # Stage a batch action in pending_actions
        await supabase_service.insert_record("pending_actions", {
            "id": "action-storage-reclaim-001",
            "user_id": user_id,
            "agent_name": self.agent_name,
            "action_type": "DELETE_STORAGE",
            "title": f"Reclaim {cleanup_recipe['total_reclaimable_gb']} GB of Storage",
            "description": f"Purge {duplicate_count} burst duplicate photos, {large_video_count} unwatched large video archives, and {chat_dump_count} chat media dumps.",
            "impact_preview": f"Will free up {cleanup_recipe['total_reclaimable_gb']} GB on your iPhone/Android cloud vault immediately.",
            "payload": {"item_ids": [i["id"] for i in items if i["is_reclaimable"]]},
            "status": "PENDING"
        })
        
        return cleanup_recipe

    async def get_sample_storage_items(self, user_id: str) -> List[Dict[str, Any]]:
        return [
            {
                "id": "st-001",
                "user_id": user_id,
                "file_name": "IMG_9824_Burst_Photo_Copy_1.HEIC",
                "file_type": "DUPLICATE_PHOTO",
                "file_size_mb": 14.2,
                "storage_location": "iCloud Photos / Camera Roll",
                "last_accessed_days": 180,
                "is_reclaimable": True,
                "recommendation": "Exact burst duplicate. Keep original IMG_9824.HEIC and delete this copy."
            },
            {
                "id": "st-002",
                "user_id": user_id,
                "file_name": "IMG_9825_Burst_Photo_Copy_2.HEIC",
                "file_type": "DUPLICATE_PHOTO",
                "file_size_mb": 14.8,
                "storage_location": "iCloud Photos / Camera Roll",
                "last_accessed_days": 180,
                "is_reclaimable": True,
                "recommendation": "Exact burst duplicate. Keep original IMG_9824.HEIC."
            },
            {
                "id": "st-003",
                "user_id": user_id,
                "file_name": "4K_Conference_Keynote_Recording_Raw.MOV",
                "file_type": "LARGE_VIDEO",
                "file_size_mb": 3480.0, # ~3.4 GB
                "storage_location": "Internal Storage / Videos",
                "last_accessed_days": 320,
                "is_reclaimable": True,
                "recommendation": "Not opened in 320 days. Move to cold archive or delete local cache."
            },
            {
                "id": "st-004",
                "user_id": user_id,
                "file_name": "WhatsApp_Forwarded_Media_Batch_Nov.zip",
                "file_type": "CHAT_DUMP",
                "file_size_mb": 860.5,
                "storage_location": "WhatsApp Media / Video Cache",
                "last_accessed_days": 90,
                "is_reclaimable": True,
                "recommendation": "Group chat forwarded video clips and memes. Safe to purge."
            },
            {
                "id": "st-005",
                "user_id": user_id,
                "file_name": "Android_SDK_Old_Setup_v24.zip",
                "file_type": "STALE_DOWNLOAD",
                "file_size_mb": 512.0,
                "storage_location": "Downloads Folder",
                "last_accessed_days": 210,
                "is_reclaimable": True,
                "recommendation": "Outdated installer file. Zero dependency on phone/laptop."
            }
        ]

storage_agent = MobileStorageAgent()

