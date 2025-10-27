# ✅ MASTER TODO: Te Kete Ako Beta Launch
**Created:** October 27, 2025 (Evening)  
**Goal:** Launch free beta at tekete.co.nz  
**Timeline:** 2 weeks  
**Status:** Crystal clear roadmap

---

## 🎯 WHERE WE ARE RIGHT NOW

**✅ What's Done:**
- 143 teaching resources (quality content)
- Beautiful design system (culturally authentic)
- Navigation working perfectly
- 5 footer pages created tonight (about, contact, help, privacy, terms)
- Supabase backend configured (secretly amazing)
- Domain purchased (tekete.co.nz)

**🔧 What Needs Work:**
- Auth pages need design polish (look like "AI slop")
- Supabase connection needs key update (401 errors)
- My Kete not connected to backend
- Site not deployed to custom domain yet

**📏 Distance to Beta Launch:** ~40 hours of focused work

---

## 📅 WEEK 1: AUTH + MY KETE (20 hours)

### Day 1-2: Auth Page Design Polish (6 hours) ⭐ PRIORITY 1

**Files to Polish:**
- [ ] `login.html` - Extract inline styles to main.css
- [ ] `register-simple.html` - Extract inline styles to main.css  
- [ ] `forgot-password.html` - Check and polish
- [ ] `reset-password.html` - Check and polish

**What to Do:**
1. Remove all `<style>` blocks from auth pages
2. Add `.auth-page` section to css/main.css
3. Use existing CSS variables (colors, fonts, spacing)
4. Add whakataukī sidebar (use daily-whakatauki.js)
5. Match design quality of unit-plans.html, handouts.html
6. Keep forms FOCUSED (no busy heroes, just clean centered forms)

**Success:** Auth pages look like they belong in Te Kete Ako

---

### Day 3: Fix Supabase Connection (4 hours) ⭐ PRIORITY 2

**Tasks:**
- [ ] Get fresh Supabase anon key (from Supabase dashboard)
- [ ] Update `js/supabase-client.js` with new key
- [ ] Test login with demo account
- [ ] Test registration (create new test user)
- [ ] Verify profile auto-creates in database
- [ ] Check header auth state updates (Login → My Kete)
- [ ] Test logout flow
- [ ] Test forgot password (if email configured)

**Success:** Login/register works end-to-end, no 401 errors

---

### Day 4-5: My Kete Basic Functionality (8 hours) ⭐ PRIORITY 3

**Phase A: Display Saved Resources (4 hours)**
- [ ] Connect My Kete to `user_saved_resources` table
- [ ] Query user's saved resources
- [ ] Display in card grid (copy browse.html card design)
- [ ] Show stats: "You've saved X resources"
- [ ] Add filters (by type, subject)
- [ ] Handle empty state ("Save your first resource!")

**Phase B: Save Button Everywhere (3 hours)**
- [ ] Create `js/save-resource.js` helper
- [ ] Add ⭐ Save button to all resource pages
- [ ] Toggle saved/unsaved state
- [ ] Update `user_saved_resources` table
- [ ] Show confirmation: "Saved to My Kete!"
- [ ] Handle auth required (redirect to login if not logged in)

**Phase C: Recently Viewed (1 hour)**
- [ ] Track views in `user_access` table
- [ ] Show "Recently Viewed" section in My Kete
- [ ] Limit to last 10 resources

**Success:** Teachers can save, view, and manage resources in My Kete

---

### Day 6: Polish & Test (2 hours)

- [ ] Test all auth flows (register, login, logout, save, view)
- [ ] Test on mobile (Chrome, Safari)
- [ ] Fix any bugs found
- [ ] Check browser console for errors
- [ ] Test with 3-5 different resources

**Success:** Everything works smoothly, no critical bugs

---

## 📅 WEEK 2: DEPLOY + POLISH (20 hours)

### Day 7-8: Content Quick Wins (8 hours)

**Batch 1: Fix Homepage Stats (30 mins)**
- [ ] Update "40+ Resources" → "140+ Resources"
- [ ] Update "7 Unit Plans" → "8 Unit Plans"
- [ ] Test homepage displays correctly

**Batch 2: Delete Test Files (30 mins)**
- [ ] Delete `test-hero.html`
- [ ] Delete any other test/diagnostic files
- [ ] Clean up commented-out code in HTML files

**Batch 3: Update Footer Links Site-Wide (2 hours)**
- [ ] Update index.html footer (about, contact, help links)
- [ ] Update browse.html footer
- [ ] Update handouts.html footer
- [ ] Update unit-plans.html footer
- [ ] Update lessons.html footer
- [ ] Update games.html footer
- [ ] Test all footer links work

**Batch 4: Top 10 Resource Polish (5 hours)**
- [ ] Identify 10 most popular handouts (ask user OR pick best ones)
- [ ] Add "Teacher Notes" section to each
- [ ] Ensure whakataukī present
- [ ] Standardize CSS (all use main.css)
- [ ] Add "Differentiation Ideas" box
- [ ] Add "Formative Check" suggestions

---

### Day 9: Pre-Deployment Checklist (4 hours)

**Testing:**
- [ ] Test all navigation dropdowns (no 404s)
- [ ] Test browse.html filters work
- [ ] Test auth system completely
- [ ] Test My Kete save/view/delete
- [ ] Mobile responsive check (iPhone, Android)
- [ ] Print test (handouts print beautifully)
- [ ] Browser compatibility (Chrome, Safari, Firefox)

**Code Quality:**
- [ ] Remove console.log statements (or wrap in DEBUG checks)
- [ ] Check for broken links (grep href="#" excluding proper ones)
- [ ] Verify all images load
- [ ] Check CSS cache busting versions

**Git:**
- [ ] Commit all changes
- [ ] Clean commit history
- [ ] Tag release: `v1.0-beta`

---

### Day 10: Deployment (4 hours)

**Netlify Setup:**
- [ ] Push code to GitHub
- [ ] Connect Netlify to GitHub repo
- [ ] Configure build settings
- [ ] Test deployment on random Netlify URL

**Custom Domain:**
- [ ] Add tekete.co.nz in Netlify
- [ ] Configure DNS records (with domain registrar)
- [ ] Wait for DNS propagation (24-48 hours)
- [ ] Enable HTTPS
- [ ] Force HTTPS redirect

**Supabase Configuration:**
- [ ] Update allowed origins: `https://tekete.co.nz`
- [ ] Add to redirect URLs: `https://tekete.co.nz/*`
- [ ] Test auth on live site

**Final Testing:**
- [ ] Visit https://tekete.co.nz
- [ ] Test auth flows on live site
- [ ] Test My Kete on live site
- [ ] Test on mobile devices
- [ ] Share with 1-2 trusted friends for testing

---

### Day 11: Beta Invites (2 hours)

**Prepare:**
- [ ] Create beta testing feedback form (simple)
- [ ] Write beta invitation email
- [ ] Prepare list of 20-30 teachers to invite

**Launch:**
- [ ] Send beta invites
- [ ] Post in NZ teacher Facebook groups (soft launch)
- [ ] Monitor for bugs/feedback
- [ ] Respond to questions quickly

---

### Day 12-14: Iteration (2 hours)

- [ ] Fix bugs reported by beta testers
- [ ] Gather feedback
- [ ] Make small improvements
- [ ] Document learnings

**Success:** 20-50 teachers using the site, giving feedback

---

## 🚀 WEEK 3-4: SUBSCRIPTION PREP (Later)

**Don't Do Yet, But Plan For:**
- [ ] Create pricing.html page
- [ ] Show subscription status in My Kete
- [ ] Build trial countdown UI
- [ ] Prepare for Stripe integration
- [ ] Content gating logic (free tier limits)

---

## 🎯 IMMEDIATE NEXT STEPS (Tomorrow Morning)

### Option A: Commit Tonight's Work First (15 mins)
```bash
git add -A
git commit -m "🎉 Footer pages complete: About, Contact, Help, Privacy, Terms + Design refinements"
git status
```

### Option B: Start Auth Polish (if you have 2-3 hours)
1. Read login.html
2. Extract inline styles
3. Add to main.css
4. Test in browser
5. Repeat for register-simple.html

### Option C: Call It a Night
- Review this TODO list
- Start fresh tomorrow with Auth Polish
- You've done great work tonight! 🧺

---

## 📊 PROGRESS TRACKER

**Week 1:** Auth + My Kete  
- [ ] Day 1-2: Auth design (6h)
- [ ] Day 3: Fix connection (4h)
- [ ] Day 4-5: My Kete (8h)
- [ ] Day 6: Test (2h)

**Week 2:** Deploy + Polish  
- [ ] Day 7-8: Content polish (8h)
- [ ] Day 9: Pre-deploy check (4h)
- [ ] Day 10: Deploy (4h)
- [ ] Day 11: Beta invites (2h)
- [ ] Day 12-14: Iterate (2h)

**Total:** ~40 hours = Beta Launch 🚀

---

## 💡 KEY PRINCIPLES

**Keep It Simple:**
- Don't add features, polish what exists
- Auth + My Kete = enough value for beta
- Get feedback, then iterate

**One Agent, Monitored:**
- No 500-agent chaos
- Focused, systematic work
- GraphRAG for reference, not decisions

**Ship Fast:**
- Beta in 2 weeks is doable
- Paid launch in 4-6 weeks
- Perfect is the enemy of shipped

---

## 🧺 TONIGHT'S ACCOMPLISHMENTS

**✅ Completed:**
1. Proper onboarding (understood current state)
2. Fine-tooth comb audit (found minor issues)
3. Created 5 footer pages (professional, bilingual)
4. Deployment guide created
5. Strategic roadmap written
6. GraphRAG understanding clarified
7. Master TODO created (this document)

**📝 Uncommitted Work:**
- 7 files with design changes (ready to commit)
- 5 new footer pages (ready to commit)

---

## 🎯 RECOMMENDED: DO THIS NOW

**Commit your work (5 mins):**
```bash
cd /Users/admin/Documents/te-kete-ako-clean
git add -A
git status  # Review what's being committed
git commit -m "🎉 Footer pages complete + Browse hero architecture + Design refinements"
```

**Then either:**
- Start auth polish (if you have energy)
- Review this TODO tomorrow and start fresh
- Tell me what you want to tackle next

**You're in great shape. 2 weeks to beta is realistic.** 🚀

---

*Master TODO created: October 27, 2025*  
*Next update: After Week 1 Day 3 (Auth connection fixed)*

