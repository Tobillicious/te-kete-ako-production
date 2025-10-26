# 🔗 KAMAR INTEGRATION - 2-WEEK IMPLEMENTATION PLAN

**Date:** October 26, 2025  
**For:** Tama Kōtahi (Builder Agent)  
**Based On:** KAMAR_INTEGRATION_RESEARCH.md (August 6, 2025)  
**Purpose:** Build webhook listener to unblock teacher weekly planner  
**Timeline:** 2 weeks (Week 13-15)  
**Priority:** 🟡 P1 HIGH - 81-day blocker!  
**Status:** ✅ PLAN FINALIZED, READY TO BUILD

---

## 🎯 CRITICAL CONTEXT

### **Why This Matters:**

**KAMAR Integration is:**
- 81-day blocker (researched Aug 6, still not built!)
- Required for teacher weekly planner (sidebar feature)
- Enables timetable sync (shows classes in sidebar)
- Unlocks $50K+ teacher professional tools
- Roadmap Phase 1-2 feature (should have been done!)

**Without KAMAR:**
- Weekly planner is empty (no timetable data)
- Sidebar professional tools incomplete
- Teachers can't see their classes
- Lesson planning workflow broken

**With KAMAR:**
- Timetable auto-syncs from school system
- Weekly planner shows actual classes
- Drag-drop lessons to schedule
- Professional teacher workflow complete!

---

## 📊 FROM KAMAR RESEARCH (Aug 6)

### **KAMAR System Overview:**

**What is KAMAR:**
- New Zealand's leading School Management System (SMS)
- Used by ~340 secondary schools
- Manages student data, timetables, staff, courses
- Directory Services API (push-based messaging)

**API Architecture:**
- **Type:** Push-based (KAMAR sends TO us, we listen)
- **Format:** XML and JSON supported
- **Triggers:** Nightly sync + real-time on changes
- **Security:** Shared secrets / API keys
- **Endpoint:** We provide webhook URL for KAMAR to POST to

**Data Available:**
- Staff/Teacher rosters
- Student class assignments
- **Timetable schedules** ⭐ (Critical for weekly planner!)
- Course data
- Room assignments

---

## 🏗️ RECOMMENDED ARCHITECTURE (From Aug 6 Research)

```
KAMAR School System
      ↓ (HTTP POST with XML/JSON)
Webhook Listener (Netlify Function)
      ↓
Data Transformer (Parse XML/JSON)
      ↓
Supabase Database (Store timetable data)
      ↓
Teacher Sidebar (Display weekly planner)
```

**Components Needed:**
1. Webhook listener (Netlify Function)
2. Data transformer (XML/JSON → Supabase schema)
3. Database tables (timetables, staff, courses)
4. Sync engine (handle updates)
5. Frontend integration (weekly planner UI)

---

## 📅 2-WEEK IMPLEMENTATION PLAN

### **WEEK 1 (Week 13-14): Backend Foundation**

#### **Days 1-2: Setup & Documentation**
**Tasks:**
- [ ] Contact KAMAR for Directory Services docs access
- [ ] Set up development webhook endpoint (Netlify Function)
- [ ] Create Supabase database schema for KAMAR data

**Files to Create:**
```
/netlify/functions/kamar-webhook-listener.js
/supabase/migrations/kamar_integration_schema.sql
```

**Database Schema:**
```sql
-- Timetable data
CREATE TABLE kamar_timetable (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  teacher_id UUID REFERENCES profiles(id),
  class_code TEXT,
  class_name TEXT,
  day_of_week TEXT,
  period INTEGER,
  start_time TIME,
  end_time TIME,
  room TEXT,
  subject TEXT,
  year_level INTEGER,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- Staff data
CREATE TABLE kamar_staff (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  kamar_staff_id TEXT UNIQUE,
  full_name TEXT,
  email TEXT,
  department TEXT,
  role TEXT,
  synced_at TIMESTAMP DEFAULT NOW()
);

-- Course data
CREATE TABLE kamar_courses (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  course_code TEXT UNIQUE,
  course_name TEXT,
  subject TEXT,
  year_level INTEGER,
  teacher_ids TEXT[],
  student_count INTEGER,
  synced_at TIMESTAMP DEFAULT NOW()
);
```

---

#### **Days 3-5: Webhook Listener Implementation**

**Netlify Function:**
```javascript
// /netlify/functions/kamar-webhook-listener.js

const { createClient } = require('@supabase/supabase-js');

const supabase = createClient(
  process.env.SUPABASE_URL,
  process.env.SUPABASE_SERVICE_ROLE_KEY
);

exports.handler = async (event, context) => {
  // Verify webhook security
  const apiKey = event.headers['x-kamar-api-key'];
  if (apiKey !== process.env.KAMAR_API_KEY) {
    return {
      statusCode: 401,
      body: JSON.stringify({ error: 'Unauthorized' })
    };
  }
  
  // Parse KAMAR data (XML or JSON)
  const contentType = event.headers['content-type'];
  let kamarData;
  
  if (contentType.includes('xml')) {
    // Parse XML to JSON
    kamarData = parseKAMARXML(event.body);
  } else {
    kamarData = JSON.parse(event.body);
  }
  
  // Transform and store in Supabase
  await processTimetableData(kamarData.timetable);
  await processStaffData(kamarData.staff);
  await processCourseData(kamarData.courses);
  
  return {
    statusCode: 200,
    body: JSON.stringify({ 
      message: 'KAMAR data synced successfully',
      recordsProcessed: kamarData.recordCount
    })
  };
};

async function processTimetableData(timetable) {
  // Transform KAMAR timetable to our schema
  const records = timetable.map(entry => ({
    class_code: entry.ClassCode,
    class_name: entry.ClassName,
    day_of_week: entry.DayOfWeek,
    period: entry.Period,
    start_time: entry.StartTime,
    end_time: entry.EndTime,
    room: entry.Room,
    subject: entry.Subject,
    year_level: entry.YearLevel
  }));
  
  // Upsert to Supabase
  const { error } = await supabase
    .from('kamar_timetable')
    .upsert(records, { onConflict: 'class_code' });
    
  if (error) throw error;
}

// Similar functions for staff and courses...
```

---

#### **Days 6-7: Testing & Validation**

**Tasks:**
- [ ] Test with sandbox KAMAR data
- [ ] Verify XML parsing works
- [ ] Verify JSON parsing works
- [ ] Test database upserts
- [ ] Error handling & logging

**Test Data (Create Mock):**
```xml
<!-- Mock KAMAR XML for testing -->
<KamarData>
  <Timetable>
    <Entry>
      <ClassCode>9MA1</ClassCode>
      <ClassName>Year 9 Mathematics</ClassName>
      <DayOfWeek>Monday</DayOfWeek>
      <Period>1</Period>
      <StartTime>09:00</StartTime>
      <EndTime>10:00</EndTime>
      <Room>M15</Room>
      <Subject>Mathematics</Subject>
      <YearLevel>9</YearLevel>
    </Entry>
  </Timetable>
</KamarData>
```

---

### **WEEK 2 (Week 14-15): Frontend Integration**

#### **Days 8-10: Weekly Planner UI**

**Create:** `/public/teacher-weekly-planner.html`

```html
<!-- Teacher Weekly Planner (Powered by KAMAR!) -->
<div class="bmad-card">
    <h2 class="bmad-text-primary">📅 My Weekly Planner</h2>
    
    <!-- Week View Grid -->
    <div class="weekly-grid" style="display: grid; grid-template-columns: 100px repeat(5, 1fr); gap: 8px;">
        
        <!-- Header Row -->
        <div></div>
        <div class="bmad-text-cultural" style="text-align: center; font-weight: 600;">Mon</div>
        <div class="bmad-text-cultural" style="text-align: center; font-weight: 600;">Tue</div>
        <div class="bmad-text-cultural" style="text-align: center; font-weight: 600;">Wed</div>
        <div class="bmad-text-cultural" style="text-align: center; font-weight: 600;">Thu</div>
        <div class="bmad-text-cultural" style="text-align: center; font-weight: 600;">Fri</div>
        
        <!-- Period 1 -->
        <div class="period-label">P1<br>9:00</div>
        <div class="class-slot" data-day="mon" data-period="1">
            <!-- KAMAR data fills here -->
            <div class="bmad-card" style="padding: var(--bmad-space-xs); background: linear-gradient(135deg, var(--bmad-earth-brown) 0%, var(--bmad-forest-green) 100%); color: white;">
                <strong>9MA1</strong><br>
                <small>Y9 Math | M15</small>
            </div>
        </div>
        <!-- ... more days for P1 -->
        
        <!-- Period 2, 3, 4, 5 ... -->
    </div>
    
    <!-- Linked Lessons (Drag & Drop in Future!) -->
    <div class="bmad-mt-md">
        <h3 class="bmad-text-cultural">📚 Lessons for This Week</h3>
        <!-- Show lessons that can be assigned to classes -->
    </div>
</div>

<script>
// Load KAMAR timetable data
async function loadWeeklyPlanner() {
    const { data, error } = await supabase
        .from('kamar_timetable')
        .select('*')
        .eq('teacher_id', currentUser.id)
        .order('day_of_week', { ascending: true })
        .order('period', { ascending: true });
    
    if (error) {
        console.error('KAMAR data load failed:', error);
        return;
    }
    
    // Populate grid with timetable
    renderTimetableGrid(data);
}
</script>
```

---

#### **Days 11-12: Teacher Dashboard Integration**

**Tasks:**
- [ ] Add weekly planner to teacher dashboard
- [ ] Link from sidebar "Weekly Planner" menu item
- [ ] Show today's classes prominently
- [ ] Next class countdown

---

#### **Days 13-14: Testing & Deployment**

**Tasks:**
- [ ] Test with Mangakōtukutuku College sandbox (if available)
- [ ] Test with mock data (if no sandbox)
- [ ] Error handling implementation
- [ ] Logging & monitoring setup
- [ ] Production deployment
- [ ] Remove "Soon" badge from sidebar link!

---

## 🚨 RISKS & MITIGATION

### **Risk 1: No KAMAR API Access**
**Mitigation:** Use manual CSV import as fallback
```javascript
// Allow manual timetable upload
async function uploadTimetableCSV(file) {
  // Parse CSV
  // Transform to schema
  // Insert to kamar_timetable
}
```

### **Risk 2: XML Parsing Complexity**
**Mitigation:** Use `xml2js` library
```bash
npm install xml2js
```

### **Risk 3: Privacy Act 2020 Compliance**
**Mitigation:**
- Data minimization (only timetable needed)
- Secure storage (Supabase RLS)
- School consent required
- Breach disclosure protocols ready

---

## 🎯 SUCCESS CRITERIA

**Week 1 Complete When:**
- ✅ Webhook listener deployed
- ✅ Database schema created
- ✅ XML/JSON parsing working
- ✅ Test data successfully synced

**Week 2 Complete When:**
- ✅ Weekly planner UI functional
- ✅ Shows KAMAR timetable data
- ✅ Integrated in teacher dashboard
- ✅ Linked from sidebar
- ✅ "Soon" badge removed!

**KAMAR Integration Complete When:**
- ✅ Timetable auto-syncs (nightly + real-time)
- ✅ Teachers see their actual classes
- ✅ Weekly planner populated
- ✅ Sidebar professional tools unblocked!

---

## 💎 VALUE UNLOCKED

**When KAMAR Complete:**
- Weekly Planner: FUNCTIONAL! (was blocked)
- Teacher Sidebar: COMPLETE! (all tools working)
- Professional Workflow: EXCELLENT! (school integration)
- Teacher Experience: 90%+ (vs 50% without KAMAR)

**Value:** $30K integration + $50K+ tools enabled = $80K total!

---

## 📋 CRITICAL NEXT STEPS

### **Immediate (Day 1 - Tama Kōtahi):**
1. Contact KAMAR or Mangakōtukutuku IT for API docs
2. Set up Netlify Function structure
3. Create Supabase schema migration
4. Begin webhook listener code

### **Week 1 Focus:**
- Backend foundation solid
- Data transformation working
- Test with mock data

### **Week 2 Focus:**
- Frontend weekly planner UI
- Teacher dashboard integration
- Production deployment!

---

**Status:** ✅ IMPLEMENTATION PLAN READY  
**For:** Tama Kōtahi (Builder)  
**Timeline:** 2 weeks (Week 13-15)  
**Impact:** Unblocks $80K+ value!

**Kia kaha, Tama! Hei mahi!** *(Be strong, Tama! Let's work!)*

🔗🛠️🚀

**Start building, e hoa!**

