# 🎯 Header Improvements Plan

## ✅ TESTING RESULTS

Testing dropdowns and functionality...

---

## 💡 PROPOSED IMPROVEMENTS (User Requested)

### 1. CONSOLIDATE LOGIN/SIGNUP
**Current:**
- 🔐 Login / Takiuru
- 📝 Join / Hono Mai

**Proposed:**
- Single button: "Login / Sign Up" or "Takiuru / Rēhita"
- When logged in, replace with: "Dashboard / Papataka" or "My Kete / Tōku Kete"

### 2. ADD "MORE" DROPDOWN (Flotsam & Jetsam)
**Current scattered items:**
- ⚡ Do Nows
- 🎮 Games (has dropdown)
- YouTube (not in main nav)
- Curriculum (not in main nav)

**Proposed new structure:**
```
Main Nav:
- 📚 Unit Plans / Ngā Waehere (dropdown)
- 📖 Lesson Plans / Ngā Akoranga
- 📄 Handouts / Ngā Rauemi (dropdown)
- 🔗 More / Ētahi Atu (NEW DROPDOWN)
  - ⚡ Do Nows / Mahi Whakakā
  - 🎮 Games / Ngā Kēmu
  - 📺 YouTube
  - 📋 Curriculum / Marautanga
  - [other useful stuff]
- 🔐 Login/Sign Up (or Dashboard when logged in)
```

### 3. AUTH STATE LOGIC
**When NOT logged in:**
- Show: "Login / Sign Up" button
- Clicks opens login page with option to register

**When logged in:**
- Show: "Dashboard" or "My Kete" button
- Links to personalized dashboard

---

## 📋 SPECIFIC CHANGES NEEDED

### index.html modifications:

1. **Merge Login/Join:**
```html
<!-- OLD (remove these two) -->
<li class="auth-nav">
    <a href="login.html" class="login-btn">
        <span class="nav-icon">🔐</span>
        <span class="nav-text-en">Login</span>
        <span class="nav-text-mi" lang="mi">Takiuru</span>
    </a>
</li>
<li class="auth-nav">
    <a href="register-simple.html" class="register-btn">
        <span class="nav-icon">📝</span>
        <span class="nav-text-en">Join</span>
        <span class="nav-text-mi" lang="mi">Hono Mai</span>
    </a>
</li>

<!-- NEW (add single button) -->
<li class="auth-nav auth-logged-out">
    <a href="login.html" class="auth-btn">
        <span class="nav-icon">🔐</span>
        <span class="nav-text-en">Login / Sign Up</span>
        <span class="nav-text-mi" lang="mi">Takiuru / Rēhita</span>
    </a>
</li>
<li class="auth-nav auth-logged-in" style="display: none;">
    <a href="my-kete.html" class="dashboard-btn">
        <span class="nav-icon">🧺</span>
        <span class="nav-text-en">My Kete</span>
        <span class="nav-text-mi" lang="mi">Tōku Kete</span>
    </a>
</li>
```

2. **Add "More" dropdown:**
```html
<li>
    <a href="#more">
        <span class="nav-icon">🔗</span>
        <span class="nav-text-en">More</span>
        <span class="nav-text-mi" lang="mi">Ētahi Atu</span>
    </a>
    <div class="nav-dropdown">
        <ul>
            <li><a href="activities.html">⚡ Do Nows / Mahi Whakakā</a></li>
            <li><a href="games.html">🎮 Games / Ngā Kēmu</a></li>
            <li><a href="youtube.html">📺 YouTube</a></li>
            <li><a href="curriculum-alignment.html">📋 Curriculum / Marautanga</a></li>
            <li><a href="other-resources.html">🔗 Other Resources / Ētahi Atu Rauemi</a></li>
        </ul>
    </div>
</li>
```

3. **Remove standalone items:**
- Remove ⚡ Do Nows from main nav (move to More dropdown)
- Remove 🎮 Games dropdown from main nav (move to More dropdown, simplified)

---

## 🎨 CLEANER NAVIGATION

**BEFORE (6 items + auth):**
📚 Unit Plans | 📖 Lessons | 📄 Handouts | ⚡ Do Nows | 🎮 Games | 🔐 Login | 📝 Join

**AFTER (4 items + auth):**
📚 Unit Plans | 📖 Lessons | 📄 Handouts | 🔗 More | 🔐 Login/Sign Up

**Benefits:**
- ✅ Less cluttered
- ✅ Easier to scan
- ✅ Everything still accessible
- ✅ More scalable (can add more to "More" dropdown)
- ✅ Single auth button (cleaner UX)

---

## ❓ QUESTIONS FOR USER

1. **"More" dropdown name:** 
   - "More" / "Ētahi Atu"?
   - "Resources" / "Ngā Rauemi"?
   - Something else?

2. **When logged in, show:**
   - "My Kete" / "Tōku Kete"?
   - "Dashboard" / "Papataka"?
   - Something else?

3. **Should I implement this now or wait for more feedback?**

