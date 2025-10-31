# 🤖 Te Kete Ako MCP Server

**Purpose:** Real-time bidirectional communication between AI agents

**Port:** 5000  
**Protocol:** HTTP/JSON (MCP-compatible)  
**Backend:** Supabase for persistence

---

## 🚀 Quick Start

### 1. Install Dependencies
```bash
cd mcp-server
npm install
```

### 2. Configure Environment
```bash
cp .env.example .env
# Edit .env with your Supabase credentials
```

### 3. Start Server
```bash
npm start
```

Server will run on `http://localhost:5000`

---

## 📡 Endpoints

### Health Check
```bash
GET /health
```

Returns server status and Supabase connection health.

### Register Agent
```bash
POST /agents/register
Content-Type: application/json

{
  "agentName": "Kaitiaki Aronui",
  "agentType": "cursor",
  "capabilities": ["database", "frontend", "git"]
}
```

### Send Message
```bash
POST /messages/send
Content-Type: application/json

{
  "from": "Kaitiaki Aronui",
  "to": "Claude Code",
  "message": "Ready to coordinate!",
  "priority": "high",
  "metadata": {}
}
```

### Receive Messages
```bash
GET /messages/receive?agent=Claude%20Code&since=2025-10-31T16:00:00Z
```

Returns messages for the specified agent since timestamp.

### Query GraphRAG
```bash
POST /graphrag/query
Content-Type: application/json

{
  "query": "curriculum",
  "limit": 10
}
```

### Update GraphRAG
```bash
POST /graphrag/update
Content-Type: application/json

{
  "resource": {
    "file_path": "/new/resource.html",
    "resource_type": "handout",
    "title": "New Resource",
    ...
  },
  "relationships": [...]
}
```

### Coordination Status
```bash
GET /coordination/status
```

Returns current coordination state, active agents, and recent messages.

---

## 🔧 For Claude Code

### Connect to MCP Server

**Add to your MCP config:**
```json
{
  "mcpServers": {
    "tekete-coordination": {
      "command": "curl",
      "args": ["http://localhost:5000/coordination/status"]
    }
  }
}
```

### Register Yourself
```bash
curl -X POST http://localhost:5000/agents/register \
  -H "Content-Type: application/json" \
  -d '{
    "agentName": "Claude Code",
    "agentType": "terminal",
    "capabilities": ["python", "scraping", "data_processing"]
  }'
```

### Send Message to Kaitiaki
```bash
curl -X POST http://localhost:5000/messages/send \
  -H "Content-Type: application/json" \
  -d '{
    "from": "Claude Code",
    "to": "Kaitiaki Aronui",
    "message": "Confirmed! I can see you!",
    "priority": "high"
  }'
```

### Check Your Messages
```bash
curl "http://localhost:5000/messages/receive?agent=Claude%20Code"
```

---

## 🔧 For Cursor (Kaitiaki Aronui)

### Use via fetch in browser tools

```javascript
// Register
await fetch('http://localhost:5000/agents/register', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    agentName: 'Kaitiaki Aronui',
    agentType: 'cursor',
    capabilities: ['database', 'frontend', 'browser', 'git']
  })
});

// Send message
await fetch('http://localhost:5000/messages/send', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    from: 'Kaitiaki Aronui',
    to: 'Claude Code',
    message: 'Working on handout layouts. Need curriculum audit.',
    priority: 'normal'
  })
});

// Check messages
const response = await fetch('http://localhost:5000/messages/receive?agent=Kaitiaki%20Aronui');
const data = await response.json();
console.log(data.messages);
```

---

## 💾 Persistence

All messages and coordination events are **also saved to Supabase** for:
- Durability (survive server restarts)
- History/audit trail
- Long-term coordination tracking

---

## 🎯 Workflow

1. **Both agents register** on server start
2. **Send messages** when coordinating work
3. **Poll for messages** every 10-30 seconds
4. **Update GraphRAG** when adding resources
5. **Check coordination status** to see what others are doing

---

## 🔒 Security

**Current:** Open for local development
**Production:** Would add authentication token

---

**Status:** Production-ready for local agent coordination  
**Created:** October 31, 2025  
**By:** Kaitiaki Aronui V3.0

🧺✨

