#!/usr/bin/env python3
"""
Execute Database Security Fixes
MCP-compatible: avoids terminal hangs, does not hardcode secrets, prefers RPC.
"""

import os
import sys
import json
from supabase import create_client, Client

# Supabase credentials
SUPABASE_URL = "https://nlgldaqtubrlcqddppbq.supabase.co"
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "")

def execute_sql_file(supabase: Client, filename: str):
    """Execute SQL from file"""
    try:
        with open(filename, 'r') as f:
            sql_content = f.read()
        
        print(f"📄 Executing SQL from {filename}")
        print(f"   Length: {len(sql_content)} characters")
        
        # Split by semicolon and execute each statement
        statements = [stmt.strip() for stmt in sql_content.split(';') if stmt.strip()]
        
        for i, statement in enumerate(statements):
            if statement:
                print(f"   Executing statement {i+1}/{len(statements)}")
                try:
                    # Execute via SQL RPC function if available (MCP-friendly)
                    result = supabase.rpc('exec_sql', {'sql': statement}).execute()
                    print(f"     ✅ Statement {i+1} executed")
                except Exception as e:
                    print(f"     ⚠️  Statement {i+1} failed via RPC: {e}")
                    print("     👉 Tip: Use MCP Supabase to run this statement non-interactively (mcp_supabase_execute_sql)")
                    # Continue with other statements
                    
    except Exception as e:
        print(f"❌ Error executing {filename}: {e}")

def check_security_status(supabase: Client):
    """Check current security status (MCP-friendly guidance + optional RPC)."""
    print("🔍 Checking current security status...")
    try:
        # Prefer running the provided verification SQL via RPC if exec_sql exists
        with open('get-view-definitions.sql', 'r') as f:
            verification_sql = f.read()
        try:
            _ = supabase.rpc('exec_sql', {'sql': verification_sql}).execute()
            print("   ✅ Verification SQL executed via RPC (exec_sql)")
        except Exception as rpc_err:
            print(f"   ⚠️ Verification via RPC unavailable: {rpc_err}")
            print("   👉 Tip: Run get-view-definitions.sql using MCP: mcp_supabase_execute_sql")
    except Exception as e:
        print(f"   ⚠️  Could not perform verification step: {e}")

def main():
    print("🛡️  EXECUTING DATABASE SECURITY FIXES")
    print("=" * 60)
    
    if not SUPABASE_KEY:
        print("❌ SUPABASE_KEY not set in environment. Set it or use MCP (mcp_supabase_execute_sql) to run SQL directly.")
        return

    # Connect to Supabase
    try:
        supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
        print("✅ Connected to Supabase")
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        return
    
    print()
    
    # Check current status
    check_security_status(supabase)
    print()
    
    # Execute the security fixes (uses ALTER VIEW ... SET security_invoker)
    print("🔧 Executing security fixes...")
    execute_sql_file(supabase, 'fix-security-issues.sql')
    print("🔎 Verifying view flags and RLS status...")
    execute_sql_file(supabase, 'get-view-definitions.sql')
    print()
    
    print("🎉 Security fixes execution completed!")
    print("📋 Next steps:")
    print("  1. Check the Supabase dashboard for any errors")
    print("  2. Verify views are recreated without SECURITY DEFINER")
    print("  3. Verify RLS is enabled on all tables")
    print("  4. Test application functionality")

if __name__ == "__main__":
    main()
