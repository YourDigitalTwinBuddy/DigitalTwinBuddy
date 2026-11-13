-- =================================================================
-- KARMIC AI PLATFORM: SUPABASE PRODUCTION DATABASE SCHEMA
-- Multi-Tenant SaaS & PaaS Architecture with pgvector & HITL Queue
-- =================================================================

-- 1. Enable Core Extensions
CREATE EXTENSION IF NOT EXISTS vector;
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- 2. Users Table (Tenant Identity)
CREATE TABLE IF NOT EXISTS public.users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    email VARCHAR(255) UNIQUE NOT NULL,
    full_name VARCHAR(255) NOT NULL,
    avatar_url TEXT,
    tier VARCHAR(50) DEFAULT 'pro', -- 'free', 'pro', 'executive'
    created_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc'::text, now()) NOT NULL
);

-- 3. Digital Twin Persona Profiles
CREATE TABLE IF NOT EXISTS public.digital_twin_profiles (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES public.users(id) ON DELETE CASCADE UNIQUE,
    twin_name VARCHAR(100) DEFAULT 'My Digital Twin',
    tone_style VARCHAR(100) DEFAULT 'Executive, Concise & Warm',
    vocabulary_rules TEXT DEFAULT 'Avoid corporate jargon; use direct, cordial sentences.',
    focus_schedule JSONB DEFAULT '{"no_morning_meetings_before": "11:00", "focus_blocks": ["14:00-16:00"]}'::jsonb,
    health_guidelines JSONB DEFAULT '{"target_sleep_hours": 8, "min_hrv_target": 65, "step_goal": 10000}'::jsonb,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc'::text, now()) NOT NULL,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc'::text, now()) NOT NULL
);

-- 4. Theme 1A: Email Clean-Up & Triage Table
CREATE TABLE IF NOT EXISTS public.email_inbox (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES public.users(id) ON DELETE CASCADE,
    sender_name VARCHAR(255) NOT NULL,
    sender_email VARCHAR(255) NOT NULL,
    subject TEXT NOT NULL,
    snippet TEXT,
    category VARCHAR(50) NOT NULL, -- 'PROMOTIONAL', 'COLD_OUTREACH', 'TRANSACTIONAL', 'VIP_ACTION'
    urgency_score INT DEFAULT 1, -- 1 to 5
    is_unsubscribe_candidate BOOLEAN DEFAULT FALSE,
    unsubscribe_url TEXT,
    draft_reply TEXT,
    status VARCHAR(50) DEFAULT 'UNREAD', -- 'UNREAD', 'CLEANED', 'ARCHIVED', 'DRAFT_STAGED'
    received_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc'::text, now()) NOT NULL
);

-- 5. Theme 1B: Mobile Storage Bloat Ledger (iOS / Android)
CREATE TABLE IF NOT EXISTS public.storage_items (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES public.users(id) ON DELETE CASCADE,
    file_name VARCHAR(255) NOT NULL,
    file_type VARCHAR(50) NOT NULL, -- 'DUPLICATE_PHOTO', 'LARGE_VIDEO', 'CHAT_DUMP', 'STALE_DOWNLOAD'
    file_size_mb FLOAT NOT NULL,
    storage_location VARCHAR(100) DEFAULT 'Cloud Drive / Photos',
    thumbnail_url TEXT,
    last_accessed_days INT DEFAULT 0,
    is_reclaimable BOOLEAN DEFAULT TRUE,
    status VARCHAR(50) DEFAULT 'FLAGGED', -- 'FLAGGED', 'APPROVED_DELETE', 'SAVED_ARCHIVE'
    flagged_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc'::text, now()) NOT NULL
);

-- 6. Theme 1C: Social Media & Newsletter Executive Digests
CREATE TABLE IF NOT EXISTS public.social_digests (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES public.users(id) ON DELETE CASCADE,
    digest_date DATE DEFAULT CURRENT_DATE,
    title VARCHAR(255) NOT NULL,
    summary_markdown TEXT NOT NULL,
    key_takeaways JSONB DEFAULT '[]'::jsonb,
    sources JSONB DEFAULT '[]'::jsonb,
    read_time_mins INT DEFAULT 3,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc'::text, now()) NOT NULL
);

-- 7. Theme 2: Health & Fitness Biometric Telemetry
CREATE TABLE IF NOT EXISTS public.health_logs (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES public.users(id) ON DELETE CASCADE,
    log_date DATE DEFAULT CURRENT_DATE NOT NULL,
    sleep_hours FLOAT DEFAULT 7.5,
    deep_sleep_hours FLOAT DEFAULT 1.5,
    rem_sleep_hours FLOAT DEFAULT 1.8,
    resting_hr INT DEFAULT 58,
    hrv_ms INT DEFAULT 68,
    steps INT DEFAULT 8500,
    recovery_score INT DEFAULT 85, -- 0 to 100
    circadian_status VARCHAR(50) DEFAULT 'OPTIMAL', -- 'OPTIMAL', 'DEPRESSED_RECOVERY', 'FATIGUE_ALERT'
    recommendations JSONB DEFAULT '[]'::jsonb,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc'::text, now()) NOT NULL,
    UNIQUE(user_id, log_date)
);

-- 8. PaaS Custom Agent & Scenario Registry
CREATE TABLE IF NOT EXISTS public.custom_agents (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES public.users(id) ON DELETE CASCADE,
    agent_name VARCHAR(100) NOT NULL,
    agent_role VARCHAR(100) NOT NULL,
    icon VARCHAR(50) DEFAULT 'Bot',
    prompt_instructions TEXT NOT NULL,
    trigger_frequency VARCHAR(50) DEFAULT 'DAILY_MORNING', -- 'REALTIME', 'HOURLY', 'DAILY_MORNING', 'ON_DEMAND'
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc'::text, now()) NOT NULL
);

-- 9. Human-in-the-Loop (HITL) Action Approval Queue
CREATE TABLE IF NOT EXISTS public.pending_actions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES public.users(id) ON DELETE CASCADE,
    agent_name VARCHAR(100) NOT NULL,
    action_type VARCHAR(100) NOT NULL, -- 'SEND_EMAIL', 'DELETE_STORAGE', 'RESCHEDULE_CALENDAR', 'UNSUBSCRIBE'
    title VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    impact_preview TEXT,
    payload JSONB NOT NULL,
    status VARCHAR(50) DEFAULT 'PENDING', -- 'PENDING', 'APPROVED', 'REJECTED', 'EXECUTED'
    created_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc'::text, now()) NOT NULL,
    resolved_at TIMESTAMP WITH TIME ZONE
);

-- 10. Epistemic Vector Memory (pgvector HNSW Index)
CREATE TABLE IF NOT EXISTS public.episodic_memory (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES public.users(id) ON DELETE CASCADE,
    content TEXT NOT NULL,
    metadata JSONB DEFAULT '{}'::jsonb,
    source_type VARCHAR(50) NOT NULL,
    embedding vector(768),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc'::text, now()) NOT NULL
);

-- Create HNSW Vector Index if memory table populated
CREATE INDEX IF NOT EXISTS idx_episodic_memory_embedding 
ON public.episodic_memory 
USING hnsw (embedding vector_cosine_ops)
WITH (m = 16, ef_construction = 64);

-- 11. Seed Default Demo User for Instant Out-of-the-Box Experience
INSERT INTO public.users (id, email, full_name, avatar_url, tier)
VALUES (
    '00000000-0000-0000-0000-000000000001',
    'digitaltwinbuddy@gmail.com',
    'Navin (Digital Twin Buddy)',
    'https://api.dicebear.com/7.x/bottts/svg?seed=karmic',
    'executive'
) ON CONFLICT (email) DO NOTHING;

INSERT INTO public.digital_twin_profiles (user_id, twin_name, tone_style, vocabulary_rules)
VALUES (
    '00000000-0000-0000-0000-000000000001',
    'Karmic Chief-of-Staff',
    'Executive, Strategic & Empathetic',
    'Keep communications concise, professional, and action-oriented.'
) ON CONFLICT (user_id) DO NOTHING;

