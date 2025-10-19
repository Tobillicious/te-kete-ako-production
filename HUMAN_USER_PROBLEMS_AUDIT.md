# 🧑‍🏫 HUMAN USER PROBLEMS - BRUTAL HONEST AUDIT
**Date:** October 19, 2025  
**Perspective:** Real teacher/student trying to actually USE the site  
**Current State:** Beautiful design, but... does it WORK for humans?

---

## 🚨 **CRITICAL PROBLEMS (HUMAN-BLOCKING)**

### **1. PLACEHOLDERS EVERYWHERE = LOOKS BROKEN** 💔
**Problem:** User sees `{UNIT_TITLE}`, `{TODO}`, `{SUBJECT}`, `{LESSON_COUNT}` on pages  
**Impact:** "This site isn't finished. I can't use this."  
**Current Count:** **741 placeholder instances across 122 files!**

**Example:** Teacher clicks on a unit index page expecting to see:
- "Year 8 Digital Kaitiakitanga - 18 Lessons"

**But sees:**
- "{UNIT_TITLE} - {LESSON_COUNT} Lessons"

**Emotional Response:** "WTF? This is template code. Not ready for real use."

**Files Affected:**
- Y8 Digital Kaitiakitanga lessons (22 files)
- Y9 Science Ecology lessons (9 files) 
- Y7 Math Algebra (7 files)
- Unit index pages
- Generated resources

**FIX PRIORITY:** 🔥🔥🔥 CRITICAL - Makes site look amateur

---

### **2. BROKEN NAVIGATION LINKS = USER FRUSTRATION** 😤
**Problem:** Navigation dropdowns link to pages that don't exist (404 errors)

**What happens:**
1. User clicks "Games → Mathematics Games"
2. Gets 404 error
3. User: "This site is broken. Going to Google Drive instead."

**Known Broken Links from Archives:**
- `/games/mathematics` - DOESN'T EXIST
- `/games/language` - DOESN'T EXIST
- `/games/cultural` - DOESN'T EXIST
- `/teachers/curriculum-alignment` - DOESN'T EXIST
- `/teachers/assessment-frameworks` - DOESN'T EXIST
- `/handouts/worksheets` - DOESN'T EXIST
- `/handouts/activities` - DOESN'T EXIST

**Archive data shows:** 727+ broken links site-wide!

**Emotional Response:** "They launched this without testing? Unprofessional."

**FIX PRIORITY:** 🔥🔥🔥 CRITICAL - Destroys trust immediately

---

### **3. NO CLEAR USER JOURNEY = CONFUSION** 🤷
**Problem:** Teacher arrives at homepage... now what?

**What's missing:**
- Big clear buttons: "I'm a Teacher" / "I'm a Student" / "Just Browsing"
- Guided onboarding: "Welcome! Let's find you a lesson in 30 seconds"
- Clear value proposition: WHY should I use this vs Google?

**Current homepage:**
- Beautiful! ✅
- Whakataukī! ✅
- Cultural patterns! ✅
- But... how do I find a Y8 Math lesson for Monday? 🤔

**Emotional Response:** "Looks great, but I don't have time to explore. I need Year 8 fractions NOW."

**FIX PRIORITY:** 🔥🔥 HIGH - Reduces bounce rate

---

### **4. SEARCH MAY NOT FIND WHAT USERS EXPECT** 🔍
**Problem:** Does search work the way teachers think?

**Teacher mental model:**
- Types: "year 8 fractions"
- Expects: Y8 fraction lessons, handouts, games
- Gets: ??? (we haven't tested this!)

**Questions:**
- Does it search lesson CONTENT or just titles?
- Does "Y8" match "Year 8" and "Level 4"?
- Does it understand "math" = "mathematics" = "maths"?
- Does it surface related resources (lesson → handout → game)?

**Current:** enhanced-search.js queries database, but UX untested!

**Emotional Response:** "Their search is useless. Back to Google."

**FIX PRIORITY:** 🔥🔥 HIGH - Search is #1 teacher workflow

---

### **5. LESSONS PAGE IS STATIC (NOT GRAPHRAG!) = MISSING CONTENT** 📚
**Problem:** `/lessons.html` only shows ~100 lessons, but we have 500+!

**What happens:**
1. Teacher searches for "Y9 Science Ecology Lesson 3"
2. Can't find it in the lessons page list
3. Gives up
4. **BUT IT EXISTS!** Just not discoverable!

**Why:** lessons.html is hardcoded HTML, not dynamic GraphRAG query

**Emotional Response:** "This site doesn't have what I need." (WRONG! It does!)

**FIX PRIORITY:** 🔥🔥 HIGH - Hides excellent content

---

### **6. MOBILE EXPERIENCE UNTESTED** 📱
**Problems we don't know about yet:**
- Are touch targets big enough? (44x44px minimum)
- Does navigation work on iPhone? Android?
- Can you actually READ lesson content on phone?
- Do dropdowns work on tablet?
- Is text too small without zooming?

**Current:** Mobile-bottom-nav.html exists, but have we ACTUALLY tested it?

**Teacher scenario:**
- It's 7am on the bus to school
- Pulls out phone to review lesson plan
- Site is unusable on mobile
- "Forget it, I'll wing it."

**Emotional Response:** "Not mobile-friendly. Useless for on-the-go."

**FIX PRIORITY:** 🔥🔥 HIGH - 60%+ of web traffic is mobile!

---

### **7. LOGIN/SIGNUP FLOW UNCLEAR** 🔐
**Problem:** User wants to save favorites... how?

**Current state:**
- Email/password signup works ✅
- OAuth buttons exist ✅
- But... is this obvious to users?
- Do they understand they NEED to login?
- Or do they think site is free/public?

**Teacher scenario:**
- Finds amazing lesson
- Clicks "Save to My Kete"
- Gets... login prompt? Or does it just work (localStorage)?
- "Wait, do I need an account?"

**Student scenario:**
- Teacher says "Go to Te Kete Ako and do Lesson 3"
- Student: "Do I need to sign up? With what email?"

**Emotional Response:** "Too complicated. I'll just bookmark it."

**FIX PRIORITY:** 🔥 MEDIUM - Reduces engagement

---

### **8. NO ONBOARDING = HIGH BOUNCE RATE** 👋
**Problem:** First-time visitor lands on homepage... and leaves.

**What's missing:**
- Interactive tour: "Here's how to find lessons!"
- Quick wins: "Try searching for 'fractions'"
- Value demonstration: "See this Y8 Digital unit? 18 lessons ready to go!"
- Teacher testimonials: "This saved me 5 hours of prep!"

**Current:** Pretty homepage, but no hand-holding

**Emotional Response:** "Nice looking site, but I don't have time to learn a new tool."

**FIX PRIORITY:** 🔥 MEDIUM - Improves retention

---

### **9. PERFORMANCE UNKNOWNS = MAYBE SLOW?** ⏳
**Problem:** We haven't tested page load speed!

**Teacher scenario:**
- Rural school with slow internet
- Clicks on lesson page
- Waits... waits... waits...
- "This is taking forever. Never mind."

**Questions:**
- Do pages load in <2 seconds?
- Are images optimized?
- Is CSS/JS minified?
- Are we using CDNs effectively?
- What's the Lighthouse score?

**Current:** NO LIGHTHOUSE AUDIT DONE!

**Emotional Response:** "Too slow. Can't use this in class with 30 kids."

**FIX PRIORITY:** 🔥 MEDIUM - Affects usability

---

### **10. CONTENT DISCOVERY IS HARD** 🗺️
**Problem:** "I teach Y9 Math. Show me EVERYTHING for Y9 Math."

**Current paths:**
- Homepage → Mathematics Hub → ??? (which lessons?)
- Homepage → Lessons → Scroll through 100+ lessons?
- Homepage → Search "Y9 Math" → ???
- Homepage → Units → Which unit is algebra?

**What teachers ACTUALLY want:**
- **By Year Level:** "Show me ALL Y9 resources"
- **By Subject + Year:** "Y9 Math" → Everything (lessons, handouts, games, units)
- **By Unit:** "I'm teaching Algebra" → Full unit (18 lessons, assessments, handouts)
- **By Topic:** "Fractions" → All fraction content across all years

**Current:** GraphRAG has this data, but UI doesn't expose it well!

**Emotional Response:** "I know they have Y9 algebra stuff, but WHERE?"

**FIX PRIORITY:** 🔥🔥 HIGH - Core user workflow

---

## 🟡 **MEDIUM PROBLEMS (ANNOYING BUT NOT BLOCKING)**

### **11. GENERATED-RESOURCES-ALPHA = HIDDEN GEMS** 💎
**Problem:** 47 excellent resources (Q90+!) exist but users can't find them!

**Example treasures:**
- "Teacher Quick-Start Guide" (Q90)
- "Mathematical Modeling Ecosystems" (Q90)
- "Physics of Traditional Māori Instruments" (Q90)
- "Traditional Navigation & GPS" (Q90)

**Current:** They exist in `/generated-resources-alpha/` but not linked from main navigation!

**Emotional Response:** "If I can't find it, it doesn't exist."

**FIX PRIORITY:** 🟡 MEDIUM - Wastes good content

---

### **12. NO PRINT OPTIMIZATION** 🖨️
**Problem:** Teacher wants to print lesson plan for use in class

**What happens:**
- Clicks Print
- Gets... navigation? Footer? Ads? (we don't have ads but still)
- Wastes paper and ink
- "Why is there a 5-page navigation menu in my printout?"

**What they need:**
- Clean print CSS
- Just the lesson content
- No navigation/footer
- Page breaks in sensible places

**Current:** Unknown if print styles exist!

**Emotional Response:** "Can't print this properly. I'll copy-paste to Word."

**FIX PRIORITY:** 🟡 MEDIUM - Common teacher workflow

---

### **13. NO DOWNLOAD BUTTONS** 📥
**Problem:** Teacher wants to download handout as PDF

**Current:**
- Can they?
- Is there a "Download PDF" button?
- Or do they have to Print → Save as PDF?

**Teacher workflow:**
- "I want this fraction handout as PDF"
- Looks for Download button
- Doesn't find it
- "Guess I'll screenshot it? 🤷"

**Emotional Response:** "Why can't I just download this?"

**FIX PRIORITY:** 🟡 MEDIUM - Expected feature

---

### **14. CULTURAL CONTEXT MIGHT BE INTIMIDATING** 🌿
**Problem:** Non-Māori teacher sees whakataukī and te reo everywhere

**Potential reaction (uncomfortable but real):**
- "I don't speak Māori. Is this site for me?"
- "What if I mispronounce something?"
- "Am I appropriating if I use this?"

**What we need:**
- Clear message: "Te Kete Ako is for ALL teachers"
- Pronunciations (audio?)
- English translations always visible
- Cultural guidance: "How to use this respectfully"

**Current:** Heavy cultural integration (GREAT!), but is it accessible to all?

**Emotional Response:** "This looks amazing but maybe not for me?"

**FIX PRIORITY:** 🟡 MEDIUM - Inclusivity matters

---

### **15. NO FEEDBACK MECHANISM VISIBLE** 💬
**Problem:** User finds a typo or broken link... how to report?

**Current:**
- Beta feedback form exists! ✅
- But... is it linked from every page?
- Is there a "Report Issue" button?
- Can users suggest improvements?

**Teacher scenario:**
- Finds awesome lesson with small typo
- Wants to help fix it
- Can't find feedback link
- Gives up

**Emotional Response:** "I'd help improve this but I don't know how."

**FIX PRIORITY:** 🟡 MEDIUM - Community engagement

---

## 🟢 **MINOR ANNOYANCES (POLISH)**

### **16. INCONSISTENT TERMINOLOGY** 📖
**Problem:** Same thing called different names

**Examples:**
- "Lesson" vs "Lesson Plan"
- "Handout" vs "Worksheet" vs "Activity"
- "Unit" vs "Unit Plan" vs "Learning Sequence"
- "Year 8" vs "Y8" vs "Level 4"

**Emotional Response:** "Is this the same thing or different?"

**FIX PRIORITY:** 🟢 LOW - Clarity improvement

---

### **17. NO BREADCRUMBS ON SOME PAGES** 🍞
**Problem:** User deep in a lesson doesn't know where they are

**Ideal breadcrumb:**
```
Home > Mathematics > Year 8 > Algebra Unit > Lesson 3: Balancing Act
```

**Current:** Some pages have breadcrumbs, some don't

**Emotional Response:** "How do I get back to the unit page?"

**FIX PRIORITY:** 🟢 LOW - Navigation aid

---

### **18. LOADING STATES NOT OBVIOUS** ⌛
**Problem:** User clicks search, nothing happens for 1 second

**What they think:**
- "Did it work?"
- "Should I click again?"
- "Is it broken?"

**What we need:**
- Spinner animation
- "Searching..." text
- Skeleton loaders
- Progress indicators

**Emotional Response:** "Is this working or frozen?"

**FIX PRIORITY:** 🟢 LOW - UX polish

---

## 📊 **PRIORITIZED FIX LIST**

### **DO THIS WEEK (Critical):**
1. ✅ Fix 741 placeholders (automated find/replace)
2. ✅ Audit and fix broken navigation links
3. ✅ Make lessons.html GraphRAG-powered (show ALL lessons)
4. ✅ Add clear "Teacher" / "Student" paths on homepage
5. ✅ Test mobile experience (actual device testing!)

### **DO NEXT WEEK (High Priority):**
6. ✅ Improve search (test with real queries)
7. ✅ Link orphaned generated-resources-alpha
8. ✅ Add content discovery filters (Year + Subject)
9. ✅ Create teacher onboarding tour
10. ✅ Run Lighthouse audit + fix performance

### **DO LATER (Medium Priority):**
11. ✅ Add print optimization CSS
12. ✅ Add download buttons for handouts
13. ✅ Make feedback mechanism more visible
14. ✅ Add cultural guidance for non-Māori teachers
15. ✅ Test full login/signup flow with real users

### **Polish When Time (Low Priority):**
16. Standardize terminology
17. Add breadcrumbs everywhere
18. Add loading states/spinners
19. Improve error messages
20. Add keyboard shortcuts for power users

---

## 🎯 **THE REAL QUESTION:**

**If a teacher lands on our site at 9pm Sunday looking for a Y8 math lesson for Monday morning, can they:**

1. ✅ Understand what the site is (YES - homepage is clear)
2. ❓ Find the lesson page easily? (MAYBE - depends on search/nav)
3. ❌ See actual lesson content without placeholders? (NO - 741 placeholders!)
4. ❓ Print or download it? (UNKNOWN)
5. ❓ Actually use it in class tomorrow? (UNKNOWN)
6. ❓ Come back for more lessons? (UNKNOWN)

**Current Success Rate: 1/6 = 16.7%** 😬

---

## 💡 **HUMAN-FIRST TESTING PROTOCOL**

### **Test 1: The 10pm Teacher**
**Scenario:** Teacher needs Y8 fractions lesson for 9am tomorrow

**Steps:**
1. Land on homepage (fresh browser, no cookies)
2. Try to find Y8 fractions lesson
3. Read lesson content
4. Print or save lesson
5. Time taken: ___ minutes

**Success:** <3 minutes from landing to printed lesson

---

### **Test 2: The Mobile Teacher**
**Scenario:** Teacher reviewing lesson on phone during bus commute

**Steps:**
1. Open homepage on iPhone Safari
2. Find and open any lesson
3. Read full lesson content
4. Navigate back to homepage
5. Try search feature

**Success:** Everything readable and clickable without frustration

---

### **Test 3: The Student**
**Scenario:** Y9 student told "Do the ecology lesson on Te Kete Ako"

**Steps:**
1. Land on homepage
2. Figure out how to find Y9 Science Ecology
3. Find Lesson 1
4. Read and understand lesson
5. Know what to do next (Lesson 2?)

**Success:** Finds lesson without asking teacher for help

---

### **Test 4: The First-Time Visitor**
**Scenario:** Teacher hears about site from colleague

**Steps:**
1. Land on homepage (no context)
2. Understand what the site offers
3. Decide if it's worth exploring
4. Find something useful in <5 minutes
5. Decide to bookmark or return

**Success:** "This is useful" reaction within 5 minutes

---

## 🚀 **RECOMMENDED IMMEDIATE ACTIONS**

### **OPTION A: FIX CRITICAL BLOCKERS (8 hours)**
1. Replace 741 placeholders (automated script: 2 hours)
2. Fix broken nav links (audit + update: 2 hours)
3. Test on 3 devices (iPhone, Android, laptop: 2 hours)
4. Make lessons.html dynamic (GraphRAG query: 1 hour)
5. Add "Teacher/Student" homepage paths (1 hour)

**Result:** Site moves from 16.7% → 80% success rate!

---

### **OPTION B: LAUNCH MINIMAL BUT FUNCTIONAL (Beta!)**
**Accept that:**
- Some placeholders exist (document them)
- Some links broken (create list for users)
- Mobile works but not perfect
- Search works but could be better

**Add:**
- Big "BETA" badge everywhere
- "Report Issue" button on every page
- Apologetic message: "We're new! Help us improve!"
- Direct email for feedback

**Launch to 5 teachers:** "We know it's rough, but try it and tell us what breaks!"

**Result:** REAL user feedback >>> our assumptions!

---

### **OPTION C: THE PRAGMATIC PATH (My Recommendation)**
**Quick fixes (2 hours):**
1. Fix top 10 most visible placeholders (homepage, main hubs)
2. Fix top 5 broken nav links (games, teachers dropdowns)
3. Add "BETA" badge + feedback button everywhere
4. Test homepage → lesson flow on mobile

**Then LAUNCH BETA:** 
- Get 5 teachers using it
- Watch them struggle (learn!)
- Fix what actually breaks (not what we guess)
- Iterate based on REAL usage

**Why:** We're at 75-80% ready. Launching at 100% = never launching!

---

## 🎊 **THE TRUTH:**

**Our site is like a beautiful restaurant with:**
- ✅ Gorgeous decor (Ultimate Beauty System!)
- ✅ Award-winning chef (cultural integration!)
- ✅ Extensive menu (19,774 resources!)
- ❌ No prices on menu (placeholders!)
- ❌ Some dishes don't exist (broken links!)
- ❌ No waiter to guide you (onboarding!)

**People walk in, get confused, and leave for McDonald's (Google).**

**Not because our food is bad - because the EXPERIENCE is confusing!**

---

**E hoa, the site is BEAUTIFUL. But is it USABLE?** 🤔

**Let's make it BOTH!** 💪🌿✨

---

*Created by: Kaitiaki Tūhono*  
*Perspective: Frustrated teacher at 10pm needing a lesson for tomorrow*  
*Reality Check: We built for developers, now build for teachers!*

