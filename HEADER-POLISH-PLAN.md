# 🎨 Header Polish Plan - Te Kete Ako

## 🔍 CURRENT ANALYSIS

**index.html (simpler) - BETTER foundation but needs:**
- ✅ Clean, stable layout
- ✅ No sizing issues
- ✅ Logo doesn't move
- ❌ Missing bilingual navigation
- ❌ Could use dropdown menus for some items

**lessons.html (feature-rich) - HAS PROBLEMS:**
- ❌ Search bumps into title
- ❌ Things go off edge
- ❌ Hover tooltips disappear behind content
- ❌ Too crowded
- ✅ Bilingual navigation (good!)
- ✅ More features (but maybe too many)

---

## 🎯 THE PERFECT HEADER (Proposal)

**STRUCTURE:**
```
┌─────────────────────────────────────────────────────────────┐
│  🧺 Te Kete Ako     [Nav Items]           [Login] [Join]    │
└─────────────────────────────────────────────────────────────┘
```

**LEFT SIDE:**
- Logo: 🧺 Te Kete Ako (or SVG logo)

**CENTER/RIGHT:**
- Unit Plans (with dropdown)
- Lesson Plans
- Handouts (with dropdown)
- Games
- Login
- Join

**FEATURES TO ADD:**
1. ✅ Bilingual navigation (English + Te Reo Māori)
2. ✅ Dropdown menus for Unit Plans & Handouts
3. ✅ Responsive collapse to icons on mobile

**FEATURES TO REMOVE/RELOCATE:**
1. ❌ Search bar (move to sidebar or dedicated search page)
2. ❌ Generate button (move to its own page)
3. ❌ Hierarchy button (move to sidebar or content area)
4. ❌ Notification bell (add later when needed)

---

## 🛠️ PROPOSED CHANGES

### 1. Start with index.html header as base
### 2. Add bilingual navigation
### 3. Add dropdown menus (Unit Plans, Handouts)
### 4. Polish spacing and hover states
### 5. Fix z-index for dropdowns
### 6. Create proper logo (SVG or better emoji solution)

---

## 📋 NAVIGATION ITEMS (Final)

**Main Header:**
- 📚 Unit Plans / Ngā Waehere (with dropdown)
- 📖 Lesson Plans / Ngā Akoranga
- 📄 Handouts / Ngā Rauemi (with dropdown)
- 🎮 Games / Ngā Kēmu
- 🔐 Login / Takiuru
- 📝 Join / Hono Mai

**Dropdowns (Unit Plans):**
- Te Ao Māori Foundation
- Systems Unit (Y8)
- Economic Justice
- Global Connections
- Future Rangatiratanga

**Dropdowns (Handouts):**
- PEEL Method Toolkit
- Understanding Haka
- Treaty of Waitangi
- Media Literacy
- Probability & Statistics
- View All Handouts →

---

## 🎨 POLISH DETAILS

**Logo:**
- Replace emoji with proper SVG (or keep emoji if it renders well)
- Consistent sizing across browsers

**Spacing:**
- More breathing room between nav items
- Proper padding top/bottom

**Hover States:**
- Smooth color transitions
- Dropdowns appear smoothly
- Fix z-index so dropdowns appear ABOVE content

**Mobile:**
- Collapse to icons only on mobile (<768px)
- Hamburger menu option? (or keep icon-only)

**Typography:**
- Bold English text
- Italic, smaller Te Reo Māori text
- Good contrast

---

## ✅ APPROVAL NEEDED

Does this plan make sense?
Should I implement it on index.html first, then standardize?

