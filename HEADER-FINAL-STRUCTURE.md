# 🎯 FINAL HEADER STRUCTURE - Option A

## 📋 NAVIGATION (User Approved!)

```
📚 Teaching Resources / Ngā Rauemi Whakaako
  ├─ Units (6-8 weeks)
  ├─ Lessons (60-75 min)
  └─ Handouts & Materials

📊 By Subject / Mā te Marau
  ├─ English / Reo Pākehā
  ├─ Math / Pāngarau
  ├─ Social Studies / Tikanga-ā-iwi
  ├─ Te Reo Māori
  └─ Science / Pūtaiao

🎓 By Year Level / Mā te Taumata
  ├─ Year 7
  ├─ Year 8
  └─ Year 9+

🔗 More / Ētahi Atu
  ├─ Games / Ngā Kēmu
  ├─ YouTube
  ├─ Curriculum / Marautanga
  └─ Other Resources

🔐 Login/Sign Up / Takiuru / Rēhita
  (→ My Kete / Tōku Kete when logged in)
```

---

## 📝 IMPLEMENTATION DETAILS

### 1. Teaching Resources Dropdown
```html
<li>
    <a href="browse.html">
        <span class="nav-icon">📚</span>
        <span class="nav-text-en">Teaching Resources</span>
        <span class="nav-text-mi" lang="mi">Ngā Rauemi Whakaako</span>
    </a>
    <div class="nav-dropdown">
        <ul>
            <li><a href="unit-plans.html">📚 Unit Plans (6-8 weeks)</a></li>
            <li><a href="lessons.html">📖 Lesson Plans (60-75 min)</a></li>
            <li><a href="handouts.html">📄 Handouts & Materials</a></li>
            <li><a href="browse.html">→ Browse All Resources</a></li>
        </ul>
    </div>
</li>
```

### 2. By Subject Dropdown
```html
<li>
    <a href="browse.html?filter=subject">
        <span class="nav-icon">📊</span>
        <span class="nav-text-en">By Subject</span>
        <span class="nav-text-mi" lang="mi">Mā te Marau</span>
    </a>
    <div class="nav-dropdown">
        <ul>
            <li><a href="browse.html?subject=english">📝 English / Reo Pākehā</a></li>
            <li><a href="browse.html?subject=math">🔢 Math / Pāngarau</a></li>
            <li><a href="browse.html?subject=social-studies">🌏 Social Studies / Tikanga-ā-iwi</a></li>
            <li><a href="browse.html?subject=te-reo">🌿 Te Reo Māori</a></li>
            <li><a href="browse.html?subject=science">🔬 Science / Pūtaiao</a></li>
        </ul>
    </div>
</li>
```

### 3. By Year Level Dropdown
```html
<li>
    <a href="browse.html?filter=year">
        <span class="nav-icon">🎓</span>
        <span class="nav-text-en">By Year Level</span>
        <span class="nav-text-mi" lang="mi">Mā te Taumata</span>
    </a>
    <div class="nav-dropdown">
        <ul>
            <li><a href="browse.html?year=7">📘 Year 7</a></li>
            <li><a href="browse.html?year=8">📗 Year 8</a></li>
            <li><a href="browse.html?year=9">📙 Year 9+</a></li>
        </ul>
    </div>
</li>
```

### 4. More Dropdown (unchanged)
```html
<li>
    <a href="#more">
        <span class="nav-icon">🔗</span>
        <span class="nav-text-en">More</span>
        <span class="nav-text-mi" lang="mi">Ētahi Atu</span>
    </a>
    <div class="nav-dropdown">
        <ul>
            <li><a href="games.html">🎮 Games / Ngā Kēmu</a></li>
            <li><a href="youtube.html">📺 YouTube</a></li>
            <li><a href="curriculum-alignment.html">📋 Curriculum / Marautanga</a></li>
            <li><a href="other-resources.html">🔗 Other Resources</a></li>
        </ul>
    </div>
</li>
```

### 5. Auth Button (unchanged)
```html
<!-- When logged out -->
<li class="auth-nav auth-logged-out">
    <a href="login.html" class="auth-btn">
        <span class="nav-icon">🔐</span>
        <span class="nav-text-en">Login / Sign Up</span>
        <span class="nav-text-mi" lang="mi">Takiuru / Rēhita</span>
    </a>
</li>

<!-- When logged in (hidden by default) -->
<li class="auth-nav auth-logged-in" style="display: none;">
    <a href="my-kete.html" class="dashboard-btn">
        <span class="nav-icon">🧺</span>
        <span class="nav-text-en">My Kete</span>
        <span class="nav-text-mi" lang="mi">Tōku Kete</span>
    </a>
</li>
```

---

## 📊 FINAL HEADER (5 items)

**Desktop view:**
```
🧺 Te Kete Ako  |  📚 Teaching Resources  |  📊 By Subject  |  🎓 By Year  |  🔗 More  |  🔐 Login/Sign Up
```

**Mobile view (icons only):**
```
🧺  |  📚  |  📊  |  🎓  |  🔗  |  🔐
```

---

## ✅ BENEFITS

- ✅ Honors hierarchy (Units → Lessons → Handouts)
- ✅ Multiple ways to find content (by type, subject, OR year)
- ✅ Teachers can think "I teach Year 8 Math" → click Year 8 or Math
- ✅ Clean header (5 items, not overwhelming)
- ✅ Fully bilingual
- ✅ Scalable (add more subjects/years easily)
- ✅ Professional organization

---

## 🚀 READY TO IMPLEMENT?

This will:
1. Replace current nav structure
2. All dropdowns work the same way
3. Links go to browse.html with filters (or direct pages)
4. Auth state logic ready

Approve to proceed?

