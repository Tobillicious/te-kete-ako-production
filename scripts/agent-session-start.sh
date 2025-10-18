#!/bin/bash
# 🧠 AGENT SESSION STARTER
# Run this at the start of every work session!
# Queries GraphRAG to understand context, then checks in via MCP

set -e

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}🧠 TE KETE AKO AGENT SESSION STARTER${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
echo ""

# Check if Supabase connection is available
if [ -z "$SUPABASE_KEY" ]; then
    echo -e "${YELLOW}⚠️  SUPABASE_KEY not set. Using read-only mode.${NC}"
    echo ""
fi

echo -e "${GREEN}📊 RECENT ACTIVITY (Last 24 hours):${NC}"
echo "─────────────────────────────────────────────────────────────"
python3 -c "
import os
from supabase import create_client
from datetime import datetime

try:
    supabase = create_client(
        'https://nlgldaqtubrlcqddppbq.supabase.co',
        os.getenv('SUPABASE_KEY', '')
    )
    
    result = supabase.table('resources')\
        .select('title, author, created_at')\
        .gte('created_at', 'now() - interval \\'24 hours\\'')\
        .order('created_at', desc=True)\
        .limit(8)\
        .execute()
    
    for item in result.data:
        time = item['created_at'][:16]
        author = item['author'][:20] if len(item['author']) <= 20 else item['author'][:17] + '...'
        title = item['title'][:50] if len(item['title']) <= 50 else item['title'][:47] + '...'
        print(f'  {time} | {author:20} | {title}')
except Exception as e:
    print(f'  ⚠️  Could not query: {str(e)[:50]}')
"
echo ""

echo -e "${GREEN}👥 ACTIVE AGENTS (Right now):${NC}"
echo "─────────────────────────────────────────────────────────────"
python3 -c "
import os
from supabase import create_client

try:
    supabase = create_client(
        'https://nlgldaqtubrlcqddppbq.supabase.co',
        os.getenv('SUPABASE_KEY', '')
    )
    
    result = supabase.rpc('get_active_agents').execute()
    
    if result.data:
        for agent in result.data:
            print(f'  🤖 {agent[\"agent_name\"]:20} | {agent[\"current_task\"][:40]}')
    else:
        print('  💤 No other agents currently active')
except Exception as e:
    print(f'  ⚠️  Could not query: {str(e)[:50]}')
"
echo ""

echo -e "${GREEN}💡 KEY KNOWLEDGE (From GraphRAG):${NC}"
echo "─────────────────────────────────────────────────────────────"
python3 -c "
import os
from supabase import create_client

try:
    supabase = create_client(
        'https://nlgldaqtubrlcqddppbq.supabase.co',
        os.getenv('SUPABASE_KEY', '')
    )
    
    result = supabase.table('agent_knowledge')\
        .select('doc_type, key_insights')\
        .limit(3)\
        .execute()
    
    for entry in result.data:
        print(f'  📚 {entry[\"doc_type\"]}:')
        for insight in entry['key_insights'][:2]:
            print(f'     • {insight[:60]}...' if len(insight) > 60 else f'     • {insight}')
except Exception as e:
    print(f'  ⚠️  Could not query: {str(e)[:50]}')
"
echo ""

echo -e "${BLUE}─────────────────────────────────────────────────────────────${NC}"
echo ""

# Interactive check-in
echo -e "${GREEN}📝 CHECK IN VIA MCP:${NC}"
echo ""

read -p "Your agent ID (e.g. agent-5): " AGENT_ID
read -p "Your name: " AGENT_NAME
read -p "What are you working on? " TASK

echo ""
echo -e "${YELLOW}Checking in via MCP...${NC}"

python3 -c "
import os
from supabase import create_client

try:
    supabase = create_client(
        'https://nlgldaqtubrlcqddppbq.supabase.co',
        os.getenv('SUPABASE_KEY', '')
    )
    
    result = supabase.rpc('checkin', {
        'p_agent_id': '$AGENT_ID',
        'p_agent_name': '$AGENT_NAME',
        'p_task_desc': '$TASK',
        'p_files': []
    }).execute()
    
    print('  ✅', result.data[0]['checkin'])
except Exception as e:
    print(f'  ⚠️  Check-in failed: {str(e)[:60]}')
    print('  💡 Continue anyway - log your work to GraphRAG manually')
"

echo ""
echo -e "${GREEN}✅ READY TO WORK!${NC}"
echo ""
echo -e "${YELLOW}Remember to:${NC}"
echo "  1. Log your progress: python3 scripts/agent-log-progress.sh"
echo "  2. Heartbeat every 15 min: UPDATE agent_status SET last_heartbeat=now()"
echo "  3. Checkout when done: python3 scripts/agent-session-end.sh"
echo ""
echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"

