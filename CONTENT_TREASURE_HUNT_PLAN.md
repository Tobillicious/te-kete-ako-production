# Content Treasure Hunt Plan

**Date:** October 12, 2025  
**Purpose:** Uncover, organize, and integrate the massive amount of valuable content that's lost, duplicated, or not properly linked

---

## 🎯 CURRENT TREASURE MAP

### 1. Authentication System Conflicts
**Issue:** Multiple login/register pages causing confusion
- **Found:** 25 login.html files, 24 register.html files
- **Problem:** Duplicates across different sections (main, lessons, experiences)
- **Impact:** User confusion, inconsistent authentication experience

### 2. GraphRAG Issues
**Status:** Partially working but incomplete
- **Current:** 309 resources cataloged (out of 400+ HTML files)
- **Missing:** Units 1-7 lessons, Experience modules, YouTube Library
- **Relationships:** 90,635 relationships mapped but incomplete coverage

### 3. Unlinked Content
**Problem:** Amazing content not accessible through main navigation
- **Hidden Gems:** Content in subdirectories not linked from main site
- **Lost Resources:** Valuable educational materials buried in file structure
- **Orphaned Pages:** High-quality content with no inbound links

### 4. Backup Bloat
**Issue:** Multiple backup directories with duplicated content
- **Found:** 5+ backup directories with full site copies
- **Problem:** Storage waste, confusion about which version is current
- **Impact:** Difficult to maintain and update content

---

## 🗺️ TREASURE HUNTING STRATEGY

### Phase 1: Content Audit & Mapping (Week 1)

#### 1.1 Complete Content Inventory
```bash
# Find all HTML files
find public -name "*.html" | wc -l
find public -name "*.html" > complete-content-list.txt

# Identify duplicates
fdupes -r public/ > duplicate-files.txt

# Find orphaned files (no inbound links)
scripts/find-orphaned-content.py
```

#### 1.2 GraphRAG Completion
- **Scan remaining 100+ HTML files** not in GraphRAG
- **Add missing content categories:**
  - Units 1-7 lessons (50+ files)
  - Experience modules
  - YouTube Library system
  - Curriculum alignment pages
- **Fix GraphRAG issues** identified in documentation

#### 1.3 Authentication System Cleanup
- **Consolidate login/register pages** to single versions
- **Remove duplicates** from lessons/ and experiences/ subdirectories
- **Create unified authentication flow**
- **Implement redirects** from old URLs to new ones

### Phase 2: Content Recovery & Integration (Week 2)

#### 2.1 Uncover Hidden Gems
```bash
# Find content not linked from navigation
scripts/find-unlinked-content.py

# Identify high-value orphaned pages
scripts/analyze-content-value.py

# Create content linking plan
scripts/generate-linking-plan.py
```

#### 2.2 Content Quality Assessment
- **Evaluate each orphaned page** for educational value
- **Identify content to keep, merge, or remove**
- **Assess cultural appropriateness and curriculum alignment**
- **Prioritize content for integration**

#### 2.3 Link Building Strategy
- **Add navigation links** to valuable orphaned content
- **Create content hubs** for related materials
- **Implement breadcrumb trails** for better navigation
- **Add "Related Content" suggestions**

### Phase 3: Content Organization & Synthesis (Week 3)

#### 3.1 Content Deduplication
- **Identify duplicate content** across different sections
- **Merge complementary content** into comprehensive resources
- **Remove redundant versions** while preserving best elements
- **Create canonical URLs** for content

#### 3.2 Content Structure Optimization
- **Organize content by curriculum levels** (Years 7-13)
- **Group by learning areas** (English, Maths, Science, etc.)
- **Create logical content hierarchies**
- **Implement consistent naming conventions**

#### 3.3 Cross-Reference Enhancement
- **Link related content** across different units
- **Create learning pathways** for students
- **Add prerequisite relationships** between lessons
- **Implement "Next Steps" suggestions**

### Phase 4: System Cleanup & Optimization (Week 4)

#### 4.1 Backup Cleanup
- **Remove redundant backup directories**
- **Keep only essential backups** (last 3 versions)
- **Implement proper backup strategy**
- **Document backup procedures**

#### 4.2 GraphRAG Optimization
- **Complete GraphRAG scanning** of all content
- **Fix relationship mapping issues**
- **Optimize search functionality**
- **Implement content recommendations**

#### 4.3 Performance Optimization
- **Remove unused files and assets**
- **Optimize image sizes and formats**
- **Implement proper caching strategies**
- **Improve site loading speed**

---

## 💎 SPECIFIC TREASURE CATEGORIES

### 1. Educational Content Gold
- **Walker Unit Lessons** (5 comprehensive lessons)
- **Hērangi Unit Lessons** (5 comprehensive lessons)
- **Y8 Systems Unit** (Complete 5-week unit)
- **Mathematics Worksheets** (Multiple topics)
- **Cultural Handouts** (Te Reo Māori, Tikanga)

### 2. Interactive Resources
- **Te Reo Wordle** (Language learning game)
- **YouTube Educational Library** (1000+ hours)
- **Virtual Marae Experience** (Cultural immersion)
- **Interactive Literacy Tools** (Reading/writing aids)
- **Assessment Rubrics** (Multiple subjects)

### 3. Teacher Resources
- **Professional Development Materials**
- **Assessment Frameworks** (AsTTle-style)
- **Curriculum Alignment Documents**
- **Cultural Competency Resources**
- **Planning Templates** (Multiple formats)

### 4. Student Resources
- **Printable Worksheets** (Various subjects)
- **Learning Progression Guides**
- **Study Skills Materials**
- **Extension Activities** (Challenge content)
- **Reflection Templates** (Kolb/Gibbs models)

---

## 🔧 TOOLS & SCRIPTS NEEDED

### 1. Content Analysis Scripts
```python
# content-analyzer.py
- Analyze HTML files for content value
- Identify duplicates and similar content
- Assess curriculum alignment
- Evaluate cultural appropriateness

# link-checker.py
- Find broken internal links
- Identify orphaned pages
- Generate linking recommendations
- Validate URL structure

# content-organizer.py
- Organize content by curriculum level
- Group by learning areas
- Create content hierarchies
- Generate navigation structure
```

### 2. GraphRAG Enhancement Scripts
```python
# graphrag-expander.py
- Scan remaining HTML files
- Add missing content to GraphRAG
- Fix relationship mapping
- Optimize search functionality

# graphrag-optimizer.py
- Clean up GraphRAG database
- Remove duplicate entries
- Fix broken relationships
- Optimize performance
```

### 3. Cleanup Scripts
```python
# duplicate-remover.py
- Identify duplicate files
- Compare content similarity
- Remove redundant versions
- Create canonical URLs

# backup-cleaner.py
- Remove old backup directories
- Keep essential backups
- Organize backup structure
- Document backup procedures
```

---

## 📊 SUCCESS METRICS

### Content Organization Metrics
- **Duplicate Reduction:** Target 80% reduction in duplicate content
- **Orphaned Content Integration:** Target 95% of valuable content linked
- **Navigation Coverage:** Target 100% of content accessible within 3 clicks
- **GraphRAG Completion:** Target 100% of content catalogued

### User Experience Metrics
- **Search Success Rate:** Target 95% of searches find relevant content
- **Navigation Efficiency:** Target average time to find content < 10 seconds
- **Content Discoverability:** Target 90% of content discoverable through navigation
- **Authentication Success:** Target 100% successful login/registration flow

### System Performance Metrics
- **Site Speed:** Target <2 second page load times
- **Storage Efficiency:** Target 50% reduction in storage usage
- **Maintenance Efficiency:** Target 80% reduction in maintenance time
- **GraphRAG Performance:** Target <1 second search response times

---

## 🚀 IMPLEMENTATION ROADMAP

### Week 1: Audit & Mapping
- **Day 1-2:** Complete content inventory and duplicate analysis
- **Day 3-4:** GraphRAG completion and authentication cleanup
- **Day 5-7:** Content quality assessment and linking plan

### Week 2: Recovery & Integration
- **Day 1-3:** Uncover hidden gems and content recovery
- **Day 4-5:** Content quality assessment and prioritization
- **Day 6-7:** Link building and navigation enhancement

### Week 3: Organization & Synthesis
- **Day 1-3:** Content deduplication and merging
- **Day 4-5:** Content structure optimization
- **Day 6-7:** Cross-reference enhancement and pathway creation

### Week 4: Cleanup & Optimization
- **Day 1-2:** Backup cleanup and system optimization
- **Day 3-4:** GraphRAG optimization and performance tuning
- **Day 5-7:** Final testing and documentation

---

## 🔄 CONTINUOUS IMPROVEMENT

### Monitoring
- **Weekly content audits** to catch new duplicates
- **Monthly GraphRAG updates** to maintain coverage
- **Quarterly performance reviews** to ensure optimal performance
- **Annual content reviews** to maintain quality standards

### Maintenance
- **Automated duplicate detection** for new content
- **Regular link checking** to prevent broken links
- **Content freshness monitoring** to ensure relevance
- **User feedback collection** for continuous improvement

This treasure hunt plan will help uncover and organize the massive amount of valuable content in Te Kete Ako, ensuring that all the amazing educational materials are properly integrated and accessible to users.
