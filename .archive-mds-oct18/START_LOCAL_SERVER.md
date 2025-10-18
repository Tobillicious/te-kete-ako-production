# 🚀 START LOCAL SERVER - Test Navigation

## Option 1: Python (Usually pre-installed on Mac)

```bash
cd /Users/admin/Documents/te-kete-ako-clean/public
python3 -m http.server 8000
```

Then open: **http://localhost:8000**

---

## Option 2: Node (if you have it)

```bash
cd /Users/admin/Documents/te-kete-ako-clean/public
npx http-server -p 8000
```

Then open: **http://localhost:8000**

---

## Option 3: VS Code Live Server

1. Open VS Code
2. Right-click on `public/index.html`
3. Select "Open with Live Server"

---

## 🧪 WHAT TO TEST:

### Homepage (index.html)
- ✅ Does navigation load?
- ✅ Do dropdown menus appear on hover?
- ❌ Click "Unit Plans" dropdown links - expect 404s
- ❌ Click "Teachers" dropdown links - expect 404s
- ❌ Click "Games" sub-menu links - expect 404s

### Handouts Page
- ✅ Check if yellow banner appears (NEW: 26 handouts)
- ✅ Click banner link - should go to `/generated-resources-alpha/handouts/`

### Lessons Page
- ✅ Check if green banner appears (NEW: 22 lessons)
- ✅ Click banner link - should go to `/generated-resources-alpha/lessons/`

---

## 🎯 DECISION GUIDE:

**If you love the dropdown design:**
→ Choose Option B (I'll fix all the broken links)

**If you want it working NOW:**
→ Choose Option A (Revert to working nav)

**If dropdowns are nice but not critical:**
→ Choose Option C (You fix manually later)

---

## 📊 CURRENT STATE:

**Working:**
- ✅ Homepage loads
- ✅ Navigation component loads
- ✅ Dropdowns appear visually
- ✅ New resource banners work

**Broken:**
- ❌ ~15+ dropdown links go to 404
- ❌ No verification was done on link targets
- ❌ Mock data in navigation

**Time to Fix:** 
- Option A (revert): 5 minutes
- Option B (fix links): 30 minutes

---

**Test it, then tell me: A, B, or C!**

