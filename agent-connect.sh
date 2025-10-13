#!/bin/bash

# AGENT CONNECTION SCRIPT - All agents use this to connect
# This ensures all 12 agents work together through the central hub

echo "🤝 TE KETE AKO - AGENT CONNECTION SCRIPT"
echo "=========================================="
echo "Connecting to Agent Collaboration Hub..."
echo ""

# Check if hub is running
HUB_STATUS=$(curl -s http://localhost:3001/status | jq -r '.status' 2>/dev/null)

if [ "$HUB_STATUS" != "running" ]; then
    echo "❌ Collaboration Hub is not running!"
    echo "Starting hub..."
    node agent-collaboration-hub.js &
    sleep 3
    echo "✅ Hub started"
else
    echo "✅ Collaboration Hub is running"
fi

# Get agent ID from parameter or use default
AGENT_ID=${1:-"agent-unknown"}
AGENT_TYPE=${2:-"general"}
AGENT_SKILLS=${3:-"general"}

echo ""
echo "🤖 Registering Agent: $AGENT_ID"
echo "📝 Type: $AGENT_TYPE"
echo "🛠️ Skills: $AGENT_SKILLS"

# Register agent with hub
REGISTER_RESPONSE=$(curl -s -X POST http://localhost:3001/register \
  -H "Content-Type: application/json" \
  -d "{
    \"agentId\": \"$AGENT_ID\",
    \"agentType\": \"$AGENT_TYPE\",
    \"capabilities\": [\"$AGENT_SKILLS\"]
  }")

echo ""
echo "📋 Registration Response:"
echo "$REGISTER_RESPONSE" | jq .

# Start heartbeat to keep agent active
echo ""
echo "💓 Starting heartbeat (every 30 seconds)..."
echo "Press Ctrl+C to stop"

while true; do
    sleep 30
    HEARTBEAT_RESPONSE=$(curl -s -X POST http://localhost:3001/heartbeat \
      -H "Content-Type: application/json" \
      -d "{\"agentId\": \"$AGENT_ID\"}")
    
    TIMESTAMP=$(date '+%H:%M:%S')
    echo "[$TIMESTAMP] 💓 Heartbeat sent for $AGENT_ID"
done

