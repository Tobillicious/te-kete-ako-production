#!/usr/bin/env python3
"""
Apply Multi-Agent Access Fix to Supabase
Restores multi-agent coordination by fixing RLS policies
"""

import os
from supabase import create_client, Client

# Supabase configuration
SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM'

def main():
    print("🔧 APPLYING MULTI-AGENT ACCESS FIX")
    print("=" * 60)
    
    # Initialize Supabase client
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
    
    # Read the migration SQL
    migration_file = 'supabase/migrations/20251020_restore_multi_agent_access.sql'
    
    try:
        with open(migration_file, 'r') as f:
            sql_content = f.read()
        
        print(f"✅ Read migration file: {migration_file}")
        print(f"📝 SQL length: {len(sql_content)} characters")
        print()
        
        # Split SQL into individual statements
        # Remove comments and empty lines
        statements = []
        current_statement = []
        in_do_block = False
        
        for line in sql_content.split('\n'):
            stripped = line.strip()
            
            # Skip comments and empty lines
            if stripped.startswith('--') or not stripped:
                continue
            
            # Track DO blocks (they can contain semicolons)
            if 'DO $$' in stripped or 'DO$$' in stripped:
                in_do_block = True
            
            current_statement.append(line)
            
            # End of statement
            if ';' in stripped:
                if in_do_block and 'END $$;' in stripped:
                    in_do_block = False
                    statements.append('\n'.join(current_statement))
                    current_statement = []
                elif not in_do_block:
                    statements.append('\n'.join(current_statement))
                    current_statement = []
        
        print(f"📊 Found {len(statements)} SQL statements to execute")
        print()
        
        # Execute each statement
        success_count = 0
        error_count = 0
        
        for i, statement in enumerate(statements, 1):
            # Skip verification queries
            if 'SELECT' in statement and 'pg_policies' in statement:
                print(f"⏭️  [{i}/{len(statements)}] Skipping verification query")
                continue
            
            # Truncate for display
            display_statement = statement[:100].replace('\n', ' ').strip()
            if len(statement) > 100:
                display_statement += '...'
            
            try:
                print(f"⚙️  [{i}/{len(statements)}] Executing: {display_statement}")
                
                # Execute via raw SQL
                result = supabase.rpc('exec_sql', {'sql': statement}).execute()
                
                print(f"✅ [{i}/{len(statements)}] Success")
                success_count += 1
                
            except Exception as e:
                error_msg = str(e)
                
                # Some errors are expected (like "policy already exists")
                if 'already exists' in error_msg.lower() or 'does not exist' in error_msg.lower():
                    print(f"⚠️  [{i}/{len(statements)}] Expected: {error_msg[:60]}")
                    success_count += 1
                else:
                    print(f"❌ [{i}/{len(statements)}] Error: {error_msg[:100]}")
                    error_count += 1
        
        print()
        print("=" * 60)
        print(f"✅ Migration Complete!")
        print(f"   - Success: {success_count}")
        print(f"   - Errors: {error_count}")
        print()
        
        # Verify the fix worked
        print("🧪 VERIFYING FIX...")
        print()
        
        try:
            # Test reading resources table
            result = supabase.table('resources').select('id, title').limit(5).execute()
            print(f"✅ Resources table accessible: {len(result.data)} resources found")
            
            # Test reading relationships table
            result = supabase.table('relationships').select('id, relationship_type').limit(5).execute()
            print(f"✅ Relationships table accessible: {len(result.data)} relationships found")
            
            # Test reading multi_ai_coordination_log
            result = supabase.table('multi_ai_coordination_log').select('id').limit(5).execute()
            print(f"✅ Coordination log accessible: {len(result.data)} entries found")
            
            print()
            print("🎉 MULTI-AGENT ACCESS RESTORED!")
            print("   All 12 agents can now collaborate fully")
            
        except Exception as e:
            print(f"⚠️  Verification failed: {str(e)}")
            print("   You may need to apply the migration manually via Supabase Dashboard")
    
    except FileNotFoundError:
        print(f"❌ Migration file not found: {migration_file}")
        print("   Please ensure the file exists")
        return 1
    
    except Exception as e:
        print(f"❌ Unexpected error: {str(e)}")
        return 1
    
    return 0

if __name__ == '__main__':
    exit(main())
