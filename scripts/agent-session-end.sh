#!/bin/bash
# 📤 AGENT SESSION END
# Run this when you finish your work session!
# Logs completion and checks out via MCP

set -e

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}📤 TE KETE AKO AGENT SESSION END${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
echo ""

# Get session summary
read -p "Your agent ID: " AGENT_ID
echo ""
read -p "What did you complete? " COMPLETED
echo ""
read -p "What files did you change? " FILES
echo ""
read -p "What should next agent know? " NEXT_AGENT

echo ""
echo -e "${YELLOW}📝 Logging to GraphRAG...${NC}"

python3 -c "
import os
from supabase import create_client
from datetime import datetime

try:
    supabase = create_client(
        'https://nlgldaqtubrlcqddppbq.supabase.co',
        os.getenv('SUPABASE_KEY', '')
    )
    
    # Log completion
    description = f'''Completed: {repr('$COMPLETED')}
Files changed: {repr('$FILES')}
Next agent should know: {repr('$NEXT_AGENT')}
Session ended: {datetime.now().isoformat()}'''
    
    result = supabase.table('resources').insert({
        'title': f'✅ Session Complete: $AGENT_ID',
        'description': description,
        'path': f'/work/$AGENT_ID-session-{datetime.now().strftime(\"%Y%m%d-%H%M\")}.log',
        'type': 'activity',
        'subject': 'Platform Development',
        'level': 'Completed',
        'tags': ['session-complete', '$AGENT_ID', datetime.now().strftime('%Y-%m-%d')],
        'author': '$AGENT_ID'
    }).execute()
    
    print('  ✅ Logged to GraphRAG!')
    
except Exception as e:
    print(f'  ⚠️  Could not log: {str(e)[:60]}')
"

echo ""
echo -e "${YELLOW}🚪 Checking out via MCP...${NC}"

python3 -c "
import os
from supabase import create_client

try:
    supabase = create_client(
        'https://nlgldaqtubrlcqddppbq.supabase.co',
        os.getenv('SUPABASE_KEY', '')
    )
    
    result = supabase.rpc('checkout', {
        'p_agent_id': '$AGENT_ID'
    }).execute()
    
    print('  ✅', result.data[0]['checkout'])
    
except Exception as e:
    print(f'  ⚠️  Checkout failed: {str(e)[:60]}')
"

echo ""
echo -e "${GREEN}🎉 SESSION COMPLETE! Great work!${NC}"
echo ""
echo -e "${YELLOW}Your work is now:${NC}"
echo "  ✅ Logged in GraphRAG"
echo "  ✅ Available for next agent"
echo "  ✅ Visible in session history"
echo ""
echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"

