# -*- coding: utf-8 -*-
"""
backend/app/config.py
Configuration loader for Karmic AI Platform using .env.cloud
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

class Settings:
    PROJECT_NAME: str = os.getenv("PROJECT_NAME", "Karmic AI Platform")
    ADMIN_EMAIL: str = os.getenv("ADMIN_EMAIL", "digitaltwinbuddy@gmail.com")
    
    # Supabase
    SUPABASE_URL: str = os.getenv("SUPABASE_URL", "https://nwzdjxeqofmxnypjhqwc.supabase.co")
    SUPABASE_ANON_KEY: str = os.getenv("SUPABASE_ANON_KEY", "")
    SUPABASE_SERVICE_ROLE_KEY: str = os.getenv("SUPABASE_SERVICE_ROLE_KEY", "")
    
    # Groq Cloud
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY", "")
    GROQ_MODEL: str = os.getenv("GROQ_MODEL", "qwen/qwen3.8-27b")
    
    # Google AI Studio
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
    GEMINI_MODEL: str = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")
    
    # Security
    JWT_SECRET: str = os.getenv("JWT_SECRET", "karmic_secret_key_alpha_2026")
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    PORT: int = int(os.getenv("PORT", "8000"))

settings = Settings()
