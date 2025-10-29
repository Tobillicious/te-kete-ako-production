# 🚀 Quick Start Local Server

**Use when Cursor terminal is stuck**

---

## Option 1: Mac Terminal.app (Recommended)

1. Open **Terminal.app** (Applications → Utilities → Terminal)
2. Copy/paste this command:
```bash
cd /Users/admin/Documents/te-kete-ako-clean && python3 -m http.server 8001
```
3. Press Enter
4. You'll see: "Serving HTTP on :: port 8001..."
5. Open browser to: **http://localhost:8001/index.html**

---

## Option 2: VS Code Terminal

1. Open VS Code
2. Terminal → New Terminal
3. Run: `cd /Users/admin/Documents/te-kete-ako-clean`
4. Run: `python3 -m http.server 8001`
5. Open: http://localhost:8001/index.html

---

## 🧪 URLs to Test

**Homepage**: http://localhost:8001/index.html  
**Browse**: http://localhost:8001/browse.html  
**Login**: http://localhost:8001/login.html  
**My Kete**: http://localhost:8001/my-kete.html  
**Sample Handout**: http://localhost:8001/handouts/media-literacy-comprehension-handout.html  
**Games**: http://localhost:8001/games/te-reo-wordle.html

---

## ✅ What to Test

### Dropdown Hover (JUST FIXED!):
- Hover over "Resources" menu
- Try moving mouse slowly down to dropdown
- Should be MUCH easier to access now!
- Dropdown should stay open for 1.2 seconds

### Header Icons:
- Should see emojis: 🔐 🧺 👤
- No ugly AI lock images!

### Bug Widget:
- Look for button in bottom-right corner
- Should appear on every page

### Auth Persistence:
- Login → Navigate to different pages
- Header should stay logged in
- My Kete should be accessible everywhere

---

## 🛑 Stop Server

When done testing:
1. Go back to terminal
2. Press `Ctrl + C`
3. Server will stop

---

**Quick Reference**: http://localhost:8001

