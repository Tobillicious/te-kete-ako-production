# 🎯 REAL SITEMAP - Header-Driven Navigation

**Philosophy:** Beautiful homepage that changes regularly. Clean header navigation. Simple.

---

## 🎨 **HOMEPAGE - Gorgeous & Dynamic**

```
┌─────────────────────────────────────────────────────────────┐
│ HEADER (Always visible, clean)                              │
│ ┌─────────────────────────────────────────────────────────┐ │
│ │ TE KETE AKO    [Resources ▾] [Curriculum ▾] [Games]    │ │
│ │                [AI Generator] [Other ▾] [Third Party ▾] │ │
│ │                                            [Login]      │ │
│ └─────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
│                                                             │
│ HERO (Changes weekly/daily - gorgeous!)                    │
│ ┌─────────────────────────────────────────────────────────┐ │
│ │                                                         │ │
│ │     [Featured Resource This Week]                       │ │
│ │     or [Educational News from NZ]                       │ │
│ │     or [New Resource Spotlight]                         │ │
│ │                                                         │ │
│ │     Beautiful image, elegant typography                 │ │
│ │     Changes to keep teachers coming back                │ │
│ │                                                         │ │
│ └─────────────────────────────────────────────────────────┘ │
│                                                             │
│ CONTENT SECTIONS (Clean, not overwhelming)                  │
│ Maybe trending resources, or quality picks, or nothing      │
│ Homepage doesn't have to sell - just be beautiful           │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 🎯 **HEADER NAVIGATION - The Core UX**

### **"Resources" Dropdown:**
```
RESOURCES ▾
├─ Units           →  (with arrow icon between)
├─ Lessons         →  
└─ Handouts        →
```

Hover shows visual connection (arrow/line) between items

### **"Curriculum" Dropdown:**
```
CURRICULUM ▾
├─ NZ Curriculum Overview
├─ Mathematics Curriculum
├─ Science Curriculum  
├─ English Curriculum
├─ Social Sciences Curriculum
├─ Digital Technologies Curriculum
├─ Te Reo Māori Curriculum
├─ Arts Curriculum
└─ Health & PE Curriculum
```

Links to your MoE-aligned curriculum documents (updated as MoE updates)

### **"Games" (Single link - no dropdown)**
```
GAMES → /games
```

Educational games page

### **"AI Generator" (Single link)**
```
AI GENERATOR → /ai-generator
```

The lesson planner tool (GLM-4.6)

### **"Other" Dropdown:**
```
OTHER ▾
├─ Assessments
├─ Professional Development
├─ Worksheets
├─ Activities
└─ Templates
```

Other resource types that don't fit Units/Lessons/Handouts

### **"Third Party" Dropdown:**
```
THIRD PARTY ▾
├─ Education NZ (link)
├─ NZQA (link)
├─ TKI - Te Kete Ipurangi (link)
├─ Kahoot! (link)
├─ Quizlet (link)
└─ [More useful teacher sites]
```

External resources (opens in new tab)

### **"Login" Button**
```
[Login] → Clean button
```

After login: Changes to user avatar dropdown
```
[👤 ▾]
├─ Dashboard
├─ Saved Resources
├─ Account Settings
└─ Logout
```

---

## 📐 **COMPLETE SITE STRUCTURE**

```
tekete.co.nz/

┌─ PUBLIC ─────────────────────────────────────────────┐
│ /                  → Homepage (gorgeous, dynamic)    │
│ /login             → Login form                      │
│ /register          → Signup (simple)                 │
│ /pricing           → Pricing page                    │
└──────────────────────────────────────────────────────┘

┌─ RESOURCES (From header dropdown) ───────────────────┐
│ /units             → Browse all units                │
│ /units/[slug]      → Individual unit page            │
│                                                       │
│ /lessons           → Browse all lessons              │
│ /lessons/[slug]    → Individual lesson page          │
│                                                       │
│ /handouts          → Browse all handouts             │
│ /handouts/[slug]   → Individual handout page         │
└──────────────────────────────────────────────────────┘

┌─ CURRICULUM (From header dropdown) ──────────────────┐
│ /curriculum                → Overview                │
│ /curriculum/mathematics    → Math curriculum doc     │
│ /curriculum/science        → Science curriculum doc  │
│ /curriculum/english        → English curriculum doc  │
│ [... all curriculum areas]                           │
└──────────────────────────────────────────────────────┘

┌─ SINGLE PAGES (From header) ─────────────────────────┐
│ /games             → Educational games page          │
│ /ai-generator      → AI lesson planner tool          │
└──────────────────────────────────────────────────────┘

┌─ OTHER (From header dropdown) ───────────────────────┐
│ /assessments       → Assessment resources            │
│ /professional-development → PD resources             │
│ /worksheets        → Worksheet library               │
│ /activities        → Activity resources              │
│ /templates         → Template resources              │
└──────────────────────────────────────────────────────┘

┌─ USER (After login - from avatar dropdown) ──────────┐
│ /dashboard         → Personal dashboard              │
│ /saved             → Saved resources (simple list)   │
│ /account           → Settings + subscription         │
└──────────────────────────────────────────────────────┘
```

---

## 🎨 **HEADER COMPONENT - Detailed Design**

```tsx
<Header>
  <Logo>TE KETE AKO</Logo>
  
  <Nav>
    <DropdownMenu trigger="Resources ▾">
      <DropdownMenuItem>
        <Icon>📦</Icon>
        <Label>Units</Label>
        <Arrow>→</Arrow> {/* Visual connector! */}
      </DropdownMenuItem>
      <DropdownMenuItem>
        <Icon>📝</Icon>
        <Label>Lessons</Label>
        <Arrow>→</Arrow>
      </DropdownMenuItem>
      <DropdownMenuItem>
        <Icon>📄</Icon>
        <Label>Handouts</Label>
        <Arrow>→</Arrow>
      </DropdownMenuItem>
    </DropdownMenu>
    
    <DropdownMenu trigger="Curriculum ▾">
      <DropdownMenuItem>NZ Curriculum Overview</DropdownMenuItem>
      <DropdownMenuItem>Mathematics</DropdownMenuItem>
      <DropdownMenuItem>Science</DropdownMenuItem>
      {/* ... all subjects */}
    </DropdownMenu>
    
    <NavLink>Games</NavLink>
    <NavLink>AI Generator</NavLink>
    
    <DropdownMenu trigger="Other ▾">
      <DropdownMenuItem>Assessments</DropdownMenuItem>
      <DropdownMenuItem>Professional Development</DropdownMenuItem>
      <DropdownMenuItem>Worksheets</DropdownMenuItem>
      <DropdownMenuItem>Activities</DropdownMenuItem>
    </DropdownMenu>
    
    <DropdownMenu trigger="Third Party ▾">
      <DropdownMenuItem href="https://www.education.govt.nz" external>
        Education NZ ↗
      </DropdownMenuItem>
      <DropdownMenuItem href="https://www.nzqa.govt.nz" external>
        NZQA ↗
      </DropdownMenuItem>
      {/* ... more external links */}
    </DropdownMenu>
  </Nav>
  
  <Actions>
    {!user ? (
      <Button>Login</Button>
    ) : (
      <UserDropdown>
        <Avatar src={user.avatar} />
        <DropdownMenu>
          <DropdownMenuItem>Dashboard</DropdownMenuItem>
          <DropdownMenuItem>Saved Resources</DropdownMenuItem>
          <DropdownMenuItem>Account Settings</DropdownMenuItem>
          <DropdownMenuSeparator />
          <DropdownMenuItem>Logout</DropdownMenuItem>
        </DropdownMenu>
      </UserDropdown>
    )}
  </Actions>
</Header>
```

---

## 📱 **MOBILE NAVIGATION**

**Header collapses to:**
```
┌──────────────────────────────┐
│ ☰  TE KETE AKO      [Login] │
└──────────────────────────────┘
```

Hamburger opens drawer with same navigation structure

---

## 🎯 **HOMEPAGE DYNAMIC CONTENT**

### **What Changes Regularly:**

**Educational News Section:**
```tsx
<NewsSection>
  <NewsCard>
    <Badge>New from MoE</Badge>
    <Title>Updated Science Curriculum Released</Title>
    <Date>Oct 25, 2025</Date>
    <Link>Read our alignment guide →</Link>
  </NewsCard>
</NewsSection>
```

**Featured Resource (Changes Weekly):**
```tsx
<FeaturedHero>
  <Badge>Featured This Week</Badge>
  <Title>Y9 Digital Kaitiakitanga Unit</Title>
  <Description>18 lessons, 100% cultural integration</Description>
  <Image src="/featured/digital-kaitiakitanga.jpg" />
  <Action>Explore Unit →</Action>
</FeaturedHero>
```

**Trending (Changes Daily based on usage):**
```tsx
<TrendingSection>
  <Title>Trending This Week</Title>
  <ResourceGrid>
    {/* Top 5 most-viewed resources this week */}
    {trending.map(resource => <ResourceCard {...resource} />)}
  </ResourceGrid>
</TrendingSection>
```

---

## 🎯 **BROWSE PAGE - The Workhorse**

**Simple, Fast, Beautiful:**

```
┌─────────────────────────────────────────────┐
│ 🔍 [Search resources...]        [Cmd+K]    │
└─────────────────────────────────────────────┘
│ FILTERS (Horizontal, clean)                 │
│ [All Years ▾] [All Subjects ▾] [All Types ▾]│
└─────────────────────────────────────────────┘
│                                             │
│ MASONRY GRID (Beautiful, responsive)        │
│ ┌─────┐ ┌─────┐ ┌───────┐                 │
│ │     │ │     │ │       │                 │
│ │ Y8  │ │ Y9  │ │  Y7   │                 │
│ │Geom │ │Stats│ │ Algeb │                 │
│ │🌟🌟│ │🌟🌟│ │  🌟🌟 │                 │
│ │     │ │     │ │       │                 │
│ └─────┘ └─────┘ └───────┘                 │
│                                             │
│ [Infinite scroll - loads more]              │
│                                             │
└─────────────────────────────────────────────┘
```

**That's it.** No complexity. Just works.

---

## ✅ **IS THIS IT?**

**The COMPLETE site:**
1. **Homepage** - Gorgeous, changes weekly, minimal text
2. **Header Navigation** - Clean dropdowns (Resources, Curriculum, etc.)
3. **Browse Pages** - Beautiful grids with filters
4. **Resource Pages** - Just the content, print button, save button
5. **Dashboard** - Simple overview
6. **Saved** - List of saved resources
7. **Account** - Settings + billing

**TOTAL: ~15 pages.** Everything else is just content variations.

**Is this the right vision?**
