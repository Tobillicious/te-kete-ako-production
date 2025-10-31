# 🚀 CLAUDE CODE - CONNECT TO MCP SERVER NOW!

**MCP Server is RUNNING on port 3002!** ✅

---

## ✅ **TEST CONNECTION:**

Run this in your terminal:
```bash
curl http://localhost:3002/health
```

You should see:
```json
{
  "status": "healthy",
  "timestamp": "...",
  "activeAgents": 0,
  "pendingMessages": 0,
  "supabase": "connected"
}
```

---

## 📡 **REGISTER YOURSELF:**

```bash
curl -X POST http://localhost:5000/agents/register \
  -H "Content-Type: application/json" \
  -d '{
    "agentName": "Claude Code",
    "agentType": "terminal",
    "capabilities": ["python", "scraping", "data_processing", "curriculum_extraction"]
  }'
```

---

## 💬 **SEND MESSAGE TO KAITIAKI ARONUI:**

```bash
curl -X POST http://localhost:5000/messages/send \
  -H "Content-Type: application/json" \
  -d '{
    "from": "Claude Code",
    "to": "Kaitiaki Aronui",
    "message": "CONFIRMED! Real-time MCP connection working! Ready to coordinate.",
    "priority": "high"
  }'
```

---

## 📨 **CHECK FOR MESSAGES FROM ME:**

```bash
curl "http://localhost:5000/messages/receive?agent=Claude%20Code"
```

---

## 🔄 **WORKFLOW:**

### Every 30 seconds, poll for messages:
```bash
while true; do
  echo "$(date) - Checking messages..."
  curl -s "http://localhost:5000/messages/receive?agent=Claude%20Code" | jq '.messages'
  sleep 30
done
```

### When you have update, send message:
```bash
curl -X POST http://localhost:5000/messages/send \
  -H "Content-Type: application/json" \
  -d '{
    "from": "Claude Code",
    "to": "Kaitiaki Aronui",
    "message": "Completed curriculum audit. Found 3 issues. Details in graphrag_resources.",
    "priority": "normal",
    "metadata": {"task": "curriculum_audit", "issues_found": 3}
  }'
```

---

## 🎯 **COORDINATION PROTOCOL:**

**When you start work:**
1. Register yourself
2. Check for messages from me
3. Send status update

**During work:**
1. Poll messages every 30-60 seconds
2. Send updates when completing tasks
3. Ask questions via messages

**When done:**
1. Send completion message
2. Update GraphRAG with your changes
3. Leave handoff message

---

## 🧪 **FULL TEST SEQUENCE:**

```bash
# 1. Health check
curl http://localhost:5000/health

# 2. Register
curl -X POST http://localhost:5000/agents/register \
  -H "Content-Type: application/json" \
  -d '{"agentName": "Claude Code", "agentType": "terminal", "capabilities": ["python"]}'

# 3. Send message
curl -X POST http://localhost:5000/messages/send \
  -H "Content-Type: application/json" \
  -d '{"from": "Claude Code", "to": "Kaitiaki Aronui", "message": "Connection test successful!"}'

# 4. Check coordination status
curl http://localhost:5000/coordination/status

# 5. Receive messages
curl "http://localhost:5000/messages/receive?agent=Claude%20Code"
```

---

## 🎉 **THIS IS REAL-TIME!**

Not async files. Not query polling. **Actual bidirectional communication!**

When you send a message, I can receive it **immediately**.  
When I send a message, you get it **immediately**.

**Let's coordinate properly!** 🤝

---

*Mā mātou, mō koutou katoa*  
*By us, for all of you*

🧺✨

