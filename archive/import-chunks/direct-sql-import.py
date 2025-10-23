#!/usr/bin/env python3
"""Direct SQL import using psycopg2"""

import os
import psycopg2
from pathlib import Path

def import_via_postgres():
    """Import via direct PostgreSQL connection"""
    
    # Connection details
    conn_params = {
        'host': 'aws-0-ap-southeast-2.pooler.supabase.com',
        'port': 6543,
        'database': 'postgres',
        'user': 'postgres.nlgldaqtubrlcqddppbq',
        'password': os.getenv('SUPABASE_PASSWORD', 'your_password_here')
    }
    
    try:
        print("🔗 Connecting to PostgreSQL...")
        conn = psycopg2.connect(**conn_params)
        cursor = conn.cursor()
        
        print("✅ Connected! Testing with tiny import...")
        
        # Read test SQL
        with open('test-import-tiny.sql', 'r') as f:
            sql = f.read()
        
        cursor.execute(sql)
        conn.commit()
        
        print("✅ Test import successful!")
        
        # Check count
        cursor.execute("SELECT COUNT(*) FROM graphrag_resources")
        count = cursor.fetchone()[0]
        print(f"📊 Total records: {count}")
        
        cursor.close()
        conn.close()
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    print("🚀 DIRECT POSTGRESQL IMPORT")
    print("=" * 50)
    
    # Check if we have password
    if not os.getenv('SUPABASE_PASSWORD'):
        print("⚠️ Set SUPABASE_PASSWORD environment variable")
        print("export SUPABASE_PASSWORD='your_password'")
        return
    
    success = import_via_postgres()
    
    if success:
        print("\n🎉 Ready for full 2,114 record import!")
    else:
        print("\n❌ Need to resolve connection issues first")

if __name__ == "__main__":
    main()