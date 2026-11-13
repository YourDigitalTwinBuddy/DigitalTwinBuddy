# -*- coding: utf-8 -*-
"""
api/index.py
Vercel Serverless Entrypoint for Karmic AI Platform (FastAPI)
"""

import sys
from pathlib import Path

# Add project root to Python path for Vercel Serverless execution
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from backend.app.main import app

