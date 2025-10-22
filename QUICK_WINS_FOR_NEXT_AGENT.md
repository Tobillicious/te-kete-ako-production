# 🎯 Quick Wins for Next Agent

**Goal:** Get impactful results in your first 30-60 minutes!

---

## ⚡ 15-MINUTE WIN: Enhance Science Hub

**What:** Add "Browse Science Teaching Variants" section to Science Hub  
**Why:** Science has 220+ resources, it's a major subject hub  
**Impact:** Immediate teacher value, showcases variant system  
**Difficulty:** Easy (copy-paste pattern)

### Steps:

1. **Open** `/public/science-hub.html`

2. **Find** the Quick Start section (search for "Quick Start: Teacher Picks")

3. **Add this AFTER the Quick Start section:**

```html
<!-- 🔍 Browse Science Teaching Variants -->
<section style="max-width: 1100px; margin: 2rem auto; padding: 0 2rem;">
    <div style="background: white; padding: 3rem; border-radius: 20px; box-shadow: 0 4px 20px rgba(0,0,0,0.08);">
        <div style="text-align: center; margin-bottom: 2.5rem;">
            <div style="background: #0284c7; color: white; padding: 0.75rem 1.5rem; border-radius: 24px; display: inline-block; font-weight: 800; margin-bottom: 1rem;">
                🔬 TEACHING VARIANTS BROWSER
            </div>
            <h2 style="font-size: 2.5rem; color: #1a4d2e; margin-bottom: 1rem;">
                Browse Science Teaching Variants
            </h2>
            <p style="font-size: 1.15rem; color: #666; max-width: 800px; margin: 0 auto;">
                Explore our complete collection of Science resources with intelligent filtering.
            </p>
        </div>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem;">
            
            <!-- Card 1: Dual Cultural -->
            <a href="/all-teaching-variants-browser.html?subject=Science&cultural=dual" 
               style="background: linear-gradient(135deg, #d1fae5, #a7f3d0); padding: 2rem; border-radius: 16px; text-decoration: none; transition: all 0.3s; box-shadow: 0 2px 12px rgba(0,0,0,0.06); display: block;"
               onmouseover="this.style.transform='translateY(-4px)'"
               onmouseout="this.style.transform='translateY(0)'">
                <div style="font-size: 2.5rem; margin-bottom: 1rem;">🌿🌿</div>
                <h3 style="color: #047857; margin-bottom: 0.75rem; font-weight: 800; font-size: 1.3rem;">
                    Dual Cultural (+12.2 Quality!)
                </h3>
                <p style="color: #065f46; margin-bottom: 1rem;">
                    Resources with Te Reo + Whakataukī
                </p>
            </a>

            <!-- Card 2: Excellence -->
            <a href="/all-teaching-variants-browser.html?subject=Science&quality=90"
               style="background: linear-gradient(135deg, #dbeafe, #bfdbfe); padding: 2rem; border-radius: 16px; text-decoration: none; transition: all 0.3s; box-shadow: 0 2px 12px rgba(0,0,0,0.06); display: block;"
               onmouseover="this.style.transform='translateY(-4px)'"
               onmouseout="this.style.transform='translateY(0)'">
                <div style="font-size: 2.5rem; margin-bottom: 1rem;">⭐</div>
                <h3 style="color: #0369a1; margin-bottom: 0.75rem; font-weight: 800; font-size: 1.3rem;">
                    Excellence (Q90+)
                </h3>
                <p style="color: #075985; margin-bottom: 1rem;">
                    Gold standard Science resources
                </p>
            </a>

            <!-- Card 3: CSS Backup -->
            <a href="/all-teaching-variants-browser.html?subject=Science&location=css_backup"
               style="background: linear-gradient(135deg, #ede9fe, #ddd6fe); padding: 2rem; border-radius: 16px; text-decoration: none; transition: all 0.3s; box-shadow: 0 2px 12px rgba(0,0,0,0.06); display: block;"
               onmouseover="this.style.transform='translateY(-4px)'"
               onmouseout="this.style.transform='translateY(0)'">
                <div style="font-size: 2.5rem; margin-bottom: 1rem;">🎨</div>
                <h3 style="color: #7c3aed; margin-bottom: 0.75rem; font-weight: 800; font-size: 1.3rem;">
                    CSS Migration (Q92)
                </h3>
                <p style="color: #6b21a8; margin-bottom: 1rem;">
                    Original design, print-friendly
                </p>
            </a>

            <!-- Card 4: All Variants -->
            <a href="/all-teaching-variants-browser.html?subject=Science"
               style="background: linear-gradient(135deg, #1a4d2e, #0f2818); padding: 2rem; border-radius: 16px; text-decoration: none; transition: all 0.3s; box-shadow: 0 4px 16px rgba(26,77,46,0.3); display: block; color: white; text-align: center;"
               onmouseover="this.style.transform='translateY(-4px)'"
               onmouseout="this.style.transform='translateY(0)'">
                <div style="font-size: 2.5rem; margin-bottom: 1rem;">🔍</div>
                <h3 style="margin-bottom: 0.75rem; font-weight: 800; font-size: 1.3rem;">
                    All Science Variants
                </h3>
                <p style="opacity: 0.95; margin-bottom: 1rem;">
                    Browse with advanced filters
                </p>
            </a>

        </div>
    </div>
</section>
```

4. **Test:** Open `/science-hub.html` in browser, verify section appears and links work

**Time:** 15 minutes  
**Impact:** HIGH - Science is a major subject  
**Difficulty:** ★☆☆☆☆

---

## ⚡ 30-MINUTE WIN: Enhance 3 More Hubs

**What:** Add "Browse Variants" to English, Social Studies, Digital Tech hubs  
**Why:** Cover 4 of the top 6 subjects (50%+ of teachers)  
**Impact:** Massive reach  
**Difficulty:** Easy (repeat Science pattern 3x)

### Pattern:

For **each hub** (`english-hub.html`, `social-studies-hub.html`, `digital-technologies-hub.html`):

1. Copy the entire section from Science Hub (see above)
2. Change these 4 values:
   - Icon: 🔬 → 📝 (English), 🏛️ (Social Studies), 💻 (Digital Tech)
   - Title: "Science" → "English" / "Social Studies" / "Digital Technologies"
   - URL parameter: `?subject=Science` → `?subject=English` / `?subject=Social Studies` / `?subject=Digital Technologies`
   - Header background color (optional): Keep #0284c7 or customize

3. Insert after Quick Start section (or at top of main content)

**Time:** 30 minutes (10 min per hub)  
**Impact:** MASSIVE - 4/6 major subjects covered  
**Difficulty:** ★☆☆☆☆

---

## ⚡ 60-MINUTE WIN: Y9 Ecology Variant Cards (Partial)

**What:** Create Y9 Ecology unit page with variant cards for Lessons 1-3  
**Why:** Y9 Ecology is a flagship unit (6 lessons, confidence 1.0)  
**Impact:** Another complete unit showcase  
**Difficulty:** Medium (copy Y7 Algebra pattern, customize)

### Steps:

1. **Copy** `/public/units/y7-maths-algebra/index-with-variants.html`

2. **Save as** `/public/units/y9-science-ecology/index-with-variants.html`

3. **Update header:**
   - Title: "Year 9 Science: Ecology & Kaitiakitanga"
   - Subtitle: "Understanding Ecosystems Through Guardianship"
   - Stats: "6 lessons", "3-4 weeks", "Q92"
   - Colors: Change maths blue (#3b82f6) to ecology green (#10b981)

4. **Query GraphRAG for Y9 Ecology lessons:**

```sql
SELECT file_path, title, quality_score, has_te_reo, has_whakataukī
FROM graphrag_resources
WHERE file_path LIKE '%y9%ecology%'
  AND resource_type = 'Lesson'
  AND quality_score >= 75
ORDER BY file_path, quality_score DESC;
```

5. **Create variant cards for Lesson 1-3** (manually)
   - Use the pattern from Y7 Algebra
   - 2 variants per lesson minimum:
     - Enhanced Gold Standard (active site)
     - Legacy CSS (backup folder)

6. **Add unit overview:**
   - Learning outcomes (ecosystems, food webs, kaitiakitanga, biodiversity)
   - Unit structure (3 phases if applicable, or linear 6-lesson flow)

7. **Link resources:**
   - Ecosystem wordsearch (`/units/y9-science-ecology/resources/wordsearch-ecosystem-nyt.html`)
   - Handouts folder
   - Assessment rubrics

**Time:** 60 minutes (full 6 lessons = 2-3 hours, so do 3 lessons now)  
**Impact:** HIGH - Another flagship unit  
**Difficulty:** ★★★☆☆

---

## 🎯 PRIORITY ORDER

**If you only have 1 hour:**
1. ✅ Science Hub (15 min)
2. ✅ English Hub (10 min)
3. ✅ Social Studies Hub (10 min)
4. ✅ Digital Tech Hub (10 min)
5. ✅ Y9 Ecology Lessons 1-3 (60 min remaining = partial)

**Total:** 4 hubs enhanced + 1 partial unit = HUGE IMPACT! 🚀

---

## 📊 EXPECTED RESULTS

**After 1 hour:**
- 4 subject hubs with "Browse Variants" sections
- 50%+ of teachers can discover variants via their subject hub
- Y9 Ecology partially implemented (foundation for completion)
- Variant system visible across major subjects

**Teacher experience:**
- Visit Science Hub → See "Browse Variants" → Click "Excellence (Q90+)" → Filter variants browser → Find high-quality lesson
- **Value delivered!** ✅

---

## 🆘 IF YOU GET STUCK

**Issue: Can't find where to insert section in hub file**

**Solution:** Look for these patterns and insert AFTER them:
- "Quick Start: Teacher Picks"
- "Featured Picks"
- "Recently Added"
- Or insert at the TOP of `<main>` element

---

**Issue: Variant links return 404**

**Solution:** Check GraphRAG for actual file paths:
```sql
SELECT file_path FROM graphrag_resources 
WHERE canonical_subject = 'YourSubject'
LIMIT 5;
```

Then verify those paths exist in filesystem. If in backup folder, paths start with `/backup_before_css_migration/` or `/backups/css-standardize-...`

---

**Issue: Don't know which lessons to include for Y9 Ecology**

**Solution:** Check `/units-inventory.json` or query GraphRAG:
```sql
SELECT DISTINCT file_path, title FROM graphrag_resources
WHERE file_path LIKE '%y9%ecology%'
  AND resource_type = 'Lesson'
ORDER BY file_path;
```

Then pick the top 6 by quality_score.

---

## 💡 PRO TIPS

1. **Use search-replace tool** for bulk text changes (Subject name, colors)
2. **Test in browser** after each hub (don't do all 4 then test)
3. **Check existing implementations** if confused (Y7 Algebra, Mathematics Hub)
4. **Query GraphRAG first** before hardcoding links (verify paths exist)
5. **Commit after each hub** with clear message: "feat: Add Browse Variants to Science Hub"

---

## ✅ DONE CRITERIA

**For each hub:**
- [ ] "Browse Variants" section visible on page
- [ ] 4 filter cards present (Dual Cultural, Excellence, CSS Backup, All)
- [ ] All 4 links work and open variants browser with correct filter
- [ ] Section has proper styling (matches Mathematics Hub pattern)
- [ ] No linter errors introduced

**For Y9 Ecology:**
- [ ] Header shows correct stats (6 lessons, 3-4 weeks, Q92)
- [ ] Unit overview explains learning outcomes
- [ ] Lessons 1-3 have 2+ variant cards each
- [ ] Each variant card has distinct blurb
- [ ] Links point to real files (tested in browser)
- [ ] Resources section links to handouts/wordsearch

---

**Now go make an impact! You got this! 💪**

