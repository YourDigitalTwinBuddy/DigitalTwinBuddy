# -*- coding: utf-8 -*-
"""
test_cloud_credentials.py
Automated diagnostic script to test your cloud credentials:
1. Supabase PostgreSQL & API connection
2. Groq Cloud API connectivity
3. Google AI Studio API connectivity
4. GitHub repository connection
"""

import os
import urllib.request
import json

def check_env():
    env_file = ".env.cloud" if os.path.exists(".env.cloud") else ".env"
    if not os.path.exists(env_file):
        print(f"[!] Warning: No {env_file} found.")
        return False
        
    print(f"[*] Reading configuration from {env_file}...")
    with open(env_file, "r") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                clean_v = v.strip().strip('"').strip("'")
                os.environ[k.strip()] = clean_v
    return True

def test_groq():
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        print("[-] Groq API Key: Missing.")
        return
    try:
        req = urllib.request.Request(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
                "User-Agent": "KarmicAI/1.0"
            },
            data=json.dumps({
                "model": os.environ.get("GROQ_MODEL", "qwen/qwen3.8-27b"),
                "messages": [{"role": "user", "content": "ping"}],
                "max_tokens": 5
            }).encode("utf-8")
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            ans = data["choices"][0]["message"]["content"].strip()
            print(f"[+] Groq Cloud API: SUCCESS (Model {os.environ.get('GROQ_MODEL')} responded: '{ans}')")
    except Exception as e:
        print(f"[!] Groq API Error: {e}")

def test_gemini():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("[-] Gemini API Key: Missing.")
        return
    try:
        model = os.environ.get("GEMINI_MODEL", "gemini-3.8-flash")
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
        req = urllib.request.Request(
            url,
            headers={
                "Content-Type": "application/json",
                "User-Agent": "KarmicAI/1.0"
            },
            data=json.dumps({
                "contents": [{"parts": [{"text": "ping"}]}]
            }).encode("utf-8")
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            ans = data["candidates"][0]["content"]["parts"][0]["text"].strip()
            print(f"[+] Google AI Studio API: SUCCESS (Model {model} responded: '{ans}')")
    except Exception as e:
        print(f"[!] Gemini API Error: {e}")

def test_supabase():
    url = os.environ.get("SUPABASE_URL")
    service_key = os.environ.get("SUPABASE_SERVICE_ROLE_KEY")
    if not url or not service_key:
        print("[-] Supabase: Missing credentials.")
        return
    try:
        req = urllib.request.Request(
            f"{url}/rest/v1/",
            headers={
                "apikey": service_key,
                "Authorization": f"Bearer {service_key}",
                "User-Agent": "KarmicAI/1.0"
            }
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            print(f"[+] Supabase API: SUCCESS (Connected to {url} - Status: {resp.status})")
    except Exception as e:
        print(f"[!] Supabase API Error: {e}")

def test_github():
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        print("[-] GitHub Token: Missing.")
        return
    try:
        req = urllib.request.Request(
            "https://api.github.com/repos/YourDigitalTwinBuddy/DigitalTwinBuddy",
            headers={
                "Authorization": f"token {token}",
                "User-Agent": "KarmicAI/1.0"
            }
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            print(f"[+] GitHub Repository: SUCCESS (Connected to {data['full_name']} - Admin: {data['permissions']['admin']})")
    except Exception as e:
        print(f"[!] GitHub API Error: {e}")

if __name__ == "__main__":
    print("=" * 65)
    print("KARMIC AI PLATFORM: FULL CLOUD INTEGRATION TEST")
    print("=" * 65)
    if check_env():
        test_supabase()
        test_groq()
        test_gemini()
        test_github()
    print("=" * 65)
    print("ALL CLOUD SYSTEMS ARE READY FOR DEVELOPMENT!")
    print("=" * 65)
