# 📋 SESSION PLAN - October 31, 2025
## Based on Complete Onboarding & Understanding

**Kaitiaki:** Kaitiaki Aronui V3.0  
**Time:** Evening Session (Post-Onboarding)  
**Onboarding:** ✅ COMPLETE (42,451 lines read, GraphRAG queried, patterns learned)

---

## 🎯 WORK SELECTION CRITERIA

Based on full understanding, I should choose work that:
1. ✅ **Follows established patterns** (account-settings.html as reference)
2. ✅ **Uses existing components** (don't reinvent)
3. ✅ **Fills documented gaps** (profile page needs glow-up)
4. ✅ **Safe to learn on** (not critical path, but eventually important)
5. ✅ **Won't block Kaiārahi** (independent work)

---

## 💎 SELECTED TASK: PROFILE PAGE GLOW-UP

### Why This Task:
- **User suggested it:** "Safe option because not critical at this stage but will be eventually. Good resource for you to learn first."
- **Clear reference:** Account-settings.html redesign is PERFECT template
- **Under-documented:** GraphRAG has NO profile design docs (I can create them)
- **Manageable scope:** Enhancement, not creation from scratch
- **Learning opportunity:** Practice the design patterns properly

### Current State (profile.html):
**What Works:**
- ✅ Auth check (login required gate)
- ✅ Loads user data from profiles table
- ✅ Displays: Avatar (initials), name, email, school, member since
- ✅ My Kete stats (saved resources count)
- ✅ Link to account-settings.html

**What's Missing (Gap Analysis from Onboarding Doc):**
- ❌ No whakataukī cultural opening
- ❌ No gradient hero section (just basic card)
- ❌ No role display (teacher/student)
- ❌ No subjects taught / year levels
- ❌ No cultural identity / iwi affiliation
- ❌ No teaching stats (resources used, curriculum coverage)
- ❌ Hardcoded inline styles (should use CSS variables)
- ❌ Plain white sections (should have cultural backgrounds)
- ❌ No animations
- ❌ Missing breadcrumb/back navigation

---

## 🎨 DESIGN APPROACH (From Learnings):

### Phase 1: Cultural Integration
**Add whakataukī relevant to profile/identity:**
- Option 1: "Ko au ko koe, ko koe ko au" (I am you, you are me - connection)
- Option 2: "Mā te huruhuru ka rere ai te manu" (Feathers let the bird fly - growth)
- **Connect it to:** Teacher identity, professional growth, learning journey

### Phase 2: Use Design System
**Replace ALL inline styles with:**
- `var(--color-forest)` for primary color
- `var(--color-cultural-light)` for section backgrounds
- `var(--shadow-medium)` for cards
- `var(--radius-lg)` for border-radius
- `linear-gradient(135deg, var(--color-forest), var(--color-secondary))` for hero

### Phase 3: Match Account-Settings Quality
**Copy successful patterns:**
- Gradient header with decorative circle
- Alternating section backgrounds (green/cream/white)
- Emoji section headers
- Floating label aesthetic
- fadeInUp animations with stagger delays
- Professional button hovers (translateY, box-shadow)

### Phase 4: Add Missing Data
**Show from profiles table:**
- Role badge (Teacher/Student/Admin)
- Subjects taught (if teacher)
- Year levels (student or taught)
- Cultural identity (if provided)
- Preferred language

### Phase 5: Enhanced Stats
**Beyond basic "saved resources":**
- Resources by type breakdown
- Last activity date
- Member duration
- Potentially: Curriculum coverage visualization (future)

---

## ✅ SUCCESS CRITERIA:

**Profile page will be considered complete when:**
1. ✅ Has cultural opening with whakataukī
2. ✅ Uses CSS variables throughout (zero hardcoded styles)
3. ✅ Beautiful gradient hero section
4. ✅ Shows role, subjects, year levels, cultural identity
5. ✅ Enhanced stats beyond just count
6. ✅ Animations and polish matching account-settings
7. ✅ Mobile responsive
8. ✅ I can demo it to user logged in as teacher@tekete.nz
9. ✅ User approves it without needing granular changes

---

## ⏰ TIMELINE:

**Estimated:** 60-90 minutes total

**Breakdown:**
- Phase 1 (Cultural): 10 mins
- Phase 2 (CSS variables): 15 mins
- Phase 3 (Match quality): 20 mins
- Phase 4 (Add data): 15 mins
- Phase 5 (Stats): 10 mins
- Testing & polish: 10-20 mins

---

## 🔄 PARALLEL WORK:

**While working, I will:**
- Check Kaiārahi messages every 15-20 mins
- Spot passive bugs as I test
- Stay available for oversight duties

---

## 📦 DELIVERABLES:

1. **Enhanced profile.html** - Beautiful, culturally integrated, fully functional
2. **Profile tested** - Logged in as teacher@tekete.nz, verified all features
3. **Screenshots** - Before/after for user approval
4. **Git commit** - Clean commit message following patterns
5. **GraphRAG update** - Document profile page design decisions

---

## 🚫 WHAT I WON'T DO:

- ❌ Create new markdown documentation files
- ❌ Build new components from scratch
- ❌ Change the design system
- ❌ Add features not in existing pages
- ❌ Over-promise on readiness
- ❌ Commit without testing

---

**READY TO BEGIN PROFILE PAGE GLOW-UP!** 💎

*Mā te whakaaro nui, mā te mahi tika*  
*(Through careful thought, through right action)*

🧺✨

