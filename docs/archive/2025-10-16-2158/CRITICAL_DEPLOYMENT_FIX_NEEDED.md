# 🚨 CRITICAL: DEPLOYMENT CONFIGURATION ISSUE

**Date:** October 15, 2025  
**Severity:** HIGH - Enhanced content not reaching production  
**Impact:** 54 enhanced lessons not visible on deployed site

---

## 🔍 **ROOT CAUSE:**

### **The Mismatch:**

1. **Our Work:** All in `public/` directory ✅
   - 54 lessons enhanced today
   - 370+ external resources added
   - All files current (Oct 15)

2. **Netlify Config:** Deploys from `dist/` ❌
   - `netlify.toml` says: `publish = "dist"`
   - But `dist/` is in `.gitignore` (not committed)
   - Build only processes index.html + auth-test.html
   - Lesson files NOT copied to dist/

3. **Result:** Production site missing all our enhancements! 😢

---

## 💡 **SOLUTION OPTIONS:**

### **OPTION 1: Deploy `public/` Directly (RECOMMENDED)**

This is a static site with 1000+ HTML files - no build process needed!

**Update netlify.toml:**
```toml
[build]
  base = "."
  publish = "public"  ← CHANGE THIS FROM "dist"
  command = "echo 'Deploying public/ directly - no build needed'"
```

**Benefits:**
- ✅ All 1000+ HTML files deployed
- ✅ All our enhancements visible
- ✅ Faster deployment (no build)
- ✅ What you edit = what deploys

### **OPTION 2: Fix Build to Copy All Files**

Update `vite.config.js`:
```javascript
import { resolve } from 'path';
import { defineConfig } from 'vite';
import { copyFileSync, mkdirSync, readdirSync, statSync } from 'fs';
import { join } from 'path';

export default defineConfig({
  root: resolve(__dirname, 'public'),
  build: {
    outDir: resolve(__dirname, 'dist'),
    emptyOutDir: true,
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'public/index.html'),
        auth: resolve(__dirname, 'public/auth-test.html'),
      },
    },
  },
  plugins: [
    {
      name: 'copy-html-files',
      closeBundle() {
        // Copy all HTML files from public/ to dist/
        // (implement full directory copy)
      }
    }
  ]
});
```

**But this is complex for a static site!**

---

## 🎯 **RECOMMENDED ACTION:**

### **Quick Fix (Deploy public/ directly):**

```bash
# 1. Update netlify.toml
sed -i '' 's/publish = "dist"/publish = "public"/' netlify.toml

# 2. Commit and push
git add netlify.toml
git commit -m "Fix: Deploy public/ directly - all enhanced lessons now visible"
git push origin main

# 3. Netlify will auto-deploy with ALL our enhancements!
```

### **For Local Development:**

```bash
# Serve from public/ to see all changes
cd /Users/admin/Documents/te-kete-ako-clean/public
python3 -m http.server 8888

# Visit: http://localhost:8888/
```

Or:

```bash
# Use Vite dev server
cd /Users/admin/Documents/te-kete-ako-clean
npm run dev

# Visit: http://localhost:5173/
```

---

## 📊 **WHAT THIS FIXES:**

**Current State (BROKEN):**
- Netlify deploys `dist/` (Oct 10, missing our work)
- `dist/` only has index.html + auth-test.html
- 54 enhanced lessons NOT in dist/
- Production site shows old content

**After Fix (WORKING):**
- Netlify deploys `public/` (Oct 15, ALL our work!)
- All 1000+ HTML files deployed
- 54 enhanced lessons visible
- Production site shows all enhancements!

---

## ✅ **VERIFICATION:**

**After deploying, check these pages on production:**

1. https://tekete.netlify.app/units/y8-digital-kaitiakitanga/lessons/lesson-1-what-is-our-digital-whenua.html
   - Should have: External Resources section

2. https://tekete.netlify.app/units/unit-1-te-ao-maori/lessons/ai-ethics-and-data-sovereignty.html
   - Should have: Te Mana Raraunga, Te Hiku Media links

3. https://tekete.netlify.app/guided-inquiry-unit/lessons/lesson-2-group-formation.html
   - Should have: Whanaungatanga resources

---

## 🚀 **WHY THIS MATTERS:**

**Without Fix:**
- Teachers don't see 370+ curated NZ resources
- Students missing culturally authentic content
- 6+ hours of systematic enhancement invisible
- GraphRAG @ 1,417 resources but not deployed
- Platform looks "months old" (as user noted!)

**With Fix:**
- All 60 enhanced lessons visible
- 370+ NZ educational authority links accessible
- Cultural integration visible
- Professional styling shows
- Platform current and world-class!

---

## ⚡ **DO THIS NOW:**

```bash
cd /Users/admin/Documents/te-kete-ako-clean

# Fix netlify.toml
sed -i '' 's/publish = "dist"/publish = "public"/' netlify.toml

# Verify the change
grep "publish" netlify.toml

# Should show: publish = "public"
```

Then commit and push to deploy all enhancements!

---

**STATUS:** Issue diagnosed - simple config fix will make all 60 lessons visible!

**Kaiārahi Ako** 🧺✨

