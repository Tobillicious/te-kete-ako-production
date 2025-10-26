# 📐 UNIT BROWSER - Excellence Design

**Tech Stack:** Next.js 14 + React + Framer Motion + Radix UI + Tailwind

**Philosophy:** Fast filtering, beautiful display, quality first.

---

## 🎯 **THE PERFECT UNIT BROWSER**

### **Layout (Desktop):**

```
┌─────────────────────────────────────────────────────────────┐
│ UNITS                                     654 total          │
└─────────────────────────────────────────────────────────────┘
│                                                             │
│ SMART FILTERS (Horizontal chips - instant filtering)        │
│ ┌───────────────────────────────────────────────────────┐   │
│ │ Year: [7] [8] [9] [10] [11-13] [All]                 │   │
│ │ Subject: [Math] [Science] [English] ... [All]         │   │
│ │ Quality: [90+ Gold] [All]                             │   │
│ │                                           23 results   │   │
│ └───────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
│                                                             │
│ MASONRY GRID (Pinterest-style, gorgeous)                    │
│ ┌────────────┐  ┌────────────┐  ┌────────────┐            │
│ │            │  │            │  │            │            │
│ │ Y8 Algebra │  │ Y9 Ecology │  │ Y7 Digital │            │
│ │            │  │            │  │ Tech       │            │
│ │ 12 lessons │  │ 18 lessons │  │            │            │
│ │ 🌟🌟🌟🌟🌟 │  │ 🌟🌟🌟🌟🌟 │  │ 6 lessons  │            │
│ │            │  │            │  │ 🌟🌟🌟🌟   │            │
│ │ [Preview]  │  │ [Preview]  │  │            │            │
│ │            │  │            │  │ [Preview]  │            │
│ └────────────┘  └────────────┘  └────────────┘            │
│                                                             │
│ [... beautiful grid, NO PAGINATION, filtered results only]  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## ⚡ **HOW IT WORKS (Next.js Magic)**

### **1. Server-Side Rendering (INSTANT LOAD)**
```tsx
// app/units/page.tsx
export default async function UnitsPage({ searchParams }) {
  // Pre-filter on server (instant!)
  const units = await getUnits({
    year: searchParams.year || 'all',
    subject: searchParams.subject || 'all',
    qualityMin: 90, // Default: show gold only
  })
  
  // Render instantly (no loading spinner!)
  return <UnitsGrid units={units} />
}
```

### **2. Client-Side Filtering (INSTANT RESPONSE)**
```tsx
// Click filter → instant re-filter, no server round-trip
function FilterChips({ allUnits }) {
  const [filtered, setFiltered] = useState(allUnits)
  
  function filterByYear(year) {
    // Instant! No loading, no API call
    setFiltered(allUnits.filter(u => u.year === year))
  }
  
  return (
    <Chips>
      <Chip onClick={() => filterByYear(8)}>Year 8</Chip>
      {/* Instant filtering! */}
    </Chips>
  )
}
```

### **3. Beautiful Masonry Grid (React Masonry)**
```tsx
import Masonry from 'react-masonry-css'

<Masonry
  breakpointCols={{ default: 4, 1280: 3, 768: 2, 640: 1 }}
  className="masonry-grid"
>
  {filtered.map(unit => (
    <UnitCard
      key={unit.id}
      unit={unit}
      onHover={showPreview} // Tooltip preview!
    />
  ))}
</Masonry>
```

### **4. Smooth Animations (Framer Motion)**
```tsx
<motion.div
  layout // Smooth reflow when filters change!
  initial={{ opacity: 0, y: 20 }}
  animate={{ opacity: 1, y: 0 }}
  exit={{ opacity: 0, y: -20 }}
>
  <UnitCard {...unit} />
</motion.div>
```

---

## 🎨 **UNIT CARD - Beautiful Design**

```tsx
<Card className="group hover:shadow-xl transition-all">
  {/* Thumbnail (if exists) */}
  <CardImage src={unit.thumbnail} />
  
  {/* Quality badge (top-right) */}
  <QualityBadge score={unit.quality}>
    🌟🌟🌟🌟🌟
  </QualityBadge>
  
  {/* Content */}
  <CardHeader>
    <CardTitle className="font-display text-pounamu-800">
      {unit.title}
    </CardTitle>
    <CardMeta className="text-neutral-600">
      Year {unit.year} • {unit.subject} • {unit.lessonCount} lessons
    </CardMeta>
  </CardHeader>
  
  {/* Cultural badge (if 100% cultural) */}
  {unit.culturalContext && (
    <Badge variant="cultural">🌿 Culturally Integrated</Badge>
  )}
  
  {/* Hover preview */}
  <CardFooter className="opacity-0 group-hover:opacity-100">
    <Button size="sm" variant="ghost">
      Preview →
    </Button>
  </CardFooter>
</Card>
```

---

## 🎯 **FILTER STRATEGY - My Recommendation**

### **Default View (Quality First):**
- **Show:** 90+ quality only (621 gold resources)
- **Why:** Teachers want best resources first
- **Toggle:** "Show all quality levels" checkbox

### **Smart Filters (Additive):**
```
Year: [All] [7] [8] [9] [10] [11-13]
      ↓
Subject: [All] [Math] [Science] [English] [Te Reo] ...
         ↓
Quality: [90+ Gold] [80+ Silver] [All]
```

**Each filter narrows results:**
- No filter: 621 gold units
- Year 8: 150 gold units (for example)
- Year 8 + Math: 23 gold units
- Year 8 + Math + All quality: 45 total units

**Results update instantly** (client-side, smooth animations)

### **Visual Feedback:**
```
┌─────────────────────────────────────────┐
│ Showing 23 units                        │
│ Year 8 • Mathematics • Gold Quality     │
│                                         │
│ [Clear filters] (if any active)         │
└─────────────────────────────────────────┘
```

---

## 📱 **MOBILE APPROACH**

**Filters become slide-up sheet:**
```
┌──────────────────┐
│ UNITS       [⚙️] │ ← Tap filter icon
└──────────────────┘
│ [Grid of cards]  │
│                  │
│                  │
└──────────────────┘

Tap [⚙️] → Sheet slides up from bottom:

┌──────────────────┐
│ FILTERS          │
│ ─────────────────│
│ Year             │
│ ○ All            │
│ ○ 7  ○ 8  ○ 9   │
│                  │
│ Subject          │
│ ○ All            │
│ ○ Math ○ Science │
│                  │
│ [Apply Filters]  │
└──────────────────┘
```

---

## 🎨 **DESIGN POLISH - Kehinde Wiley Style**

### **Card Hover Effects:**
```tsx
// Subtle scale + shadow (elegant, not flashy)
<motion.div
  whileHover={{ 
    scale: 1.02,
    boxShadow: '0 20px 40px rgba(27, 127, 90, 0.2)'
  }}
  transition={{ duration: 0.2 }}
>
```

### **Filter Chip Design:**
```tsx
// Active filter: Gold border, filled background
<Chip active className="
  bg-kowhai-100 
  border-2 border-kowhai-500 
  text-pounamu-800
  font-semibold
">
  Year 8
</Chip>

// Inactive: Subtle, clickable
<Chip className="
  bg-white 
  border border-neutral-300
  hover:border-pounamu-500
  transition-colors
">
  Year 9
</Chip>
```

### **Quality Badge (Animated):**
```tsx
<motion.div
  initial={{ rotate: 0 }}
  whileHover={{ rotate: [0, -10, 10, -10, 0] }} // Wiggle!
  transition={{ duration: 0.5 }}
>
  🌟🌟🌟🌟🌟
</motion.div>
```

---

## 🎯 **MY COMPLETE RECOMMENDATION**

### **1. Default View:**
- Show **90+ quality only** (gold standard)
- Organized by **Subject** (collapsible sections)
- Within each subject: **grouped by Year** (sub-sections)
- Beautiful **masonry grid** of cards

### **2. Filtering:**
- **Quick chips** at top (Year, Subject, Quality)
- Click chip → instant filter (client-side)
- Smooth animations (Framer Motion layout animations)
- Clear active filters anytime

### **3. Results Display:**
- **All matching results visible** (no pagination!)
- If too many (>100), group by subject/year (collapsible)
- If perfect number (<50), just show grid
- Count always visible: "Showing 23 units"

### **4. Card Design:**
- Thumbnail image (if exists)
- Title (Kehinde Wiley typography)
- Meta (Year, Subject, Lesson count)
- Quality stars (top-right)
- Cultural badge (if 100%)
- Hover: Preview button appears

### **5. Quality Control:**
- **Default:** 90+ only (621 gold resources)
- **Option:** "Include all quality levels" (checkbox)
- **Why:** Teachers trust us to show them the best first

---

## ✅ **FINAL STRUCTURE**

```
/units
  ├─ Default: All subjects, all years, 90+ quality only
  ├─ Filters: Year chips, Subject chips, Quality toggle
  ├─ Display: Masonry grid (subject → year grouping if >50 results)
  ├─ Animation: Smooth layout shifts (Framer Motion)
  └─ Result: Beautiful, fast, finds what teacher needs in seconds

/lessons (Same exact pattern)
/handouts (Same exact pattern)
```

**Consistent. Professional. Quality-first.**

---

**Approve this and I'll start building the Next.js prototype with this exact UX?**

