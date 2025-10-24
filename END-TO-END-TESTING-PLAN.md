# 🧪 End-to-End Workflow Testing Plan

**Date:** October 24, 2025  
**Site:** https://tekete.netlify.app  
**Agent:** Cursor Agent (Bug Fix & GraphRAG)  
**Status:** Testing in progress...

---

## 🎯 **TEST SCENARIOS**

### **Workflow 1: Student Experience** 👨‍🎓
- [ ] Homepage loads cleanly
- [ ] Navigate to "I'm a Student" → getting-started.html
- [ ] Browse lessons by subject
- [ ] Click on a specific lesson (e.g., Y7 Algebra)
- [ ] Lesson content displays properly
- [ ] Navigation works
- [ ] Mobile view renders correctly

### **Workflow 2: Teacher Experience** 👨‍🏫
- [ ] Click "I'm a Teacher" → teachers/index.html
- [ ] Browse unit plans
- [ ] Open a complete unit (e.g., Y8 Digital Kaitiakitanga)
- [ ] Verify all 18 lessons link correctly
- [ ] Check if navigation/footer load
- [ ] Test resource downloads/links

### **Workflow 3: Search & Discovery** 🔍
- [ ] Use site search functionality
- [ ] Search for "science ecology"
- [ ] Verify GraphRAG results appear
- [ ] Check if recommendations show
- [ ] Test cross-subject discovery links

### **Workflow 4: Navigation & Components** 🧭
- [ ] Main navigation dropdown menus work
- [ ] Footer loads on all pages
- [ ] Mobile bottom nav appears (on mobile)
- [ ] FAB (Floating Action Button) works
- [ ] Breadcrumbs display correctly

### **Workflow 5: GraphRAG Features** 🧠
- [ ] Hidden gems page loads
- [ ] Excellence collection displays
- [ ] Connection badges hidden from users (Claude's CSS fix)
- [ ] No "brain" or "intelligence hub" buttons visible
- [ ] GraphRAG backend still working (queries succeed)

---

## 🔧 **TESTING METHOD**

Since I can't browse the web directly, I'll guide YOU through testing:

### **Quick Test Checklist:**

**1. Open https://tekete.netlify.app**
  - Does homepage load?
  - Console clean (only PWA icon warning)?
  - Three buttons visible (Teacher/Student/Browse)?

**2. Click "I'm a Teacher"**
  - Does /teachers/index.html load?
  - Can you find unit plans?
  - Navigation working?

**3. Open any lesson**
  - Content displays?
  - Navigation/footer present?
  - No errors in console?

**4. Try search**
  - Search box works?
  - Results appear?
  - Can click through to resources?

**5. Mobile test (if possible)**
  - Resize browser to mobile width
  - Navigation collapses properly?
  - Touch targets big enough?

---

## 📋 **ISSUES TO REPORT**

If you find any issues, please paste:
1. **URL** where the issue occurs
2. **Console errors** (F12 → Console tab)
3. **What's broken** (description)
4. **Expected behavior**

I'll fix them immediately!

---

## ✅ **EXPECTED RESULTS**

**Console:**
```
✅ PWA: Service Worker registered!
⚠️ PWA icon warning (cosmetic only)
```

**Site Functionality:**
- ✅ All pages load
- ✅ Navigation works
- ✅ Content displays
- ✅ GraphRAG features hidden from casual users
- ✅ Search operational
- ✅ Mobile responsive

---

**Ready to test! Please try the workflows above and let me know what you find!** 🚀

