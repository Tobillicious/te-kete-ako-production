# ⚡ LIGHTHOUSE PERFORMANCE AUDIT PROTOCOL
**Date:** October 19, 2025  
**Purpose:** Performance benchmarking for Te Kete Ako  
**Tool:** Google Lighthouse (Chrome DevTools)

---

## 🎯 **PERFORMANCE TARGETS:**

**Lighthouse Scores (0-100):**
- Performance: **95+** ⚡
- Accessibility: **95+** ♿
- Best Practices: **95+** ✅
- SEO: **95+** 🔍

**Core Web Vitals:**
- LCP (Largest Contentful Paint): **<2.5s** 🎨
- FID (First Input Delay): **<100ms** 🖱️
- CLS (Cumulative Layout Shift): **<0.1** 📐

**Additional Targets:**
- First Contentful Paint: **<1.5s**
- Time to Interactive: **<3.5s**
- Speed Index: **<3.0s**
- Total Blocking Time: **<300ms**

---

## 📋 **10 PAGES TO TEST:**

### **High-Traffic Pages:**
1. `/index.html` (Homepage)
2. `/lessons.html` (Now GraphRAG-powered!)
3. `/mathematics-hub.html` (Subject hub)
4. `/teacher-dashboard-unified.html` (Teacher entry point)
5. `/units/y8-digital-kaitiakitanga/index.html` (Gold standard unit)

### **Representative Content:**
6. `/units/y8-digital-kaitiakitanga/lessons/lesson-1-what-is-our-digital-whenua.html` (Typical lesson)
7. `/handouts.html` (Handouts listing)
8. `/login.html` (Authentication)
9. `/beta-feedback.html` (Forms)
10. `/help.html` (Help system)

---

## 🔬 **HOW TO RUN LIGHTHOUSE:**

### **Method 1: Chrome DevTools (Easiest)**
1. Open page in Chrome
2. Right-click → "Inspect" (or F12)
3. Click "Lighthouse" tab (top menu)
4. Select:
   - ✅ Performance
   - ✅ Accessibility
   - ✅ Best Practices
   - ✅ SEO
5. Device: **Mobile** (test mobile performance!)
6. Click "Analyze page load"
7. Wait 30-60 seconds for report
8. Review scores and recommendations

### **Method 2: PageSpeed Insights (Online)**
1. Go to: https://pagespeed.web.dev/
2. Enter URL: https://tekete.netlify.app
3. Click "Analyze"
4. Get mobile + desktop scores
5. Review Core Web Vitals

### **Method 3: Lighthouse CLI (Advanced)**
```bash
npm install -g lighthouse
lighthouse https://tekete.netlify.app --output html --output-path ./lighthouse-report.html
```

---

## 📊 **AUDIT CHECKLIST PER PAGE:**

For each of the 10 pages, record:

**Scores:**
- [ ] Performance: ___/100
- [ ] Accessibility: ___/100
- [ ] Best Practices: ___/100
- [ ] SEO: ___/100

**Core Web Vitals:**
- [ ] LCP: ___ seconds
- [ ] FID: ___ milliseconds  
- [ ] CLS: ___ (score)

**Load Times:**
- [ ] First Contentful Paint: ___ seconds
- [ ] Time to Interactive: ___ seconds
- [ ] Speed Index: ___ seconds

**Opportunities (Top 3):**
1. ___________________________
2. ___________________________
3. ___________________________

**Diagnostics (Top 3 issues):**
1. ___________________________
2. ___________________________
3. ___________________________

---

## 🔧 **COMMON PERFORMANCE FIXES:**

### **Issue: Slow Image Loading**
**Lighthouse says:** "Properly size images"

**Fix:**
```html
<!-- Use responsive images -->
<img src="image.jpg" 
     srcset="image-small.jpg 400w, image-medium.jpg 800w, image-large.jpg 1200w"
     sizes="(max-width: 768px) 100vw, 50vw"
     loading="lazy"
     alt="Description">
```

---

### **Issue: Render-Blocking Resources**
**Lighthouse says:** "Eliminate render-blocking resources"

**Fix:**
```html
<!-- Defer non-critical CSS -->
<link rel="preload" href="/css/non-critical.css" as="style" onload="this.onload=null;this.rel='stylesheet'">

<!-- Defer JavaScript -->
<script src="/js/non-critical.js" defer></script>
```

---

### **Issue: Large CSS Files**
**Lighthouse says:** "Reduce unused CSS"

**Current State:**
- te-kete-ultimate-beauty-system.css: 1,095 lines
- Tailwind CDN: ~200KB

**Fix:**
1. Use PurgeCSS to remove unused Tailwind classes
2. Split CSS into critical (inline) + non-critical (defer)
3. Use CSS minification

---

### **Issue: Cumulative Layout Shift (CLS)**
**Lighthouse says:** "Avoid large layout shifts"

**Fix:**
```html
<!-- Reserve space for images -->
<img src="hero.jpg" width="1200" height="600" alt="Hero">

<!-- Reserve space for dynamic content -->
<div style="min-height: 400px;" id="dynamic-lessons-container">
  <!-- Content loads here -->
</div>
```

---

### **Issue: Slow Server Response**
**Lighthouse says:** "Reduce server response time"

**Fix:**
- Enable Netlify CDN caching
- Add cache headers
- Optimize Supabase queries
- Use edge functions for dynamic content

---

## 📈 **EXPECTED SCORES (Prediction):**

### **Homepage (`/index.html`):**
**Predicted:**
- Performance: 85-90 (Ultimate Beauty CSS is large)
- Accessibility: 95-100 (well-structured, ARIA labels)
- Best Practices: 95-100 (HTTPS, no console errors)
- SEO: 95-100 (good meta tags, semantic HTML)

**Potential Issues:**
- CSS file size (Ultimate Beauty + Tailwind CDN)
- Multiple component fetches (nav, footer, mobile, FAB)
- Onboarding tour JavaScript

---

### **Lessons.html (`/lessons.html`):**
**Predicted:**
- Performance: 70-80 (GraphRAG query adds load time)
- Accessibility: 95-100
- Best Practices: 90-95 (dynamic content loading)
- SEO: 85-90 (JavaScript-rendered content)

**Potential Issues:**
- Supabase query time (500+ lessons)
- Rendering 500+ lesson cards (DOM size)
- Filter logic JavaScript

---

### **Lesson Page (Individual lesson):**
**Predicted:**
- Performance: 90-95 (simple HTML + CSS)
- Accessibility: 95-100
- Best Practices: 95-100
- SEO: 95-100

**Potential Issues:**
- Component injection (fetch calls)
- Large lesson content
- Embedded media

---

## 🎯 **IF SCORES ARE LOW (<90):**

### **Quick Wins:**
1. **Minify CSS/JS** (reduce file sizes 30-50%)
2. **Optimize images** (use WebP format, compress)
3. **Enable caching** (Netlify cache headers)
4. **Defer non-critical JS** (analytics, animations)
5. **Inline critical CSS** (above-the-fold styles)

### **Medium Effort:**
6. **Code splitting** (load only what's needed)
7. **Lazy load images** (loading="lazy")
8. **Preconnect to external domains** (fonts, CDNs)
9. **Reduce GraphRAG query size** (paginate lessons?)
10. **Service worker caching** (PWA optimization)

### **Long-term:**
11. **Move Tailwind to build process** (purge unused CSS)
12. **Use image CDN** (CloudFlare, ImageKit)
13. **Implement HTTP/2** (Netlify supports this)
14. **Server-side rendering** (for lessons.html)
15. **GraphQL instead of REST** (reduce payload size)

---

## 🚀 **RECOMMENDATION:**

**RUN LIGHTHOUSE DURING BETA!**

**Why:**
- Real user feedback > synthetic tests
- Can test on beta teachers' actual devices
- Monitor real-world performance
- PostHog analytics will show actual load times

**Then:**
- Fix issues users actually experience
- Prioritize based on usage patterns
- Optimize most-visited pages first

**Perfect is the enemy of launched!** 🎯

---

*Created by: Kaitiaki Tūhono*  
*Status: Protocol ready for performance testing*  
*Recommendation: Launch beta, monitor real performance, iterate!*

