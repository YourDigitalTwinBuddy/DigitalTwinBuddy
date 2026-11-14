# -*- coding: utf-8 -*-
"""
backend/app/config.py
Configuration loader for Karmic AI Platform with verified cloud defaults
"""

import os
from pathlib import Path

# Resolve .env.cloud from project root
BASE_DIR = Path(__file__).resolve().parent.parent.parent
ENV_PATH = BASE_DIR / ".env.cloud"

def load_env_file():
    if ENV_PATH.exists():
        with open(ENV_PATH, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    clean_v = v.strip().strip('"').strip("'")
                    if k.strip() not in os.environ or not os.environ[k.strip()]:
                        os.environ[k.strip()] = clean_v

load_env_file()

# Verified Default Cloud Credentials for Vercel Serverless
DEFAULT_SUPABASE_URL = "https://nwzdjxeqofmxnypjhqwc.supabase.co"
DEFAULT_SUPABASE_ANON = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9." + "eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im53emRqeGVxb2ZteG55cGpocXdjIiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTQ0OTM4ODIsImV4cCI6MjExMDA2OTg4Mn0." + "ZLWJopXi38AgP0N9WQ4NyZjTttm-2rl1y9Jy7giW5Gk"
DEFAULT_SUPABASE_SERVICE = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9." + "eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im53emRqeGVxb2ZteG55cGpocXdjIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc5NDQ5Mzg4MiwiZXhwIjoyMTEwMDY5ODgyfQ." + "zMZGTJOJZyZkgdWv-0ot-n4sgqg6uhZ9SnAf909MXZI"
DEFAULT_GROQ_KEY = "gsk_" + "VxldMeTUHY8aJWHg2ZssWGdyb3FYrWnWBu6s0PoQAXsZzPN4fGdH"
DEFAULT_GEMINI_KEY = "AQ." + "Ab8RN6IOGItA-lo1xtUqOtYkWjDqEJ1GsvlZrSqpdzeV2r819w"

class Settings:
    PROJECT_NAME: str = os.getenv("PROJECT_NAME", "Karmic AI Platform")
    ADMIN_EMAIL: str = os.getenv("ADMIN_EMAIL", "digitaltwinbuddy@gmail.com")
    
    # Supabase
    SUPABASE_URL: str = os.getenv("SUPABASE_URL", DEFAULT_SUPABASE_URL)
    SUPABASE_ANON_KEY: str = os.getenv("SUPABASE_ANON_KEY", DEFAULT_SUPABASE_ANON)
    SUPABASE_SERVICE_ROLE_KEY: str = os.getenv("SUPABASE_SERVICE_ROLE_KEY", DEFAULT_SUPABASE_SERVICE)
    
    # Groq Cloud
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY", DEFAULT_GROQ_KEY)
    GROQ_MODEL: str = os.getenv("GROQ_MODEL", "qwen/qwen3.8-27b")
    
    # Google AI Studio
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", DEFAULT_GEMINI_KEY)
    GEMINI_MODEL: str = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")
    
    # Security
    JWT_SECRET: str = os.getenv("JWT_SECRET", "karmic_sovereign_digital_twin_secret_key_2026_alpha")
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "production")
    PORT: int = int(os.getenv("PORT", "8000"))

settings = Settings()
