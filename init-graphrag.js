const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');

// Supabase connection
const SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co';
const SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM';

const supabase = createClient(SUPABASE_URL, SUPABASE_KEY);

async function initializeTables() {
  console.log('🔧 Initializing GraphRAG tables...');
  
  try {
    // Read SQL file
    const sql = fs.readFileSync('./init-graphrag-tables.sql', 'utf8');
    
    // Execute SQL
    const { error } = await supabase.rpc('exec_sql', { sql_string: sql });
    
    if (error) {
      console.error('Error initializing tables:', error);
      
      // Try direct table creation if RPC fails
      await createTablesDirectly();
    } else {
      console.log('✅ GraphRAG tables initialized successfully');
    }
  } catch (err) {
    console.error('Failed to initialize tables:', err);
    
    // Try direct table creation
    await createTablesDirectly();
  }
}

async function createTablesDirectly() {
  console.log('🔧 Creating tables directly...');
  
  try {
    // Create site_structure table
    const { error: structureError } = await supabase.rpc('create_site_structure_table');
    if (structureError && !structureError.message.includes('already exists')) {
      console.error('Error creating site_structure table:', structureError);
    }
    
    // Create content_hierarchy table
    const { error: hierarchyError } = await supabase.rpc('create_content_hierarchy_table');
    if (hierarchyError && !hierarchyError.message.includes('already exists')) {
      console.error('Error creating content_hierarchy table:', hierarchyError);
    }
    
    console.log('✅ Tables creation attempted');
  } catch (err) {
    console.error('Failed to create tables directly:', err);
  }
}

// Run initialization
initializeTables();
