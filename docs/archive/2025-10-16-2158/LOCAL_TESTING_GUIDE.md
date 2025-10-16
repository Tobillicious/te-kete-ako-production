# 🧪 LOCAL TESTING GUIDE

**Date:** October 16, 2025  
**Status:** Local server started  
**URL:** http://localhost:8000/

---

## ✅ SERVER RUNNING

**Command:** `python3 -m http.server 8000`  
**Directory:** `/Users/admin/Documents/te-kete-ako-clean/public`  
**Status:** Running in background

---

## 🌐 HOW TO ACCESS

### **In Your Browser:**

**Open:** `http://localhost:8000/`

This will show you the homepage of your production site!

---

## 📋 TESTING CHECKLIST

### **Homepage Test:**
- [ ] Visit: http://localhost:8000/
- [ ] Check: Professional design loads
- [ ] Check: Mega menu navigation appears
- [ ] Check: Statistics show (1,520 resources)
- [ ] Check: No console errors (F12 → Console tab)

### **Navigation Test:**
- [ ] Hover over "Units" in mega menu
- [ ] Check: Dropdown appears with unit list
- [ ] Click: Any unit
- [ ] Check: Unit page loads professionally
- [ ] Check: Navigation works throughout

### **Orphaned Pages Test:**
- [ ] Visit: http://localhost:8000/generated-resources-alpha/
- [ ] Check: Index page shows
- [ ] Click: Handouts
- [ ] Check: 26 handouts listed
- [ ] Click: Any handout
- [ ] Check: Loads with professional styling

### **Teacher Dashboard Test:**
- [ ] Visit: http://localhost:8000/teacher-dashboard.html
- [ ] Check: Dashboard loads
- [ ] Check: Featured units show
- [ ] Check: Statistics display
- [ ] Check: Professional styling throughout

### **Mobile Test:**
- [ ] Resize browser to mobile width (F12 → Toggle device toolbar)
- [ ] Check: Hamburger menu appears
- [ ] Click: Hamburger menu
- [ ] Check: Mobile menu opens
- [ ] Check: Navigation works on mobile

### **Console Check:**
- [ ] Press F12 (or Cmd+Option+I on Mac)
- [ ] Click: Console tab
- [ ] Check: No red errors
- [ ] Check: CSS files load with cache-busting hashes
- [ ] Check: No 404 errors

---

## 🎯 KEY PAGES TO TEST

**Must-test for October 22:**

1. **Homepage:** http://localhost:8000/
2. **Teacher Dashboard:** http://localhost:8000/teacher-dashboard.html
3. **Y8 Systems Unit:** http://localhost:8000/y8-systems/
4. **Y8 Lesson 1-1:** http://localhost:8000/y8-systems/lessons/lesson-1-1.html
5. **Generated Resources:** http://localhost:8000/generated-resources-alpha/
6. **Handouts Index:** http://localhost:8000/generated-resources-alpha/handouts/
7. **Units Index:** http://localhost:8000/units/

---

## 🔧 TROUBLESHOOTING

### **If page doesn't load:**
1. Check server is running: `lsof -ti:8000`
2. Check no errors in terminal where server is running
3. Try: http://127.0.0.1:8000/ (alternative localhost)
4. Clear browser cache (Cmd+Shift+R on Mac)

### **If CSS doesn't load:**
1. Open browser console (F12)
2. Look for 404 errors
3. Check if CSS files exist in public/css/min/
4. Verify cache-busting hashes in HTML

### **If navigation doesn't work:**
1. Check console for JavaScript errors
2. Verify navigation-header.html exists
3. Check navigation JS files load

### **To stop the server:**
```bash
# Find process ID
lsof -ti:8000

# Kill the process
kill [PID]
```

Or just close the terminal where it's running.

---

## 🎨 WHAT YOU SHOULD SEE

### **Homepage:**
- ✅ Professional hero section
- ✅ Mega menu with sticky header
- ✅ Statistics: 1,520 resources
- ✅ Beautiful West Coast NZ colors
- ✅ Smooth animations on hover

### **Navigation:**
- ✅ Sticky header (scrolls with you)
- ✅ Dropdown menus (Units, Resources, etc.)
- ✅ Smooth hover effects
- ✅ Mobile hamburger menu
- ✅ Professional throughout

### **Teacher Dashboard:**
- ✅ Featured units display
- ✅ Quick access links
- ✅ Platform statistics
- ✅ Professional layout

### **Lessons:**
- ✅ Consistent styling
- ✅ Professional design
- ✅ Print-ready
- ✅ Mobile responsive

---

## 📱 MOBILE TESTING

**In Browser:**
1. Press F12 (DevTools)
2. Click device toolbar icon (or Cmd+Shift+M)
3. Select: iPhone or iPad
4. Test: Navigation, scrolling, clicking
5. Verify: Hamburger menu works

**On Real Device (Optional):**
1. Find your computer's local IP: `ifconfig | grep "inet "`
2. On phone, visit: `http://[YOUR-IP]:8000/`
3. Test site on actual mobile device

---

## 🎯 EXPECTED RESULTS

**All pages should:**
- ✅ Load quickly
- ✅ Show professional styling
- ✅ Have working navigation
- ✅ Be mobile responsive
- ✅ Print correctly
- ✅ No console errors

**Unified CSS system means:**
- Consistent colors throughout
- Consistent spacing
- Consistent typography
- Professional appearance everywhere

---

## 💬 IF YOU SEE ISSUES

**Report:**
1. Which page has the issue
2. What's wrong (screenshot helps!)
3. Browser console errors
4. Device/browser used

**I can fix:**
- Broken links
- CSS issues
- JavaScript errors
- Mobile problems

---

## 🚀 AFTER TESTING

**If everything looks good:**
✅ Site is ready for deployment!  
✅ Can push to production: `git push origin main`  
✅ Netlify will auto-deploy  
✅ Ready for October 22!

**If issues found:**
🔧 We'll fix them together  
🔧 Make additional commits  
🔧 Test again  
🔧 Deploy when perfect  

---

**Status:** Server running, ready to test!  
**URL:** http://localhost:8000/  
**Next:** Open browser and explore your professional site! 🧺✨

