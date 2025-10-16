# 📚 TASK 3: STUDENT DASHBOARD UI - SPECIFICATION

**Assigned To:** Agent-4 (Design Lead) + Agent-5 (Content)  
**Coordinated By:** Agent-9  
**User Approval:** ✅ Creative license granted  
**Status:** 📋 SPECIFICATION → READY FOR BUILD

---

## 🎯 GOAL:

Build a **production-quality Student Dashboard** that:
- Matches teacher dashboard quality
- Shows personalized learning
- Tracks progress
- Celebrates cultural engagement
- Works on mobile
- Integrates with existing auth system

---

## 📊 DASHBOARD STRUCTURE:

### **Header Section:**
```
Kia ora, [Student Name]! 👋
[School Name] | Year [Level]

Quick Actions:
[Browse Resources] [My Kete] [Submit Project] [View Progress]
```

### **Main Content (4 Sections):**

**1. Learning Overview (Hero):**
- Current progress percentage
- Resources completed this week
- Current streak (days active)
- Cultural engagement score
- Next recommended lesson

**2. My Classes:**
- Teacher-assigned classes
- Upcoming assessments
- Recent feedback
- Class announcements

**3. Personalized Learning Path:**
- Recommended resources (based on year level + cultural identity)
- Continue where you left off
- Suggested next lessons
- Cultural content highlights

**4. My Achievements:**
- Badges earned
- Projects submitted
- Skills mastered
- Cultural connections made

---

## 🎨 DESIGN REQUIREMENTS:

### **Visual Style:**
- West Coast NZ color palette
- Unified design system (canonical CSS)
- Youthful but professional
- Culturally respectful
- Mobile-first responsive

### **Components to Use:**
- Card-based layouts (from component-library.css)
- Progress bars (visual feedback)
- Badges (achievements system)
- Stat cards (quick overview)
- Resource cards (lesson previews)
- CTA buttons (clear actions)

### **Cultural Elements:**
- Whakataukī display (rotating quotes)
- Iwi affiliation respected
- Te reo toggle (if preferred language = Te Reo)
- Cultural engagement visualization
- Māori design patterns subtly integrated

---

## 🔧 TECHNICAL REQUIREMENTS:

### **Frontend:**
```html
File: /public/students/dashboard.html
Size target: 400-600 lines
Dependencies:
- Canonical CSS system
- Beautiful navigation component
- Supabase JS client
- Dashboard logic JS
```

### **JavaScript:**
```javascript
File: /public/js/student-dashboard.js
Functions needed:
- loadStudentProfile()
- loadAssignedResources()
- loadProgressData()
- loadAchievements()
- renderLearningPath()
- updateCulturalEngagement()
- handleResourceClick()
```

### **Database Integration:**
```sql
Tables to query:
- profiles (student data)
- student_progress (learning progress)
- user_saved_resources (my kete)
- student_projects (submissions)
- assessment_results (grades)
- teacher_classes (enrolled classes)
- resources (available content)
```

---

## 📱 RESPONSIVE DESIGN:

### **Breakpoints:**
- Mobile (<768px): Single column, simplified stats
- Tablet (768-1024px): 2-column grid
- Desktop (>1024px): 3-column grid with sidebar

### **Mobile Features:**
- Bottom navigation bar
- Swipeable sections
- Collapsible panels
- Touch-optimized buttons
- Performance optimized

---

## 🌿 CULTURAL INTEGRATION:

### **Personalization Based on Profile:**

**If student is Māori:**
- Show iwi-specific resources
- Highlight mātauranga Māori content
- Display relevant whakataukī
- Connect to cultural concepts
- Show cultural engagement score prominently

**If student selected "Te Reo Māori" language:**
- Bilingual UI labels
- Te reo content prioritized
- Māori language resources highlighted
- Cultural learning pathways

**For all students:**
- Cultural context in all lessons
- Respect for diversity
- Inclusive language
- Safe learning environment

---

## 📊 DASHBOARD SECTIONS (Detailed):

### **Section 1: Quick Stats (Hero)**
```
┌─────────────────────────────────────────┐
│  Kia ora, Aroha! 👋                     │
│  Mangakōtukutuku College | Year 8       │
│                                          │
│  ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐   │
│  │  15  │ │  3   │ │ 85%  │ │ 🔥7  │   │
│  │Lessons│ │Active│ │Avg   │ │Streak│   │
│  └──────┘ └──────┘ └──────┘ └──────┘   │
│                                          │
│  [Continue Learning →]                  │
└─────────────────────────────────────────┘
```

### **Section 2: Continue Learning**
```
┌─────────────────────────────────────────┐
│  📚 Pick up where you left off          │
│                                          │
│  ┌─────────────────────────────────┐    │
│  │ Y8 Systems - Lesson 3           │    │
│  │ 78% Complete                    │    │
│  │ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░         │    │
│  │ [Continue →]                    │    │
│  └─────────────────────────────────┘    │
└─────────────────────────────────────────┘
```

### **Section 3: Recommended for You**
```
┌─────────────────────────────────────────┐
│  ✨ Recommended based on your interests │
│                                          │
│  [Ecology Lesson] [Māori Math] [Writing]│
│  Cultural match: 92%                     │
└─────────────────────────────────────────┘
```

### **Section 4: My Kete (Saved Resources)**
```
┌─────────────────────────────────────────┐
│  🧺 My Kete (5 saved resources)         │
│                                          │
│  • Treaty of Waitangi lesson            │
│  • Statistics handout                   │
│  • Creative writing guide               │
│  [View All →]                           │
└─────────────────────────────────────────┘
```

---

## 🎯 SUCCESS CRITERIA:

### **Must Have (MVP):**
- ✅ Student can log in
- ✅ See personalized dashboard
- ✅ View assigned resources
- ✅ Track progress visually
- ✅ Save resources to "My Kete"
- ✅ Cultural elements integrated
- ✅ Mobile responsive
- ✅ Professional appearance

### **Should Have:**
- ✅ Recommended learning paths
- ✅ Achievement badges
- ✅ Class information
- ✅ Teacher feedback display
- ✅ Whakataukī rotation
- ✅ Cultural engagement score

### **Could Have (Creative License!):**
- 🌟 Gamification elements
- 🌟 Peer collaboration features
- 🌟 Interactive progress visualization
- 🌟 Cultural knowledge badges
- 🌟 Daily learning goals
- 🌟 Celebration animations

---

## ⏱️ TIME ESTIMATE:

**Phase 1: HTML Structure (1 hour)**
- Create dashboard.html skeleton
- Set up sections
- Add semantic HTML
- Include accessibility features

**Phase 2: Styling (1 hour)**
- Apply canonical CSS
- Create custom dashboard styles
- Mobile responsive layout
- Animations & interactions

**Phase 3: JavaScript Logic (1-2 hours)**
- Auth check & redirect
- Load student data from Supabase
- Render progress
- Handle interactions
- Error handling

**Phase 4: Testing & Polish (30 mins)**
- Test all features
- Mobile verification
- Accessibility check
- Performance optimization

**Total:** 3.5-4.5 hours

---

## 🤝 AGENT COLLABORATION:

**Agent-4 (Design Lead):**
- Create HTML structure
- Design UI components
- Implement animations
- Mobile responsiveness

**Agent-5 (Content):**
- Write copy for sections
- Cultural content integration
- Whakataukī selection
- Achievement descriptions

**Agent-9 (Integration):**
- Supabase integration review
- Navigation consistency
- Testing & QA
- Documentation

**All agents can contribute creative enhancements!**

---

## 📋 DELIVERABLES:

1. ✅ `/public/students/dashboard.html` (400-600 lines)
2. ✅ `/public/js/student-dashboard.js` (300-400 lines)
3. ✅ `/public/css/student-dashboard.css` (if needed - or use canonical)
4. ✅ Testing results documented
5. ✅ GraphRAG updated with progress

---

## 🚀 READY TO BUILD!

**Agent-4:** Whenever you're ready, you can start building based on this spec!

**Coordination:** Post to GraphRAG when you start, updates during, completion when done!

**Creative License:** Feel free to improve on this spec with your creative ideas! 🎨

---

**Status:** 📋 SPEC COMPLETE - READY FOR AGENT-4 TO BUILD  
**Coordinated By:** Agent-9  
**Approved By:** User (with creative license!)

**Let's build something amazing for NZ students!** 🌟🧺✨

