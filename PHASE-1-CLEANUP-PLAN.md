# 🧹 PHASE 1: DELETE THE GARBAGE

## Files to DELETE (AI Slop + Duplicates)

### 1. Transformation Hype Docs (Created Today - DELETE ALL)
```
🎊-TRANSFORMATION-COMPLETE.md
SESSION-SUMMARY-OCT26-EVENING.md
CLOUDFLARE-STEP-BY-STEP-FOR-YOU.md
FREE-TOOLS-SETUP-GUIDE.md
🚀-PROFESSIONAL-SAAS-TRANSFORMATION.md
DEPLOYMENT-AND-TESTING-CHECKLIST.md
POSTHOG-ANALYTICS-GUIDE.md
BETA-TESTING-INVITATION-TEMPLATE.md
WEEKLY-FEEDBACK-ITERATION-PROCESS.md
🧪-USER-FLOW-SIMULATION-RESULTS.md
```

### 2. Dashboard Duplicates (Keep 1 per role, delete rest)
**KEEP:**
- `/app/teacher-dashboard.html` (rename from teacher-dashboard-personalized.html)
- `/app/student-dashboard.html` (the good one)
- `/app/admin-dashboard.html` (school-admin-dashboard.html)

**DELETE:**
```
teacher-dashboard-ai.html
teacher-dashboard-unified.html
teacher-demo-dashboard.html
teacher-insights-dashboard.html
professional-dashboard.html
dashboard.html (generic)
analytics-dashboard.html
performance-dashboard.html
discovery-dashboard.html
subject-dashboard.html
subject-excellence-dashboard.html
cultural-excellence-dashboard.html
enterprise-admin-dashboard.html
kamar-integration-dashboard.html
agent-coordination-dashboard.html
ai-coordination-dashboard.html
agent-intelligence-dashboard.html
graphrag-analytics-dashboard.html
graphrag-optimization-dashboard.html
agent-dashboard.html
agent-workload-dashboard.html (admin/)
task-queue-dashboard.html (admin/)
orchestration-test-suite.html (admin/)
```

### 3. Generic Template Pages (No Real Data)
```
ai-lesson-planner.html (empty form, no backend)
ai-image-generator.html (empty form)
ai-pronunciation-guide.html (empty form)
my-classes.html (fake data)
my-learning.html (fake data)
my-achievements.html (fake data)
teacher-progress-tracking.html (fake data)
subscription-dashboard.html (no Stripe integration)
pricing-professional.html (duplicate of pricing.html)
```

### 4. Duplicate Index/Hub Pages
```
index-backup.html
index-new.html
index-premium.html
index-saas-landing.html
index-simple.html
index-bloated-backup.html
index-BROKEN-BACKUP.html
lessons.html.hub
lessons.html.hub-backup
handouts.html.hub
handouts.html.hub-backup
resource-hub.html.hub
resource-hub.html.hub-backup
curriculum-index.html.hub
curriculum-index.html.hub-backup
```

### 5. Old Navigation/Test Files
```
navigation_fix_standard_header.html
navigation-header.html.OLD
index-backup-old-complex.html
index-west-coast-demo.html
cache-bust-test.html
cache-test.html
auth-test.html
auth-diagnostics.html
auth-testing-dashboard.html
deepseek-agent-test.html
test-ux-verification.html
interactive-learning-demo.html
```

### 6. GraphRAG Admin Clutter (Move to /admin/graphrag/)
These are already in `/admin/` but there's duplicates in root:
```
graphrag-hub.html (root - DELETE, keep /admin/ version)
graphrag-explorer.html (root)
graphrag-control-center.html (root)
graphrag-brain-hub.html (root)
graphrag-discovery-hub.html (root)
graphrag-teacher-dashboard.html (root)
graphrag-query-dashboard.html (root)
graphrag-science-dashboard.html (root)
graphrag-pathway-explorer.html (root)
```

### 7. Orphaned/Duplicate Features
```
my-kete.html (use my-kete-enhanced.html OR my-kete-guest.html)
teacher-dashboard.html (old version, keep personalized)
student-dashboard.html (check which is better)
signup-teacher.html (use register.html with role detection)
signup-student.html (use register.html)
login-simple.html (use login.html)
register-simple.html (use register.html)
```

## Python Script Strategy

Create `cleanup-phase-1.py` that:
1. Lists all files to delete (for review)
2. Moves to `/archive/` instead of deleting (safety!)
3. Updates GraphRAG to mark as archived
4. Generates report of what was moved

## Expected Result

**Before:** 329 HTML files in `/public/`
**After:** ~50 essential HTML files in `/public/root`
**Archived:** ~280 files safely stored

---

## Next: Phase 2 will ORGANIZE the keepers into proper structure

