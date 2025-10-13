#!/usr/bin/env node

/**
 * ================================================================
 * SETUP GRAPHRAG SCHEMA FOR AGENT COORDINATION
 * ================================================================
 * 
 * Creates the complete database schema for 12-agent collaboration
 * through Supabase GraphRAG knowledge base
 * 
 * ================================================================
 */

const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');
const path = require('path');

// Configuration
const SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co';
const SUPABASE_SERVICE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1MzA4OTMzOSwiZXhwIjoyMDY4NjY1MzM5fQ.QEy2Y87lgNGzunseLEDAW2AMGmAn9M8YYsspsRIIQE';

const supabase = createClient(SUPABASE_URL, SUPABASE_SERVICE_KEY);

async function setupSchema() {
    console.log('🔧 Setting up GraphRAG schema for agent coordination...');
    
    try {
        // 1. Create resource_concepts table
        console.log('Creating resource_concepts table...');
        const { error: conceptsError } = await supabase.rpc('execute_sql', {
            sql: `
                CREATE TABLE IF NOT EXISTS resource_concepts (
                    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                    resource_id UUID REFERENCES resources(id) ON DELETE CASCADE,
                    concept_name TEXT NOT NULL,
                    relevance_score DECIMAL(3,2) DEFAULT 0.5,
                    cultural_context TEXT,
                    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
                    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
                );
                
                CREATE INDEX IF NOT EXISTS idx_resource_concepts_name ON resource_concepts(concept_name);
                CREATE INDEX IF NOT EXISTS idx_resource_concepts_resource_id ON resource_concepts(resource_id);
            `
        });
        
        if (conceptsError) {
            console.error('Error creating resource_concepts:', conceptsError);
        } else {
            console.log('✅ resource_concepts table created');
        }
        
        // 2. Create resource_relationships table
        console.log('Creating resource_relationships table...');
        const { error: relationshipsError } = await supabase.rpc('execute_sql', {
            sql: `
                CREATE TABLE IF NOT EXISTS resource_relationships (
                    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                    source_resource_id UUID REFERENCES resources(id) ON DELETE CASCADE,
                    target_resource_id UUID REFERENCES resources(id) ON DELETE CASCADE,
                    relationship_type TEXT NOT NULL,
                    strength DECIMAL(3,2) DEFAULT 0.5,
                    description TEXT,
                    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
                );
                
                CREATE INDEX IF NOT EXISTS idx_resource_relationships_source ON resource_relationships(source_resource_id);
                CREATE INDEX IF NOT EXISTS idx_resource_relationships_target ON resource_relationships(target_resource_id);
                CREATE INDEX IF NOT EXISTS idx_resource_relationships_type ON resource_relationships(relationship_type);
            `
        });
        
        if (relationshipsError) {
            console.error('Error creating resource_relationships:', relationshipsError);
        } else {
            console.log('✅ resource_relationships table created');
        }
        
        // 3. Create agent_tasks table
        console.log('Creating agent_tasks table...');
        const { error: tasksError } = await supabase.rpc('execute_sql', {
            sql: `
                CREATE TABLE IF NOT EXISTS agent_tasks (
                    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                    task_name TEXT NOT NULL,
                    task_description TEXT,
                    assigned_agent_id TEXT,
                    status TEXT DEFAULT 'pending',
                    priority TEXT DEFAULT 'medium',
                    dependencies TEXT[],
                    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
                    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
                    completed_at TIMESTAMP WITH TIME ZONE,
                    knowledge_required TEXT[],
                    knowledge_generated TEXT[]
                );
                
                CREATE INDEX IF NOT EXISTS idx_agent_tasks_status ON agent_tasks(status);
                CREATE INDEX IF NOT EXISTS idx_agent_tasks_agent ON agent_tasks(assigned_agent_id);
                CREATE INDEX IF NOT EXISTS idx_agent_tasks_priority ON agent_tasks(priority);
            `
        });
        
        if (tasksError) {
            console.error('Error creating agent_tasks:', tasksError);
        } else {
            console.log('✅ agent_tasks table created');
        }
        
        // 4. Create agent_knowledge table
        console.log('Creating agent_knowledge table...');
        const { error: knowledgeError } = await supabase.rpc('execute_sql', {
            sql: `
                CREATE TABLE IF NOT EXISTS agent_knowledge (
                    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                    agent_id TEXT NOT NULL,
                    knowledge_type TEXT NOT NULL,
                    knowledge_content TEXT NOT NULL,
                    source_task_id UUID REFERENCES agent_tasks(id) ON DELETE SET NULL,
                    confidence DECIMAL(3,2) DEFAULT 0.5,
                    verified BOOLEAN DEFAULT FALSE,
                    verification_agent_id TEXT,
                    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
                    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
                );
                
                CREATE INDEX IF NOT EXISTS idx_agent_knowledge_agent ON agent_knowledge(agent_id);
                CREATE INDEX IF NOT EXISTS idx_agent_knowledge_type ON agent_knowledge(knowledge_type);
                CREATE INDEX IF NOT EXISTS idx_agent_knowledge_verified ON agent_knowledge(verified);
            `
        });
        
        if (knowledgeError) {
            console.error('Error creating agent_knowledge:', knowledgeError);
        } else {
            console.log('✅ agent_knowledge table created');
        }
        
        // 5. Create cultural_metadata table
        console.log('Creating cultural_metadata table...');
        const { error: culturalError } = await supabase.rpc('execute_sql', {
            sql: `
                CREATE TABLE IF NOT EXISTS cultural_metadata (
                    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                    resource_id UUID REFERENCES resources(id) ON DELETE CASCADE,
                    cultural_level TEXT NOT NULL,
                    iwi_hapu_connections TEXT[],
                    te_reo_terms TEXT[],
                    cultural_concepts TEXT[],
                    protocols TEXT[],
                    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
                    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
                );
                
                CREATE INDEX IF NOT EXISTS idx_cultural_metadata_resource ON cultural_metadata(resource_id);
                CREATE INDEX IF NOT EXISTS idx_cultural_metadata_level ON cultural_metadata(cultural_level);
            `
        });
        
        if (culturalError) {
            console.error('Error creating cultural_metadata:', culturalError);
        } else {
            console.log('✅ cultural_metadata table created');
        }
        
        // 6. Create agent_coordination table
        console.log('Creating agent_coordination table...');
        const { error: coordinationError } = await supabase.rpc('execute_sql', {
            sql: `
                CREATE TABLE IF NOT EXISTS agent_coordination (
                    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                    coordination_type TEXT NOT NULL,
                    initiating_agent_id TEXT NOT NULL,
                    target_agent_ids TEXT[],
                    message TEXT NOT NULL,
                    context_data JSONB,
                    status TEXT DEFAULT 'pending',
                    response TEXT,
                    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
                    responded_at TIMESTAMP WITH TIME ZONE
                );
                
                CREATE INDEX IF NOT EXISTS idx_agent_coordination_type ON agent_coordination(coordination_type);
                CREATE INDEX IF NOT EXISTS idx_agent_coordination_status ON agent_coordination(status);
                CREATE INDEX IF NOT EXISTS idx_agent_coordination_initiator ON agent_coordination(initiating_agent_id);
            `
        });
        
        if (coordinationError) {
            console.error('Error creating agent_coordination:', coordinationError);
        } else {
            console.log('✅ agent_coordination table created');
        }
        
        console.log('\n🎉 GraphRAG schema setup complete!');
        console.log('All tables are now ready for 12-agent coordination');
        
    } catch (error) {
        console.error('❌ Schema setup failed:', error);
    }
}

// Run the setup
setupSchema().then(() => {
    console.log('\n✅ Setup complete');
    process.exit(0);
}).catch(error => {
    console.error('❌ Setup failed:', error);
    process.exit(1);
});
