-- Karmic AI Platform: Database Initialization Script
-- Enables pgvector extension and creates initial tables for Pilot Memory & Tasks

CREATE EXTENSION IF NOT EXISTS vector;
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- 1. Users Table (Sovereign Local Tenant)
CREATE TABLE IF NOT EXISTS users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    email VARCHAR(255) UNIQUE NOT NULL,
    full_name VARCHAR(255) NOT NULL,
    persona_preferences JSONB DEFAULT '{}',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 2. Epistemic Episodic Memory Table (Vector Store with 1024-dim BGE-M3 / MiniLM embeddings)
CREATE TABLE IF NOT EXISTS episodic_memory (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    content TEXT NOT NULL,
    metadata JSONB DEFAULT '{}',
    source_type VARCHAR(50) NOT NULL, -- 'email', 'calendar', 'document', 'interaction'
    embedding vector(1024), -- Dimension matches BGE-M3
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- HNSW Vector Index for Sub-10ms Approximate Nearest Neighbor Retrieval
CREATE INDEX IF NOT EXISTS idx_episodic_memory_embedding 
ON episodic_memory 
USING hnsw (embedding vector_cosine_ops)
WITH (m = 16, ef_construction = 64);

-- Full-Text Lexical Search Index for Hybrid RAG (BM25 Equivalent in Postgres)
CREATE INDEX IF NOT EXISTS idx_episodic_memory_fts 
ON episodic_memory 
USING gin (to_tsvector('english', content));

-- 3. Epistemic Knowledge Graph Nodes (Entities & Concepts)
CREATE TABLE IF NOT EXISTS kg_nodes (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    name VARCHAR(255) NOT NULL,
    entity_type VARCHAR(50) NOT NULL, -- 'Person', 'Company', 'Project', 'Topic', 'Preference'
    properties JSONB DEFAULT '{}',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(user_id, name, entity_type)
);

-- 4. Epistemic Knowledge Graph Edges (Relationships & Claims)
CREATE TABLE IF NOT EXISTS kg_edges (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    source_node_id UUID REFERENCES kg_nodes(id) ON DELETE CASCADE,
    target_node_id UUID REFERENCES kg_nodes(id) ON DELETE CASCADE,
    relation_type VARCHAR(100) NOT NULL, -- 'WORKS_WITH', 'ATTENDING', 'PREFERS', 'SUPERVISES'
    weight FLOAT DEFAULT 1.0,
    evidence TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 5. Human-in-the-Loop Action Approval Queue
CREATE TABLE IF NOT EXISTS pending_actions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    agent_id VARCHAR(50) NOT NULL,
    action_type VARCHAR(100) NOT NULL, -- 'send_email', 'book_meeting', 'delete_event', 'execute_tool'
    payload JSONB NOT NULL,
    status VARCHAR(20) DEFAULT 'PENDING', -- 'PENDING', 'APPROVED', 'REJECTED', 'EXECUTED'
    explanation TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    resolved_at TIMESTAMP WITH TIME ZONE
);

